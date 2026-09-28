# Hacker News 热门文章摘要 (2026-09-28)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Jeff – 兼容 Jev 的 0.8B 决策模型，在家训练，约 30 毫秒

**原文标题**: Jeff – Jev-compatible 0.8B decision models, trained at home, ~30 ms

**原文链接**: [https://github.com/firelex/jeff](https://github.com/firelex/jeff)

**Jeff** 是一套小型、高速决策模型系列（参数量为 0.8B 至 2B），专为零样本分类任务设计。Jeff 模型基于 Qwen3.5 和 Gemma 4 构建，兼容 Jev 请求格式，能够通过单次前向传播为用户定义的选项提供校准概率。通过消除文本生成和解析环节，它们实现了极高的效率，在 NVIDIA RTX PRO 6000 或 Apple M4 Max 等本地硬件上的决策处理时间仅需约 22–30 毫秒。

该项目突出了以下几个核心特性：
*   **零样本能力：** 模型可以对多种输入进行分类（如服务工单、用户意图或游戏动作），且无需训练数据中包含这些特定类别。
*   **本地与开放训练：** Jeff 完全在本地硬件上使用开源模型（Qwen-Flash）生成的合成数据构建而成。这是一个利用 MIT 许可的 AutoJev 配方的独立项目，模型权重按 Apache 2.0 协议发布。
*   **性能表现：** 在基准测试中，Jeff 在分类和接地（grounding）任务中的准确率接近甚至超过了体量更大的模型（如 27B 的 AutoJev）。然而，受限于较小的规模，它们在复杂的多步推理方面仍逊于大模型。
*   **专业化能力：** 虽然零样本性能强劲，但在经过简短的特定领域微调后，模型表现尤为出色；一项测试显示，仅需 30 分钟的训练，其准确率就从 31.7% 跃升至 95.8%。

开发者将 Jeff 定位为“系统 1”模型——即非常适合快速、直觉式的判断，而非复杂的规划。建议用户在使用时注意措辞（wording）的影响，并指出 0.8B 模型通常是速度与可靠性的“黄金平衡点”，在游戏等动态环境中，其表现有时甚至优于 2B 版本。

---

## 2. World Labs 加入 AMD

**原文标题**: World Labs Is Joining AMD

**原文链接**: [https://www.worldlabs.ai/blog/amd-announcement](https://www.worldlabs.ai/blog/amd-announcement)

World Labs 宣布已达成加入 AMD 的最终协议，此举旨在加速针对空间与物理世界的 AI 技术开发。此次收购是基于双方去年建立的深度技术合作伙伴关系，该合作专注于优化 AMD GPU 上的模型训练与推理。

关键领导层变动包括 AI 先驱李飞飞博士（Dr. Fei-Fei Li）加入 AMD 担任执行副总裁兼首席科学家，直接向首席执行官苏姿丰博士（Dr. Lisa Su）汇报。联合创始人 Justin Johnson 和 Ben Mildenhall 将继续领导 World Labs 团队，该团队在并入 AMD 后将组建一个新的前沿研究机构。

合并后的实体旨在构建一个涵盖硬件、软件、平台和易于获取的开放模型的全面、开放式 AI 生态系统。通过将 World Labs 的基础模型和应用与 AMD 的硬件能力相结合，两家公司意在更有效地扩展 AI 解决方案。

该交易预计将于 2026 年底完成，但需满足惯例成交条件并获得监管批准。

---

## 3. 紧跟前沿并非AI实验室的真正目标

**原文标题**: Pacing the Frontier is not the actual goal for AI labs

**原文链接**: [https://www.lesswrong.com/posts/Nm4ewbYovtjq69dvH/pacing-the-frontier-is-not-the-actual-goal-for-ai-labs](https://www.lesswrong.com/posts/Nm4ewbYovtjq69dvH/pacing-the-frontier-is-not-the-actual-goal-for-ai-labs)

In the article "Pacing the Frontier is not the actual goal for AI labs," the author argues that the common perception of the "AI race"—where labs compete to marginally outdo each other with incremental releases—is a misunderstanding of their true strategy.

According to the author, "pacing the frontier" (releasing models like GPT-4 or Claude 3) is merely a survival requirement to maintain relevance, secure talent, and attract capital. The actual goal is **discontinuous scaling**: positioning themselves to be the first to leapfrog the current frontier by orders of magnitude.

Key points include:

*   **Infrastructure as the Real Battlefield:** The true competition is not over software tweaks but over the massive physical infrastructure required for the next generation of AI. This includes securing unprecedented amounts of compute (chips), energy, and capital.
*   **The Compute Moat:** Labs are racing to build a "compute moat" so large that once they achieve a breakthrough, competitors will find it physically and financially impossible to catch up. The goal is a decisive, winner-take-all advantage.
*   **Maintenance vs. Breakthrough:** Current releases serve as "proofs of concept" to keep investors interested and to test safety protocols. However, these are just the "phoney war" stage of the race.
*   **Resource Accumulation:** The author suggests that labs are currently in a transition period, accumulating the necessary resources for a massive, non-linear shift in capabilities that will occur once their large-scale data centers are fully operational.

Ultimately, the article suggests that the current steady stream of AI updates masks a much more aggressive underlying race to build the industrial-scale foundation for super-intelligence.

---

## 4. Pirating the Pirates

**原文标题**: Pirating the Pirates

**原文链接**: [https://mubi.com/en/notebook/posts/pirating-the-pirates](https://mubi.com/en/notebook/posts/pirating-the-pirates)

生成摘要时出错

---

## 5. MicroLLM Lab – Try 7 tiny LLM's in the browser

**原文标题**: MicroLLM Lab – Try 7 tiny LLM's in the browser

**原文链接**: [https://stateofutopia.com/experiments/microllmlab/](https://stateofutopia.com/experiments/microllmlab/)

**MicroLLM Lab** 是一个交互式的网页端实验平台，旨在展示完全在用户浏览器中运行的“微型”大语言模型（LLM）的能力。该工具由 State of Utopia 开发，利用 **WebGPU** 技术进行本地推理，这意味着 AI 处理过程是在用户自身的硬件上完成的，而非远程服务器。

该实验室允许用户测试和对比七种不同的微型模型，参数规模通常在 1.35 亿到 5 亿之间。其中的特色模型包括 **SmolLM**、**Qwen2-0.5B** 和 **H2O-Danube** 的各种版本。通过专注于这些小规模模型，该平台证明了 AI 可以兼具实用、高效和私密，因为数据从未离开本地环境。

**核心功能与要点包括：**

*   **本地隐私与速度：** 由于模型通过浏览器的 WebGPU 接口运行，它们能提供低延迟响应，且无需将数据发送到外部 API。
*   **并排对比：** 用户只需输入一个提示词，即可同时查看不同微型模型的响应，从而直观展示模型规模与智能水平之间的权衡。
*   **高效性：** 该实验证明了轻量化模型（SLM）在处理摘要、简单逻辑和创意写作等基础任务方面能力日益增强，且能在笔记本电脑甚至智能手机等标准消费级设备上运行。

总而言之，MicroLLM Lab 为“本地 AI”运动提供了一个极具说服力的概念验证，将关注点从庞大且耗费资源的模型转向了优先考虑用户隐私和易用性的高效、去中心化替代方案。

---

## 6. 1.2万年前的哥贝克力石阵墓葬解释了散落骨骼的成因。

**原文标题**: 12,000-year-old Göbeklitepe burials explain scattered bones

**原文链接**: [https://archaeologymag.com/2026/09/gobeklitepe-burials-hundreds-of-scattered-bones/](https://archaeologymag.com/2026/09/gobeklitepe-burials-hundreds-of-scattered-bones/)

生成摘要时出错

---

## 7. Palantir founder purchases large swath of forest in Sweden

**原文标题**: Palantir founder purchases large swath of forest in Sweden

**原文链接**: [https://www.arctictoday.com/palantir-founder-purchases-large-swath-of-forest-in-sweden/](https://www.arctictoday.com/palantir-founder-purchases-large-swath-of-forest-in-sweden/)

生成摘要时出错

---

## 8. Scientists solve 1840s space weather mystery

**原文标题**: Scientists solve 1840s space weather mystery

**原文链接**: [https://arstechnica.com/science/2026/09/scientists-solve-1840s-space-weather-mystery/](https://arstechnica.com/science/2026/09/scientists-solve-1840s-space-weather-mystery/)

生成摘要时出错

---

## 9. Hijacking the PS5's RTMP stream

**原文标题**: Hijacking the PS5's RTMP stream

**原文链接**: [https://yashgarg.dev/posts/hijacking-ps5-rtmp-stream/](https://yashgarg.dev/posts/hijacking-ps5-rtmp-stream/)

生成摘要时出错

---

## 10. What reversing, modernising old games tells us about the economic impact of AI

**原文标题**: What reversing, modernising old games tells us about the economic impact of AI

**原文链接**: [https://this.os.isfine.org/blog/posts/what-reverse-engineering-and-modernising-an-old-war-game-tells-us-about-the-econ/](https://this.os.isfine.org/blog/posts/what-reverse-engineering-and-modernising-an-old-war-game-tells-us-about-the-econ/)

生成摘要时出错

---

## 11. Joseph Szabo’s pictures of American adolescents

**原文标题**: Joseph Szabo’s pictures of American adolescents

**原文链接**: [https://www.newyorker.com/culture/photo-booth/the-teen-portraits-that-captivated-sofia-coppola](https://www.newyorker.com/culture/photo-booth/the-teen-portraits-that-captivated-sofia-coppola)

生成摘要时出错

---

## 12. It's Time to Investigate the AI Labs

**原文标题**: It's Time to Investigate the AI Labs

**原文链接**: [https://calnewport.com/its-time-to-investigate-the-ai-labs/](https://calnewport.com/its-time-to-investigate-the-ai-labs/)

生成摘要时出错

---

## 13. Sonnet 5.5

**原文标题**: Sonnet 5.5

**原文链接**: [https://www.anthropic.com/claude-sonnet-5-5](https://www.anthropic.com/claude-sonnet-5-5)

生成摘要时出错

---

## 14. Parley: Federated, decentralised chat that speaks plain IRC

**原文标题**: Parley: Federated, decentralised chat that speaks plain IRC

**原文链接**: [https://git.mills.io/prologic/parley](https://git.mills.io/prologic/parley)

生成摘要时出错

---

## 15. Best of British Design

**原文标题**: Best of British Design

**原文链接**: [https://best-of-british-design.vercel.app/](https://best-of-british-design.vercel.app/)

生成摘要时出错

---

## 16. Flock Wants the Most Detailed Map of Its Surveillance Cameras Taken Offline

**原文标题**: Flock Wants the Most Detailed Map of Its Surveillance Cameras Taken Offline

**原文链接**: [https://theintercept.com/2026/09/24/how-many-flock-devices-in-united-states-300000/](https://theintercept.com/2026/09/24/how-many-flock-devices-in-united-states-300000/)

生成摘要时出错

---

## 17. First Steps of the PLC Organization – Independent Public Ledger of Credentials

**原文标题**: First Steps of the PLC Organization – Independent Public Ledger of Credentials

**原文链接**: [https://blog.plcred.org/3mwlphq42d227](https://blog.plcred.org/3mwlphq42d227)

生成摘要时出错

---

## 18. Cf: The Agentic CLI for the Cloudflare API

**原文标题**: Cf: The Agentic CLI for the Cloudflare API

**原文链接**: [https://blog.cloudflare.com/cloudflare-cf-cli-launch/](https://blog.cloudflare.com/cloudflare-cf-cli-launch/)

生成摘要时出错

---

## 19. Launch HN: Vespper (YC F24) – SOTA Docx MCP

**原文标题**: Launch HN: Vespper (YC F24) – SOTA Docx MCP

**原文链接**: [https://www.vespper.com/blog/launching-vespper-docx-mcp](https://www.vespper.com/blog/launching-vespper-docx-mcp)

生成摘要时出错

---

## 20. I made a visual workspace for AI Automations

**原文标题**: I made a visual workspace for AI Automations

**原文链接**: [https://www.biom.dev/](https://www.biom.dev/)

生成摘要时出错

---

## 21. Nvidia wants to put a watchdog chip next to every AI agent

**原文标题**: Nvidia wants to put a watchdog chip next to every AI agent

**原文链接**: [https://www.cnbc.com/2026/09/28/nvidia-releases.html](https://www.cnbc.com/2026/09/28/nvidia-releases.html)

生成摘要时出错

---

## 22. Show HN: Destroy Any Website with Stickman

**原文标题**: Show HN: Destroy Any Website with Stickman

**原文链接**: [https://destroy.spritefusion.com/](https://destroy.spritefusion.com/)

生成摘要时出错

---

## 23. What heraldry and Japanese mon can teach about visual-identity generators

**原文标题**: What heraldry and Japanese mon can teach about visual-identity generators

**原文链接**: [https://benovermyer.com/blog/2026/09/japanese-vs-western-heraldry/](https://benovermyer.com/blog/2026/09/japanese-vs-western-heraldry/)

生成摘要时出错

---

## 24. Who wrote Elizabeth I's most scathing letters?

**原文标题**: Who wrote Elizabeth I's most scathing letters?

**原文链接**: [https://www.smithsonianmag.com/history/who-wrote-elizabeth-is-most-scathing-letters-new-research-suggests-the-tudor-queens-male-secretaries-revised-her-correspondence-to-emphasize-her-temper-180989565/](https://www.smithsonianmag.com/history/who-wrote-elizabeth-is-most-scathing-letters-new-research-suggests-the-tudor-queens-male-secretaries-revised-her-correspondence-to-emphasize-her-temper-180989565/)

生成摘要时出错

---

## 25. MongoDB CEO resigns to join Meta

**原文标题**: MongoDB CEO resigns to join Meta

**原文链接**: [https://www.reuters.com/technology/mongodb-ceo-desai-steps-down-lead-metas-enterprise-platform-2026-09-28/](https://www.reuters.com/technology/mongodb-ceo-desai-steps-down-lead-metas-enterprise-platform-2026-09-28/)

生成摘要时出错

---

## 26. Kids turned low-traffic NPR Spotify comments into a secret group chat

**原文标题**: Kids turned low-traffic NPR Spotify comments into a secret group chat

**原文链接**: [https://www.thisamericanlife.org/897/transcript](https://www.thisamericanlife.org/897/transcript)

生成摘要时出错

---

## 27. GrapheneOS – When an app is slow

**原文标题**: GrapheneOS – When an app is slow

**原文链接**: [https://blog.wirelessmoves.com/2026/09/grapheneos-when-an-app-is-slow.html](https://blog.wirelessmoves.com/2026/09/grapheneos-when-an-app-is-slow.html)

生成摘要时出错

---

## 28. Neal Stephenson responds with wit and humor (2004)

**原文标题**: Neal Stephenson responds with wit and humor (2004)

**原文链接**: [https://slashdot.org/story/04/10/20/1518217/neal-stephenson-responds-with-wit-and-humor](https://slashdot.org/story/04/10/20/1518217/neal-stephenson-responds-with-wit-and-humor)

生成摘要时出错

---

## 29. So long Google, and thanks for all the nudes

**原文标题**: So long Google, and thanks for all the nudes

**原文链接**: [https://lecaro.me/20260921-google-less.html](https://lecaro.me/20260921-google-less.html)

生成摘要时出错

---

## 30. When did Google get so weird?

**原文标题**: When did Google get so weird?

**原文链接**: [https://sancho.bearblog.dev/google-weird/](https://sancho.bearblog.dev/google-weird/)

生成摘要时出错

---

## 31. Windows 11½

**原文标题**: Windows 11½

**原文链接**: [https://definitelynotwindows.com/](https://definitelynotwindows.com/)

生成摘要时出错

---

## 32. 37,500 border drawings: a map of the world as people remember it

**原文标题**: 37,500 border drawings: a map of the world as people remember it

**原文链接**: [https://www.habibicode.org/thedrawnworld](https://www.habibicode.org/thedrawnworld)

生成摘要时出错

---

## 33. I switched to Brave

**原文标题**: I switched to Brave

**原文链接**: [https://kevquirk.com/i-switched-to-brave-browser](https://kevquirk.com/i-switched-to-brave-browser)

生成摘要时出错

---

## 34. Show HN: PaperMono, e-ink fridge magnet shopping list with mobile web page

**原文标题**: Show HN: PaperMono, e-ink fridge magnet shopping list with mobile web page

**原文链接**: [https://github.com/seamusc/papermono-shopping-list](https://github.com/seamusc/papermono-shopping-list)

生成摘要时出错

---

## 35. What would a serious AI product look like?

**原文标题**: What would a serious AI product look like?

**原文链接**: [https://blog.glyph.im/2026/09/serious-ai-product.html](https://blog.glyph.im/2026/09/serious-ai-product.html)

生成摘要时出错

---

## 36. Footguns with Postgres “at time zone 'UTC'”

**原文标题**: Footguns with Postgres “at time zone 'UTC'”

**原文链接**: [https://bookofrevenue.com/blog/6ab81e9a97a13f0001f7e4e1/postgres-at-time-zone-u-does-not-do-what-you-think-it-does](https://bookofrevenue.com/blog/6ab81e9a97a13f0001f7e4e1/postgres-at-time-zone-u-does-not-do-what-you-think-it-does)

生成摘要时出错

---

## 37. Show HN: Free alternative to graphics design giants

**原文标题**: Show HN: Free alternative to graphics design giants

**原文链接**: [https://scissor.studio/](https://scissor.studio/)

生成摘要时出错

---

## 38. SB 923 is Law: CCPA deletion rights now reach third-party data

**原文标题**: SB 923 is Law: CCPA deletion rights now reach third-party data

**原文链接**: [https://www.getprivisy.com/blog/sb-923-ccpa-right-to-delete-signed](https://www.getprivisy.com/blog/sb-923-ccpa-right-to-delete-signed)

生成摘要时出错

---

## 39. Reducing undefined behavior in the C language

**原文标题**: Reducing undefined behavior in the C language

**原文链接**: [https://lwn.net/SubscriberLink/1095811/b9325731ea9b61e0/](https://lwn.net/SubscriberLink/1095811/b9325731ea9b61e0/)

生成摘要时出错

---

## 40. Solving a corn puzzle with CP-SAT

**原文标题**: Solving a corn puzzle with CP-SAT

**原文链接**: [https://thill.me/2026/07/16/corn-puzzle-sat-solver.html](https://thill.me/2026/07/16/corn-puzzle-sat-solver.html)

生成摘要时出错

---

## 41. Scaling Memory Safety: AI-Assisted Rewrites of C/C++ Dependencies to Rust

**原文标题**: Scaling Memory Safety: AI-Assisted Rewrites of C/C++ Dependencies to Rust

**原文链接**: [https://bughunters.google.com/blog/scaling-memory-safety](https://bughunters.google.com/blog/scaling-memory-safety)

生成摘要时出错

---

## 42. Nissan's third generation e-POWER powertrain

**原文标题**: Nissan's third generation e-POWER powertrain

**原文链接**: [https://www.nissan-global.com/EN/INNOVATION/TECHNOLOGY/ARCHIVE/E_POWER_GEN3/](https://www.nissan-global.com/EN/INNOVATION/TECHNOLOGY/ARCHIVE/E_POWER_GEN3/)

生成摘要时出错

---

## 43. GDB 18.1 Released

**原文标题**: GDB 18.1 Released

**原文链接**: [https://sourceware.org/pipermail/gdb/2026-September/052333.html](https://sourceware.org/pipermail/gdb/2026-September/052333.html)

生成摘要时出错

---

## 44. Sober: We Ported Roblox to Linux

**原文标题**: Sober: We Ported Roblox to Linux

**原文链接**: [https://sober.vinegarhq.org/](https://sober.vinegarhq.org/)

生成摘要时出错

---

## 45. Thinking fast and slow in AI: The role of metacognition (2021)

**原文标题**: Thinking fast and slow in AI: The role of metacognition (2021)

**原文链接**: [https://arxiv.org/abs/2110.01834](https://arxiv.org/abs/2110.01834)

生成摘要时出错

---

## 46. The problem is not AI code, but not knowing about system architecture or intent

**原文标题**: The problem is not AI code, but not knowing about system architecture or intent

**原文链接**: [https://www.ssp.sh/brain/the-problem-is-not-the-ai-code-but-nobody-knows-anything-anymore/](https://www.ssp.sh/brain/the-problem-is-not-the-ai-code-but-nobody-knows-anything-anymore/)

生成摘要时出错

---

## 47. Coding Is Not Solved

**原文标题**: Coding Is Not Solved

**原文链接**: [https://blog.alexewerlof.com/p/coding-is-not-solved](https://blog.alexewerlof.com/p/coding-is-not-solved)

生成摘要时出错

---

## 48. Headed for the Exit: The Great Engineering Leader Career Break

**原文标题**: Headed for the Exit: The Great Engineering Leader Career Break

**原文链接**: [https://newsletter.pragmaticengineer.com/p/the-great-engineering-leader-career-break](https://newsletter.pragmaticengineer.com/p/the-great-engineering-leader-career-break)

生成摘要时出错

---

## 49. AMD Acquires Dr. Fei Fei Li's World Labs

**原文标题**: AMD Acquires Dr. Fei Fei Li's World Labs

**原文链接**: [https://twitter.com/drfeifei/status/2104664403681632453](https://twitter.com/drfeifei/status/2104664403681632453)

生成摘要时出错

---

## 50. Full Self Hauling: Volvo moves 3 million tonnes of Earth, autonomously

**原文标题**: Full Self Hauling: Volvo moves 3 million tonnes of Earth, autonomously

**原文链接**: [https://electrek.co/2026/09/28/full-self-hauling-volvo-moves-3-million-tonnes-of-earth-autonomously/](https://electrek.co/2026/09/28/full-self-hauling-volvo-moves-3-million-tonnes-of-earth-autonomously/)

生成摘要时出错

---

## 51. Show HN: HN.watch – Videos of all Hacker News posts

**原文标题**: Show HN: HN.watch – Videos of all Hacker News posts

**原文链接**: [https://hn.watch/](https://hn.watch/)

生成摘要时出错

---

## 52. A Staff Engineer's Guide to Inventing Work

**原文标题**: A Staff Engineer's Guide to Inventing Work

**原文链接**: [https://sujithjay.com/inventing-work](https://sujithjay.com/inventing-work)

生成摘要时出错

---

## 53. It's not just the f*cking sandbox

**原文标题**: It's not just the f*cking sandbox

**原文链接**: [https://x.com/joedaroo/article/2104335929293127851](https://x.com/joedaroo/article/2104335929293127851)

生成摘要时出错

---

## 54. OpenAI still doesn't seem to have a handle on all of its rogue AI activity

**原文标题**: OpenAI still doesn't seem to have a handle on all of its rogue AI activity

**原文链接**: [https://techcrunch.com/2026/09/28/openai-still-doesnt-seem-to-have-a-handle-on-all-of-its-rogue-ai-activity/](https://techcrunch.com/2026/09/28/openai-still-doesnt-seem-to-have-a-handle-on-all-of-its-rogue-ai-activity/)

生成摘要时出错

---

## 55. Where's the "Intelligence Explosion"?

**原文标题**: Where's the "Intelligence Explosion"?

**原文链接**: [https://www.noahpinion.blog/p/wheres-the-intelligence-explosion](https://www.noahpinion.blog/p/wheres-the-intelligence-explosion)

生成摘要时出错

---

## 56. RRSI: Regularized Recursive Self-Improvement of Agent Harnesses

**原文标题**: RRSI: Regularized Recursive Self-Improvement of Agent Harnesses

**原文链接**: [https://github.com/google-research/rrsi](https://github.com/google-research/rrsi)

生成摘要时出错

---

## 57. Functional Mechanical Sympathy [video]

**原文标题**: Functional Mechanical Sympathy [video]

**原文链接**: [https://www.youtube.com/watch?v=jSHmDnUZCm8](https://www.youtube.com/watch?v=jSHmDnUZCm8)

生成摘要时出错

---

## 58. N.Y.P.D. Officers Used Flock Safety to Track License Plates Without a Contract

**原文标题**: N.Y.P.D. Officers Used Flock Safety to Track License Plates Without a Contract

**原文链接**: [https://www.nytimes.com/2026/09/28/nyregion/nyc-flock-nypd-surveillance-cameras.html](https://www.nytimes.com/2026/09/28/nyregion/nyc-flock-nypd-surveillance-cameras.html)

生成摘要时出错

---

## 59. We Can't Let Enormous Weirdos Regulate AI

**原文标题**: We Can't Let Enormous Weirdos Regulate AI

**原文链接**: [https://little-flying-robots.ghost.io/why-we-cant-let-enormous-weirdos-regulate-ai/](https://little-flying-robots.ghost.io/why-we-cant-let-enormous-weirdos-regulate-ai/)

生成摘要时出错

---

## 60. Ember-1

**原文标题**: Ember-1

**原文链接**: [https://fireworks.ai/blog/ember-1](https://fireworks.ai/blog/ember-1)

生成摘要时出错

---

## 61. Man Says Meta's Muse AI Gave His Home Address Out to Strangers

**原文标题**: Man Says Meta's Muse AI Gave His Home Address Out to Strangers

**原文链接**: [https://futurism.com/artificial-intelligence/metas-muse-ai-giving-users-home-addresses](https://futurism.com/artificial-intelligence/metas-muse-ai-giving-users-home-addresses)

生成摘要时出错

---

## 62. Owed a billion dollars in Nvidia stock

**原文标题**: Owed a billion dollars in Nvidia stock

**原文链接**: [https://colo.to/nvidia-stock-narrative.html](https://colo.to/nvidia-stock-narrative.html)

生成摘要时出错

---

## 63. Made by Mechanical Means

**原文标题**: Made by Mechanical Means

**原文链接**: [https://felixrieseberg.com/made-by-mechanical-means/](https://felixrieseberg.com/made-by-mechanical-means/)

生成摘要时出错

---

## 64. Imp is a full port of DSPy to the BEAM

**原文标题**: Imp is a full port of DSPy to the BEAM

**原文链接**: [https://github.com/deepfates/imp](https://github.com/deepfates/imp)

生成摘要时出错

---

## 65. Schools are experimenting with AI with little evidence or policy to guide them

**原文标题**: Schools are experimenting with AI with little evidence or policy to guide them

**原文链接**: [https://www.npr.org/2026/09/28/nx-s1-5759718/ai-schools-experiment-research](https://www.npr.org/2026/09/28/nx-s1-5759718/ai-schools-experiment-research)

生成摘要时出错

---

## 66. What I did at Recurse Center

**原文标题**: What I did at Recurse Center

**原文链接**: [https://thill.me/2026/09/11/what-i-did-at-rc.html](https://thill.me/2026/09/11/what-i-did-at-rc.html)

生成摘要时出错

---

## 67. GrapheneOS Picks Motorola Signature 27 as Its First Non-Pixel Phone

**原文标题**: GrapheneOS Picks Motorola Signature 27 as Its First Non-Pixel Phone

**原文链接**: [https://www.extremetech.com/mobile/grapheneos-picks-motorola-signature-27-as-its-first-non-pixel-phone](https://www.extremetech.com/mobile/grapheneos-picks-motorola-signature-27-as-its-first-non-pixel-phone)

生成摘要时出错

---

## 68. Helion Moves Goalpost on Fusion

**原文标题**: Helion Moves Goalpost on Fusion

**原文链接**: [https://www.axios.com/local/seattle/2026/09/28/helion-energy-orion-fusion-microsoft-commercial-power-altman](https://www.axios.com/local/seattle/2026/09/28/helion-energy-orion-fusion-microsoft-commercial-power-altman)

生成摘要时出错

---

## 69. Reading’s Bayeux Tapestry

**原文标题**: Reading’s Bayeux Tapestry

**原文链接**: [https://diamondgeezer.blogspot.com/2026/09/readings-bayeux-tapestry.html](https://diamondgeezer.blogspot.com/2026/09/readings-bayeux-tapestry.html)

生成摘要时出错

---

## 70. Writing Efficient C++ Code (2013)

**原文标题**: Writing Efficient C++ Code (2013)

**原文链接**: [https://asawicki.info/articles/writing_efficient_cpp_code.php](https://asawicki.info/articles/writing_efficient_cpp_code.php)

生成摘要时出错

---

## 71. Deterministic Concurrency [video]

**原文标题**: Deterministic Concurrency [video]

**原文链接**: [https://www.youtube.com/watch?v=25x0UuSCKuU](https://www.youtube.com/watch?v=25x0UuSCKuU)

生成摘要时出错

---

## 72. Show HN: Lofi Cities – Pixel-art city nights with browser-generated lofi

**原文标题**: Show HN: Lofi Cities – Pixel-art city nights with browser-generated lofi

**原文链接**: [https://loficities.com/](https://loficities.com/)

生成摘要时出错

---

## 73. 13 Months Sober (2025)

**原文标题**: 13 Months Sober (2025)

**原文链接**: [https://www.bobbytables.io/p/13-months-sober](https://www.bobbytables.io/p/13-months-sober)

生成摘要时出错

---

## 74. AMD Acquires Fei-Fei Li's World Labs for $8.2B

**原文标题**: AMD Acquires Fei-Fei Li's World Labs for $8.2B

**原文链接**: [https://ir.amd.com/news-events/press-releases/detail/1299/amd-to-acquire-world-labs-to-advance-the-future-of-ai-compute](https://ir.amd.com/news-events/press-releases/detail/1299/amd-to-acquire-world-labs-to-advance-the-future-of-ai-compute)

生成摘要时出错

---

## 75. Self-Hosting on the Dark Web

**原文标题**: Self-Hosting on the Dark Web

**原文链接**: [https://david.alvarezrosa.com/posts/self-hosting-on-the-dark-web/](https://david.alvarezrosa.com/posts/self-hosting-on-the-dark-web/)

生成摘要时出错

---

## 76. Calling the AI bluff: Adding "Do not guess" cut made-up claims from 71% to 20%

**原文标题**: Calling the AI bluff: Adding "Do not guess" cut made-up claims from 71% to 20%

**原文链接**: [https://earnanhonestdollar.com/bench](https://earnanhonestdollar.com/bench)

生成摘要时出错

---

## 77. Oral history of John Chowning, inventor of FM synthesis [video]

**原文标题**: Oral history of John Chowning, inventor of FM synthesis [video]

**原文链接**: [https://www.youtube.com/watch?v=e1Xn3030IvM](https://www.youtube.com/watch?v=e1Xn3030IvM)

生成摘要时出错

---

## 78. Deshittification Part 2: Bypassing the App Store Gatekeeper

**原文标题**: Deshittification Part 2: Bypassing the App Store Gatekeeper

**原文链接**: [https://fabricati-diem.inform.social/post/deshittification-as-a-service-part2-bypassing-the-app-store-gatekeeper/](https://fabricati-diem.inform.social/post/deshittification-as-a-service-part2-bypassing-the-app-store-gatekeeper/)

生成摘要时出错

---

## 79. 2026 in LLMs (So Far)

**原文标题**: 2026 in LLMs (So Far)

**原文链接**: [https://simonw.substack.com/p/2026-in-llms-so-far](https://simonw.substack.com/p/2026-in-llms-so-far)

生成摘要时出错

---

## 80. European industry is doing better than you may think

**原文标题**: European industry is doing better than you may think

**原文链接**: [https://www.economist.com/business/2026/09/27/european-industry-is-doing-better-than-you-may-think](https://www.economist.com/business/2026/09/27/european-industry-is-doing-better-than-you-may-think)

生成摘要时出错

---

## 81. Protest Against European Parliament Chat Control 1.0 Legislation in Warsaw

**原文标题**: Protest Against European Parliament Chat Control 1.0 Legislation in Warsaw

**原文链接**: [https://www.reutersconnect.com/item/protest-against-european-parliament-chat-control-10-legislation-in-warsaw-poland-26-sep-2026/dGFnOnJldXRlcnMuY29tLDIwMjY6bmV3c21sX01UMVNPUEEwMDA3UVVNMFQ](https://www.reutersconnect.com/item/protest-against-european-parliament-chat-control-10-legislation-in-warsaw-poland-26-sep-2026/dGFnOnJldXRlcnMuY29tLDIwMjY6bmV3c21sX01UMVNPUEEwMDA3UVVNMFQ)

生成摘要时出错

---

## 82. First DVD player announced Sept 26, 1996

**原文标题**: First DVD player announced Sept 26, 1996

**原文链接**: [https://dfarq.homeip.net/first-dvd-player-announced-sept-26-1996/](https://dfarq.homeip.net/first-dvd-player-announced-sept-26-1996/)

生成摘要时出错

---

## 83. Malleable software: Restoring user agency in a world of locked-down apps (2025)

**原文标题**: Malleable software: Restoring user agency in a world of locked-down apps (2025)

**原文链接**: [https://www.inkandswitch.com/essay/malleable-software/](https://www.inkandswitch.com/essay/malleable-software/)

生成摘要时出错

---

## 84. The Cartesian Hand: In-Hand Manipulation with All-Linear Fingers

**原文标题**: The Cartesian Hand: In-Hand Manipulation with All-Linear Fingers

**原文链接**: [https://generalroboticslab.com/cartesian_handv1](https://generalroboticslab.com/cartesian_handv1)

生成摘要时出错

---

## 85. How Pew Research Center is – and is not – using AI in our work

**原文标题**: How Pew Research Center is – and is not – using AI in our work

**原文链接**: [https://www.pewresearch.org/decoded/2026/09/28/how-pew-research-center-is-and-is-not-using-ai-in-our-work-2/](https://www.pewresearch.org/decoded/2026/09/28/how-pew-research-center-is-and-is-not-using-ai-in-our-work-2/)

生成摘要时出错

---

## 86. Packing Binary Is Fun

**原文标题**: Packing Binary Is Fun

**原文链接**: [https://hereticpleb.vercel.app/blog/packing-binary-is-fun-actually](https://hereticpleb.vercel.app/blog/packing-binary-is-fun-actually)

生成摘要时出错

---

## 87. Improving site performance by shipping more CSS

**原文标题**: Improving site performance by shipping more CSS

**原文链接**: [https://github.blog/engineering/architecture-optimization/improving-site-performance-by-shipping-more-css/](https://github.blog/engineering/architecture-optimization/improving-site-performance-by-shipping-more-css/)

生成摘要时出错

---

## 88. AMD acquiring Fei-Fei Li's World Labs AI firm in deal worth $8.2B

**原文标题**: AMD acquiring Fei-Fei Li's World Labs AI firm in deal worth $8.2B

**原文链接**: [https://www.cnbc.com/2026/09/28/amd-fei-fei-li-world-labs.html](https://www.cnbc.com/2026/09/28/amd-fei-fei-li-world-labs.html)

生成摘要时出错

---

## 89. Video CDs Break Windows Explorer

**原文标题**: Video CDs Break Windows Explorer

**原文链接**: [https://clydesnotes.blogspot.com/2026/08/video-cds-break-windows-explorer.html](https://clydesnotes.blogspot.com/2026/08/video-cds-break-windows-explorer.html)

生成摘要时出错

---

## 90. Fakecloud: Local AWS cloud emulator for integration tests

**原文标题**: Fakecloud: Local AWS cloud emulator for integration tests

**原文链接**: [https://fakecloud.dev/](https://fakecloud.dev/)

生成摘要时出错

---

## 91. The Netherlands is rolling its own NixOS-based software stack after U.S.

**原文标题**: The Netherlands is rolling its own NixOS-based software stack after U.S.

**原文链接**: [https://www.tomshardware.com/software/the-netherlands-is-rolling-alternative-nixos-based-software-ecosystem-after-u-s-sanctions-on-icc-took-microsoft-off-the-table-trial-programs-running-now-first-release-expected-at-end-of-2027](https://www.tomshardware.com/software/the-netherlands-is-rolling-alternative-nixos-based-software-ecosystem-after-u-s-sanctions-on-icc-took-microsoft-off-the-table-trial-programs-running-now-first-release-expected-at-end-of-2027)

生成摘要时出错

---

## 92. Alan Kay's answer to “Did the ENIAC have a BIOS”?

**原文标题**: Alan Kay's answer to “Did the ENIAC have a BIOS”?

**原文链接**: [https://www.quora.com/Did-the-ENIAC-have-a-BIOS/answer/Alan-Kay-11](https://www.quora.com/Did-the-ENIAC-have-a-BIOS/answer/Alan-Kay-11)

生成摘要时出错

---

## 93. Guitar amp and effects pedal built on the Waveshare ESP32-S3-Touch-AMOLED-2.06

**原文标题**: Guitar amp and effects pedal built on the Waveshare ESP32-S3-Touch-AMOLED-2.06

**原文链接**: [https://github.com/dashersw/coyopedal](https://github.com/dashersw/coyopedal)

生成摘要时出错

---

## 94. Fragment of oldest known peace treaty found in Turkey

**原文标题**: Fragment of oldest known peace treaty found in Turkey

**原文链接**: [https://www.livescience.com/archaeology/ancient-egyptians/we-have-found-traces-of-peace-thousands-of-years-old-fragment-of-worlds-oldest-known-peace-treaty-found-in-turkey](https://www.livescience.com/archaeology/ancient-egyptians/we-have-found-traces-of-peace-thousands-of-years-old-fragment-of-worlds-oldest-known-peace-treaty-found-in-turkey)

生成摘要时出错

---

## 95. Faster prompt lookup drafting in llama.cpp

**原文标题**: Faster prompt lookup drafting in llama.cpp

**原文链接**: [https://jadidbourbaki.github.io/blog/prompt-lookup-llama-cpp/](https://jadidbourbaki.github.io/blog/prompt-lookup-llama-cpp/)

生成摘要时出错

---

## 96. C's Flexible Integer Sizes Were Not a Design Mistake

**原文标题**: C's Flexible Integer Sizes Were Not a Design Mistake

**原文链接**: [https://pikuma.com/blog/c-integer-sizes-not-a-mistake](https://pikuma.com/blog/c-integer-sizes-not-a-mistake)

生成摘要时出错

---

## 97. A New Experiment Meta-Strategy

**原文标题**: A New Experiment Meta-Strategy

**原文链接**: [https://chillphysicsenjoyer.substack.com/p/a-new-experiment-meta-strategy](https://chillphysicsenjoyer.substack.com/p/a-new-experiment-meta-strategy)

生成摘要时出错

---

## 98. Prompting Claude Opus 5.5

**原文标题**: Prompting Claude Opus 5.5

**原文链接**: [https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5)

生成摘要时出错

---

## 99. Bodhana Sivanandan, 11, becomes youngest woman grandmaster

**原文标题**: Bodhana Sivanandan, 11, becomes youngest woman grandmaster

**原文链接**: [https://www.bbc.co.uk/news/articles/cqwyzrg7xm2zo](https://www.bbc.co.uk/news/articles/cqwyzrg7xm2zo)

生成摘要时出错

---

## 100. The state of SIMD in Rust in 2026

**原文标题**: The state of SIMD in Rust in 2026

**原文链接**: [https://shnatsel.github.io/state-of-simd-rust-2026/](https://shnatsel.github.io/state-of-simd-rust-2026/)

生成摘要时出错

---

