# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-12-20.md)

*最后自动更新时间: 2025-12-20 17:44:03*
## 1. 尽管自托管 Postgres

**原文标题**: Go ahead, self-host Postgres

**原文链接**: [https://pierce.dev/notes/go-ahead-self-host-postgres#user-content-fn-1](https://pierce.dev/notes/go-ahead-self-host-postgres#user-content-fn-1)

文章《尽管去自托管 Postgres 吧》(Go ahead, self-host Postgres) 挑战了现代行业的教条，即托管数据库服务（如 AWS RDS）是必不可少的。作者认为，对自托管的恐惧是云服务商推行的一种叙事，目的是为其对本质上是开源软件的产品收取的巨额溢价提供正当理由。

**自托管的理由：**
*   **成本效益：** 云服务的定价已变得极具侵略性。以中端 RDS 实例的价格，用户可以租用一台 CPU 和内存配置显著更高的专用服务器。
*   **性能：** 自托管允许对托管服务通常锁定的参数（如内存界限和 NVMe 存储优化）进行细粒度调优。作者指出，在迁移到专用服务器后，查询延迟降低了 20%。
*   **运维简单：** 作者声称，包括备份、安全更新和监控在内的维护工作每月仅需 30 到 60 分钟。虽然自托管将事故响应的责任转移给了用户，但作者指出，托管服务也会发生故障，且往往让用户缺乏解决问题的工具。

**成功的技术关键：**
作者为那些准备切换的用户强调了几个关键的配置领域：
*   **内存：** 手动调优 `shared_buffers` 和 `effective_cache_size`，而不是依赖默认的 Docker 设置。
*   **连接：** 使用 PgBouncer 等连接池工具来管理开销。
*   **存储：** 调整 `random_page_cost` 以反映现代 NVMe SSD 的速度。

**结论：**
虽然托管服务仍推荐给完全的初学者、具有特殊规模的大型企业或受严格监管的行业（如 PCI/HIPAA），但作者认为，大多数团队都处于一个“甜蜜点”，即自托管既快速、稳定，又便宜得多。他鼓励任何每月为 RDS 支付超过 200 美元的人尝试进行自托管迁移。

---

## 2. 日志级别 ‘error’ 应当意味着有某些问题需要修复。

**原文标题**: Log level 'error' should mean that something needs to be fixed

**原文链接**: [https://utcc.utoronto.ca/~cks/space/blog/programming/ErrorsShouldRequireFixing](https://utcc.utoronto.ca/~cks/space/blog/programming/ErrorsShouldRequireFixing)

这篇文章由 Chris Siebenmann 撰写于 2025 年 2 月 17 日，解释了其博客 *Wandering Thoughts* 的部分访问者被阻止访问的原因。

主要核心观点包括：

*   **反爬虫措施：** 由于旨在抓取大语言模型（LLM）训练数据的高流量爬虫大幅增加，作者实施了严格的屏蔽措施。
*   **针对旧版浏览器：** 系统专门屏蔽了“版本过旧且可疑”的浏览器，特别是自动化爬虫经常使用的旧版 Chrome 浏览器。
*   **存档服务的问题：** `archive.today` 及其变体（如 `.is`、`.ph` 等）目前已被屏蔽。作者指出，这些服务使用旧版 Chrome 的 User-Agent 字符串，并伪造反向 DNS 记录以冒充 Googlebot，导致系统无法将其与恶意攻击者区分开来。
*   **推荐替代方案：** 建议用户改用 `archive.org` (Internet Archive)，因为它是一个行为规范、能正确识别自身身份的爬虫。
*   **解决误报：** 若合法用户被误屏蔽，可联系作者的大学邮箱并提供具体的 User-Agent 字符串，以协助优化屏蔽标准。

*（注：虽然提示中的标题提到了日志级别，但提供的内容完全侧重于浏览器屏蔽和反爬虫措施。）*

---

## 3. Gemini 3 Pro 对决 2.5 Pro：宝可梦 水晶版

**原文标题**: Gemini 3 Pro vs. 2.5 Pro in Pokemon Crystal

**原文链接**: [https://blog.jcz.dev/gemini-3-pro-vs-25-pro-in-pokemon-crystal](https://blog.jcz.dev/gemini-3-pro-vs-25-pro-in-pokemon-crystal)

无法访问文章链接。

---

## 4. Immersa：基于 Web 的开源 3D 演示工具

**原文标题**: Immersa: Open-source Web-based 3D Presentation Tool

**原文链接**: [https://github.com/ertugrulcetin/immersa](https://github.com/ertugrulcetin/immersa)

**Immersa** 是一款开源的网页版演示工具，旨在创建沉浸式的 3D 演示文稿。与传统的 2D 幻灯片软件不同，Immersa 允许用户在三维空间中排列 3D 模型 (.glb)、图像和 3D 文本。

该工具的核心亮点是其**基于插值的动画系统**。当用户复制幻灯片并修改物体的坐标、旋转或缩放时，Immersa 会在演示过程中自动生成这些状态之间的平滑过渡动画。

**核心特性：**
*   **3D 场景编辑器：** 包含一个带有相机控制和物体操作手柄（gizmos）的完整视口。
*   **内容支持：** 无缝导入 .glb 模型、标准图像格式（JPG/PNG）以及可定制的 3D 文本。
*   **本地存储：** 所有数据通过 IndexedDB 存储在浏览器本地，确保了隐私和持久性，且无需强制注册云端账户。
*   **工作流工具：** 功能包括撤销/重做、键盘快捷键（例如“D”用于复制，“T”用于文本），以及将演示文稿导出为 .edn 文件的能力。

**技术栈：**
该项目由 Ertuğrul Çetin 开发，使用 **ClojureScript**、**Re-frame** 以及用于 3D 渲染的 **Babylon.js** 构建。本地编译需要 Node.js 和 Java (JDK 11+)，并采用 MIT 许可证开源。

Immersa 提供了现代化的深色主题界面，非常适合希望超越静态幻灯片、追求动态空间叙事的创作者。

---

## 5. 纯硅 Demo 编程：无 CPU，无内存，仅 4k 逻辑门

**原文标题**: Pure Silicon Demo Coding: No CPU, No Memory, Just 4k Gates

**原文链接**: [https://www.a1k0n.net/2025/12/19/tiny-tapeout-demo.html](https://www.a1k0n.net/2025/12/19/tiny-tapeout-demo.html)

本文详细介绍了为 Tiny Tapeout 8 竞赛开发定制 ASIC Demo 的过程。该设计受限于约 4,000 个逻辑门，且**不包含 CPU、RAM 或 ROM**。设计输出为 2 位 RGB VGA 视频和 1 位音频，所有状态均存储在耗电的触发器中。

由于在没有内存的情况下无法使用数据压缩等传统“尺寸编码”（sizecoding）技巧，作者通过降低**算法复杂度**来优化设计。关键技术实现包括：

*   **正弦滚动条：** 为避免占用大量内存的查找表，设计采用“辛积分器”（向量旋转），通过简单的移位和加法计算每像素和每帧的数值，从而生成正弦波。
*   **3D 棋盘格：** 作者实现了不恢复余数除法算法来进行实时透视变换，将屏幕坐标投影到 3D 平面上。
*   **基于逻辑的数据：** 文本和音乐被直接编码到逻辑门阵列中。由于综合工具会将真值表转换为逻辑门，设计采用了重复的“ABAC”音乐模式和 2 的幂次方字符间距，以便编译器简化硬件需求。
*   **视觉与音频：** Demo 中的星空由线性反馈移位寄存器（LFSR）驱动，1 位音频通过 Σ-Δ 转换生成，作者发现这比 PWM 更易于实现。

该项目在固化至 Skywater 130nm 工艺之前，使用 Verilator 仿真和 OrangeCrab FPGA 进行了原型设计。最终设计使用了 3,374 个单元和 293 个触发器，几乎填满了芯片区域的每一平方纳米。这一成果凸显了 ASIC 设计的独特约束：虽然状态和变化非常“昂贵”，但重复模式和数学捷径基本上是“免费”的。

---

## 6. NIST 博尔德分部的 NTP 服务已断电

**原文标题**: NTP at NIST Boulder Has Lost Power

**原文链接**: [https://lists.nanog.org/archives/list/nanog@lists.nanog.org/message/ACADD3NKOG2QRWZ56OSNNG7UIEKKTZXL/](https://lists.nanog.org/archives/list/nanog@lists.nanog.org/message/ACADD3NKOG2QRWZ56OSNNG7UIEKKTZXL/)

由于极端强风以及为预防山火而采取的预防性停电，美国国家标准与技术研究院（NIST）博尔德分部的原子系综时间尺度在经历长时间电力中断后已宣告失效。此次停电始于2025年12月17日，导致位于博尔德的互联网时间服务（NTP）数据变得不准确。

NIST的杰夫·谢尔曼（Jeff Sherman）报告称，虽然部分服务器在备用电源支持下仍可访问，但他正努力将其禁用，以防止错误的时间数据外泄。受影响的服务器包括 time-a-b.nist.gov 至 time-e-b.nist.gov 以及经过身份验证的 ntp-b.nist.gov。

在关键备用发电机发生故障并影响了主信号分配链后，事态进一步恶化。目前的紧急救援重点是在电池备用电源耗尽之前，为氢原子钟确保替代电源。

由于场地关闭和员工进入受限，目前尚无法评估维修完成的具体时间。不过，位于另一栋校区建筑内并由不同发电机支持的其他时钟可能幸存，这将使 NIST 在电力恢复后无需依赖外部参考信号，即可重新校准主时间尺度。

---

## 7. Skills 正式登陆 Codex

**原文标题**: Skills Officially Comes to Codex

**原文链接**: [https://developers.openai.com/codex/skills/](https://developers.openai.com/codex/skills/)

Codex 官方推出了 **Agent Skills**（智能体技能），该功能允许用户通过特定任务的工作流来扩展 AI 的能力。一项“技能”是一个包含 `SKILL.md` 文件（提供指令和元数据）以及可选脚本、文档和资产的软件包。

**功能与调用**
技能利用“渐进式披露”来高效管理上下文；Codex 最初仅加载可用技能的名称和描述。可以通过两种方式激活技能：
*   **显式调用：** 通过使用 `/skills` 斜杠命令，或在 CLI、IDE 中输入 `$` 来引用技能。
*   **隐式调用：** 当 Codex 自动检测到用户的任务与某项技能的描述匹配时。

**存储与范围**
技能存储在不同的位置，Codex 遵循特定的优先级层次结构。如果两个技能同名，优先级较高位置的版本将覆盖其他版本。优先级（从高到低）如下：
1.  **REPO（仓库）：** 本地文件夹、父目录或 git 仓库根目录。
2.  **USER（用户）：** 用户的个人主目录。
3.  **ADMIN（管理员）：** 用于共享自动化的全系统位置。
4.  **SYSTEM（系统）：** 直接随 Codex 捆绑的默认技能。

**创建与安装**
用户可以通过整理文件夹手动创建技能，也可以使用内置的 `$skill-creator` 技能自动创建。为了扩展技能库，用户可以使用 `$skill-installer` 从 GitHub 下载精选技能，例如 Linear 或 Notion 的集成。Codex 还附带了如 `$plan` 等内部技能，用于协助研究和构建复杂的开发任务。

---

## 8. Privacy doesn't mean anything anymore, anonymity does

**原文标题**: Privacy doesn't mean anything anymore, anonymity does

**原文链接**: [https://servury.com/blog/privacy-is-marketing-anonymity-is-architecture/](https://servury.com/blog/privacy-is-marketing-anonymity-is-architecture/)

生成摘要时出错

---

## 9. CSS Grid Lanes

**原文标题**: CSS Grid Lanes

**原文链接**: [https://webkit.org/blog/17660/introducing-css-grid-lanes/](https://webkit.org/blog/17660/introducing-css-grid-lanes/)

生成摘要时出错

---

## 10. Reflections on AI at the End of 2025

**原文标题**: Reflections on AI at the End of 2025

**原文链接**: [https://antirez.com/news/157](https://antirez.com/news/157)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 2 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 3 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 4 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 5 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 6 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 7 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 8 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 9 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 10 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 11 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 12 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 13 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 14 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 15 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 16 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 17 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 18 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 19 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 20 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 21 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 22 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 23 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 24 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 25 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 26 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 27 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 28 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 29 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 30 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 31 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 32 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 33 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 34 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 35 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 36 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 37 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 38 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 39 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 40 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 41 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 42 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 43 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 44 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 45 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 46 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 47 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 48 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 49 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 50 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 51 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 52 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 53 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 54 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 55 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 56 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 57 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 58 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 59 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 60 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 61 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 62 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 63 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 64 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 65 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 66 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 67 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 68 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 69 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 70 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 71 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 72 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 73 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 74 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 75 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 76 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 77 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 78 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 79 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 80 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 81 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 82 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 83 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 84 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 85 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 86 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 87 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 88 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 89 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 90 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 91 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 92 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 93 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 94 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 95 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 96 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 97 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 98 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 99 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 100 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 101 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 102 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 103 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 104 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 105 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 106 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 107 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 108 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 109 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 110 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 111 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 112 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 113 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 114 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 115 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 116 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 117 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 118 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 119 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 120 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 121 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 122 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 123 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 124 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 125 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 126 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 127 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 128 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 129 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 130 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 131 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 132 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 133 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 134 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 135 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 136 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 137 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 138 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 139 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 140 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 141 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 142 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 143 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 144 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 145 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 146 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 147 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 148 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 149 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 150 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 151 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 152 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 153 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 154 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 155 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 156 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 157 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 158 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 159 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 160 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 161 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 162 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 163 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 164 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 165 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 166 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 167 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 168 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 169 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 170 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 171 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 172 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 173 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 174 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 175 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 176 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 177 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 178 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 179 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 180 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 181 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 182 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 183 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 184 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 185 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 186 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 187 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 188 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 189 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 190 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 191 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 192 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 193 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 194 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 195 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 196 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 197 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 198 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 199 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 200 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 201 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 202 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 203 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 204 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 205 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 206 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 207 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 208 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 209 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 210 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 211 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 212 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 213 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 214 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 215 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 216 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 217 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 218 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 219 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 220 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 221 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 222 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 223 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 224 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 225 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 226 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 227 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 228 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 229 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 230 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 231 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 232 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 233 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 234 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 235 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 236 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 237 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 238 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 239 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 240 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 241 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 242 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 243 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 244 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 245 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 246 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 247 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 248 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 249 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 250 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 251 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 252 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 253 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 254 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 255 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 256 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 257 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 258 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 259 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 260 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 261 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 262 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 263 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 264 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 265 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 266 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 267 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 268 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 269 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 270 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 271 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 272 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 273 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 274 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 275 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
