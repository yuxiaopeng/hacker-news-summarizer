# Hacker News 热门文章摘要 (2026-06-21)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 15分钟居家莱姆病蜱虫检测

**原文标题**: 15-minute at-home Lyme disease tick test

**原文链接**: [https://www.bostonglobe.com/2026/06/17/business/lyme-disease-tick-test/](https://www.bostonglobe.com/2026/06/17/business/lyme-disease-tick-test/)

**LymeAlert** 是一款新型的 15 分钟居家诊断工具，旨在检测蜱虫是否携带莱姆病细菌。该工具由儿科骨科助理医师、麻省理工学院毕业生 Erin Dawicki 开发，为传统的实验室检测提供了一种更快速、更实惠的选择。传统实验室检测费用最高可达 450 美元，且处理时间通常需要一周以上。

该测试售价为 40 美元，操作时用户需将最多五只蜱虫放入一个内置研磨器的专用容器中。在蜱虫被研磨成浆状后，插入一条经过化学处理的试纸，若检测到莱姆病细菌，试纸便会变色。Dawicki 的目标是减少不必要的就医和抗生素的过度处方，同时确保被受感染蜱虫叮咬的人群能在关键的 72 小时黄金窗口期内获得治疗。

尽管医学专家承认快速测试的潜在益处，但也有人提醒，假阳性结果可能会引起不必要的恐慌。此外，目前的版本仅能检测莱姆病，无法检测引起 α-半乳糖综合征（Alpha-gal syndrome）等其他蜱传病原体。Dawicki 计划在未来开发能够检测多种感染的升级版本。

除了实体测试工具，该公司还将推出一款智能手机应用程序，允许用户匿名报告受感染蜱虫的发现位置。这些数据将结合美国国家航空航天局（NASA）的卫星图像和人工智能算法，绘制社区级别的蜱传疾病传播预测图。LymeAlert 预计将于今年 8 月正式上市。

---

## 2. 谁拥有你的 ATProto 身份？

**原文标题**: Who owns your ATProto identity?

**原文链接**: [https://kevinak.se/blog/who-actually-owns-your-atproto-identity-hint-its-probably-not-you](https://kevinak.se/blog/who-actually-owns-your-atproto-identity-hint-its-probably-not-you)

本文探讨了 AT Protocol (ATProto) 生态系统中的一个关键安全漏洞：密钥管理的中心化。虽然 ATProto 的设计初衷是去中心化，但作者认为目前的实现方式（如 Bluesky 所使用的）要求用户对个人数据服务器 (PDS) 运营商寄予极高的信任。

核心问题在于 PDS 同时持有用户的**签名密钥**和**轮换密钥**。这赋予了运营商以下权力：

*   **冒充用户**：PDS 可以发布帖文、点赞并提交 commit，而这些操作在加密层面与用户本人的活动无法区分。 
*   **武器化跨应用身份**：由于 ATProto 为多个应用（如社交类的 Bluesky、Git 类的 Tangled、写作类的 Leaflet）提供统一身份，一旦 PDS 遭到攻击，攻击者就可以在用户的整个数字生态系统中冒充该用户。
*   **撤销身份**：运营商可以使用轮换密钥更改用户的去中心化标识符 (DID)，从而有效地将用户拒之门外，并剥夺其与网络中任何应用交互的能力。

作者指出，虽然“自主控制的轮换密钥”可以防止运营商封锁用户，但该功能目前隐藏在 API 中，并非标准注册流程的一部分。为了解决这一问题，作者建议将备份轮换密钥的注册设为账号创建过程中面向用户的默认环节。

最后，文章警告称，ATProto 目前以真正的自主权换取了用户的便利。通过将“核心权力”交给 PDS 运营商，用户面临着从内鬼员工到国家行为体等各种风险，这与该协议的去中心化承诺相违背。

---

## 3. 谷歌 IPv6 采用率达 50%

**原文标题**: Google Hits 50% IPv6

**原文链接**: [https://blog.apnic.net/2026/04/28/google-hits-50-ipv6/](https://blog.apnic.net/2026/04/28/google-hits-50-ipv6/)

本文探讨了谷歌 IPv6 采用率达到 50% 这一里程碑，指出虽然这并未改变技术功能，但它提供了一个强有力的倡导工具，鼓励互联网服务提供商（ISP）和相关组织认真对待这一转型。

尽管取得了进展，作者仍指出了目前阻碍全面部署的几个关键障碍：

*   **可见性与工具：** 搜索引擎和浏览器通常无法让使用 IPv4 连接的用户找到仅支持 IPv6 的网站，而测速和在线率检查器等性能工具也经常误报或忽略 IPv6 数据。
*   **技术限制：** 目前 Linux 内核的局限性导致在不包含 IPv4 组件的情况下无法编译 IPv6。
*   **行业惯性：** 许多 ISP 仍缺乏明确的部署时间表，且主要平台（最典型的是 GitHub）尚未采用 IPv6。
*   **教育：** IT 相关课程通常未能对 IPv6 进行全面覆盖。

作者总结道，解决这些具体障碍对于加速全球向 IPv6 的转型至关重要。

---

## 4. 巴西全国手机收到未经授权警报

**原文标题**: Unauthorized alert sent to cell phones across Brazil

**原文链接**: [https://www.cnn.com/2026/06/20/americas/brazil-hackers-unauthorized-alert-latam](https://www.cnn.com/2026/06/20/americas/brazil-hackers-unauthorized-alert-latam)

周六上午，包括圣保罗和里约热内卢等中心城市在内的巴西多个州的手机用户收到了一条未经授权的“极端警报”，疑为黑客所为。

信息内容为“misantropi4”，是葡萄牙语中“厌世”（misanthropy）一词的数字字母混写（leetspeak）版本。这些警报是通过国家民防部的应急预警平台（类似于美国安珀警报、可直接广播至移动设备的系统）以及短信发送的。

**此次事件的关键细节包括：**
*   **地理范围：** 警报最初出现在南部的巴拉那州，随后蔓延至人口稠密的圣保罗和里约热内卢。
*   **政府回应：** 巴西国家民防部证实，该系统被未经授权的人员远程触发。作为应对，预警平台已暂时下线，当局正在努力重建安全协议。
*   **并无实际威胁：** 受影响各州的民防机构确认，并未发生任何实际的紧急情况、自然灾害或需要发布极端警报的事件。
*   **调查情况：** 巴西国家电信管理局（Anatel）及其他联邦机构正在调查入侵来源以及小区广播（Cellbroadcast）工具的不稳定性。

政府目前正致力于在确保安全的前提下恢复该工具。目前尚无任何组织声称对此次入侵负责。

---

## 5. DOS 游戏《F-15 攻击鹰 II》逆向项目招募 DOS 测试飞行员

**原文标题**: DOS Game "F-15 Strike Eagle II" reversing project needs DOS test pilots

**原文链接**: [https://neuviemeporte.github.io/f15-se2/2026/06/20/needyou.html](https://neuviemeporte.github.io/f15-se2/2026/06/20/needyou.html)

针对1989年DOS游戏《F-15鹰式攻击机II》（F-15 Strike Eagle II）的C语言源码重构逆向工程项目已迎来重大里程碑。经过一段时间的飞速进展，团队已成功重构了所有可执行文件的C代码，完成了汇编数据的迁移，并为绝大多数例程创建了功能性的C语言替代方案。

随着项目重点从匹配汇编操作码转向维持游戏的可玩性，开发者现正招募“测试飞行员”来查找Bug，尤其是那些与数据布局相关的错误。当前发布的版本（v0.9.1）兼容游戏451.03版（包含“沙漠风暴”资料片）。测试者可以通过将原版可执行文件替换为新版本来参与测试。虽然当前构建版本默认采用VGA/MCGA显示，且暂不支持声音和摇杆，但完整的游戏循环——任务简报、飞行及任务总结——现已可以正常运行。

该项目目前的目标是实现“Bug级还原”（bug-for-bug reconstruction），这意味着测试者应仅报告原版游戏中不存在的新问题，如程序崩溃、图形花屏或输入失效。报告应包含对触发问题前操作的描述，并尽可能附带截图。这一里程碑标志着该项目开始向未来多平台移植阶段转型。

---

## 6. UHF X11：专为 visionOS 和 Apple Vision Pro 打造的 X11

**原文标题**: UHF X11: X11 Built for VisionOS and Apple Vision Pro

**原文链接**: [https://www.lispm.net/apps/uhf-x11/](https://www.lispm.net/apps/uhf-x11/)

**UHF X11** 是一款专门为 **visionOS** 和 **Apple Vision Pro** 设计的 X11 窗口系统实现。

该软件的核心功能是**无根空间窗口** (Rootless Spatial Windows)，它使单个 X11 应用程序能够像 visionOS 原生应用一样运行。每个顶级 X11 窗口都会作为一个独立的窗口打开，而不是被限制在单一的虚拟桌面中，用户可以在其 3D 空间环境内的任何位置自由地放置和排列这些窗口。

---

## 7. SMPTE 免费开放其标准

**原文标题**: SMPTE Makes Its Standards Freely Accessible

**原文链接**: [https://www.smpte.org/blog/smpte-makes-its-standards-freely-accessible-openingstandards-library-to-the-global-media-technology-community](https://www.smpte.org/blog/smpte-makes-its-standards-freely-accessible-openingstandards-library-to-the-global-media-technology-community)

**SMPTE 标准开放获取公告摘要**

2026年6月17日，电影与电视工程师协会（SMPTE）宣布了一项具有里程碑意义的举措：将其全面的技术标准库向全球媒体技术社区免费开放。该协会总部位于纽约州怀特普莱恩斯，是全球领先的媒体专业人士、技术专家和工程师组织。

该举措的主要目标是推动全行业的标准采用、简化实施流程，并提高媒体与娱乐领域的互操作性。通过提供标准的开放获取，SMPTE 旨在为创作者和工程师消除障碍，确保所有人都能获得基础性技术框架，例如用于 IP 现场制作的 ST 2110 系列标准和媒体微服务术语。

除了标准制定工作外，该公告还强调了 SMPTE 通过以下方式推进媒体技术的广泛使命：
*   **教育：** 通过 SMPTE 学院提供专业培训，包括“ST 2110 训练营”和色彩管理工作流课程。
*   **出版物：** 通过《电影成像期刊》（*Motion Imaging Journal*）提供行业见解和经过同行评审的研究。
*   **社区：** 通过个人和企业会员、全球活动以及媒体技术峰会支持专业成长。

这一向开放获取的转型标志着该组织支持行业方式的重大转变，旨在迈向一种更具包容性的模式，从而促进全球范围内的创新和卓越技术。

---

## 8. Building reliable agentic AI systems

**原文标题**: Building reliable agentic AI systems

**原文链接**: [https://martinfowler.com/articles/reliable-llm-bayer.html](https://martinfowler.com/articles/reliable-llm-bayer.html)

生成摘要时出错

---

## 9. Whole cross-sectional human ultrasound tomography

**原文标题**: Whole cross-sectional human ultrasound tomography

**原文链接**: [https://www.nature.com/articles/s41551-026-01660-4](https://www.nature.com/articles/s41551-026-01660-4)

生成摘要时出错

---

## 10. 罕见中世纪书签拍卖成交价超出预期

**原文标题**: Rare medieval bookmark exceeds expectations at auction

**原文链接**: [https://www.thehistoryblog.com/archives/76314](https://www.thehistoryblog.com/archives/76314)

生成摘要时出错

---

## 11. Venture Debt for Deep Tech: Financing the Future

**原文标题**: Venture Debt for Deep Tech: Financing the Future

**原文链接**: [https://www.latimes.com/b2b/banking-finance/story/2026-06-21/venture-debt-deep-tech-funding](https://www.latimes.com/b2b/banking-finance/story/2026-06-21/venture-debt-deep-tech-funding)

生成摘要时出错

---

## 12. Proportional-Integral-Derivative Controllers

**原文标题**: Proportional-Integral-Derivative Controllers

**原文链接**: [https://en.wikipedia.org/wiki/PID_controller](https://en.wikipedia.org/wiki/PID_controller)

生成摘要时出错

---

## 13. Alice is impatient

**原文标题**: Alice is impatient

**原文链接**: [https://brooker.co.za/blog/2026/06/19/waiting.html](https://brooker.co.za/blog/2026/06/19/waiting.html)

生成摘要时出错

---

## 14. Guide to the TD4 4-bit DIY CPU

**原文标题**: Guide to the TD4 4-bit DIY CPU

**原文链接**: [https://www.philipzucker.com/td4-4bit-cpu/](https://www.philipzucker.com/td4-4bit-cpu/)

生成摘要时出错

---

## 15. Linux eliminates the strncpy API after six years of work, 360 patches

**原文标题**: Linux eliminates the strncpy API after six years of work, 360 patches

**原文链接**: [https://www.phoronix.com/news/Linux-7.2-Drops-strncpy](https://www.phoronix.com/news/Linux-7.2-Drops-strncpy)

生成摘要时出错

---

## 16. GPT-5.5 hallucinates 3x more than MIT-licensed GLM-5.2

**原文标题**: GPT-5.5 hallucinates 3x more than MIT-licensed GLM-5.2

**原文链接**: [https://arrowtsx.dev/bigger-models/](https://arrowtsx.dev/bigger-models/)

生成摘要时出错

---

## 17. Don’t use AI to write things that you present as your own work

**原文标题**: Don’t use AI to write things that you present as your own work

**原文链接**: [https://www.satisfice.com/blog/archives/488148](https://www.satisfice.com/blog/archives/488148)

生成摘要时出错

---

## 18. Show HN: TownSquare, a tiny presence layer for websites

**原文标题**: Show HN: TownSquare, a tiny presence layer for websites

**原文链接**: [https://townsquare.cauenapier.com/](https://townsquare.cauenapier.com/)

生成摘要时出错

---

## 19. NSA director: 'Mythos "broke into almost all of our classified systems in hours"

**原文标题**: NSA director: 'Mythos "broke into almost all of our classified systems in hours"

**原文链接**: [https://www.economist.com/briefing/2026/06/14/donald-trumps-blocking-of-anthropic-is-capricious-and-chaotic](https://www.economist.com/briefing/2026/06/14/donald-trumps-blocking-of-anthropic-is-capricious-and-chaotic)

生成摘要时出错

---

## 20. Show HN: StartupWiki – A Free Alternative to Crunchbase

**原文标题**: Show HN: StartupWiki – A Free Alternative to Crunchbase

**原文链接**: [https://startupwiki.tech/](https://startupwiki.tech/)

生成摘要时出错

---

## 21. Bun has an open PR adding shared-memory threads to JavaScriptCore

**原文标题**: Bun has an open PR adding shared-memory threads to JavaScriptCore

**原文链接**: [https://github.com/oven-sh/WebKit/pull/249](https://github.com/oven-sh/WebKit/pull/249)

生成摘要时出错

---

## 22. Project Fetch: Phase Two

**原文标题**: Project Fetch: Phase Two

**原文链接**: [https://www.anthropic.com/research/project-fetch-phase-two](https://www.anthropic.com/research/project-fetch-phase-two)

生成摘要时出错

---

## 23. PostgresBench: A Reproducible Benchmark for Postgres Services

**原文标题**: PostgresBench: A Reproducible Benchmark for Postgres Services

**原文链接**: [https://clickhouse.com/blog/postgresbench](https://clickhouse.com/blog/postgresbench)

生成摘要时出错

---

## 24. Show HN: Make PDFs look scanned (CLI or in the browser via WASM)

**原文标题**: Show HN: Make PDFs look scanned (CLI or in the browser via WASM)

**原文链接**: [https://github.com/overflowy/make-look-scanned](https://github.com/overflowy/make-look-scanned)

生成摘要时出错

---

## 25. The rise of South Korea’s weapons business

**原文标题**: The rise of South Korea’s weapons business

**原文链接**: [https://www.politico.com/news/magazine/2026/06/20/south-korea-weapons-dealer-trump-00959559](https://www.politico.com/news/magazine/2026/06/20/south-korea-weapons-dealer-trump-00959559)

生成摘要时出错

---

## 26. Peter H. Diamandis, MD on X: "The Next 5 Years: A Supersonic Tsunami" / X

**原文标题**: Peter H. Diamandis, MD on X: "The Next 5 Years: A Supersonic Tsunami" / X

**原文链接**: [https://twitter.com/PeterDiamandis/status/2068716115941834885](https://twitter.com/PeterDiamandis/status/2068716115941834885)

生成摘要时出错

---

## 27. CSSQuake

**原文标题**: CSSQuake

**原文链接**: [https://cssquake.com/](https://cssquake.com/)

生成摘要时出错

---

## 28. The Wholesale Plagiarism of Obscure Sorrows

**原文标题**: The Wholesale Plagiarism of Obscure Sorrows

**原文链接**: [https://waxy.org/2026/06/the-wholesale-plagiarism-of-obscure-sorrows/](https://waxy.org/2026/06/the-wholesale-plagiarism-of-obscure-sorrows/)

生成摘要时出错

---

## 29. Armstrong Effect

**原文标题**: Armstrong Effect

**原文链接**: [https://en.wikipedia.org/wiki/Armstrong_effect](https://en.wikipedia.org/wiki/Armstrong_effect)

生成摘要时出错

---

## 30. The Lost Story of Alan Turing's "Delilah" Project (2025)

**原文标题**: The Lost Story of Alan Turing's "Delilah" Project (2025)

**原文链接**: [https://spectrum.ieee.org/alan-turings-delilah](https://spectrum.ieee.org/alan-turings-delilah)

生成摘要时出错

---

## 31. Inference cost at scale with napkin math

**原文标题**: Inference cost at scale with napkin math

**原文链接**: [https://injuly.in/blog/napkin-inference-cost/index.html](https://injuly.in/blog/napkin-inference-cost/index.html)

生成摘要时出错

---

## 32. Semiconductor Lifeline Keeps Fighter Jets in the Air

**原文标题**: Semiconductor Lifeline Keeps Fighter Jets in the Air

**原文链接**: [https://spectrum.ieee.org/phoenix-semiconductors-legacychips-oems](https://spectrum.ieee.org/phoenix-semiconductors-legacychips-oems)

生成摘要时出错

---

## 33. 100 Greatest Bird Names of All Time

**原文标题**: 100 Greatest Bird Names of All Time

**原文链接**: [https://birdhistory.substack.com/p/the-100-greatest-bird-names-of-all](https://birdhistory.substack.com/p/the-100-greatest-bird-names-of-all)

生成摘要时出错

---

## 34. Billionaire Tax Officially Heads to Nov. 3 Ballot

**原文标题**: Billionaire Tax Officially Heads to Nov. 3 Ballot

**原文链接**: [https://www.sos.ca.gov/administration/news-releases-and-advisories/2026-news-releases-and-advisories/california-secretary-state-shirley-n-weber-phd-announces-new-measure-eligible-november-2026-general-election-ballot-imposes-one](https://www.sos.ca.gov/administration/news-releases-and-advisories/2026-news-releases-and-advisories/california-secretary-state-shirley-n-weber-phd-announces-new-measure-eligible-november-2026-general-election-ballot-imposes-one)

生成摘要时出错

---

## 35. Millimeter wave technology drills 100 meters into granite

**原文标题**: Millimeter wave technology drills 100 meters into granite

**原文链接**: [https://www.thinkgeoenergy.com/quaise-energy-achieves-100-meters-of-drilling-using-millimeter-wave-technology/](https://www.thinkgeoenergy.com/quaise-energy-achieves-100-meters-of-drilling-using-millimeter-wave-technology/)

生成摘要时出错

---

## 36. NOLA 'Nacular: One man's crusade to preserve New Orleans's vernacular signage

**原文标题**: NOLA 'Nacular: One man's crusade to preserve New Orleans's vernacular signage

**原文链接**: [https://countryroadsmagazine.com/art-and-culture/people-places/nola-nacular/](https://countryroadsmagazine.com/art-and-culture/people-places/nola-nacular/)

生成摘要时出错

---

## 37. Think of the children: How to force real ID for all internet traffic (2023)

**原文标题**: Think of the children: How to force real ID for all internet traffic (2023)

**原文链接**: [https://nochan.net/b/Internet-Crap/20230829-Think-Of-The-Children/](https://nochan.net/b/Internet-Crap/20230829-Think-Of-The-Children/)

生成摘要时出错

---

## 38. Show HN: Microcrad – Micrograd Reimplemented in C

**原文标题**: Show HN: Microcrad – Micrograd Reimplemented in C

**原文链接**: [https://github.com/oraziorillo/microcrad](https://github.com/oraziorillo/microcrad)

生成摘要时出错

---

## 39. Show HN: We post-trained a model that pen tests instead of refusing

**原文标题**: Show HN: We post-trained a model that pen tests instead of refusing

**原文链接**: [https://www.argusred.com/cli](https://www.argusred.com/cli)

生成摘要时出错

---

## 40. Bootimus – A Self-Contained PXE and HTTP Boot Server

**原文标题**: Bootimus – A Self-Contained PXE and HTTP Boot Server

**原文链接**: [https://bootimus.com](https://bootimus.com)

生成摘要时出错

---

## 41. LLMs Are Complicated Now

**原文标题**: LLMs Are Complicated Now

**原文链接**: [https://ianbarber.blog/2026/06/19/llms-are-complicated-now/](https://ianbarber.blog/2026/06/19/llms-are-complicated-now/)

生成摘要时出错

---

## 42. Why has the pointe shoe been so resistant to change?

**原文标题**: Why has the pointe shoe been so resistant to change?

**原文链接**: [https://dancemagazine.com/pointe-shoe-innovation/](https://dancemagazine.com/pointe-shoe-innovation/)

生成摘要时出错

---

## 43. Temporary Cloudflare accounts for AI agents

**原文标题**: Temporary Cloudflare accounts for AI agents

**原文链接**: [https://blog.cloudflare.com/temporary-accounts/](https://blog.cloudflare.com/temporary-accounts/)

生成摘要时出错

---

## 44. Safe SIMD in Rust, Even on the Inside – By Sergey "Shnatsel" Davidoff

**原文标题**: Safe SIMD in Rust, Even on the Inside – By Sergey "Shnatsel" Davidoff

**原文链接**: [https://shnatsel.medium.com/safe-simd-in-rust-even-on-the-inside-c6f1ff381828](https://shnatsel.medium.com/safe-simd-in-rust-even-on-the-inside-c6f1ff381828)

生成摘要时出错

---

## 45. Pondering routing more of my traffic via nodes outside the UK

**原文标题**: Pondering routing more of my traffic via nodes outside the UK

**原文链接**: [https://neilzone.co.uk/2026/06/pondering-routing-more-of-my-traffic-via-nodes-outside-the-uk-because-of-the-direction-of-uk-online-safety-policy/](https://neilzone.co.uk/2026/06/pondering-routing-more-of-my-traffic-via-nodes-outside-the-uk-because-of-the-direction-of-uk-online-safety-policy/)

生成摘要时出错

---

## 46. Vacation With An Artist – Mini-Apprenticeships with Artists in Their Studios

**原文标题**: Vacation With An Artist – Mini-Apprenticeships with Artists in Their Studios

**原文链接**: [https://vawaa.com/](https://vawaa.com/)

生成摘要时出错

---

## 47. Show HN: My Windows XP portfolio with working Game Boy and iPod

**原文标题**: Show HN: My Windows XP portfolio with working Game Boy and iPod

**原文链接**: [https://mitchivin.com/](https://mitchivin.com/)

生成摘要时出错

---

## 48. AI Under Trump's Control: Can France Still Avoid Digital Dependence?

**原文标题**: AI Under Trump's Control: Can France Still Avoid Digital Dependence?

**原文链接**: [https://thenewassociationwebmasters.blogspot.com/2026/06/ai-under-american-control-can-france.html](https://thenewassociationwebmasters.blogspot.com/2026/06/ai-under-american-control-can-france.html)

生成摘要时出错

---

## 49. Bab: A hash function for content-addressable storage

**原文标题**: Bab: A hash function for content-addressable storage

**原文链接**: [https://bab-hash.org/spec](https://bab-hash.org/spec)

生成摘要时出错

---

## 50. Rich Programmer Food (2007)

**原文标题**: Rich Programmer Food (2007)

**原文链接**: [https://steve-yegge.blogspot.com/2007/06/rich-programmer-food.html](https://steve-yegge.blogspot.com/2007/06/rich-programmer-food.html)

生成摘要时出错

---

## 51. Windows 11 New Media Player Uses 3.5x More RAM, Charges for Popular Video Codecs

**原文标题**: Windows 11 New Media Player Uses 3.5x More RAM, Charges for Popular Video Codecs

**原文链接**: [https://www.extremetech.com/computing/windows-11s-new-media-player-uses-35x-more-ram-charges-for-popular-video](https://www.extremetech.com/computing/windows-11s-new-media-player-uses-35x-more-ram-charges-for-popular-video)

生成摘要时出错

---

## 52. The discovery that changed how scientists think about memory

**原文标题**: The discovery that changed how scientists think about memory

**原文链接**: [https://www.ibm.com/think/news/discovery-changed-how-scientists-think-about-memory-kavli-prize](https://www.ibm.com/think/news/discovery-changed-how-scientists-think-about-memory-kavli-prize)

生成摘要时出错

---

## 53. The ability to regrow body parts is dormant in mammals, not lost

**原文标题**: The ability to regrow body parts is dormant in mammals, not lost

**原文链接**: [https://www.sciencedaily.com/releases/2026/06/260617032207.htm](https://www.sciencedaily.com/releases/2026/06/260617032207.htm)

生成摘要时出错

---

## 54. Hyundai buys Boston Dynamics

**原文标题**: Hyundai buys Boston Dynamics

**原文链接**: [https://startupfortune.com/hyundai-takes-full-control-of-boston-dynamics-as-softbank-exits-for-325-million/](https://startupfortune.com/hyundai-takes-full-control-of-boston-dynamics-as-softbank-exits-for-325-million/)

生成摘要时出错

---

## 55. Now You Don't: When Espionage Meets Magic

**原文标题**: Now You Don't: When Espionage Meets Magic

**原文链接**: [https://www.politicshome.com/news/article/now-dont-espionage-meets-magic](https://www.politicshome.com/news/article/now-dont-espionage-meets-magic)

生成摘要时出错

---

## 56. Surprising economics of load-balanced systems

**原文标题**: Surprising economics of load-balanced systems

**原文链接**: [https://brooker.co.za/blog/2020/08/06/erlang.html](https://brooker.co.za/blog/2020/08/06/erlang.html)

生成摘要时出错

---

## 57. Web Browsers on PDAS

**原文标题**: Web Browsers on PDAS

**原文链接**: [https://vale.rocks/posts/pda-browsers](https://vale.rocks/posts/pda-browsers)

生成摘要时出错

---

## 58. How the Fifth Lateran Council Unlocked Financial Theory

**原文标题**: How the Fifth Lateran Council Unlocked Financial Theory

**原文链接**: [https://sebastiangarren.com/2026/06/17/lending-is-meritorious-and-should-be-praised-how-the-fifth-lateran-council-unlocked-financial-theory/](https://sebastiangarren.com/2026/06/17/lending-is-meritorious-and-should-be-praised-how-the-fifth-lateran-council-unlocked-financial-theory/)

生成摘要时出错

---

## 59. Where to Find the Colors Your Screen Can't Show You

**原文标题**: Where to Find the Colors Your Screen Can't Show You

**原文链接**: [https://moultano.wordpress.com/2026/06/19/where-to-find-the-colors-your-screen-cant-show-you/](https://moultano.wordpress.com/2026/06/19/where-to-find-the-colors-your-screen-cant-show-you/)

生成摘要时出错

---

## 60. AMD will reinstate memory encryption on Ryzen 9000 CPUs via BIOS update in July

**原文标题**: AMD will reinstate memory encryption on Ryzen 9000 CPUs via BIOS update in July

**原文链接**: [https://www.tomshardware.com/pc-components/cpus/amd-will-reinstate-memory-encryption-on-ryzen-9000-cpus-through-a-bios-update-in-july-tsme-is-coming-back-after-valuable-community-feedback](https://www.tomshardware.com/pc-components/cpus/amd-will-reinstate-memory-encryption-on-ryzen-9000-cpus-through-a-bios-update-in-july-tsme-is-coming-back-after-valuable-community-feedback)

生成摘要时出错

---

## 61. Tesla plans to sell modular AI data center hardware called 'Megapod'

**原文标题**: Tesla plans to sell modular AI data center hardware called 'Megapod'

**原文链接**: [https://electrek.co/2026/06/21/tesla-megapod-ai-data-center-hardware/](https://electrek.co/2026/06/21/tesla-megapod-ai-data-center-hardware/)

生成摘要时出错

---

## 62. The deskilling of web dev is damaging our health

**原文标题**: The deskilling of web dev is damaging our health

**原文链接**: [https://www.baldurbjarnason.com/2024/the-deskilling-of-web-dev-is-harming-us-all/](https://www.baldurbjarnason.com/2024/the-deskilling-of-web-dev-is-harming-us-all/)

生成摘要时出错

---

## 63. A 1969 camera operators' strike created Upstairs Downstairs multiverse

**原文标题**: A 1969 camera operators' strike created Upstairs Downstairs multiverse

**原文链接**: [https://ironicsans.ghost.io/the-color-strike/](https://ironicsans.ghost.io/the-color-strike/)

生成摘要时出错

---

## 64. Human Judgment as a Specification

**原文标题**: Human Judgment as a Specification

**原文链接**: [https://blog.brownplt.org/2026/06/09/pick.html](https://blog.brownplt.org/2026/06/09/pick.html)

生成摘要时出错

---

## 65. When I reject AI code even if it works

**原文标题**: When I reject AI code even if it works

**原文链接**: [https://vinibrasil.com/when-i-reject-ai-code-even-if-it-works/](https://vinibrasil.com/when-i-reject-ai-code-even-if-it-works/)

生成摘要时出错

---

## 66. The Cold War's Accidental Whale Observatory

**原文标题**: The Cold War's Accidental Whale Observatory

**原文链接**: [https://thereader.mitpress.mit.edu/the-cold-wars-accidental-whale-observatory/](https://thereader.mitpress.mit.edu/the-cold-wars-accidental-whale-observatory/)

生成摘要时出错

---

## 67. Show HN: Talos – Open-source WASM interpreter for Lean

**原文标题**: Show HN: Talos – Open-source WASM interpreter for Lean

**原文链接**: [https://github.com/cajal-technologies/talos](https://github.com/cajal-technologies/talos)

生成摘要时出错

---

## 68. Vulgar Materialism

**原文标题**: Vulgar Materialism

**原文链接**: [https://borretti.me/article/on-vulgar-materialism](https://borretti.me/article/on-vulgar-materialism)

生成摘要时出错

---

## 69. Printing Gaussian Splats

**原文标题**: Printing Gaussian Splats

**原文链接**: [https://www.patreon.com/DanyBittel/posts/printing-splats-161333338](https://www.patreon.com/DanyBittel/posts/printing-splats-161333338)

生成摘要时出错

---

## 70. Computed goto for efficient dispatch tables (2012)

**原文标题**: Computed goto for efficient dispatch tables (2012)

**原文链接**: [https://eli.thegreenplace.net/2012/07/12/computed-goto-for-efficient-dispatch-tables](https://eli.thegreenplace.net/2012/07/12/computed-goto-for-efficient-dispatch-tables)

生成摘要时出错

---

## 71. A Perceptron in Age of Empires II

**原文标题**: A Perceptron in Age of Empires II

**原文链接**: [https://adewynter.github.io/notes/aoe2-circuits](https://adewynter.github.io/notes/aoe2-circuits)

生成摘要时出错

---

## 72. Can you see three trees?

**原文标题**: Can you see three trees?

**原文链接**: [https://www.not-ship.com/can-you-see-three-trees/](https://www.not-ship.com/can-you-see-three-trees/)

生成摘要时出错

---

## 73. Sword Swallowing and Its Side Effects

**原文标题**: Sword Swallowing and Its Side Effects

**原文链接**: [https://pmc.ncbi.nlm.nih.gov/articles/PMC1761150/](https://pmc.ncbi.nlm.nih.gov/articles/PMC1761150/)

生成摘要时出错

---

## 74. There are no instances in ATProto

**原文标题**: There are no instances in ATProto

**原文链接**: [https://overreacted.io/there-are-no-instances-in-atproto/](https://overreacted.io/there-are-no-instances-in-atproto/)

生成摘要时出错

---

## 75. Bobby Prince, composer for Doom, Wolfenstein 3D, and Duke Nukem 3D, has died

**原文标题**: Bobby Prince, composer for Doom, Wolfenstein 3D, and Duke Nukem 3D, has died

**原文链接**: [https://www.legacy.com/legacy/robert-bobby-prince-lll](https://www.legacy.com/legacy/robert-bobby-prince-lll)

生成摘要时出错

---

## 76. AURpocalypse now: a look at the recent AUR attacks

**原文标题**: AURpocalypse now: a look at the recent AUR attacks

**原文链接**: [https://lwn.net/SubscriberLink/1077619/f7b07c5489fdd43a/](https://lwn.net/SubscriberLink/1077619/f7b07c5489fdd43a/)

生成摘要时出错

---

## 77. Egyptian Fractions (2006)

**原文标题**: Egyptian Fractions (2006)

**原文链接**: [https://blog.plover.com/math/egyptian-fractions.html](https://blog.plover.com/math/egyptian-fractions.html)

生成摘要时出错

---

## 78. From PGP to Mythos: a brief history of export controls that didn't stop anyone

**原文标题**: From PGP to Mythos: a brief history of export controls that didn't stop anyone

**原文链接**: [https://techcrunch.com/2026/06/19/encryption-spyware-and-now-mythos-history-shows-why-cyber-export-control-doesnt-work/](https://techcrunch.com/2026/06/19/encryption-spyware-and-now-mythos-history-shows-why-cyber-export-control-doesnt-work/)

生成摘要时出错

---

## 79. Pre-2022 Books

**原文标题**: Pre-2022 Books

**原文链接**: [https://notes.lorenzogravina.com/musings/pre-2022-books](https://notes.lorenzogravina.com/musings/pre-2022-books)

生成摘要时出错

---

## 80. Telescope Ranchers

**原文标题**: Telescope Ranchers

**原文链接**: [https://kottke.org/26/06/telescope-ranchers](https://kottke.org/26/06/telescope-ranchers)

生成摘要时出错

---

## 81. Show HN: Ember, a native iOS Hacker News reader I built around accessibility

**原文标题**: Show HN: Ember, a native iOS Hacker News reader I built around accessibility

**原文链接**: [https://github.com/DatanoiseTV/ember-hackernews](https://github.com/DatanoiseTV/ember-hackernews)

生成摘要时出错

---

## 82. I Stored a Website in a Favicon

**原文标题**: I Stored a Website in a Favicon

**原文链接**: [https://www.timwehrle.de/blog/i-stored-a-website-in-a-favicon/](https://www.timwehrle.de/blog/i-stored-a-website-in-a-favicon/)

生成摘要时出错

---

## 83. Dirty Little Zine – a tool for making an 8 page printable Zine

**原文标题**: Dirty Little Zine – a tool for making an 8 page printable Zine

**原文链接**: [https://dirtylittlezine.com/](https://dirtylittlezine.com/)

生成摘要时出错

---

## 84. Polymarket Paid Dozens to Post Videos of Themselves 'Winning' with Fake Bets

**原文标题**: Polymarket Paid Dozens to Post Videos of Themselves 'Winning' with Fake Bets

**原文链接**: [https://m.slashdot.org/story/455718](https://m.slashdot.org/story/455718)

生成摘要时出错

---

## 85. Mencius (2016)

**原文标题**: Mencius (2016)

**原文链接**: [https://scholarworks.iu.edu/iuswrrest/api/core/bitstreams/265d73a0-6bfa-45df-92ff-4e7d3f8be4b1/content](https://scholarworks.iu.edu/iuswrrest/api/core/bitstreams/265d73a0-6bfa-45df-92ff-4e7d3f8be4b1/content)

生成摘要时出错

---

## 86. Court Records Should Be Free

**原文标题**: Court Records Should Be Free

**原文链接**: [https://www.eff.org/deeplinks/2026/06/court-records-should-be-free](https://www.eff.org/deeplinks/2026/06/court-records-should-be-free)

生成摘要时出错

---

## 87. Show HN: Metiq: a real time 3D globe for 100 public datasets

**原文标题**: Show HN: Metiq: a real time 3D globe for 100 public datasets

**原文链接**: [https://metiq.space](https://metiq.space)

生成摘要时出错

---

## 88. I found 10k GitHub repositories distributing Trojan malware

**原文标题**: I found 10k GitHub repositories distributing Trojan malware

**原文链接**: [https://orchidfiles.com/github-repositories-distributing-malware/](https://orchidfiles.com/github-repositories-distributing-malware/)

生成摘要时出错

---

## 89. Norway imposes near ban on AI in elementary school

**原文标题**: Norway imposes near ban on AI in elementary school

**原文链接**: [https://www.reuters.com/technology/norway-imposes-near-ban-ai-elementary-school-2026-06-19/](https://www.reuters.com/technology/norway-imposes-near-ban-ai-elementary-school-2026-06-19/)

生成摘要时出错

---

## 90. Show HN: Criterion Closet as a website – pull any of 1,247 films off the shelf

**原文标题**: Show HN: Criterion Closet as a website – pull any of 1,247 films off the shelf

**原文链接**: [https://the-criterion-closet.vercel.app](https://the-criterion-closet.vercel.app)

生成摘要时出错

---

