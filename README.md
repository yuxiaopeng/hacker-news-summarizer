# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-08-04.md)

*最后自动更新时间: 2026-08-04 19:12:37*
## 1. 威诺纳警察局所有Flock摄像头遭锯断并被盗

**原文标题**: All of Winona Police Department's Flock cameras cut down and stolen

**原文链接**: [https://www.valleynewslive.com/2026/08/04/every-flock-camera-winona-minnesota-cut-down-stolen-coordinated-theft/](https://www.valleynewslive.com/2026/08/04/every-flock-camera-winona-minnesota-cut-down-stolen-coordinated-theft/)

威诺纳警察局正在调查一起协同盗窃案。8月1日，该局全部八台Flock车牌识别摄像头均被人从电线杆上锯断并窃走。此外，布法罗县位于密西西比河大桥上的两台摄像头也以相同方式被盗。

威诺纳警察局的总经济损失估计为24,000美元，每台摄像头价值约3,000美元。执法部门利用这些自动化设备抓取车辆数据——包括车牌、品牌和颜色——以协助调查肇事逃逸和失踪人员案件。

该事件反映了全国范围内破坏Flock技术的趋势。虽然警方视这些摄像头为保障公共安全的重要工具，但公民自由倡导者批评此类系统扩大了政府监控，并对数据隐私表示担忧。

目前尚未确定嫌疑人，调查仍在进行中。威诺纳警察局请求任何了解盗窃案相关信息的人员主动提供线索。

---

## 2. Show HN：用于生成多样化肤色的简单算法和色彩空间

**原文标题**: Show HN: Simple algorithm and color space to generate diverse skin tones

**原文链接**: [https://toneyalexander.github.io/inclusive-color-space/](https://toneyalexander.github.io/inclusive-color-space/)

本文介绍了一种自定义色彩空间和算法，旨在为角色编辑器和艺术工具等数字应用生成多样化且具有包容性的人类肤色。其目标是提供一个“足够好”的数学框架，填补表情符号（emoji）有限的选择与 1600 万色 RGB 全频谱极高复杂性之间的空白。

**方法论**
作者通过以下多步流程开发了该系统：
1. **手动标记：** 手动将 RGB 颜色分类为合理的肤色，以创建原始数据集。
2. **主成分分析 (PCA)：** 利用这种统计方法将数据云旋转并拉伸为更易处理的 XYZ 坐标系。
3. **函数拟合：** 作者使用 Desmos 手动将球面方程拟合到数据中，从而创建了全新的“TUV”色彩空间。

**TUV 色彩空间**
其中一个最重要的发现是，PCA 自然地将坐标轴与直观的人类概念对齐：
* **T：** 调节深浅程度。
* **U：** 调节“红润”（偏粉）与“赭色”（偏黄）色调。
* **V：** 调节冷暖底色。

**实现与局限性**
该项目包含了用于从这个“肤色球体”中采样并转换回 RGB 的 Python 和 JavaScript 代码。作者强调，这是一种工程优先、且“非科学”的方法。他们承认该方法存在若干局限性，包括标记的主观性、不同屏幕校准的影响，以及皮肤复杂的生物学特性（涉及光散射和健康因素），这些是单一颜色无法完全捕捉的。

最终，这项工作为希望改善数字媒体代表性的开发者提供了一个实用的、开源的起点。

---

## 3. 各位，安全真的很难。

**原文标题**: Security Is Hard, Y'all

**原文链接**: [https://textslashplain.com/2026/08/04/security-is-hard-yall/](https://textslashplain.com/2026/08/04/security-is-hard-yall/)

无法访问文章链接。

---

## 4. Hop.earth – 基于 OpenStreetMap 的赛车游戏

**原文标题**: Hop.earth – OpenStreetMap based car racing game

**原文链接**: [https://hop.earth/?server=lkhr7&route=fQ5nuu9R](https://hop.earth/?server=lkhr7&route=fQ5nuu9R)

**Hop.earth** 是一款赛车游戏，通过利用 OpenStreetMap (OSM) 数据将现实世界中的地点转化为可游玩的赛道，让玩家能够“驰骋世界”。

该平台通过集成高分辨率地形和地理空间数据集来确保环境的准确性，从而彰显其独特优势。关键数据源包括用于全球地形的哥白尼数字高程模型 (COP-DEM-GLO-30)，以及来自法国 IGN RGE ALTI® 和西班牙 CNIG LIDAR 的专业区域数据。通过整合这些资源，Hop.earth 为玩家提供了植根于真实全球地理的沉浸式赛车体验。

---

## 5. 数据集：2000-2026年已倒闭的心理健康初创公司，按18个字段编码

**原文标题**: Dataset: Dead mental health startups, 2000-2026, coded on 18 fields

**原文链接**: [https://mentalium.me/en/research/mental-health-startup-graveyard-dataset/](https://mentalium.me/en/research/mental-health-startup-graveyard-dataset/)

“已倒闭心理健康初创企业”数据集对2000年至2026年间退出市场的542家数字心理健康机构进行了全面分析。该数据集涵盖了倒闭、破产和收购情况，并从融资、营收模式以及解释失败原因的定性“关键失误”字段等18个维度对每家公司进行了编码。

数据的主要发现是，商业模式（即支付方是谁）对生存的影响远比团队构成更为显著。与面向消费者的模式（死亡率为53%）相比，由机构（雇主、保险公司或医院）资助的初创公司死亡率明显更低（21%），退出率则更高（57%）。值得注意的是，数据表明，拥有医学背景的联合创始人对公司成功退出的可能性完全没有影响，两组样本的退出率均为47%。

研究方法采用了混合方式：事实性数据（日期、融资、结果）源自Crunchbase和行业媒体等数据库，而四个定性分类维度则通过LLM智能体确定。为确保透明度，作者提供了一份逻辑说明文件，记录了每个LLM生成标签背后的推理过程。

该数据集由Mentalium创始人编制，旨在识别该细分领域中反复出现的失败模式。它基于CC BY 4.0许可协议发布，允许免费使用和转载。这些数据是一份长达406页、题为《心理健康初创企业坟场：542家倒闭公司及七大模式》报告的基础，为该领域的未来创业者和投资者提供了警示性参考。

---

## 6. Warp Agent 命令行工具

**原文标题**: The Warp Agent CLI

**原文链接**: [https://www.warp.dev/blog/introducing-the-warp-agent-cli-coding-agent](https://www.warp.dev/blog/introducing-the-warp-agent-cli-coding-agent)

Warp 推出了 **Warp Agent CLI**，这是一款独立工具，可将 Warp 终端的 AI 能力引入任何环境，包括 iTerm2、VS Code、Ghostty 以及标准的 Windows/Mac 终端。

该 CLI 基于类似于 tmux 的独特多路复用（“muxing”）架构构建，提供了一个超越传统终端封装器的持久化会话层。这种基础设施允许 Agent 在切换目录时保持状态，控制交互式全屏应用程序（如 Vim、Python REPL 或 GDB），并能在无需安装远程二进制文件的情况下通过 SSH 会话运行。

核心功能包括：
*   **高级编排**：该 CLI 支持多 Agent 工作流，可将复杂任务委派给专门的子 Agent。它还提供“云端 Agent 接力”功能，允许用户在本地启动任务，并将其转移到云端进行远程执行和监控。
*   **智能 UI**：它具备自然语言检测功能，可区分 Shell 命令与 AI 提示词，并集成了 Warp 标志性的参数和标志（flags）Tab 补全功能。
*   **模型路由**：为了优化性能和成本，该 CLI 充当“帕累托效率调度器”，根据任务复杂度自动将任务路由至前沿模型或开源权重模型。

用户可以通过 Warp 订阅、即用即付积分或连接自己的 OpenAI 兼容 API 密钥来使用该工具。Warp Agent CLI 定位于“自主开发”时代的工具，旨在弥合本地终端工作流与云端软件工厂之间的差距。

---

## 7. 单块 AMD MI300X 上的 DeepSeek V4 Flash

**原文标题**: DeepSeek V4 Flash on a Single AMD MI300X

**原文链接**: [https://github.com/ryanzhou/deepseek-v4-flash-mi300x](https://github.com/ryanzhou/deepseek-v4-flash-mi300x)

This article details a production-ready configuration for running the 304B-parameter **DeepSeek-V4-Flash-0731** model on a **single AMD MI300X GPU**. By leveraging the MI300X’s 192GB HBM3 capacity, the setup hosts the entire model without weight offloading or additional quantization, providing a cost-effective alternative to NVIDIA-based deployments.

The repository addresses several hardware-specific challenges unique to the MI300X (gfx942). Key technical contributions include:

*   **Correctness Fixes:** Patches for the FNUZ FP8 format (specific to MI300X) and MXFP4 MoE routing to prevent data corruption and scaling errors that occur when using standard OCP semantics.
*   **Kernel Tuning:** Optimized AITER GEMM tables and Triton kernel overrides that improve decode performance by up to 62% for specific architecture shapes.
*   **Speculative Decoding:** Integration of DSpark-7 with probabilistic drafting and block rejection, achieving single-stream decode speeds of **168.6 tok/s**.
*   **Memory Management:** A hybrid KV strategy utilizing 20GB of GPU VRAM and a 96GB CPU tier for prefix-cache entries, supporting a 256K validated context and up to 64 concurrent streams.

Performance benchmarks show prefill speeds of approximately **8K tok/s** and an aggregate throughput of **830 tok/s** during 64-stream bursts. The solution is delivered as a Docker Compose stack with digest-pinned vLLM ROCm images and file overlays to ensure stability and reproducibility. This work builds upon and extends previous community efforts to optimize the vLLM stack for MI300X hardware in high-concurrency production environments.

---

## 8. Launch HN: EdotEnv (YC S26) – Quant Trading RL Envs to Teach LLMs Research

**原文标题**: Launch HN: EdotEnv (YC S26) – Quant Trading RL Envs to Teach LLMs Research

**原文链接**: [https://edotenv.com/](https://edotenv.com/)

生成摘要时出错

---

## 9. Truemetrics (YC S23) Is Hiring in Berlin – GTM Lead

**原文标题**: Truemetrics (YC S23) Is Hiring in Berlin – GTM Lead

**原文链接**: [https://www.ycombinator.com/companies/truemetrics/jobs/bIQQ7tP-founding-gtm-lead](https://www.ycombinator.com/companies/truemetrics/jobs/bIQQ7tP-founding-gtm-lead)

生成摘要时出错

---

## 10. Vlt 1.0 and Hosted Package Registries

**原文标题**: Vlt 1.0 and Hosted Package Registries

**原文链接**: [https://www.vlt.io/blog/1-0](https://www.vlt.io/blog/1-0)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 2 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 3 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 4 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 5 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 6 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 7 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 8 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 9 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 10 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 11 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 12 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 13 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 14 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 15 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 16 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 17 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 18 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 19 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 20 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 21 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 22 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 23 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 24 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 25 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 26 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 27 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 28 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 29 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 30 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 31 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 32 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 33 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 34 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 35 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 36 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 37 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 38 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 39 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 40 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 41 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 42 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 43 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 44 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 45 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 46 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 47 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 48 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 49 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 50 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 51 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 52 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 53 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 54 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 55 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 56 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 57 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 58 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 59 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 60 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 61 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 62 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 63 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 64 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 65 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 66 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 67 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 68 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 69 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 70 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 71 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 72 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 73 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 74 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 75 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 76 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 77 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 78 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 79 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 80 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 81 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 82 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 83 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 84 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 85 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 86 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 87 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 88 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 89 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 90 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 91 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 92 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 93 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 94 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 95 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 96 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 97 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 98 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 99 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 100 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 101 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 102 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 103 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 104 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 105 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 106 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 107 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 108 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 109 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 110 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 111 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 112 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 113 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 114 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 115 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 116 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 117 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 118 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 119 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 120 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 121 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 122 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 123 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 124 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 125 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 126 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 127 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 128 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 129 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 130 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 131 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 132 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 133 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 134 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 135 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 136 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 137 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 138 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 139 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 140 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 141 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 142 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 143 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 144 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 145 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 146 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 147 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 148 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 149 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 150 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 151 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 152 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 153 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 154 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 155 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 156 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 157 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 158 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 159 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 160 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 161 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 162 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 163 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 164 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 165 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 166 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 167 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 168 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 169 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 170 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 171 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 172 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 173 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 174 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 175 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 176 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 177 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 178 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 179 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 180 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 181 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 182 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 183 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 184 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 185 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 186 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 187 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 188 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 189 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 190 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 191 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 192 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 193 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 194 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 195 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 196 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 197 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 198 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 199 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 200 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 201 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 202 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 203 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 204 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 205 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 206 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 207 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 208 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 209 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 210 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 211 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 212 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 213 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 214 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 215 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 216 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 217 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 218 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 219 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 220 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 221 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 222 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 223 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 224 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 225 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 226 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 227 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 228 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 229 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 230 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 231 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 232 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 233 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 234 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 235 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 236 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 237 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 238 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 239 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 240 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 241 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 242 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 243 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 244 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 245 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 246 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 247 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 248 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 249 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 250 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 251 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 252 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 253 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 254 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 255 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 256 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 257 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 258 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 259 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 260 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 261 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 262 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 263 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 264 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 265 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 266 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 267 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 268 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 269 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 270 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 271 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 272 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 273 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 274 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 275 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 276 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 277 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 278 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 279 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 280 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 281 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 282 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 283 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 284 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 285 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 286 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 287 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 288 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 289 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 290 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 291 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 292 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 293 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 294 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 295 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 296 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 297 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 298 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 299 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 300 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 301 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 302 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 303 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 304 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 305 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 306 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 307 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 308 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 309 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 310 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 311 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 312 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 313 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 314 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 315 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 316 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 317 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 318 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 319 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 320 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 321 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 322 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 323 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 324 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 325 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 326 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 327 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 328 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 329 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 330 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 331 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 332 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 333 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 334 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 335 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 336 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 337 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 338 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 339 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 340 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 341 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 342 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 343 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 344 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 345 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 346 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 347 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 348 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 349 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 350 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 351 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 352 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 353 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 354 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 355 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 356 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 357 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 358 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 359 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 360 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 361 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 362 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 363 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 364 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 365 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 366 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 367 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 368 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 369 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 370 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 371 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 372 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 373 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 374 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 375 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 376 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 377 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 378 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 379 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 380 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 381 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 382 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 383 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 384 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 385 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 386 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 387 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 388 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 389 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 390 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 391 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 392 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 393 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 394 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 395 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 396 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 397 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 398 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 399 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 400 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 401 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 402 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 403 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 404 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 405 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 406 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 407 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 408 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 409 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 410 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 411 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 412 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 413 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 414 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 415 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 416 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 417 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 418 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 419 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 420 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 421 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 422 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 423 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 424 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 425 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 426 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 427 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 428 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 429 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 430 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 431 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 432 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 433 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 434 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 435 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 436 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 437 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 438 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 439 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 440 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 441 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 442 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 443 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 444 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 445 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 446 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 447 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 448 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 449 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 450 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 451 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 452 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 453 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 454 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 455 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 456 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 457 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 458 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 459 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 460 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 461 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 462 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 463 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 464 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 465 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 466 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 467 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 468 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 469 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 470 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 471 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 472 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 473 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 474 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 475 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 476 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 477 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 478 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 479 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 480 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 481 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 482 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 483 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 484 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 485 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 486 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 487 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 488 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 489 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 490 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 491 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 492 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 493 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 494 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 495 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 496 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 497 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 498 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 499 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 500 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 501 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 502 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
