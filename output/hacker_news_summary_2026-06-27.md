# Hacker News 热门文章摘要 (2026-06-27)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 匿名 GitHub 账号正大批量发布未公开的零日漏洞

**原文标题**: Anonymous GitHub account mass-dropping undisclosed 0-days

**原文链接**: [https://github.com/bikini/exploitarium](https://github.com/bikini/exploitarium)

一名匿名研究人员（Discord 账号 @ashdfrkl）发布了一个名为 **“Exploitarium”** 的 GitHub 仓库，该仓库是一个整合了漏洞研究和未公开零日漏洞概念验证（PoC）漏洞利用的综合存档库。

该仓库作为中心枢纽，汇集了此前独立的项目以及日期标注为 2026 年 6 月的新“直接录入”研究。该集合涵盖了广泛的高知名度软件和协议，包括：
*   **浏览器与媒体：** Firefox（私密 URL 外泄）、VLC（VP9 崩溃）和 FFmpeg。
*   **开发与基础设施：** Docker（目标逃逸）、Ghidra 12.1.2（RCE/ACE）、Gitea 和 ImageMagick。
*   **网络与系统：** Nmap（IPv6 回绕）、libssh2、OpenVPN 和 c-ares（UAF）。
*   **语言与工具：** PHP 8.5.7（Soap RCE）、7zip 和 RustDesk。

创建者利用 Git blob ID 匹配来验证整合数据的完整性，确保来自 12 个原始仓库的 96 条跟踪条目与其源代码保持完全一致。

尽管“大规模投放”未公开漏洞具有重大的安全隐患，但作者将该项目定义为“基于诚信的公开披露漏洞研究”。仓库中包含严厉的“滥用”警告，反对恶意使用，并声明该项目的目标是培养对网络安全的兴趣。该研究人员鼓励社区分享该仓库，并通过 Discord 与其联系进行协作，并称公众参与是其持续披露的主要动力。

---

## 2. OpenRA

**原文标题**: OpenRA

**原文链接**: [https://www.openra.net/](https://www.openra.net/)

生成摘要时出错

---

## 3. DSpark: Speculative decoding accelerates LLM inference [pdf]

**原文标题**: DSpark: Speculative decoding accelerates LLM inference [pdf]

**原文链接**: [https://github.com/deepseek-ai/DeepSpec/blob/main/DSpark_paper.pdf](https://github.com/deepseek-ai/DeepSpec/blob/main/DSpark_paper.pdf)

生成摘要时出错

---

## 4. 可疑的不连续性 (2020)

**原文标题**: Suspicious Discontinuities (2020)

**原文链接**: [https://danluu.com/discontinuities/](https://danluu.com/discontinuities/)

《可疑的不连续性》（Suspicious Discontinuities）探讨了政策、社会系统和技术中的剧烈阈值如何产生扭曲的激励机制和“非自然”的数据分布。当输入的微小变化导致输出发生不成比例的变化时，就会出现这些“断崖”，促使个人为了规避惩罚或获取利益而“钻系统的空子”。

作者提供了该现象的几个关键案例：
*   **经济与教育政策：** 奥巴马医改（ACA）补贴和佩尔助学金（Pell Grants）的硬性收入门槛，使得个人为了保持在阈值以下以增加总可支配收入，而故意损失金钱（通常通过高风险期权交易）在财务上变得合理。
*   **科学研究：** $p < 0.05$ 的统计显著性标准导致了“p-hacking”，即研究人员通过操纵数据或选择性发表结果来跨越“显著性”红线。
*   **教育：** 波兰的考试数据显示，在及格线位置出现了可疑的得分峰值，这表明阅卷者会为略低于门槛的学生“找分”。
*   **体育：** 青少年年龄分组产生了“相对年龄效应”，即在日历年年初出生的孩子更有可能成功，因为在选拔时他们比同龄人身体发育更成熟。
*   **法律与政治：** 量刑法律导致毒品指控在强制性最低刑期阈值处出现激增，而选举舞弊往往表现为投票率数据在整数处出现“非自然”的峰值。

作者认为，这些界限分明的规则通常是“次优”的，会导致系统性的低效。为了缓解这些问题，文章建议用**渐进式退出**（slow phase-outs）或连续分布来取代剧烈的不连续性，从而平滑激励机制，减轻操纵结果或行为的压力。

---

## 5. Fintech Engineering Handbook

**原文标题**: Fintech Engineering Handbook

**原文链接**: [https://w.pitula.me/fintech-engineering-handbook/](https://w.pitula.me/fintech-engineering-handbook/)

The **Fintech Engineering Handbook** provides a framework for building reliable financial systems, centered on three core principles: **no invented data** (preventing duplicates), **no lost data** (ensuring full persistence), and **no trust** (verifying all internal and external inputs).

**Representing and Moving Money**
The handbook emphasizes precision, strictly forbidding floating-point types due to unpredictable rounding errors. Instead, it recommends arbitrary-precision decimals or minor-unit integers. Rounding must be an explicit business decision, handled at boundaries to avoid "minting" or losing money. Furthermore, amounts should always be paired with currencies in a single data structure to prevent invalid cross-currency arithmetic. Foreign exchange (FX) rates should be treated as directional and time-sensitive, with the data source explicitly recorded.

**The Ledger and Recording**
Financial records should utilize **double-entry bookkeeping**, where money is moved between accounts rather than just updated. In this model, balances are derived from a history of immutable, append-only entries. The system must distinguish between different timestamps: **Value time** (when it happened), **Booking time** (when it was recorded), and **Settlement time** (when funds moved).

**Auditability and Integrity**
To satisfy regulatory requirements, systems must maintain a comprehensive **audit trail** documenting the "what, when, who, and why" of every change. **Event sourcing** is highlighted as a premier pattern for this, as it derives the system state directly from an immutable log of events, ensuring the trail never drifts from reality. Finally, the handbook stresses **immutability**, suggesting that financial records should be protected by database permissions or cryptographic checksums to ensure they remain tamper-evident and verifiable.

---

## 6. AI 正在设计人类甚至无法想象的无线电芯片

**原文标题**: AI Is Designing Radio Chips That Humans Couldn't Even Imagine

**原文链接**: [https://spectrum.ieee.org/ai-radio-chip-design](https://spectrum.ieee.org/ai-radio-chip-design)

Traditional radio-frequency integrated circuit (RFIC) design is an essential but notoriously difficult "dark art" that governs the functionality of 5G, satellite communications, and autonomous vehicles. Unlike standard computing chips, RFICs require the complex balancing of electromagnetic fields, thermodynamics, and physical constraints. This artisanal process has historically relied on human intuition and existing design templates, creating a massive bottleneck in wireless technology development.

Researchers at Princeton University are breaking this bottleneck by using AI to design RFICs from scratch. By employing reinforcement learning and inverse design, the AI is freed from the constraints of human aesthetics and intelligibility. Much like AlphaGo Zero, which learned to play Go through self-play rather than human examples, this AI explores the vast design space to discover novel circuit topologies and electromagnetic structures that traditional designers would never conceive.

The results are transformative:
*   **Performance:** AI-generated chips, which often resemble abstract art rather than symmetrical circuits, frequently outperform state-of-the-art human designs.
*   **Efficiency:** The AI can conceive working designs in a fraction of the time, reducing the design cycle by orders of magnitude.
*   **Innovation:** Using diffusion models, researchers can rapidly generate novel RF layouts that optimize for specific performance goals while managing complex physical trade-offs like impedance matching.

The author concludes that the future of RFIC design lies in shifting away from artisanal manual labor toward algorithmic synthesis. To fully realize this potential, the industry must develop large, shared datasets and open ecosystems, allowing AI to master universal electromagnetic and circuit behaviors. This transition is critical for the next generation of wireless technology, including 6G and beyond.

---

## 7. Post-Mythos Cybersecurity: Keep calm and carry on

**原文标题**: Post-Mythos Cybersecurity: Keep calm and carry on

**原文链接**: [https://cephalosec.com/blog/cybersecurity-in-the-post-mythos-era-keep-calm-and-carry-on/](https://cephalosec.com/blog/cybersecurity-in-the-post-mythos-era-keep-calm-and-carry-on/)

生成摘要时出错

---

## 8. Supabase (YC S20) Is Hiring for Multigres

**原文标题**: Supabase (YC S20) Is Hiring for Multigres

**原文链接**: [https://jobs.ashbyhq.com/supabase/2e718684-4f75-4a99-8d6b-3b6bd44e4228](https://jobs.ashbyhq.com/supabase/2e718684-4f75-4a99-8d6b-3b6bd44e4228)

生成摘要时出错

---

## 9. Zuckerberg's Increasingly Bizarre War on Whistleblowers

**原文标题**: Zuckerberg's Increasingly Bizarre War on Whistleblowers

**原文链接**: [https://pluralistic.net/2026/06/27/zuckerstreisand-2/](https://pluralistic.net/2026/06/27/zuckerstreisand-2/)

生成摘要时出错

---

## 10. If you can't hold it, you don't own it

**原文标题**: If you can't hold it, you don't own it

**原文链接**: [https://dervis.de/physical/](https://dervis.de/physical/)

生成摘要时出错

---

## 11. One man, two kernels, and a lot of RISC-V

**原文标题**: One man, two kernels, and a lot of RISC-V

**原文链接**: [https://www.theregister.com/software/2026/06/26/one-man-two-kernels-and-a-lot-of-risc-v/5262858](https://www.theregister.com/software/2026/06/26/one-man-two-kernels-and-a-lot-of-risc-v/5262858)

生成摘要时出错

---

## 12. Reducing tick density along recreational trails in Ottawa, Canada

**原文标题**: Reducing tick density along recreational trails in Ottawa, Canada

**原文链接**: [https://www.sciencedirect.com/science/article/pii/S1877959X26000476](https://www.sciencedirect.com/science/article/pii/S1877959X26000476)

生成摘要时出错

---

## 13. Previewing GPT‑5.6 Sol: a next-generation model

**原文标题**: Previewing GPT‑5.6 Sol: a next-generation model

**原文链接**: [https://openai.com/index/previewing-gpt-5-6-sol/](https://openai.com/index/previewing-gpt-5-6-sol/)

生成摘要时出错

---

## 14. Researchers have developed pixels that can emit and analyse light together

**原文标题**: Researchers have developed pixels that can emit and analyse light together

**原文链接**: [https://ethz.ch/en/news-and-events/eth-news/news/2026/06/a-new-type-of-pixel.html](https://ethz.ch/en/news-and-events/eth-news/news/2026/06/a-new-type-of-pixel.html)

生成摘要时出错

---

## 15. How Many Elementary Particles Are There, Really?

**原文标题**: How Many Elementary Particles Are There, Really?

**原文链接**: [https://www.quantamagazine.org/how-many-elementary-particles-are-there-really-20260615/](https://www.quantamagazine.org/how-many-elementary-particles-are-there-really-20260615/)

生成摘要时出错

---

## 16. Long Wave radio era set to end with switch-off

**原文标题**: Long Wave radio era set to end with switch-off

**原文链接**: [https://www.economist.com/britain/2026/06/25/the-bbc-switches-off-its-oldest-service](https://www.economist.com/britain/2026/06/25/the-bbc-switches-off-its-oldest-service)

Unable to access the article link.

---

## 17. Task Failed Successfully: Saturating NIC and Disk Bandwidth

**原文标题**: Task Failed Successfully: Saturating NIC and Disk Bandwidth

**原文链接**: [https://blog.mrcroxx.com/posts/task-failed-successfully-saturating-nic-and-disk-bandwidth/](https://blog.mrcroxx.com/posts/task-failed-successfully-saturating-nic-and-disk-bandwidth/)

生成摘要时出错

---

## 18. Beer CSS – Build material design in record time

**原文标题**: Beer CSS – Build material design in record time

**原文链接**: [https://www.beercss.com](https://www.beercss.com)

生成摘要时出错

---

## 19. Linux on Older Hardware: The Complete Revival Guide

**原文标题**: Linux on Older Hardware: The Complete Revival Guide

**原文链接**: [https://www.fosslinux.com/158206/linux-on-older-hardware-revival-guide.htm](https://www.fosslinux.com/158206/linux-on-older-hardware-revival-guide.htm)

生成摘要时出错

---

## 20. The US Army Issued Ocarinas to Soldiers in World War II

**原文标题**: The US Army Issued Ocarinas to Soldiers in World War II

**原文链接**: [https://www.flutetunes.com/articles/my-flute-goes-to-war/](https://www.flutetunes.com/articles/my-flute-goes-to-war/)

生成摘要时出错

---

## 21. Streaming services' obnoxiously loud ads become illegal on July 1 in California

**原文标题**: Streaming services' obnoxiously loud ads become illegal on July 1 in California

**原文链接**: [https://arstechnica.com/gadgets/2026/06/streaming-services-obnoxiously-loud-ads-become-illegal-on-july-1-in-california/](https://arstechnica.com/gadgets/2026/06/streaming-services-obnoxiously-loud-ads-become-illegal-on-july-1-in-california/)

生成摘要时出错

---

## 22. Why does kinetic energy increase quadratically, not linearly, with speed? (2011)

**原文标题**: Why does kinetic energy increase quadratically, not linearly, with speed? (2011)

**原文链接**: [https://physics.stackexchange.com/questions/535/why-does-kinetic-energy-increase-quadratically-not-linearly-with-speed](https://physics.stackexchange.com/questions/535/why-does-kinetic-energy-increase-quadratically-not-linearly-with-speed)

生成摘要时出错

---

## 23. WordStar: A Writer's Word Processor (1996)

**原文标题**: WordStar: A Writer's Word Processor (1996)

**原文链接**: [https://www.sfwriter.com/wordstar.htm](https://www.sfwriter.com/wordstar.htm)

生成摘要时出错

---

## 24. Doctors suspected man had brain cancer. He had worms

**原文标题**: Doctors suspected man had brain cancer. He had worms

**原文链接**: [https://arstechnica.com/health/2026/06/doctors-suspected-man-had-brain-cancer-he-actually-had-worms/](https://arstechnica.com/health/2026/06/doctors-suspected-man-had-brain-cancer-he-actually-had-worms/)

生成摘要时出错

---

## 25. Underarm Bowling Incident of 1981

**原文标题**: Underarm Bowling Incident of 1981

**原文链接**: [https://en.wikipedia.org/wiki/Underarm_bowling_incident_of_1981](https://en.wikipedia.org/wiki/Underarm_bowling_incident_of_1981)

生成摘要时出错

---

## 26. Anatomy of a Failed (Nation-State?) Attack

**原文标题**: Anatomy of a Failed (Nation-State?) Attack

**原文链接**: [https://grack.com/blog/2026/06/25/dissecting-a-failed-nation-state-attack/](https://grack.com/blog/2026/06/25/dissecting-a-failed-nation-state-attack/)

生成摘要时出错

---

## 27. Jest/Vitest interactive course (runs in the browser)

**原文标题**: Jest/Vitest interactive course (runs in the browser)

**原文链接**: [https://howtotestfrontend.com/courses/jest-vitest-fundamentals](https://howtotestfrontend.com/courses/jest-vitest-fundamentals)

生成摘要时出错

---

## 28. Faster KNN search in Manticore: 2-pass HNSW, batched distances, and AVX-512

**原文标题**: Faster KNN search in Manticore: 2-pass HNSW, batched distances, and AVX-512

**原文链接**: [https://medium.com/@s_nikolaev/faster-knn-search-in-manticore-2-pass-hnsw-batched-distances-and-avx-512-b85604647aab](https://medium.com/@s_nikolaev/faster-knn-search-in-manticore-2-pass-hnsw-batched-distances-and-avx-512-b85604647aab)

生成摘要时出错

---

## 29. Cultures of Making and Relating

**原文标题**: Cultures of Making and Relating

**原文链接**: [https://blog.khinsen.net/posts/2026/06/25/cultures.html](https://blog.khinsen.net/posts/2026/06/25/cultures.html)

生成摘要时出错

---

## 30. MicroVMs: Run isolated sandboxes with full lifecycle control

**原文标题**: MicroVMs: Run isolated sandboxes with full lifecycle control

**原文链接**: [https://aws.amazon.com/blogs/aws/run-isolated-sandboxes-with-full-lifecycle-control-aws-lambda-introduces-microvms/](https://aws.amazon.com/blogs/aws/run-isolated-sandboxes-with-full-lifecycle-control-aws-lambda-introduces-microvms/)

生成摘要时出错

---

## 31. The gap between open weights LLMs and closed source LLMs

**原文标题**: The gap between open weights LLMs and closed source LLMs

**原文链接**: [https://blog.doubleword.ai/frontier-os-llm](https://blog.doubleword.ai/frontier-os-llm)

生成摘要时出错

---

## 32. AI in mathematics is forcing big questions

**原文标题**: AI in mathematics is forcing big questions

**原文链接**: [https://spectrum.ieee.org/ai-in-mathematics](https://spectrum.ieee.org/ai-in-mathematics)

生成摘要时出错

---

## 33. U.S. allows Anthropic to release Mythos AI to ‘trusted’ US organizations

**原文标题**: U.S. allows Anthropic to release Mythos AI to ‘trusted’ US organizations

**原文链接**: [https://www.semafor.com/article/06/27/2026/us-releases-powerful-anthropic-model-mythos-to-some-us-companies](https://www.semafor.com/article/06/27/2026/us-releases-powerful-anthropic-model-mythos-to-some-us-companies)

生成摘要时出错

---

## 34. International investment and local rules push prices up faster than supply

**原文标题**: International investment and local rules push prices up faster than supply

**原文链接**: [https://news.mccombs.utexas.edu/research/foreign-funds-help-make-housing-unaffordable/](https://news.mccombs.utexas.edu/research/foreign-funds-help-make-housing-unaffordable/)

生成摘要时出错

---

## 35. Like a Bouncer at a Bookstore: Texas' App Store Accountability Act

**原文标题**: Like a Bouncer at a Bookstore: Texas' App Store Accountability Act

**原文链接**: [https://cdt.org/insights/like-a-bouncer-at-a-bookstore-texas-app-store-accountability-act-is-unconstitutional/](https://cdt.org/insights/like-a-bouncer-at-a-bookstore-texas-app-store-accountability-act-is-unconstitutional/)

生成摘要时出错

---

## 36. U.S. government will decide who gets to use GPT-5.6

**原文标题**: U.S. government will decide who gets to use GPT-5.6

**原文链接**: [https://www.washingtonpost.com/technology/2026/06/26/openai-says-us-government-will-vet-users-its-latest-ai-model/](https://www.washingtonpost.com/technology/2026/06/26/openai-says-us-government-will-vet-users-its-latest-ai-model/)

生成摘要时出错

---

## 37. Screen time can damage under-twos' development, landmark study suggests

**原文标题**: Screen time can damage under-twos' development, landmark study suggests

**原文链接**: [https://www.theguardian.com/society/2026/jun/27/screen-time-damage-under-twos-development-study](https://www.theguardian.com/society/2026/jun/27/screen-time-damage-under-twos-development-study)

生成摘要时出错

---

## 38. Ultrasound imaging of the brain

**原文标题**: Ultrasound imaging of the brain

**原文链接**: [https://alephneuro.com/blog/ultrasound-brain](https://alephneuro.com/blog/ultrasound-brain)

生成摘要时出错

---

## 39. A peek into Reddit's anti-spam internals

**原文标题**: A peek into Reddit's anti-spam internals

**原文链接**: [https://lyra.horse/blog/2026/06/reddit-spam-internals/](https://lyra.horse/blog/2026/06/reddit-spam-internals/)

生成摘要时出错

---

## 40. Hellishly Slow Level 13 Deflate Compression

**原文标题**: Hellishly Slow Level 13 Deflate Compression

**原文链接**: [https://kirill.korins.ky/articles/hellishly-slow-level-13-deflate-compression/](https://kirill.korins.ky/articles/hellishly-slow-level-13-deflate-compression/)

生成摘要时出错

---

## 41. OpenTTD 16.0-Beta1

**原文标题**: OpenTTD 16.0-Beta1

**原文链接**: [https://www.openttd.org/news/2026/06/25/openttd-16-0-beta1](https://www.openttd.org/news/2026/06/25/openttd-16-0-beta1)

生成摘要时出错

---

## 42. Show HN: Hacker News on a train station-style flip board

**原文标题**: Show HN: Hacker News on a train station-style flip board

**原文链接**: [https://popflame.quickish.space/hn-flipboard/](https://popflame.quickish.space/hn-flipboard/)

生成摘要时出错

---

## 43. You've tried DuckDuckGo and Brave Search, now get serious with SearXNG

**原文标题**: You've tried DuckDuckGo and Brave Search, now get serious with SearXNG

**原文链接**: [https://www.neowin.net/editorials/youve-tried-duckduckgo-and-brave-search-now-get-serious-with-searxng/](https://www.neowin.net/editorials/youve-tried-duckduckgo-and-brave-search-now-get-serious-with-searxng/)

生成摘要时出错

---

## 44. Show HN: Smart model routing directly in Claude, Codex and Cursor

**原文标题**: Show HN: Smart model routing directly in Claude, Codex and Cursor

**原文链接**: [https://github.com/workweave/router](https://github.com/workweave/router)

生成摘要时出错

---

## 45. Fusion Programming Language

**原文标题**: Fusion Programming Language

**原文链接**: [https://fusion-lang.org/](https://fusion-lang.org/)

生成摘要时出错

---

## 46. Om

**原文标题**: Om

**原文链接**: [https://daringfireball.net/2026/06/om](https://daringfireball.net/2026/06/om)

生成摘要时出错

---

## 47. What Is a Nomogram and Why Would It Interest Me?

**原文标题**: What Is a Nomogram and Why Would It Interest Me?

**原文链接**: [https://lefakkomies.github.io/pynomo-doc/introduction/introduction.html#what-is-a-nomogram-and-why-would-it-interest-me](https://lefakkomies.github.io/pynomo-doc/introduction/introduction.html#what-is-a-nomogram-and-why-would-it-interest-me)

生成摘要时出错

---

## 48. We can still stop California's 3D printer surveillance scheme

**原文标题**: We can still stop California's 3D printer surveillance scheme

**原文链接**: [https://www.eff.org/deeplinks/2026/06/we-can-still-stop-californias-3d-printer-surveillance-scheme](https://www.eff.org/deeplinks/2026/06/we-can-still-stop-californias-3d-printer-surveillance-scheme)

生成摘要时出错

---

## 49. Belonging to the Land

**原文标题**: Belonging to the Land

**原文链接**: [https://www.5jt.com/belonging-to-the-land](https://www.5jt.com/belonging-to-the-land)

生成摘要时出错

---

## 50. Software Is Becoming Marketing

**原文标题**: Software Is Becoming Marketing

**原文链接**: [https://www.terezatizkova.com/writing/software-abundance](https://www.terezatizkova.com/writing/software-abundance)

生成摘要时出错

---

## 51. How H-E-B Became Texas' Most Beloved Brand (2024)

**原文标题**: How H-E-B Became Texas' Most Beloved Brand (2024)

**原文链接**: [https://texashighways.com/culture/how-heb-became-texas-most-beloved-brand/](https://texashighways.com/culture/how-heb-became-texas-most-beloved-brand/)

生成摘要时出错

---

## 52. Show HN: DBOSify – Drop-in Temporal replacement built on Postgres

**原文标题**: Show HN: DBOSify – Drop-in Temporal replacement built on Postgres

**原文链接**: [https://github.com/dbos-inc/dbosify-py](https://github.com/dbos-inc/dbosify-py)

生成摘要时出错

---

## 53. A C++ implementation of a fast hash map and hash set using hopscotch hashing

**原文标题**: A C++ implementation of a fast hash map and hash set using hopscotch hashing

**原文链接**: [https://github.com/Tessil/hopscotch-map](https://github.com/Tessil/hopscotch-map)

生成摘要时出错

---

## 54. Pre-Modern Armies for Worldbuilders, Part III: Paying for It

**原文标题**: Pre-Modern Armies for Worldbuilders, Part III: Paying for It

**原文链接**: [https://acoup.blog/2026/06/26/collections-pre-modern-armies-for-worldbuilders-part-iii-paying-for-it/](https://acoup.blog/2026/06/26/collections-pre-modern-armies-for-worldbuilders-part-iii-paying-for-it/)

生成摘要时出错

---

## 55. Tuta: They are bringing back ChatControl

**原文标题**: Tuta: They are bringing back ChatControl

**原文链接**: [https://mastodon.social/@Tutanota/116815262001889776](https://mastodon.social/@Tutanota/116815262001889776)

生成摘要时出错

---

## 56. My Steam Machine is a 50ft HDMI cable

**原文标题**: My Steam Machine is a 50ft HDMI cable

**原文链接**: [https://blog.matthewbrunelle.com/my-steam-machine-is-a-50ft-hdmi-cable/](https://blog.matthewbrunelle.com/my-steam-machine-is-a-50ft-hdmi-cable/)

生成摘要时出错

---

## 57. An entire Herculaneum scroll has been read for the first time

**原文标题**: An entire Herculaneum scroll has been read for the first time

**原文链接**: [https://scrollprize.org/firstscroll](https://scrollprize.org/firstscroll)

生成摘要时出错

---

## 58. IBM MCGA Gate Array Reverse Engineering

**原文标题**: IBM MCGA Gate Array Reverse Engineering

**原文链接**: [https://github.com/schlae/IBM_MCGA](https://github.com/schlae/IBM_MCGA)

生成摘要时出错

---

## 59. Om Malik has died

**原文标题**: Om Malik has died

**原文链接**: [https://om.co/2026/06/24/1966-2026/](https://om.co/2026/06/24/1966-2026/)

生成摘要时出错

---

## 60. Text Files as a User Interface

**原文标题**: Text Files as a User Interface

**原文链接**: [https://ratfactor.com/cards/text-files-as-ui](https://ratfactor.com/cards/text-files-as-ui)

生成摘要时出错

---

## 61. A human postmortem of the 1996 AOL outage

**原文标题**: A human postmortem of the 1996 AOL outage

**原文链接**: [https://ngrok.com/blog/aol-was-down-1996](https://ngrok.com/blog/aol-was-down-1996)

生成摘要时出错

---

## 62. A Tiny Compiler for Data-Parallel Kernels

**原文标题**: A Tiny Compiler for Data-Parallel Kernels

**原文链接**: [https://healeycodes.com/a-tiny-compiler-for-data-parallel-kernels](https://healeycodes.com/a-tiny-compiler-for-data-parallel-kernels)

生成摘要时出错

---

## 63. Evan's Jujutsu Tutorial

**原文标题**: Evan's Jujutsu Tutorial

**原文链接**: [https://evmar.github.io/jjtut/](https://evmar.github.io/jjtut/)

生成摘要时出错

---

## 64. LaTeX.wasm: LaTeX Engines in Browsers

**原文标题**: LaTeX.wasm: LaTeX Engines in Browsers

**原文链接**: [https://www.swiftlatex.com/](https://www.swiftlatex.com/)

生成摘要时出错

---

## 65. Thousands more artists join Ireland's basic income plan

**原文标题**: Thousands more artists join Ireland's basic income plan

**原文链接**: [https://rgmii.org/blog/thousands-more-artists-join-irelands-basic-income-plan/](https://rgmii.org/blog/thousands-more-artists-join-irelands-basic-income-plan/)

生成摘要时出错

---

## 66. Making Sense of Proof by Contradiction [pdf]

**原文标题**: Making Sense of Proof by Contradiction [pdf]

**原文链接**: [https://www.foster77.co.uk/Foster,%20Scottish%20Mathematical%20Council%20Journal,%20Making%20sense%20of%20proof%20by%20contradiction.pdf](https://www.foster77.co.uk/Foster,%20Scottish%20Mathematical%20Council%20Journal,%20Making%20sense%20of%20proof%20by%20contradiction.pdf)

生成摘要时出错

---

## 67. The "Bizarre Headgear" exhibit at the Sam Noble museum

**原文标题**: The "Bizarre Headgear" exhibit at the Sam Noble museum

**原文链接**: [https://svpow.com/2026/05/15/the-bizarre-headgear-exhibit-at-the-sam-noble-museum-is-incredible/](https://svpow.com/2026/05/15/the-bizarre-headgear-exhibit-at-the-sam-noble-museum-is-incredible/)

生成摘要时出错

---

## 68. PlayStation Is Deleting 551 Movies from Customers' Accounts

**原文标题**: PlayStation Is Deleting 551 Movies from Customers' Accounts

**原文链接**: [https://kotaku.com/playstation-store-movies-digital-studio-canal-terminator-2000711013](https://kotaku.com/playstation-store-movies-digital-studio-canal-terminator-2000711013)

生成摘要时出错

---

## 69. SCC Technical Assistance Program

**原文标题**: SCC Technical Assistance Program

**原文链接**: [https://nerocam.com/scc_tap.asp](https://nerocam.com/scc_tap.asp)

生成摘要时出错

---

## 70. Bipartite Matching Is in NC

**原文标题**: Bipartite Matching Is in NC

**原文链接**: [https://scottaaronson.blog/?p=9851](https://scottaaronson.blog/?p=9851)

生成摘要时出错

---

## 71. Modern GPU Programming for MLSys

**原文标题**: Modern GPU Programming for MLSys

**原文链接**: [https://mlc.ai/modern-gpu-programming-for-mlsys/](https://mlc.ai/modern-gpu-programming-for-mlsys/)

生成摘要时出错

---

## 72. Anthropic says Alibaba used 25k accounts to mine Claude

**原文标题**: Anthropic says Alibaba used 25k accounts to mine Claude

**原文链接**: [https://arstechnica.com/tech-policy/2026/06/anthropic-claims-alibaba-defied-trump-to-attack-claude-and-steal-capabilities/](https://arstechnica.com/tech-policy/2026/06/anthropic-claims-alibaba-defied-trump-to-attack-claude-and-steal-capabilities/)

生成摘要时出错

---

## 73. Gossamer: a Rust-flavoured language with real goroutines and pause-free memory

**原文标题**: Gossamer: a Rust-flavoured language with real goroutines and pause-free memory

**原文链接**: [https://gossamer-lang.org/](https://gossamer-lang.org/)

生成摘要时出错

---

## 74. An "infovore" shares his chats

**原文标题**: An "infovore" shares his chats

**原文链接**: [https://chatgptpro.substack.com/p/tyler-cowen](https://chatgptpro.substack.com/p/tyler-cowen)

生成摘要时出错

---

## 75. OpenAI leans toward waiting until next year for IPO

**原文标题**: OpenAI leans toward waiting until next year for IPO

**原文链接**: [https://www.nytimes.com/2026/06/25/technology/openai-ipo-artificial-intelligence.html](https://www.nytimes.com/2026/06/25/technology/openai-ipo-artificial-intelligence.html)

生成摘要时出错

---

## 76. Show HN: WebBase-III – dBASE III rebuilt in the browser with its own interpreter

**原文标题**: Show HN: WebBase-III – dBASE III rebuilt in the browser with its own interpreter

**原文链接**: [https://github.com/DDecoene/WebBaseIII](https://github.com/DDecoene/WebBaseIII)

生成摘要时出错

---

## 77. AgentKits – 60 production-ready AI agent blueprints with guardrails

**原文标题**: AgentKits – 60 production-ready AI agent blueprints with guardrails

**原文链接**: [https://www.agent-kits.com](https://www.agent-kits.com)

生成摘要时出错

---

## 78. Show HN: Autofit2 – End-to-end pipeline for multilingual text classification

**原文标题**: Show HN: Autofit2 – End-to-end pipeline for multilingual text classification

**原文链接**: [https://github.com/neospe/autofit2](https://github.com/neospe/autofit2)

生成摘要时出错

---

## 79. The unbearable cheapness of open weight models

**原文标题**: The unbearable cheapness of open weight models

**原文链接**: [https://jamesoclaire.com/2026/06/25/the-unbearable-cheapness-of-open-weight-models/](https://jamesoclaire.com/2026/06/25/the-unbearable-cheapness-of-open-weight-models/)

生成摘要时出错

---

## 80. Show HN: The TypeScript Semantic Layer for ClickHouse

**原文标题**: Show HN: The TypeScript Semantic Layer for ClickHouse

**原文链接**: [https://github.com/hypequery/hypequery](https://github.com/hypequery/hypequery)

生成摘要时出错

---

## 81. We all depend on open source. We will defend it together

**原文标题**: We all depend on open source. We will defend it together

**原文链接**: [https://akrites.org/letter/](https://akrites.org/letter/)

生成摘要时出错

---

## 82. Perry – compiles TypeScript to native GUI and CLI apps. No runtime / Electron

**原文标题**: Perry – compiles TypeScript to native GUI and CLI apps. No runtime / Electron

**原文链接**: [https://perryts.com](https://perryts.com)

生成摘要时出错

---

## 83. What happened after 2k people tried to hack my AI assistant

**原文标题**: What happened after 2k people tried to hack my AI assistant

**原文链接**: [https://www.fernandoi.cl/posts/hackmyclaw/](https://www.fernandoi.cl/posts/hackmyclaw/)

生成摘要时出错

---

## 84. Framework's 10G Ethernet module exposes USB-C's complexity

**原文标题**: Framework's 10G Ethernet module exposes USB-C's complexity

**原文链接**: [https://www.jeffgeerling.com/blog/2026/framework-10g-ethernet-module-usb-c-complexity/](https://www.jeffgeerling.com/blog/2026/framework-10g-ethernet-module-usb-c-complexity/)

生成摘要时出错

---

## 85. Incident CVE-2026-LGTM

**原文标题**: Incident CVE-2026-LGTM

**原文链接**: [https://nesbitt.io/2026/06/26/incident-report-cve-2026-lgtm.html](https://nesbitt.io/2026/06/26/incident-report-cve-2026-lgtm.html)

生成摘要时出错

---

## 86. Tmux 3.7 Terminal Multiplexer Released with Initial Floating Pane Support

**原文标题**: Tmux 3.7 Terminal Multiplexer Released with Initial Floating Pane Support

**原文链接**: [https://linuxiac.com/tmux-3-7-terminal-multiplexer-released-with-initial-floating-pane-support/](https://linuxiac.com/tmux-3-7-terminal-multiplexer-released-with-initial-floating-pane-support/)

生成摘要时出错

---

## 87. Libre Barcode Project

**原文标题**: Libre Barcode Project

**原文链接**: [https://graphicore.github.io/librebarcode/](https://graphicore.github.io/librebarcode/)

生成摘要时出错

---

## 88. Jolla Phone (October 2026)

**原文标题**: Jolla Phone (October 2026)

**原文链接**: [https://commerce.jolla.com/products/jolla-phone-october-2026](https://commerce.jolla.com/products/jolla-phone-october-2026)

生成摘要时出错

---

## 89. Springer Nature has removed two studies by Max Planck

**原文标题**: Springer Nature has removed two studies by Max Planck

**原文链接**: [https://www.science.org/content/article/why-have-papers-one-history-s-most-famous-physicists-been-retracted](https://www.science.org/content/article/why-have-papers-one-history-s-most-famous-physicists-been-retracted)

生成摘要时出错

---

## 90. Primed for Malware: Stop Selling Compromised Android Devices

**原文标题**: Primed for Malware: Stop Selling Compromised Android Devices

**原文链接**: [https://www.eff.org/deeplinks/2026/06/primed-malware-stop-selling-compromised-android-devices](https://www.eff.org/deeplinks/2026/06/primed-malware-stop-selling-compromised-android-devices)

生成摘要时出错

---

