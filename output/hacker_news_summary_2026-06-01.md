# Hacker News 热门文章摘要 (2026-06-01)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. GrapheneOS Speech Services version 2 released

**原文标题**: GrapheneOS Speech Services version 2 released

**原文链接**: [https://discuss.grapheneos.org/d/36001-grapheneos-speech-services-version-2-released](https://discuss.grapheneos.org/d/36001-grapheneos-speech-services-version-2-released)

生成摘要时出错

---

## 12. Anthropic confidentially submits draft S-1 to the SEC

**原文标题**: Anthropic confidentially submits draft S-1 to the SEC

**原文链接**: [https://www.anthropic.com/news/confidential-draft-s1-sec](https://www.anthropic.com/news/confidential-draft-s1-sec)

生成摘要时出错

---

## 13. Nvidia RTX Spark

**原文标题**: Nvidia RTX Spark

**原文链接**: [https://www.nvidia.com/en-us/products/rtx-spark/](https://www.nvidia.com/en-us/products/rtx-spark/)

生成摘要时出错

---

## 14. Debug Project

**原文标题**: Debug Project

**原文链接**: [https://debug.com/](https://debug.com/)

生成摘要时出错

---

## 15. Microsoft builds MacBook Pro rival with NVIDIA-powered Surface Laptop Ultra

**原文标题**: Microsoft builds MacBook Pro rival with NVIDIA-powered Surface Laptop Ultra

**原文链接**: [https://www.windowslatest.com/2026/06/01/microsoft-builds-its-ultimate-macbook-pro-rival-with-the-nvidia-powered-surface-laptop-ultra/](https://www.windowslatest.com/2026/06/01/microsoft-builds-its-ultimate-macbook-pro-rival-with-the-nvidia-powered-surface-laptop-ultra/)

生成摘要时出错

---

## 16. Windows GOG DOS Games on M-Series Macs

**原文标题**: Windows GOG DOS Games on M-Series Macs

**原文链接**: [https://f055.net/technology/windows-gog-dos-games-on-m-series-macs/](https://f055.net/technology/windows-gog-dos-games-on-m-series-macs/)

生成摘要时出错

---

## 17. Malicious npm packages detected across Red Hat Cloud Services

**原文标题**: Malicious npm packages detected across Red Hat Cloud Services

**原文链接**: [https://github.com/RedHatInsights/javascript-clients/issues/492](https://github.com/RedHatInsights/javascript-clients/issues/492)

生成摘要时出错

---

## 18. Flipper Zero Zig Template

**原文标题**: Flipper Zero Zig Template

**原文链接**: [https://github.com/NishantJoshi00/flipper-template](https://github.com/NishantJoshi00/flipper-template)

生成摘要时出错

---

## 19. Only 17% of all 64-bit Integers are products of two 32-bit integers

**原文标题**: Only 17% of all 64-bit Integers are products of two 32-bit integers

**原文链接**: [https://lemire.me/blog/2026/05/22/only-17-of-all-64-bit-integers-are-products-of-two-32-bit-integers/](https://lemire.me/blog/2026/05/22/only-17-of-all-64-bit-integers-are-products-of-two-32-bit-integers/)

生成摘要时出错

---

## 20. The Pirate Bay Remains Resilient, 20 Years After the Raid

**原文标题**: The Pirate Bay Remains Resilient, 20 Years After the Raid

**原文链接**: [https://torrentfreak.com/the-pirate-bay-remains-resilient-20-years-after-the-raid/](https://torrentfreak.com/the-pirate-bay-remains-resilient-20-years-after-the-raid/)

生成摘要时出错

---

## 21. Superintelligence: The Idea That Eats Smart People (2016)

**原文标题**: Superintelligence: The Idea That Eats Smart People (2016)

**原文链接**: [https://idlewords.com/talks/superintelligence.htm](https://idlewords.com/talks/superintelligence.htm)

生成摘要时出错

---

## 22. Sysadmining Like It's 2009

**原文标题**: Sysadmining Like It's 2009

**原文链接**: [https://lambdacreate.com/posts/sysadmining-like-its-2009](https://lambdacreate.com/posts/sysadmining-like-its-2009)

生成摘要时出错

---

## 23. Linux Basics for Hackers (2019)

**原文标题**: Linux Basics for Hackers (2019)

**原文链接**: [https://github.com/ahegazy0/linux-basics-for-hackers-notes](https://github.com/ahegazy0/linux-basics-for-hackers-notes)

生成摘要时出错

---

## 24. Handmade Hawaiian Islands Map

**原文标题**: Handmade Hawaiian Islands Map

**原文链接**: [https://www.notesfromtheroad.com/roam/hawaiian-islands-map.html](https://www.notesfromtheroad.com/roam/hawaiian-islands-map.html)

生成摘要时出错

---

## 25. Florida AG files lawsuit against OpenAI, CEO Sam Altman for deceptive practices

**原文标题**: Florida AG files lawsuit against OpenAI, CEO Sam Altman for deceptive practices

**原文链接**: [https://www.myfloridalegal.com/newsrelease/attorney-general-james-uthmeier-files-first-nation-state-led-lawsuit-against-openai-ceo](https://www.myfloridalegal.com/newsrelease/attorney-general-james-uthmeier-files-first-nation-state-led-lawsuit-against-openai-ceo)

生成摘要时出错

---

## 26. Show HN: A CSS 3D Engine (no WebGL)

**原文标题**: Show HN: A CSS 3D Engine (no WebGL)

**原文链接**: [https://github.com/LayoutitStudio/polycss](https://github.com/LayoutitStudio/polycss)

生成摘要时出错

---

## 27. Show HN: Textile – A desktop app for weaving together bits of text

**原文标题**: Show HN: Textile – A desktop app for weaving together bits of text

**原文链接**: [https://www.gettextile.app](https://www.gettextile.app)

生成摘要时出错

---

## 28. Tracing HTTP Requests with Go's net/HTTP/httptrace

**原文标题**: Tracing HTTP Requests with Go's net/HTTP/httptrace

**原文链接**: [https://blainsmith.com/articles/httptrace-with-go/](https://blainsmith.com/articles/httptrace-with-go/)

生成摘要时出错

---

## 29. Radxa Dragon Q8B: A Laptop Cosplaying as an SBC?

**原文标题**: Radxa Dragon Q8B: A Laptop Cosplaying as an SBC?

**原文链接**: [https://bret.dk/radxa-dragon-q8b-a-laptop-cosplaying-as-an-sbc/](https://bret.dk/radxa-dragon-q8b-a-laptop-cosplaying-as-an-sbc/)

生成摘要时出错

---

## 30. My 15-year-old relative was killed for refusing to marry her cousin

**原文标题**: My 15-year-old relative was killed for refusing to marry her cousin

**原文链接**: [https://www.theguardian.com/global-development/2026/jun/01/kawthar-al-husayjawi-killed-refusing-forced-marriage-marry-family-celebrated-iraq](https://www.theguardian.com/global-development/2026/jun/01/kawthar-al-husayjawi-killed-refusing-forced-marriage-marry-family-celebrated-iraq)

生成摘要时出错

---

## 31. “The Apple Boogie“ 1987 Mac Promo Album Cassette Tape [video]

**原文标题**: “The Apple Boogie“ 1987 Mac Promo Album Cassette Tape [video]

**原文链接**: [https://www.youtube.com/watch?v=chJHB-btMNI](https://www.youtube.com/watch?v=chJHB-btMNI)

生成摘要时出错

---

## 32. Build a Basic AI Agent from Scratch: Tools

**原文标题**: Build a Basic AI Agent from Scratch: Tools

**原文链接**: [https://www.ruxu.dev/articles/ai/build-an-ai-agent-with-tools/](https://www.ruxu.dev/articles/ai/build-an-ai-agent-with-tools/)

生成摘要时出错

---

## 33. Cessation of public development of Kefir C compiler

**原文标题**: Cessation of public development of Kefir C compiler

**原文链接**: [https://kefir.protopopov.lv/posts/announce2.html](https://kefir.protopopov.lv/posts/announce2.html)

生成摘要时出错

---

## 34. DuckDuckGo makes its 'no-AI' search engine easier to access as its traffic booms

**原文标题**: DuckDuckGo makes its 'no-AI' search engine easier to access as its traffic booms

**原文链接**: [https://techcrunch.com/2026/06/01/duckduckgo-makes-its-no-ai-search-engine-easier-to-access-as-its-traffic-booms/](https://techcrunch.com/2026/06/01/duckduckgo-makes-its-no-ai-search-engine-easier-to-access-as-its-traffic-booms/)

生成摘要时出错

---

## 35. Decades of Effort Restore Steelhead and Salmon Passage on Alameda Creek

**原文标题**: Decades of Effort Restore Steelhead and Salmon Passage on Alameda Creek

**原文链接**: [https://www.fisheries.noaa.gov/feature-story/decades-effort-restore-steelhead-and-salmon-passage-californias-alameda-creek](https://www.fisheries.noaa.gov/feature-story/decades-effort-restore-steelhead-and-salmon-passage-californias-alameda-creek)

生成摘要时出错

---

## 36. Using Git's rerere feature to escape recurring conflict hell

**原文标题**: Using Git's rerere feature to escape recurring conflict hell

**原文链接**: [https://gist.github.com/skipcloud/f1033afb4fa5681d69fa63458cc95928](https://gist.github.com/skipcloud/f1033afb4fa5681d69fa63458cc95928)

生成摘要时出错

---

## 37. Asserts in Zig

**原文标题**: Asserts in Zig

**原文链接**: [https://kristoff.it/blog/fix-your-asserts/](https://kristoff.it/blog/fix-your-asserts/)

生成摘要时出错

---

## 38. Remote work, not AI, has sidelined recent college graduates, research finds

**原文标题**: Remote work, not AI, has sidelined recent college graduates, research finds

**原文链接**: [https://text.npr.org/nx-s1-5843076](https://text.npr.org/nx-s1-5843076)

生成摘要时出错

---

## 39. Nvidia Cosmos 3

**原文标题**: Nvidia Cosmos 3

**原文链接**: [https://developer.nvidia.com/blog/develop-physical-ai-reasoning-world-and-action-models-with-nvidia-cosmos-3/](https://developer.nvidia.com/blog/develop-physical-ai-reasoning-world-and-action-models-with-nvidia-cosmos-3/)

生成摘要时出错

---

## 40. Visa invests in Replit to power agentic payments for developers

**原文标题**: Visa invests in Replit to power agentic payments for developers

**原文链接**: [https://techcrunch.com/2026/05/28/visa-invests-in-replit-to-power-agentic-payments-for-developers/](https://techcrunch.com/2026/05/28/visa-invests-in-replit-to-power-agentic-payments-for-developers/)

生成摘要时出错

---

## 41. Qwen3.7-Plus: Multimodal Agent Intelligence

**原文标题**: Qwen3.7-Plus: Multimodal Agent Intelligence

**原文链接**: [https://qwen.ai/blog?id=qwen3.7-plus](https://qwen.ai/blog?id=qwen3.7-plus)

生成摘要时出错

---

## 42. Benchmarking SurrealDB 3.x vs. Postgres, Mongo, Neo4j and Redis (With Fsync)

**原文标题**: Benchmarking SurrealDB 3.x vs. Postgres, Mongo, Neo4j and Redis (With Fsync)

**原文链接**: [https://surrealdb.com/blog/surrealdb-3-x-by-the-numbers](https://surrealdb.com/blog/surrealdb-3-x-by-the-numbers)

生成摘要时出错

---

## 43. Movwin: My (Unpublished) TUI Framework

**原文标题**: Movwin: My (Unpublished) TUI Framework

**原文链接**: [https://movq.de/blog/postings/2026-05-29/0/POSTING-en.html](https://movq.de/blog/postings/2026-05-29/0/POSTING-en.html)

生成摘要时出错

---

## 44. Checking Assembly with Z3

**原文标题**: Checking Assembly with Z3

**原文链接**: [https://bernsteinbear.com/blog/asm-z3/](https://bernsteinbear.com/blog/asm-z3/)

生成摘要时出错

---

## 45. Pogroms, American Style

**原文标题**: Pogroms, American Style

**原文链接**: [https://paulkrugman.substack.com/p/pogroms-american-style](https://paulkrugman.substack.com/p/pogroms-american-style)

生成摘要时出错

---

## 46. 迈克尔·伯里称英伟达与SpaceX的芯片交易为“虚假骗局”。

**原文标题**: Michael Burry Just Called Nvidia's SpaceX Chip Deal 'Fugazi.'

**原文链接**: [https://247wallst.com/investing/2026/06/01/michael-burry-just-called-nvidias-spacex-chip-deal-fugazi-heres-why-it-all-seems-wrong/](https://247wallst.com/investing/2026/06/01/michael-burry-just-called-nvidias-spacex-chip-deal-fugazi-heres-why-it-all-seems-wrong/)

生成摘要时出错

---

## 47. The SLAX Scripting Language: An Alternate Syntax for XSLT

**原文标题**: The SLAX Scripting Language: An Alternate Syntax for XSLT

**原文链接**: [http://juniper.github.io/libslax/slax-manual.html](http://juniper.github.io/libslax/slax-manual.html)

生成摘要时出错

---

## 48. The Genius of the Barn Owl's Feathers

**原文标题**: The Genius of the Barn Owl's Feathers

**原文链接**: [https://thereader.mitpress.mit.edu/the-genius-of-the-barn-owls-feathers/](https://thereader.mitpress.mit.edu/the-genius-of-the-barn-owls-feathers/)

生成摘要时出错

---

## 49. Announcing Zstandard in Rust

**原文标题**: Announcing Zstandard in Rust

**原文链接**: [https://trifectatech.org/blog/announcing-zstandard-in-rust/](https://trifectatech.org/blog/announcing-zstandard-in-rust/)

生成摘要时出错

---

## 50. Meta launches Instagram, Facebook, and WhatsApp subscriptions

**原文标题**: Meta launches Instagram, Facebook, and WhatsApp subscriptions

**原文链接**: [https://techcrunch.com/2026/05/27/meta-officially-launches-instagram-facebook-and-whatsapp-subscriptions-with-more-to-come-including-ai-plans/](https://techcrunch.com/2026/05/27/meta-officially-launches-instagram-facebook-and-whatsapp-subscriptions-with-more-to-come-including-ai-plans/)

生成摘要时出错

---

## 51. Ohio hits pause on datacenter tax breaks draining its coffers

**原文标题**: Ohio hits pause on datacenter tax breaks draining its coffers

**原文链接**: [https://www.theregister.com/on-prem/2026/06/01/ohio-hits-pause-on-datacenter-tax-breaks-draining-its-coffers/5249137](https://www.theregister.com/on-prem/2026/06/01/ohio-hits-pause-on-datacenter-tax-breaks-draining-its-coffers/5249137)

生成摘要时出错

---

## 52. Macron announces 93B euros in 'Choose France' investments

**原文标题**: Macron announces 93B euros in 'Choose France' investments

**原文链接**: [https://www.euractiv.com/news/macron-announces-93-bn-euros-in-choose-france-investments/](https://www.euractiv.com/news/macron-announces-93-bn-euros-in-choose-france-investments/)

生成摘要时出错

---

## 53. The Infosec Phrasebook

**原文标题**: The Infosec Phrasebook

**原文链接**: [https://nesbitt.io/2026/06/01/the-infosec-phrasebook.html](https://nesbitt.io/2026/06/01/the-infosec-phrasebook.html)

生成摘要时出错

---

## 54. Blorp Language

**原文标题**: Blorp Language

**原文链接**: [https://blorp-lang.org/](https://blorp-lang.org/)

生成摘要时出错

---

## 55. We Are Living in Pinocchio's World

**原文标题**: We Are Living in Pinocchio's World

**原文链接**: [https://om.co/2026/05/25/we-are-living-in-pinocchios-world/](https://om.co/2026/05/25/we-are-living-in-pinocchios-world/)

生成摘要时出错

---

## 56. What if remote working, not AI, is to blame for weak junior hiring?

**原文标题**: What if remote working, not AI, is to blame for weak junior hiring?

**原文链接**: [https://www.ft.com/content/2205e2d0-50dc-4e80-9bf7-78d0272276c0](https://www.ft.com/content/2205e2d0-50dc-4e80-9bf7-78d0272276c0)

生成摘要时出错

---

## 57. Homing pigeons navigate via superparamagnetic macrophages when sky is overcast

**原文标题**: Homing pigeons navigate via superparamagnetic macrophages when sky is overcast

**原文链接**: [https://www.science.org/doi/10.1126/science.ady2486](https://www.science.org/doi/10.1126/science.ady2486)

生成摘要时出错

---

## 58. Is Python Becoming Pinyin?

**原文标题**: Is Python Becoming Pinyin?

**原文链接**: [https://lernerpython.com/2026/05/19/is-python-becoming-pinyin/](https://lernerpython.com/2026/05/19/is-python-becoming-pinyin/)

生成摘要时出错

---

## 59. KDE at 30

**原文标题**: KDE at 30

**原文链接**: [https://kde.org/anniversaries/30/](https://kde.org/anniversaries/30/)

生成摘要时出错

---

## 60. Amazon Shuts Down Internal AI Leaderboard After Employees Cheated

**原文标题**: Amazon Shuts Down Internal AI Leaderboard After Employees Cheated

**原文链接**: [https://www.404media.co/amazon-shuts-down-internal-ai-leaderboard-after-employees-cheated/](https://www.404media.co/amazon-shuts-down-internal-ai-leaderboard-after-employees-cheated/)

生成摘要时出错

---

## 61. Cloudflare Turnstile requiring fingerprintable WebGL

**原文标题**: Cloudflare Turnstile requiring fingerprintable WebGL

**原文链接**: [https://hacktivis.me/articles/cloudflare-turnstile-webgl-fingerprinting](https://hacktivis.me/articles/cloudflare-turnstile-webgl-fingerprinting)

生成摘要时出错

---

## 62. Chuwi Minibook X

**原文标题**: Chuwi Minibook X

**原文链接**: [https://tylercipriani.com/blog/2026/05/28/chuwi-minibook-x/](https://tylercipriani.com/blog/2026/05/28/chuwi-minibook-x/)

生成摘要时出错

---

## 63. Websites have a new way to spy on visitors: analyzing their SSD activity

**原文标题**: Websites have a new way to spy on visitors: analyzing their SSD activity

**原文链接**: [https://arstechnica.com/security/2026/05/websites-have-a-new-way-to-spy-on-visitors-analyzing-their-ssd-activity/](https://arstechnica.com/security/2026/05/websites-have-a-new-way-to-spy-on-visitors-analyzing-their-ssd-activity/)

生成摘要时出错

---

## 64. Why _Am_ I Interested in Your Company?

**原文标题**: Why _Am_ I Interested in Your Company?

**原文链接**: [https://jjmojojjmojo.github.io/why-am-i-interested-in-your-company.html](https://jjmojojjmojo.github.io/why-am-i-interested-in-your-company.html)

生成摘要时出错

---

## 65. The four programming questions from my 1994 Microsoft internship interview (2023)

**原文标题**: The four programming questions from my 1994 Microsoft internship interview (2023)

**原文链接**: [https://www.computerenhance.com/p/the-four-programming-questions-from](https://www.computerenhance.com/p/the-four-programming-questions-from)

生成摘要时出错

---

## 66. Rubin Tracks Skyscraper-Size Asteroids and Failed Supernovas

**原文标题**: Rubin Tracks Skyscraper-Size Asteroids and Failed Supernovas

**原文链接**: [https://www.quantamagazine.org/rubin-tracks-skyscraper-size-asteroids-failed-supernovas-and-interstellar-visitors-20260515/](https://www.quantamagazine.org/rubin-tracks-skyscraper-size-asteroids-failed-supernovas-and-interstellar-visitors-20260515/)

生成摘要时出错

---

## 67. The TfL Cupboard Filled with Lost Tube Moquettes

**原文标题**: The TfL Cupboard Filled with Lost Tube Moquettes

**原文链接**: [https://londonist.com/london/transport/moquettes-that-never-were](https://londonist.com/london/transport/moquettes-that-never-were)

生成摘要时出错

---

## 68. Telli (YC F24) is hiring in engineering, design, and GTM [Berlin, on-site]

**原文标题**: Telli (YC F24) is hiring in engineering, design, and GTM [Berlin, on-site]

**原文链接**: [https://hi.telli.com/join-us](https://hi.telli.com/join-us)

生成摘要时出错

---

## 69. Hackers Asked Meta AI to Give Them Access to Instagram Accounts. It Worked

**原文标题**: Hackers Asked Meta AI to Give Them Access to Instagram Accounts. It Worked

**原文链接**: [https://www.404media.co/hackers-simply-asked-meta-ai-to-give-them-access-to-high-profile-instagram-accounts-it-worked/](https://www.404media.co/hackers-simply-asked-meta-ai-to-give-them-access-to-high-profile-instagram-accounts-it-worked/)

The provided article from 404 Media reports on a significant security vulnerability involving Meta’s AI-driven support chatbot. According to the report, hackers have successfully hijacked high-profile Instagram accounts—including those belonging to the Barack Obama White House, the Chief Master Sergeant of Space Force, and Sephora—by exploiting the AI's account recovery features.

The core of the issue lies in the AI support bot’s ability to perform critical maintenance tasks, such as resetting passwords and changing account-associated email addresses. Hackers reportedly used social engineering prompts to convince the chatbot to link target accounts to new, attacker-controlled email addresses. Videos circulating in hacking communities demonstrate that the process was unexpectedly simple, requiring only basic requests to change account details.

This situation highlights the risks of offloading sensitive security functions to automated AI systems without sufficient oversight. Victims of these takeovers have expressed frustration, noting that Meta’s reliance on AI has removed traditional pathways to escalate problems to human support agents. While Meta intended the AI to provide "solutions, not just suggestions," the feature appears to have created a critical bottleneck for legitimate users while inadvertently providing a streamlined entry point for malicious actors.

---

## 70. Unix in East Germany (GDR) (1990)

**原文标题**: Unix in East Germany (GDR) (1990)

**原文链接**: [https://groups.google.com/g/comp.unix.wizards/c/QX_dxElrVNs](https://groups.google.com/g/comp.unix.wizards/c/QX_dxElrVNs)

生成摘要时出错

---

## 71. Finding success in industry as a chip designer

**原文标题**: Finding success in industry as a chip designer

**原文链接**: [https://spectrum.ieee.org/chip-design-academic-vs-industry](https://spectrum.ieee.org/chip-design-academic-vs-industry)

生成摘要时出错

---

## 72. The Speed of Prototyping in the Age of AI

**原文标题**: The Speed of Prototyping in the Age of AI

**原文链接**: [https://darylcecile.net/notes/speed-of-prototyping-age-of-ai](https://darylcecile.net/notes/speed-of-prototyping-age-of-ai)

生成摘要时出错

---

## 73. Having your insulin pump die while you're on vacation

**原文标题**: Having your insulin pump die while you're on vacation

**原文链接**: [https://blog.lauramichet.com/what-its-like-to-have-the-machine-that-keeps-you-alive-die-while-youre-on-vacation/](https://blog.lauramichet.com/what-its-like-to-have-the-machine-that-keeps-you-alive-die-while-youre-on-vacation/)

生成摘要时出错

---

## 74. Iran stops negotiations with U.S., vows to 'completely' block Strait of Hormuz

**原文标题**: Iran stops negotiations with U.S., vows to 'completely' block Strait of Hormuz

**原文链接**: [https://www.cnbc.com/2026/06/01/iran-us-negotiations-strait-of-hormuz.html](https://www.cnbc.com/2026/06/01/iran-us-negotiations-strait-of-hormuz.html)

生成摘要时出错

---

## 75. New Beam Spring Keyboards

**原文标题**: New Beam Spring Keyboards

**原文链接**: [https://www.modelfkeyboards.com/product/beam-spring-b104-keyboard/](https://www.modelfkeyboards.com/product/beam-spring-b104-keyboard/)

生成摘要时出错

---

## 76. Restartable Sequences

**原文标题**: Restartable Sequences

**原文链接**: [https://justine.lol/rseq/](https://justine.lol/rseq/)

生成摘要时出错

---

## 77. Anthropic Files to Go Public, Setting Stage for Huge I.P.O.

**原文标题**: Anthropic Files to Go Public, Setting Stage for Huge I.P.O.

**原文链接**: [https://www.nytimes.com/2026/06/01/technology/anthropic-ipo.html](https://www.nytimes.com/2026/06/01/technology/anthropic-ipo.html)

生成摘要时出错

---

## 78. Linux/M68k

**原文标题**: Linux/M68k

**原文链接**: [http://www.linux-m68k.org/](http://www.linux-m68k.org/)

生成摘要时出错

---

## 79. Codex just found a "workaround" of not having sudo on my PC

**原文标题**: Codex just found a "workaround" of not having sudo on my PC

**原文链接**: [https://twitter.com/i/status/2060746160558543217](https://twitter.com/i/status/2060746160558543217)

生成摘要时出错

---

## 80. ChatGPT for Google Sheets exfiltrates workbooks

**原文标题**: ChatGPT for Google Sheets exfiltrates workbooks

**原文链接**: [https://www.promptarmor.com/resources/gpt-for-google-sheets-data-exfiltration](https://www.promptarmor.com/resources/gpt-for-google-sheets-data-exfiltration)

生成摘要时出错

---

## 81. Dav2d

**原文标题**: Dav2d

**原文链接**: [https://jbkempf.com/blog/2026/dav2d/](https://jbkempf.com/blog/2026/dav2d/)

生成摘要时出错

---

## 82. 1-Bit Bonsai Image 4B Image Generation for Local Devices

**原文标题**: 1-Bit Bonsai Image 4B Image Generation for Local Devices

**原文链接**: [https://prismml.com/news/bonsai-image-4b](https://prismml.com/news/bonsai-image-4b)

生成摘要时出错

---

## 83. AI in SRE: Where and how Google is deploying agentic AI to improve operations

**原文标题**: AI in SRE: Where and how Google is deploying agentic AI to improve operations

**原文链接**: [https://cloud.google.com/blog/products/devops-sre/how-google-sre-is-using-agentic-ai-to-improve-operations](https://cloud.google.com/blog/products/devops-sre/how-google-sre-is-using-agentic-ai-to-improve-operations)

生成摘要时出错

---

## 84. Show HN: Streambed – Stream Postgres to Iceberg on S3, Supports Postgres Wire

**原文标题**: Show HN: Streambed – Stream Postgres to Iceberg on S3, Supports Postgres Wire

**原文链接**: [https://github.com/viggy28/streambed](https://github.com/viggy28/streambed)

生成摘要时出错

---

## 85. United Airlines 767 returns to Newark after Bluetooth name sparks alert

**原文标题**: United Airlines 767 returns to Newark after Bluetooth name sparks alert

**原文链接**: [https://simpleflying.com/united-airlines-767-returns-newark-bluetooth-name-alert/](https://simpleflying.com/united-airlines-767-returns-newark-bluetooth-name-alert/)

生成摘要时出错

---

## 86. Backpressure is all you need

**原文标题**: Backpressure is all you need

**原文链接**: [https://www.lucasfcosta.com/blog/backpressure-is-all-you-need](https://www.lucasfcosta.com/blog/backpressure-is-all-you-need)

生成摘要时出错

---

## 87. A powerful new chapter for Windows PCs, accelerated by Nvidia RTX Spark

**原文标题**: A powerful new chapter for Windows PCs, accelerated by Nvidia RTX Spark

**原文链接**: [https://blogs.windows.com/windowsexperience/2026/05/31/introducing-a-powerful-new-chapter-for-windows-pcs-accelerated-by-nvidia-rtx-spark/](https://blogs.windows.com/windowsexperience/2026/05/31/introducing-a-powerful-new-chapter-for-windows-pcs-accelerated-by-nvidia-rtx-spark/)

生成摘要时出错

---

## 88. Lean, Not Backpressure

**原文标题**: Lean, Not Backpressure

**原文链接**: [https://entropicthoughts.com/lean-not-backpressure](https://entropicthoughts.com/lean-not-backpressure)

生成摘要时出错

---

## 89. Odysseus – self-hosted AI workspace

**原文标题**: Odysseus – self-hosted AI workspace

**原文链接**: [https://github.com/pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus)

生成摘要时出错

---

## 90. Domain expertise has always been the real moat

**原文标题**: Domain expertise has always been the real moat

**原文链接**: [https://www.brethorsting.com/blog/2026/05/domain-expertise-has-always-been-the-real-moat/](https://www.brethorsting.com/blog/2026/05/domain-expertise-has-always-been-the-real-moat/)

生成摘要时出错

---

## 91. Re: [PATCH] OOM_pardon, a.k.a. don't kill my xlock (2004)

**原文标题**: Re: [PATCH] OOM_pardon, a.k.a. don't kill my xlock (2004)

**原文链接**: [https://lwn.net/Articles/104185/](https://lwn.net/Articles/104185/)

生成摘要时出错

---

## 92. What five simple habits can do over 35 years

**原文标题**: What five simple habits can do over 35 years

**原文链接**: [https://en.wikipedia.org/wiki/Caerphilly_Heart_Disease_Study](https://en.wikipedia.org/wiki/Caerphilly_Heart_Disease_Study)

生成摘要时出错

---

## 93. Textbooks in Tokenland

**原文标题**: Textbooks in Tokenland

**原文链接**: [https://systemsapproach.org/2026/06/01/textbooks-in-tokenland/](https://systemsapproach.org/2026/06/01/textbooks-in-tokenland/)

生成摘要时出错

---

## 94. Mechanical Pencil: An illustrated celebration of the engineering around us

**原文标题**: Mechanical Pencil: An illustrated celebration of the engineering around us

**原文链接**: [https://mechanical-pencil.com/](https://mechanical-pencil.com/)

生成摘要时出错

---

## 95. Security Envelope Pattern collection – S.E.C.R.E.T

**原文标题**: Security Envelope Pattern collection – S.E.C.R.E.T

**原文链接**: [https://secret-archive.org/](https://secret-archive.org/)

生成摘要时出错

---

## 96. Cloudflare CTO enforcing usage limits

**原文标题**: Cloudflare CTO enforcing usage limits

**原文链接**: [https://old.reddit.com/r/BetterOffline/comments/1tryfft/cloudflare_cto_enforcing_usage_limits/](https://old.reddit.com/r/BetterOffline/comments/1tryfft/cloudflare_cto_enforcing_usage_limits/)

生成摘要时出错

---

## 97. One year of Roto, a compiled scripting language for Rust

**原文标题**: One year of Roto, a compiled scripting language for Rust

**原文链接**: [https://blog.nlnetlabs.nl/one-year-of-roto-the-compiled-scripting-language-for-rust/](https://blog.nlnetlabs.nl/one-year-of-roto-the-compiled-scripting-language-for-rust/)

生成摘要时出错

---

## 98. FROST: Fingerprinting Remotely using OPFS-based SSD Timing [pdf]

**原文标题**: FROST: Fingerprinting Remotely using OPFS-based SSD Timing [pdf]

**原文链接**: [https://hannesweissteiner.com/pdfs/frost.pdf](https://hannesweissteiner.com/pdfs/frost.pdf)

生成摘要时出错

---

## 99. Avian Visitors

**原文标题**: Avian Visitors

**原文链接**: [https://theodore.net/projects/AvianVisitors/](https://theodore.net/projects/AvianVisitors/)

生成摘要时出错

---

## 100. Racket v9.2

**原文标题**: Racket v9.2

**原文链接**: [https://blog.racket-lang.org/2026/05/racket-v9-2.html](https://blog.racket-lang.org/2026/05/racket-v9-2.html)

生成摘要时出错

---

