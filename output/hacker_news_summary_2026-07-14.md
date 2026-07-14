# Hacker News 热门文章摘要 (2026-07-14)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Linux 输入延迟测试：X11 vs. Wayland、VRR 和 DXVK

**原文标题**: Measuring Input Latency on Linux: X11 vs. Wayland, VRR, and DXVK

**原文链接**: [https://marco-nett.de/blog/measuring-input-latency-on-linux-x11-vs-wayland-vrr-dxvk/](https://marco-nett.de/blog/measuring-input-latency-on-linux-x11-vs-wayland-vrr-dxvk/)

本文详细介绍了一项针对 Linux 游戏性能的技术调查。作者使用自制的硬件延迟测量仪，旨在摆脱“安慰剂”式的优化，精确测量端到端系统延迟。在 500Hz 的高端硬件环境下，作者对比了 X11 与 Wayland 的表现、可变刷新率（VRR）的影响，以及 `dxvk-low-latency` 分支的实际效果。

**主要发现：**

*   **XWayland 是最大元凶：** 最显著的发现是，通过 XWayland 运行游戏会增加约 **3.13ms** 的延迟。仅此一项的影响就超过了几乎所有其他优化手段的总和。
*   **X11 对比原生 Wayland：** 虽然 X11 在技术上稍快，但领先幅度微乎其微（0.14ms 至 0.22ms）。原生 Wayland 表现出极强的竞争力，打破了其天生不适合竞技游戏的传言。
*   **VRR 效果显著：** 开启 VRR（G-Sync/FreeSync）能稳定降低 **0.26ms 至 0.45ms** 的延迟。更重要的是，它通过收窄帧交付时间的分布（减少抖动）显著提升了稳定性。
*   **DXVK Low-Latency 的优势：** `dxvk-low-latency` 分支带来了持续的性能提升。虽然在限帧场景下收益较小，但在不限帧的情况下，它通过防止渲染队列积压并确保 GPU 不至于完全饱和，使延迟降低了 **0.84ms**。

**结论：**

若要在 Linux 上获得最低延迟，作者建议**务必避免使用 XWayland**，应选择原生 Wayland 协议或 X11。虽然在理想条件下，叠加所有优化手段（X11、VRR 及 DXVK 分支）的总收益仅约为 **0.72ms**，但这些设置通过提供更稳定的帧生成时间和减少实际游戏中的延迟波动，显著改善了操作的“手感”。

---

## 2. 高塔仍在攀升

**原文标题**: The Tower Keeps Rising

**原文链接**: [https://lucumr.pocoo.org/2026/7/13/the-tower-keeps-rising/](https://lucumr.pocoo.org/2026/7/13/the-tower-keeps-rising/)

In "The Tower Keeps Rising," Armin Ronacher explores the impact of AI agents on software development through the lens of the Tower of Babel. While the biblical story suggests that the loss of a shared language halts progress, Ronacher argues that AI-assisted programming creates a different, more disorienting outcome: construction continues even after collective human understanding has collapsed.

The core of Ronacher’s argument is that large-scale software projects rely less on individual coding speed and more on a "shared language"—a common mental model of system boundaries, invariants, and architectural goals. Historically, this shared understanding was maintained by the "friction" of human collaboration. Processes like code reviews and technical debates forced developers to synchronize their knowledge and agree on how a system should function.

AI agents remove this friction. They allow developers to execute complex changes across a codebase without needing to consult others or fully grasp the underlying system logic. While this increases individual productivity, it erodes the shared architectural language that allows humans to reason about the project together. 

The result is "vibecoded" software: a codebase where changes are landed continuously by "tireless translators," but the internal coherence disappears. Unlike the ruins of Babel, these digital towers do not fall; they keep rising. Ronacher warns that the lack of an immediate failure makes this trend dangerous, as it masks the fact that the humans involved no longer truly understand the structure they are building. The system continues to grow, but the architectural language required to manage it is lost.

---

## 3. Your 'app' could have been a webpage (so I fixed it for you)

**原文标题**: Your 'app' could have been a webpage (so I fixed it for you)

**原文链接**: [https://danq.me/2026/07/09/your-app-could-have-been-a-webpage/](https://danq.me/2026/07/09/your-app-could-have-been-a-webpage/)

生成摘要时出错

---

## 4. S&P downgrades Oracle to BBB – only one notch above junk level

**原文标题**: S&P downgrades Oracle to BBB – only one notch above junk level

**原文链接**: [https://www.heise.de/en/news/S-P-downgrades-Oracle-to-BBB-only-one-notch-above-junk-level-11363472.html](https://www.heise.de/en/news/S-P-downgrades-Oracle-to-BBB-only-one-notch-above-junk-level-11363472.html)

生成摘要时出错

---

## 5. How to stop Claude from saying load-bearing

**原文标题**: How to stop Claude from saying load-bearing

**原文链接**: [https://jola.dev/posts/how-to-stop-claude-from-saying-load-bearing](https://jola.dev/posts/how-to-stop-claude-from-saying-load-bearing)

生成摘要时出错

---

## 6. Show HN: Opening lines of famous literary works

**原文标题**: Show HN: Opening lines of famous literary works

**原文链接**: [https://www.verbaprima.com/](https://www.verbaprima.com/)

生成摘要时出错

---

## 7. Launch HN: Agnost AI (YC S26) – Extract user feedback from agent conversations

**原文标题**: Launch HN: Agnost AI (YC S26) – Extract user feedback from agent conversations

**原文链接**: [https://agnost.ai](https://agnost.ai)

生成摘要时出错

---

## 8. Kontigo (YC S24) Is Hiring (Head of Security)

**原文标题**: Kontigo (YC S24) Is Hiring (Head of Security)

**原文链接**: [https://www.ycombinator.com/companies/kontigo/jobs/uNttrlv-head-of-security](https://www.ycombinator.com/companies/kontigo/jobs/uNttrlv-head-of-security)

生成摘要时出错

---

## 9. Are we offloading too much of our thinking to AI?

**原文标题**: Are we offloading too much of our thinking to AI?

**原文链接**: [https://www.artfish.ai/p/offloading-thinking-to-ai](https://www.artfish.ai/p/offloading-thinking-to-ai)

生成摘要时出错

---

## 10. The zero-cost fallacy: open-source software in the agentic era

**原文标题**: The zero-cost fallacy: open-source software in the agentic era

**原文链接**: [https://www.thoughtworks.com/insights/blog/open-source/zero-cost-fallacy-open-source-agentic-era](https://www.thoughtworks.com/insights/blog/open-source/zero-cost-fallacy-open-source-agentic-era)

生成摘要时出错

---

## 11. A tiny cell that broke a big rule of biology

**原文标题**: A tiny cell that broke a big rule of biology

**原文链接**: [https://grist.org/science/nitrogen-cycle-cell-discovery-nitroplast-science-fertilizer-algae-bacteria/](https://grist.org/science/nitrogen-cycle-cell-discovery-nitroplast-science-fertilizer-algae-bacteria/)

生成摘要时出错

---

## 12. Beautiful Type Erasure with C++26 Reflection

**原文标题**: Beautiful Type Erasure with C++26 Reflection

**原文链接**: [https://ryanjk5.github.io/posts/rjk-duck/](https://ryanjk5.github.io/posts/rjk-duck/)

生成摘要时出错

---

## 13. Paxos Made Simple (2001)[pdf]

**原文标题**: Paxos Made Simple (2001)[pdf]

**原文链接**: [https://lamport.azurewebsites.net/pubs/paxos-simple.pdf](https://lamport.azurewebsites.net/pubs/paxos-simple.pdf)

生成摘要时出错

---

## 14. Show HN: I RL-trained an agent that trains models with RL (for –$1.3k)

**原文标题**: Show HN: I RL-trained an agent that trains models with RL (for –$1.3k)

**原文链接**: [https://github.com/Danau5tin/ai-trains-ai](https://github.com/Danau5tin/ai-trains-ai)

生成摘要时出错

---

## 15. Punch yourself in the face with reality

**原文标题**: Punch yourself in the face with reality

**原文链接**: [https://adi.bio/reality](https://adi.bio/reality)

生成摘要时出错

---

## 16. Superoptimizer – A Look at the Smallest Program

**原文标题**: Superoptimizer – A Look at the Smallest Program

**原文链接**: [https://dl.acm.org/doi/epdf/10.1145/36177.36194](https://dl.acm.org/doi/epdf/10.1145/36177.36194)

生成摘要时出错

---

## 17. European "age verification" "app" forcing everyone to use Android or iOS

**原文标题**: European "age verification" "app" forcing everyone to use Android or iOS

**原文链接**: [https://github.com/eu-digital-identity-wallet/av-doc-technical-specification/discussions/19](https://github.com/eu-digital-identity-wallet/av-doc-technical-specification/discussions/19)

生成摘要时出错

---

## 18. The Agentic Loop: Three loops in a trench coat

**原文标题**: The Agentic Loop: Three loops in a trench coat

**原文链接**: [https://www.bobbytables.io/p/the-agentic-loop-three-loops-in-a](https://www.bobbytables.io/p/the-agentic-loop-three-loops-in-a)

生成摘要时出错

---

## 19. How the FSF sysadmins block botnets with reaction

**原文标题**: How the FSF sysadmins block botnets with reaction

**原文链接**: [https://www.fsf.org/blogs/community/blocking-botnets-with-reaction](https://www.fsf.org/blogs/community/blocking-botnets-with-reaction)

生成摘要时出错

---

## 20. Show HN: Juggler – an open-source GUI coding agent, by the creator of JUCE

**原文标题**: Show HN: Juggler – an open-source GUI coding agent, by the creator of JUCE

**原文链接**: [https://github.com/juggler-ai/juggler](https://github.com/juggler-ai/juggler)

生成摘要时出错

---

## 21. Australian energy retailers must provide three hours of free daytime electricity

**原文标题**: Australian energy retailers must provide three hours of free daytime electricity

**原文链接**: [https://lenergy.com.au/free-daytime-electricity-is-coming-heres-how-it-actually-works/](https://lenergy.com.au/free-daytime-electricity-is-coming-heres-how-it-actually-works/)

生成摘要时出错

---

## 22. A metallurgist's doubts about self-replicating probes

**原文标题**: A metallurgist's doubts about self-replicating probes

**原文链接**: [https://www.centauri-dreams.org/2026/07/10/a-metallurgists-doubts-about-self-replicating-probes/](https://www.centauri-dreams.org/2026/07/10/a-metallurgists-doubts-about-self-replicating-probes/)

生成摘要时出错

---

## 23. Alternative(s) to run CUDA on non-Nvidia hardware

**原文标题**: Alternative(s) to run CUDA on non-Nvidia hardware

**原文链接**: [https://www.hpcwire.com/2026/07/09/spectral-compute-aims-to-set-cuda-free-will-it-succeed/](https://www.hpcwire.com/2026/07/09/spectral-compute-aims-to-set-cuda-free-will-it-succeed/)

生成摘要时出错

---

## 24. Our Amish Language

**原文标题**: Our Amish Language

**原文链接**: [https://www.thedial.world/articles/news/amish-pennsylvania-dutch](https://www.thedial.world/articles/news/amish-pennsylvania-dutch)

In “Our Amish Language,” Eythana Miller explores the decline of Pennsylvania Dutch (Deitsch) within her modernizing community in Libby, Montana. Founded in 1992 as a traditional but spiritually open community, Libby eventually relaxed its rules on clothing and technology, leading to a gradual shift from Deitsch to English.

Now a student at UC Berkeley, Miller reflects on the "image problem" and internalized stigma surrounding her mother tongue. Historically, Pennsylvania Dutch has been dismissed by both outsiders and its own speakers as a “miserably broken mishmash” or “wrong German.” Miller challenges these perceptions by citing linguistic scholarship which argues that the distinction between a “dialect” and a “language” is often based on social status and political recognition rather than linguistic validity. 

To preserve the language and document her community’s transition, Miller launched an oral history project, recording dozens of hours of video interviews in Deitsch. She notes that the language is primarily oral and functional, reflecting the physical nature of her ancestors' lives. However, this practicality comes at a cost; the language lacks abstract vocabulary—such as a distinct word for “love”—and is increasingly being supplanted by English loanwords. 

Ultimately, Miller’s work serves as both a repository for a fading culture and a personal journey to reframe her heritage. By recording native speakers and acknowledging the language's legitimacy, she seeks to honor a mother tongue that is being slowly erased by the pressures of modernization and the dominance of English.

---

## 25. Indian scientists produce most detailed 3D atlas of the human brainstem

**原文标题**: Indian scientists produce most detailed 3D atlas of the human brainstem

**原文链接**: [https://www.bbc.com/news/articles/cg53l737v1qo](https://www.bbc.com/news/articles/cg53l737v1qo)

生成摘要时出错

---

## 26. Germany set to restrict its Freedom of Information Act

**原文标题**: Germany set to restrict its Freedom of Information Act

**原文链接**: [https://www.dw.com/en/germany-freedom-of-information-act/a-77939695](https://www.dw.com/en/germany-freedom-of-information-act/a-77939695)

生成摘要时出错

---

## 27. The git history command

**原文标题**: The git history command

**原文链接**: [https://lalitm.com/post/git-history/](https://lalitm.com/post/git-history/)

生成摘要时出错

---

## 28. No Spanish reading crisis?

**原文标题**: No Spanish reading crisis?

**原文链接**: [https://www.commonreader.co.uk/p/no-spanish-reading-crisis](https://www.commonreader.co.uk/p/no-spanish-reading-crisis)

生成摘要时出错

---

## 29. Differentiable Fortran with LFortran and Enzyme

**原文标题**: Differentiable Fortran with LFortran and Enzyme

**原文链接**: [https://docs.pasteurlabs.ai/projects/tesseract-core/latest/blog/2026-07-09-enzyme-lfortran-autodiff.html](https://docs.pasteurlabs.ai/projects/tesseract-core/latest/blog/2026-07-09-enzyme-lfortran-autodiff.html)

生成摘要时出错

---

## 30. Satellite Tracker – Live Map of Starlink and 30k Satellites

**原文标题**: Satellite Tracker – Live Map of Starlink and 30k Satellites

**原文链接**: [https://satellitemap.space/](https://satellitemap.space/)

生成摘要时出错

---

## 31. Tensor Is the Might

**原文标题**: Tensor Is the Might

**原文链接**: [https://zserge.com/posts/tensor/](https://zserge.com/posts/tensor/)

生成摘要时出错

---

## 32. What did SFFA vs. Harvard reveal about admissions?

**原文标题**: What did SFFA vs. Harvard reveal about admissions?

**原文链接**: [https://sorting-machine.pages.dev/](https://sorting-machine.pages.dev/)

生成摘要时出错

---

## 33. Codex starts encrypting sub-agent prompts

**原文标题**: Codex starts encrypting sub-agent prompts

**原文链接**: [https://github.com/openai/codex/issues/28058](https://github.com/openai/codex/issues/28058)

生成摘要时出错

---

## 34. Actegories

**原文标题**: Actegories

**原文链接**: [https://bartoszmilewski.com/2026/06/30/actegories/](https://bartoszmilewski.com/2026/06/30/actegories/)

生成摘要时出错

---

## 35. Agnes Callard’s theory of the uni-context

**原文标题**: Agnes Callard’s theory of the uni-context

**原文链接**: [https://www.derekthompson.org/p/a-philosophers-one-word-theory-to](https://www.derekthompson.org/p/a-philosophers-one-word-theory-to)

生成摘要时出错

---

## 36. IBM Stock has worst day

**原文标题**: IBM Stock has worst day

**原文链接**: [https://www.cnn.com/2026/07/14/tech/ibm-stock-worst-day-ever](https://www.cnn.com/2026/07/14/tech/ibm-stock-worst-day-ever)

生成摘要时出错

---

## 37. YouTrackDB is a general-use object-oriented graph database

**原文标题**: YouTrackDB is a general-use object-oriented graph database

**原文链接**: [https://github.com/JetBrains/youtrackdb](https://github.com/JetBrains/youtrackdb)

生成摘要时出错

---

## 38. Just Let Me Write Digits

**原文标题**: Just Let Me Write Digits

**原文链接**: [https://gendx.dev/blog/2026/07/13/input-digits.html](https://gendx.dev/blog/2026/07/13/input-digits.html)

生成摘要时出错

---

## 39. Codex scraped the ICM website and discovered 2026 Fields Medal winner list

**原文标题**: Codex scraped the ICM website and discovered 2026 Fields Medal winner list

**原文链接**: [https://phemex.com/news/article/2026-fields-medal-winners-list-leaked-includes-two-peking-university-alumni-92948](https://phemex.com/news/article/2026-fields-medal-winners-list-leaked-includes-two-peking-university-alumni-92948)

生成摘要时出错

---

## 40. Fundamentals of Wireless Communication (2005)

**原文标题**: Fundamentals of Wireless Communication (2005)

**原文链接**: [https://web.stanford.edu/~dntse/wireless_book.html](https://web.stanford.edu/~dntse/wireless_book.html)

生成摘要时出错

---

## 41. An Englishwoman who sketched India before photography took hold

**原文标题**: An Englishwoman who sketched India before photography took hold

**原文链接**: [https://www.bbc.com/news/articles/cm2drrv6q54o](https://www.bbc.com/news/articles/cm2drrv6q54o)

生成摘要时出错

---

## 42. Proof of care in the age of AI

**原文标题**: Proof of care in the age of AI

**原文链接**: [https://jacobfilipp.com/care/](https://jacobfilipp.com/care/)

生成摘要时出错

---

## 43. The Future Worth Building Is Human

**原文标题**: The Future Worth Building Is Human

**原文链接**: [https://thinkingmachines.ai/blog/the-future-worth-building-is-human/](https://thinkingmachines.ai/blog/the-future-worth-building-is-human/)

生成摘要时出错

---

## 44. How to build a circular LCD clock

**原文标题**: How to build a circular LCD clock

**原文链接**: [https://blinry.org/lcd-clock/](https://blinry.org/lcd-clock/)

生成摘要时出错

---

## 45. Notable Knot Index (2016)

**原文标题**: Notable Knot Index (2016)

**原文链接**: [https://knots.neocities.org/knotindex](https://knots.neocities.org/knotindex)

生成摘要时出错

---

## 46. The Death of the Creator Middle Class

**原文标题**: The Death of the Creator Middle Class

**原文链接**: [https://letters.byburk.net/p/the-death-of-the-creator-middle-class](https://letters.byburk.net/p/the-death-of-the-creator-middle-class)

生成摘要时出错

---

## 47. Coding agents think ahead of time

**原文标题**: Coding agents think ahead of time

**原文链接**: [https://arxiv.org/abs/2607.05188](https://arxiv.org/abs/2607.05188)

生成摘要时出错

---

## 48. The Economics of Recursive Self-Improvement [pdf]

**原文标题**: The Economics of Recursive Self-Improvement [pdf]

**原文链接**: [https://elasticity.institute/rsi-paper.pdf](https://elasticity.institute/rsi-paper.pdf)

生成摘要时出错

---

## 49. The infinite scroll may become endangered if controversial Calif. law passes

**原文标题**: The infinite scroll may become endangered if controversial Calif. law passes

**原文链接**: [https://www.sfgate.com/politics/article/meta-social-media-teenagers-22337724.php](https://www.sfgate.com/politics/article/meta-social-media-teenagers-22337724.php)

生成摘要时出错

---

## 50. OpenAI mandates hardware-backed passkeys for Trusted Access Cyber members

**原文标题**: OpenAI mandates hardware-backed passkeys for Trusted Access Cyber members

**原文链接**: [https://www.yubico.com/blog/openai-mandates-hardware-backed-passkeys-for-trusted-access-cyber-members-to-log-into-chatgpt-accounts/](https://www.yubico.com/blog/openai-mandates-hardware-backed-passkeys-for-trusted-access-cyber-members-to-log-into-chatgpt-accounts/)

生成摘要时出错

---

## 51. Nokia’s years of mobile-phone supremacy ended in an afternoon

**原文标题**: Nokia’s years of mobile-phone supremacy ended in an afternoon

**原文链接**: [https://spectrum.ieee.org/nokia-phones-history](https://spectrum.ieee.org/nokia-phones-history)

生成摘要时出错

---

## 52. Is x86 ready to ACE it?

**原文标题**: Is x86 ready to ACE it?

**原文链接**: [https://chipsandcheese.com/p/is-x86-ready-to-ace-it](https://chipsandcheese.com/p/is-x86-ready-to-ace-it)

生成摘要时出错

---

## 53. FDA authorized Zyn nicotine pouches without knowing what they were made of

**原文标题**: FDA authorized Zyn nicotine pouches without knowing what they were made of

**原文链接**: [https://www.statnews.com/2026/07/14/zyn-nicotine-pouches-fda-approval-microplastic-risk/](https://www.statnews.com/2026/07/14/zyn-nicotine-pouches-fda-approval-microplastic-risk/)

生成摘要时出错

---

## 54. Show HN: Rejourney – Open-source revenue leak prediction for web and mobile apps

**原文标题**: Show HN: Rejourney – Open-source revenue leak prediction for web and mobile apps

**原文链接**: [https://github.com/rejourneyco/rejourney](https://github.com/rejourneyco/rejourney)

生成摘要时出错

---

## 55. Reverse Sprinkler Physics Problem

**原文标题**: Reverse Sprinkler Physics Problem

**原文链接**: [https://www.nytimes.com/2026/07/14/science/reverse-sprinkler-physics-problem.html](https://www.nytimes.com/2026/07/14/science/reverse-sprinkler-physics-problem.html)

生成摘要时出错

---

## 56. MorphoHDL: A minimalistic language for growing circuits

**原文标题**: MorphoHDL: A minimalistic language for growing circuits

**原文链接**: [https://paradigms-of-intelligence.github.io/morpho/](https://paradigms-of-intelligence.github.io/morpho/)

生成摘要时出错

---

## 57. Japan develops a method to recover up to 90% of lithium from used EV batteries

**原文标题**: Japan develops a method to recover up to 90% of lithium from used EV batteries

**原文链接**: [https://tech.supercarblondie.com/japan-recovers-up-to-90-of-lithium-from-used-ev-batteries/](https://tech.supercarblondie.com/japan-recovers-up-to-90-of-lithium-from-used-ev-batteries/)

生成摘要时出错

---

## 58. Microsoft Reports Maasive 25 Percent Jump in Emissions

**原文标题**: Microsoft Reports Maasive 25 Percent Jump in Emissions

**原文链接**: [https://www.wired.com/story/microsoft-25-percent-jump-in-carbon-emissions/](https://www.wired.com/story/microsoft-25-percent-jump-in-carbon-emissions/)

生成摘要时出错

---

## 59. World-First 'Super Alloy' Could Transform the Way Metals Are Made

**原文标题**: World-First 'Super Alloy' Could Transform the Way Metals Are Made

**原文链接**: [https://www.sciencealert.com/world-first-super-alloy-could-transform-the-way-metals-are-made](https://www.sciencealert.com/world-first-super-alloy-could-transform-the-way-metals-are-made)

生成摘要时出错

---

## 60. The Conservationist Who Turned 40 Terabytes of Public Data into a Video Game

**原文标题**: The Conservationist Who Turned 40 Terabytes of Public Data into a Video Game

**原文链接**: [https://blog.exe.dev/meet-the-conservationist-who-turned-40-terabytes-of-government-data-into-a-video-game](https://blog.exe.dev/meet-the-conservationist-who-turned-40-terabytes-of-government-data-into-a-video-game)

生成摘要时出错

---

## 61. Demis Hassabis has a plan to harness AI safely

**原文标题**: Demis Hassabis has a plan to harness AI safely

**原文链接**: [https://twitter.com/demishassabis/status/2076957440109625718](https://twitter.com/demishassabis/status/2076957440109625718)

生成摘要时出错

---

## 62. New York becomes the first state to impose a data center moratorium

**原文标题**: New York becomes the first state to impose a data center moratorium

**原文链接**: [https://www.reuters.com/world/new-york-becomes-first-state-impose-data-center-moratorium-2026-07-14/](https://www.reuters.com/world/new-york-becomes-first-state-impose-data-center-moratorium-2026-07-14/)

生成摘要时出错

---

## 63. Linux 0.11 rewritten in idiomatic Rust, boots in QEMU

**原文标题**: Linux 0.11 rewritten in idiomatic Rust, boots in QEMU

**原文链接**: [https://github.com/Poseidon-fan/linux-0.11-rs](https://github.com/Poseidon-fan/linux-0.11-rs)

生成摘要时出错

---

## 64. What are Forward Deployed Engineers, and why are they so in demand? (2025)

**原文标题**: What are Forward Deployed Engineers, and why are they so in demand? (2025)

**原文链接**: [https://newsletter.pragmaticengineer.com/p/forward-deployed-engineers](https://newsletter.pragmaticengineer.com/p/forward-deployed-engineers)

生成摘要时出错

---

## 65. Show HN: Oodle.ai – $10 per million agent traces

**原文标题**: Show HN: Oodle.ai – $10 per million agent traces

**原文链接**: [https://www.oodle.ai/product/agent-observability](https://www.oodle.ai/product/agent-observability)

生成摘要时出错

---

## 66. Iran exploited mobile flaws to locate U.S. troops in the Middle East

**原文标题**: Iran exploited mobile flaws to locate U.S. troops in the Middle East

**原文链接**: [https://techcrunch.com/2026/07/14/iran-abused-mobile-networks-vulnerabilities-to-locate-u-s-military-in-the-middle-east-report-says/](https://techcrunch.com/2026/07/14/iran-abused-mobile-networks-vulnerabilities-to-locate-u-s-military-in-the-middle-east-report-says/)

生成摘要时出错

---

## 67. The great digital fatigue: How digital burnout is changing social media use

**原文标题**: The great digital fatigue: How digital burnout is changing social media use

**原文链接**: [https://blog.incogni.com/digital-fatigue-and-burnout/](https://blog.incogni.com/digital-fatigue-and-burnout/)

生成摘要时出错

---

## 68. Show HN: Clawk – Give coding agents a disposable Linux VM, not your laptop

**原文标题**: Show HN: Clawk – Give coding agents a disposable Linux VM, not your laptop

**原文链接**: [https://github.com/clawkwork/clawk](https://github.com/clawkwork/clawk)

生成摘要时出错

---

## 69. GhostLock, a stack-UAF that has existed in all Linux distributions for 15 years

**原文标题**: GhostLock, a stack-UAF that has existed in all Linux distributions for 15 years

**原文链接**: [https://nebusec.ai/research/ionstack-part-2/](https://nebusec.ai/research/ionstack-part-2/)

生成摘要时出错

---

## 70. Building and shipping Mac and iOS apps without opening Xcode

**原文标题**: Building and shipping Mac and iOS apps without opening Xcode

**原文链接**: [https://scottwillsey.com/building-and-shipping-mac-and-ios-apps-without-ever-opening-xcode/](https://scottwillsey.com/building-and-shipping-mac-and-ios-apps-without-ever-opening-xcode/)

生成摘要时出错

---

## 71. Linux on the Sega 32X. Who needs hardware synchronization primitives anyway?

**原文标题**: Linux on the Sega 32X. Who needs hardware synchronization primitives anyway?

**原文链接**: [https://cakehonolulu.github.io/linux-on-32x/](https://cakehonolulu.github.io/linux-on-32x/)

生成摘要时出错

---

## 72. Precursor

**原文标题**: Precursor

**原文链接**: [https://blog.cloudflare.com/introducing-precursor/](https://blog.cloudflare.com/introducing-precursor/)

生成摘要时出错

---

## 73. Two Case Studies of NaN

**原文标题**: Two Case Studies of NaN

**原文链接**: [https://sebsite.pw/w/20260709-nan.html](https://sebsite.pw/w/20260709-nan.html)

生成摘要时出错

---

## 74. U of Chicago law school bans laptops from classes amid AI backlash

**原文标题**: U of Chicago law school bans laptops from classes amid AI backlash

**原文链接**: [https://www.the-independent.com/tech/laptop-ban-university-ai-backlash-b3013911.html](https://www.the-independent.com/tech/laptop-ban-university-ai-backlash-b3013911.html)

生成摘要时出错

---

## 75. Apple's new SpeechAnalyzer API, benchmarked against Whisper and its predecessor

**原文标题**: Apple's new SpeechAnalyzer API, benchmarked against Whisper and its predecessor

**原文链接**: [https://get-inscribe.com/blog/apple-speech-api-benchmark.html](https://get-inscribe.com/blog/apple-speech-api-benchmark.html)

生成摘要时出错

---

## 76. Crates.io: Development Update

**原文标题**: Crates.io: Development Update

**原文链接**: [https://blog.rust-lang.org/2026/07/13/crates-io-development-update/](https://blog.rust-lang.org/2026/07/13/crates-io-development-update/)

生成摘要时出错

---

## 77. DSLs Enable Reliable Use of LLMs

**原文标题**: DSLs Enable Reliable Use of LLMs

**原文链接**: [https://martinfowler.com/articles/llm-and-dsls.html](https://martinfowler.com/articles/llm-and-dsls.html)

生成摘要时出错

---

## 78. Writing a bindless GPU abstraction layer

**原文标题**: Writing a bindless GPU abstraction layer

**原文链接**: [https://www.kevin-gibson.com/blog/writing-a-bindless-gpu-abstraction-layer/](https://www.kevin-gibson.com/blog/writing-a-bindless-gpu-abstraction-layer/)

生成摘要时出错

---

## 79. Ancient Roman Board Game

**原文标题**: Ancient Roman Board Game

**原文链接**: [https://ludus-coriovalli.web.app/](https://ludus-coriovalli.web.app/)

生成摘要时出错

---

## 80. Zero Knowledge Tolstoyan Art

**原文标题**: Zero Knowledge Tolstoyan Art

**原文链接**: [https://max-amb.github.io/blog/zero_knowledge_tolstoyan_art/](https://max-amb.github.io/blog/zero_knowledge_tolstoyan_art/)

生成摘要时出错

---

## 81. Show HN: I implemented a neural network in SQL

**原文标题**: Show HN: I implemented a neural network in SQL

**原文链接**: [https://github.com/xqlsystems/xarray-sql/blob/claude/xarray-sql-mnist-demo/benchmarks/nn.py](https://github.com/xqlsystems/xarray-sql/blob/claude/xarray-sql-mnist-demo/benchmarks/nn.py)

生成摘要时出错

---

## 82. Do frontier models matter if most production AI ends up running on open models?

**原文标题**: Do frontier models matter if most production AI ends up running on open models?

**原文链接**: [https://techcrunch.com/2026/07/14/the-real-ai-race-may-no-longer-be-at-the-frontier-open-models-hugging-face/](https://techcrunch.com/2026/07/14/the-real-ai-race-may-no-longer-be-at-the-frontier-open-models-hugging-face/)

生成摘要时出错

---

## 83. Show HN: Jacquard, a programming language for AI-written, human-reviewed code

**原文标题**: Show HN: Jacquard, a programming language for AI-written, human-reviewed code

**原文链接**: [https://github.com/jbwinters/jacquard-lang](https://github.com/jbwinters/jacquard-lang)

生成摘要时出错

---

## 84. TFTP Honey Pot Results

**原文标题**: TFTP Honey Pot Results

**原文链接**: [https://bruceediger.com/posts/tftp-honeypot-results/](https://bruceediger.com/posts/tftp-honeypot-results/)

生成摘要时出错

---

## 85. Jektex 0.2.0 – A Jekyll plugin for LaTeX rendering is now ~10x faster

**原文标题**: Jektex 0.2.0 – A Jekyll plugin for LaTeX rendering is now ~10x faster

**原文链接**: [https://github.com/yagarea/jektex](https://github.com/yagarea/jektex)

生成摘要时出错

---

## 86. A Study of Microsoft's Early 2026 Rollout of Claude Code and GitHub Copilot CLI

**原文标题**: A Study of Microsoft's Early 2026 Rollout of Claude Code and GitHub Copilot CLI

**原文链接**: [https://arxiv.org/abs/2607.01418](https://arxiv.org/abs/2607.01418)

生成摘要时出错

---

## 87. Why is LinkedIn enumerating my browser extensions?

**原文标题**: Why is LinkedIn enumerating my browser extensions?

**原文链接**: [https://insertchaos.bearblog.dev/the-strange-case-of-an-attack-on-my-browser/](https://insertchaos.bearblog.dev/the-strange-case-of-an-attack-on-my-browser/)

生成摘要时出错

---

## 88. Backtrack-Free Cursive

**原文标题**: Backtrack-Free Cursive

**原文链接**: [https://mmapped.blog/posts/52-backtrack-free-cursive](https://mmapped.blog/posts/52-backtrack-free-cursive)

生成摘要时出错

---

## 89. Benchmarking 15 “E-Waste” GPUs with Modern Workloads

**原文标题**: Benchmarking 15 “E-Waste” GPUs with Modern Workloads

**原文链接**: [https://esologic.com/benchmarking-tesla-gpus/](https://esologic.com/benchmarking-tesla-gpus/)

生成摘要时出错

---

## 90. What will be left for us to work on?

**原文标题**: What will be left for us to work on?

**原文链接**: [https://www.normaltech.ai/p/what-will-be-left-for-us-to-work](https://www.normaltech.ai/p/what-will-be-left-for-us-to-work)

生成摘要时出错

---

## 91. Show HN: YouTube Guitar Tab Parser

**原文标题**: Show HN: YouTube Guitar Tab Parser

**原文链接**: [https://github.com/marcelpanse/youtube-guitar-tab-parser](https://github.com/marcelpanse/youtube-guitar-tab-parser)

生成摘要时出错

---

## 92. Show HN: Hackney – Compare Uber, Lyft, Waymo, and Robotaxi Prices

**原文标题**: Show HN: Hackney – Compare Uber, Lyft, Waymo, and Robotaxi Prices

**原文链接**: [https://hackney.app/](https://hackney.app/)

生成摘要时出错

---

## 93. Show HN: Sx 2.0 – Share AI skills with your team through a Dropbox folder

**原文标题**: Show HN: Sx 2.0 – Share AI skills with your team through a Dropbox folder

**原文链接**: [https://sleuth-io.github.io/sx/2026/07/10/your-dropbox-is-now-a-skill-server.html](https://sleuth-io.github.io/sx/2026/07/10/your-dropbox-is-now-a-skill-server.html)

生成摘要时出错

---

## 94. Lessons Learned from CISA's Recent GitHub Leak

**原文标题**: Lessons Learned from CISA's Recent GitHub Leak

**原文链接**: [https://krebsonsecurity.com/2026/07/lessons-learned-from-cisas-recent-github-leak/](https://krebsonsecurity.com/2026/07/lessons-learned-from-cisas-recent-github-leak/)

生成摘要时出错

---

## 95. Building Food Metadata with LLM Juries

**原文标题**: Building Food Metadata with LLM Juries

**原文链接**: [https://careersatdoordash.com/blog/building-food-metadata-with-llm-juries-context-optimization-multimodal-ai/](https://careersatdoordash.com/blog/building-food-metadata-with-llm-juries-context-optimization-multimodal-ai/)

生成摘要时出错

---

## 96. Hating AI in 2026

**原文标题**: Hating AI in 2026

**原文链接**: [https://www.eamoncaddigan.net/posts/ai-in-2026/](https://www.eamoncaddigan.net/posts/ai-in-2026/)

生成摘要时出错

---

## 97. Show HN: DOM-docx – HTML to native, editable Word docs (MIT)

**原文标题**: Show HN: DOM-docx – HTML to native, editable Word docs (MIT)

**原文链接**: [https://github.com/floodtide/dom-docx](https://github.com/floodtide/dom-docx)

生成摘要时出错

---

## 98. We need a PIT Crew for news

**原文标题**: We need a PIT Crew for news

**原文链接**: [https://werd.io/we-need-a-pit-crew-for-news/](https://werd.io/we-need-a-pit-crew-for-news/)

生成摘要时出错

---

## 99. Telegram's t.me domain has been suspended

**原文标题**: Telegram's t.me domain has been suspended

**原文链接**: [https://www.whois.com/whois/t.me](https://www.whois.com/whois/t.me)

生成摘要时出错

---

## 100. Vint Cerf, “father of the Internet”, is retiring

**原文标题**: Vint Cerf, “father of the Internet”, is retiring

**原文链接**: [https://techcrunch.com/2026/06/30/the-father-of-the-internet-is-finally-retiring/](https://techcrunch.com/2026/06/30/the-father-of-the-internet-is-finally-retiring/)

生成摘要时出错

---

