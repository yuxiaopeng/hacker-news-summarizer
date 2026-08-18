# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-08-18.md)

*最后自动更新时间: 2026-08-18 17:55:52*
## 1. 将铁路网络用作平板扫描仪

**原文标题**: Using the railway network as a flatbed scanner

**原文链接**: [https://philo.gay/linecam/](https://philo.gay/linecam/)

在《将铁路网用作平板扫描仪》一文中，Philo 详细介绍了一个利用工业线阵扫描相机，从火车和渡轮等移动车辆上捕捉超宽、高分辨率全景图的项目。

**概念与硬件**
受数字扫描后背和“缝隙扫描”摄影的启发，Philo 使用了一台通常用于传送带检测的 Basler ruL2048-19gm 工业相机。与捕捉像素网格的标准相机不同，该相机以极高的频率（最高每秒 19,000 次）捕捉单条 2,048 像素的垂直线。车辆的移动构成了图像的水平轴，从而有效地将交通网络变成了一个巨大的平板扫描仪。整套装置包括一个定制的 3D 打印外壳、一个 28mm 镜头、一个用于追踪速度的加速度计/陀螺仪，以及一个用于将数据同步到笔记本电脑的微控制器。

**技术挑战**
该项目面临多重障碍：
*   **速度一致性：** 车辆速度的变化会导致生成的图像拉伸或压缩。Philo 利用加速度计数据对图像进行归一化处理，但整合这些含噪声的数据十分困难。
*   **数据处理：** 每秒捕捉数千行数据需要定制软件。Philo 使用 Dear ImGUI 开发了一个图形用户界面（GUI）来管理曝光和实时预览，克服了 OpenCV 等标准库的局限性。
*   **环境因素：** 为确保图像清晰而采用的高快门速度需要充足的日光，这导致隧道和夜间拍摄无法实现。

**成果**
尽管这套 DIY 设备因外观“可疑”在蒙特利尔与安保人员发生了轻微摩擦，但该项目成功拍摄了海量图像，包括一张旧金山-奥克兰轮渡航线的 56,894 像素宽灰度图，以及波士顿 MBTA 系统的精细全景图。该项目展示了工业传感器如何被重新用于创意大画幅数字摄影。

---

## 2. 修复变砖的 Framework 笔记本

**原文标题**: Fixing a bricked Framework laptop

**原文链接**: [https://quantum5.ca/2026/08/16/fixing-bricked-amd-7040-series-framework-13-laptop-with-20-tools/](https://quantum5.ca/2026/08/16/fixing-bricked-amd-7040-series-framework-13-laptop-with-20-tools/)

2026年，一位 Framework Laptop 13（AMD Ryzen 7040系列）用户在安装推荐的 BIOS 更新（v3.20）时遭遇了系统故障。尽管 Framework 的品牌核心理念是可修复性和对 Linux 的支持，但此次更新却导致设备“变砖”，屏幕花屏且毫无反应。

当作者联系 Framework 售后支持时，对方以一年保修期已过为由，除了建议花费 500 多加元购买更换主板外，未提供任何其他解决方案。作者发现，许多其他用户也报告了该版本更新导致的类似故障。作者特别指出，与戴尔、惠普等竞争对手甚至几十年前的老主板不同，Framework 缺乏内置的“紧急”BIOS 恢复机制（例如在故障后通过 USB 驱动器进行刷写）。

作者拒绝支付更换新主板的费用，转而尝试手动刷写 BIOS 芯片。技术挑战涉及一颗华邦（Winbond）25R256JWEQ 芯片，这是一款 1.8V SPI 闪存组件。由于该芯片采用 WSON（无引脚）封装，无法轻易使用夹具固定。作者确定了弹簧探针（pogo pin）和 USB 闪存编程器是无需焊接即可进行原位芯片连接的必要工具。

本文既是对 Framework 缺乏软件恢复工具的抨击，也是为那些被迫通过高级硬件维修来修复软件致死“变砖”问题的用户提供的详细指南。通过记录 BIOS 镜像的提取过程和具体的硬件需求，作者旨在帮助他人避开昂贵的主板更换开支。

---

## 3. 亚马逊税

**原文标题**: The Amazon tax

**原文链接**: [https://seths.blog/2026/08/the-amazon-tax/](https://seths.blog/2026/08/the-amazon-tax/)

生成摘要时出错

---

## 4. Launch HN: machine0 (YC S26) – 命令行驱动的持久化 CPU 和 GPU 虚拟机

**原文标题**: Launch HN: machine0 (YC S26) – Persistent CPU and GPU VMs from the CLI

**原文链接**: [https://machine0.io](https://machine0.io)

**machine0 (YC S26)** 是一家云基础设施平台，专门为长期运行的 AI 智能体（Agents）和计算密集型工作负载提供持久化的 CPU 与 GPU 虚拟机。该服务主要通过命令行界面（CLI）进行管理，强调可复现性、自动化和程序化控制。

**关键特性与硬件：**
*   **性能：** 提供 1 到 60 核 vCPU 以及高达 240 GB RAM 的虚拟机。高端 GPU 选项包括 NVIDIA H100、H200、L40S 以及 AMD MI300X。
*   **持久性与计费：** 虚拟机将保持活动状态，直到手动停止或挂起。采用按分钟计费制，用户可以“挂起”机器以暂停计算费用，仅需支付镜像存储费用。
*   **操作系统：** 支持用于确定性、可复现构建的 NixOS 以及 Ubuntu。两者均预装了 Docker、Python 和 AI 专用工具。
*   **网络：** 每个虚拟机在五个全球区域（美国、英国、欧盟和亚洲）均配有静态 IP 和自动 HTTPS 端点。

**智能体优先设计：**
machine0 因其契合 AI 驱动的工作流而脱颖而出。它集成了**模型上下文协议 (MCP)**，允许智能体通过编程方式管理基础设施。用户可以使用“配置方案 (profiles)”将凭据、环境变量和提示词直接注入虚拟机，并由 Claude Code 和 Codex 等工具自动识别。此外，专门的 `/create-machine` 技能允许大语言模型 (LLM) 根据自然语言提示生成并配置可复现的 NixOS 环境。

**价格：**
CPU 实例起售价为 0.013 美元/小时，GPU 实例起售价为 0.836 美元/小时。该平台还提供创建“黄金镜像”和快照的功能，支持用户瞬间克隆环境并消除配置漂移。

---

## 5. Cursor 发布 Origin：GitHub 替代方案

**原文标题**: Cursor launches Origin, GitHub alternative

**原文链接**: [https://cursor.com/changelog/origin-code-hosting](https://cursor.com/changelog/origin-code-hosting)

Cursor 宣布推出代码托管平台 **Origin**，作为 GitHub 的替代方案，目前正面向付费订阅用户开启早期 Beta 测试。Origin 采用“Agent 原生”设计，将代码库、拉取请求（PR）和 AI Agent 集成到一个统一的生态系统中，旨在实现大规模的 AI 驱动开发。

**核心功能与特性：**

*   **代码托管与 GitHub 同步：** 用户可以直接在 Origin 上托管代码库，或关联现有的 GitHub 账号。该平台支持实时双向同步，允许用户直接在 Cursor 中管理 GitHub 的 PR、评论和评审。虽然 GitHub 仍是同步项目的“权威源”，但 Origin 提供了一个镜像环境，以实现无缝交互。
*   **AI Agent 集成：** Origin 为 AI 交互进行了优化。AI Agent 可以浏览代码库、回答复杂问题、修改代码、更新 PR 并推送分支，从而将开发流程集中在 Cursor 环境内。
*   **应用生态系统与 CI/CD：** 该平台包含一个不断扩展的集成生态系统。目前的合作伙伴包括用于 PR 自动预览部署的 **Vercel**，以及用于 CI/CD 的 **Depot** 或 **Buildkite**。值得注意的是，这些工具可以运行现有的 GitHub Actions 工作流或原生流水线。
*   **精简化管理：** 新增的“Codebase”标签页允许用户创建代码库、管理访问权限并监控同步状态。每个组织都会为其托管项目获得一个自定义 URL（例如 `cursor.com/codebase/name`）。

Origin 目前正向所有付费方案用户发布（选择退出的企业组织除外）。这标志着 Cursor 从单一的代码编辑器向综合性托管和 AI 编排平台的重大转变。

---

## 6. Linux 7.3 提升了显存耗尽时的性能

**原文标题**: Linux 7.3 improves performance when running out of vRAM

**原文链接**: [https://pixelcluster.dev/VRAM-Overcommit/](https://pixelcluster.dev/VRAM-Overcommit/)

Linux 内核 7.3 对显存（VRAM）管理进行了显著改进，特别是针对系统如何处理游戏过度提交 GPU 显存的情况。传统上，显存耗尽会导致性能大幅下降或应用程序崩溃。此次更新旨在确保此类情况仅表现为性能问题，而非稳定性问题。

解决的一个关键技术障碍是命令提交期间的“内存不足”错误。此前，当多个进程竞争显存时，内核在尝试锁定和移动内存分配时经常会遇到“ABBA”死锁情况。内核以往并不会解决这些死锁，而是直接退出并返回错误，导致游戏崩溃。通过将 `drm_exec` 辅助库集成到 TTM（Linux 通用 GPU 显存管理层）中，内核现在利用“负伤-中止-重试”（wound-abort-retry）循环来安全地解决这些死锁，从而防止在高内存压力下发生崩溃。

在性能方面，本文强调了过度提交显存的物理限制。当数据被驱逐到系统内存时，GPU 必须通过 PCIe 总线获取数据。在 PCIe 4.0 x16 的速度下，每帧获取超过约 1GiB 的数据将无法维持 30 FPS。此外，性能下降通常还受到“乒乓”效应的影响，即相互竞争的应用程序（如游戏和合成器）不断驱逐并重新导入彼此的内存——特别是显示硬件所需的“扫描输出”缓冲区。

通过修复底层锁定机制并减少不必要的内存移动，Linux 7.3 确保了在显存耗尽时游戏仍能保持稳定。虽然由于硬件带宽限制，性能下降仍不可避免，但系统现在能更平稳地处理这些约束，防止了之前内核版本中常见的灾难性故障。

---

## 7. Python Polars Cheatsheet (based on our O'Reilly book)

**原文标题**: Python Polars Cheatsheet (based on our O'Reilly book)

**原文链接**: [https://opensource.posit.co/resources/cheatsheets/polars/](https://opensource.posit.co/resources/cheatsheets/polars/)

本文是 Python Polars 的全面指南。Polars 是一款专为快速、极具表现力的数据转换和分析而设计的高性能 DataFrame 库。Polars 基于 Apache Arrow 内存规范构建，提供双重 API：用于立即执行的**即时执行 API (eager API)** 和用于构建优化查询计划的**延迟执行 API (lazy API)**。这种延迟引擎支持高级优化，例如谓词下推 (predicate pushdown) 以及针对超内存数据集的外存流式处理 (out-of-core streaming)。

本指南概述了三种主要数据结构——**Series**、**DataFrames** 和 **LazyFrames**，并指出 Polars 优先采用不可变性和方法链模式，而非 pandas 等库中常见的行索引系统。

涵盖的关键技术操作包括：
*   **数据输入/输出 (Data I/O)：** 用于在 Parquet、CSV、JSON 和 Delta Lake 等格式间读取、扫描、写入和流式传输数据的函数。
*   **数据转换：** 使用表达式和选择器选择并创建列、过滤行以及排序数据。
*   **数据重塑：** 透视 (pivoting) 与逆透视 (unpivoting) 技术，展开 (exploding) 列表列，以及解构 (unnesting) 结构体。
*   **聚合：** 强大的分组工具，包括用于时间序列分析的动态和滚动窗口，以及使用 `.over()` 表达式的窗口函数。
*   **数据合并：** 多样的连接策略（包括内连接、左连接、全连接、半连接、反连接和 asof 连接）以及拼接方法（水平、垂直和对角线拼接）。

总之，Polars 被定位为一种现代化、高效的数据工程与分析工具。它利用“表达式”（操作树）来构建复杂的数据流水线，使这些流水线既具有高度的可读性，又在性能上经过了深度优化。

---

## 8. 我们已将防辐射背心送往月球并成功返回，实验证明其确实有效。

**原文标题**: We've flown a radiation-blocking vest to the Moon and back, and it worked

**原文链接**: [https://arstechnica.com/science/2026/08/weve-flown-a-radiation-blocking-vest-to-the-moon-and-back-and-it-worked/](https://arstechnica.com/science/2026/08/weve-flown-a-radiation-blocking-vest-to-the-moon-and-back-and-it-worked/)

StemRad, an Israeli-American startup, has successfully tested "AstroRad," a wearable radiation-shielding vest, aboard NASA’s uncrewed Artemis I mission. The vest offers a novel solution to the dangers of solar storms, which can cause radiation sickness and increase cancer risks for astronauts traveling to the Moon or Mars.

**Targeted Protection and Design**
Rather than shielding the entire spacecraft or the astronaut’s whole body—both of which are mass-prohibitive—AstroRad uses "targeted shielding." It prioritizes radiation-sensitive tissues, such as bone marrow, breasts, and reproductive organs. By protecting even a fraction of a person's bone marrow, the body can potentially regenerate blood cells and survive high-dose exposure. The vest is constructed from thousands of hexagonal high-density polyethylene (HDPE) rods, a material rich in hydrogen that effectively blocks protons. This "tessellated" design allows the vest to remain flexible, enabling astronauts to work and move freely.

**Mission Results**
During the flight, the vest was worn by a "phantom" torso named Zohar, while an unprotected phantom, Helga, served as a control. Although no solar storm occurred during the mission, researchers used data from the Van Allen radiation belts to simulate how the vest would perform during historical solar events. The simulations showed the vest could reduce radiation doses by 40% to 60%. This level of protection is comparable to the Orion spacecraft’s dedicated storm shelter but allows the crew to remain mobile and operational.

**Limitations and Future Development**
While effective against solar particles, the vest provides little protection against high-energy galactic cosmic rays. Furthermore, weight remains a challenge; the original vest weighed 26 kilograms. However, using Artemis I data, engineers have already reduced the weight to 16 kilograms without significantly compromising protection. This technology could potentially extend an astronaut’s career by nearly 200 days by keeping their lifetime radiation exposure within safe limits.

---

## 9. Teaching my kid to code with a modern MUD

**原文标题**: Teaching my kid to code with a modern MUD

**原文链接**: [https://tau.dev/2026/08/07/canon](https://tau.dev/2026/08/07/canon)

生成摘要时出错

---

## 10. Code-native generation of highly programmable 3D assets (2026)

**原文标题**: Code-native generation of highly programmable 3D assets (2026)

**原文链接**: [https://arxiv.org/abs/2607.22738](https://arxiv.org/abs/2607.22738)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 2 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 3 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 4 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 5 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 6 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 7 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 8 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 9 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 10 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 11 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 12 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 13 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 14 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 15 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 16 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 17 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 18 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 19 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 20 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 21 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 22 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 23 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 24 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 25 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 26 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 27 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 28 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 29 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 30 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 31 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 32 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 33 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 34 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 35 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 36 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 37 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 38 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 39 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 40 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 41 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 42 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 43 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 44 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 45 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 46 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 47 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 48 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 49 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 50 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 51 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 52 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 53 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 54 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 55 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 56 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 57 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 58 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 59 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 60 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 61 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 62 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 63 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 64 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 65 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 66 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 67 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 68 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 69 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 70 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 71 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 72 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 73 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 74 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 75 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 76 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 77 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 78 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 79 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 80 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 81 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 82 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 83 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 84 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 85 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 86 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 87 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 88 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 89 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 90 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 91 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 92 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 93 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 94 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 95 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 96 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 97 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 98 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 99 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 100 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 101 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 102 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 103 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 104 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 105 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 106 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 107 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 108 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 109 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 110 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 111 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 112 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 113 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 114 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 115 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 116 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 117 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 118 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 119 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 120 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 121 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 122 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 123 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 124 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 125 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 126 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 127 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 128 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 129 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 130 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 131 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 132 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 133 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 134 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 135 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 136 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 137 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 138 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 139 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 140 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 141 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 142 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 143 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 144 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 145 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 146 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 147 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 148 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 149 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 150 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 151 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 152 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 153 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 154 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 155 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 156 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 157 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 158 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 159 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 160 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 161 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 162 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 163 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 164 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 165 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 166 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 167 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 168 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 169 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 170 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 171 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 172 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 173 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 174 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 175 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 176 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 177 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 178 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 179 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 180 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 181 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 182 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 183 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 184 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 185 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 186 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 187 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 188 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 189 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 190 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 191 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 192 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 193 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 194 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 195 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 196 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 197 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 198 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 199 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 200 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 201 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 202 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 203 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 204 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 205 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 206 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 207 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 208 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 209 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 210 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 211 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 212 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 213 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 214 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 215 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 216 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 217 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 218 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 219 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 220 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 221 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 222 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 223 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 224 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 225 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 226 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 227 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 228 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 229 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 230 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 231 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 232 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 233 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 234 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 235 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 236 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 237 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 238 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 239 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 240 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 241 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 242 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 243 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 244 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 245 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 246 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 247 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 248 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 249 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 250 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 251 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 252 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 253 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 254 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 255 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 256 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 257 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 258 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 259 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 260 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 261 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 262 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 263 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 264 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 265 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 266 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 267 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 268 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 269 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 270 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 271 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 272 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 273 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 274 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 275 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 276 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 277 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 278 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 279 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 280 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 281 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 282 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 283 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 284 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 285 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 286 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 287 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 288 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 289 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 290 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 291 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 292 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 293 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 294 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 295 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 296 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 297 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 298 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 299 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 300 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 301 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 302 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 303 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 304 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 305 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 306 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 307 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 308 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 309 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 310 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 311 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 312 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 313 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 314 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 315 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 316 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 317 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 318 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 319 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 320 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 321 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 322 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 323 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 324 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 325 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 326 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 327 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 328 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 329 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 330 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 331 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 332 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 333 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 334 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 335 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 336 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 337 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 338 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 339 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 340 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 341 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 342 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 343 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 344 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 345 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 346 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 347 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 348 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 349 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 350 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 351 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 352 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 353 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 354 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 355 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 356 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 357 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 358 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 359 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 360 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 361 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 362 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 363 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 364 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 365 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 366 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 367 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 368 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 369 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 370 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 371 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 372 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 373 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 374 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 375 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 376 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 377 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 378 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 379 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 380 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 381 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 382 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 383 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 384 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 385 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 386 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 387 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 388 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 389 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 390 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 391 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 392 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 393 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 394 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 395 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 396 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 397 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 398 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 399 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 400 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 401 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 402 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 403 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 404 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 405 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 406 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 407 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 408 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 409 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 410 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 411 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 412 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 413 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 414 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 415 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 416 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 417 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 418 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 419 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 420 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 421 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 422 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 423 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 424 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 425 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 426 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 427 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 428 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 429 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 430 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 431 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 432 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 433 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 434 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 435 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 436 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 437 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 438 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 439 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 440 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 441 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 442 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 443 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 444 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 445 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 446 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 447 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 448 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 449 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 450 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 451 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 452 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 453 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 454 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 455 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 456 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 457 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 458 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 459 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 460 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 461 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 462 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 463 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 464 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 465 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 466 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 467 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 468 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 469 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 470 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 471 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 472 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 473 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 474 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 475 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 476 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 477 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 478 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 479 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 480 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 481 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 482 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 483 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 484 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 485 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 486 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 487 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 488 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 489 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 490 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 491 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 492 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 493 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 494 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 495 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 496 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 497 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 498 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 499 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 500 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 501 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 502 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 503 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 504 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 505 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 506 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 507 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 508 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 509 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 510 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 511 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 512 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 513 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 514 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 515 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
