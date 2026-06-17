# Hacker News 热门文章摘要 (2026-06-17)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Epic Games 发布 Lore 版本控制系统

**原文标题**: Epic Games announces Lore version control system

**原文链接**: [https://lore.org/](https://lore.org/)

Epic Games 宣布推出 **Lore**，这是一个下一代开源版本控制系统 (VCS)，专为处理现代游戏开发和媒体项目的海量规模而设计。与传统系统不同，Lore 针对源代码与大型二进制资产共存的环境进行了优化，能够同时满足开发者和艺术家的工作流程需求。

**技术架构**
Lore 采用基于 Merkle 树和不可变版本链的中心化、内容寻址架构。这确保了加密数据的完整性和“防篡改”的历史记录。主要技术特性包括：
*   **大文件分块：** 将沉重的资产分解为可复用的数据块，以最大限度地减少冗余并优化传输。
*   **按需填充 (On-Demand Hydration)：** 支持稀疏工作区，仅在需要时下载数据，从而保持本地环境的轻量化。
*   **高扩展性：** 采用内置缓存的面向服务设计，使系统能够处理大型团队的高吞吐量需求。
*   **高效分支：** 分支以轻量级引用的形式实现，支持近乎瞬时的创建和切换，且无需复制底层数据。

**集成与开源理念**
Lore 完全开源，并在 **MIT 许可证**下发布。Epic Games 强调协作模式，鼓励社区贡献代码，旨在打造版本控制的开放标准。

该系统提供功能完备的命令行界面 (CLI)，并为多种编程语言提供 SDK，包括 **C/C++、C#、Rust、Go、Python 和 JavaScript**，确保其能够无缝集成到各种生产管线中。

**入门指南**
该项目目前托管在 Epic Games 的 GitHub 仓库中，用户可以在此处获取核心库、服务器代码和文档。此外，官方还建立了专门的 Discord 社区，为早期采用者和贡献者提供支持。

---

## 2. Only 16 Percent of Americans Think AI Will Have a Positive Impact on Society

**原文标题**: Only 16 Percent of Americans Think AI Will Have a Positive Impact on Society

**原文链接**: [https://techcrunch.com/2026/06/17/only-16-percent-of-americans-think-ai-will-have-a-positive-impact-on-society-a-new-study-shows/](https://techcrunch.com/2026/06/17/only-16-percent-of-americans-think-ai-will-have-a-positive-impact-on-society-a-new-study-shows/)

A recent Pew Research study reveals a profound disconnect between Americans’ increasing use of AI and their deep-seated skepticism regarding its future. While AI adoption is surging—with ChatGPT usage doubling since 2023 to 44% of adults—only 16% of Americans believe the technology will have a positive impact on society over the next 20 years. Conversely, 40% anticipate a negative impact, and two-thirds feel development is moving too quickly.

Public trust in the oversight of AI is notably low: 67% of respondents doubt the government’s ability to regulate the industry effectively, and 59% do not trust corporations to develop the technology safely. Surprisingly, young people (under 30) are the most pessimistic, with only 14% expecting a positive societal outcome.

Usage patterns also highlight demographic divides:
*   **Gender:** Men use AI more frequently and express more enthusiasm, while women remain more skeptical.
*   **Age:** While those under 50 are the primary users, nearly 75% of Americans aged 65 and older have never used a chatbot and express little interest in doing so.
*   **Market Dominance:** ChatGPT remains the leader, followed by Google’s Gemini (24%) and Microsoft’s Copilot (17%).

Despite their reservations, many Americans now find AI unavoidable. Approximately 25% use chatbots daily for work or research, and 60% regularly consume AI-generated internet summaries. Ultimately, the report portrays a nation that is integrating AI into daily life out of utility or necessity, even as it remains profoundly uneasy about the long-term consequences.

---

## 3. Launch HN: Adam (YC W25) – Open-Source AI CAD

**原文标题**: Launch HN: Adam (YC W25) – Open-Source AI CAD

**原文链接**: [https://github.com/Adam-CAD/CADAM](https://github.com/Adam-CAD/CADAM)

生成摘要时出错

---

## 4. GLM-5.2 是 Artificial Analysis 上新晋领先的开源权重模型。

**原文标题**: GLM-5.2 is the new leading open weights model on Artificial Analysis

**原文链接**: [https://artificialanalysis.ai/articles/glm-5-2-is-the-new-leading-open-weights-model-on-the-artificial-analysis-intelligence-index](https://artificialanalysis.ai/articles/glm-5-2-is-the-new-leading-open-weights-model-on-the-artificial-analysis-intelligence-index)

2026年6月17日，Z ai 发布了 **GLM-5.2**，该模型已正式成为 Artificial Analysis 智能指数 v4.1 上领先的开源权重模型。它凭借 51 分的得分，超越了 MiniMax-M3、DeepSeek V4 Pro 和 Kimi K2.6 等竞争对手。

**关键性能与技术规格：**
*   **架构：** 保持与 GLM-5.1 相同的规模（总参数 744B / 激活参数 40B），但实现了 11 分的智力提升。
*   **基准测试：** 该模型在科学推理（CritPt、HLE 和 GPQA Diamond）和智能体性能方面表现出显著进步。值得注意的是，它在 GDPval-AA v2 上获得了 1524 分，足以媲美 GPT-5.5 等私有模型。
*   **上下文窗口：** 从上一版本的 20 万 token 大幅扩展至 100 万 token。
*   **许可协议：** 基于 MIT 协议发布。

**成本与效率：**
GLM-5.2 处于**“智力 vs. 单任务成本”帕累托前沿**，这意味着在同等智力水平下，它提供了最低的成本（每任务 0.46 美元）。然而，它的 token 效率低于同类模型，每任务消耗 4.3 万个输出 token（其中 3.7 万个为推理 token）。其 API 定价与 GLM-5.1 保持一致：每百万输入 token 1.40 美元，每百万输出 token 4.40 美元。

**可用性：**
除了 Z ai 的官方 API 外，该模型还通过 DeepInfra、Novita、Nebius、硅基流动 (Siliconflow) 和 Fireworks 等第三方供应商广泛提供。尽管 GLM-5.2 在开源权重类别中处于领先地位，但在综合性能上目前仍落后于 Anthropic 的 Claude Fable 5 等“神话级” (Mythos-class) 私有模型。

---

## 5. How we run Firecracker VMs inside EC2 and start browsers in less than 1s

**原文标题**: How we run Firecracker VMs inside EC2 and start browsers in less than 1s

**原文链接**: [https://browser-use.com/posts/firecracker-browser-infra](https://browser-use.com/posts/firecracker-browser-infra)

Browser Use Cloud recently overhauled its infrastructure to achieve three primary goals for its cloud browsers: speed, security, and affordability. By transitioning from Unikraft unikernels to **Firecracker VMs** running on standard **AWS EC2** instances, the company reduced costs from $0.06 to $0.02 per hour and achieved start times of under one second.

To overcome the latency of "nested virtualization" (running a VM inside an EC2 VM), the team implemented several low-level optimizations:

*   **Memory Management:** By switching from 4KB to **2MB memory pages**, they reduced expensive page faults by 91%, cutting VM resume time from 9.8s to 3.1s. They also utilized a custom `userfaultfd` handler to proactively load memory pages.
*   **CPU Optimization:** To handle Chromium’s resource-heavy startup, vCPUs are left unpinned during the launch burst to spread the load across the host. Once the browser is ready, vCPUs are pinned to specific cores with real-time priority to ensure stability and high density.
*   **Communication:** The host monitors the VM via **vsock** instead of HTTP polling, reducing "VM exits" and latency.
*   **Stealth and Efficiency:** Instead of using resource-heavy display servers, they developed a custom **headless Chromium fork**. By patching the browser at a low level and using real-world fingerprints, they achieved a top-tier 81% anti-bot bypass rate without the overhead of a graphical interface.

The result is a system with a **p50 creation latency of 825ms** and 100% reliability during stress tests. Moving forward, the team plans to snapshot VMs *after* Chromium has already launched, which could shave another 500ms off the startup time by eliminating the browser’s internal boot process.

---

## 6. US holds off blacklisting DeepSeek, more than 100 firms deemed security risks

**原文标题**: US holds off blacklisting DeepSeek, more than 100 firms deemed security risks

**原文链接**: [https://www.reuters.com/world/china/us-holds-off-blacklisting-chinas-deepseek-more-than-100-firms-deemed-security-2026-06-17/](https://www.reuters.com/world/china/us-holds-off-blacklisting-chinas-deepseek-more-than-100-firms-deemed-security-2026-06-17/)

生成摘要时出错

---

## 7. The Competitive Moat That AI Can't Replicate

**原文标题**: The Competitive Moat That AI Can't Replicate

**原文链接**: [https://ghostinthedata.info/posts/2026/2026-06-13-human-connection-moat/](https://ghostinthedata.info/posts/2026/2026-06-13-human-connection-moat/)

生成摘要时出错

---

## 8. Sixty percent of US consumers say 'AI' in brand messaging is a turnoff

**原文标题**: Sixty percent of US consumers say 'AI' in brand messaging is a turnoff

**原文链接**: [https://wpvip.com/future-of-the-web-2026/](https://wpvip.com/future-of-the-web-2026/)

生成摘要时出错

---

## 9. RFC 10008: The new HTTP Query Method

**原文标题**: RFC 10008: The new HTTP Query Method

**原文链接**: [https://www.rfc-editor.org/info/rfc10008/](https://www.rfc-editor.org/info/rfc10008/)

生成摘要时出错

---

## 10. U.S. science is in chaos

**原文标题**: U.S. science is in chaos

**原文链接**: [https://www.scientificamerican.com/article/americas-compact-between-science-and-politics-is-broken/](https://www.scientificamerican.com/article/americas-compact-between-science-and-politics-is-broken/)

生成摘要时出错

---

## 11. Trellis AI (YC W24)  hiring a product lead to build agents for healthcare access

**原文标题**: Trellis AI (YC W24)  hiring a product lead to build agents for healthcare access

**原文链接**: [https://www.ycombinator.com/companies/trellis-ai/jobs/Cg94htp-product-lead](https://www.ycombinator.com/companies/trellis-ai/jobs/Cg94htp-product-lead)

生成摘要时出错

---

## 12. Want your images back? That'll be $5

**原文标题**: Want your images back? That'll be $5

**原文链接**: [https://www.lutr.dev/want-your-images-back-sure-that-ll-be-5-dollars](https://www.lutr.dev/want-your-images-back-sure-that-ll-be-5-dollars)

生成摘要时出错

---

## 13. The hacker sent by Anthropic to calm the government's nerves about AI safety

**原文标题**: The hacker sent by Anthropic to calm the government's nerves about AI safety

**原文链接**: [https://www.wsj.com/tech/ai/anthropic-mythos-safety-nicholas-carlini-20bceaa3](https://www.wsj.com/tech/ai/anthropic-mythos-safety-nicholas-carlini-20bceaa3)

生成摘要时出错

---

## 14. Why thinking out loud with someone beats thinking alone

**原文标题**: Why thinking out loud with someone beats thinking alone

**原文链接**: [https://www.thesignalist.io/s/the-dialogue-dividend/](https://www.thesignalist.io/s/the-dialogue-dividend/)

生成摘要时出错

---

## 15. MicroUI – A tiny, portable, immediate-mode UI library written in ANSI C

**原文标题**: MicroUI – A tiny, portable, immediate-mode UI library written in ANSI C

**原文链接**: [https://github.com/rxi/microui](https://github.com/rxi/microui)

生成摘要时出错

---

## 16. TREX: An AI code reviewer that runs your code

**原文标题**: TREX: An AI code reviewer that runs your code

**原文链接**: [https://www.greptile.com/blog/trex-code-execution](https://www.greptile.com/blog/trex-code-execution)

生成摘要时出错

---

## 17. Show HN: Inkwash, a watercolor sketching app and explanation

**原文标题**: Show HN: Inkwash, a watercolor sketching app and explanation

**原文链接**: [https://johnowhitaker.github.io/inkwash/about](https://johnowhitaker.github.io/inkwash/about)

生成摘要时出错

---

## 18. Hacker News but for independent blogs

**原文标题**: Hacker News but for independent blogs

**原文链接**: [https://bubbles.town/](https://bubbles.town/)

生成摘要时出错

---

## 19. French physicist and media star loses doctorate after plagiarism investigation

**原文标题**: French physicist and media star loses doctorate after plagiarism investigation

**原文链接**: [https://www.science.org/content/article/french-physicist-and-media-star-loses-doctorate-after-plagiarism-investigation](https://www.science.org/content/article/french-physicist-and-media-star-loses-doctorate-after-plagiarism-investigation)

生成摘要时出错

---

## 20. The Capitoline Wolf

**原文标题**: The Capitoline Wolf

**原文链接**: [https://thehappytraveler.ca/travel-guide-italy/capitoline-wolf-siena-rome-myths/](https://thehappytraveler.ca/travel-guide-italy/capitoline-wolf-siena-rome-myths/)

生成摘要时出错

---

## 21. Kirkland Roundabouts

**原文标题**: Kirkland Roundabouts

**原文链接**: [https://kirklandroundabouts.com](https://kirklandroundabouts.com)

生成摘要时出错

---

## 22. AI demands more engineering discipline. Not less

**原文标题**: AI demands more engineering discipline. Not less

**原文链接**: [https://charitydotwtf.substack.com/p/ai-demands-more-engineering-discipline](https://charitydotwtf.substack.com/p/ai-demands-more-engineering-discipline)

生成摘要时出错

---

## 23. AI chemist improves a challenging reaction in medicinal chemistry

**原文标题**: AI chemist improves a challenging reaction in medicinal chemistry

**原文链接**: [https://openai.com/index/ai-chemist-improves-reaction/](https://openai.com/index/ai-chemist-improves-reaction/)

生成摘要时出错

---

## 24. Show HN: An 8-bit live gamecast for baseball

**原文标题**: Show HN: An 8-bit live gamecast for baseball

**原文链接**: [https://ribbie.tv/watch](https://ribbie.tv/watch)

生成摘要时出错

---

## 25. Seventeen Camels and Where They Can Take You

**原文标题**: Seventeen Camels and Where They Can Take You

**原文链接**: [https://mathenchant.wordpress.com/2026/06/15/seventeen-camels-and-where-they-can-take-you/](https://mathenchant.wordpress.com/2026/06/15/seventeen-camels-and-where-they-can-take-you/)

生成摘要时出错

---

## 26. Image Compression

**原文标题**: Image Compression

**原文链接**: [https://www.makingsoftware.com/chapters/image-compression](https://www.makingsoftware.com/chapters/image-compression)

生成摘要时出错

---

## 27. Volkswagen started blocking GrapheneOS users

**原文标题**: Volkswagen started blocking GrapheneOS users

**原文链接**: [https://discuss.grapheneos.org/d/35949-volkswagen-app?page=3](https://discuss.grapheneos.org/d/35949-volkswagen-app?page=3)

生成摘要时出错

---

## 28. Why do commercial spaces sit vacant? (2025)

**原文标题**: Why do commercial spaces sit vacant? (2025)

**原文链接**: [https://www.freerange.city/p/why-do-commercial-spaces-sit-vacant](https://www.freerange.city/p/why-do-commercial-spaces-sit-vacant)

生成摘要时出错

---

## 29. The founder's playbook: Building an AI-native startup

**原文标题**: The founder's playbook: Building an AI-native startup

**原文链接**: [https://claude.com/blog/the-founders-playbook](https://claude.com/blog/the-founders-playbook)

生成摘要时出错

---

## 30. Abandoned and Little-Known Airfields

**原文标题**: Abandoned and Little-Known Airfields

**原文链接**: [https://airfields-freeman.com/](https://airfields-freeman.com/)

生成摘要时出错

---

## 31. Show HN: Deconvolution – a Rust image deconvolution and restoration crate

**原文标题**: Show HN: Deconvolution – a Rust image deconvolution and restoration crate

**原文链接**: [https://github.com/pbkx/deconvolution](https://github.com/pbkx/deconvolution)

生成摘要时出错

---

## 32. Show HN: High-Res Neural Cellular Automata

**原文标题**: Show HN: High-Res Neural Cellular Automata

**原文链接**: [https://cells2pixels.github.io/](https://cells2pixels.github.io/)

生成摘要时出错

---

## 33. GLM 5.2 Performance Benchmarks

**原文标题**: GLM 5.2 Performance Benchmarks

**原文链接**: [https://artificialanalysis.ai/models/glm-5-2](https://artificialanalysis.ai/models/glm-5-2)

生成摘要时出错

---

## 34. Map Clustering Is Not My Favorite

**原文标题**: Map Clustering Is Not My Favorite

**原文链接**: [https://blog.greg.technology/2026/06/12/map-clustering-is-not-my-favorite.html](https://blog.greg.technology/2026/06/12/map-clustering-is-not-my-favorite.html)

生成摘要时出错

---

## 35. Show HN: Capacitor Alarm Clock

**原文标题**: Show HN: Capacitor Alarm Clock

**原文链接**: [https://github.com/ArcaEge/capacitor-alarm-clock](https://github.com/ArcaEge/capacitor-alarm-clock)

生成摘要时出错

---

## 36. The Rise and (Potential) Fall of Letterboxd

**原文标题**: The Rise and (Potential) Fall of Letterboxd

**原文链接**: [https://www.statsignificant.com/p/the-rise-and-potential-fall-of-letterboxd](https://www.statsignificant.com/p/the-rise-and-potential-fall-of-letterboxd)

生成摘要时出错

---

## 37. Humiliating IIS servers for fun and jail time

**原文标题**: Humiliating IIS servers for fun and jail time

**原文链接**: [https://mll.sh/humiliating-iis-servers-for-fun-and-jail-time/](https://mll.sh/humiliating-iis-servers-for-fun-and-jail-time/)

生成摘要时出错

---

## 38. Bringing down my ZSH load times from ~3.1s to ~230ms

**原文标题**: Bringing down my ZSH load times from ~3.1s to ~230ms

**原文链接**: [https://iam.mt/bringing-down-my-zsh-load-times-from-3-1s-to-230ms/](https://iam.mt/bringing-down-my-zsh-load-times-from-3-1s-to-230ms/)

生成摘要时出错

---

## 39. Subterranean fungi networks more than 100 quadrillion km in length

**原文标题**: Subterranean fungi networks more than 100 quadrillion km in length

**原文链接**: [https://www.theguardian.com/science/2026/jun/11/arbuscular-mycorrhizal-fungi-plant-life-climate-global-mapping-study](https://www.theguardian.com/science/2026/jun/11/arbuscular-mycorrhizal-fungi-plant-life-climate-global-mapping-study)

生成摘要时出错

---

## 40. Language Courses in the Public Domain

**原文标题**: Language Courses in the Public Domain

**原文链接**: [https://fsi-languages.yojik.eu/](https://fsi-languages.yojik.eu/)

生成摘要时出错

---

## 41. Running local models is good now

**原文标题**: Running local models is good now

**原文链接**: [https://vickiboykis.com/2026/06/15/running-local-models-is-good-now/](https://vickiboykis.com/2026/06/15/running-local-models-is-good-now/)

生成摘要时出错

---

## 42. Pentagon boasts of using AI to write reports mandated by Congress (1.5mil users)

**原文标题**: Pentagon boasts of using AI to write reports mandated by Congress (1.5mil users)

**原文链接**: [https://arstechnica.com/ai/2026/06/pentagon-boasts-of-using-ai-to-write-reports-mandated-by-congress/](https://arstechnica.com/ai/2026/06/pentagon-boasts-of-using-ai-to-write-reports-mandated-by-congress/)

生成摘要时出错

---

## 43. GrapheneOS has been ported to Android 17

**原文标题**: GrapheneOS has been ported to Android 17

**原文链接**: [https://discuss.grapheneos.org/d/36469-grapheneos-has-been-ported-to-android-17-and-official-releases-are-coming-soon](https://discuss.grapheneos.org/d/36469-grapheneos-has-been-ported-to-android-17-and-official-releases-are-coming-soon)

生成摘要时出错

---

## 44. Open-source React UI and D-pad focus engine for Meta Ray-Ban Display

**原文标题**: Open-source React UI and D-pad focus engine for Meta Ray-Ban Display

**原文链接**: [https://glasskit.app/ui](https://glasskit.app/ui)

生成摘要时出错

---

## 45. Agentic coding deserves more than a chat box bolted onto VS Code

**原文标题**: Agentic coding deserves more than a chat box bolted onto VS Code

**原文链接**: [https://github.com/evanklem/polypore](https://github.com/evanklem/polypore)

生成摘要时出错

---

## 46. From Chesterton's fence to Chesterton's gap

**原文标题**: From Chesterton's fence to Chesterton's gap

**原文链接**: [https://stephantul.github.io/blog/unfence/](https://stephantul.github.io/blog/unfence/)

生成摘要时出错

---

## 47. Wolfram Language and Mathematica version 15

**原文标题**: Wolfram Language and Mathematica version 15

**原文链接**: [https://writings.stephenwolfram.com/2026/06/launching-version-15-of-wolfram-language-mathematica-built-in-useful-ai-lots-of-new-core-functionality/](https://writings.stephenwolfram.com/2026/06/launching-version-15-of-wolfram-language-mathematica-built-in-useful-ai-lots-of-new-core-functionality/)

生成摘要时出错

---

## 48. SpaceX to buy Cursor for $60B

**原文标题**: SpaceX to buy Cursor for $60B

**原文链接**: [https://www.reuters.com/legal/transactional/spacex-buy-anysphere-60-billion-2026-06-16/](https://www.reuters.com/legal/transactional/spacex-buy-anysphere-60-billion-2026-06-16/)

生成摘要时出错

---

## 49. Capital Factory CEO Joshua Baer killed in plane crash near Laredo, TX

**原文标题**: Capital Factory CEO Joshua Baer killed in plane crash near Laredo, TX

**原文链接**: [https://cbsaustin.com/news/local/capital-factory-ceo-joshua-baer-killed-in-plane-crash-near-laredo-texas](https://cbsaustin.com/news/local/capital-factory-ceo-joshua-baer-killed-in-plane-crash-near-laredo-texas)

生成摘要时出错

---

## 50. Show HN: I built 184 free browser tools – PDF, image, dev, AI tasks, no upload

**原文标题**: Show HN: I built 184 free browser tools – PDF, image, dev, AI tasks, no upload

**原文链接**: [https://brevio.pro](https://brevio.pro)

生成摘要时出错

---

## 51. DeepSeek v4 Pro 1.6T model post-trained by Huawei on 1000 Ascend 910C chips

**原文标题**: DeepSeek v4 Pro 1.6T model post-trained by Huawei on 1000 Ascend 910C chips

**原文链接**: [https://www.tomshardware.com/tech-industry/artificial-intelligence/huawei-led-team-claims-it-post-trained-deepseeks-1-6-trillion-parameter-models-on-ascend-910c-chips](https://www.tomshardware.com/tech-industry/artificial-intelligence/huawei-led-team-claims-it-post-trained-deepseeks-1-6-trillion-parameter-models-on-ascend-910c-chips)

生成摘要时出错

---

## 52. Semiclassical Gravity Efficiently Solves NP-Complete Problems

**原文标题**: Semiclassical Gravity Efficiently Solves NP-Complete Problems

**原文链接**: [https://arxiv.org/abs/2606.14806](https://arxiv.org/abs/2606.14806)

生成摘要时出错

---

## 53. UK's Social Media Ban: The Monumental Pretext for Total Digital Surveillance

**原文标题**: UK's Social Media Ban: The Monumental Pretext for Total Digital Surveillance

**原文链接**: [https://modernity.news/2026/06/16/uks-social-media-ban-the-monumental-pretext-for-total-digital-surveillance/](https://modernity.news/2026/06/16/uks-social-media-ban-the-monumental-pretext-for-total-digital-surveillance/)

生成摘要时出错

---

## 54. Making 'food out of thin air' (2024)

**原文标题**: Making 'food out of thin air' (2024)

**原文链接**: [https://www.noemamag.com/making-food-out-of-thin-air/](https://www.noemamag.com/making-food-out-of-thin-air/)

生成摘要时出错

---

## 55. A brief tour of the PDP-11, the most influential minicomputer of all time (2022)

**原文标题**: A brief tour of the PDP-11, the most influential minicomputer of all time (2022)

**原文链接**: [https://arstechnica.com/gadgets/2022/03/a-brief-tour-of-the-pdp-11-the-most-influential-minicomputer-of-all-time/](https://arstechnica.com/gadgets/2022/03/a-brief-tour-of-the-pdp-11-the-most-influential-minicomputer-of-all-time/)

生成摘要时出错

---

## 56. Qwen-Robot Suite: A Foundation Model Suite for Physical World Intelligence

**原文标题**: Qwen-Robot Suite: A Foundation Model Suite for Physical World Intelligence

**原文链接**: [https://qwen.ai/blog?id=qwen-robotsuite](https://qwen.ai/blog?id=qwen-robotsuite)

生成摘要时出错

---

## 57. 10Gb/s Ethernet: switching to a Broadcom SFP+ module

**原文标题**: 10Gb/s Ethernet: switching to a Broadcom SFP+ module

**原文链接**: [https://www.gilesthomas.com/2026/06/10g-ethernet-switching-to-broadcom-sfp-plus](https://www.gilesthomas.com/2026/06/10g-ethernet-switching-to-broadcom-sfp-plus)

生成摘要时出错

---

## 58. TIL: You can make HTTP requests without curl using Bash /dev/TCP

**原文标题**: TIL: You can make HTTP requests without curl using Bash /dev/TCP

**原文链接**: [https://mareksuppa.com/til/bash-dev-tcp-http-without-curl/](https://mareksuppa.com/til/bash-dev-tcp-http-without-curl/)

生成摘要时出错

---

## 59. AI will lead to labor shortages, Bezos says in optimistic talk

**原文标题**: AI will lead to labor shortages, Bezos says in optimistic talk

**原文链接**: [https://www.reuters.com/business/world-at-work/ai-will-lead-labour-shortages-jeff-bezos-says-vivatech-2026-06-17/](https://www.reuters.com/business/world-at-work/ai-will-lead-labour-shortages-jeff-bezos-says-vivatech-2026-06-17/)

生成摘要时出错

---

## 60. ChatGPT Is Down

**原文标题**: ChatGPT Is Down

**原文链接**: [https://chatgpt.com](https://chatgpt.com)

生成摘要时出错

---

## 61. Mechanical Watch (2022)

**原文标题**: Mechanical Watch (2022)

**原文链接**: [https://ciechanow.ski/mechanical-watch/](https://ciechanow.ski/mechanical-watch/)

生成摘要时出错

---

## 62. Calvin and Hobbes and the price of integrity

**原文标题**: Calvin and Hobbes and the price of integrity

**原文链接**: [https://therepublicofletters.substack.com/p/calvin-and-hobbes-and-the-price-of](https://therepublicofletters.substack.com/p/calvin-and-hobbes-and-the-price-of)

生成摘要时出错

---

## 63. Has AI already killed self-help nonfiction books?

**原文标题**: Has AI already killed self-help nonfiction books?

**原文链接**: [https://tim.blog/2026/06/12/has-ai-already-killed-nonfiction/](https://tim.blog/2026/06/12/has-ai-already-killed-nonfiction/)

生成摘要时出错

---

## 64. Show HN: cuTile Rust: Safe, data-race-free GPU kernels in Rust

**原文标题**: Show HN: cuTile Rust: Safe, data-race-free GPU kernels in Rust

**原文链接**: [https://github.com/nvlabs/cutile-rs](https://github.com/nvlabs/cutile-rs)

生成摘要时出错

---

## 65. A backdoor in a LinkedIn job offer

**原文标题**: A backdoor in a LinkedIn job offer

**原文链接**: [https://roman.pt/posts/linkedin-backdoor/](https://roman.pt/posts/linkedin-backdoor/)

生成摘要时出错

---

## 66. Apple's weird anti-nausea dots cured my car sickness

**原文标题**: Apple's weird anti-nausea dots cured my car sickness

**原文链接**: [https://www.theverge.com/tech/942854/apple-vehicle-motion-cues-review-really-work](https://www.theverge.com/tech/942854/apple-vehicle-motion-cues-review-really-work)

生成摘要时出错

---

## 67. I hacked into the worst e-bike and fixed it [video]

**原文标题**: I hacked into the worst e-bike and fixed it [video]

**原文链接**: [https://www.youtube.com/watch?v=hPrtVGimBYs](https://www.youtube.com/watch?v=hPrtVGimBYs)

生成摘要时出错

---

## 68. A Nipkow Disk Mechanical TV Simulator

**原文标题**: A Nipkow Disk Mechanical TV Simulator

**原文链接**: [https://analogtv.net/mechanical-lab](https://analogtv.net/mechanical-lab)

生成摘要时出错

---

## 69. GPT‑NL: a sovereign language model for the Netherlands

**原文标题**: GPT‑NL: a sovereign language model for the Netherlands

**原文链接**: [https://www.tno.nl/en/digital/artificial-intelligence/gpt-nl/](https://www.tno.nl/en/digital/artificial-intelligence/gpt-nl/)

生成摘要时出错

---

## 70. Is Meta destroying its engineering organization?

**原文标题**: Is Meta destroying its engineering organization?

**原文链接**: [https://newsletter.pragmaticengineer.com/p/why-is-meta-destroying-its-engineering](https://newsletter.pragmaticengineer.com/p/why-is-meta-destroying-its-engineering)

生成摘要时出错

---

## 71. I admire Fabrice Bellard. He is almost certainly a better overall programmer

**原文标题**: I admire Fabrice Bellard. He is almost certainly a better overall programmer

**原文链接**: [https://twitter.com/ID_AA_Carmack/status/2064095424420487226](https://twitter.com/ID_AA_Carmack/status/2064095424420487226)

生成摘要时出错

---

## 72. Stop Using JWTs

**原文标题**: Stop Using JWTs

**原文链接**: [https://gist.github.com/samsch/0d1f3d3b4745d778f78b230cf6061452](https://gist.github.com/samsch/0d1f3d3b4745d778f78b230cf6061452)

生成摘要时出错

---

## 73. Poland Invests $11M in ElevenLabs to Build AI Tech Hub

**原文标题**: Poland Invests $11M in ElevenLabs to Build AI Tech Hub

**原文链接**: [https://www.bloomberg.com/news/articles/2026-06-17/poland-invests-11-million-in-elevenlabs-to-build-ai-tech-hub](https://www.bloomberg.com/news/articles/2026-06-17/poland-invests-11-million-in-elevenlabs-to-build-ai-tech-hub)

生成摘要时出错

---

## 74. Findaforager.com – The Database to Find a Forager Near You

**原文标题**: Findaforager.com – The Database to Find a Forager Near You

**原文链接**: [https://www.robingreenfield.org/findaforager/](https://www.robingreenfield.org/findaforager/)

生成摘要时出错

---

## 75. The Ordinary Life, and How a Good Life Might Look Boring

**原文标题**: The Ordinary Life, and How a Good Life Might Look Boring

**原文链接**: [https://www.ssp.sh/brain/the-ordinary-boring-life/](https://www.ssp.sh/brain/the-ordinary-boring-life/)

生成摘要时出错

---

## 76. The Manhoff Archives: Color photos of Stalin-era USSR taken by a US diplomat

**原文标题**: The Manhoff Archives: Color photos of Stalin-era USSR taken by a US diplomat

**原文链接**: [https://www.rferl.org/a/the-manhoff-archive/28359558.html](https://www.rferl.org/a/the-manhoff-archive/28359558.html)

生成摘要时出错

---

## 77. Stop Killing Games fails to secure EU law despite 1.3M signatures

**原文标题**: Stop Killing Games fails to secure EU law despite 1.3M signatures

**原文链接**: [https://www.dexerto.com/gaming/stop-killing-games-fails-to-secure-eu-law-despite-1-3m-signatures-3376431/](https://www.dexerto.com/gaming/stop-killing-games-fails-to-secure-eu-law-despite-1-3m-signatures-3376431/)

生成摘要时出错

---

## 78. Al Arabiya English obtains 14-point draft of US-Iran Memorandum of Understanding

**原文标题**: Al Arabiya English obtains 14-point draft of US-Iran Memorandum of Understanding

**原文链接**: [https://english.alarabiya.net/News/middle-east/2026/06/16/al-arabiya-obtains-14point-draft-usiran-deal](https://english.alarabiya.net/News/middle-east/2026/06/16/al-arabiya-obtains-14point-draft-usiran-deal)

生成摘要时出错

---

## 79. Pentagon says Grok has been used to launch missiles at Iran

**原文标题**: Pentagon says Grok has been used to launch missiles at Iran

**原文链接**: [https://thehill.com/policy/technology/5928204-pentagon-musk-grok-chatbot-iran-strikes/](https://thehill.com/policy/technology/5928204-pentagon-musk-grok-chatbot-iran-strikes/)

生成摘要时出错

---

## 80. Lattice Triangles Are Rare

**原文标题**: Lattice Triangles Are Rare

**原文链接**: [https://axiommath.ai/territory/the-reveal](https://axiommath.ai/territory/the-reveal)

生成摘要时出错

---

## 81. Frood, an Alpine Initramfs NAS (2024)

**原文标题**: Frood, an Alpine Initramfs NAS (2024)

**原文链接**: [https://words.filippo.io/frood/](https://words.filippo.io/frood/)

生成摘要时出错

---

## 82. Multiple JetBrains IDE plugins caught stealing AI keys

**原文标题**: Multiple JetBrains IDE plugins caught stealing AI keys

**原文链接**: [https://www.aikido.dev/blog/multiple-jetbrains-ide-plugins-caught-stealing-ai-keys](https://www.aikido.dev/blog/multiple-jetbrains-ide-plugins-caught-stealing-ai-keys)

生成摘要时出错

---

## 83. Iroh 1.0

**原文标题**: Iroh 1.0

**原文链接**: [https://www.iroh.computer/blog/v1](https://www.iroh.computer/blog/v1)

生成摘要时出错

---

## 84. Unicorn – The Ultimate CPU Emulator

**原文标题**: Unicorn – The Ultimate CPU Emulator

**原文链接**: [https://www.unicorn-engine.org/](https://www.unicorn-engine.org/)

生成摘要时出错

---

## 85. Minecraft: Java Edition 26.2, the first version with Vulkan 1.2

**原文标题**: Minecraft: Java Edition 26.2, the first version with Vulkan 1.2

**原文链接**: [https://www.minecraft.net/en-us/article/minecraft-java-edition-26-2](https://www.minecraft.net/en-us/article/minecraft-java-edition-26-2)

生成摘要时出错

---

## 86. SubQ 1.1 Small

**原文标题**: SubQ 1.1 Small

**原文链接**: [https://subq.ai/subq-1-1-small-technical-report](https://subq.ai/subq-1-1-small-technical-report)

生成摘要时出错

---

## 87. The Amphibious Villagers of Indonesia

**原文标题**: The Amphibious Villagers of Indonesia

**原文链接**: [https://www.economist.com/interactive/1843/2026/06/12/the-amphibious-villagers-of-indonesia](https://www.economist.com/interactive/1843/2026/06/12/the-amphibious-villagers-of-indonesia)

生成摘要时出错

---

## 88. But yak shaving is fun (2019)

**原文标题**: But yak shaving is fun (2019)

**原文链接**: [https://parksb.github.io/en/article/32.html](https://parksb.github.io/en/article/32.html)

生成摘要时出错

---

## 89. All about the IBM 1130 Computing System

**原文标题**: All about the IBM 1130 Computing System

**原文链接**: [http://ibm1130.org/](http://ibm1130.org/)

生成摘要时出错

---

## 90. Making espresso with ultrasound

**原文标题**: Making espresso with ultrasound

**原文链接**: [https://www.unsw.edu.au/newsroom/news/2026/06/New-way-making-espresso](https://www.unsw.edu.au/newsroom/news/2026/06/New-way-making-espresso)

生成摘要时出错

---

## 91. Why stdx is not on crates.io

**原文标题**: Why stdx is not on crates.io

**原文链接**: [https://kerkour.com/stdx-cratesio](https://kerkour.com/stdx-cratesio)

生成摘要时出错

---

## 92. An interview with an Apple emoji designer

**原文标题**: An interview with an Apple emoji designer

**原文链接**: [https://shadycharacters.co.uk/2026/06/ollie-wagner/](https://shadycharacters.co.uk/2026/06/ollie-wagner/)

生成摘要时出错

---

## 93. Chameleon Ultra: a flashdrive sized NFC toolkit

**原文标题**: Chameleon Ultra: a flashdrive sized NFC toolkit

**原文链接**: [https://github.com/RfidResearchGroup/ChameleonUltra](https://github.com/RfidResearchGroup/ChameleonUltra)

生成摘要时出错

---

## 94. The time the x86 emulator team found code so bad they fixed it during emulation

**原文标题**: The time the x86 emulator team found code so bad they fixed it during emulation

**原文链接**: [https://devblogs.microsoft.com/oldnewthing/20260615-00/?p=112419](https://devblogs.microsoft.com/oldnewthing/20260615-00/?p=112419)

生成摘要时出错

---

## 95. Making ast.walk 220x Faster

**原文标题**: Making ast.walk 220x Faster

**原文链接**: [https://reflex.dev/blog/why-ast-walk-when-you-can-ast-sprint/](https://reflex.dev/blog/why-ast-walk-when-you-can-ast-sprint/)

生成摘要时出错

---

## 96. KDE Plasma 6.7 Released

**原文标题**: KDE Plasma 6.7 Released

**原文链接**: [https://lwn.net/Articles/1078160/](https://lwn.net/Articles/1078160/)

生成摘要时出错

---

## 97. Apple is about to make Hide My Email useless

**原文标题**: Apple is about to make Hide My Email useless

**原文链接**: [https://arseniyshestakov.com/2026/06/16/apple-is-about-to-make-hide-my-email-useless/](https://arseniyshestakov.com/2026/06/16/apple-is-about-to-make-hide-my-email-useless/)

生成摘要时出错

---

## 98. TinyWind: A pixel pirate sailing game with real wind physics (380k+ kms sailed)

**原文标题**: TinyWind: A pixel pirate sailing game with real wind physics (380k+ kms sailed)

**原文链接**: [https://tinywind.io](https://tinywind.io)

生成摘要时出错

---

## 99. Feds freaked over Fable 5 after 'fix this code', not jailbreak, say researchers

**原文标题**: Feds freaked over Fable 5 after 'fix this code', not jailbreak, say researchers

**原文链接**: [https://www.theregister.com/security/2026/06/15/feds-freaked-over-fable-5-after-simple-fix-this-code-prompt-not-jailbreak-says-researcher/5255827](https://www.theregister.com/security/2026/06/15/feds-freaked-over-fable-5-after-simple-fix-this-code-prompt-not-jailbreak-says-researcher/5255827)

生成摘要时出错

---

## 100. Understanding the rationale behind a rule when trying to circumvent it

**原文标题**: Understanding the rationale behind a rule when trying to circumvent it

**原文链接**: [https://devblogs.microsoft.com/oldnewthing/20260611-00/?p=112415](https://devblogs.microsoft.com/oldnewthing/20260611-00/?p=112415)

生成摘要时出错

---

