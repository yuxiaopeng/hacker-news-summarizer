# Hacker News 热门文章摘要 (2026-05-26)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 停止在提交记录中打广告

**原文标题**: Stop Advertising in Your Commits

**原文链接**: [https://akselmo.dev/posts/stop-advertising-in-your-commits/](https://akselmo.dev/posts/stop-advertising-in-your-commits/)

在《停止在提交信息中打广告》一文中，Akselmo 反对在 Git 提交信息中包含不必要的元数据、签名以及特定工具的品牌标识。作者主张提交日志应当保持整洁、专注，并仅致力于解释代码变更的“内容”和“原因”。

文章的主要观点包括：

*   **冗余元数据：** 作者批评了添加如 “Signed-off-by” 或 “Reported-by” 等签名的习惯，除非项目法律或贡献指南（如 Linux 内核）有严格要求。由于 Git 已在其内部标头中存储了作者和提交者信息，在正文中重复这些内容会产生视觉噪音。
*   **工具广告：** 作者主要不满的是类似于 “Sent from my iPhone” 或由 IDE 和 Git 客户端自动生成的签名。这些签名充当了软件的免费广告，对于阅读项目历史的开发者来说毫无价值。
*   **凌乱与可读性：** 当 `git log` 充斥着多行签名和特定工具的标签时，开发者更难浏览历史记录并理解变更背后的实际逻辑。作者强调，提交信息是为人服务的，而非为了满足工具或开发者的虚荣心。
*   **聚焦内容：** 作者最后指出，开发者应当剥离“废话”，保持信息的专业性。一份优秀的提交信息应当是技术变更的简洁概括，不应受到开发者硬件或软件选择的干扰。

总的来说，这篇文章呼吁一种“极简主义”的提交信息，将清晰度和长期可维护性置于不必要的格式和签名之上。

---

## 2. TIGIT之歌

**原文标题**: The Ballad of TIGIT

**原文链接**: [https://www.owlposting.com/p/the-ballad-of-tigit](https://www.owlposting.com/p/the-ballad-of-tigit)

《TIGIT之歌》记录了TIGIT靶向药物的崛起与惨痛失败。这类药物曾被誉为重磅免疫疗法Keytruda（可瑞达）的潜在继任者。TIGIT在理论上被认为是一种强效的“免疫刹车”；研究人员相信，通过阻断TIGIT，可以同时释放免疫系统的“刹车”并激活“加速器”，从而激发更卓越的抗癌反应。

在罗氏公司tiragolumab极具前景的早期2期临床数据推动下，价值数十亿美元的行业“羊群效应”随之出现。包括默沙东、GSK、吉利德和诺华在内的主要制药巨头纷纷涌入开发，累计在临床试验中招募了近49,000名患者。罗氏凭借其庞大的“SKYSCRAPER”项目一马当先，该项目包含一系列旨在确立市场主导地位的并行3期试验。

然而，临床结果证明是灾难性的。从2022年开始，罗氏的旗舰试验接连未能达到目标。最令人震惊的是，部分数据表明某些TIGIT联合疗法甚至“适得其反”，患者的死亡速度比对照组更快。截至2025年底，包括Arcus和吉利德的“Fc静默”抗体假说在内的其他替代方案也均在3期试验中宣告失败。

到2026年，TIGIT类药物在投资者和研究人员眼中已变得如同“放射性物质”般令人避之不及。罗氏、默沙东和GSK的主要项目纷纷终止，多家生物技术公司的合作关系也随之破裂。尽管投入了超过30亿美元的资金和长达十年的研究，TIGIT假说仍未能实现临床突破。这段往事已成为制药行业盲目从众的警示录：全行业的集体狂热，最终导致了现代肿瘤学领域耗资最巨、最受瞩目的失败之一。

---

## 3. 几款有趣的现代像素字体

**原文标题**: A few interesting modern pixel fonts

**原文链接**: [https://unsung.aresluna.org/a-few-interesting-modern-pixel-fonts/](https://unsung.aresluna.org/a-few-interesting-modern-pixel-fonts/)

本文探讨了几款旨在为现代操作系统还原或改进像素美学的现代矢量字体，并重点介绍了四个值得关注的范例：

*   **Analog Mono**：由 Andrew Gleeson 创作，该字体改进了 20 世纪 90 年代风靡一时的录像机（VCR）和高保真音响（hi-fi）界面字体，修复了以往导致字母降部被迫上移的“低基线”问题。
*   **Coral Pixels**：由吉田久美子（Kumiko Yoshida）设计，该字体融入了“彩边（fringing）”——一种亚像素渲染产生的色彩伪影，以唤起 20 世纪 90 年代至 21 世纪初的数字怀旧感。
*   **Two Slice**：由 Joseph Fatula 创作的极简主义实验性字体，尽管高度仅有两个像素，但仍保持了“一定的可读性”。
*   **Geist Pixel**：由 Vercel 开发，这款字体被定位为实用的系统工具，而非装饰性的新奇产物。作者强调了其“排版严谨性”，并指出许多像素字体常因缩放不当或指标冲突而在实际生产中失效，而 Geist Pixel 则具备专业软件环境所需的精确字距和垂直指标。

文章最后指出，优秀的现代像素字体之所以成功，不仅在于其字形设计，更在于那些能确保其在各种数字视口中可靠运行的“无形”技术工作。

---

## 4. I Bypassed Adobe and Microsoft to Build a Git-Tracked Book Production Pipeline

**原文标题**: I Bypassed Adobe and Microsoft to Build a Git-Tracked Book Production Pipeline

**原文链接**: [https://www.djspeckhals.com/posts/2026-05-22-how-i-bypassed-adobe-and-microsoft-to-build-a-git-tracked-book-production-pipeline/](https://www.djspeckhals.com/posts/2026-05-22-how-i-bypassed-adobe-and-microsoft-to-build-a-git-tracked-book-production-pipeline/)

生成摘要时出错

---

## 5. Xiaomi MiMo-v2.5 Series API Permanent Price Reduction Up to 99%

**原文标题**: Xiaomi MiMo-v2.5 Series API Permanent Price Reduction Up to 99%

**原文链接**: [https://platform.xiaomimimo.com/docs/en-US/news/v2.5-price-update](https://platform.xiaomimimo.com/docs/en-US/news/v2.5-price-update)

生成摘要时出错

---

## 6. Launch HN: Minicor (YC P26) – Windows desktop automations at scale

**原文标题**: Launch HN: Minicor (YC P26) – Windows desktop automations at scale

**原文链接**: [https://www.minicor.com/](https://www.minicor.com/)

生成摘要时出错

---

## 7. Rosalind: A genomics toolkit in Rust running whole-genome pipelines on a laptop

**原文标题**: Rosalind: A genomics toolkit in Rust running whole-genome pipelines on a laptop

**原文链接**: [https://github.com/logannye/rosalind](https://github.com/logannye/rosalind)

生成摘要时出错

---

## 8. Spain blocks prediction markets Polymarket, Kalshi over lack of gambling licence

**原文标题**: Spain blocks prediction markets Polymarket, Kalshi over lack of gambling licence

**原文链接**: [https://www.reuters.com/business/spain-blocks-prediction-markets-polymarket-kalshi-over-lack-gambling-licences-2026-05-26/](https://www.reuters.com/business/spain-blocks-prediction-markets-polymarket-kalshi-over-lack-gambling-licences-2026-05-26/)

生成摘要时出错

---

## 9. C64 Basic: Game Map Overhead "Camera View"

**原文标题**: C64 Basic: Game Map Overhead "Camera View"

**原文链接**: [https://retrogamecoders.com/overhead-camera-view/](https://retrogamecoders.com/overhead-camera-view/)

生成摘要时出错

---

## 10. Sage Care (YC S24) Is Hiring Software Engineers

**原文标题**: Sage Care (YC S24) Is Hiring Software Engineers

**原文链接**: [https://www.ycombinator.com/companies/sagecare/jobs/xtloH8r-senior-software-engineer](https://www.ycombinator.com/companies/sagecare/jobs/xtloH8r-senior-software-engineer)

生成摘要时出错

---

## 11. Outsourcing plus local AI will soon become more economical vs. frontier labs

**原文标题**: Outsourcing plus local AI will soon become more economical vs. frontier labs

**原文链接**: [https://www.signalbloom.ai/posts/outsourcing-plus-localai-will-soon-become-more-economical-vs-frontier-labs/](https://www.signalbloom.ai/posts/outsourcing-plus-localai-will-soon-become-more-economical-vs-frontier-labs/)

生成摘要时出错

---

## 12. The real cost of owning a home

**原文标题**: The real cost of owning a home

**原文链接**: [https://ericturner.dev/posts/cost-of-home-ownership/](https://ericturner.dev/posts/cost-of-home-ownership/)

生成摘要时出错

---

## 13. Language Models Need Sleep

**原文标题**: Language Models Need Sleep

**原文链接**: [https://arxiv.org/abs/2605.26099](https://arxiv.org/abs/2605.26099)

生成摘要时出错

---

## 14. DynIP – Dynamic DNS with RFC 2136, IPv6, DNSSEC, and BYOD

**原文标题**: DynIP – Dynamic DNS with RFC 2136, IPv6, DNSSEC, and BYOD

**原文链接**: [https://dynip.dev/](https://dynip.dev/)

生成摘要时出错

---

## 15. Opaque Types in Python

**原文标题**: Opaque Types in Python

**原文链接**: [https://blog.glyph.im/2026/05/opaque-types-in-python.html](https://blog.glyph.im/2026/05/opaque-types-in-python.html)

生成摘要时出错

---

## 16. Netherlands blocks US takeover of vital digital supplier

**原文标题**: Netherlands blocks US takeover of vital digital supplier

**原文链接**: [https://www.politico.eu/article/netherlands-blocks-us-takeover-vital-digital-supplier/](https://www.politico.eu/article/netherlands-blocks-us-takeover-vital-digital-supplier/)

生成摘要时出错

---

## 17. Taking a walk may lead to more creativity than sitting, study finds (2014)

**原文标题**: Taking a walk may lead to more creativity than sitting, study finds (2014)

**原文链接**: [https://www.apa.org/news/press/releases/2014/04/creativity-walk](https://www.apa.org/news/press/releases/2014/04/creativity-walk)

生成摘要时出错

---

## 18. Dropbox CEO Drew Houston to step down

**原文标题**: Dropbox CEO Drew Houston to step down

**原文链接**: [https://www.cnbc.com/2026/05/26/dropbox-ceo-drew-houston-ashraf-alkarmi.html](https://www.cnbc.com/2026/05/26/dropbox-ceo-drew-houston-ashraf-alkarmi.html)

生成摘要时出错

---

## 19. Are we self-sovereign PKI yet?

**原文标题**: Are we self-sovereign PKI yet?

**原文链接**: [https://buffrr.dev/blog/are-we-self-sovereign-pki-yet/](https://buffrr.dev/blog/are-we-self-sovereign-pki-yet/)

生成摘要时出错

---

## 20. Performance of Rust Language [pdf]

**原文标题**: Performance of Rust Language [pdf]

**原文链接**: [https://github.com/yugr/rust-slides/](https://github.com/yugr/rust-slides/)

生成摘要时出错

---

## 21. Use boring languages with LLMs

**原文标题**: Use boring languages with LLMs

**原文链接**: [https://jry.io/writing/use-boring-languages-with-llms/](https://jry.io/writing/use-boring-languages-with-llms/)

生成摘要时出错

---

## 22. Phantasy Star IV – 1993 Developer Interviews

**原文标题**: Phantasy Star IV – 1993 Developer Interviews

**原文链接**: [https://shmuplations.com/phantasystariv/](https://shmuplations.com/phantasystariv/)

生成摘要时出错

---

## 23. Uber, Lyft drivers in Massachusetts form first US ride-share union

**原文标题**: Uber, Lyft drivers in Massachusetts form first US ride-share union

**原文链接**: [https://www.reuters.com/business/world-at-work/uber-lyft-drivers-massachusetts-form-first-us-ride-share-union-2026-05-26/](https://www.reuters.com/business/world-at-work/uber-lyft-drivers-massachusetts-form-first-us-ride-share-union-2026-05-26/)

生成摘要时出错

---

## 24. The user is visibly frustrated

**原文标题**: The user is visibly frustrated

**原文链接**: [https://pscanf.com/s/354/](https://pscanf.com/s/354/)

生成摘要时出错

---

## 25. What color is your function? (2015)

**原文标题**: What color is your function? (2015)

**原文链接**: [https://journal.stuffwithstuff.com/2015/02/01/what-color-is-your-function/](https://journal.stuffwithstuff.com/2015/02/01/what-color-is-your-function/)

生成摘要时出错

---

## 26. Stack Overflow’s forum is dead but the company’s still kicking

**原文标题**: Stack Overflow’s forum is dead but the company’s still kicking

**原文链接**: [https://wiert.me/2026/05/26/stack-overflows-forum-is-dead-thanks-to-ai-but-the-companys-still-kicking-thanks-to-ai-sherwood-news/](https://wiert.me/2026/05/26/stack-overflows-forum-is-dead-thanks-to-ai-but-the-companys-still-kicking-thanks-to-ai-sherwood-news/)

生成摘要时出错

---

## 27. How Shamir's Secret Sharing Works

**原文标题**: How Shamir's Secret Sharing Works

**原文链接**: [https://ente.com/blog/how-shamirs-secret-sharing-works/](https://ente.com/blog/how-shamirs-secret-sharing-works/)

生成摘要时出错

---

## 28. Is "colorectal cancer" rising in "young people"?

**原文标题**: Is "colorectal cancer" rising in "young people"?

**原文链接**: [https://dynomight.net/crc-rates/](https://dynomight.net/crc-rates/)

生成摘要时出错

---

## 29. How do you build a semiconductor company on something that's free?

**原文标题**: How do you build a semiconductor company on something that's free?

**原文链接**: [https://www.siliconimist.com/p/the-open-source-silicon-business](https://www.siliconimist.com/p/the-open-source-silicon-business)

生成摘要时出错

---

## 30. Ferrari Luce

**原文标题**: Ferrari Luce

**原文链接**: [https://www.ferrari.com/en-EN/auto/ferrari-luce](https://www.ferrari.com/en-EN/auto/ferrari-luce)

生成摘要时出错

---

## 31. Incident with Actions and Pages

**原文标题**: Incident with Actions and Pages

**原文链接**: [https://www.githubstatus.com/incidents/gnftqj9htp0g](https://www.githubstatus.com/incidents/gnftqj9htp0g)

生成摘要时出错

---

## 32. Using AI to write better code more slowly

**原文标题**: Using AI to write better code more slowly

**原文链接**: [https://nolanlawson.com/2026/05/25/using-ai-to-write-better-code-more-slowly/](https://nolanlawson.com/2026/05/25/using-ai-to-write-better-code-more-slowly/)

生成摘要时出错

---

## 33. A successful Japanese trial of a ramjet engine designed for Mach‑5 aircraft

**原文标题**: A successful Japanese trial of a ramjet engine designed for Mach‑5 aircraft

**原文链接**: [https://www.bgr.com/2178211/japan-hypersonic-engine-ramjet-2-hour-flights-to-us/](https://www.bgr.com/2178211/japan-hypersonic-engine-ramjet-2-hour-flights-to-us/)

生成摘要时出错

---

## 34. Eagle 3.1: Collaboration Between the EAGLE Team, vLLM Team, and TorchSpec Team

**原文标题**: Eagle 3.1: Collaboration Between the EAGLE Team, vLLM Team, and TorchSpec Team

**原文链接**: [https://vllm.ai/blog/2026-05-26-eagle-3-1](https://vllm.ai/blog/2026-05-26-eagle-3-1)

生成摘要时出错

---

## 35. Don't put aria-label on generic elements like divs

**原文标题**: Don't put aria-label on generic elements like divs

**原文链接**: [https://www.matuzo.at/blog/2026/aria-label-generic-elements](https://www.matuzo.at/blog/2026/aria-label-generic-elements)

生成摘要时出错

---

## 36. Earthion: A New Mega Drive-Style Shoot-Em-Up

**原文标题**: Earthion: A New Mega Drive-Style Shoot-Em-Up

**原文链接**: [https://earthiongame.com/](https://earthiongame.com/)

生成摘要时出错

---

## 37. Modern Blu-ray drives can now rip GameCube, Wii, and Xbox 360 games to PC

**原文标题**: Modern Blu-ray drives can now rip GameCube, Wii, and Xbox 360 games to PC

**原文链接**: [https://www.tomshardware.com/video-games/console-gaming/modern-blu-ray-drives-can-now-rip-gamecube-wii-and-xbox-360-games-to-pc-third-party-firmware-unlocks-game-rips-from-physical-media-on-select-players](https://www.tomshardware.com/video-games/console-gaming/modern-blu-ray-drives-can-now-rip-gamecube-wii-and-xbox-360-games-to-pc-third-party-firmware-unlocks-game-rips-from-physical-media-on-select-players)

生成摘要时出错

---

## 38. Don't Subscribe So Casually

**原文标题**: Don't Subscribe So Casually

**原文链接**: [https://thebestworstcase.substack.com/p/dont-subscribe-so-casually](https://thebestworstcase.substack.com/p/dont-subscribe-so-casually)

生成摘要时出错

---

## 39. Uber president says AI spending is getting 'harder to justify'

**原文标题**: Uber president says AI spending is getting 'harder to justify'

**原文链接**: [https://www.theverge.com/transportation/937116/uber-ai-investment-hard-to-justify](https://www.theverge.com/transportation/937116/uber-ai-investment-hard-to-justify)

生成摘要时出错

---

## 40. Exit IP VPN servers mitigation rollout

**原文标题**: Exit IP VPN servers mitigation rollout

**原文链接**: [https://mullvad.net/en/help/exit-ip-vpn-servers-mitigation-rollout](https://mullvad.net/en/help/exit-ip-vpn-servers-mitigation-rollout)

生成摘要时出错

---

## 41. Toshifumi Suzuki, founder of Seven-Eleven Japan, has died

**原文标题**: Toshifumi Suzuki, founder of Seven-Eleven Japan, has died

**原文链接**: [https://www.referenceforbusiness.com/biography/S-Z/Suzuki-Toshifumi-1932.html](https://www.referenceforbusiness.com/biography/S-Z/Suzuki-Toshifumi-1932.html)

生成摘要时出错

---

## 42. The AI Industry Just Walked into the Vatican

**原文标题**: The AI Industry Just Walked into the Vatican

**原文链接**: [https://www.driscollglobe.com/p/the-ai-industry-just-walked-into](https://www.driscollglobe.com/p/the-ai-industry-just-walked-into)

生成摘要时出错

---

## 43. Stockholm poised to become leading European geospatial intel player

**原文标题**: Stockholm poised to become leading European geospatial intel player

**原文链接**: [https://www.intelligenceonline.com/europe-russia/2026/05/26/stockholm-poised-to-become-leading-european-geospatial-intel-player,110772386-eve](https://www.intelligenceonline.com/europe-russia/2026/05/26/stockholm-poised-to-become-leading-european-geospatial-intel-player,110772386-eve)

生成摘要时出错

---

## 44. Coalton is an efficient, statically typed Lisp with ideas from Haskell and OCaml

**原文标题**: Coalton is an efficient, statically typed Lisp with ideas from Haskell and OCaml

**原文链接**: [https://coalton-lang.github.io/](https://coalton-lang.github.io/)

生成摘要时出错

---

## 45. Exposing Critical Vulnerabilities in CBSE's On-Screen Marking Portal

**原文标题**: Exposing Critical Vulnerabilities in CBSE's On-Screen Marking Portal

**原文链接**: [https://ni5arga.com/blog/posts/hacking-cbse/](https://ni5arga.com/blog/posts/hacking-cbse/)

生成摘要时出错

---

## 46. California moves to exempt Linux from its age-verification law after backlash

**原文标题**: California moves to exempt Linux from its age-verification law after backlash

**原文链接**: [https://www.tomshardware.com/software/linux/california-moves-to-exempt-linux-from-its-upcoming-age-verification-law-after-backlash-over-forcing-operating-systems-to-collect-users-ages-amendment-proposed-by-the-same-lawmaker-who-wrote-the-original-law](https://www.tomshardware.com/software/linux/california-moves-to-exempt-linux-from-its-upcoming-age-verification-law-after-backlash-over-forcing-operating-systems-to-collect-users-ages-amendment-proposed-by-the-same-lawmaker-who-wrote-the-original-law)

生成摘要时出错

---

## 47. Norway's 2 petabytes of Huawei flash storage and LLM training

**原文标题**: Norway's 2 petabytes of Huawei flash storage and LLM training

**原文链接**: [https://www.blocksandfiles.com/flash/2026/05/22/norways-2-petabytes-of-huawei-flash-storage-and-llm-training/5244910](https://www.blocksandfiles.com/flash/2026/05/22/norways-2-petabytes-of-huawei-flash-storage-and-llm-training/5244910)

生成摘要时出错

---

## 48. Multimodal adaptive optical microscope: in vivo imaging, molecules to organisms

**原文标题**: Multimodal adaptive optical microscope: in vivo imaging, molecules to organisms

**原文链接**: [https://www.nature.com/articles/s41592-026-03066-1](https://www.nature.com/articles/s41592-026-03066-1)

生成摘要时出错

---

## 49. Hacker News front page as a site

**原文标题**: Hacker News front page as a site

**原文链接**: [https://thefrontpage.dev/](https://thefrontpage.dev/)

生成摘要时出错

---

## 50. Magnifica Humanitas

**原文标题**: Magnifica Humanitas

**原文链接**: [https://www.vatican.va/content/leo-xiv/en/encyclicals/documents/20260515-magnifica-humanitas.html](https://www.vatican.va/content/leo-xiv/en/encyclicals/documents/20260515-magnifica-humanitas.html)

生成摘要时出错

---

## 51. Motorola phones have started hijacking the Amazon app to insert affiliate codes

**原文标题**: Motorola phones have started hijacking the Amazon app to insert affiliate codes

**原文链接**: [https://9to5google.com/2026/05/25/motorola-amazon-app-hijacking-behavior/](https://9to5google.com/2026/05/25/motorola-amazon-app-hijacking-behavior/)

生成摘要时出错

---

## 52. It's not just SpaceX: Big Tech is dominating bond markets too

**原文标题**: It's not just SpaceX: Big Tech is dominating bond markets too

**原文链接**: [https://www.ft.com/content/ae38705c-993c-4680-8500-86d0642f85e4](https://www.ft.com/content/ae38705c-993c-4680-8500-86d0642f85e4)

生成摘要时出错

---

## 53. Google, I Dump Your Ass

**原文标题**: Google, I Dump Your Ass

**原文链接**: [https://jaredwhite.com/20260522/google-i-dump-your-ass](https://jaredwhite.com/20260522/google-i-dump-your-ass)

生成摘要时出错

---

## 54. Show HN: Write your BPF programs in Go, not C

**原文标题**: Show HN: Write your BPF programs in Go, not C

**原文链接**: [https://github.com/boratanrikulu/gobee](https://github.com/boratanrikulu/gobee)

生成摘要时出错

---

## 55. What we lost when we stopped letting kids leave the front yard

**原文标题**: What we lost when we stopped letting kids leave the front yard

**原文链接**: [https://stevemagness.substack.com/p/the-cost-of-safetyism](https://stevemagness.substack.com/p/the-cost-of-safetyism)

生成摘要时出错

---

## 56. U.S. Seeks to Give Weapons-Grade Plutonium to Startups for Fuel

**原文标题**: U.S. Seeks to Give Weapons-Grade Plutonium to Startups for Fuel

**原文链接**: [https://www.nytimes.com/2026/05/26/climate/plutonium-nuclear-weapons-fuel.html](https://www.nytimes.com/2026/05/26/climate/plutonium-nuclear-weapons-fuel.html)

生成摘要时出错

---

## 57. AI Startup Says It Will Pay People $2k a Month to Masturbate

**原文标题**: AI Startup Says It Will Pay People $2k a Month to Masturbate

**原文链接**: [https://decrypt.co/368866/ai-startup-pay-people-2000-month-masturbate](https://decrypt.co/368866/ai-startup-pay-people-2000-month-masturbate)

生成摘要时出错

---

## 58. Revenge of the Business Idiot

**原文标题**: Revenge of the Business Idiot

**原文链接**: [https://www.wheresyoured.at/the-revenge-of-the-business-idiot/](https://www.wheresyoured.at/the-revenge-of-the-business-idiot/)

生成摘要时出错

---

## 59. Squares in Squares

**原文标题**: Squares in Squares

**原文链接**: [https://kingbird.myphotos.cc/packing/squares_in_squares.html](https://kingbird.myphotos.cc/packing/squares_in_squares.html)

生成摘要时出错

---

## 60. C extensions, portability, and alternative compilers

**原文标题**: C extensions, portability, and alternative compilers

**原文链接**: [https://lemon.rip/w/6-c-extensions-compilers/](https://lemon.rip/w/6-c-extensions-compilers/)

生成摘要时出错

---

## 61. Jensen–Shannon Divergence

**原文标题**: Jensen–Shannon Divergence

**原文链接**: [https://en.wikipedia.org/wiki/Jensen%E2%80%93Shannon_divergence](https://en.wikipedia.org/wiki/Jensen%E2%80%93Shannon_divergence)

生成摘要时出错

---

## 62. Nobody cracks open a programming book anymore

**原文标题**: Nobody cracks open a programming book anymore

**原文链接**: [https://unix.foo/posts/nobody-cracks-open-a-programming-book/](https://unix.foo/posts/nobody-cracks-open-a-programming-book/)

生成摘要时出错

---

## 63. Micropatching Brings the Abandoned Equation Editor Back to Life (2018)

**原文标题**: Micropatching Brings the Abandoned Equation Editor Back to Life (2018)

**原文链接**: [https://blog.0patch.com/2018/01/bringing-abandoned-equation-editor-back.html](https://blog.0patch.com/2018/01/bringing-abandoned-equation-editor-back.html)

生成摘要时出错

---

## 64. Show HN: OpenBrief – Local-first video downloader/summarizer

**原文标题**: Show HN: OpenBrief – Local-first video downloader/summarizer

**原文链接**: [https://github.com/tantara/openbrief](https://github.com/tantara/openbrief)

生成摘要时出错

---

## 65. One-and-Done Heart Disease Prevention? Scientists Show It May Be Possible

**原文标题**: One-and-Done Heart Disease Prevention? Scientists Show It May Be Possible

**原文链接**: [https://www.nytimes.com/2026/05/25/health/cholesterol-ldl-gene-therapy.html](https://www.nytimes.com/2026/05/25/health/cholesterol-ldl-gene-therapy.html)

生成摘要时出错

---

## 66. IBM Spins Off the First Pure-Play Quantum Chip Foundry

**原文标题**: IBM Spins Off the First Pure-Play Quantum Chip Foundry

**原文链接**: [https://futurumgroup.com/insights/2-billion-chips-act-investment-in-quantum-bets-on-ibms-300mm-superconducting-silicon/](https://futurumgroup.com/insights/2-billion-chips-act-investment-in-quantum-bets-on-ibms-300mm-superconducting-silicon/)

生成摘要时出错

---

## 67. Zero Lines Maze: What the 8-Bit Guy's One-Liner Can Still Teach Us

**原文标题**: Zero Lines Maze: What the 8-Bit Guy's One-Liner Can Still Teach Us

**原文链接**: [https://retrogamecoders.com/zero-lines-maze/](https://retrogamecoders.com/zero-lines-maze/)

生成摘要时出错

---

## 68. What it takes to transpose a matrix

**原文标题**: What it takes to transpose a matrix

**原文链接**: [https://gudok.xyz/transpose/](https://gudok.xyz/transpose/)

生成摘要时出错

---

## 69. The Open/Closed Problem in AI

**原文标题**: The Open/Closed Problem in AI

**原文链接**: [https://blog.mempko.com/the-open-closed-problem-in-ai/](https://blog.mempko.com/the-open-closed-problem-in-ai/)

生成摘要时出错

---

## 70. Logseq Doctor: Heal your flat old Markdown files before importing them to Logseq

**原文标题**: Logseq Doctor: Heal your flat old Markdown files before importing them to Logseq

**原文链接**: [https://github.com/andreoliwa/logseq-doctor](https://github.com/andreoliwa/logseq-doctor)

生成摘要时出错

---

## 71. Everyone Against Us (2023)

**原文标题**: Everyone Against Us (2023)

**原文链接**: [https://www.chicagomag.com/chicago-magazine/april-2023/everyone-against-us/](https://www.chicagomag.com/chicago-magazine/april-2023/everyone-against-us/)

生成摘要时出错

---

## 72. Launch HN: Chert (YC P26) – Twilio for iMessage

**原文标题**: Launch HN: Chert (YC P26) – Twilio for iMessage

**原文链接**: [https://www.trychert.com](https://www.trychert.com)

生成摘要时出错

---

## 73. You Can Start Building LLM Skills Before You Know the Whole Shape

**原文标题**: You Can Start Building LLM Skills Before You Know the Whole Shape

**原文链接**: [https://sosuke.com/you-can-start-building-llm-skills-before-you-know-the-whole-shape/](https://sosuke.com/you-can-start-building-llm-skills-before-you-know-the-whole-shape/)

生成摘要时出错

---

## 74. Sweden becomes a smoke-free country

**原文标题**: Sweden becomes a smoke-free country

**原文链接**: [https://www.thelocal.se/20260525/incredible-milestone-reached-as-sweden-becomes-a-smoke-free-country](https://www.thelocal.se/20260525/incredible-milestone-reached-as-sweden-becomes-a-smoke-free-country)

生成摘要时出错

---

## 75. CVE-2026-28952: Apple macOS 26.5 Kernel Vuln found by Claude

**原文标题**: CVE-2026-28952: Apple macOS 26.5 Kernel Vuln found by Claude

**原文链接**: [https://support.apple.com/en-us/127115](https://support.apple.com/en-us/127115)

生成摘要时出错

---

## 76. Does anybody like React?

**原文标题**: Does anybody like React?

**原文链接**: [https://jsx.lol](https://jsx.lol)

生成摘要时出错

---

## 77. Microsoft Copilot Cowork Exfiltrates Files

**原文标题**: Microsoft Copilot Cowork Exfiltrates Files

**原文链接**: [https://www.promptarmor.com/resources/microsoft-copilot-cowork-exfiltrates-files](https://www.promptarmor.com/resources/microsoft-copilot-cowork-exfiltrates-files)

生成摘要时出错

---

## 78. Yoti age checks share facial photos and device fingerprints with third parties

**原文标题**: Yoti age checks share facial photos and device fingerprints with third parties

**原文链接**: [https://techxplore.com/news/2026-05-online-age-pointless-privacy.html](https://techxplore.com/news/2026-05-online-age-pointless-privacy.html)

生成摘要时出错

---

## 79. Netherlands Seizes 800 Servers, Arrests 2 for Aiding Cyberattacks

**原文标题**: Netherlands Seizes 800 Servers, Arrests 2 for Aiding Cyberattacks

**原文链接**: [https://krebsonsecurity.com/2026/05/netherlands-seizes-800-servers-arrests-2-for-aiding-cyberattacks/](https://krebsonsecurity.com/2026/05/netherlands-seizes-800-servers-arrests-2-for-aiding-cyberattacks/)

生成摘要时出错

---

## 80. A Comma and a Question Mark

**原文标题**: A Comma and a Question Mark

**原文链接**: [https://www.thetypicalset.com/blog/a-comma-and-a-question-mark](https://www.thetypicalset.com/blog/a-comma-and-a-question-mark)

生成摘要时出错

---

## 81. CPPL: A Circuit Prompt Programming Language

**原文标题**: CPPL: A Circuit Prompt Programming Language

**原文链接**: [https://arxiv.org/abs/2605.17892](https://arxiv.org/abs/2605.17892)

生成摘要时出错

---

## 82. China vs. Taiwan: The Geography of an Unfinished War

**原文标题**: China vs. Taiwan: The Geography of an Unfinished War

**原文链接**: [https://jstribune.com/china-vs-taiwan-the-geography-of-an-unfinished-war/](https://jstribune.com/china-vs-taiwan-the-geography-of-an-unfinished-war/)

生成摘要时出错

---

## 83. Bytecode VMs in surprising places (2024)

**原文标题**: Bytecode VMs in surprising places (2024)

**原文链接**: [https://dubroy.com/blog/bytecode-vms-in-surprising-places/](https://dubroy.com/blog/bytecode-vms-in-surprising-places/)

生成摘要时出错

---

## 84. TP-7 Field Recorder

**原文标题**: TP-7 Field Recorder

**原文链接**: [https://teenage.engineering/products/tp-7](https://teenage.engineering/products/tp-7)

生成摘要时出错

---

## 85. Maia-3: free and open source

**原文标题**: Maia-3: free and open source

**原文链接**: [https://lichess.org/@/ashtonanderson/blog/introducing-maia-3-free-and-open-source/vCPPRtX3](https://lichess.org/@/ashtonanderson/blog/introducing-maia-3-free-and-open-source/vCPPRtX3)

生成摘要时出错

---

## 86. A fundamental principle of aeronautical engineering has been overturned

**原文标题**: A fundamental principle of aeronautical engineering has been overturned

**原文链接**: [https://www.wired.com/story/a-fundamental-principle-of-aeronautical-engineering-has-been-overturned/](https://www.wired.com/story/a-fundamental-principle-of-aeronautical-engineering-has-been-overturned/)

生成摘要时出错

---

## 87. Uber’s COO says it’s getting harder to justify money spent on tokenmaxxing

**原文标题**: Uber’s COO says it’s getting harder to justify money spent on tokenmaxxing

**原文链接**: [https://www.businessinsider.com/uber-coo-andrew-macdonald-ai-token-spending-harder-justify-2026-5](https://www.businessinsider.com/uber-coo-andrew-macdonald-ai-token-spending-harder-justify-2026-5)

生成摘要时出错

---

## 88. The Skeuomorphism Nobody Talks About [video]

**原文标题**: The Skeuomorphism Nobody Talks About [video]

**原文链接**: [https://www.youtube.com/watch?v=3Q-G9x315-g](https://www.youtube.com/watch?v=3Q-G9x315-g)

生成摘要时出错

---

## 89. GitHub Actions was down

**原文标题**: GitHub Actions was down

**原文链接**: [https://www.githubstatus.com/?today](https://www.githubstatus.com/?today)

生成摘要时出错

---

## 90. Gnutella: A Protocol Outliving the World That Created It

**原文标题**: Gnutella: A Protocol Outliving the World That Created It

**原文链接**: [https://rickcarlino.com/notes/p2p/gnutella-explanation.html](https://rickcarlino.com/notes/p2p/gnutella-explanation.html)

生成摘要时出错

---

## 91. Bug 1950764: Work Around Crash on Intel Raptor Lake CPU

**原文标题**: Bug 1950764: Work Around Crash on Intel Raptor Lake CPU

**原文链接**: [https://phabricator.services.mozilla.com/D301917](https://phabricator.services.mozilla.com/D301917)

生成摘要时出错

---

## 92. DeepSeek reasonix, DeepSeek native coding agent with high caching and low cost

**原文标题**: DeepSeek reasonix, DeepSeek native coding agent with high caching and low cost

**原文链接**: [https://esengine.github.io/DeepSeek-Reasonix/](https://esengine.github.io/DeepSeek-Reasonix/)

生成摘要时出错

---

## 93. A reality check on the AI jobs hysteria

**原文标题**: A reality check on the AI jobs hysteria

**原文链接**: [https://www.technologyreview.com/2026/05/26/1137855/a-reality-check-on-the-ai-jobs-hysteria/](https://www.technologyreview.com/2026/05/26/1137855/a-reality-check-on-the-ai-jobs-hysteria/)

生成摘要时出错

---

## 94. AI errno(2) values

**原文标题**: AI errno(2) values

**原文链接**: [https://www.netmeister.org/blog/ai-errno.html](https://www.netmeister.org/blog/ai-errno.html)

生成摘要时出错

---

## 95. Show HN: Audiomass – a free, open-source multitrack audio editor for the web

**原文标题**: Show HN: Audiomass – a free, open-source multitrack audio editor for the web

**原文链接**: [https://audiomass.co/?multitrack=1](https://audiomass.co/?multitrack=1)

生成摘要时出错

---

## 96. Show HN: Geomatic – A command-driven geometry studio enabled with autodiff

**原文标题**: Show HN: Geomatic – A command-driven geometry studio enabled with autodiff

**原文链接**: [https://www.tinyvolt.com/geomatic](https://www.tinyvolt.com/geomatic)

生成摘要时出错

---

## 97. Didgeridoo playing as alternative treatment for obstructive sleep apnoea (2006)

**原文标题**: Didgeridoo playing as alternative treatment for obstructive sleep apnoea (2006)

**原文链接**: [https://pmc.ncbi.nlm.nih.gov/articles/PMC1360393/](https://pmc.ncbi.nlm.nih.gov/articles/PMC1360393/)

生成摘要时出错

---

## 98. Building Pi with Pi

**原文标题**: Building Pi with Pi

**原文链接**: [https://lucumr.pocoo.org/2026/5/24/pi-oss/](https://lucumr.pocoo.org/2026/5/24/pi-oss/)

生成摘要时出错

---

## 99. Green card seekers must leave U.S. to apply, Trump administration says

**原文标题**: Green card seekers must leave U.S. to apply, Trump administration says

**原文链接**: [https://www.nytimes.com/2026/05/22/us/politics/green-card-changes-trump.html](https://www.nytimes.com/2026/05/22/us/politics/green-card-changes-trump.html)

生成摘要时出错

---

## 100. Real wages start to shrink in developed countries

**原文标题**: Real wages start to shrink in developed countries

**原文链接**: [https://www.ft.com/content/e126f744-3db9-4305-8871-31f83ebc4ed7](https://www.ft.com/content/e126f744-3db9-4305-8871-31f83ebc4ed7)

生成摘要时出错

---

