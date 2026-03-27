# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-03-27.md)

*最后自动更新时间: 2026-03-27 18:15:39*
## 1. .claude/ 文件夹剖析

**原文标题**: Anatomy of the .claude/ folder

**原文链接**: [https://blog.dailydoseofds.com/p/anatomy-of-the-claude-folder](https://blog.dailydoseofds.com/p/anatomy-of-the-claude-folder)

本文探讨了 `.claude/` 文件夹，它是 Claude Code 的“控制中心”，允许开发者超越默认的 AI 行为，打造一个深度集成的工程伙伴。配置分为两个层级：**项目级**（提交到 Git 以实现团队统一规则）和**全局主目录**（`~/.claude/`，用于个人偏好和会话历史）。

其结构的核心组件包括：

*   **CLAUDE.md & CLAUDE.local.md：** 核心指令手册，定义了构建/测试命令、架构和规范。使用 `.local.md` 进行个人配置覆盖，且不会被提交到仓库。
*   **rules/ 文件夹：** 将大型项目的指令模块化。通过使用 YAML frontmatter，规则可以实现**路径作用域限制**，即仅当 Claude 在特定目录中工作时才会激活。
*   **commands/ 文件夹：** 支持自定义斜杠命令（例如 `/project:review`）。这些命令利用 Shell 命令执行（`!`）将实时数据（如 git diffs 或 GitHub issues）直接注入提示词。
*   **skills/ 文件夹：** 定义当任务匹配技能描述时，Claude 可以**自动**调用的工作流。技能是“包”，可以包含多个支撑性参考文件。
*   **agents/ 文件夹：** 定义专门的子智能体角色（例如安全审计员），具备受限的工具访问权限和特定的模型偏好，以便在隔离的上下文窗口中处理复杂任务。
*   **settings.json：** 安全与权限层。它使用**允许/拒绝列表**来控制哪些工具（Bash、读取、写入）可由 Claude 自主使用，哪些需要手动确认。

通过合理配置这些文件，团队可以确保 Claude 遵循架构边界、遵守特定的代码检查规则，并安全高效地自动化重复性工作流。

---

## 2. 使用 Certbot 在兄弟打印机上安装 Let's Encrypt TLS 证书

**原文标题**: Installing a Let's Encrypt TLS Certificate on a Brother Printer with Certbot

**原文链接**: [https://owltec.ca/Other/Installing+a+Let%27s+Encrypt+TLS+certificate+on+a+Brother+printer+automatically+with+Certbot+(%26+Cloudflare)](https://owltec.ca/Other/Installing+a+Let%27s+Encrypt+TLS+certificate+on+a+Brother+printer+automatically+with+Certbot+(%26+Cloudflare))

这篇来自 OwlTec 的文章提供了一份技术指南，介绍了如何将兄弟 (Brother) 打印机的自签名证书替换为受信任的 Let’s Encrypt TLS 证书，从而消除浏览器安全警告。

该流程的核心是使用 **Certbot** 和 **Cloudflare DNS-01 验证**。这种方法非常适合打印机，因为它通过 DNS 记录验证域名所有权，而无需打印机暴露在公共互联网中。

**工作流程的关键环节包括：**

*   **DNS 验证：** 利用 Certbot Cloudflare 插件自动创建 TXT 记录。这使得用户可以为本地设备使用公共域名获取证书。
*   **证书生成：** 使用 Certbot 获取证书和私钥。
*   **格式转换：** 由于兄弟打印机通常需要特定格式（如 PKCS#12/PFX）的证书，该指南详细说明了如何使用 **OpenSSL** 将证书和私钥打包成一个兼容的文件。
*   **安装：** 通过打印机“网络”和“安全”设置中的**网络管理界面 (WBM)**，手动或通过编程方式上传生成的文件。

该摘要强调，虽然 Certbot 实现了证书续期的自动化，但主要的挑战在于向硬件设备的部署。通过这一方案，管理员可以确保用户与打印机之间实现加密且受信任的通信，避免出现“连接不受信任”的错误提示。

---

## 3. Desk for people who work at home with a cat

**原文标题**: Desk for people who work at home with a cat

**原文链接**: [https://soranews24.com/2026/03/27/japan-now-has-a-special-desk-for-people-who-work-at-home-with-a-pet-catphotos/](https://soranews24.com/2026/03/27/japan-now-has-a-special-desk-for-people-who-work-at-home-with-a-pet-catphotos/)

摘要生成出错

---

## 4. 世界各地海滩的沙子

**原文标题**: Sand from Different Beaches in the World

**原文链接**: [https://magnifiedsand.com/](https://magnifiedsand.com/)

本文对英国林迪斯法恩（圣岛）沙子的地质特征进行了概括性介绍。重点探讨了该岛独特的成分构成，这些成分源于一种被称为“岩床”的地质侵入体。基于这一地质构造，这里的沙子在微观上由三种截然不同的岩石类型融合而成：沉积岩、侵入岩和喷出岩。这种多样性彰显了构成该岛自然景观特色的复杂火山活动及侵蚀历史。

---

## 5. 伊朗学校爆炸案归咎于AI，真相却更令人担忧。

**原文标题**: AI got the blame for the Iran school bombing. The truth is more worrying

**原文链接**: [https://www.theguardian.com/news/2026/mar/26/ai-got-the-blame-for-the-iran-school-bombing-the-truth-is-far-more-worrying](https://www.theguardian.com/news/2026/mar/26/ai-got-the-blame-for-the-iran-school-bombing-the-truth-is-far-more-worrying)

在《人工智能因伊朗学校爆炸事件受指责，真相却更令人不安》一文中，凯文·T·贝克（Kevin T. Baker）指出，2026年伊朗一所小学发生的悲剧性轰炸并非“失控”聊天机器人的产物，而是由高速打击目标基础设施加剧的人类官僚体系的灾难性失败。

尽管媒体报道聚焦于像Anthropic公司的Claude这样的大型语言模型是否对目标产生了“幻觉”，但实际涉及的系统是“梅文计划”（Project Maven）。该计划最初由谷歌发起，后由Palantir接手，是一个旨在压缩“杀伤链”的数据融合平台——即缩短从发现目标到摧毁目标之间的官僚化步骤。通过将卫星图像和传感器数据整合到一个“精简”界面中，“梅文计划”允许少数操作员在几秒钟内做出打击决策。

这场学校惨案的发生是因为美国国防情报局的一个数据库自2016年以来从未更新；尽管该建筑在多年前已改建为学校，但数据库仍将其标记为军事大院。贝克断言，围绕大型语言模型的“人工智能臆想”转移了公众对真正危险的注意力：即“第三次抵消战略”——这是一种将行动速度置于人类审议之上的军事学说。

贝克通过类比越战期间失败的“白冰屋行动”警告称，这些系统创造了一个掩盖复杂性的“抽象层”，并促使军方信任其自身数据而非现实。伊朗的悲剧凸显了一个系统性问题，即技术的构建速度已经超越了人类监管的能力范围。问题不在于人工智能获得了“人格”或走向失控，而在于人类制造了一台致命机器，使人为失误不可避免地演变为致命后果。

---

## 6. 比 Jq 更快的替代方案

**原文标题**: A Faster Alternative to Jq

**原文链接**: [https://micahkepe.com/blog/jsongrep/](https://micahkepe.com/blog/jsongrep/)

在文章**《Jq 的更快替代方案》**中，Micah Kepe 介绍了 **jsongrep**。这是一个用 Rust 编写的高性能命令行工具，旨在比行业标准的 `jq` 更高效地搜索和过滤 JSON 数据。

Kepe 承认，虽然 `jq` 功能极其强大且通用，但在处理海量数据集时，往往面临学习曲线陡峭和性能瓶颈的问题。`jsongrep` 的定位并非 `jq` 复杂转换功能的完整替代品，而是一个用于快速数据提取的专门工具。

**本文的核心亮点包括：**

*   **性能：** `jsongrep` 基于 Rust 构建，并针对速度进行了优化。在执行简单的键/值查找和“grep”任务时，它的速度明显快于 `jq`，非常适合处理大规模日志或海量 JSON 文件。
*   **易用性：** 该工具为需要查找特定数据点的用户提供了更直观的语法，无需钻研 `jq` 复杂的领域特定语言 (DSL)。
*   **专注的使用场景：** 它的主要优势在于“grep”操作——即快速定位并打印 JSON 结构的特定部分。它利用一种简化的基于路径的方法来遍历嵌套数据。
*   **轻量化设计：** 通过专注于功能子集（侧重搜索而非复杂的重构），它保持了更小的资源占用和更高的执行速度。

**结论：**
Kepe 总结道，虽然 `jq` 仍然是处理复杂结构转换的首选，但对于在数据探索过程中优先考虑速度和简洁性的开发人员及系统管理员来说，`jsongrep` 是一个更好的替代方案。在 `jq` 的性能开销过高的情况下，它提供了一种极其高效的方式来解析海量 JSON 数据。

---

## 7. “文书洪流”：我是如何在晚餐前“淹没”一名官僚的

**原文标题**: The 'paperwork flood': How I drowned a bureaucrat before dinner

**原文链接**: [https://sightlessscribbles.com/posts/the-paperwork-flood/](https://sightlessscribbles.com/posts/the-paperwork-flood/)

在这篇关于“恶意服从”的叙述中，自幼失明的作者讲述了他在面对政府“残疾持续性审查”要求提供伤残证明时的挫败感。当一名办事人员坚持要求其通过传真而非电子邮件提供纸质证明文件时，作者决定用对方索要的“证据”让该系统彻底瘫痪。

凭借技术手段和互联网传真服务，作者汇编了一份长达512页的巨型PDF文件，其中包含了他从童年至今的所有医疗记录。随后，他发起了一场数字“围攻”，将文件发往政府办公室的传真机。极大的传输量迫使该办公室陷入持续不断的打印状态，不仅耗尽了碳粉和纸张，还导致机器卡死。

这一策略大获成功。在连续打印两小时后，那名办事人员致电作者，哀求他停止传输。作者则坚持“无辜”服从的姿态，声称该过程是自动化的，无法停止。在“文件洪水”的压力下，对方最终屈服，同意将其档案标记为已更新并立即保障其福利。这个故事既是对残障人士所面临的不必要重重阻碍的批判，也是对战胜僵化官僚体制的一次机智胜利的颂扬。

---

## 8. 如何及为何对图像取对数 [视频]

**原文标题**: How and why to take a logarithm of an image [video]

**原文链接**: [https://www.youtube.com/watch?v=ldxFjLJ3rVY](https://www.youtube.com/watch?v=ldxFjLJ3rVY)

根据提供的标题“如何以及为何对图像取对数”，以下是数字图像处理中该主题通常涉及的概念简要总结（注：您提供的原文本为通用的 YouTube 页脚，不包含实际内容）：

**总结：图像处理中的对数变换**

对图像取对数是一种点处理技术，主要用于**动态范围压缩**和暗区的**细节增强**。

**为何取对数？**
主要原因是为了使高动态范围图像中被隐藏的细节可视化。当图像包含跨越多个数量级的像素值时（常见于傅里叶变换或医学影像），低光强值在肉眼看来通常是全黑的。对数函数将这些低光强（暗部）值扩展到更宽的输出级别范围，同时压缩高光强（亮部）值。这使得阴影中的特征变得可见，且不会使高光部分过度饱和。

**如何取对数？**
该变换遵循特定的数学公式：
\[ S = c \cdot \log(1 + r) \]
*   **$r$：** 原始输入像素值。
*   **$S$：** 生成的输出像素值。
*   **$1$：** 加到输入值中以确保当输入为零时结果也为零（因为 $\log(0)$ 未定义）。
*   **$c$：** 缩放常数，用于确保最终值符合显示范围（例如 8 位图像的 0–255）。

**主要结果：**
1.  **对比度增强**：它能有效提升图像最暗部分的对比度。
2.  **频域可视化**：它是显示图像**傅里叶变换**的标准方法，否则中心峰值会由于亮度极高而导致周围的频率数据不可见。
3.  **非线性**：与线性缩放不同，它模拟了人眼感知光线的非线性方式，使其成为一种强大的视觉预处理工具。

---

## 9. People inside Microsoft are fighting to drop mandatory Microsoft Account

**原文标题**: People inside Microsoft are fighting to drop mandatory Microsoft Account

**原文链接**: [https://www.windowscentral.com/microsoft/windows-11/people-inside-microsoft-are-fighting-to-drop-windows-11s-mandatory-microsoft-account-requirements-during-setup](https://www.windowscentral.com/microsoft/windows-11/people-inside-microsoft-are-fighting-to-drop-windows-11s-mandatory-microsoft-account-requirements-during-setup)

生成摘要时出错

---

## 10. Building FireStriker: Making Civic Tech Free

**原文标题**: Building FireStriker: Making Civic Tech Free

**原文链接**: [https://firestriker.org/blog/building-firestriker-why-im-making-civic-tech-free](https://firestriker.org/blog/building-firestriker-why-im-making-civic-tech-free)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 2 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 3 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 4 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 5 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 6 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 7 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 8 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 9 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 10 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 11 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 12 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 13 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 14 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 15 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 16 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 17 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 18 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 19 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 20 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 21 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 22 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 23 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 24 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 25 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 26 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 27 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 28 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 29 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 30 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 31 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 32 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 33 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 34 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 35 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 36 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 37 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 38 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 39 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 40 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 41 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 42 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 43 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 44 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 45 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 46 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 47 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 48 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 49 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 50 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 51 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 52 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 53 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 54 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 55 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 56 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 57 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 58 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 59 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 60 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 61 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 62 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 63 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 64 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 65 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 66 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 67 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 68 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 69 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 70 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 71 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 72 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 73 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 74 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 75 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 76 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 77 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 78 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 79 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 80 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 81 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 82 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 83 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 84 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 85 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 86 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 87 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 88 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 89 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 90 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 91 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 92 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 93 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 94 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 95 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 96 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 97 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 98 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 99 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 100 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 101 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 102 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 103 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 104 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 105 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 106 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 107 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 108 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 109 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 110 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 111 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 112 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 113 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 114 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 115 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 116 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 117 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 118 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 119 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 120 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 121 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 122 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 123 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 124 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 125 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 126 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 127 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 128 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 129 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 130 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 131 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 132 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 133 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 134 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 135 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 136 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 137 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 138 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 139 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 140 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 141 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 142 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 143 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 144 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 145 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 146 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 147 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 148 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 149 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 150 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 151 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 152 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 153 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 154 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 155 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 156 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 157 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 158 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 159 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 160 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 161 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 162 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 163 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 164 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 165 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 166 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 167 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 168 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 169 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 170 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 171 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 172 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 173 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 174 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 175 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 176 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 177 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 178 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 179 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 180 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 181 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 182 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 183 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 184 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 185 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 186 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 187 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 188 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 189 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 190 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 191 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 192 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 193 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 194 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 195 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 196 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 197 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 198 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 199 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 200 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 201 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 202 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 203 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 204 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 205 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 206 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 207 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 208 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 209 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 210 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 211 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 212 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 213 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 214 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 215 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 216 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 217 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 218 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 219 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 220 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 221 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 222 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 223 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 224 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 225 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 226 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 227 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 228 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 229 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 230 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 231 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 232 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 233 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 234 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 235 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 236 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 237 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 238 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 239 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 240 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 241 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 242 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 243 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 244 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 245 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 246 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 247 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 248 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 249 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 250 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 251 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 252 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 253 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 254 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 255 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 256 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 257 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 258 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 259 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 260 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 261 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 262 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 263 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 264 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 265 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 266 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 267 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 268 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 269 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 270 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 271 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 272 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 273 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 274 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 275 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 276 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 277 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 278 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 279 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 280 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 281 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 282 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 283 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 284 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 285 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 286 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 287 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 288 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 289 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 290 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 291 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 292 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 293 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 294 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 295 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 296 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 297 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 298 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 299 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 300 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 301 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 302 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 303 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 304 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 305 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 306 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 307 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 308 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 309 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 310 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 311 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 312 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 313 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 314 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 315 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 316 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 317 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 318 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 319 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 320 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 321 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 322 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 323 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 324 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 325 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 326 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 327 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 328 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 329 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 330 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 331 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 332 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 333 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 334 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 335 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 336 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 337 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 338 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 339 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 340 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 341 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 342 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 343 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 344 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 345 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 346 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 347 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 348 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 349 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 350 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 351 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 352 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 353 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 354 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 355 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 356 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 357 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 358 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 359 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 360 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 361 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 362 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 363 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 364 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 365 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 366 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 367 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 368 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 369 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 370 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 371 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 372 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
