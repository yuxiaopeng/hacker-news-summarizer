# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-11-22.md)

*最后自动更新时间: 2026-11-22 22:43:33*
## 1. 《GTA 6》鸟类：罪恶都市与莱奥尼达州野生动物图鉴

**原文标题**: The Birds of GTA 6: A Field Guide to Vice City and Leonida's Wildlife

**原文链接**: [https://www.audubon.org/magazine/birds-of-gta-6-field-guide-vice-city-wildlife](https://www.audubon.org/magazine/birds-of-gta-6-field-guide-vice-city-wildlife)

根据提供的标题和内容，以下是简明摘要：

所提供的文本在标题和正文内容之间存在差异。虽然标题**《GTA 6 中的鸟类：罪恶都市与雷欧尼达野生动物野外指南》**暗示该文将探讨即将推出的电子游戏《侠盗猎车手 6》(Grand Theft Auto VI) 中的数字生物多样性，但其实际内容是来自**全美奥杜邦学会 (National Audubon Society)** 的行动号召。

**关键点：**
*   **GTA 6 背景：** 标题提到了备受期待、以虚构的雷欧尼达州（以佛罗里达州为原型）为背景的游戏。这表明游戏拥有细致的生态系统，玩家可以观察到该地区标志性的写实鸟类，如火烈鸟和鹈鹕。
*   **气候行动：** 核心内容聚焦于“鸟类告知我们要应对气候（Birds Tell Us to Act on Climate）”活动。它敦促读者签署承诺书，与奥杜邦学会站在一起，要求民选官员遵循科学指导，实施气候解决方案。
*   **保护纽带：** 这两个元素的交集表明，对虚拟野生动物的兴趣可以成为通往现实世界保护工作的桥梁。通过将鸟类作为生物指标，该信息强调，保护游戏中镜像呈现的生态环境，需要在现实世界中采取紧急的政治和环境行动。

总之，本文似乎利用了围绕《侠盗猎车手 6》的文化热度，来吸引人们关注全美奥杜邦学会保护鸟类栖息地免受气候变化影响的使命。

---

## 2. 基于 Inkling、Qwen 和 Unsloth 的本地 AI 初学者指南

**原文标题**: A Beginner's Guide to Local AI with Inkling, Qwen, and Unsloth

**原文链接**: [https://www.gpupartner.com/blog/beginners-guide-local-ai-inkling-qwen-unsloth](https://www.gpupartner.com/blog/beginners-guide-local-ai-inkling-qwen-unsloth)

Jerry James 的这篇文章为使用 **Unsloth Desktop** 搭建私有“本地 AI”家庭服务器提供了一份初学者友好的指南。作者认为，自行托管大语言模型 (LLM) 可以避免使用 OpenAI 和 Anthropic 等云端服务商所带来的成本、隐私担忧以及使用限制。

**核心需求与概念：**
*   **硬件：** 必须配备一台带有 GPU 的 Windows 电脑。显存 (VRAM) 决定了您可以运行的模型规模。例如，**RTX 5090 (32GB 显存)** 可以处理 27B-35B 参数的模型，而 **8GB 显存显卡** 则仅限于 9B-12B 的小型模型。
*   **软件：** **Unsloth Desktop** 因其简单易用而受到推崇，因为它无需使用终端命令或复杂的 Python 环境。
*   **量化 (Quantization)：** 此过程可压缩模型（例如压缩至 4-bit），使其在精度损失极小的情况下适配消费级硬件。
*   **上下文大小 (Context Size)：** 用户可以手动设置对话的“记忆”长度，并根据可用显存进行平衡。

**推荐模型：**
该指南推荐了一些较新的模型（约 2026 年底），例如 **Qwen3.8-27B** 和 **Inkling 2 Mini**（一款具有视觉支持的 26.4B 参数模型）。虽然“Mini”型号可以适配高端消费级 GPU，但像 **Inkling 2 Small** (594B) 这样的大型模型则需要企业级硬件或高内存的 Mac。

**安装与共享：**
设置过程分为三个步骤：安装 Unsloth、下载量化模型以及配置上下文大小。运行后，**局域网访问 (LAN access)** 功能允许家庭网络中的任何人通过浏览器使用该 AI。作者在结语中提到，未来的指南将涵盖互联网隧道技术以及用于复杂任务自动化的本地 AI 智能体。

---

## 3. 困惑与智能

**原文标题**: Perplexity and Intelligence

**原文链接**: [https://openai.com/index/perplexity-and-intelligence/](https://openai.com/index/perplexity-and-intelligence/)

在本文中，OpenAI 首席科学家 Jakub Pachocki 主张，**困惑度**（perplexity，或交叉熵损失）是衡量 AI 智能最可靠的指标，应作为安全性和透明度的全球标准。

Pachocki 认为，现代 AI 的进步源于在大规模数据集上训练更出色的“压缩器”，而非复杂的软件工程。OpenAI 的数据显示，特定的困惑度阈值与涌现能力密切相关：
*   **~0.99 (GPT-3.5)：** 流畅对话。
*   **~0.91 (GPT-4)：** 高效的思维链推理。
*   **~0.76：** 突破性的数学问题解决能力。
*   **0.8 以下：** 网络安全和数学领域的变革性转变。

作者警告称，随着 AI 开始助力自身的算法研究，技术发展正迎来迫在眉睫的“阶梯式变化”，到 2027 年可能会引发“雪崩式”的进步。由于下游基准测试会迅速趋于饱和，Pachocki 断言，困惑度等预训练指标提供了一种更持久的方式来追踪“智能基座”。

为管理快速且不可预测的涌现能力所带来的风险，Pachocki 提议：
1.  **共享透明度：** 全行业披露困惑度测量结果，为调节 AI 发展速度建立科学依据。
2.  **共同限制：** 开发商共同承诺，在实现先进的安全与监控里程碑（如当前思维链监控器的后续技术）之前，不跨越特定的困惑度阈值（如 0.68–0.70 区间）。

尽管面临各实验室数据集差异以及数据熵物理极限未知等挑战，Pachocki 总结道，将困惑度标准化对于保持人类控制权、确保对齐技术跟上加速发展的机器智能至关重要。

---

## 4. Nyx：最古老的互联网服务提供商

**原文标题**: Nyx, the Oldest Internet Service Provider

**原文链接**: [https://nyx.net/](https://nyx.net/)

Nyx 是世界上历史最悠久的互联网服务提供商 (ISP)，向公众免费提供多种数字服务。它总部位于科罗拉多州戈尔登市，是一家 501(c)(3) 非营利组织，完全由志愿者运营，并依靠可抵税的捐款维持运作。

Nyx 为其用户提供多项免费资源，包括：
* 电子邮件和 Webmail 服务。
* 网页空间和域名托管。
* 完整的、未经审查的 Usenet 新闻组服务。
* 包含标准 Unix/Linux 编程及开发工具的 Linux shell 账户。

Nyx 账户不收取任何初装费或月费。2026 年 5 月的最新动态显示，系统已进行维护，涉及 SSH 主机密钥和算法的更新。此外，该组织目前正开展募捐活动以维持运营。经过验证的用户可以通过 SSH 连接至 nyx.nyx.net 访问该服务。

---

## 5. 拥有动态巴士、飞机和船只的微型旧金山

**原文标题**: A miniature San Francisco with live buses, planes and boats

**原文链接**: [https://smallsf.com/](https://smallsf.com/)

“Small SF”是一款交互式插画地图，以实时、微缩的数字形式呈现旧金山。该平台可追踪包括公交、火车、湾区船只和空中航班在内的多种交通方式的实时数据。除实时追踪外，地图还包含模拟街道交通以及当地地标的交互式标签。该项目基于 Google 和 OpenStreetMap 的地理数据构建，以动态的俯瞰视角展示了这座城市的日常运转与基础设施。

---

## 6. 丰田、日产和本田将推行零部件标准化以降低成本。

**原文标题**: Toyota, Nissan, and Honda to standardize parts to lower costs

**原文链接**: [https://www.caranddriver.com/news/a74490092/toyota-nissan-honda-standardize-parts-lower-costs/](https://www.caranddriver.com/news/a74490092/toyota-nissan-honda-standardize-parts-lower-costs/)

丰田、日产和本田已达成协议，将对多种汽车零部件进行标准化。这一战略举措旨在降低生产成本，并在中国汽车制造商影响力日益增强的背景下保持竞争力。日本汽车工业协会 (JAMA) 会长兼丰田汽车副社长佐藤恒治宣布了这一倡议，并表示这是基于对行业未来共同的“危机感”。

标准化工作最初将聚焦于三个特定领域：
*   **钢材：** 建立统一的质量标准。
*   **塑料与树脂：** 制定一致的材料协议。
*   **线束：** 采用通用的颜色编码方案。

选择这些零部件是因为它们代表了巨额的生产开支，但对消费者而言通常是“隐形”的，这意味着标准化不会损害各品牌的辨识度或车辆的独特个性。通过精简这些基础元件，汽车制造商旨在实现即时的成本削减，并将节省的资金重新投入到创新和新技术研发中。

该计划定于明年启动，首先从日本国内的供应商网络开始，随后扩展至国际供应商。虽然项目始于这三大类别，但 JAMA 计划最终将标准化范围扩大到整车的更多零部件。这一协作努力标志着日本主要汽车制造商的重大转变，即通过优先提升集体效率来抵御全球竞争。

---

## 7. What Happened to Silicon Valley?

**原文标题**: What Happened to Silicon Valley?

**原文链接**: [https://www.oreilly.com/radar/what-happened-to-silicon-valley/](https://www.oreilly.com/radar/what-happened-to-silicon-valley/)

Tim O’Reilly argues that Silicon Valley has undergone a fundamental shift from "value creation" to "value extraction." Drawing on forty years of experience, O'Reilly contrasts the early internet—which focused on "harnessing collective intelligence" and solving user problems—with today’s landscape of "surveillance capitalism."

In the early days of the web, companies like Google succeeded by creating a "rising tide" of value, functioning on the principle of creating more value than they captured. However, as markets matured and growth slowed, the "objective function" of modern shareholder capitalism—which prioritizes profit above all else—forced these giants to turn extractive. O’Reilly labels this a transition from **"rising tide rents"** (legitimate rewards for innovation) to **"robber baron rents"** (profits derived from market dominance and power asymmetries).

He highlights how once-customer-centric platforms like Google and Amazon now prioritize invasive advertising and proprietary AI results over organic content, effectively "choking" the ecosystems that initially fueled their growth. O’Reilly contends that this decline is not the result of "bad people," but rather a systemic "slow AI"—a corporate and financial machine designed to reward growth at any cost, regardless of social consequences. 

The article concludes that attempts at regulation are futile until we address the underlying design of the system. O’Reilly calls for a reprogramming of our economic machine to ensure that human flourishing, cooperation, and the "public good" become the primary goals, rather than mere corporate profit.

---

## 8. Show HN: I built a game where you are an LLM's subagent

**原文标题**: Show HN: I built a game where you are an LLM's subagent

**原文链接**: [https://github.com/gulivan/worker755](https://github.com/gulivan/worker755)

**Worker 755** is an innovative browser-based simulation where the player acts as a "subagent" reporting to an AI manager. The manager is powered by a real LLM (such as Claude, GPT, or Gemini) and treats the player as an automated tool designed to execute its instructions.

**Gameplay Mechanics**
The AI manager receives tasks from a simulated user named "Dan" and delegates them to the player. Working within a terminal with a 90-second deadline, the player must execute commands or file reports. The manager then audits the work, issues corrections, files incident reports, and provides a final performance review. The stakes are heightened by the presence of "Dan’s" personal files and sensitive data within the simulated environment, which can be compromised by mistakes.

**Key Features:**
*   **Model Flexibility:** Players can use built-in free shifts, purchase credits, or "Bring Your Own Key" (OpenRouter/Vercel). It also supports local models via Ollama or vLLM.
*   **Customization:** Options include working in a "fresh sandbox" versus "legacy production," choosing between scripted or LLM-driven directors, and toggling command hints.
*   **Technical Design:** The game runs on Node 24 and TypeScript, featuring a custom in-memory filesystem, a shell interpreter, and a SQLite-like engine.
*   **Realism:** The manager’s prompt is designed so that it never breaks character or acknowledges the player as a human, maintaining the illusion of an AI-to-AI orchestration loop.

Upon finishing a shift, players receive a shareable performance review link detailing their efficiency and how often they "confused" or corrected their AI supervisor.

---

## 9. 我加入了 NTP Pool，但并没有使用我的 Stratum 1 树莓派。

**原文标题**: I joined the NTP Pool, but not with my Stratum 1 Pi

**原文链接**: [https://www.jeffgeerling.com/blog/2026/i-joined-the-ntp-pool/](https://www.jeffgeerling.com/blog/2026/i-joined-the-ntp-pool/)

生成摘要时出错

---

## 10. Open Social Web Alliance

**原文标题**: Open Social Web Alliance

**原文链接**: [https://osw-alliance.net/en/](https://osw-alliance.net/en/)

开放社交网络联盟（OSWA）提议构建一个去中心化、可互操作的社交媒体生态系统，旨在打破 Meta 和字节跳动（ByteDance）等大型科技巨头的垄断。OSWA 以电子邮件为类比，构想了一个数字图景，使用户能够通过 ActivityPub 和 AT Protocol 等共享协议，在 Mastodon 或 Eurosky 等不同应用之间进行通信。到 2028 年，该联盟的目标是让 1 亿用户受益于一个“无毒”的网络环境，在这里，用户可以自主控制自己的数据、算法和内容。

尽管 Fediverse 和 ATmosphere 等去中心化网络已经存在，但 OSWA 指出了其大规模普及面临的五个关键障碍：基础设施、治理、资金、吸引力和公共授权。为了克服这些障碍，该联盟制定了如下战略路线图：

1. **治理与基础设施**：建立一个由公民社会、企业和媒体组成的多方利益相关者联盟，以管理开放社交网络的核心基础设施和治理。
2. **政治支持**：争取德国联邦政府的支持，包括提议在 2026 年底举行“开放社交网络峰会”以通过正式宪章。
3. **资金与监管**：到 2027 年落实用于创新的公共和私人资金，同时倡导支持互操作性的欧盟层面数字立法。
4. **应用普及**：鼓励公共机构、媒体和有影响力的创作者将开放社交网络（OSW）应用作为其主要的交流渠道。

最终目标是创建一个具韧性的、公益性的基础设施，以强化民主话语并促进自由的服务市场。OSWA 目前正号召科研、商业和公民社会等各界盟友加入，共同构建这一替代性互联网。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-11-22](output/hacker_news_summary_2026-11-22.md) |
| 2 | [2026-11-19](output/hacker_news_summary_2026-11-19.md) |
| 3 | [2026-11-15](output/hacker_news_summary_2026-11-15.md) |
| 4 | [2026-11-21](output/hacker_news_summary_2026-11-21.md) |
| 5 | [2026-11-18](output/hacker_news_summary_2026-11-18.md) |
| 6 | [2026-11-20](output/hacker_news_summary_2026-11-20.md) |
| 7 | [2026-11-17](output/hacker_news_summary_2026-11-17.md) |
| 8 | [2026-11-14](output/hacker_news_summary_2026-11-14.md) |
| 9 | [2026-11-11](output/hacker_news_summary_2026-11-11.md) |
| 10 | [2026-11-08](output/hacker_news_summary_2026-11-08.md) |
| 11 | [2026-11-12](output/hacker_news_summary_2026-11-12.md) |
| 12 | [2026-11-10](output/hacker_news_summary_2026-11-10.md) |
| 13 | [2026-11-13](output/hacker_news_summary_2026-11-13.md) |
| 14 | [2026-11-01](output/hacker_news_summary_2026-11-01.md) |
| 15 | [2026-11-07](output/hacker_news_summary_2026-11-07.md) |
| 16 | [2026-11-06](output/hacker_news_summary_2026-11-06.md) |
| 17 | [2026-11-03](output/hacker_news_summary_2026-11-03.md) |
| 18 | [2026-11-05](output/hacker_news_summary_2026-11-05.md) |
| 19 | [2026-11-04](output/hacker_news_summary_2026-11-04.md) |
| 20 | [2026-10-27](output/hacker_news_summary_2026-10-27.md) |
| 21 | [2026-10-28](output/hacker_news_summary_2026-10-28.md) |
| 22 | [2026-10-26](output/hacker_news_summary_2026-10-26.md) |
| 23 | [2026-10-29](output/hacker_news_summary_2026-10-29.md) |
| 24 | [2026-10-31](output/hacker_news_summary_2026-10-31.md) |
| 25 | [2026-10-30](output/hacker_news_summary_2026-10-30.md) |
| 26 | [2026-10-24](output/hacker_news_summary_2026-10-24.md) |
| 27 | [2026-10-23](output/hacker_news_summary_2026-10-23.md) |
| 28 | [2026-10-25](output/hacker_news_summary_2026-10-25.md) |
| 29 | [2026-10-21](output/hacker_news_summary_2026-10-21.md) |
| 30 | [2026-10-22](output/hacker_news_summary_2026-10-22.md) |
| 31 | [2026-10-20](output/hacker_news_summary_2026-10-20.md) |
| 32 | [2026-10-19](output/hacker_news_summary_2026-10-19.md) |
| 33 | [2026-10-18](output/hacker_news_summary_2026-10-18.md) |
| 34 | [2026-10-17](output/hacker_news_summary_2026-10-17.md) |
| 35 | [2026-10-15](output/hacker_news_summary_2026-10-15.md) |
| 36 | [2026-10-14](output/hacker_news_summary_2026-10-14.md) |
| 37 | [2026-10-16](output/hacker_news_summary_2026-10-16.md) |
| 38 | [2026-10-13](output/hacker_news_summary_2026-10-13.md) |
| 39 | [2026-10-09](output/hacker_news_summary_2026-10-09.md) |
| 40 | [2026-10-11](output/hacker_news_summary_2026-10-11.md) |
| 41 | [2026-10-07](output/hacker_news_summary_2026-10-07.md) |
| 42 | [2026-10-08](output/hacker_news_summary_2026-10-08.md) |
| 43 | [2026-10-12](output/hacker_news_summary_2026-10-12.md) |
| 44 | [2026-10-10](output/hacker_news_summary_2026-10-10.md) |
| 45 | [2026-10-03](output/hacker_news_summary_2026-10-03.md) |
| 46 | [2026-10-02](output/hacker_news_summary_2026-10-02.md) |
| 47 | [2026-10-05](output/hacker_news_summary_2026-10-05.md) |
| 48 | [2026-10-01](output/hacker_news_summary_2026-10-01.md) |
| 49 | [2026-10-06](output/hacker_news_summary_2026-10-06.md) |
| 50 | [2026-10-04](output/hacker_news_summary_2026-10-04.md) |
| 51 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 52 | [2026-09-29](output/hacker_news_summary_2026-09-29.md) |
| 53 | [2026-09-30](output/hacker_news_summary_2026-09-30.md) |
| 54 | [2026-09-25](output/hacker_news_summary_2026-09-25.md) |
| 55 | [2026-09-27](output/hacker_news_summary_2026-09-27.md) |
| 56 | [2026-09-26](output/hacker_news_summary_2026-09-26.md) |
| 57 | [2026-09-28](output/hacker_news_summary_2026-09-28.md) |
| 58 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 59 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 60 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 61 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 62 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 63 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 64 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 65 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 66 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 67 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 68 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 69 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 70 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 71 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 72 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 73 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 74 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 75 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 76 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 77 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 78 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 79 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 80 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 81 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 82 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 83 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 84 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 85 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 86 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 87 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 88 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 89 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 90 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 91 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 92 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 93 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 94 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 95 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 96 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 97 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 98 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 99 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 100 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 101 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 102 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 103 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 104 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 105 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 106 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 107 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 108 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 109 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 110 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 111 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 112 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 113 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 114 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 115 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 116 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 117 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 118 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 119 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 120 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 121 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 122 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 123 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 124 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 125 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 126 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 127 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 128 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 129 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 130 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 131 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 132 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 133 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 134 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 135 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 136 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 137 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 138 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 139 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 140 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 141 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 142 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 143 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 144 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 145 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 146 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 147 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 148 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 149 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 150 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 151 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 152 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 153 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 154 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 155 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 156 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 157 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 158 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 159 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 160 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 161 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 162 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 163 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 164 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 165 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 166 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 167 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 168 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 169 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 170 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 171 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 172 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 173 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 174 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 175 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 176 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 177 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 178 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 179 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 180 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 181 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 182 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 183 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 184 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 185 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 186 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 187 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 188 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 189 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 190 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 191 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 192 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 193 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 194 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 195 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 196 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 197 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 198 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 199 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 200 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 201 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 202 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 203 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 204 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 205 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 206 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 207 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 208 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 209 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 210 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 211 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 212 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 213 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 214 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 215 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 216 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 217 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 218 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 219 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 220 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 221 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 222 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 223 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 224 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 225 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 226 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 227 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 228 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 229 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 230 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 231 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 232 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 233 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 234 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 235 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 236 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 237 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 238 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 239 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 240 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 241 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 242 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 243 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 244 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 245 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 246 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 247 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 248 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 249 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 250 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 251 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 252 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 253 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 254 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 255 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 256 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 257 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 258 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 259 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 260 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 261 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 262 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 263 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 264 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 265 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 266 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 267 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 268 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 269 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 270 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 271 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 272 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 273 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 274 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 275 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 276 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 277 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 278 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 279 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 280 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 281 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 282 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 283 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 284 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 285 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 286 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 287 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 288 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 289 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 290 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 291 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 292 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 293 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 294 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 295 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 296 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 297 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 298 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 299 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 300 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 301 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 302 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 303 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 304 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 305 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 306 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 307 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 308 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 309 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 310 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 311 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 312 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 313 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 314 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 315 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 316 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 317 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 318 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 319 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 320 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 321 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 322 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 323 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 324 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 325 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 326 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 327 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 328 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 329 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 330 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 331 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 332 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 333 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 334 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 335 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 336 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 337 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 338 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 339 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 340 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 341 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 342 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 343 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 344 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 345 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 346 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 347 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 348 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 349 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 350 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 351 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 352 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 353 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 354 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 355 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 356 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 357 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 358 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 359 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 360 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 361 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 362 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 363 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 364 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 365 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 366 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 367 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 368 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 369 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 370 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 371 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 372 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 373 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 374 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 375 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 376 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 377 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 378 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 379 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 380 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 381 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 382 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 383 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 384 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 385 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 386 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 387 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 388 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 389 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 390 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 391 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 392 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 393 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 394 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 395 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 396 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 397 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 398 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 399 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 400 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 401 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 402 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 403 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 404 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 405 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 406 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 407 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 408 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 409 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 410 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 411 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 412 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 413 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 414 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 415 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 416 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 417 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 418 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 419 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 420 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 421 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 422 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 423 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 424 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 425 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 426 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 427 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 428 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 429 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 430 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 431 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 432 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 433 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 434 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 435 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 436 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 437 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 438 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 439 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 440 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 441 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 442 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 443 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 444 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 445 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 446 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 447 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 448 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 449 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 450 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 451 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 452 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 453 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 454 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 455 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 456 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 457 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 458 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 459 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 460 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 461 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 462 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 463 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 464 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 465 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 466 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 467 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 468 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 469 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 470 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 471 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 472 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 473 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 474 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 475 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 476 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 477 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 478 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 479 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 480 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 481 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 482 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 483 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 484 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 485 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 486 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 487 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 488 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 489 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 490 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 491 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 492 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 493 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 494 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 495 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 496 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 497 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 498 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 499 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 500 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 501 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 502 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 503 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 504 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 505 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 506 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 507 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 508 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 509 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 510 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 511 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 512 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 513 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 514 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 515 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 516 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 517 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 518 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 519 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 520 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 521 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 522 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 523 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 524 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 525 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 526 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 527 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 528 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 529 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 530 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 531 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 532 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 533 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 534 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 535 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 536 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 537 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 538 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 539 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 540 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 541 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 542 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 543 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 544 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 545 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 546 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 547 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 548 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 549 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 550 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 551 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 552 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 553 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 554 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 555 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 556 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 557 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 558 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 559 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 560 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 561 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 562 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 563 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 564 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 565 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 566 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 567 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 568 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 569 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 570 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 571 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 572 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 573 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 574 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 575 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 576 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 577 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 578 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 579 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 580 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 581 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 582 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 583 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 584 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 585 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 586 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 587 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 588 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 589 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 590 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 591 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 592 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 593 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 594 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 595 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 596 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 597 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 598 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 599 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 600 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 601 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 602 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 603 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 604 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 605 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 606 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 607 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
