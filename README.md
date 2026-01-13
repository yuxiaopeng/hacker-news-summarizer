# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-01-13.md)

*最后自动更新时间: 2026-01-13 17:55:39*
## 1. 郁金香创意计算机

**原文标题**: The Tulip Creative Computer

**原文链接**: [https://github.com/shorepine/tulipcc](https://github.com/shorepine/tulipcc)

**Tulip 创意计算机 (Tulip CC)** 是一款便携、低功耗且价格亲民的设备，专为音乐、图形、编程和写作而设计。它搭载 ESP32-S3 芯片并运行 MicroPython，提供了一个无干扰的实时环境，开机即可瞬间进入 Python 提示符界面。

**关键技术特性：**
*   **性能与存储：** 配备 8.5MB RAM 和 32MB 闪存。系统支持 1024x600 电容式触摸屏，并针对低功耗进行了优化，依靠锂聚合物电池可运行数小时。
*   **音频合成：** 核心亮点是集成了支持 120 音色的 AMY 合成引擎，支持调频 (FM)、加法和减法合成，并配有音序器和模拟风格滤波器。它还内置了硬件 MIDI 输入和输出接口。
*   **图形系统：** GPU 负责处理文本层（支持 ANSI 颜色）、高分辨率滚动背景缓冲区，以及多达 32 个支持碰撞检测的硬件精灵 (Sprites)。
*   **连接性：** Tulip 提供用于网络访问（HTTP/sockets）的 WiFi，支持键盘和 MIDI 控制器的 USB 接口，以及用于外接传感器和硬件模块的 I2C 接口。

**软件与社区：**
Tulip 内置了文本编辑器和“Tulip World”（一个原生的 BBS 聊天室和文件共享区）。该系统完全开源，用户可以通过三种形式体验：专用 Tulip CC 硬件（通过 Makerfabs 购买售价 59 美元，或自行 DIY 组装）、网页版，以及适用于 Mac 和 Linux 的桌面应用程序。

Tulip 专为初学者和资深创客设计，是一个独立的“创意计算机”，适合任何希望在专用硬件环境中构建游戏、合成音乐或进行 Python 实验的人。

---

## 2. Show HN: DebtBomb – 让 TODO 过期并自动创建 Jira 工单

**原文标题**: Show HN: DebtBomb – Make TODOs expire and automatically create Jira tickets

**原文链接**: [https://github.com/jobin-404/debtbomb](https://github.com/jobin-404/debtbomb)

**DebtBomb** 是一款跨语言工具，旨在通过对源代码注释强制执行过期日期，防止技术债无限期累积。它解决了“临时”变通方案（如 `TODO` 或 `FIXME` 标记）在代码库中被遗忘并逐渐腐烂的常见问题。

通过在注释中使用 `@debtbomb` 标签，开发者可以为代码附加特定的过期日期、负责人和原因。该工具的核心功能是通过 `debtbomb check` 命令集成到 CI/CD 流水线中。如果某个“债务炸弹”达到过期日期，工具将触发构建失败，迫使团队要么解决该项债务，要么有意识地延长截止日期。

**核心特性包括：**
*   **CI 强制执行：** 到期即导致构建失败，以确保可见性。
*   **预警窗口：** 通过 `--warn-in-days` 标志，团队可以在不立即阻塞发布的情况下，提前获知即将过期的债务。
*   **聚合报告：** 生成按负责人、模块和紧急程度（如：已过期 vs. 30 天内过期）分类的摘要报告。
*   **语言无关：** 支持多种注释风格（`//`、`#`、`--`、`/* */`），使其兼容几乎任何编程语言。
*   **智能扫描：** 自动忽略非人工编写的文件（如 `node_modules`、压缩后的代码和二进制文件），并支持通过 `.debtbombignore` 文件进行自定义排除。

DebtBomb 作为一个采用 MIT 许可证开源的 Go 软件包，将技术债从被动的文档记录转变为主动的、有时间限制的强制约束。

---

## 3. 2025年，太阳能与电池为我们节省了多少

**原文标题**: What a year of solar and batteries saved us in 2025

**原文链接**: [https://scotthelme.co.uk/what-a-year-of-solar-and-batteries-really-saved-us-in-2025/](https://scotthelme.co.uk/what-a-year-of-solar-and-batteries-really-saved-us-in-2025/)

在这份2025年度回顾中，一位英国房主对其家庭能源系统的表现进行了评估。该系统由4.2kWp太阳能电池阵列和三台特斯拉Powerwall 2电池组成。尽管由于两辆电动汽车、家庭服务器和热水浴缸的使用，家庭用电需求极高（每年17.3 MWh），但该系统显著减轻了其经济负担。

**关键财务与能源数据：**
*   **能源平衡：** 家庭购电量为20.1 MWh，售电量为6.0 MWh，太阳能发电量为3.2 MWh。
*   **成本节约：** 通过利用智能电价方案（Octopus Energy），他们实现了“负荷转移”——在£0.07/kWh的谷值电价时段为电池充电，从而避开了£0.28/kWh的峰值电价。
*   **净成本：** 全年净电费总额为£557.37，实际电价仅为£0.03/kWh。如果没有该系统，预计成本将超过£3,632，相当于每年节省了£3,078。
*   **出口收益：** 6月份激活的出口电价方案允许房主以£0.15/kWh的价格出售多余能源。在夏季高峰月份，这部分收入完全抵消了用电支出，产生了负电费账单。

**投资展望：**
系统总安装成本为£39,360。根据2025年的数据，该投资的年回报率为9%，预计回本周期约为11年。除了财务收益外，房主还强调了停电保护带来的附加价值。

展望2026年，作者预期通过全年的出口积分和优化的Home Assistant自动化系统，实现年度净电费为零的目标。

---

## 4. 苹果创作者工作室

**原文标题**: Apple Creator Studio

**原文链接**: [https://www.apple.com/newsroom/2026/01/introducing-apple-creator-studio-an-inspiring-collection-of-creative-apps/](https://www.apple.com/newsroom/2026/01/introducing-apple-creator-studio-an-inspiring-collection-of-creative-apps/)

Apple 宣布推出 **Apple Creator Studio**，这是一款将于 2026 年 1 月 28 日发布的全面创意订阅套装。该服务专为专业人士和学生设计，整合了 Apple 多款最强大的工具，包括 Final Cut Pro、Logic Pro、Pixelmator Pro、Motion、Compressor 和 MainStage，同时通过优质内容和生成式 AI 增强了 Keynote 和 Pages 等生产力应用。

其主要亮点是跨生态系统集成的先进 **AI 驱动功能**：
*   **Final Cut Pro：** 引入了“转写”和“视觉搜索”以快速定位素材，“节拍检测”用于节奏感剪辑，以及 iPad 专属的“蒙太奇制作器 (Montage Maker)”，利用 AI 自动剪辑片段。
*   **Logic Pro：** 增加了用于逼真电子乐演奏的 AI“合成器乐手 (Synth Player)”以及“和弦识别 (Chord ID)”功能，后者可将音频或 MIDI 自动转录为和弦进行。
*   **Pixelmator Pro：** 这款屡获殊荣的图像编辑器首次登陆 iPad，提供针对触摸优化的界面并支持 Apple Pencil 全功能，同时包含“超分辨率”和全新的“变形”工具等 AI 工具。

该套装还推出了 **内容枢纽 (Content Hub)**，这是一个为 Keynote、Pages 和 Numbers 提供的精选媒体素材库，同时配备了可根据文本生成图像的生成式 AI 工具。

**价格与上市时间：**
Apple Creator Studio 的订阅价格为 **每月 12.99 美元或每年 129 美元**，学生和教职员工可享受每月 2.99 美元的优惠价。虽然该订阅支持跨平台访问（Mac、iPad 和 iPhone），但 Apple 将继续为偏好传统所有权模式的用户提供专业应用的 Mac 独立版本，可供一次性购买。

---

## 5. Cowork：将 Claude Code 用于你的其他工作

**原文标题**: Cowork: Claude Code for the rest of your work

**原文链接**: [https://claude.com/blog/cowork-research-preview](https://claude.com/blog/cowork-research-preview)

Anthropic 发布了 **Cowork**，这是一个旨在将“Claude Code”的高自主性能力带给普通用户的功能预览版。订阅了 Claude Max 的 macOS 用户可通过应用程序使用 Cowork，该功能允许用户授予 AI 访问特定本地文件夹的权限，使其能够直接在电脑上读取、编辑、创建和整理文件。

与标准的对话式 AI 不同，Cowork 具有显著的自主运行能力。其核心功能包括：

*   **任务执行：** 它可以处理复杂的整理任务，例如重命名下载文件、将截图中的数据提取到电子表格中，或根据零散的笔记起草报告。
*   **工作流效率：** 用户可以并行排队多个任务，从传统的来回对话模式转变为“同事”模式，由 AI 稳步执行预定计划。
*   **扩展技能：** 该工具集成了现有连接器以及用于生成文档和演示文稿的新“技能”。配合 Chrome 浏览器中的 Claude 使用时，它还可以执行基于浏览器的任务。

**安全与控制**
用户可以严格控制 Cowork 访问哪些文件夹和连接器。虽然 Claude 在执行重大操作时需要获得许可，但文中指出，如果收到指令，AI 可能会执行破坏性操作（如删除文件）。用户还需警惕“提示词注入”风险——即外部网页内容尝试恶意篡改 AI 计划的行为，这仍是安全研究的一个活跃领域。

**可用性**
Cowork 目前作为研究预览版提供给 macOS 平台的 Claude Max 订阅用户，旨在收集有关自主代理使用情况的反馈。Anthropic 计划在未来的更新中推出 Windows 支持、跨设备同步以及增强的安全功能。

---

## 6. 斯科特·亚当斯逝世

**原文标题**: Scott Adams has died

**原文链接**: [https://www.usatoday.com/story/entertainment/celebrities/2026/01/13/scott-adams-dead-dilbert-creator-prostate-cancer/88158828007/](https://www.usatoday.com/story/entertainment/celebrities/2026/01/13/scott-adams-dead-dilbert-creator-prostate-cancer/88158828007/)

《呆伯特》（Dilbert）连环漫画创作者斯科特·亚当斯（Scott Adams）在与前列腺癌抗争后去世，享年68岁。2026年1月13日，他的前妻谢莉·迈尔斯（Shelly Miles）在其节目《与斯科特·亚当斯一起喝真咖啡》（Real Coffee with Scott Adams）的直播中确认了他的死讯。亚当斯此前曾透露，他的癌症已经扩散到骨骼，且已处于晚期。

亚当斯凭借1989年首发的《呆伯特》享誉国际，该漫画以讽刺企业办公文化的荒诞而著称。在事业巅峰时期，这部漫画在全球2000多家报纸上连载，并于1997年为亚当斯赢得了享有盛誉的鲁本奖（Reuben Award）。

然而，2023年，由于他在YouTube直播中发表了种族主义言论，导致大多数主流报纸纷纷停刊其漫画，他的声誉也因此变得两极分化。争议发生后，亚当斯将《呆伯特》转移到了一个订阅制的网络平台。

在元旦写下并由迈尔斯代读的最后遗言中，亚当斯透露他最近已皈依耶稣基督。他对自己的作品感到自豪，表示自己为生命“倾尽了所有”，并请求追随者们要“传递爱心”，努力“做一个有用的人”，以此作为他留给世人的持久遗产。

---

## 7. Legion Health (YC S21) 招聘顶级创始工程师，负责 AI 原生运营

**原文标题**: Legion Health (YC S21) Hiring Cracked Founding Eng for AI-Native Ops

**原文链接**: [https://jobs.ashbyhq.com/legionhealth/ffdd2b52-eb21-489e-b124-3c0804231424](https://jobs.ashbyhq.com/legionhealth/ffdd2b52-eb21-489e-b124-3c0804231424)

Legion Health 是一家由 Y Combinator (S21) 支持的初创公司，目前正招聘一名**创始工程师**，负责领导其 **AI 原生运营基础设施 (AI-Native Ops Infrastructure)** 的开发。

该公司展现出强劲的市场增长势头和财务稳定性，目前**年度经常性收入 (ARR) 已超过 300 万美元**，累计融资总额达 **700 万美元**。

**该职位的关键信息包括：**
*   **角色：** 创始工程师，专注于构建大规模、AI 集成的运营系统。
*   **理想人选：** 该职位寻求一名“顶级 (cracked)”工程师——这是行业内对能够处理复杂基础设施并适应初创公司快速节奏的顶尖、高效开发者的简称。
*   **核心重点：** 职位以“AI 原生运营”为中心，表明公司正超越简单的 AI 应用，致力于构建以人工智能为核心组件的基础设施。

该职位提供了加入一家已验证产品市场契合度 (PMF) 且处于增长阶段的医疗科技公司的机会，具备初创团队成员典型的高影响力工作环境。

---

## 8. Influencers and OnlyFans models are dominating U.S. O-1 visa requests

**原文标题**: Influencers and OnlyFans models are dominating U.S. O-1 visa requests

**原文链接**: [https://www.theguardian.com/us-news/2026/jan/11/onlyfans-influencers-us-o-1-visa](https://www.theguardian.com/us-news/2026/jan/11/onlyfans-influencers-us-o-1-visa)

生成摘要时出错

---

## 9. Text-based web browsers

**原文标题**: Text-based web browsers

**原文链接**: [https://cssence.com/2026/text-based-web-browsers/](https://cssence.com/2026/text-based-web-browsers/)

生成摘要时出错

---

## 10. Show HN: An iOS budget app I've been maintaining since 2011

**原文标题**: Show HN: An iOS budget app I've been maintaining since 2011

**原文链接**: [https://primoco.me/en/](https://primoco.me/en/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 2 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 3 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 4 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 5 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 6 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 7 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 8 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 9 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 10 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 11 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 12 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 13 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 14 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 15 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 16 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 17 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 18 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 19 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 20 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 21 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 22 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 23 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 24 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 25 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 26 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 27 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 28 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 29 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 30 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 31 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 32 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 33 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 34 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 35 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 36 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 37 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 38 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 39 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 40 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 41 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 42 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 43 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 44 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 45 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 46 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 47 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 48 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 49 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 50 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 51 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 52 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 53 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 54 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 55 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 56 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 57 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 58 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 59 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 60 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 61 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 62 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 63 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 64 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 65 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 66 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 67 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 68 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 69 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 70 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 71 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 72 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 73 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 74 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 75 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 76 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 77 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 78 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 79 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 80 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 81 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 82 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 83 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 84 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 85 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 86 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 87 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 88 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 89 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 90 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 91 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 92 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 93 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 94 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 95 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 96 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 97 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 98 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 99 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 100 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 101 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 102 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 103 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 104 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 105 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 106 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 107 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 108 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 109 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 110 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 111 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 112 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 113 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 114 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 115 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 116 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 117 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 118 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 119 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 120 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 121 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 122 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 123 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 124 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 125 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 126 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 127 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 128 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 129 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 130 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 131 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 132 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 133 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 134 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 135 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 136 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 137 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 138 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 139 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 140 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 141 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 142 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 143 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 144 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 145 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 146 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 147 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 148 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 149 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 150 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 151 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 152 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 153 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 154 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 155 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 156 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 157 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 158 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 159 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 160 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 161 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 162 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 163 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 164 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 165 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 166 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 167 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 168 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 169 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 170 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 171 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 172 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 173 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 174 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 175 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 176 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 177 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 178 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 179 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 180 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 181 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 182 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 183 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 184 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 185 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 186 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 187 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 188 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 189 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 190 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 191 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 192 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 193 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 194 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 195 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 196 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 197 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 198 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 199 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 200 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 201 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 202 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 203 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 204 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 205 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 206 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 207 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 208 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 209 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 210 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 211 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 212 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 213 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 214 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 215 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 216 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 217 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 218 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 219 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 220 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 221 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 222 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 223 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 224 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 225 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 226 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 227 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 228 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 229 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 230 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 231 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 232 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 233 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 234 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 235 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 236 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 237 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 238 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 239 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 240 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 241 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 242 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 243 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 244 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 245 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 246 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 247 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 248 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 249 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 250 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 251 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 252 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 253 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 254 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 255 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 256 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 257 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 258 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 259 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 260 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 261 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 262 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 263 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 264 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 265 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 266 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 267 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 268 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 269 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 270 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 271 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 272 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 273 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 274 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 275 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 276 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 277 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 278 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 279 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 280 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 281 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 282 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 283 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 284 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 285 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 286 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 287 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 288 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 289 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 290 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 291 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 292 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 293 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 294 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 295 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 296 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 297 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 298 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 299 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
