# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-02-21.md)

*最后自动更新时间: 2026-02-21 17:56:01*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 2 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 3 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 4 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 5 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 6 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 7 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 8 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 9 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 10 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 11 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 12 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 13 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 14 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 15 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 16 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 17 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 18 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 19 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 20 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 21 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 22 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 23 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 24 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 25 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 26 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 27 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 28 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 29 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 30 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 31 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 32 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 33 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 34 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 35 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 36 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 37 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 38 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 39 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 40 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 41 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 42 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 43 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 44 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 45 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 46 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 47 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 48 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 49 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 50 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 51 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 52 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 53 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 54 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 55 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 56 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 57 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 58 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 59 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 60 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 61 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 62 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 63 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 64 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 65 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 66 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 67 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 68 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 69 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 70 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 71 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 72 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 73 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 74 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 75 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 76 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 77 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 78 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 79 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 80 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 81 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 82 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 83 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 84 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 85 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 86 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 87 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 88 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 89 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 90 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 91 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 92 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 93 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 94 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 95 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 96 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 97 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 98 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 99 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 100 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 101 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 102 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 103 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 104 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 105 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 106 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 107 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 108 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 109 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 110 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 111 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 112 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 113 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 114 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 115 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 116 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 117 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 118 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 119 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 120 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 121 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 122 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 123 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 124 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 125 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 126 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 127 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 128 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 129 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 130 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 131 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 132 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 133 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 134 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 135 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 136 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 137 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 138 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 139 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 140 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 141 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 142 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 143 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 144 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 145 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 146 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 147 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 148 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 149 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 150 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 151 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 152 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 153 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 154 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 155 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 156 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 157 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 158 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 159 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 160 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 161 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 162 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 163 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 164 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 165 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 166 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 167 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 168 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 169 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 170 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 171 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 172 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 173 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 174 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 175 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 176 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 177 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 178 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 179 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 180 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 181 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 182 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 183 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 184 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 185 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 186 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 187 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 188 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 189 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 190 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 191 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 192 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 193 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 194 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 195 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 196 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 197 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 198 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 199 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 200 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 201 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 202 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 203 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 204 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 205 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 206 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 207 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 208 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 209 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 210 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 211 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 212 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 213 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 214 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 215 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 216 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 217 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 218 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 219 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 220 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 221 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 222 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 223 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 224 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 225 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 226 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 227 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 228 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 229 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 230 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 231 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 232 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 233 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 234 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 235 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 236 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 237 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 238 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 239 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 240 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 241 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 242 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 243 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 244 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 245 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 246 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 247 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 248 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 249 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 250 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 251 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 252 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 253 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 254 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 255 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 256 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 257 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 258 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 259 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 260 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 261 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 262 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 263 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 264 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 265 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 266 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 267 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 268 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 269 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 270 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 271 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 272 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 273 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 274 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 275 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 276 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 277 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 278 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 279 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 280 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 281 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 282 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 283 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 284 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 285 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 286 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 287 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 288 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 289 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 290 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 291 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 292 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 293 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 294 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 295 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 296 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 297 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 298 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 299 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 300 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 301 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 302 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 303 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 304 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 305 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 306 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 307 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 308 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 309 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 310 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 311 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 312 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 313 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 314 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 315 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 316 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 317 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 318 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 319 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 320 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 321 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 322 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 323 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 324 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 325 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 326 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 327 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 328 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 329 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 330 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 331 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 332 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 333 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 334 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 335 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 336 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 337 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 338 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
