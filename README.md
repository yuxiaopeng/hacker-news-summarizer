# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-07-14.md)

*最后自动更新时间: 2026-07-14 18:34:04*
## 1. Linux 输入延迟测试：X11 vs. Wayland、VRR 和 DXVK

**原文标题**: Measuring Input Latency on Linux: X11 vs. Wayland, VRR, and DXVK

**原文链接**: [https://marco-nett.de/blog/measuring-input-latency-on-linux-x11-vs-wayland-vrr-dxvk/](https://marco-nett.de/blog/measuring-input-latency-on-linux-x11-vs-wayland-vrr-dxvk/)

本文详细介绍了一项针对 Linux 游戏性能的技术调查。作者使用自制的硬件延迟测量仪，旨在摆脱“安慰剂”式的优化，精确测量端到端系统延迟。在 500Hz 的高端硬件环境下，作者对比了 X11 与 Wayland 的表现、可变刷新率（VRR）的影响，以及 `dxvk-low-latency` 分支的实际效果。

**主要发现：**

*   **XWayland 是最大元凶：** 最显著的发现是，通过 XWayland 运行游戏会增加约 **3.13ms** 的延迟。仅此一项的影响就超过了几乎所有其他优化手段的总和。
*   **X11 对比原生 Wayland：** 虽然 X11 在技术上稍快，但领先幅度微乎其微（0.14ms 至 0.22ms）。原生 Wayland 表现出极强的竞争力，打破了其天生不适合竞技游戏的传言。
*   **VRR 效果显著：** 开启 VRR（G-Sync/FreeSync）能稳定降低 **0.26ms 至 0.45ms** 的延迟。更重要的是，它通过收窄帧交付时间的分布（减少抖动）显著提升了稳定性。
*   **DXVK Low-Latency 的优势：** `dxvk-low-latency` 分支带来了持续的性能提升。虽然在限帧场景下收益较小，但在不限帧的情况下，它通过防止渲染队列积压并确保 GPU 不至于完全饱和，使延迟降低了 **0.84ms**。

**结论：**

若要在 Linux 上获得最低延迟，作者建议**务必避免使用 XWayland**，应选择原生 Wayland 协议或 X11。虽然在理想条件下，叠加所有优化手段（X11、VRR 及 DXVK 分支）的总收益仅约为 **0.72ms**，但这些设置通过提供更稳定的帧生成时间和减少实际游戏中的延迟波动，显著改善了操作的“手感”。

---

## 2. 高塔仍在攀升

**原文标题**: The Tower Keeps Rising

**原文链接**: [https://lucumr.pocoo.org/2026/7/13/the-tower-keeps-rising/](https://lucumr.pocoo.org/2026/7/13/the-tower-keeps-rising/)

In "The Tower Keeps Rising," Armin Ronacher explores the impact of AI agents on software development through the lens of the Tower of Babel. While the biblical story suggests that the loss of a shared language halts progress, Ronacher argues that AI-assisted programming creates a different, more disorienting outcome: construction continues even after collective human understanding has collapsed.

The core of Ronacher’s argument is that large-scale software projects rely less on individual coding speed and more on a "shared language"—a common mental model of system boundaries, invariants, and architectural goals. Historically, this shared understanding was maintained by the "friction" of human collaboration. Processes like code reviews and technical debates forced developers to synchronize their knowledge and agree on how a system should function.

AI agents remove this friction. They allow developers to execute complex changes across a codebase without needing to consult others or fully grasp the underlying system logic. While this increases individual productivity, it erodes the shared architectural language that allows humans to reason about the project together. 

The result is "vibecoded" software: a codebase where changes are landed continuously by "tireless translators," but the internal coherence disappears. Unlike the ruins of Babel, these digital towers do not fall; they keep rising. Ronacher warns that the lack of an immediate failure makes this trend dangerous, as it masks the fact that the humans involved no longer truly understand the structure they are building. The system continues to grow, but the architectural language required to manage it is lost.

---

## 3. Your 'app' could have been a webpage (so I fixed it for you)

**原文标题**: Your 'app' could have been a webpage (so I fixed it for you)

**原文链接**: [https://danq.me/2026/07/09/your-app-could-have-been-a-webpage/](https://danq.me/2026/07/09/your-app-could-have-been-a-webpage/)

生成摘要时出错

---

## 4. S&P downgrades Oracle to BBB – only one notch above junk level

**原文标题**: S&P downgrades Oracle to BBB – only one notch above junk level

**原文链接**: [https://www.heise.de/en/news/S-P-downgrades-Oracle-to-BBB-only-one-notch-above-junk-level-11363472.html](https://www.heise.de/en/news/S-P-downgrades-Oracle-to-BBB-only-one-notch-above-junk-level-11363472.html)

生成摘要时出错

---

## 5. How to stop Claude from saying load-bearing

**原文标题**: How to stop Claude from saying load-bearing

**原文链接**: [https://jola.dev/posts/how-to-stop-claude-from-saying-load-bearing](https://jola.dev/posts/how-to-stop-claude-from-saying-load-bearing)

生成摘要时出错

---

## 6. Show HN: Opening lines of famous literary works

**原文标题**: Show HN: Opening lines of famous literary works

**原文链接**: [https://www.verbaprima.com/](https://www.verbaprima.com/)

生成摘要时出错

---

## 7. Launch HN: Agnost AI (YC S26) – Extract user feedback from agent conversations

**原文标题**: Launch HN: Agnost AI (YC S26) – Extract user feedback from agent conversations

**原文链接**: [https://agnost.ai](https://agnost.ai)

生成摘要时出错

---

## 8. Kontigo (YC S24) Is Hiring (Head of Security)

**原文标题**: Kontigo (YC S24) Is Hiring (Head of Security)

**原文链接**: [https://www.ycombinator.com/companies/kontigo/jobs/uNttrlv-head-of-security](https://www.ycombinator.com/companies/kontigo/jobs/uNttrlv-head-of-security)

生成摘要时出错

---

## 9. Are we offloading too much of our thinking to AI?

**原文标题**: Are we offloading too much of our thinking to AI?

**原文链接**: [https://www.artfish.ai/p/offloading-thinking-to-ai](https://www.artfish.ai/p/offloading-thinking-to-ai)

生成摘要时出错

---

## 10. The zero-cost fallacy: open-source software in the agentic era

**原文标题**: The zero-cost fallacy: open-source software in the agentic era

**原文链接**: [https://www.thoughtworks.com/insights/blog/open-source/zero-cost-fallacy-open-source-agentic-era](https://www.thoughtworks.com/insights/blog/open-source/zero-cost-fallacy-open-source-agentic-era)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 2 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 3 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 4 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 5 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 6 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 7 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 8 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 9 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 10 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 11 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 12 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 13 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 14 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 15 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 16 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 17 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 18 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 19 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 20 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 21 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 22 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 23 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 24 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 25 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 26 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 27 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 28 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 29 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 30 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 31 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 32 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 33 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 34 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 35 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 36 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 37 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 38 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 39 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 40 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 41 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 42 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 43 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 44 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 45 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 46 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 47 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 48 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 49 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 50 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 51 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 52 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 53 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 54 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 55 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 56 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 57 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 58 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 59 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 60 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 61 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 62 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 63 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 64 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 65 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 66 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 67 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 68 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 69 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 70 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 71 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 72 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 73 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 74 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 75 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 76 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 77 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 78 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 79 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 80 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 81 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 82 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 83 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 84 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 85 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 86 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 87 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 88 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 89 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 90 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 91 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 92 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 93 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 94 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 95 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 96 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 97 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 98 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 99 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 100 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 101 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 102 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 103 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 104 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 105 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 106 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 107 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 108 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 109 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 110 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 111 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 112 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 113 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 114 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 115 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 116 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 117 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 118 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 119 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 120 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 121 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 122 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 123 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 124 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 125 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 126 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 127 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 128 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 129 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 130 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 131 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 132 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 133 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 134 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 135 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 136 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 137 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 138 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 139 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 140 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 141 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 142 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 143 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 144 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 145 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 146 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 147 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 148 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 149 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 150 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 151 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 152 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 153 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 154 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 155 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 156 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 157 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 158 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 159 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 160 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 161 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 162 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 163 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 164 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 165 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 166 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 167 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 168 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 169 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 170 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 171 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 172 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 173 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 174 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 175 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 176 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 177 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 178 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 179 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 180 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 181 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 182 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 183 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 184 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 185 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 186 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 187 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 188 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 189 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 190 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 191 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 192 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 193 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 194 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 195 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 196 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 197 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 198 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 199 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 200 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 201 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 202 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 203 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 204 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 205 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 206 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 207 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 208 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 209 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 210 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 211 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 212 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 213 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 214 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 215 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 216 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 217 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 218 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 219 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 220 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 221 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 222 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 223 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 224 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 225 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 226 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 227 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 228 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 229 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 230 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 231 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 232 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 233 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 234 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 235 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 236 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 237 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 238 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 239 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 240 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 241 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 242 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 243 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 244 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 245 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 246 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 247 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 248 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 249 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 250 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 251 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 252 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 253 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 254 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 255 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 256 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 257 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 258 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 259 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 260 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 261 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 262 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 263 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 264 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 265 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 266 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 267 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 268 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 269 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 270 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 271 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 272 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 273 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 274 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 275 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 276 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 277 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 278 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 279 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 280 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 281 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 282 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 283 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 284 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 285 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 286 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 287 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 288 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 289 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 290 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 291 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 292 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 293 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 294 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 295 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 296 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 297 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 298 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 299 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 300 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 301 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 302 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 303 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 304 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 305 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 306 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 307 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 308 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 309 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 310 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 311 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 312 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 313 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 314 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 315 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 316 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 317 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 318 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 319 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 320 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 321 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 322 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 323 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 324 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 325 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 326 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 327 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 328 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 329 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 330 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 331 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 332 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 333 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 334 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 335 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 336 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 337 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 338 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 339 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 340 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 341 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 342 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 343 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 344 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 345 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 346 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 347 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 348 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 349 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 350 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 351 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 352 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 353 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 354 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 355 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 356 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 357 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 358 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 359 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 360 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 361 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 362 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 363 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 364 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 365 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 366 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 367 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 368 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 369 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 370 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 371 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 372 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 373 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 374 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 375 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 376 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 377 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 378 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 379 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 380 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 381 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 382 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 383 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 384 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 385 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 386 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 387 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 388 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 389 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 390 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 391 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 392 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 393 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 394 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 395 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 396 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 397 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 398 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 399 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 400 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 401 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 402 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 403 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 404 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 405 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 406 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 407 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 408 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 409 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 410 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 411 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 412 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 413 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 414 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 415 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 416 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 417 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 418 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 419 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 420 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 421 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 422 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 423 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 424 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 425 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 426 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 427 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 428 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 429 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 430 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 431 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 432 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 433 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 434 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 435 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 436 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 437 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 438 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 439 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 440 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 441 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 442 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 443 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 444 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 445 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 446 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 447 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 448 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 449 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 450 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 451 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 452 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 453 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 454 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 455 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 456 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 457 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 458 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 459 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 460 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 461 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 462 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 463 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 464 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 465 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 466 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 467 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 468 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 469 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 470 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 471 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 472 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 473 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 474 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 475 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 476 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 477 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 478 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 479 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 480 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 481 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
