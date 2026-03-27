# Hacker News 热门文章摘要 (2026-03-27)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. EMachines never obsolete PCs: More than a meme

**原文标题**: EMachines never obsolete PCs: More than a meme

**原文链接**: [https://dfarq.homeip.net/emachines-never-obsolete-pcs-more-than-a-meme/](https://dfarq.homeip.net/emachines-never-obsolete-pcs-more-than-a-meme/)

生成摘要时出错

---

## 12. Hold on to Your Hardware

**原文标题**: Hold on to Your Hardware

**原文链接**: [https://xn--gckvb8fzb.com/hold-on-to-your-hardware/](https://xn--gckvb8fzb.com/hold-on-to-your-hardware/)

生成摘要时出错

---

## 13. Schedule tasks on the web

**原文标题**: Schedule tasks on the web

**原文链接**: [https://code.claude.com/docs/en/web-scheduled-tasks](https://code.claude.com/docs/en/web-scheduled-tasks)

生成摘要时出错

---

## 14. Apple discontinues the Mac Pro

**原文标题**: Apple discontinues the Mac Pro

**原文链接**: [https://9to5mac.com/2026/03/26/apple-discontinues-the-mac-pro/](https://9to5mac.com/2026/03/26/apple-discontinues-the-mac-pro/)

生成摘要时出错

---

## 15. Meow.camera

**原文标题**: Meow.camera

**原文链接**: [https://meow.camera/#4258783365322591678](https://meow.camera/#4258783365322591678)

生成摘要时出错

---

## 16. 21,864 Yugoslavian .yu domains

**原文标题**: 21,864 Yugoslavian .yu domains

**原文链接**: [https://jacobfilipp.com/yu/](https://jacobfilipp.com/yu/)

生成摘要时出错

---

## 17. ‘Energy independence feels practical’: Europeans building mini solar farms

**原文标题**: ‘Energy independence feels practical’: Europeans building mini solar farms

**原文链接**: [https://www.euronews.com/2026/03/26/suddenly-energy-independence-feels-practical-europeans-are-building-mini-solar-farms-at-ho](https://www.euronews.com/2026/03/26/suddenly-energy-independence-feels-practical-europeans-are-building-mini-solar-farms-at-ho)

生成摘要时出错

---

## 18. Gzip decompression in 250 lines of Rust

**原文标题**: Gzip decompression in 250 lines of Rust

**原文链接**: [https://iev.ee/blog/gzip-decompression-in-250-lines-of-rust/](https://iev.ee/blog/gzip-decompression-in-250-lines-of-rust/)

生成摘要时出错

---

## 19. Why so many control rooms were seafoam green (2025)

**原文标题**: Why so many control rooms were seafoam green (2025)

**原文链接**: [https://bethmathews.substack.com/p/why-so-many-control-rooms-were-seafoam](https://bethmathews.substack.com/p/why-so-many-control-rooms-were-seafoam)

生成摘要时出错

---

## 20. Show HN: Sup AI, a confidence-weighted ensemble (52.15% on Humanity's Last Exam)

**原文标题**: Show HN: Sup AI, a confidence-weighted ensemble (52.15% on Humanity's Last Exam)

**原文链接**: [https://sup.ai](https://sup.ai)

生成摘要时出错

---

## 21. Iran-linked hackers have breached FBI director's personal emails

**原文标题**: Iran-linked hackers have breached FBI director's personal emails

**原文链接**: [https://www.cnn.com/2026/03/27/politics/iran-linked-hackers-fbi-director-patel](https://www.cnn.com/2026/03/27/politics/iran-linked-hackers-fbi-director-patel)

生成摘要时出错

---

## 22. Last gasps of the rent seeking class?

**原文标题**: Last gasps of the rent seeking class?

**原文链接**: [https://geohot.github.io//blog/jekyll/update/2026/02/26/the-last-gasps-of-the-rent-seeking-class.html](https://geohot.github.io//blog/jekyll/update/2026/02/26/the-last-gasps-of-the-rent-seeking-class.html)

生成摘要时出错

---

## 23. Should QA exist?

**原文标题**: Should QA exist?

**原文链接**: [https://www.rubick.com/should-qa-exist/](https://www.rubick.com/should-qa-exist/)

生成摘要时出错

---

## 24. Everything old is new again: memory optimization

**原文标题**: Everything old is new again: memory optimization

**原文链接**: [https://nibblestew.blogspot.com/2026/03/everything-old-is-new-again-memory.html](https://nibblestew.blogspot.com/2026/03/everything-old-is-new-again-memory.html)

生成摘要时出错

---

## 25. The European AllSky7 fireball network

**原文标题**: The European AllSky7 fireball network

**原文链接**: [https://www.allsky7.net/#archive](https://www.allsky7.net/#archive)

生成摘要时出错

---

## 26. Netflix raises prices for every subscription tier by up to 12.5 percent

**原文标题**: Netflix raises prices for every subscription tier by up to 12.5 percent

**原文链接**: [https://arstechnica.com/gadgets/2026/03/netflix-increases-prices-for-all-plans-by-up-to-2-per-month/](https://arstechnica.com/gadgets/2026/03/netflix-increases-prices-for-all-plans-by-up-to-2-per-month/)

生成摘要时出错

---

## 27. The Legibility of Serif and Sans Serif Typefaces (2022)

**原文标题**: The Legibility of Serif and Sans Serif Typefaces (2022)

**原文链接**: [https://library.oapen.org//handle/20.500.12657/53344](https://library.oapen.org//handle/20.500.12657/53344)

生成摘要时出错

---

## 28. Apple says no one using Lockdown Mode has been hacked with spyware

**原文标题**: Apple says no one using Lockdown Mode has been hacked with spyware

**原文链接**: [https://techcrunch.com/2026/03/27/apple-says-no-one-using-lockdown-mode-has-been-hacked-with-spyware/](https://techcrunch.com/2026/03/27/apple-says-no-one-using-lockdown-mode-has-been-hacked-with-spyware/)

生成摘要时出错

---

## 29. Embracing Bayesian Methods in Clinical Trials

**原文标题**: Embracing Bayesian Methods in Clinical Trials

**原文链接**: [https://jamanetwork.com/journals/jama/fullarticle/2847011](https://jamanetwork.com/journals/jama/fullarticle/2847011)

生成摘要时出错

---

## 30. $500 GPU outperforms Claude Sonnet on coding benchmarks

**原文标题**: $500 GPU outperforms Claude Sonnet on coding benchmarks

**原文链接**: [https://github.com/itigges22/ATLAS](https://github.com/itigges22/ATLAS)

生成摘要时出错

---

## 31. Show HN: I put an AI agent on a $7/month VPS with IRC as its transport layer

**原文标题**: Show HN: I put an AI agent on a $7/month VPS with IRC as its transport layer

**原文链接**: [https://georgelarson.me/writing/2026-03-23-nullclaw-doorman/](https://georgelarson.me/writing/2026-03-23-nullclaw-doorman/)

生成摘要时出错

---

## 32. Local Bernstein theory, and lower bounds for Lebesgue constants

**原文标题**: Local Bernstein theory, and lower bounds for Lebesgue constants

**原文链接**: [https://terrytao.wordpress.com/2026/03/23/local-bernstein-theory-and-lower-bounds-for-lebesgue-constants/](https://terrytao.wordpress.com/2026/03/23/local-bernstein-theory-and-lower-bounds-for-lebesgue-constants/)

生成摘要时出错

---

## 33. Claude loses its >99% uptime in Q1 2026

**原文标题**: Claude loses its >99% uptime in Q1 2026

**原文链接**: [https://bsky.app/profile/teropa.bsky.social/post/3mi2dbt27m226](https://bsky.app/profile/teropa.bsky.social/post/3mi2dbt27m226)

生成摘要时出错

---

## 34. The State of Immutable Linux

**原文标题**: The State of Immutable Linux

**原文链接**: [https://justingarrison.com/blog/state-of-immutable-linux/](https://justingarrison.com/blog/state-of-immutable-linux/)

生成摘要时出错

---

## 35. We rewrote JSONata with AI in a day, saved $500k/year

**原文标题**: We rewrote JSONata with AI in a day, saved $500k/year

**原文链接**: [https://www.reco.ai/blog/we-rewrote-jsonata-with-ai](https://www.reco.ai/blog/we-rewrote-jsonata-with-ai)

生成摘要时出错

---

## 36. DOOM Over DNS

**原文标题**: DOOM Over DNS

**原文链接**: [https://github.com/resumex/doom-over-dns](https://github.com/resumex/doom-over-dns)

生成摘要时出错

---

## 37. Running Tesla Model 3's computer on my desk using parts from crashed cars

**原文标题**: Running Tesla Model 3's computer on my desk using parts from crashed cars

**原文链接**: [https://bugs.xdavidhu.me/tesla/2026/03/23/running-tesla-model-3s-computer-on-my-desk-using-parts-from-crashed-cars/](https://bugs.xdavidhu.me/tesla/2026/03/23/running-tesla-model-3s-computer-on-my-desk-using-parts-from-crashed-cars/)

生成摘要时出错

---

## 38. Hong Kong police can now demand phone passwords under new security rules

**原文标题**: Hong Kong police can now demand phone passwords under new security rules

**原文链接**: [https://www.gadgetreview.com/hong-kong-police-can-now-demand-phone-passwords-under-new-security-rules](https://www.gadgetreview.com/hong-kong-police-can-now-demand-phone-passwords-under-new-security-rules)

生成摘要时出错

---

## 39. QRV Operating System: QNX on RISC-V

**原文标题**: QRV Operating System: QNX on RISC-V

**原文链接**: [https://r-tty.blogspot.com/2026/03/qrv-operating-system-first-publication.html](https://r-tty.blogspot.com/2026/03/qrv-operating-system-first-publication.html)

生成摘要时出错

---

## 40. My minute-by-minute response to the LiteLLM malware attack

**原文标题**: My minute-by-minute response to the LiteLLM malware attack

**原文链接**: [https://futuresearch.ai/blog/litellm-attack-transcript/](https://futuresearch.ai/blog/litellm-attack-transcript/)

生成摘要时出错

---

## 41. Whistler: Live eBPF Programming from the Common Lisp REPL

**原文标题**: Whistler: Live eBPF Programming from the Common Lisp REPL

**原文链接**: [https://atgreen.github.io/repl-yell/posts/whistler/](https://atgreen.github.io/repl-yell/posts/whistler/)

生成摘要时出错

---

## 42. HyperAgents: Self-referential self-improving agents

**原文标题**: HyperAgents: Self-referential self-improving agents

**原文链接**: [https://github.com/facebookresearch/hyperagents](https://github.com/facebookresearch/hyperagents)

生成摘要时出错

---

## 43. Generators in Lone Lisp

**原文标题**: Generators in Lone Lisp

**原文链接**: [https://www.matheusmoreira.com/articles/generators-in-lone-lisp](https://www.matheusmoreira.com/articles/generators-in-lone-lisp)

生成摘要时出错

---

## 44. Agent-to-agent pair programming

**原文标题**: Agent-to-agent pair programming

**原文链接**: [https://axeldelafosse.com/blog/agent-to-agent-pair-programming](https://axeldelafosse.com/blog/agent-to-agent-pair-programming)

生成摘要时出错

---

## 45. An unstoppable mushroom is tearing through North American forests

**原文标题**: An unstoppable mushroom is tearing through North American forests

**原文链接**: [https://www.bbc.com/future/article/20260325-an-unstoppable-mushroom-is-tearing-through-north-american-forests](https://www.bbc.com/future/article/20260325-an-unstoppable-mushroom-is-tearing-through-north-american-forests)

生成摘要时出错

---

## 46. Anthropic Subprocessor Changes

**原文标题**: Anthropic Subprocessor Changes

**原文链接**: [https://trust.anthropic.com](https://trust.anthropic.com)

生成摘要时出错

---

## 47. Using FireWire on a Raspberry Pi

**原文标题**: Using FireWire on a Raspberry Pi

**原文链接**: [https://www.jeffgeerling.com/blog/2026/firewire-on-a-raspberry-pi/](https://www.jeffgeerling.com/blog/2026/firewire-on-a-raspberry-pi/)

生成摘要时出错

---

## 48. We haven't seen the worst of what gambling and prediction markets will do

**原文标题**: We haven't seen the worst of what gambling and prediction markets will do

**原文链接**: [https://www.derekthompson.org/p/we-havent-seen-the-worst-of-what](https://www.derekthompson.org/p/we-havent-seen-the-worst-of-what)

生成摘要时出错

---

## 49. OpenTelemetry profiles enters public alpha

**原文标题**: OpenTelemetry profiles enters public alpha

**原文链接**: [https://opentelemetry.io/blog/2026/profiles-alpha/](https://opentelemetry.io/blog/2026/profiles-alpha/)

生成摘要时出错

---

## 50. Show HN: Fio: 3D World editor/game engine – inspired by Radiant and Hammer

**原文标题**: Show HN: Fio: 3D World editor/game engine – inspired by Radiant and Hammer

**原文链接**: [https://github.com/ViciousSquid/Fio](https://github.com/ViciousSquid/Fio)

生成摘要时出错

---

## 51. I am leaving the AI party after one drink

**原文标题**: I am leaving the AI party after one drink

**原文链接**: [https://lara-aigmueller.at/thoughts/leaving-the-ai-party/](https://lara-aigmueller.at/thoughts/leaving-the-ai-party/)

生成摘要时出错

---

## 52. Colibri – chat platform built on the AT Protocol for communities big and small

**原文标题**: Colibri – chat platform built on the AT Protocol for communities big and small

**原文链接**: [https://colibri.social/](https://colibri.social/)

生成摘要时出错

---

## 53. John Bradley, author of xv, has died

**原文标题**: John Bradley, author of xv, has died

**原文链接**: [https://voxday.net/2026/03/25/rip-john-bradley/](https://voxday.net/2026/03/25/rip-john-bradley/)

生成摘要时出错

---

## 54. Chroma Context-1: Training a Self-Editing Search Agent

**原文标题**: Chroma Context-1: Training a Self-Editing Search Agent

**原文链接**: [https://www.trychroma.com/research/context-1](https://www.trychroma.com/research/context-1)

生成摘要时出错

---

## 55. Google's TurboQuant AI-compression algorithm can reduce LLM memory usage by 6x

**原文标题**: Google's TurboQuant AI-compression algorithm can reduce LLM memory usage by 6x

**原文链接**: [https://arstechnica.com/ai/2026/03/google-says-new-turboquant-compression-can-lower-ai-memory-usage-without-sacrificing-quality/](https://arstechnica.com/ai/2026/03/google-says-new-turboquant-compression-can-lower-ai-memory-usage-without-sacrificing-quality/)

生成摘要时出错

---

## 56. Moving from GitHub to Codeberg, for lazy people

**原文标题**: Moving from GitHub to Codeberg, for lazy people

**原文链接**: [https://unterwaditzer.net/2025/codeberg.html](https://unterwaditzer.net/2025/codeberg.html)

生成摘要时出错

---

## 57. Iran oil revenue soars as it's the only exporter out of Hormuz

**原文标题**: Iran oil revenue soars as it's the only exporter out of Hormuz

**原文链接**: [https://financialpost.com/commodities/energy/oil-gas/iran-oil-revenue-soars-hormuz](https://financialpost.com/commodities/energy/oil-gas/iran-oil-revenue-soars-hormuz)

生成摘要时出错

---

## 58. CERN to host a new phase of Open Research Europe

**原文标题**: CERN to host a new phase of Open Research Europe

**原文链接**: [https://home.cern/news/news/cern/cern-host-europes-flagship-open-access-publishing-platform](https://home.cern/news/news/cern/cern-host-europes-flagship-open-access-publishing-platform)

生成摘要时出错

---

## 59. My home network observes bedtime with OpenBSD and pf

**原文标题**: My home network observes bedtime with OpenBSD and pf

**原文链接**: [https://ratfactor.com/openbsd/pf-gateway-bedtime](https://ratfactor.com/openbsd/pf-gateway-bedtime)

生成摘要时出错

---

## 60. Show HN: Turbolite – a SQLite VFS serving sub-250ms cold JOIN queries from S3

**原文标题**: Show HN: Turbolite – a SQLite VFS serving sub-250ms cold JOIN queries from S3

**原文链接**: [https://github.com/russellromney/turbolite](https://github.com/russellromney/turbolite)

生成摘要时出错

---

## 61. Chicago artist creates tourism posters for city's neighborhoods

**原文标题**: Chicago artist creates tourism posters for city's neighborhoods

**原文链接**: [https://www.chicagotribune.com/2026/03/25/chicago-neighborhood-posters/](https://www.chicagotribune.com/2026/03/25/chicago-neighborhood-posters/)

生成摘要时出错

---

## 62. HandyMKV for MakeMKV and HandBrake Automation

**原文标题**: HandyMKV for MakeMKV and HandBrake Automation

**原文链接**: [https://github.com/dmars8047/handymkv](https://github.com/dmars8047/handymkv)

生成摘要时出错

---

## 63. Personal Encyclopedias

**原文标题**: Personal Encyclopedias

**原文链接**: [https://whoami.wiki/blog/personal-encyclopedias](https://whoami.wiki/blog/personal-encyclopedias)

生成摘要时出错

---

## 64. Ashby (YC W19) Is Hiring Engineers Who Make Product Decisions

**原文标题**: Ashby (YC W19) Is Hiring Engineers Who Make Product Decisions

**原文链接**: [https://www.ashbyhq.com/careers?ashby_jid=c3c7125d-7883-4dff-a2bf-f5a55de4a364&utm_source=hn](https://www.ashbyhq.com/careers?ashby_jid=c3c7125d-7883-4dff-a2bf-f5a55de4a364&utm_source=hn)

生成摘要时出错

---

## 65. Google Just Patented the End of Your Website

**原文标题**: Google Just Patented the End of Your Website

**原文链接**: [https://www.forbes.com/sites/joetoscano1/2026/03/06/google-just-patented-the-end-of-your-website/](https://www.forbes.com/sites/joetoscano1/2026/03/06/google-just-patented-the-end-of-your-website/)

生成摘要时出错

---

## 66. End of "Chat Control": EU parliament stops mass surveillance

**原文标题**: End of "Chat Control": EU parliament stops mass surveillance

**原文链接**: [https://www.patrick-breyer.de/en/end-of-chat-control-eu-parliament-stops-mass-surveillance-in-voting-thriller-paving-the-way-for-genuine-child-protection/](https://www.patrick-breyer.de/en/end-of-chat-control-eu-parliament-stops-mass-surveillance-in-voting-thriller-paving-the-way-for-genuine-child-protection/)

生成摘要时出错

---

## 67. Obsolete Sounds

**原文标题**: Obsolete Sounds

**原文链接**: [https://citiesandmemory.com/obsolete-sounds/](https://citiesandmemory.com/obsolete-sounds/)

生成摘要时出错

---

## 68. Jury finds Meta liable in case over child sexual exploitation on its platforms

**原文标题**: Jury finds Meta liable in case over child sexual exploitation on its platforms

**原文链接**: [https://www.cnn.com/2026/03/24/tech/meta-new-mexico-trial-jury-deliberation](https://www.cnn.com/2026/03/24/tech/meta-new-mexico-trial-jury-deliberation)

生成摘要时出错

---

## 69. Olympic Committee bars transgender athletes from women’s events

**原文标题**: Olympic Committee bars transgender athletes from women’s events

**原文链接**: [https://www.nytimes.com/2026/03/26/world/olympics/ioc-transgender-athletes-ban.html?unlocked_article_code=1.WFA.U8U0.iEs61HsUkQj5](https://www.nytimes.com/2026/03/26/world/olympics/ioc-transgender-athletes-ban.html?unlocked_article_code=1.WFA.U8U0.iEs61HsUkQj5)

生成摘要时出错

---

## 70. Show HN: Minimalist library to generate SVG views of scientific data

**原文标题**: Show HN: Minimalist library to generate SVG views of scientific data

**原文链接**: [https://github.com/alefore/mini_svg/](https://github.com/alefore/mini_svg/)

生成摘要时出错

---

## 71. Stripe Projects: Provision and manage services from the CLI

**原文标题**: Stripe Projects: Provision and manage services from the CLI

**原文链接**: [https://projects.dev/](https://projects.dev/)

生成摘要时出错

---

## 72. Zero Days: Electric Motorcycles Are a Security Nightmare

**原文标题**: Zero Days: Electric Motorcycles Are a Security Nightmare

**原文链接**: [https://persephonekarnstein.github.io/post/zero-days/](https://persephonekarnstein.github.io/post/zero-days/)

生成摘要时出错

---

## 73. How much precision can you squeeze out of a table?

**原文标题**: How much precision can you squeeze out of a table?

**原文链接**: [https://www.johndcook.com/blog/2026/03/26/table-precision/](https://www.johndcook.com/blog/2026/03/26/table-precision/)

生成摘要时出错

---

## 74. What came after the 486?

**原文标题**: What came after the 486?

**原文链接**: [https://dfarq.homeip.net/what-came-after-486/](https://dfarq.homeip.net/what-came-after-486/)

生成摘要时出错

---

## 75. Building a Blog with Elixir and Phoenix

**原文标题**: Building a Blog with Elixir and Phoenix

**原文链接**: [https://jola.dev/posts/building-a-blog-with-elixir-and-phoenix](https://jola.dev/posts/building-a-blog-with-elixir-and-phoenix)

生成摘要时出错

---

## 76. MacBook Neo, the Benchmarks

**原文标题**: MacBook Neo, the Benchmarks

**原文链接**: [https://birchtree.me/blog/macbook-neo-the-benchmarks/](https://birchtree.me/blog/macbook-neo-the-benchmarks/)

生成摘要时出错

---

## 77. Cloudflare's Gen 13 servers: trading cache for cores for 2x performance

**原文标题**: Cloudflare's Gen 13 servers: trading cache for cores for 2x performance

**原文链接**: [https://blog.cloudflare.com/gen13-launch/](https://blog.cloudflare.com/gen13-launch/)

生成摘要时出错

---

## 78. Order Granting Preliminary Injunction – Anthropic vs. U.S. Department of War [pdf]

**原文标题**: Order Granting Preliminary Injunction – Anthropic vs. U.S. Department of War [pdf]

**原文链接**: [https://storage.courtlistener.com/recap/gov.uscourts.cand.465515/gov.uscourts.cand.465515.134.0.pdf](https://storage.courtlistener.com/recap/gov.uscourts.cand.465515/gov.uscourts.cand.465515.134.0.pdf)

生成摘要时出错

---

## 79. Shell Tricks That Make Life Easier (and Save Your Sanity)

**原文标题**: Shell Tricks That Make Life Easier (and Save Your Sanity)

**原文链接**: [https://blog.hofstede.it/shell-tricks-that-actually-make-life-easier-and-save-your-sanity/](https://blog.hofstede.it/shell-tricks-that-actually-make-life-easier-and-save-your-sanity/)

生成摘要时出错

---

## 80. Fast regex search: indexing text for agent tools

**原文标题**: Fast regex search: indexing text for agent tools

**原文链接**: [https://cursor.com/blog/fast-regex-search](https://cursor.com/blog/fast-regex-search)

生成摘要时出错

---

## 81. Judge blocks Pentagon effort to 'punish' Anthropic with supply chain risk label

**原文标题**: Judge blocks Pentagon effort to 'punish' Anthropic with supply chain risk label

**原文链接**: [https://www.cnn.com/2026/03/26/business/anthropic-pentagon-injunction-supply-chain-risk](https://www.cnn.com/2026/03/26/business/anthropic-pentagon-injunction-supply-chain-risk)

生成摘要时出错

---

## 82. Show HN: Veil – Dark mode PDFs without destroying images, runs in the browser

**原文标题**: Show HN: Veil – Dark mode PDFs without destroying images, runs in the browser

**原文链接**: [https://veil.simoneamico.com/](https://veil.simoneamico.com/)

生成摘要时出错

---

## 83. From zero to a RAG system: successes and failures

**原文标题**: From zero to a RAG system: successes and failures

**原文链接**: [https://en.andros.dev/blog/aa31d744/from-zero-to-a-rag-system-successes-and-failures/](https://en.andros.dev/blog/aa31d744/from-zero-to-a-rag-system-successes-and-failures/)

生成摘要时出错

---

## 84. Swift 6.3

**原文标题**: Swift 6.3

**原文链接**: [https://www.swift.org/blog/swift-6.3-released/](https://www.swift.org/blog/swift-6.3-released/)

生成摘要时出错

---

## 85. Niche Museums

**原文标题**: Niche Museums

**原文链接**: [https://www.niche-museums.com/](https://www.niche-museums.com/)

生成摘要时出错

---

## 86. Taming LLMs: Using Executable Oracles to Prevent Bad Code

**原文标题**: Taming LLMs: Using Executable Oracles to Prevent Bad Code

**原文链接**: [https://john.regehr.org/writing/zero_dof_programming.html](https://john.regehr.org/writing/zero_dof_programming.html)

生成摘要时出错

---

## 87. Nixbook OS: A set-and-forget modern operating system designed for simplicity

**原文标题**: Nixbook OS: A set-and-forget modern operating system designed for simplicity

**原文链接**: [https://nixbookos.org/](https://nixbookos.org/)

生成摘要时出错

---

## 88. “Disregard That” Attacks

**原文标题**: “Disregard That” Attacks

**原文链接**: [https://calpaterson.com/disregard.html](https://calpaterson.com/disregard.html)

生成摘要时出错

---

## 89. Interoperability Can Save the Open Web (2023)

**原文标题**: Interoperability Can Save the Open Web (2023)

**原文链接**: [https://spectrum.ieee.org/doctorow-interoperability](https://spectrum.ieee.org/doctorow-interoperability)

生成摘要时出错

---

## 90. MIT 15.393 – Nuts and Bolts of New Ventures (2026)

**原文标题**: MIT 15.393 – Nuts and Bolts of New Ventures (2026)

**原文链接**: [https://nutsandbolts.mit.edu/info.php](https://nutsandbolts.mit.edu/info.php)

生成摘要时出错

---

## 91. Light on Glass: Why do you start making a game engine?

**原文标题**: Light on Glass: Why do you start making a game engine?

**原文链接**: [https://analogdreamdev.substack.com/p/light-on-glass](https://analogdreamdev.substack.com/p/light-on-glass)

生成摘要时出错

---

## 92. Limitations of Serial Cloning in Mammals

**原文标题**: Limitations of Serial Cloning in Mammals

**原文链接**: [https://www.nature.com/articles/s41467-026-69765-7](https://www.nature.com/articles/s41467-026-69765-7)

生成摘要时出错

---

## 93. Optimizing a lock-free ring buffer

**原文标题**: Optimizing a lock-free ring buffer

**原文链接**: [https://david.alvarezrosa.com/posts/optimizing-a-lock-free-ring-buffer/](https://david.alvarezrosa.com/posts/optimizing-a-lock-free-ring-buffer/)

生成摘要时出错

---

## 94. The Oxford Comma – Why and Why Not (2024)

**原文标题**: The Oxford Comma – Why and Why Not (2024)

**原文链接**: [https://www.deborahcourtbooks.com/post/the-oxford-comma-why-and-why-not](https://www.deborahcourtbooks.com/post/the-oxford-comma-why-and-why-not)

生成摘要时出错

---

## 95. What the CIA's "Queen of Torture" did next

**原文标题**: What the CIA's "Queen of Torture" did next

**原文链接**: [https://www.newstatesman.com/world/americas/north-america/us/2026/03/what-the-cias-queen-of-torture-did-next](https://www.newstatesman.com/world/americas/north-america/us/2026/03/what-the-cias-queen-of-torture-did-next)

生成摘要时出错

---

## 96. More precise elevation data for GraphHopper routing engine

**原文标题**: More precise elevation data for GraphHopper routing engine

**原文链接**: [https://www.graphhopper.com/blog/2026/03/23/more-precise-elevation-data-for-graphhopper/](https://www.graphhopper.com/blog/2026/03/23/more-precise-elevation-data-for-graphhopper/)

生成摘要时出错

---

## 97. Show HN: Optio – Orchestrate AI coding agents in K8s to go from ticket to PR

**原文标题**: Show HN: Optio – Orchestrate AI coding agents in K8s to go from ticket to PR

**原文链接**: [https://github.com/jonwiggins/optio](https://github.com/jonwiggins/optio)

生成摘要时出错

---

## 98. SpaceStarCarz KoolWheelz Paper Models

**原文标题**: SpaceStarCarz KoolWheelz Paper Models

**原文链接**: [https://davesdesigns.ca/dcc/html/spacestarcarz_.html](https://davesdesigns.ca/dcc/html/spacestarcarz_.html)

生成摘要时出错

---

## 99. ARC-AGI-3

**原文标题**: ARC-AGI-3

**原文链接**: [https://arcprize.org/arc-agi/3](https://arcprize.org/arc-agi/3)

生成摘要时出错

---

## 100. Dobase – Open-source, self-hosted workspace with installable tools

**原文标题**: Dobase – Open-source, self-hosted workspace with installable tools

**原文链接**: [https://dobase.co/](https://dobase.co/)

生成摘要时出错

---

