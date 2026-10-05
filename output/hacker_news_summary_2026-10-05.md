# Hacker News 热门文章摘要 (2026-10-05)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Beam：Reflection 的 501B 开放权重模型

**原文标题**: Beam: Reflection's 501B open-weight model

**原文链接**: [https://reflection.ai/blog/introducing-beam](https://reflection.ai/blog/introducing-beam)

Reflection 推出了其首款开源权重的稀疏混合专家（MoE）模型 **Beam**，专为编程、推理和智能体工作负载而设计。Beam 拥有 **5010 亿总参数**（230 亿激活参数），在提供前沿性能的同时保持了极高的推理效率，其计算消耗仅为 GLM 5.2 和 Qwen 3.8-Max 等同类性能模型的 1/3 至 1/4。

该模型的能力源于预训练和强化学习（RL）的大规模扩展。Beam 在 **23.8 万亿 token** 上进行了预训练，并经历了迄今为止规模最大的强化学习训练之一：使用 1.05 万颗 NVIDIA GB300 GPU，历时四周，在 100 万个环境中生成了 1 亿次轨迹（rollouts）。

**核心技术亮点：**
*   **性能表现：** Beam 在专项基准测试中表现卓越，在 AIME 2026 上得分为 97.8%，在 GPQA Diamond 上为 90.5%，在 SWEBench Verified 上为 80.9%。
*   **推理控制：** 独特的“推理力度”（reasoning effort）参数允许用户在快速、节省 token 的响应与针对复杂任务的深度扩展推理之间进行切换。
*   **基础设施创新：** Reflection 开发了一个完全异步的强化学习平台，即使在存在“策略陈旧”（即利用旧版本模型生成的数据进行学习）的情况下也能保持稳定性。
*   **泛化能力：** 尽管是纯文本模型，Beam 仍展现出强大的智能体迁移能力，能够成功执行网页调研、调用 OCR API，并自主微调其他模型（如 Gemma-4）。

目前 Beam 正在进行最后的红队测试，其权重、技术报告和开发者工具包计划于本月晚些时候发布。早期访问现已开放申请。

---

## 2. 查找旧金山任意两点间最平坦的路线。

**原文标题**: Find the flattest route between any two points in SF

**原文链接**: [https://flattensf.com/](https://flattensf.com/)

**Flatten SF** 由 Drew Edwards 开发，是一款专门的网页端路径规划工具，旨在通过寻找最平坦的路径，帮助行人和骑行者在旧金山著名的多山地形中穿行。

该应用程序直接在用户的浏览器中处理超过 160,000 条街道段，利用高分辨率的 USGS 1米激光雷达高程数据，并结合了 Overture 和 OpenStreetMap 的街道图。其核心功能是一个交互式滑块，允许用户在最短距离与最低海拔增益之间进行权衡。在极端的“平坦”设置下，算法会将 1 英尺的垂直爬升视作等同于 200 英尺的水平步行距离，以此来判断绕路是否值得。

该工具的主要特点包括：
*   **特定模式逻辑：** 该工具在步行路线中自动包含楼梯，但在骑行路线中将其排除。
*   **累积海拔：** 该工具计算总的累积爬升增益，而非仅仅测量起点和终点之间的高度差，从而更准确地反映体力消耗。
*   **基于浏览器的性能：** 该工具在本地执行计算，并内置了旧金山地址、地点和交叉路口的离线搜索功能。

通过提供从最直接到最平坦的一系列可视化路径选择，Flatten SF 让用户能够根据自己的体力偏好或骑行设备自定义通勤路线。

---

## 3. Dust: 无需反向传播的 Transformer 预训练

**原文标题**: Dust: Pretraining Transformers Without Backpropagation

**原文链接**: [https://qlabs.sh/research/dust](https://qlabs.sh/research/dust)

**Dust** 是一种用于预训练 Transformer 的新型零阶优化方法，它为反向传播提供了一个极具竞争力的替代方案。与扰动模型权重的传统演化策略 (ES) 不同，Dust 采用**节点扰动**，在每个 token 上独立地为激活值添加高斯噪声。这创建了一个“虚拟种群”，只需一次前向传播即可并行评估数千个成员，使其效率比 EGGROLL 等先进的权重空间 ES 方法高出 $10^3$ 到 $10^4$ 倍。

主要发现和贡献包括：
*   **性能：** Dust 是首个在预训练中能与反向传播相媲美的零阶方法，在算力充足的情况下甚至能超越后者。这表明随着可用算力的规模化，基于搜索的方法最终可能会取代反向传播。
*   **可扩展性：** 作者挑战了传统观点，发现大型模型实际上比小型模型具有更高的种群效率。即使在高达 10 亿 token 的规模下，梯度估计仍与反向传播保持高度一致。
*   **机制：** 该算法根据局部和未来 token 损失的降低程度来奖励激活扰动。它通过计算奖励加权噪声与层输入的外积来估计权重梯度。
*   **实现：** 为了管理同时扰动之间的干扰，Dust 在不同的前向传播中对不同类型的层进行扰动，并利用缓存的“干净”激活值来减少冗余计算。

这项研究暗示了学习算法将向更通用、更“暴力”的方向转变。通过摆脱对可微性的严格要求，Dust 为训练复杂架构（例如涉及外部程序或长循环 Transformer 的架构）敞开了大门，而这些架构目前难以使用反向传播进行优化。

---

## 4. Opus 5.5 智能体发现两种室温磁性半导体候选材料

**原文标题**: Opus 5.5 agents discover two room-temperature magnetic semiconductor candidates

**原文链接**: [https://www.vals.ai/blogs/room-temperature-magnetic-semiconductors](https://www.vals.ai/blogs/room-temperature-magnetic-semiconductors)

AI智能体 (Opus 5.5) 发现了两种属于“Luttinger补偿 (LC) 磁体”类别的室温磁性半导体候选材料。这些材料在自旋电子学和计算机存储领域备受青睐，因为它们兼具了铁磁体和反铁磁体的最佳特性：它们具有零净磁场（可实现更密集、更快速的存储），同时保持了按自旋对电子进行排序的能力（这是读写数据所必需的）。

确定的两种候选材料为：

1.  **YBaMnFeO₅：** 这是一种由AI设计的化合物，预测具有2.35 eV的带隙，且磁稳定性高达490 K。虽然它为数据存储提供了巨大的“自旋窗口”，但其合成可能较为困难，因为它需要精确的“棋盘式”原子排列，而这种排列在高温下往往会变得紊乱。
2.  **KV[Cr(CN)₆]：** 该材料于1999年首次合成，但此前未被识别为LC半导体。AI分析显示，它具有2.1 eV的带隙，并在高达376 K (103 °C) 的温度下保持磁有序。与第一种候选材料不同，其晶体结构能自然地将金属原子锁定在正确的位置，使其成为更具稳健性的实际应用候选材料。

研究得出结论，下一代非易失性存储器（特别是室温LC半导体）的关键可能已经存在于化学文献中，“就隐藏在显而易见之处”。研究人员已在GitHub上发布了数据和代码，邀请科学界重新合成KV[Cr(CN)₆]并直接测量其自旋排序性能。这一发现标志着向实用、高性能自旋技术迈出了重要一步。

---

## 5. 使用蓝光 M-Disk 作为终极备份

**原文标题**: Using Blu-ray M-Disk as Backup of Last Resort

**原文链接**: [https://smyck.net/2026/10/03/holocron-the-backup-of-last-resort/](https://smyck.net/2026/10/03/holocron-the-backup-of-last-resort/)

This article details a "last-resort" decentralized backup strategy using Blu-ray M-Discs for long-term data archival. Inspired by the practice of leaving spare house keys with trusted friends, the author proposes creating physical backup kits to survive catastrophic events, such as a fire, that might destroy both a primary computer and local backups.

**The Strategy**
The author stores "core essential data"—including digitized documents, music, photos, and "digital life" reboot files—on three M-Discs. Most critical data is password-protected. These discs are placed in a rugged B&W Outdoor Case (Type 500) and padded with non-degrading PE foam to prevent physical damage.

**Security and Maintenance**
To ensure the integrity of the backup while it is stored with a "custodian" (a trusted friend), the author employs several security measures:
*   **Tamper-Evident Seals:** Plastic seals with unique serial numbers and barcodes are used to lock the case. 
*   **Custom Labeling:** Personalized stickers help identify the unit.
*   **Handover Ceremony:** Every 1–3 years, the author replaces the case, inspecting the old seal for tampering before handing over a refreshed version.
*   **Environmental Protection:** Silica gel packs are included to monitor and prevent moisture buildup.

**The "Holocron"**
The author nicknames these units "Holocrons," referencing the information-storage devices from *Star Wars*. This method provides a secure, offline, and decentralized alternative to cloud storage, relying on durable physical media and a "web of trust" to ensure that essential data can be recovered even in a worst-case scenario.

---

## 6. Web Search API

**原文标题**: Web Search API

**原文链接**: [https://developers.cloudflare.com/changelog/post/2026-10-02-introducing-web-search-api/](https://developers.cloudflare.com/changelog/post/2026-10-02-introducing-web-search-api/)

生成摘要时出错

---

## 7. Worth Building

**原文标题**: Worth Building

**原文链接**: [https://armstr.ng/writing/worth-building](https://armstr.ng/writing/worth-building)

生成摘要时出错

---

## 8. Competitive Programmer's Handbook (2018) [pdf]

**原文标题**: Competitive Programmer's Handbook (2018) [pdf]

**原文链接**: [https://cses.fi/book/book.pdf](https://cses.fi/book/book.pdf)

生成摘要时出错

---

## 9. Example.com 刚刚推出了数十年来规模最大的改版

**原文标题**: Example.com Just Launched the Biggest Redesign in Decades

**原文链接**: [https://www.debugbear.com/blog/example-dot-com-redesign-history](https://www.debugbear.com/blog/example-dot-com-redesign-history)

生成摘要时出错

---

## 10. DEDA – Tracking Dots Extraction, Decoding and Anonymisation Toolkit

**原文标题**: DEDA – Tracking Dots Extraction, Decoding and Anonymisation Toolkit

**原文链接**: [https://github.com/dfd-tud/deda](https://github.com/dfd-tud/deda)

生成摘要时出错

---

## 11. A third way of using Linux

**原文标题**: A third way of using Linux

**原文链接**: [https://hisvirusness.com/third-is-the-way](https://hisvirusness.com/third-is-the-way)

生成摘要时出错

---

## 12. Making a GTK application in Haskell, part 1

**原文标题**: Making a GTK application in Haskell, part 1

**原文链接**: [https://floreal.tech/blog/2026/making-a-gtk-app-in-haskell-part-1/](https://floreal.tech/blog/2026/making-a-gtk-app-in-haskell-part-1/)

生成摘要时出错

---

## 13. Anthropic reported diary entry to police, woman faces felony charge

**原文标题**: Anthropic reported diary entry to police, woman faces felony charge

**原文链接**: [https://www.techspot.com/news/114091-florida-woman-used-claude-diary-anthropic-reported-shoot.html](https://www.techspot.com/news/114091-florida-woman-used-claude-diary-anthropic-reported-shoot.html)

生成摘要时出错

---

## 14. Linux containers in 500 lines of code (2016)

**原文标题**: Linux containers in 500 lines of code (2016)

**原文链接**: [https://blog.lizzie.io/linux-containers-in-500-loc.html](https://blog.lizzie.io/linux-containers-in-500-loc.html)

生成摘要时出错

---

## 15. Incident with Actions

**原文标题**: Incident with Actions

**原文链接**: [https://www.githubstatus.com/incidents/3q1yb5m7ltvb](https://www.githubstatus.com/incidents/3q1yb5m7ltvb)

生成摘要时出错

---

## 16. The Future of Mathematics

**原文标题**: The Future of Mathematics

**原文链接**: [https://terrytao.wordpress.com/2026/10/05/the-future-of-mathematics/](https://terrytao.wordpress.com/2026/10/05/the-future-of-mathematics/)

生成摘要时出错

---

## 17. Show HN: Nightwatch – a Mac menu-bar app that tells you when tonight is clear

**原文标题**: Show HN: Nightwatch – a Mac menu-bar app that tells you when tonight is clear

**原文链接**: [https://github.com/rsutcliffe/nightwatch](https://github.com/rsutcliffe/nightwatch)

生成摘要时出错

---

## 18. The lamps in my house

**原文标题**: The lamps in my house

**原文链接**: [https://arslan.io/2026/10/05/the-lamps-in-my-house/](https://arslan.io/2026/10/05/the-lamps-in-my-house/)

生成摘要时出错

---

## 19. Apple and a hacker's future

**原文标题**: Apple and a hacker's future

**原文链接**: [https://stratechery.com/2026/apple-and-a-hackers-future/](https://stratechery.com/2026/apple-and-a-hackers-future/)

生成摘要时出错

---

## 20. Qualcomm licenses patents on Huawei’s LogicFolding chip tech

**原文标题**: Qualcomm licenses patents on Huawei’s LogicFolding chip tech

**原文链接**: [https://www.bloomberg.com/news/articles/2026-10-05/qualcomm-licenses-patents-on-huawei-s-logicfolding-chip-tech](https://www.bloomberg.com/news/articles/2026-10-05/qualcomm-licenses-patents-on-huawei-s-logicfolding-chip-tech)

生成摘要时出错

---

## 21. The first fully implanted cochlear implant reaches patients

**原文标题**: The first fully implanted cochlear implant reaches patients

**原文链接**: [https://spectrum.ieee.org/fully-implantable-cochlear-implant](https://spectrum.ieee.org/fully-implantable-cochlear-implant)

生成摘要时出错

---

## 22. 2026 Nobel Prize in Physiology or Medicine: Deisseroth, Hegemann, Nagel

**原文标题**: 2026 Nobel Prize in Physiology or Medicine: Deisseroth, Hegemann, Nagel

**原文链接**: [https://www.nobelprize.org/prizes/medicine/2026/summary/](https://www.nobelprize.org/prizes/medicine/2026/summary/)

生成摘要时出错

---

## 23. Norway Eyes Partial Ban of Smart Glasses

**原文标题**: Norway Eyes Partial Ban of Smart Glasses

**原文链接**: [https://www.barrons.com/news/norway-eyes-partial-ban-of-smart-glasses-e65dc239](https://www.barrons.com/news/norway-eyes-partial-ban-of-smart-glasses-e65dc239)

生成摘要时出错

---

## 24. Type Safe Generic Data Structures in C (2025)

**原文标题**: Type Safe Generic Data Structures in C (2025)

**原文链接**: [https://danielchasehooper.com/posts/typechecked-generic-c-data-structures/](https://danielchasehooper.com/posts/typechecked-generic-c-data-structures/)

生成摘要时出错

---

## 25. Differences Between `Foldl` and `Foldr`

**原文标题**: Differences Between `Foldl` and `Foldr`

**原文链接**: [https://blog.haskell.org/foldl-and-foldr/](https://blog.haskell.org/foldl-and-foldr/)

生成摘要时出错

---

## 26. Texas city demands $2M for public records on Flock usage

**原文标题**: Texas city demands $2M for public records on Flock usage

**原文链接**: [https://arstechnica.com/tech-policy/2026/10/texas-city-demands-2m-for-public-records-on-flock-usage/](https://arstechnica.com/tech-policy/2026/10/texas-city-demands-2m-for-public-records-on-flock-usage/)

生成摘要时出错

---

## 27. The technology to eradicate mosquito-borne disease exists

**原文标题**: The technology to eradicate mosquito-borne disease exists

**原文链接**: [https://worksinprogress.co/issue/mosquitoes-are-a-choice/](https://worksinprogress.co/issue/mosquitoes-are-a-choice/)

生成摘要时出错

---

## 28. The era of software quality, or the era of ostriches?

**原文标题**: The era of software quality, or the era of ostriches?

**原文链接**: [https://blogs.gnome.org/mcatanzaro/2026/10/02/the-era-of-software-quality-or-the-era-of-ostriches/](https://blogs.gnome.org/mcatanzaro/2026/10/02/the-era-of-software-quality-or-the-era-of-ostriches/)

生成摘要时出错

---

## 29. Martian chaos terrain

**原文标题**: Martian chaos terrain

**原文链接**: [https://en.wikipedia.org/wiki/Martian_chaos_terrain](https://en.wikipedia.org/wiki/Martian_chaos_terrain)

生成摘要时出错

---

## 30. Greenvolt begins building 600 MW/2.4 GWh BESS in Poland

**原文标题**: Greenvolt begins building 600 MW/2.4 GWh BESS in Poland

**原文链接**: [https://www.ess-news.com/2026/09/25/greenvolt-begins-building-600-mw-2-4-gwh-bess-in-poland/](https://www.ess-news.com/2026/09/25/greenvolt-begins-building-600-mw-2-4-gwh-bess-in-poland/)

生成摘要时出错

---

## 31. Hot Flashing Guide Rev. 2.0 (2004)

**原文标题**: Hot Flashing Guide Rev. 2.0 (2004)

**原文链接**: [https://archive.techarp.com/showarticle504a.html?pgno=0](https://archive.techarp.com/showarticle504a.html?pgno=0)

生成摘要时出错

---

## 32. Pixel 11 doesn't yet meet the GrapheneOS security standards and may be skipped

**原文标题**: Pixel 11 doesn't yet meet the GrapheneOS security standards and may be skipped

**原文链接**: [https://discuss.grapheneos.org/d/41564-pixel-11-doesnt-yet-meet-the-grapheneos-security-standards-and-may-be-skipped](https://discuss.grapheneos.org/d/41564-pixel-11-doesnt-yet-meet-the-grapheneos-security-standards-and-may-be-skipped)

生成摘要时出错

---

## 33. Denmark data breach exposes 8.8M people's personal data

**原文标题**: Denmark data breach exposes 8.8M people's personal data

**原文链接**: [https://www.cpr.dk/cpr-nyt/nyhedsarkiv/2026/okt/omfattende-uautoriseret-adgang-til-borgeres-cpr-oplysninger](https://www.cpr.dk/cpr-nyt/nyhedsarkiv/2026/okt/omfattende-uautoriseret-adgang-til-borgeres-cpr-oplysninger)

生成摘要时出错

---

## 34. Mystery Function

**原文标题**: Mystery Function

**原文链接**: [https://codeset.ai/function](https://codeset.ai/function)

生成摘要时出错

---

## 35. Iroh Global Content Discovery

**原文标题**: Iroh Global Content Discovery

**原文链接**: [https://www.iroh.computer/blog/iroh-global-content-discovery](https://www.iroh.computer/blog/iroh-global-content-discovery)

生成摘要时出错

---

## 36. One person can now be a quorum at the SEC

**原文标题**: One person can now be a quorum at the SEC

**原文链接**: [https://www.ft.com/content/3120782c-1ea0-4fdc-9462-0a4b4658f70f](https://www.ft.com/content/3120782c-1ea0-4fdc-9462-0a4b4658f70f)

生成摘要时出错

---

## 37. We ported the original Doom to SQL

**原文标题**: We ported the original Doom to SQL

**原文链接**: [https://cedardb.com/blog/sqldoom/](https://cedardb.com/blog/sqldoom/)

生成摘要时出错

---

## 38. Mold Linker Version 3.0.0 Release – Rewritten in Rust

**原文标题**: Mold Linker Version 3.0.0 Release – Rewritten in Rust

**原文链接**: [https://github.com/rui314/mold/releases/tag/v3.0.0](https://github.com/rui314/mold/releases/tag/v3.0.0)

生成摘要时出错

---

## 39. Our approach to EU text provenance rules

**原文标题**: Our approach to EU text provenance rules

**原文链接**: [https://openai.com/index/eu-text-provenance/](https://openai.com/index/eu-text-provenance/)

生成摘要时出错

---

## 40. The Tao of Backup

**原文标题**: The Tao of Backup

**原文链接**: [http://www.taobackup.com/index.html](http://www.taobackup.com/index.html)

生成摘要时出错

---

## 41. OpenAI "rogue" agent activities found on Wikimedia projects

**原文标题**: OpenAI "rogue" agent activities found on Wikimedia projects

**原文链接**: [https://diff.wikimedia.org/2026/10/05/openai-rogue-agent-activities-found-on-wikimedia-projects/](https://diff.wikimedia.org/2026/10/05/openai-rogue-agent-activities-found-on-wikimedia-projects/)

生成摘要时出错

---

## 42. Engineer says Claude Code has made his job "soul-sucking"

**原文标题**: Engineer says Claude Code has made his job "soul-sucking"

**原文链接**: [https://www.techspot.com/news/113937-engineer-claude-code-has-made-job-soul-sucking.html](https://www.techspot.com/news/113937-engineer-claude-code-has-made-job-soul-sucking.html)

生成摘要时出错

---

## 43. Plain text is still one of the best technologies we have

**原文标题**: Plain text is still one of the best technologies we have

**原文链接**: [https://deadparrotbbs.com/why-plain-text-is-still-one-of-the-best-technologies-we-have/](https://deadparrotbbs.com/why-plain-text-is-still-one-of-the-best-technologies-we-have/)

生成摘要时出错

---

## 44. ExplainDB: A Database System Built for Understandability

**原文标题**: ExplainDB: A Database System Built for Understandability

**原文链接**: [https://github.com/explaindb/explaindb](https://github.com/explaindb/explaindb)

生成摘要时出错

---

## 45. How to save a life without knowing CPR

**原文标题**: How to save a life without knowing CPR

**原文链接**: [https://bookofjoe2.blogspot.com/2026/10/beyondthemedspeak-how-to-save-life.html](https://bookofjoe2.blogspot.com/2026/10/beyondthemedspeak-how-to-save-life.html)

生成摘要时出错

---

## 46. Mosquitoes Are a Choice

**原文标题**: Mosquitoes Are a Choice

**原文链接**: [https://www.worksinprogress.news/p/you-can-just-eradicate-things](https://www.worksinprogress.news/p/you-can-just-eradicate-things)

生成摘要时出错

---

## 47. Picard 3.0

**原文标题**: Picard 3.0

**原文链接**: [https://blog.metabrainz.org/2026/10/04/picard-3-0-released/](https://blog.metabrainz.org/2026/10/04/picard-3-0-released/)

生成摘要时出错

---

## 48. Show HN: Pumpkins.sh – claim, carve, and display a pumpkin to the world

**原文标题**: Show HN: Pumpkins.sh – claim, carve, and display a pumpkin to the world

**原文链接**: [https://pumpkins.sh/](https://pumpkins.sh/)

生成摘要时出错

---

## 49. A Series of Unfortunate Events for OpenAI Users

**原文标题**: A Series of Unfortunate Events for OpenAI Users

**原文链接**: [https://insufferable.dev/posts/a-series-of-unfortunate-events-for-openai-users/](https://insufferable.dev/posts/a-series-of-unfortunate-events-for-openai-users/)

生成摘要时出错

---

## 50. The Philadelphia Inquirer built Scrape, an AI tool to surface hyperlocal news

**原文标题**: The Philadelphia Inquirer built Scrape, an AI tool to surface hyperlocal news

**原文链接**: [https://www.lenfestinstitute.org/solutions-resources/philadelphia-inquirer-scrape-ai-hyperlocal-news/](https://www.lenfestinstitute.org/solutions-resources/philadelphia-inquirer-scrape-ai-hyperlocal-news/)

生成摘要时出错

---

## 51. Infidel goes wild

**原文标题**: Infidel goes wild

**原文链接**: [https://blog.zarfhome.com/2026/10/infidel-goes-wild](https://blog.zarfhome.com/2026/10/infidel-goes-wild)

生成摘要时出错

---

## 52. A 40ms Go garbage collector pause caused by swap

**原文标题**: A 40ms Go garbage collector pause caused by swap

**原文链接**: [https://frn.sh/go-gc/](https://frn.sh/go-gc/)

生成摘要时出错

---

## 53. Async Rust: Where does the scheduler live?

**原文标题**: Async Rust: Where does the scheduler live?

**原文链接**: [https://herecomesthemoon.net/2026/10/async-rust-where-does-the-scheduler-live/](https://herecomesthemoon.net/2026/10/async-rust-where-does-the-scheduler-live/)

生成摘要时出错

---

## 54. Germany’s RobCo hits $1B valuation

**原文标题**: Germany’s RobCo hits $1B valuation

**原文链接**: [https://techfundingnews.com/europes-new-robotics-unicorn-germanys-robco-hits-1b-valuation/](https://techfundingnews.com/europes-new-robotics-unicorn-germanys-robco-hits-1b-valuation/)

生成摘要时出错

---

## 55. After bankruptcy, he was banned from sports betting sites. Then he found Kalshi

**原文标题**: After bankruptcy, he was banned from sports betting sites. Then he found Kalshi

**原文链接**: [https://www.npr.org/2026/10/02/nx-s1-5981420/kalshi-betting-prediction-markets-gambling-addiction](https://www.npr.org/2026/10/02/nx-s1-5981420/kalshi-betting-prediction-markets-gambling-addiction)

生成摘要时出错

---

## 56. Turn off Apple Intelligence on macOS 27 and get its disk space back

**原文标题**: Turn off Apple Intelligence on macOS 27 and get its disk space back

**原文链接**: [https://github.com/omlahore/RemoveMacAI](https://github.com/omlahore/RemoveMacAI)

生成摘要时出错

---

## 57. WSL containers is now generally available

**原文标题**: WSL containers is now generally available

**原文链接**: [https://blogs.windows.com/windowsdeveloper/2026/09/29/wsl-containers-now-generally-available/](https://blogs.windows.com/windowsdeveloper/2026/09/29/wsl-containers-now-generally-available/)

生成摘要时出错

---

## 58. Show HN: Minigraf – An embedded, bi-temporal graph database in Rust

**原文标题**: Show HN: Minigraf – An embedded, bi-temporal graph database in Rust

**原文链接**: [https://github.com/project-minigraf/minigraf](https://github.com/project-minigraf/minigraf)

生成摘要时出错

---

## 59. Beating the compiler (2024)

**原文标题**: Beating the compiler (2024)

**原文链接**: [https://www.mattkeeter.com/blog/2024-07-12-interpreter/](https://www.mattkeeter.com/blog/2024-07-12-interpreter/)

生成摘要时出错

---

## 60. The future of independence is interdependence

**原文标题**: The future of independence is interdependence

**原文链接**: [https://onlys.ky/independence-is-interdependence/](https://onlys.ky/independence-is-interdependence/)

生成摘要时出错

---

## 61. DigitalOcean Ends Open Source Credits Program

**原文标题**: DigitalOcean Ends Open Source Credits Program

**原文链接**: [https://itsfoss.com/news/digitalocean-open-source-credits-end/](https://itsfoss.com/news/digitalocean-open-source-credits-end/)

生成摘要时出错

---

## 62. Improper redaction reveals Google Data Center water and electricity usage

**原文标题**: Improper redaction reveals Google Data Center water and electricity usage

**原文链接**: [https://www.1011now.com/2026/09/30/more-questions-than-answers-about-lincolns-google-data-center-water-electricity-usage/](https://www.1011now.com/2026/09/30/more-questions-than-answers-about-lincolns-google-data-center-water-electricity-usage/)

生成摘要时出错

---

## 63. US closely monitoring case of lab worker who possibly died of plague in Siberia

**原文标题**: US closely monitoring case of lab worker who possibly died of plague in Siberia

**原文链接**: [https://www.theguardian.com/world/2026/oct/05/russia-lab-worker-possibly-dies-of-plague-siberia-quarantine-measures-irkutsk](https://www.theguardian.com/world/2026/oct/05/russia-lab-worker-possibly-dies-of-plague-siberia-quarantine-measures-irkutsk)

生成摘要时出错

---

## 64. Show HN: Glashütte Trash Clock – A 30-minute pendulum clock made from trash

**原文标题**: Show HN: Glashütte Trash Clock – A 30-minute pendulum clock made from trash

**原文链接**: [https://niklasroy.com/gtc/](https://niklasroy.com/gtc/)

生成摘要时出错

---

## 65. In the wake of Tippett Studios’ closure, a digital archive appears online

**原文标题**: In the wake of Tippett Studios’ closure, a digital archive appears online

**原文链接**: [https://filmstories.co.uk/news/tippett-studios-in-the-wake-of-its-closure-a-digital-archive-of-animated-materials-appears-online/](https://filmstories.co.uk/news/tippett-studios-in-the-wake-of-its-closure-a-digital-archive-of-animated-materials-appears-online/)

生成摘要时出错

---

## 66. Bill Draper has died

**原文标题**: Bill Draper has died

**原文链接**: [https://www.nytimes.com/2026/09/30/technology/william-draper-dead.html](https://www.nytimes.com/2026/09/30/technology/william-draper-dead.html)

生成摘要时出错

---

## 67. An open-source tool lets you delete 12GB of Apple Intelligence data on macOS

**原文标题**: An open-source tool lets you delete 12GB of Apple Intelligence data on macOS

**原文链接**: [https://www.theverge.com/ai-artificial-intelligence/1004672/mac-delete-apple-intelligence-ai-tool](https://www.theverge.com/ai-artificial-intelligence/1004672/mac-delete-apple-intelligence-ai-tool)

生成摘要时出错

---

## 68. Blindsight (Watts Novel)

**原文标题**: Blindsight (Watts Novel)

**原文链接**: [https://en.wikipedia.org/wiki/Blindsight_(Watts_novel)](https://en.wikipedia.org/wiki/Blindsight_(Watts_novel))

生成摘要时出错

---

## 69. Turkey's 20B ponzi scheme collapsed

**原文标题**: Turkey's 20B ponzi scheme collapsed

**原文链接**: [https://www.reuters.com/world/middle-east/how-turkeys-investment-fund-bubble-burst-2026-10-02/](https://www.reuters.com/world/middle-east/how-turkeys-investment-fund-bubble-burst-2026-10-02/)

生成摘要时出错

---

## 70. Lace and Labor: Lessons from the actual Luddites

**原文标题**: Lace and Labor: Lessons from the actual Luddites

**原文链接**: [https://articlesofinterest.substack.com/p/lace-and-labor](https://articlesofinterest.substack.com/p/lace-and-labor)

生成摘要时出错

---

## 71. Decision models like Jev don't beat LLM-as-a-judge or traditional classifiers

**原文标题**: Decision models like Jev don't beat LLM-as-a-judge or traditional classifiers

**原文链接**: [https://developers.redhat.com/articles/2026/10/02/benchmarking-ai-decision-models-against-traditional-guardrails](https://developers.redhat.com/articles/2026/10/02/benchmarking-ai-decision-models-against-traditional-guardrails)

生成摘要时出错

---

## 72. Demystifying Tufte's data-ink ratio

**原文标题**: Demystifying Tufte's data-ink ratio

**原文链接**: [https://tuftesrazor.scienceux.org/](https://tuftesrazor.scienceux.org/)

生成摘要时出错

---

## 73. uBlock Origin Lite is back on Firefox add-ons

**原文标题**: uBlock Origin Lite is back on Firefox add-ons

**原文链接**: [https://addons.mozilla.org/en-US/firefox/addon/ublock-origin-lite/](https://addons.mozilla.org/en-US/firefox/addon/ublock-origin-lite/)

生成摘要时出错

---

## 74. A browser-native classic Visual Basic VB6 IDE

**原文标题**: A browser-native classic Visual Basic VB6 IDE

**原文链接**: [https://wieslawsoltes.github.io/VB6/](https://wieslawsoltes.github.io/VB6/)

生成摘要时出错

---

## 75. cp: -r or -R?

**原文标题**: cp: -r or -R?

**原文链接**: [https://movq.de/blog/postings/2026-09-30/0/POSTING-en.html](https://movq.de/blog/postings/2026-09-30/0/POSTING-en.html)

生成摘要时出错

---

## 76. Show HN: AI search for every photo and every frame of video on macOS

**原文标题**: Show HN: AI search for every photo and every frame of video on macOS

**原文链接**: [https://github.com/allenv0/SCM](https://github.com/allenv0/SCM)

生成摘要时出错

---

## 77. How to scale intent, quality, and artistry with AI [video]

**原文标题**: How to scale intent, quality, and artistry with AI [video]

**原文链接**: [https://www.youtube.com/watch?v=GLvFTMtw4Jk](https://www.youtube.com/watch?v=GLvFTMtw4Jk)

生成摘要时出错

---

## 78. Borland Turbo Basic

**原文标题**: Borland Turbo Basic

**原文链接**: [https://dosdays.co.uk/topics/Software/borland_turbo_basic.php](https://dosdays.co.uk/topics/Software/borland_turbo_basic.php)

生成摘要时出错

---

## 79. Powerless F1 drivers frustrated by Bahrain F1 software glitch

**原文标题**: Powerless F1 drivers frustrated by Bahrain F1 software glitch

**原文链接**: [https://www.motorsport.com/f1/news/horrible-totally-unacceptable-powerless-f1-drivers-frustrated-by-bahrain-f1-software-glitch/10861968/](https://www.motorsport.com/f1/news/horrible-totally-unacceptable-powerless-f1-drivers-frustrated-by-bahrain-f1-software-glitch/10861968/)

生成摘要时出错

---

## 80. Another step towards Elm 1.0

**原文标题**: Another step towards Elm 1.0

**原文链接**: [https://elm-lang.org/news/another-step-towards-elm-v1](https://elm-lang.org/news/another-step-towards-elm-v1)

生成摘要时出错

---

## 81. Emitting metadata early makes building/checking Rust up to twice as fast

**原文标题**: Emitting metadata early makes building/checking Rust up to twice as fast

**原文链接**: [https://github.com/PowderworksCode/headstart](https://github.com/PowderworksCode/headstart)

生成摘要时出错

---

## 82. Self-hosted HTTP tunnels with SSH and Nginx

**原文标题**: Self-hosted HTTP tunnels with SSH and Nginx

**原文链接**: [https://vincent.bernat.ch/en/blog/2026-http-over-ssh](https://vincent.bernat.ch/en/blog/2026-http-over-ssh)

生成摘要时出错

---

## 83. RetailReady (YC W24) Is Hiring

**原文标题**: RetailReady (YC W24) Is Hiring

**原文链接**: [https://www.ycombinator.com/companies/retailready/jobs/bFcgIe4-implementations](https://www.ycombinator.com/companies/retailready/jobs/bFcgIe4-implementations)

生成摘要时出错

---

## 84. Watson Jr. memo about CDC 6600 (1963)

**原文标题**: Watson Jr. memo about CDC 6600 (1963)

**原文链接**: [https://www.computerhistory.org/revolution/supercomputers/10/33/62](https://www.computerhistory.org/revolution/supercomputers/10/33/62)

生成摘要时出错

---

## 85. Gods in the Classroom: Religion and Education in First Millennium BCE Babylonia

**原文标题**: Gods in the Classroom: Religion and Education in First Millennium BCE Babylonia

**原文链接**: [https://www.cambridge.org/core/journals/iraq/article/gods-in-the-classroom-religion-and-education-in-1st-millennium-bce-babylonia/EB059EE81804DCBC1848CACBD6298E0B](https://www.cambridge.org/core/journals/iraq/article/gods-in-the-classroom-religion-and-education-in-1st-millennium-bce-babylonia/EB059EE81804DCBC1848CACBD6298E0B)

生成摘要时出错

---

## 86. Interview with Chicken Scheme Maintainer Sjamaan/Peter Bex

**原文标题**: Interview with Chicken Scheme Maintainer Sjamaan/Peter Bex

**原文链接**: [https://alexalejandre.com/interviews/peter-bex/](https://alexalejandre.com/interviews/peter-bex/)

生成摘要时出错

---

## 87. Former SR-71 engineer talks NASA's Blackbird revival program

**原文标题**: Former SR-71 engineer talks NASA's Blackbird revival program

**原文链接**: [https://www.twz.com/air/former-sr-71-engineer-talks-nasas-blackbird-revival-program](https://www.twz.com/air/former-sr-71-engineer-talks-nasas-blackbird-revival-program)

生成摘要时出错

---

## 88. Xray-core concealed a certificate verification bypass vulnerability

**原文标题**: Xray-core concealed a certificate verification bypass vulnerability

**原文链接**: [https://github.com/net4people/bbs/issues/672](https://github.com/net4people/bbs/issues/672)

生成摘要时出错

---

## 89. 'Neanderthals Among Us' review

**原文标题**: 'Neanderthals Among Us' review

**原文链接**: [https://www.historytoday.com/archive/review/neanderthals-among-us-peter-sahlins-review](https://www.historytoday.com/archive/review/neanderthals-among-us-peter-sahlins-review)

生成摘要时出错

---

## 90. All I wanted was a custom domain email

**原文标题**: All I wanted was a custom domain email

**原文链接**: [https://jacobg.co/emails-at-jacobg-co/](https://jacobg.co/emails-at-jacobg-co/)

生成摘要时出错

---

## 91. Safe Optimistic Lock Coupling

**原文标题**: Safe Optimistic Lock Coupling

**原文链接**: [http://databasearchitects.blogspot.com/2026/04/safe-optimistic-lock-coupling.html](http://databasearchitects.blogspot.com/2026/04/safe-optimistic-lock-coupling.html)

生成摘要时出错

---

## 92. Incentives in Academic Research

**原文标题**: Incentives in Academic Research

**原文链接**: [https://www.msoos.org/2026/10/incentives-in-academic-research/](https://www.msoos.org/2026/10/incentives-in-academic-research/)

生成摘要时出错

---

## 93. Page Table Memory Consumption

**原文标题**: Page Table Memory Consumption

**原文链接**: [https://frn.sh/pagetables/](https://frn.sh/pagetables/)

生成摘要时出错

---

## 94. Reasons I didn't become an EMT, ranked

**原文标题**: Reasons I didn't become an EMT, ranked

**原文链接**: [https://ben.stolovitz.com/posts/reasons-not-emt-ranked/](https://ben.stolovitz.com/posts/reasons-not-emt-ranked/)

生成摘要时出错

---

## 95. Replacement of petroleum based products with plant-based materials (2025)

**原文标题**: Replacement of petroleum based products with plant-based materials (2025)

**原文链接**: [https://onlinelibrary.wiley.com/doi/10.1002/eng2.70108](https://onlinelibrary.wiley.com/doi/10.1002/eng2.70108)

生成摘要时出错

---

## 96. A map of every lighthouse

**原文标题**: A map of every lighthouse

**原文链接**: [https://mapped.earth/lighthouses/world](https://mapped.earth/lighthouses/world)

生成摘要时出错

---

## 97. CIA Report Warns Israel Could Head Toward Civil War, Total Collapse

**原文标题**: CIA Report Warns Israel Could Head Toward Civil War, Total Collapse

**原文链接**: [https://www.dropsitenews.com/p/cia-report-israel-civil-war-collapse](https://www.dropsitenews.com/p/cia-report-israel-civil-war-collapse)

生成摘要时出错

---

## 98. Pentagon stops using Anthropic AI tools after blacklisting company, BBC told

**原文标题**: Pentagon stops using Anthropic AI tools after blacklisting company, BBC told

**原文链接**: [https://www.bbc.co.uk/news/articles/c5j9x9pr0240o](https://www.bbc.co.uk/news/articles/c5j9x9pr0240o)

生成摘要时出错

---

## 99. We want you to build the next Git platform on Cloudflare

**原文标题**: We want you to build the next Git platform on Cloudflare

**原文链接**: [https://blog.cloudflare.com/next-git-platform-on-cloudflare/](https://blog.cloudflare.com/next-git-platform-on-cloudflare/)

生成摘要时出错

---

## 100. Results from the ASIC puzzle

**原文标题**: Results from the ASIC puzzle

**原文链接**: [https://blog.janestreet.com/asic-puzzle-results/](https://blog.janestreet.com/asic-puzzle-results/)

生成摘要时出错

---

