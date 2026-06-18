# Hacker News 热门文章摘要 (2026-06-18)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 我发现了1万个分发木马程序的GitHub仓库。

**原文标题**: I found 10k GitHub repositories distributing Trojan malware

**原文链接**: [https://orchidfiles.com/github-repositories-distributing-malware/](https://orchidfiles.com/github-repositories-distributing-malware/)

在本文中，一位研究人员详细揭示了一场涉及约 10,000 个分发木马程序的 GitHub 仓库的大规模恶意软件活动。该活动采用了一种复杂的欺骗技术：攻击者克隆合法的仓库——包括其完整的提交历史和贡献者名单——以此建立信任并绕过安全算法。

**恶意模式**
攻击者的策略是在仓库的 `README.md` 文件中嵌入指向恶意 ZIP 压缩包的链接。为了在搜索结果中保持靠前排名并规避检测，攻击者会定期删除并重新推送相同的提交（标题通常为“Update README.md”）。这些 ZIP 文件通常包含一个命令启动器（`.cmd`）、一个重命名的可执行文件、一个 DLL 和一个数据文件。尽管压缩包的 URL 在 VirusTotal 上通常显示为零检出，但其内部文件会被标记为木马（与 SmartLoader 或 StealC 等恶意软件相关）。

**发现过程与研究方法**
作者在发现自己项目的未经授权副本被搜索引擎索引后，察觉到了这一趋势。为了确定该活动的规模，研究人员利用 `gharchive` 分析了五天内的 1,600 万次提交推送。通过筛选特定模式——例如每天更新 1 至 24 次、使用通用的提交信息以及特定的文件结构——他们识别出了 10,000 个恶意仓库。

**结论与影响**
研究人员指出，攻击者利用新仓库和热门标签进行搜索引擎优化（SEO），使其在特定的小众搜索词结果中名列前茅。在这些研究结果以及名为“Git Malware Finder”的检测工具发布后，GitHub 开始大规模清理被识别的账号。作者总结认为，虽然 GitHub 的自动化系统在数月内都未能发现这些仓库，但该模式通过行为分析是极易识别的。

---

## 2. 瑞士议会解除新建核电站禁令

**原文标题**: Swiss parliament lifts ban on new nuclear power plants

**原文链接**: [https://www.bluewin.ch/en/news/switzerland/parliament-lifts-ban-on-new-nuclear-power-plants-3257535.html](https://www.bluewin.ch/en/news/switzerland/parliament-lifts-ban-on-new-nuclear-power-plants-3257535.html)

生成摘要时出错

---

## 3. Migrating from GNU Stow to Chezmoi

**原文标题**: Migrating from GNU Stow to Chezmoi

**原文链接**: [https://rednafi.com/misc/chezmoi/](https://rednafi.com/misc/chezmoi/)

生成摘要时出错

---

## 4. Hospitals and universities repurposing drugs at 90% lower cost

**原文标题**: Hospitals and universities repurposing drugs at 90% lower cost

**原文链接**: [https://www.kcl.ac.uk/news/hospitals-and-universities-repurposing-drugs-at-90-lower-cost](https://www.kcl.ac.uk/news/hospitals-and-universities-repurposing-drugs-at-90-lower-cost)

生成摘要时出错

---

## 5. Launch HN: TesterArmy (YC P26) – Agents that test web and mobile apps

**原文标题**: Launch HN: TesterArmy (YC P26) – Agents that test web and mobile apps

**原文链接**: [https://tester.army](https://tester.army)

生成摘要时出错

---

## 6. The Harajuku Moment

**原文标题**: The Harajuku Moment

**原文链接**: [https://tim.blog/2024/02/09/harajuku-moment/](https://tim.blog/2024/02/09/harajuku-moment/)

生成摘要时出错

---

## 7. Advanced Compilers: The Self-Guided Online Course

**原文标题**: Advanced Compilers: The Self-Guided Online Course

**原文链接**: [https://www.cs.cornell.edu/courses/cs6120/2025fa/self-guided/](https://www.cs.cornell.edu/courses/cs6120/2025fa/self-guided/)

生成摘要时出错

---

## 8. The founder of Craigslist has given away half a billion dollars

**原文标题**: The founder of Craigslist has given away half a billion dollars

**原文链接**: [https://www.independent.co.uk/us/money/craigslist-multimillionaire-craig-newmark-b2980681.html](https://www.independent.co.uk/us/money/craigslist-multimillionaire-craig-newmark-b2980681.html)

生成摘要时出错

---

## 9. TerraPower in Deal with Meta for Eight Natrium 345 MW Advanced Nuclear Plants

**原文标题**: TerraPower in Deal with Meta for Eight Natrium 345 MW Advanced Nuclear Plants

**原文链接**: [https://neutronbytes.com/2026/01/09/terrapower-in-mega-deal-with-meta-for-eight-natrium-345-mw-advanced-nuclear-plants/](https://neutronbytes.com/2026/01/09/terrapower-in-mega-deal-with-meta-for-eight-natrium-345-mw-advanced-nuclear-plants/)

生成摘要时出错

---

## 10. Modos Color Monitor Pushes E-Paper Displays Further

**原文标题**: Modos Color Monitor Pushes E-Paper Displays Further

**原文链接**: [https://spectrum.ieee.org/modos-e-paper-monitor](https://spectrum.ieee.org/modos-e-paper-monitor)

生成摘要时出错

---

## 11. A website that lists websites to submit your website to

**原文标题**: A website that lists websites to submit your website to

**原文链接**: [https://www.submission.directory/](https://www.submission.directory/)

生成摘要时出错

---

## 12. Agentic Resource Discovery Specification

**原文标题**: Agentic Resource Discovery Specification

**原文链接**: [https://agenticresourcediscovery.org/introduction/](https://agenticresourcediscovery.org/introduction/)

生成摘要时出错

---

## 13. Emacs, how it all started (for me)

**原文标题**: Emacs, how it all started (for me)

**原文链接**: [https://xvw.lol/en/articles/emacs-start.html](https://xvw.lol/en/articles/emacs-start.html)

生成摘要时出错

---

## 14. Show HN: Gerrymandle - Daily puzzle game where you redraw electoral districts

**原文标题**: Show HN: Gerrymandle - Daily puzzle game where you redraw electoral districts

**原文链接**: [https://gerrymandle.cc/](https://gerrymandle.cc/)

生成摘要时出错

---

## 15. Emacs 31 is around the corner: The changes I'm daily driving

**原文标题**: Emacs 31 is around the corner: The changes I'm daily driving

**原文链接**: [https://www.rahuljuliato.com/posts/emacs-31-around-the-corner](https://www.rahuljuliato.com/posts/emacs-31-around-the-corner)

生成摘要时出错

---

## 16. DeepSeek Introduces Vision

**原文标题**: DeepSeek Introduces Vision

**原文链接**: [https://chat.deepseek.com/](https://chat.deepseek.com/)

生成摘要时出错

---

## 17. The Korean telecom giant at the center of Anthropic's Mythos controversy

**原文标题**: The Korean telecom giant at the center of Anthropic's Mythos controversy

**原文链接**: [https://www.wired.com/story/sk-telecom-anthropic-mythos-export-controls/](https://www.wired.com/story/sk-telecom-anthropic-mythos-export-controls/)

生成摘要时出错

---

## 18. The Token Compression Illusion: Why I'm Skeptical of RTK

**原文标题**: The Token Compression Illusion: Why I'm Skeptical of RTK

**原文链接**: [https://mroczek.dev/articles/the-token-compression-illusion-why-im-skeptical-of-rtk/](https://mroczek.dev/articles/the-token-compression-illusion-why-im-skeptical-of-rtk/)

生成摘要时出错

---

## 19. Has W Social switched to closed source?

**原文标题**: Has W Social switched to closed source?

**原文链接**: [https://blog.elenarossini.com/w-social-public-institutions-and-the-theater-of-european-digital-sovereignty/](https://blog.elenarossini.com/w-social-public-institutions-and-the-theater-of-european-digital-sovereignty/)

生成摘要时出错

---

## 20. My LSM tree was slower than a B-tree. Then I profiled it

**原文标题**: My LSM tree was slower than a B-tree. Then I profiled it

**原文链接**: [https://aasheesh.vercel.app/blog/lsm-tree](https://aasheesh.vercel.app/blog/lsm-tree)

生成摘要时出错

---

## 21. .gitignore Isn't the Only Way to Ignore Files in Git

**原文标题**: .gitignore Isn't the Only Way to Ignore Files in Git

**原文链接**: [https://nelson.cloud/.gitignore-isnt-the-only-way-to-ignore-files-in-git/](https://nelson.cloud/.gitignore-isnt-the-only-way-to-ignore-files-in-git/)

生成摘要时出错

---

## 22. How Alberta Eradicated Rats

**原文标题**: How Alberta Eradicated Rats

**原文链接**: [https://worksinprogress.co/issue/albertas-war-on-rats/](https://worksinprogress.co/issue/albertas-war-on-rats/)

生成摘要时出错

---

## 23. Local Qwen isn't a worse Opus, it's a different tool

**原文标题**: Local Qwen isn't a worse Opus, it's a different tool

**原文链接**: [https://blog.alexellis.io/local-ai-is-not-opus/](https://blog.alexellis.io/local-ai-is-not-opus/)

生成摘要时出错

---

## 24. Microsoft new Outlook takes 10 seconds to do what Outlook Classic does instantly

**原文标题**: Microsoft new Outlook takes 10 seconds to do what Outlook Classic does instantly

**原文链接**: [https://www.windowslatest.com/2026/06/15/microsofts-new-outlook-takes-10-seconds-to-do-what-outlook-classic-does-instantly-on-windows/](https://www.windowslatest.com/2026/06/15/microsofts-new-outlook-takes-10-seconds-to-do-what-outlook-classic-does-instantly-on-windows/)

生成摘要时出错

---

## 25. We built a persistent agent memory layer on Elasticsearch with 0.89 recall

**原文标题**: We built a persistent agent memory layer on Elasticsearch with 0.89 recall

**原文链接**: [https://www.elastic.co/search-labs/blog/agent-memory-elasticsearch](https://www.elastic.co/search-labs/blog/agent-memory-elasticsearch)

生成摘要时出错

---

## 26. Midjourney Medical

**原文标题**: Midjourney Medical

**原文链接**: [https://www.midjourney.com/medical/blogpost](https://www.midjourney.com/medical/blogpost)

生成摘要时出错

---

## 27. I need your clothes, your boots, and your motorcycle

**原文标题**: I need your clothes, your boots, and your motorcycle

**原文链接**: [https://rbelmont.mameworld.info/?p=1725](https://rbelmont.mameworld.info/?p=1725)

生成摘要时出错

---

## 28. Ubiquiti: Enterprise NAS, Built on ZFS

**原文标题**: Ubiquiti: Enterprise NAS, Built on ZFS

**原文链接**: [https://blog.ui.com/article/introducing-enterprise-nas](https://blog.ui.com/article/introducing-enterprise-nas)

生成摘要时出错

---

## 29. Vinyl Cache and Varnish Cache

**原文标题**: Vinyl Cache and Varnish Cache

**原文链接**: [https://vinyl-cache.org/organization/on_vinyl_cache_and_varnish_cache.html#org-vinyl-varnish](https://vinyl-cache.org/organization/on_vinyl_cache_and_varnish_cache.html#org-vinyl-varnish)

生成摘要时出错

---

## 30. Migrate from OpenClaw

**原文标题**: Migrate from OpenClaw

**原文链接**: [https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw)

生成摘要时出错

---

## 31. Unity vs. Floating Point

**原文标题**: Unity vs. Floating Point

**原文链接**: [https://aras-p.info/blog/2026/06/11/Unity-vs-floating-point/](https://aras-p.info/blog/2026/06/11/Unity-vs-floating-point/)

生成摘要时出错

---

## 32. Seven Perfect Shuffles Randomize a Deck of Cards. But How Many Sloppy Ones?

**原文标题**: Seven Perfect Shuffles Randomize a Deck of Cards. But How Many Sloppy Ones?

**原文链接**: [https://www.quantamagazine.org/seven-perfect-shuffles-randomize-a-deck-of-cards-but-how-many-sloppy-ones-20260617/](https://www.quantamagazine.org/seven-perfect-shuffles-randomize-a-deck-of-cards-but-how-many-sloppy-ones-20260617/)

生成摘要时出错

---

## 33. Image Toolbox (T8RIN)

**原文标题**: Image Toolbox (T8RIN)

**原文链接**: [https://github.com/T8RIN/ImageToolbox/](https://github.com/T8RIN/ImageToolbox/)

生成摘要时出错

---

## 34. The feedback loops behind Kubernetes

**原文标题**: The feedback loops behind Kubernetes

**原文链接**: [https://planetscale.com/blog/the-feedback-loops-behind-kubernetes](https://planetscale.com/blog/the-feedback-loops-behind-kubernetes)

生成摘要时出错

---

## 35. AMD silently removes memory encryption from consumer Ryzen CPUs

**原文标题**: AMD silently removes memory encryption from consumer Ryzen CPUs

**原文链接**: [https://www.tomshardware.com/pc-components/cpus/amd-silently-removes-memory-encryption-from-consumer-ryzen-cpus-leaving-users-unaware-that-they-may-be-vulnerable-security-feature-vanishes-after-newer-agesa-firmware-amd-engineers-go-radio-silent-when-pressed-about-the-change](https://www.tomshardware.com/pc-components/cpus/amd-silently-removes-memory-encryption-from-consumer-ryzen-cpus-leaving-users-unaware-that-they-may-be-vulnerable-security-feature-vanishes-after-newer-agesa-firmware-amd-engineers-go-radio-silent-when-pressed-about-the-change)

生成摘要时出错

---

## 36. AI Regulation Should Be Rational, Not Retaliatory

**原文标题**: AI Regulation Should Be Rational, Not Retaliatory

**原文链接**: [https://www.eff.org/deeplinks/2026/06/ai-regulation-should-be-rational-not-retaliatory](https://www.eff.org/deeplinks/2026/06/ai-regulation-should-be-rational-not-retaliatory)

生成摘要时出错

---

## 37. Tons of Loctite adhesive used in Sagrada Familia's central towers

**原文标题**: Tons of Loctite adhesive used in Sagrada Familia's central towers

**原文链接**: [https://www.henkel.com/press-and-media/press-releases-and-kits/2026-06-17-henkel-technology-supports-completion-of-the-sagrada-familia-s-central-towers-2171148](https://www.henkel.com/press-and-media/press-releases-and-kits/2026-06-17-henkel-technology-supports-completion-of-the-sagrada-familia-s-central-towers-2171148)

生成摘要时出错

---

## 38. I hate compilers

**原文标题**: I hate compilers

**原文链接**: [https://xeiaso.net/notes/2026/anubis-wasm-vendor-binary/](https://xeiaso.net/notes/2026/anubis-wasm-vendor-binary/)

生成摘要时出错

---

## 39. Lore – Open source version control system designed for scalability

**原文标题**: Lore – Open source version control system designed for scalability

**原文链接**: [https://lore.org/](https://lore.org/)

生成摘要时出错

---

## 40. Sogen – High-performance Windows and Linux userspace emulator

**原文标题**: Sogen – High-performance Windows and Linux userspace emulator

**原文链接**: [https://sogen.dev/](https://sogen.dev/)

生成摘要时出错

---

## 41. How Madrid built its metro cheaply (2024)

**原文标题**: How Madrid built its metro cheaply (2024)

**原文链接**: [https://worksinprogress.co/issue/how-madrid-built-its-metro-cheaply/](https://worksinprogress.co/issue/how-madrid-built-its-metro-cheaply/)

生成摘要时出错

---

## 42. Trellis AI (YC W24)  hiring a product lead to build agents for healthcare access

**原文标题**: Trellis AI (YC W24)  hiring a product lead to build agents for healthcare access

**原文链接**: [https://www.ycombinator.com/companies/trellis-ai/jobs/Cg94htp-product-lead](https://www.ycombinator.com/companies/trellis-ai/jobs/Cg94htp-product-lead)

生成摘要时出错

---

## 43. Notes from Tired Egyptian Whose Job Is Explaining That Humans Built the Pyramids

**原文标题**: Notes from Tired Egyptian Whose Job Is Explaining That Humans Built the Pyramids

**原文链接**: [https://www.mcsweeneys.net/articles/notes-from-a-tired-egyptian-guy-whose-job-is-explaining-that-humans-built-the-pyramids](https://www.mcsweeneys.net/articles/notes-from-a-tired-egyptian-guy-whose-job-is-explaining-that-humans-built-the-pyramids)

生成摘要时出错

---

## 44. Ozempic and Wegovy linked to surprising drop in violent behavior

**原文标题**: Ozempic and Wegovy linked to surprising drop in violent behavior

**原文链接**: [https://www.sciencedaily.com/releases/2026/06/260617032152.htm](https://www.sciencedaily.com/releases/2026/06/260617032152.htm)

生成摘要时出错

---

## 45. Taxonomy of the Occlupanida (parasitoids on bread bag tags)

**原文标题**: Taxonomy of the Occlupanida (parasitoids on bread bag tags)

**原文链接**: [https://www.horg.com/horg/?page_id=921](https://www.horg.com/horg/?page_id=921)

生成摘要时出错

---

## 46. Launch HN: Adam (YC W25) – Open-Source AI CAD

**原文标题**: Launch HN: Adam (YC W25) – Open-Source AI CAD

**原文链接**: [https://github.com/Adam-CAD/CADAM](https://github.com/Adam-CAD/CADAM)

生成摘要时出错

---

## 47. US Supreme Court limits ban on gun ownership by marijuana users

**原文标题**: US Supreme Court limits ban on gun ownership by marijuana users

**原文链接**: [https://www.reuters.com/world/us/us-supreme-court-backs-challenge-ban-gun-ownership-by-drug-users-2026-06-18/](https://www.reuters.com/world/us/us-supreme-court-backs-challenge-ban-gun-ownership-by-drug-users-2026-06-18/)

生成摘要时出错

---

## 48. The forge we deserve

**原文标题**: The forge we deserve

**原文链接**: [https://btao.org/posts/2026-05-09-the-forge-we-deserve/](https://btao.org/posts/2026-05-09-the-forge-we-deserve/)

生成摘要时出错

---

## 49. TypeScript 7.0 RC

**原文标题**: TypeScript 7.0 RC

**原文链接**: [https://devblogs.microsoft.com/typescript/announcing-typescript-7-0-rc/](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0-rc/)

生成摘要时出错

---

## 50. Smashed Toilet Phone Web Server

**原文标题**: Smashed Toilet Phone Web Server

**原文链接**: [https://www.offthebricks.com/articles/smashed-toilet-phone-web-server](https://www.offthebricks.com/articles/smashed-toilet-phone-web-server)

生成摘要时出错

---

## 51. The AI Hate Progression

**原文标题**: The AI Hate Progression

**原文链接**: [https://www.xodium.net/2026/06/the-ai-hate-progression.html](https://www.xodium.net/2026/06/the-ai-hate-progression.html)

生成摘要时出错

---

## 52. US holds off blacklisting DeepSeek, more than 100 firms deemed security risks

**原文标题**: US holds off blacklisting DeepSeek, more than 100 firms deemed security risks

**原文链接**: [https://www.reuters.com/world/china/us-holds-off-blacklisting-chinas-deepseek-more-than-100-firms-deemed-security-2026-06-17/](https://www.reuters.com/world/china/us-holds-off-blacklisting-chinas-deepseek-more-than-100-firms-deemed-security-2026-06-17/)

生成摘要时出错

---

## 53. About ASCII art and Jgs font (2023)

**原文标题**: About ASCII art and Jgs font (2023)

**原文链接**: [https://velvetyne.fr/news/about-ascii-art-and-jgs-font/](https://velvetyne.fr/news/about-ascii-art-and-jgs-font/)

生成摘要时出错

---

## 54. Show HN: An 8-bit live gamecast for baseball

**原文标题**: Show HN: An 8-bit live gamecast for baseball

**原文链接**: [https://ribbie.tv/watch](https://ribbie.tv/watch)

生成摘要时出错

---

## 55. The hacker sent by Anthropic to calm the government's nerves about AI safety

**原文标题**: The hacker sent by Anthropic to calm the government's nerves about AI safety

**原文链接**: [https://www.wsj.com/tech/ai/anthropic-mythos-safety-nicholas-carlini-20bceaa3](https://www.wsj.com/tech/ai/anthropic-mythos-safety-nicholas-carlini-20bceaa3)

生成摘要时出错

---

## 56. Storied Colors – A catalogue of named colors

**原文标题**: Storied Colors – A catalogue of named colors

**原文链接**: [https://storiedcolors.com/](https://storiedcolors.com/)

生成摘要时出错

---

## 57. Subterranean fungi networks more than 100 quadrillion km in length

**原文标题**: Subterranean fungi networks more than 100 quadrillion km in length

**原文链接**: [https://www.theguardian.com/science/2026/jun/11/arbuscular-mycorrhizal-fungi-plant-life-climate-global-mapping-study](https://www.theguardian.com/science/2026/jun/11/arbuscular-mycorrhizal-fungi-plant-life-climate-global-mapping-study)

生成摘要时出错

---

## 58. RFC 10008: The new HTTP Query Method

**原文标题**: RFC 10008: The new HTTP Query Method

**原文链接**: [https://www.rfc-editor.org/info/rfc10008/](https://www.rfc-editor.org/info/rfc10008/)

生成摘要时出错

---

## 59. SpaceX to buy Cursor for $60B

**原文标题**: SpaceX to buy Cursor for $60B

**原文链接**: [https://www.reuters.com/legal/transactional/spacex-buy-anysphere-60-billion-2026-06-16/](https://www.reuters.com/legal/transactional/spacex-buy-anysphere-60-billion-2026-06-16/)

生成摘要时出错

---

## 60. Drowning Doesn't Look Like Drowning (2021)

**原文标题**: Drowning Doesn't Look Like Drowning (2021)

**原文链接**: [https://gcaptain.com/drowning/](https://gcaptain.com/drowning/)

生成摘要时出错

---

## 61. Don't Stack Weaknesses

**原文标题**: Don't Stack Weaknesses

**原文链接**: [https://staysaasy.com/startups/2026/06/16/stacked-weaknesses.html](https://staysaasy.com/startups/2026/06/16/stacked-weaknesses.html)

生成摘要时出错

---

## 62. Abandoned and Little-Known Airfields

**原文标题**: Abandoned and Little-Known Airfields

**原文链接**: [https://airfields-freeman.com/](https://airfields-freeman.com/)

生成摘要时出错

---

## 63. New Super Pac Aims to Rally Tech Workers to Help Limit A.I

**原文标题**: New Super Pac Aims to Rally Tech Workers to Help Limit A.I

**原文链接**: [https://www.nytimes.com/2026/06/18/technology/ai-super-pac-guardrails-alliance.html](https://www.nytimes.com/2026/06/18/technology/ai-super-pac-guardrails-alliance.html)

生成摘要时出错

---

## 64. US Supreme Court drug users cannot be prohibited from firearms [pdf]

**原文标题**: US Supreme Court drug users cannot be prohibited from firearms [pdf]

**原文链接**: [https://www.supremecourt.gov/opinions/25pdf/24-1234_g2bh.pdf](https://www.supremecourt.gov/opinions/25pdf/24-1234_g2bh.pdf)

生成摘要时出错

---

## 65. Why thinking out loud with someone beats thinking alone

**原文标题**: Why thinking out loud with someone beats thinking alone

**原文链接**: [https://www.thesignalist.io/s/the-dialogue-dividend/](https://www.thesignalist.io/s/the-dialogue-dividend/)

生成摘要时出错

---

## 66. Show HN: Spin Lab

**原文标题**: Show HN: Spin Lab

**原文链接**: [https://srijanshukla.com/artifacts/spin-lab/](https://srijanshukla.com/artifacts/spin-lab/)

生成摘要时出错

---

## 67. Map Clustering Is Not My Favorite

**原文标题**: Map Clustering Is Not My Favorite

**原文链接**: [https://blog.greg.technology/2026/06/12/map-clustering-is-not-my-favorite.html](https://blog.greg.technology/2026/06/12/map-clustering-is-not-my-favorite.html)

生成摘要时出错

---

## 68. GLM 5.2 Performance Benchmarks

**原文标题**: GLM 5.2 Performance Benchmarks

**原文链接**: [https://artificialanalysis.ai/models/glm-5-2](https://artificialanalysis.ai/models/glm-5-2)

生成摘要时出错

---

## 69. Loreline – Tools for writing interactive fiction

**原文标题**: Loreline – Tools for writing interactive fiction

**原文链接**: [https://loreline.app/en/](https://loreline.app/en/)

生成摘要时出错

---

## 70. Can you see three trees?

**原文标题**: Can you see three trees?

**原文链接**: [https://www.not-ship.com/can-you-see-three-trees/](https://www.not-ship.com/can-you-see-three-trees/)

生成摘要时出错

---

## 71. AI demands more engineering discipline. Not less

**原文标题**: AI demands more engineering discipline. Not less

**原文链接**: [https://charitydotwtf.substack.com/p/ai-demands-more-engineering-discipline](https://charitydotwtf.substack.com/p/ai-demands-more-engineering-discipline)

生成摘要时出错

---

## 72. Show HN: High-Res Neural Cellular Automata

**原文标题**: Show HN: High-Res Neural Cellular Automata

**原文链接**: [https://cells2pixels.github.io/](https://cells2pixels.github.io/)

生成摘要时出错

---

## 73. Language Courses in the Public Domain

**原文标题**: Language Courses in the Public Domain

**原文链接**: [https://fsi-languages.yojik.eu/](https://fsi-languages.yojik.eu/)

生成摘要时出错

---

## 74. Hacker News but for independent blogs

**原文标题**: Hacker News but for independent blogs

**原文链接**: [https://bubbles.town/](https://bubbles.town/)

生成摘要时出错

---

## 75. Show HN: Capacitor Alarm Clock

**原文标题**: Show HN: Capacitor Alarm Clock

**原文链接**: [https://github.com/ArcaEge/capacitor-alarm-clock](https://github.com/ArcaEge/capacitor-alarm-clock)

生成摘要时出错

---

## 76. The Return of Rigorous Full-System Timing Simulation

**原文标题**: The Return of Rigorous Full-System Timing Simulation

**原文链接**: [https://www.sigarch.org/the-return-of-rigorous-full-system-timing-simulation/](https://www.sigarch.org/the-return-of-rigorous-full-system-timing-simulation/)

生成摘要时出错

---

## 77. Volkswagen started blocking GrapheneOS users

**原文标题**: Volkswagen started blocking GrapheneOS users

**原文链接**: [https://discuss.grapheneos.org/d/35949-volkswagen-app?page=3](https://discuss.grapheneos.org/d/35949-volkswagen-app?page=3)

生成摘要时出错

---

## 78. ACLU: Do Automatic License Plate Readers violate privacy under the 4th Amendment

**原文标题**: ACLU: Do Automatic License Plate Readers violate privacy under the 4th Amendment

**原文链接**: [https://www.aclu.org/cases/schmidt-v-norfolk](https://www.aclu.org/cases/schmidt-v-norfolk)

生成摘要时出错

---

## 79. Kirkland Roundabouts

**原文标题**: Kirkland Roundabouts

**原文链接**: [https://kirklandroundabouts.com](https://kirklandroundabouts.com)

生成摘要时出错

---

## 80. Made a free macOS menu bar app that fixes typing in the wrong keyboard layout

**原文标题**: Made a free macOS menu bar app that fixes typing in the wrong keyboard layout

**原文链接**: [https://flickey.site](https://flickey.site)

生成摘要时出错

---

## 81. Dwarf Fortress in the Browser

**原文标题**: Dwarf Fortress in the Browser

**原文链接**: [https://github.com/Sessa93/remote-df](https://github.com/Sessa93/remote-df)

生成摘要时出错

---

## 82. Show HN: Inkwash, a watercolor sketching app and explanation

**原文标题**: Show HN: Inkwash, a watercolor sketching app and explanation

**原文链接**: [https://johnowhitaker.github.io/inkwash/about](https://johnowhitaker.github.io/inkwash/about)

生成摘要时出错

---

## 83. Windows 93

**原文标题**: Windows 93

**原文链接**: [http://windows93.net/](http://windows93.net/)

生成摘要时出错

---

## 84. MicroUI – A tiny, portable, immediate-mode UI library written in ANSI C

**原文标题**: MicroUI – A tiny, portable, immediate-mode UI library written in ANSI C

**原文链接**: [https://github.com/rxi/microui](https://github.com/rxi/microui)

生成摘要时出错

---

