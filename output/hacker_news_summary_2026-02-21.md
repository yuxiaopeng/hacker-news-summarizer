# Hacker News 热门文章摘要 (2026-02-21)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 填写安全审查表时不该写的内容

**原文标题**: What Not to Write on Your Security Clearance Form

**原文链接**: [https://milk.com/wall-o-shame/security_clearance.html](https://milk.com/wall-o-shame/security_clearance.html)

在这篇1988年的文章中，莱斯·厄尼斯特（Les Earnest）讲述了1943年的一件童年往事，以此揭示政府官僚机构和安全审查的复杂性。

十二岁那年，厄尼斯特和朋友在读了一本关于代码与密码的书后，对密码学产生了浓厚兴趣。他们自创了一种秘密的“行话代码”，厄尼斯特将密钥副本藏在了他的眼镜盒里。在圣地亚哥旅行时，他不慎在电车上丢了眼镜盒。由于当时正值二战，民众对日本间谍活动深感恐慌，一位市民捡到盒子后将其中的代码上交给了联邦调查局（FBI）。

FBI随即展开了一项高规格调查，耗费数千美元并历时数周，最终通过眼镜处方追踪到了厄尼斯特。在发现所谓的“间谍”只是个孩子后，一名探员归还了眼镜，但保留了代码记录。从此，厄尼斯特在FBI留下了正式的档案。

多年后，厄尼斯特在大学期间申请海军电子实验室的暑期工作，需要填写安全审查表。当被问及是否曾受过FBI调查时，他如实回答“是”，并注明自己曾“被怀疑是日本间谍”。

安全官员意识到，这样一个敏感（尽管无辜）的条目会引发官僚主义的噩梦，甚至导致申请直接被拒，于是撕毁了申请表。他命令厄尼斯特重新填写一份完全隐瞒此事的表格，并警告说如果如实记录，他将永远无法通过审查。厄尼斯特听从了建议，最终顺利通过审查。他由此总结道：在面对安全审查表时，为了避免不必要的麻烦，某些真相最好还是保持沉默。

---

## 2. 我验证了我的领英身份，以下是我提交的信息。

**原文标题**: I Verified My LinkedIn Identity. Here's What I Handed Over

**原文链接**: [https://thelocalstack.eu/posts/linkedin-identity-verification-privacy/](https://thelocalstack.eu/posts/linkedin-identity-verification-privacy/)

本文深入探讨了 LinkedIn（领英）身份验证过程所带来的广泛隐私影响。虽然用户是为了获得象征真实性的“蓝勾”标记，但实际上他们并非向 LinkedIn 提供信息，而是向一家名为 **Persona Identities, Inc.** 的美国第三方公司提供敏感数据。

作者揭示，仅需三分钟的验证过程所收集的信息远超护照扫描件。Persona 会采集**生物识别面部几何结构**、NFC 芯片数据以及包括“犹豫检测”在内的“行为生物特征”。这些数据会与全球政府数据库和征信机构进行交叉比对。此外，Persona 以“正当利益”而非“明确同意”作为法律依据，将这些身份证明文件用作 **AI 训练数据**。

关键调查结果包括：
*   **数据散布：** 包括 **OpenAI、Anthropic 和 Amazon** 在内的 17 家次级处理商参与处理数据。其中 16 家位于美国，处理链条中完全没有欧盟实体。
*   **法律弱点：** 由于 Persona 是一家美国公司，其受**美国《云法案》（CLOUD Act）**管辖。这使得美国执法部门可以要求获取存储在 Persona 任何服务器（包括位于欧盟的服务器）上的数据，且这类要求通常通过包含禁言令的“国家安全”请求发出。
*   **追责受限：** Persona 的服务条款将其在数据泄露中的赔偿责任限制在仅 **50 美元**，并要求强制性仲裁，这限制了用户寻求法律公正的能力。

作者总结道，将不可更改的生物识别数据和政府身份证件交给复杂的美国科技公司网络所带来的永久性风险，远超社交媒体勋章带来的表面好处。作者建议已验证用户行使其 GDPR（通用数据保护条例）权利，要求删除数据，并联系 Persona 的数据保护官以反对将其数据用于 AI 训练。

---

## 3. 保持安卓开放

**原文标题**: Keep Android Open

**原文链接**: [https://f-droid.org/2026/02/20/twif.html](https://f-droid.org/2026/02/20/twif.html)

2026年2月20日出版的“F-Droid本周动态”发出了关于Android开放性未来的严正警告。F-Droid澄清道，尽管公众存在误解，但谷歌仍在北京推进其“封锁”平台的计划。作为回应，F-Droid、IzzyOnDroid和Obtainium正在上线警告横幅，以提醒用户并鼓励他们抗议谷歌向集权式“守门人”的转型。

**开发动态**
F-Droid Basic已更新至2.0-alpha3版本。主要更新包括：
*   支持将已安装应用列表导出为CSV格式。
*   新增安装历史记录功能和镜像选择器。
*   优化界面以符合Material Design 3设计规范。
*   **注意：** 使用1.23.x版本的用户必须手动开启“测试版更新”才能接收此版本。

**应用更新与新闻**
生态系统内有多项重大更新值得关注：
*   **Conversations/Quicksy：** 正在通过进程间通信（IPC）直接与Google Play服务对接，而非使用专有库，从而向完全的开源（FLOSS）版本迈进。
*   **ProtonVPN：** 移除了对OpenVPN的支持，转而采用WireGuard和Stealth协议，使应用体积缩小了40%。
*   **Nextcloud：** 进行了大规模发布，包括Nextcloud Hub 26 “Winter”以及各项客户端应用（Talk、Notes、Cookbook）的更新。
*   **Dolphin Emulator（海豚模拟器）：** 重大更新至2512版本，包含大量变更日志和性能改进。
*   **技术说明：** 随着近期Debian系统的升级，F-Droid正鼓励开发者迁移至Java 21，以简化构建流程。

**软件仓库变更**
本周新增了 **NeoDB You**，并移除了包括 **Tomdroid** 和 **OpenAthena** 在内的五款应用。此外，另有287款应用获得更新，其中包括NewPipe、Aurora Store和Element X等热门应用。

---

## 4. 你能理解多久以前的英语？

**原文标题**: How far back in time can you understand English?

**原文链接**: [https://www.deadlanguagesociety.com/p/how-far-back-in-time-understand-english](https://www.deadlanguagesociety.com/p/how-far-back-in-time-understand-english)

在《你能理解多久以前的英语？》中，语言学博士科林·戈里（Colin Gorrie）通过一项富有创意的语言学实验，展示了英语在1000年间的演变过程。文章围绕一个虚构的故事展开，讲述了一名旅行者访问神秘小镇伍尔弗利特（Wulfleet）的经历；每隔几个段落，故事就会向回跨越一个世纪，并采用那个时代真实的拼写、语法和“语调”。

该实验突出了几个关键的语言学里程碑：

*   **1700–2000年：** 英语保持得非常稳定。虽然“语调”从现代博客风格转变为乔治亚时代的日记风格，但得益于18世纪中叶的语言标准化，现代读者仍能轻松理解其拼写和语法。
*   **1500–1600年（早期现代英语）：** 语言开始发生显著变化，出现了如“thou”之类的古语代词、不同的动词词尾以及“长s”（ʃ）。
*   **1200–1400年（中古英语）：** 阅读变得十分吃力，文中引入了陌生的字母如 thorn (**þ**) 和 yogh (**ȝ**)，并伴有浓厚的日耳曼语影响和非标准化的拼写。
*   **1000–1100年（古英语）：** 对于未经训练的现代读者来说，这时的语言几乎无法辨认，呈现为一种使用了 wynn (**ƿ**) 和 ash (**æ**) 等字母的“外语”（盎格鲁-撒克逊语）。

虚构的情节映衬了这种对过去的追溯：叙述者最终被一个狼一般的“主人”囚禁，随后被一位名叫埃尔夫吉夫（Ælfgifu）的女子营救。故事在公元1000年结束，两人被古老的魔法困在了伍尔弗利特。最终，戈里证明了虽然我们可以轻松欣赏过去300年间的文学作品，但英语的深厚历史揭示了它从日耳曼语根源到如今全球通用语言的剧烈变革。

---

## 5. The Nekonomicon – Nekochan.net 存档，已更新

**原文标题**: The Nekonomicon – Nekochan.net Archive, Updated

**原文链接**: [http://nekonomicon.irixnet.org/](http://nekonomicon.irixnet.org/)

**The Nekonomicon** 是一个更新后的数字档案馆，致力于保存 **Nekochan.net** 社区（历史上是 Silicon Graphics 及复古计算爱好者的聚集地）的历史与内容。该档案库分为三个卷册：

*   **第1卷（终结之书）：** 作为导言和参考指南，阐述了 Nekonomicon 的性质与宗旨。
*   **第2卷（笔记之书）：** 作为社区集体知识的仓库，收录了来自 Nekochan 论坛的存档讨论及文字作品。
*   **第3卷（图集之书）：** 侧重于影像保存，收录了原网站的照片馆。

总而言之，该合集是 Nekochan 网站的一份全面历史记录，为其文字讨论和视觉媒介资料提供了持久的保存，以供未来参考。

---

## 6. macOS 鲜为人知的命令行沙盒工具 (2025)

**原文标题**: macOS's Little-Known Command-Line Sandboxing Tool (2025)

**原文链接**: [https://igorstechnoclub.com/sandbox-exec/](https://igorstechnoclub.com/sandbox-exec/)

This article explores **`sandbox-exec`**, a native macOS command-line utility used to execute applications within a secure, isolated environment. By restricting access to system resources, the tool minimizes potential damage from malicious code and protects user privacy.

**Key Components and Usage:**
The tool operates using **sandbox profiles** (`.sb` files) written in a Scheme-like (Lisp) syntax. These profiles define what an application can or cannot access based on two primary philosophies:
*   **Deny by Default (Whitelisting):** The most secure approach, where all actions are blocked unless explicitly permitted.
*   **Allow by Default (Blacklisting):** A more permissive approach that allows all actions except those specifically restricted.

Rules within these profiles can target resources using literal paths, regular expressions, or glob patterns. Users can also leverage pre-built system profiles found in `/System/Library/Sandbox/Profiles/`.

**Practical Applications and Debugging:**
Power users can use `sandbox-exec` to create network-isolated terminal sessions or restricted testing environments for scripts. If a sandboxed application fails to run correctly, users can debug the issue by monitoring system logs via the **Console app** or using the `log stream` command to identify "deny" violations in real-time.

**Limitations:**
Despite its power, the tool has notable drawbacks:
*   **Deprecation:** Apple encourages developers to use "App Sandbox" instead.
*   **Complexity:** Modern GUI applications often have complex dependencies that are difficult to sandbox manually without trial and error.
*   **No GUI:** Configuration is strictly text-based, requiring a learning curve.

**Conclusion:**
`sandbox-exec` remains a potent, flexible tool for developers and security-conscious power users. It offers a level of granular control over application permissions that standard macOS security settings cannot match, making it ideal for testing untrusted code or hardening specific workflows.

---

## 7. AI uBlock Blacklist

**原文标题**: AI uBlock Blacklist

**原文链接**: [https://github.com/alvi-se/ai-ublock-blacklist](https://github.com/alvi-se/ai-ublock-blacklist)

生成摘要时出错

---

## 8. I found a Vulnerability. They found a Lawyer

**原文标题**: I found a Vulnerability. They found a Lawyer

**原文链接**: [https://dixken.de/blog/i-found-a-vulnerability-they-found-a-lawyer](https://dixken.de/blog/i-found-a-vulnerability-they-found-a-lawyer)

生成摘要时出错

---

## 9. Turn Dependabot off

**原文标题**: Turn Dependabot off

**原文链接**: [https://words.filippo.io/dependabot/](https://words.filippo.io/dependabot/)

生成摘要时出错

---

## 10. Show HN: Iron-Wolf – Wolfenstein 3D source port in Rust

**原文标题**: Show HN: Iron-Wolf – Wolfenstein 3D source port in Rust

**原文链接**: [https://github.com/Ragnaroek/iron-wolf](https://github.com/Ragnaroek/iron-wolf)

生成摘要时出错

---

## 11. Facebook is cooked

**原文标题**: Facebook is cooked

**原文链接**: [https://pilk.website/3/facebook-is-absolutely-cooked](https://pilk.website/3/facebook-is-absolutely-cooked)

生成摘要时出错

---

## 12. Andrej Karpathy talks about "Claws"

**原文标题**: Andrej Karpathy talks about "Claws"

**原文链接**: [https://simonwillison.net/2026/Feb/21/claws/](https://simonwillison.net/2026/Feb/21/claws/)

生成摘要时出错

---

## 13. Ggml.ai joins Hugging Face to ensure the long-term progress of Local AI

**原文标题**: Ggml.ai joins Hugging Face to ensure the long-term progress of Local AI

**原文链接**: [https://github.com/ggml-org/llama.cpp/discussions/19759](https://github.com/ggml-org/llama.cpp/discussions/19759)

生成摘要时出错

---

## 14. Wikipedia deprecates Archive.today, starts removing archive links

**原文标题**: Wikipedia deprecates Archive.today, starts removing archive links

**原文链接**: [https://arstechnica.com/tech-policy/2026/02/wikipedia-bans-archive-today-after-site-executed-ddos-and-altered-web-captures/](https://arstechnica.com/tech-policy/2026/02/wikipedia-bans-archive-today-after-site-executed-ddos-and-altered-web-captures/)

生成摘要时出错

---

## 15. Padlet (YC W13) Is Hiring in San Francisco and Singapore

**原文标题**: Padlet (YC W13) Is Hiring in San Francisco and Singapore

**原文链接**: [https://padlet.jobs](https://padlet.jobs)

生成摘要时出错

---

## 16. Lean 4: How the theorem prover works and why it's the new competitive edge in AI

**原文标题**: Lean 4: How the theorem prover works and why it's the new competitive edge in AI

**原文链接**: [https://venturebeat.com/ai/lean4-how-the-theorem-prover-works-and-why-its-the-new-competitive-edge-in](https://venturebeat.com/ai/lean4-how-the-theorem-prover-works-and-why-its-the-new-competitive-edge-in)

生成摘要时出错

---

## 17. CXMT has been offering DDR4 chips at about half the prevailing market rate

**原文标题**: CXMT has been offering DDR4 chips at about half the prevailing market rate

**原文链接**: [https://www.koreaherald.com/article/10679206](https://www.koreaherald.com/article/10679206)

生成摘要时出错

---

## 18. CERN rebuilt the original browser from 1989 (2019)

**原文标题**: CERN rebuilt the original browser from 1989 (2019)

**原文链接**: [https://worldwideweb.cern.ch](https://worldwideweb.cern.ch)

生成摘要时出错

---

## 19. Coccinelle: The Linux kernel's source-to-source transformation tool

**原文标题**: Coccinelle: The Linux kernel's source-to-source transformation tool

**原文链接**: [https://github.com/coccinelle/coccinelle](https://github.com/coccinelle/coccinelle)

生成摘要时出错

---

## 20. The bare minimum for syncing Git repos

**原文标题**: The bare minimum for syncing Git repos

**原文链接**: [https://alexwlchan.net/2026/bare-git/](https://alexwlchan.net/2026/bare-git/)

生成摘要时出错

---

## 21. Every company building your AI assistant is now an ad company

**原文标题**: Every company building your AI assistant is now an ad company

**原文链接**: [https://juno-labs.com/blogs/every-company-building-your-ai-assistant-is-an-ad-company](https://juno-labs.com/blogs/every-company-building-your-ai-assistant-is-an-ad-company)

生成摘要时出错

---

## 22. What Is OAuth?

**原文标题**: What Is OAuth?

**原文链接**: [https://leaflet.pub/p/did:plc:3vdrgzr2zybocs45yfhcr6ur/3mfd2oxx5v22b](https://leaflet.pub/p/did:plc:3vdrgzr2zybocs45yfhcr6ur/3mfd2oxx5v22b)

生成摘要时出错

---

## 23. Approaches to writing two-sentence journal entries

**原文标题**: Approaches to writing two-sentence journal entries

**原文链接**: [https://alexanderbjoy.com/two-sentence-journal-approaches/](https://alexanderbjoy.com/two-sentence-journal-approaches/)

生成摘要时出错

---

## 24. Understanding Std:Shared_mutex from C++17

**原文标题**: Understanding Std:Shared_mutex from C++17

**原文链接**: [https://www.cppstories.com/2026/shared_mutex/](https://www.cppstories.com/2026/shared_mutex/)

生成摘要时出错

---

## 25. JWasm: Masm Compatible Assembler

**原文标题**: JWasm: Masm Compatible Assembler

**原文链接**: [https://github.com/Baron-von-Riedesel/JWasm](https://github.com/Baron-von-Riedesel/JWasm)

生成摘要时出错

---

## 26. Gitas – A tool for Git account switching

**原文标题**: Gitas – A tool for Git account switching

**原文链接**: [https://github.com/letmutex/gitas](https://github.com/letmutex/gitas)

生成摘要时出错

---

## 27. Index, Count, Offset, Size

**原文标题**: Index, Count, Offset, Size

**原文链接**: [https://tigerbeetle.com/blog/2026-02-16-index-count-offset-size/](https://tigerbeetle.com/blog/2026-02-16-index-count-offset-size/)

生成摘要时出错

---

## 28. Blue light filters don't work – controlling total luminance is a better bet

**原文标题**: Blue light filters don't work – controlling total luminance is a better bet

**原文链接**: [https://www.neuroai.science/p/blue-light-filters-dont-work](https://www.neuroai.science/p/blue-light-filters-dont-work)

生成摘要时出错

---

## 29. The path to ubiquitous AI (17k tokens/sec)

**原文标题**: The path to ubiquitous AI (17k tokens/sec)

**原文链接**: [https://taalas.com/the-path-to-ubiquitous-ai/](https://taalas.com/the-path-to-ubiquitous-ai/)

生成摘要时出错

---

## 30. OpenScan

**原文标题**: OpenScan

**原文链接**: [https://openscan.eu/pages/scan-gallery](https://openscan.eu/pages/scan-gallery)

生成摘要时出错

---

## 31. Show HN: Mines.fyi – all the mines in the US in a leaflet visualization

**原文标题**: Show HN: Mines.fyi – all the mines in the US in a leaflet visualization

**原文链接**: [https://mines.fyi/](https://mines.fyi/)

生成摘要时出错

---

## 32. Cord: Coordinating Trees of AI Agents

**原文标题**: Cord: Coordinating Trees of AI Agents

**原文链接**: [https://www.june.kim/cord](https://www.june.kim/cord)

生成摘要时出错

---

## 33. Trump's global tariffs struck down by US Supreme Court

**原文标题**: Trump's global tariffs struck down by US Supreme Court

**原文链接**: [https://www.bbc.com/news/live/c0l9r67drg7t](https://www.bbc.com/news/live/c0l9r67drg7t)

生成摘要时出错

---

## 34. When etcd crashes, check your disks first

**原文标题**: When etcd crashes, check your disks first

**原文链接**: [https://nubificus.co.uk/blog/etcd/](https://nubificus.co.uk/blog/etcd/)

生成摘要时出错

---

## 35. Gabriel Knight 3: Blood of the Sacred, Blood of the Damned

**原文标题**: Gabriel Knight 3: Blood of the Sacred, Blood of the Damned

**原文链接**: [https://www.filfre.net/2026/02/gabriel-knight-3-blood-of-the-sacred-blood-of-the-damned/](https://www.filfre.net/2026/02/gabriel-knight-3-blood-of-the-sacred-blood-of-the-damned/)

生成摘要时出错

---

## 36. Across the US, people are dismantling and destroying Flock surveillance cameras

**原文标题**: Across the US, people are dismantling and destroying Flock surveillance cameras

**原文链接**: [https://www.bloodinthemachine.com/p/across-the-us-people-are-dismantling](https://www.bloodinthemachine.com/p/across-the-us-people-are-dismantling)

生成摘要时出错

---

## 37. Show HN: A native macOS client for Hacker News, built with SwiftUI

**原文标题**: Show HN: A native macOS client for Hacker News, built with SwiftUI

**原文链接**: [https://github.com/IronsideXXVI/Hacker-News](https://github.com/IronsideXXVI/Hacker-News)

生成摘要时出错

---

## 38. Untapped Way to Learn a Codebase: Build a Visualizer

**原文标题**: Untapped Way to Learn a Codebase: Build a Visualizer

**原文链接**: [https://jimmyhmiller.com/learn-codebase-visualizer](https://jimmyhmiller.com/learn-codebase-visualizer)

生成摘要时出错

---

## 39. Lil' Fun Langs

**原文标题**: Lil' Fun Langs

**原文链接**: [https://taylor.town/scrapscript-000](https://taylor.town/scrapscript-000)

生成摘要时出错

---

## 40. Chris Lattner: Claude C Compiler

**原文标题**: Chris Lattner: Claude C Compiler

**原文链接**: [https://www.modular.com/blog/the-claude-c-compiler-what-it-reveals-about-the-future-of-software](https://www.modular.com/blog/the-claude-c-compiler-what-it-reveals-about-the-future-of-software)

生成摘要时出错

---

## 41. Making frontier cybersecurity capabilities available to defenders

**原文标题**: Making frontier cybersecurity capabilities available to defenders

**原文链接**: [https://www.anthropic.com/news/claude-code-security](https://www.anthropic.com/news/claude-code-security)

生成摘要时出错

---

## 42. Choose Your Fictions Well (2010)

**原文标题**: Choose Your Fictions Well (2010)

**原文链接**: [http://henryjenkins.org/blog/2010/04/choose_your_ficitons_well.html](http://henryjenkins.org/blog/2010/04/choose_your_ficitons_well.html)

生成摘要时出错

---

## 43. SwiftForth IDE for Windows, Linux, macOS

**原文标题**: SwiftForth IDE for Windows, Linux, macOS

**原文链接**: [https://www.forth.com/swiftforth/](https://www.forth.com/swiftforth/)

生成摘要时出错

---

## 44. 24 Hour Fitness won't let you unsubscribe from marketing spam, so I fixed it

**原文标题**: 24 Hour Fitness won't let you unsubscribe from marketing spam, so I fixed it

**原文链接**: [https://ahmedkaddoura.com/projects/24hf-unsubscribe](https://ahmedkaddoura.com/projects/24hf-unsubscribe)

生成摘要时出错

---

## 45. The true story behind the Toronto mystery tunnel (2015)

**原文标题**: The true story behind the Toronto mystery tunnel (2015)

**原文链接**: [https://macleans.ca/society/elton-mcdonald-and-the-incredible-true-story-behind-the-toronto-mystery-tunnel/](https://macleans.ca/society/elton-mcdonald-and-the-incredible-true-story-behind-the-toronto-mystery-tunnel/)

生成摘要时出错

---

## 46. Palantir Captured the UK Ministry of Defence

**原文标题**: Palantir Captured the UK Ministry of Defence

**原文链接**: [https://www.ft.com/content/5207928a-13e8-4832-8c6f-2e78740c16c9](https://www.ft.com/content/5207928a-13e8-4832-8c6f-2e78740c16c9)

生成摘要时出错

---

## 47. Acme Weather

**原文标题**: Acme Weather

**原文链接**: [https://acmeweather.com/blog/introducing-acme-weather](https://acmeweather.com/blog/introducing-acme-weather)

生成摘要时出错

---

## 48. Continuous batching (2025)

**原文标题**: Continuous batching (2025)

**原文链接**: [https://huggingface.co/blog/continuous_batching](https://huggingface.co/blog/continuous_batching)

生成摘要时出错

---

## 49. I found a useful Git one liner buried in leaked CIA developer docs

**原文标题**: I found a useful Git one liner buried in leaked CIA developer docs

**原文链接**: [https://spencer.wtf/2026/02/20/cleaning-up-merged-git-branches-a-one-liner-from-the-cias-leaked-dev-docs.html](https://spencer.wtf/2026/02/20/cleaning-up-merged-git-branches-a-one-liner-from-the-cias-leaked-dev-docs.html)

生成摘要时出错

---

## 50. Building a model that visualizes strategic golf

**原文标题**: Building a model that visualizes strategic golf

**原文链接**: [https://golfcoursewiki.substack.com/p/i-spent-the-last-month-and-a-half](https://golfcoursewiki.substack.com/p/i-spent-the-last-month-and-a-half)

生成摘要时出错

---

## 51. How to Review an AUR Package

**原文标题**: How to Review an AUR Package

**原文链接**: [https://bertptrs.nl/2026/01/30/how-to-review-an-aur-package.html](https://bertptrs.nl/2026/01/30/how-to-review-an-aur-package.html)

生成摘要时出错

---

## 52. LibreOffice blasts OnlyOffice for working with Microsoft to lock users in

**原文标题**: LibreOffice blasts OnlyOffice for working with Microsoft to lock users in

**原文链接**: [https://www.neowin.net/news/libreoffice-blasts-fake-open-source-onlyoffice-for-working-with-microsoft-to-lock-users-in/](https://www.neowin.net/news/libreoffice-blasts-fake-open-source-onlyoffice-for-working-with-microsoft-to-lock-users-in/)

生成摘要时出错

---

## 53. A chatbot's worst enemy is page refresh

**原文标题**: A chatbot's worst enemy is page refresh

**原文链接**: [https://zknill.io/posts/chatbots-worst-enemy-is-page-refresh/](https://zknill.io/posts/chatbots-worst-enemy-is-page-refresh/)

生成摘要时出错

---

## 54. Raspberry Pi Pico 2 at 873.5MHz with 3.05V Core Abuse

**原文标题**: Raspberry Pi Pico 2 at 873.5MHz with 3.05V Core Abuse

**原文链接**: [https://learn.pimoroni.com/article/overclocking-the-pico-2](https://learn.pimoroni.com/article/overclocking-the-pico-2)

生成摘要时出错

---

## 55. Gemini 3.1 Pro

**原文标题**: Gemini 3.1 Pro

**原文链接**: [https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-pro/](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-pro/)

生成摘要时出错

---

## 56. Reproducible and traceable configuration for Conan C and C++ package manager

**原文标题**: Reproducible and traceable configuration for Conan C and C++ package manager

**原文链接**: [https://blog.conan.io/cpp/conan/configuration/reproducibility/lockfile/2026/02/17/Reproducible-Configuration-Conan.html](https://blog.conan.io/cpp/conan/configuration/reproducibility/lockfile/2026/02/17/Reproducible-Configuration-Conan.html)

生成摘要时出错

---

## 57. Huge study finds a link between cannabis use in teens and psychosis later

**原文标题**: Huge study finds a link between cannabis use in teens and psychosis later

**原文链接**: [https://www.npr.org/2026/02/21/nx-s1-5719338/cannabis-marijuana-weed-teens-psychosis-jama](https://www.npr.org/2026/02/21/nx-s1-5719338/cannabis-marijuana-weed-teens-psychosis-jama)

生成摘要时出错

---

## 58. WebMCP App for Composing Music

**原文标题**: WebMCP App for Composing Music

**原文链接**: [https://music.leanmcp.live/?id=RrFINcOq](https://music.leanmcp.live/?id=RrFINcOq)

生成摘要时出错

---

## 59. Child's Play: Tech's new generation and the end of thinking

**原文标题**: Child's Play: Tech's new generation and the end of thinking

**原文链接**: [https://harpers.org/archive/2026/03/childs-play-sam-kriss-ai-startup-roy-lee/](https://harpers.org/archive/2026/03/childs-play-sam-kriss-ai-startup-roy-lee/)

生成摘要时出错

---

## 60. Reading the undocumented MEMS accelerometer on Apple Silicon MacBooks via iokit

**原文标题**: Reading the undocumented MEMS accelerometer on Apple Silicon MacBooks via iokit

**原文链接**: [https://github.com/olvvier/apple-silicon-accelerometer](https://github.com/olvvier/apple-silicon-accelerometer)

生成摘要时出错

---

## 61. PayPal discloses data breach that exposed user info for 6 months

**原文标题**: PayPal discloses data breach that exposed user info for 6 months

**原文链接**: [https://www.bleepingcomputer.com/news/security/paypal-discloses-data-breach-exposing-users-personal-information/](https://www.bleepingcomputer.com/news/security/paypal-discloses-data-breach-exposing-users-personal-information/)

生成摘要时出错

---

## 62. EU mandates replaceable batteries by 2027 (2023)

**原文标题**: EU mandates replaceable batteries by 2027 (2023)

**原文链接**: [https://environment.ec.europa.eu/news/new-law-more-sustainable-circular-and-safe-batteries-enters-force-2023-08-17_en](https://environment.ec.europa.eu/news/new-law-more-sustainable-circular-and-safe-batteries-enters-force-2023-08-17_en)

生成摘要时出错

---

## 63. ATAboy is a USB adapter for legacy CHS only style IDE (PATA) drives

**原文标题**: ATAboy is a USB adapter for legacy CHS only style IDE (PATA) drives

**原文链接**: [https://github.com/redruM0381/ATAboy](https://github.com/redruM0381/ATAboy)

生成摘要时出错

---

## 64. The Rediscovery of 103 Hokusai Lost Sketches (2021)

**原文标题**: The Rediscovery of 103 Hokusai Lost Sketches (2021)

**原文链接**: [https://japan-forward.com/eternal-hokusai-the-rediscovery-of-103-hokusai-lost-sketches/](https://japan-forward.com/eternal-hokusai-the-rediscovery-of-103-hokusai-lost-sketches/)

生成摘要时出错

---

## 65. FreeCAD

**原文标题**: FreeCAD

**原文链接**: [https://www.freecad.org/index.php](https://www.freecad.org/index.php)

生成摘要时出错

---

## 66. The Popper Principle

**原文标题**: The Popper Principle

**原文链接**: [https://theamericanscholar.org/the-popper-principle/](https://theamericanscholar.org/the-popper-principle/)

生成摘要时出错

---

## 67. Minions – Stripe's Coding Agents Part 2

**原文标题**: Minions – Stripe's Coding Agents Part 2

**原文链接**: [https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents-part-2](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents-part-2)

生成摘要时出错

---

## 68. Show HN: Ghostty-based terminal with vertical tabs and notifications

**原文标题**: Show HN: Ghostty-based terminal with vertical tabs and notifications

**原文链接**: [https://github.com/manaflow-ai/cmux](https://github.com/manaflow-ai/cmux)

生成摘要时出错

---

## 69. AI is not a coworker, it's an exoskeleton

**原文标题**: AI is not a coworker, it's an exoskeleton

**原文链接**: [https://www.kasava.dev/blog/ai-as-exoskeleton](https://www.kasava.dev/blog/ai-as-exoskeleton)

生成摘要时出错

---

## 70. An ARM Homelab Server, or a Minisforum MS-R1 Review

**原文标题**: An ARM Homelab Server, or a Minisforum MS-R1 Review

**原文链接**: [https://sour.coffee/2026/02/20/an-arm-homelab-server-or-a-minisforum-ms-r1-review/](https://sour.coffee/2026/02/20/an-arm-homelab-server-or-a-minisforum-ms-r1-review/)

生成摘要时出错

---

## 71. Infrastructure decisions I endorse or regret after 4 years at a startup (2024)

**原文标题**: Infrastructure decisions I endorse or regret after 4 years at a startup (2024)

**原文链接**: [https://cep.dev/posts/every-infrastructure-decision-i-endorse-or-regret-after-4-years-running-infrastructure-at-a-startup/](https://cep.dev/posts/every-infrastructure-decision-i-endorse-or-regret-after-4-years-running-infrastructure-at-a-startup/)

生成摘要时出错

---

## 72. Lexega Turns SQL into Signals

**原文标题**: Lexega Turns SQL into Signals

**原文链接**: [https://lexega.com/blog/how-lexega-turns-sql-into-signals](https://lexega.com/blog/how-lexega-turns-sql-into-signals)

生成摘要时出错

---

## 73. Web Components: The Framework-Free Renaissance

**原文标题**: Web Components: The Framework-Free Renaissance

**原文链接**: [https://www.caimito.net/en/blog/2026/02/17/web-components-the-framework-free-renaissance.html](https://www.caimito.net/en/blog/2026/02/17/web-components-the-framework-free-renaissance.html)

生成摘要时出错

---

## 74. Fast KV Compaction via Attention Matching

**原文标题**: Fast KV Compaction via Attention Matching

**原文链接**: [https://arxiv.org/abs/2602.16284](https://arxiv.org/abs/2602.16284)

生成摘要时出错

---

## 75. Pi for Excel: AI sidebar add-in for Excel

**原文标题**: Pi for Excel: AI sidebar add-in for Excel

**原文链接**: [https://github.com/tmustier/pi-for-excel](https://github.com/tmustier/pi-for-excel)

生成摘要时出错

---

## 76. US plans online portal to bypass content bans in Europe and elsewhere

**原文标题**: US plans online portal to bypass content bans in Europe and elsewhere

**原文链接**: [https://www.reuters.com/world/us-plans-online-portal-bypass-content-bans-europe-elsewhere-2026-02-18/](https://www.reuters.com/world/us-plans-online-portal-bypass-content-bans-europe-elsewhere-2026-02-18/)

生成摘要时出错

---

## 77. Defer available in gcc and clang

**原文标题**: Defer available in gcc and clang

**原文链接**: [https://gustedt.wordpress.com/2026/02/15/defer-available-in-gcc-and-clang/](https://gustedt.wordpress.com/2026/02/15/defer-available-in-gcc-and-clang/)

生成摘要时出错

---

## 78. Show HN: Micasa – track your house from the terminal

**原文标题**: Show HN: Micasa – track your house from the terminal

**原文链接**: [https://micasa.dev](https://micasa.dev)

生成摘要时出错

---

## 79. Sizing chaos

**原文标题**: Sizing chaos

**原文链接**: [https://pudding.cool/2026/02/womens-sizing/](https://pudding.cool/2026/02/womens-sizing/)

生成摘要时出错

---

## 80. Consistency diffusion language models: Up to 14x faster, no quality loss

**原文标题**: Consistency diffusion language models: Up to 14x faster, no quality loss

**原文链接**: [https://www.together.ai/blog/consistency-diffusion-language-models](https://www.together.ai/blog/consistency-diffusion-language-models)

生成摘要时出错

---

## 81. Lessons learned from `oapi-codegen`'s time in the GitHub Secure Open Source Fund

**原文标题**: Lessons learned from `oapi-codegen`'s time in the GitHub Secure Open Source Fund

**原文链接**: [https://www.jvt.me/posts/2026/02/17/oapi-codegen-github-secure/](https://www.jvt.me/posts/2026/02/17/oapi-codegen-github-secure/)

生成摘要时出错

---

## 82. Show HN: A physically-based GPU ray tracer written in Julia

**原文标题**: Show HN: A physically-based GPU ray tracer written in Julia

**原文链接**: [https://makie.org/website/blogposts/raytracing/](https://makie.org/website/blogposts/raytracing/)

生成摘要时出错

---

## 83. Visible Spectra of the Elements

**原文标题**: Visible Spectra of the Elements

**原文链接**: [https://atomic-spectra.net/](https://atomic-spectra.net/)

生成摘要时出错

---

## 84. Be wary of Bluesky

**原文标题**: Be wary of Bluesky

**原文链接**: [https://kevinak.se/blog/be-wary-of-bluesky](https://kevinak.se/blog/be-wary-of-bluesky)

生成摘要时出错

---

## 85. Archaeologists find possible first direct evidence of Hannibal's war elephants

**原文标题**: Archaeologists find possible first direct evidence of Hannibal's war elephants

**原文链接**: [https://www.smithsonianmag.com/smart-news/archaeologists-unearthed-a-2200-year-old-bone-they-say-it-could-be-the-first-direct-evidence-of-hannibals-legendary-war-elephants-180988185/](https://www.smithsonianmag.com/smart-news/archaeologists-unearthed-a-2200-year-old-bone-they-say-it-could-be-the-first-direct-evidence-of-hannibals-legendary-war-elephants-180988185/)

生成摘要时出错

---

## 86. My 1981 adventure game is now a multimedia extravaganza

**原文标题**: My 1981 adventure game is now a multimedia extravaganza

**原文链接**: [https://technologizer.com/home/2026/02/16/arctic-adventure-2026/](https://technologizer.com/home/2026/02/16/arctic-adventure-2026/)

生成摘要时出错

---

## 87. Don't create .gitkeep files, use .gitignore instead (2023)

**原文标题**: Don't create .gitkeep files, use .gitignore instead (2023)

**原文链接**: [https://adamj.eu/tech/2023/09/18/git-dont-create-gitkeep/](https://adamj.eu/tech/2023/09/18/git-dont-create-gitkeep/)

生成摘要时出错

---

## 88. Instant AI Response

**原文标题**: Instant AI Response

**原文链接**: [https://chatjimmy.ai/](https://chatjimmy.ai/)

生成摘要时出错

---

## 89. How were video transfers made? (2011)

**原文标题**: How were video transfers made? (2011)

**原文链接**: [https://www.film-tech.com/ubb/f12/t000972.html](https://www.film-tech.com/ubb/f12/t000972.html)

生成摘要时出错

---

## 90. Measuring AI agent autonomy in practice

**原文标题**: Measuring AI agent autonomy in practice

**原文链接**: [https://www.anthropic.com/research/measuring-agent-autonomy](https://www.anthropic.com/research/measuring-agent-autonomy)

生成摘要时出错

---

## 91. Trump raises tariffs to 15% day after Supreme Court ruling

**原文标题**: Trump raises tariffs to 15% day after Supreme Court ruling

**原文链接**: [https://www.bbc.co.uk/news/articles/cn8z48xwqn3o](https://www.bbc.co.uk/news/articles/cn8z48xwqn3o)

生成摘要时出错

---

## 92. Voith Schneider Propeller

**原文标题**: Voith Schneider Propeller

**原文链接**: [https://en.wikipedia.org/wiki/Voith_Schneider_Propeller](https://en.wikipedia.org/wiki/Voith_Schneider_Propeller)

生成摘要时出错

---

## 93. A beginner's guide to split keyboards

**原文标题**: A beginner's guide to split keyboards

**原文链接**: [https://www.justinmklam.com/posts/2026/02/beginners-guide-split-keyboards/](https://www.justinmklam.com/posts/2026/02/beginners-guide-split-keyboards/)

生成摘要时出错

---

## 94. I tried building my startup entirely on European infrastructure

**原文标题**: I tried building my startup entirely on European infrastructure

**原文链接**: [https://www.coinerella.com/made-in-eu-it-was-harder-than-i-thought/](https://www.coinerella.com/made-in-eu-it-was-harder-than-i-thought/)

生成摘要时出错

---

## 95. Show HN: Mini-Diarium - An encrypted, local, cross-platform journaling app

**原文标题**: Show HN: Mini-Diarium - An encrypted, local, cross-platform journaling app

**原文链接**: [https://github.com/fjrevoredo/mini-diarium](https://github.com/fjrevoredo/mini-diarium)

生成摘要时出错

---

## 96. Show HN: A small, simple music theory library in C99

**原文标题**: Show HN: A small, simple music theory library in C99

**原文链接**: [https://github.com/thelowsunoverthemoon/mahler.c](https://github.com/thelowsunoverthemoon/mahler.c)

生成摘要时出错

---

## 97. Uncovering insiders and alpha on Polymarket with AI

**原文标题**: Uncovering insiders and alpha on Polymarket with AI

**原文链接**: [https://twitter.com/peterjliu/status/2024901585806225723](https://twitter.com/peterjliu/status/2024901585806225723)

生成摘要时出错

---

## 98. Zero downtime migrations at petabyte scale (2024)

**原文标题**: Zero downtime migrations at petabyte scale (2024)

**原文链接**: [https://planetscale.com/blog/zero-downtime-migrations-at-petabyte-scale](https://planetscale.com/blog/zero-downtime-migrations-at-petabyte-scale)

生成摘要时出错

---

## 99. Dinosaur Food: 100M year old foods we still eat today (2022)

**原文标题**: Dinosaur Food: 100M year old foods we still eat today (2022)

**原文链接**: [https://borischerny.com/food/2022/01/17/Dinosaur-food.html](https://borischerny.com/food/2022/01/17/Dinosaur-food.html)

生成摘要时出错

---

## 100. Claude Sonnet 4.6

**原文标题**: Claude Sonnet 4.6

**原文链接**: [https://www.anthropic.com/news/claude-sonnet-4-6](https://www.anthropic.com/news/claude-sonnet-4-6)

生成摘要时出错

---

