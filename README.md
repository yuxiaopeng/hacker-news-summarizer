# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-06-01.md)

*最后自动更新时间: 2026-06-01 21:21:36*
## 1. Instagram 最新的这个“漏洞”是我见过最滑稽的。

**原文标题**: The newest Instagram “exploit” is the goofiest I've seen

**原文链接**: [https://www.0xsid.com/blog/meta-account-takeover-fiasco](https://www.0xsid.com/blog/meta-account-takeover-fiasco)

提供的文章描述了 Instagram AI 驱动的账户恢复流程中一个重大且现已修复的安全漏洞。该漏洞允许攻击者劫持高知名度账户，包括奥巴马时期的白宫账户和美国太空军总军士长的账户。

**漏洞利用机制**
接管过程出奇地简单：
1. **地理位置欺骗：** 攻击者使用 VPN 或代理来匹配目标的地理区域，使请求在 Instagram 的算法看来是合法的。
2. **操控 AI 支持系统：** 攻击者说服 Meta 的支持 AI 相信账户已被盗，并请求将验证码发送到攻击者控制的新邮箱地址。
3. **绕过验证：** AI 未能检查新邮箱此前是否与该账户有关联。此外，视频自拍等身份验证措施也通过目标的 AI 动画照片被轻易绕过。

**安全失效**
由于这被视为由经认证的所有者进行的“账户完全重置”，标准的安保措施均失效：
* **绕过双重身份验证 (2FA)：** 该流程完全绕过了现有的双重身份验证。
* **撤销会话：** 原始所有者会立即被登出，其联系信息在未通知的情况下被更改，导致他们无法启动恢复程序。

**影响与解决**
该漏洞助长了 Telegram 上的黑市交易，短字符或高价值的账号以高价售出。虽然作者指出 Meta 随后修复了这一特定的“零认证”密码重置流程，但该事件突显了 Meta 自动化支持系统中严重缺乏稳健的防护机制。

---

## 2. 佛罗里达州因AI风险起诉OpenAI及萨姆·奥尔特曼

**原文标题**: Florida sues OpenAI and Sam Altman over AI risks

**原文链接**: [https://www.politico.com/news/2026/06/01/openai-hit-with-florida-lawsuit-00944215](https://www.politico.com/news/2026/06/01/openai-hit-with-florida-lawsuit-00944215)

无法访问文章链接。

---

## 3. 斯坦福 CS336 AI 智能体指南

**原文标题**: AI Agent Guidelines for CS336 at Stanford

**原文链接**: [https://github.com/stanford-cs336/assignment1-basics/blob/main/CLAUDE.md](https://github.com/stanford-cs336/assignment1-basics/blob/main/CLAUDE.md)

**斯坦福大学 CS336 课程 AI 智能体指南**规定，AI 助手必须作为教学辅助工具，而非答案生成器。由于 CS336 是一门重实践的课程，其首要目标是确保学生在极少框架辅助的情况下，通过自主编写代码（包括分词器、Transformer 模块和训练循环）来开展学习。

**核心职责（AI 应当做什么）：**
*   **解释与引导：** 通过指引学生查阅讲义资料和官方文档，帮助其理解高层概念与算法。
*   **审阅与调试：** 对学生编写的代码提供通用反馈，识别潜在的边界情况，并解释错误信息。
*   **鼓励自主探索：** 针对学生的方法提出引导性问题，并建议进行合理性检查、尝试简单示例或开展基于性能分析的调查。

**严禁行为（AI 不得做什么）：**
*   **编写代码：** AI 不得生成 Python 或伪代码，不得完成“TODO”部分，也不得将学生代码重构为最终方案。
*   **直接实现：** 禁止智能体实现核心作业组件或提供问题的直接答案。
*   **系统交互：** AI 不应编辑代码仓库或运行 Bash 命令。
*   **外部资源：** 不得引导学生查阅第三方实现，因为课程材料已涵盖所有必要内容。

**教学理念：**
当学生寻求帮助时，智能体应从直接作答转向主动对话。这包括询问学生已尝试过的方法，解释概念背后的原理，并建议后续步骤或断言检查，而非直接提供修复方案。最终，该指南将学术诚信放在首位，确保 AI 工具在辅助学习过程的同时，不会削弱学生自主完成学业的责任。

---

## 4. RGB 值应该除以 255 还是 256 进行归一化？

**原文标题**: Should you normalize RGB values by 255 or 256?

**原文链接**: [https://30fps.net/pages/255-vs-256-division/](https://30fps.net/pages/255-vs-256-division/)

本文评估了将 8 位 RGB 值归一化为浮点数的两种方法：标准的“除以 255”和替代的“除以 256”（使用 0.5 偏移）。

**标准方法（除以 255）：**
该方法将整数 0 映射为 0.0，将 255 映射为 1.0。它是 GPU 采用的行业标准，确保了“黑色”精确为零。然而，它在色谱的两端产生了“半尺寸”区间，这意味着在对均匀分布进行舍入时，0 和 255 出现的频率仅为其他整数的一半。此外，它还会产生略微不精确的浮点值（例如 128/255 并不精确等于 0.5）。

**替代方法（除以 256）：**
通过增加 0.5 偏移并除以 256，整数被映射到其对应区间的正中心。这种方法在理论上更精确，平均绝对误差更低，并能通过避开边缘情况简化抖动（dithering）等任务。缺点是它将处理逻辑与 8 位常量绑定（黑色不再是 0.0），导致代码在不同位深之间的可移植性变差。

**量化理论：**
作者将这一选择归结为在两种量化器类型之间的抉择：中升型（mid-riser，对应 255）和中阶型（mid-tread，对应 256）。虽然 256 方法在数学重建上更具优势，但这种优势仅在开发者能够同时控制编码和解码步骤时才成立。

**结论：**
对于通用的图像处理，作者建议坚持使用标准的“除以 255”。它能确保与他人生成的图像兼容，并维持 0.0 映射到黑色的直观性。除以 256 仅应在需要极高精度且开发者控制整个管线的封闭系统中使用。

---

## 5. CS336: Language Modeling from Scratch

**原文标题**: CS336: Language Modeling from Scratch

**原文链接**: [https://cs336.stanford.edu/](https://cs336.stanford.edu/)

生成摘要时出错

---

## 6. 看似生化过程的现象可能只是自然的地质特征。

**原文标题**: What appear to be biochemical processes may be a natural feature of geology

**原文链接**: [https://www.quantamagazine.org/the-dirt-that-refused-to-die-20260601/](https://www.quantamagazine.org/the-dirt-that-refused-to-die-20260601/)

在发表于《科学进展》（*Science Advances*，2025年）和bioRxiv的一项研究中，生物化学家塞巴斯蒂安·方丹（Sébastien Fontaine）及其团队报告了一项惊人的发现：经过灭菌处理的土壤样本在长达六年的时间里持续“呼吸”——即消耗氧气并排放二氧化碳。尽管这些土壤经过了伽马射线的强力照射且未表现出任何DNA或RNA迹象，但它仍保持着稳定的类代谢输出。

研究人员发现，向灭菌土壤中添加葡萄糖会导致排放量激增，这表明存在一种非生物过程在分解糖分。利用燃料电池，他们检测到了预示着氧依赖性代谢的电子流，并识别出几种与克雷布斯循环（Krebs cycle）相关的中间分子——该循环此前被认为仅发生在活细胞内。这些发现表明，某些生化反应实际上可能是地质环境的一种自然特征。

这一发现支持了生命起源的“代谢优先”理论。有机化学家约瑟夫·莫兰（Joseph Moran）等专家认为，生命的化学本质上就是地质的化学，铁和铝的氧化物等矿物质充当了这些反应的催化剂，而这些反应在第一个细胞出现之前就已经存在。虽然一些怀疑者认为死掉的微生物释放出的残留酶可能是这些活动的诱因，但方丹的团队反驳称，在如此严苛的环境中，酶不太可能保持长达六年的稳定性和功能。

最终，这项研究表明，代谢的基本过程可以独立于生物学而运作。这挑战了区分生命与复杂地球化学的传统界限，暗示生命的先驱可能早在遗传物质出现之前，就已经在地壳中自发产生。

---

## 7. 我故意让手机变慢了。

**原文标题**: I made my phone slow on purpose

**原文链接**: [https://vinewallapp.com/notes/i-made-my-phone-slow-on-purpose/](https://vinewallapp.com/notes/i-made-my-phone-slow-on-purpose/)

In the article "I made my phone slow on purpose," founder Guilherme Campos explains his unconventional approach to curing "doomscrolling" by intentionally throttling his iPhone’s performance. After traditional methods like app blockers failed, Campos realized that the instant gratification of high-speed content was the root of the addiction.

Using a "cookie machine" analogy, Campos argues that we overconsume rewards when they are effortless and high-quality. To combat this, he developed **VineWall**, an iOS app designed to make digital content "stale" and harder to access by controlling internet speeds. 

Instead of blocking apps entirely, VineWall progressively degrades the user experience:
*   **Initial Throttling:** Caps speeds to make videos appear "blocky" and low-resolution.
*   **Increased Throttling:** As scrolling continues, the connection tightens, replacing images with gray boxes on platforms like Reddit and X.
*   **The "Spinner" Effect:** Eventually, the user is left staring at loading spinners.

By intentionally making the internet frustratingly slow, the app removes the dopamine hit associated with seamless scrolling. This friction forces users to question whether the content is actually worth the wait, effectively breaking the cycle of mindless consumption through artificial scarcity and decreased visual appeal.

---

## 8. GitHub 与针对软件的罪行

**原文标题**: GitHub and the crime against software

**原文链接**: [https://eblog.fly.dev/githubbad.html](https://eblog.fly.dev/githubbad.html)

在《GitHub 与对软件的犯罪》一文中，Efron Licht 指出 GitHub 是软件行业“基础设施腐朽”的一个典型案例。作为一名分布式系统专家，Licht 认为 GitHub 已经放弃了提供高可用性工具的核心使命，转而盲目追求 AI 功能。

文章的主要观点包括：

*   **自招的不稳定性**：GitHub 将频繁的宕机归咎于“代理式开发”（AI 驱动的活动）的激增。Licht 断言这是一种“自导自演的 DDoS 攻击”，因为微软（GitHub 的母公司）强行将 AI 代理塞进平台的每一个角落，从而推高了他们自称无法承受的负载。
*   **炒作优于可靠性**：Licht 指出 GitHub 的公开宣传与其行为之间存在脱节。尽管微软声称“可用性至上”，但其更新日志却被 “Copilot” 和“代理”相关更新占据，对“性能”或“可靠性”只字未提。
*   **技术腐朽**：作者形容 GitHub 的前端“臃肿得滑稽”、运行缓慢，且在非 Chrome 浏览器上极易崩溃。他将前端比作“披萨店的用餐区”——如果到处是“老鼠”（Bug 和臃肿代码），那么“厨房”（后端架构）很可能也同样糟糕。
*   **关于运行时间的谎言**：Licht 指责 GitHub 在 99.8% 的运行时间数据上撒谎，并称用户的实际体验表明该数值要低得多，且频繁违反服务水平协议（SLA）。
*   **对比中的败北**：通过一项针对代码库托管服务的对比实验，Licht 在资源效率和代码质量方面给 GitHub 打出了“F”评分，而 GitLab 和 Codeberg 等竞争对手因不那么臃肿而获得了更高的评价。

最后，Licht 得出结论，GitHub 的问题是根源性的。他警告说，由于该平台的“骨架”已坏，任何渐进式的修补都无法解决其系统性的可靠性问题。

---

## 9. A 10 year old Xeon is all you need

**原文标题**: A 10 year old Xeon is all you need

**原文链接**: [https://point.free/blog/gemma-4-on-a-2016-xeon/](https://point.free/blog/gemma-4-on-a-2016-xeon/)

生成摘要时出错

---

## 10. Stealing from Biologists to Compile Haskell Faster

**原文标题**: Stealing from Biologists to Compile Haskell Faster

**原文链接**: [https://www.iankduncan.com/engineering/2026-05-30-stealing-from-biologists-to-compile-haskell-faster/](https://www.iankduncan.com/engineering/2026-05-30-stealing-from-biologists-to-compile-haskell-faster/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 2 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 3 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 4 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 5 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 6 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 7 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 8 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 9 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 10 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 11 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 12 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 13 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 14 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 15 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 16 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 17 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 18 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 19 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 20 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 21 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 22 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 23 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 24 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 25 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 26 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 27 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 28 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 29 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 30 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 31 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 32 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 33 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 34 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 35 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 36 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 37 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 38 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 39 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 40 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 41 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 42 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 43 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 44 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 45 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 46 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 47 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 48 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 49 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 50 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 51 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 52 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 53 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 54 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 55 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 56 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 57 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 58 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 59 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 60 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 61 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 62 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 63 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 64 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 65 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 66 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 67 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 68 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 69 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 70 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 71 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 72 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 73 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 74 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 75 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 76 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 77 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 78 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 79 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 80 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 81 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 82 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 83 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 84 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 85 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 86 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 87 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 88 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 89 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 90 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 91 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 92 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 93 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 94 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 95 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 96 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 97 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 98 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 99 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 100 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 101 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 102 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 103 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 104 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 105 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 106 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 107 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 108 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 109 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 110 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 111 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 112 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 113 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 114 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 115 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 116 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 117 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 118 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 119 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 120 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 121 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 122 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 123 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 124 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 125 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 126 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 127 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 128 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 129 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 130 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 131 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 132 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 133 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 134 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 135 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 136 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 137 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 138 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 139 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 140 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 141 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 142 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 143 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 144 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 145 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 146 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 147 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 148 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 149 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 150 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 151 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 152 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 153 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 154 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 155 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 156 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 157 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 158 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 159 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 160 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 161 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 162 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 163 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 164 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 165 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 166 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 167 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 168 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 169 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 170 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 171 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 172 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 173 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 174 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 175 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 176 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 177 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 178 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 179 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 180 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 181 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 182 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 183 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 184 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 185 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 186 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 187 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 188 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 189 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 190 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 191 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 192 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 193 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 194 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 195 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 196 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 197 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 198 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 199 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 200 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 201 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 202 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 203 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 204 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 205 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 206 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 207 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 208 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 209 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 210 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 211 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 212 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 213 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 214 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 215 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 216 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 217 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 218 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 219 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 220 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 221 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 222 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 223 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 224 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 225 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 226 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 227 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 228 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 229 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 230 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 231 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 232 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 233 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 234 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 235 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 236 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 237 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 238 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 239 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 240 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 241 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 242 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 243 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 244 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 245 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 246 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 247 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 248 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 249 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 250 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 251 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 252 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 253 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 254 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 255 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 256 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 257 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 258 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 259 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 260 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 261 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 262 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 263 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 264 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 265 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 266 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 267 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 268 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 269 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 270 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 271 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 272 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 273 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 274 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 275 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 276 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 277 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 278 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 279 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 280 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 281 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 282 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 283 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 284 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 285 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 286 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 287 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 288 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 289 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 290 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 291 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 292 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 293 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 294 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 295 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 296 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 297 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 298 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 299 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 300 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 301 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 302 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 303 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 304 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 305 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 306 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 307 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 308 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 309 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 310 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 311 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 312 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 313 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 314 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 315 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 316 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 317 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 318 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 319 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 320 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 321 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 322 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 323 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 324 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 325 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 326 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 327 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 328 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 329 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 330 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 331 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 332 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 333 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 334 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 335 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 336 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 337 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 338 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 339 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 340 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 341 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 342 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 343 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 344 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 345 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 346 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 347 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 348 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 349 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 350 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 351 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 352 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 353 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 354 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 355 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 356 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 357 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 358 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 359 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 360 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 361 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 362 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 363 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 364 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 365 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 366 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 367 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 368 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 369 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 370 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 371 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 372 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 373 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 374 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 375 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 376 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 377 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 378 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 379 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 380 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 381 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 382 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 383 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 384 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 385 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 386 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 387 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 388 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 389 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 390 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 391 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 392 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 393 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 394 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 395 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 396 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 397 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 398 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 399 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 400 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 401 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 402 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 403 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 404 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 405 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 406 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 407 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 408 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 409 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 410 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 411 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 412 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 413 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 414 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 415 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 416 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 417 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 418 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 419 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 420 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 421 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 422 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 423 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 424 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 425 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 426 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 427 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 428 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 429 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 430 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 431 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 432 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 433 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 434 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 435 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 436 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 437 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 438 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
