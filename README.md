# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-07-08.md)

*最后自动更新时间: 2026-07-08 18:48:00*
## 1. Chatto 现已开源

**原文标题**: Chatto is now Open Source

**原文链接**: [https://www.hmans.dev/blog/chatto-is-open-source](https://www.hmans.dev/blog/chatto-is-open-source)

在名为《Chatto 现已开源》的博文中，开发者 Hendrik Mans 宣布他的聊天应用项目 Chatto 已从潜在的商业产品转型为采用 MIT 许可证的开源项目。

Mans 最初将 Chatto 开发为 Discord 和 Slack 等平台的现代、轻量级替代方案。在意识到自己不再希望将其作为商业 SaaS 业务运营后，他决定公开代码，以确保其对社区的效用，并允许他人托管自己的私人通信中心。

**Chatto 的主要特性和细节包括：**

*   **用途：** 专为小型社区、朋友圈和家庭设计，旨在提供私密、无干扰的对话环境。
*   **核心功能：** 该平台支持有序频道、私信、富文本/Markdown 支持、文件上传（通过 AWS S3）以及表情符号回应。
*   **技术栈：** 该应用基于 **React**、**TypeScript** 和 **Tailwind CSS** 构建。它利用 **Pusher** 实现实时消息传递，并拥有简洁的响应式界面。
*   **自托管：** 通过开源该项目，Mans 使用户能够自托管该应用，从而完全掌控自己的数据和基础设施。

这一举措标志着从利润驱动模式向社区导向模式的转变。Mans 鼓励开发者在 GitHub 上探索该代码库，无论是将其作为自己项目的基石，还是仅仅为了学习其在实时 Web 技术方面的实现。

---

## 2. Mistral 的 Robostral Navigate：一款最先进的机器人导航模型

**原文标题**: Mistral's Robostral Navigate: a state of the art robotics navigation model

**原文链接**: [https://mistral.ai/news/robostral-navigate/](https://mistral.ai/news/robostral-navigate/)

Mistral AI 推出了 **Robostral Navigate**，这是一款专为自主机器人导航设计的 8B 参数模型。该模型的一大特色是仅使用**单目 RGB 摄像头**即可实现最先进的性能，无需昂贵的激光雷达 (LiDAR) 或深度传感器。

在 R2R-CE（连续环境中的房到房）基准测试中，该模型在未知环境下的**成功率达到 76.6%**。这一表现比之前的多传感器系统高出 4.5 个百分点，比最出色的单摄像头方案高出 9.7 个百分点。该模型能够理解自然语言指令，并通过“指向”（预测目标图像坐标）或在目标不可见时使用局部位移来进行导航。

**核心技术亮点：**
*   **自主研发**：该模型完全从零开始构建，而非依赖现有的开源视觉语言模型 (VLM)，重点关注物体定位等接地 (grounding) 能力。
*   **基于模拟的训练**：Mistral 在 6,000 个模拟场景中生成了 40 万条轨迹，构建了稳健的数据集。
*   **高效性**：通过使用“前缀缓存”策略，团队将训练 token 数量减少了 **22 倍**，将数月的训练时间缩短至数天。
*   **强化学习**：在监督训练之后，团队应用了名为 CISPO 的在线强化学习算法，通过让模型在试错中学习，使成功率进一步提升了 3.2%。

Robostral Navigate 与硬件无关，可适配各种尺寸的轮式、足式及飞行机器人。Mistral 将其视为迈向统一具身智能 (Embodied AI) 的基础性一步，在物流、制造和酒店服务等领域具有即时应用价值。

---

## 3. Grok 4.5

**原文标题**: Grok 4.5

**原文链接**: [https://x.ai/news/grok-4-5](https://x.ai/news/grok-4-5)

On July 8, 2026, SpaceXAI announced the launch of **Grok 4.5**, its most advanced model to date, specifically optimized for coding, agentic tasks, and professional knowledge work. Trained on NVIDIA GB300 GPUs using large-scale reinforcement learning, the model focuses on "per-token intelligence" to handle complex, multi-step engineering challenges.

**Key Highlights:**
*   **Performance:** Grok 4.5 excels in STEM and software engineering benchmarks, rivaling or exceeding models like GPT 5.5 and Opus 4.8. It notably ranks #1 on Harvey's Legal Agent Benchmark and shows high resolve rates on SWE Bench Pro.
*   **Speed and Efficiency:** The model operates at "fast-model" speeds of 80 tokens per second. SpaceXAI emphasizes its "token efficiency," claiming it can resolve tasks using roughly 4.2x fewer output tokens than competitors, significantly reducing latency and operational costs.
*   **Office Integration:** Beyond coding, Grok 4.5 is integrated into "Grok Build" for office productivity. It can generate complex Excel models with web research, design native PowerPoint diagrams, and draft professional prose in Word.
*   **Coding Prowess:** The model supports end-to-end application development—from Rust and C++ tasks to Three.js simulations—often requiring only a single prompt to reach production-ready results.

**Availability and Pricing:**
Grok 4.5 is priced competitively at **$2 per million input tokens** and **$6 per million output tokens**. It is available immediately via the SpaceXAI console, Grok Build, and the Cursor code editor. While currently available in most regions, availability in the EU is expected to follow in mid-July 2026.

---

## 4. GPT‑Live

**原文标题**: GPT‑Live

**原文链接**: [https://openai.com/index/introducing-gpt-live/](https://openai.com/index/introducing-gpt-live/)

生成摘要时出错

---

## 5. SWE-1.7 智能水平接近 GPT 5.5 与 Opus

**原文标题**: SWE-1.7 Reach Near GPT 5.5 and Opus Intelligence

**原文链接**: [https://cognition.com/blog/swe-1-7](https://cognition.com/blog/swe-1-7)

生成摘要时出错

---

## 6. Decoding the obfuscated bash script on a Uniqlo t-shirt

**原文标题**: Decoding the obfuscated bash script on a Uniqlo t-shirt

**原文链接**: [https://tris.sherliker.net/blog/obfuscated-self-evaluating-bash-script-by-cdn-akamai-being-supplied-to-consumers-via-retail-stores/](https://tris.sherliker.net/blog/obfuscated-self-evaluating-bash-script-by-cdn-akamai-being-supplied-to-consumers-via-retail-stores/)

生成摘要时出错

---

## 7. Show HN: Microsoft releases Flint, a visualization language for AI agents

**原文标题**: Show HN: Microsoft releases Flint, a visualization language for AI agents

**原文链接**: [https://microsoft.github.io/flint-chart/#/](https://microsoft.github.io/flint-chart/#/)

生成摘要时出错

---

## 8. What Do We Know About the Microplastics Inside Us?

**原文标题**: What Do We Know About the Microplastics Inside Us?

**原文链接**: [https://e360.yale.edu/features/cassandra-rauert-interview](https://e360.yale.edu/features/cassandra-rauert-interview)

生成摘要时出错

---

## 9. Cloudflare Meerkat - Globally distributed consensus

**原文标题**: Cloudflare Meerkat - Globally distributed consensus

**原文链接**: [https://blog.cloudflare.com/meerkat-introduction/](https://blog.cloudflare.com/meerkat-introduction/)

生成摘要时出错

---

## 10. EU now one step away from reviving private message scanning rules

**原文标题**: EU now one step away from reviving private message scanning rules

**原文链接**: [https://cyberinsider.com/eu-now-one-step-away-from-reviving-private-message-scanning-rules/](https://cyberinsider.com/eu-now-one-step-away-from-reviving-private-message-scanning-rules/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 2 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 3 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 4 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 5 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 6 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 7 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 8 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 9 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 10 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 11 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 12 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 13 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 14 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 15 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 16 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 17 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 18 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 19 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 20 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 21 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 22 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 23 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 24 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 25 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 26 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 27 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 28 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 29 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 30 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 31 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 32 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 33 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 34 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 35 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 36 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 37 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 38 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 39 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 40 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 41 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 42 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 43 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 44 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 45 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 46 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 47 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 48 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 49 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 50 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 51 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 52 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 53 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 54 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 55 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 56 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 57 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 58 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 59 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 60 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 61 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 62 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 63 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 64 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 65 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 66 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 67 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 68 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 69 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 70 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 71 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 72 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 73 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 74 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 75 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 76 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 77 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 78 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 79 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 80 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 81 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 82 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 83 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 84 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 85 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 86 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 87 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 88 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 89 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 90 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 91 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 92 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 93 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 94 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 95 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 96 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 97 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 98 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 99 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 100 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 101 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 102 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 103 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 104 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 105 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 106 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 107 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 108 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 109 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 110 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 111 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 112 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 113 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 114 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 115 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 116 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 117 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 118 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 119 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 120 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 121 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 122 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 123 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 124 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 125 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 126 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 127 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 128 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 129 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 130 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 131 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 132 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 133 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 134 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 135 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 136 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 137 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 138 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 139 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 140 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 141 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 142 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 143 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 144 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 145 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 146 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 147 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 148 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 149 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 150 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 151 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 152 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 153 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 154 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 155 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 156 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 157 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 158 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 159 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 160 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 161 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 162 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 163 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 164 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 165 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 166 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 167 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 168 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 169 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 170 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 171 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 172 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 173 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 174 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 175 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 176 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 177 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 178 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 179 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 180 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 181 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 182 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 183 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 184 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 185 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 186 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 187 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 188 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 189 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 190 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 191 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 192 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 193 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 194 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 195 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 196 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 197 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 198 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 199 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 200 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 201 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 202 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 203 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 204 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 205 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 206 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 207 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 208 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 209 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 210 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 211 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 212 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 213 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 214 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 215 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 216 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 217 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 218 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 219 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 220 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 221 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 222 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 223 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 224 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 225 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 226 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 227 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 228 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 229 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 230 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 231 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 232 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 233 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 234 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 235 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 236 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 237 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 238 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 239 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 240 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 241 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 242 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 243 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 244 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 245 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 246 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 247 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 248 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 249 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 250 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 251 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 252 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 253 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 254 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 255 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 256 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 257 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 258 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 259 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 260 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 261 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 262 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 263 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 264 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 265 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 266 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 267 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 268 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 269 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 270 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 271 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 272 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 273 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 274 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 275 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 276 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 277 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 278 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 279 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 280 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 281 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 282 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 283 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 284 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 285 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 286 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 287 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 288 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 289 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 290 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 291 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 292 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 293 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 294 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 295 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 296 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 297 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 298 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 299 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 300 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 301 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 302 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 303 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 304 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 305 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 306 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 307 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 308 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 309 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 310 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 311 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 312 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 313 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 314 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 315 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 316 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 317 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 318 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 319 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 320 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 321 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 322 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 323 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 324 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 325 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 326 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 327 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 328 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 329 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 330 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 331 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 332 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 333 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 334 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 335 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 336 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 337 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 338 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 339 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 340 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 341 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 342 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 343 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 344 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 345 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 346 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 347 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 348 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 349 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 350 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 351 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 352 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 353 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 354 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 355 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 356 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 357 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 358 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 359 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 360 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 361 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 362 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 363 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 364 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 365 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 366 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 367 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 368 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 369 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 370 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 371 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 372 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 373 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 374 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 375 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 376 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 377 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 378 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 379 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 380 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 381 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 382 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 383 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 384 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 385 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 386 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 387 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 388 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 389 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 390 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 391 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 392 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 393 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 394 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 395 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 396 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 397 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 398 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 399 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 400 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 401 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 402 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 403 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 404 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 405 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 406 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 407 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 408 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 409 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 410 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 411 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 412 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 413 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 414 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 415 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 416 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 417 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 418 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 419 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 420 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 421 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 422 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 423 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 424 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 425 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 426 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 427 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 428 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 429 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 430 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 431 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 432 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 433 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 434 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 435 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 436 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 437 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 438 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 439 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 440 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 441 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 442 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 443 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 444 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 445 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 446 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 447 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 448 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 449 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 450 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 451 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 452 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 453 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 454 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 455 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 456 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 457 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 458 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 459 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 460 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 461 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 462 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 463 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 464 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 465 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 466 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 467 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 468 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 469 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 470 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 471 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 472 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 473 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 474 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 475 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
