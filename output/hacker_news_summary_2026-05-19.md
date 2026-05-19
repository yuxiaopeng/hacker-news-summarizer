# Hacker News 热门文章摘要 (2026-05-19)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 我打造了一个虚拟博物馆，几乎涵盖了你能想到的所有操作系统。

**原文标题**: I’ve built a virtual museum with nearly every operating system you can think of

**原文链接**: [https://virtualosmuseum.org/](https://virtualosmuseum.org/)

**虚拟操作系统博物馆**（Virtual OS Museum）是一个全面的软件保存项目，收录了 1,700 多个安装实例和 570 种不同的操作系统。该项目由一名开发者历经 20 年打造，旨在通过消除复杂的模拟器配置和繁琐的安装过程等技术门槛，让用户能够“一键式”体验计算机历史。

该博物馆以 Linux 虚拟机的形式交付，兼容 QEMU、VirtualBox 和 UTM。它内置了一个自定义的、独立于模拟器的启动器，并配有快照系统，方便用户快速回滚损坏的系统环境。其目录涵盖了存储程序计算机的完整历史，从 1948 年的曼彻斯特婴儿机（Manchester Baby）到现代系统。主要亮点包括：

*   **大型机和小型机：** CTSS、Multics、MVS 和早期 IBM 系统。
*   **工作站和 Unix：** SunOS、IRIX、NeXTSTEP、A/UX 以及各种 BSD/Linux 发行版。
*   **家用和个人电脑：** Apple II、Commodore 64、ZX Spectrum、各种 DOS 版本、OS/2、早期 Windows（1.0 到 Longhorn）以及经典 Mac OS。
*   **移动和研究系统：** PalmOS、Symbian、Newton OS、BeOS、Plan 9 和 Smalltalk 环境。

该项目提供两种版本：预装了所有镜像以供离线使用的**完整版**（Full），以及按需下载系统的**精简版**（Lite）。许多系统安装中都包含符合当时时代的应用程序和开发工具，旨在真实还原这些机器当年的使用体验。

创作者持续为博物馆更新新平台和模拟器补丁。用户可以通过 Patreon 和 Ko-fi 支持该项目，社区则可以通过 Discord 和 GitLab 参与贡献。

---

## 2. Apple unveils new accessibility features

**原文标题**: Apple unveils new accessibility features

**原文链接**: [https://www.apple.com/newsroom/2026/05/apple-unveils-new-accessibility-features-and-updates-with-apple-intelligence/](https://www.apple.com/newsroom/2026/05/apple-unveils-new-accessibility-features-and-updates-with-apple-intelligence/)

Apple has announced a suite of new accessibility features and updates powered by "Apple Intelligence," scheduled for release later in 2026. These advancements leverage on-device AI to enhance tools for users with vision, hearing, and physical disabilities while maintaining Apple’s commitment to privacy.

**Key AI-Powered Updates:**
*   **VoiceOver and Magnifier:** A new "Image Explorer" provides detailed descriptions of onscreen and real-world visual content. Through "Live Recognition," users can press the Action button to ask natural language questions about their surroundings and receive detailed responses.
*   **Voice Control:** Navigation becomes more intuitive with natural language input, allowing users to "say what they see" to interact with app elements without needing exact labels.
*   **Accessibility Reader:** This tool now supports complex documents like scientific articles, offering on-demand summaries and built-in translation while preserving custom formatting.

**New Ecosystem Features:**
*   **Generated Subtitles:** Using on-device speech recognition, the Apple ecosystem can now automatically generate captions for uncaptioned videos, including personal recordings and social media content.
*   **Vision Pro Wheelchair Control:** In a significant mobility update, Apple Vision Pro users can now control compatible power wheelchairs (starting with Tolt and LUCI systems) using precision eye-tracking.
*   **Hikawa Grip & Stand:** A MagSafe adaptive accessory designed for users with limited grip or mobility is now available globally in three new colors.

**Additional Improvements:**
Other updates include "Vehicle Motion Cues" for visionOS to reduce motion sickness, face gesture support for system actions, larger text options for tvOS, and expanded "Name Recognition" support for over 50 languages. Additionally, Apple has added support for the Sony Access game controller across its platforms.

---

## 3. I’ve joined Anthropic

**原文标题**: I’ve joined Anthropic

**原文链接**: [https://twitter.com/karpathy/status/2056753169888334312](https://twitter.com/karpathy/status/2056753169888334312)

生成摘要时出错

---

## 4. Gaussian Splat of a Strawberry

**原文标题**: Gaussian Splat of a Strawberry

**原文链接**: [https://superspl.at/scene/84df8849](https://superspl.at/scene/84df8849)

生成摘要时出错

---

## 5. KV Cache 正在成为推理的存储层次结构。

**原文标题**: KV Cache Is Becoming the Memory Hierarchy of Inference

**原文链接**: [https://touchdown-labs.com/blog/kv-cache-memory-hierarchy-inference.html](https://touchdown-labs.com/blog/kv-cache-memory-hierarchy-inference.html)

Touchdown Labs 的这篇文章指出，随着大语言模型（LLM）迈向海量上下文窗口，**键值（KV）缓存**的管理已成为推理工程的核心瓶颈和重中之重。

KV 缓存存储了先前 Token 的数学表示，以避免文本生成过程中的重复计算。LLM 的权重是静态的，但 KV 缓存会随批次大小和上下文长度线性增长。对于现代长上下文模型，缓存极易超出 GPU 昂贵的高带宽内存（HBM）的容量。

其核心论点是，KV 缓存正演变为一种**多级存储层次结构**，类似于传统 CPU 使用 L1、L2 和 L3 缓存的方式。为攻克这一“内存墙”，业界正采用以下关键策略：

*   **量化 (Quantization)：** 降低 KV 缓存的精度（如从 FP16 降至 8 位或 4 位），从而在同样的内存空间内塞入更多数据。
*   **分页注意力 (PagedAttention)：** 受操作系统虚拟内存启发，该技术（由 vLLM 推广）通过非连续内存块管理 KV 缓存，以消除内存碎片并实现高效共享。
*   **卸载 (Offloading)：** 将“冷”KV 缓存从高速 GPU 显存迁移到速度较慢但成本更低的系统内存（DDR）甚至 NVMe 存储中，仅在必要时换回。
*   **逐出与稀疏化 (Eviction and Sparsity)：** 识别并剔除缓存中“次要”的 Token，在不耗尽内存的前提下维持性能。

作者总结道，LLM 可扩展性的未来不再仅取决于原始算力（FLOPS），而在于对这种 KV 缓存层级的精细编排。能否在不同存储层级间高效调度数据，将是长上下文 AI 应用实现商业落地的决定性因素。

---

## 6. Gentoo 新闻：Copy Fail、Dirty Frag 和 Fragnesia 内核漏洞

**原文标题**: Gentoo News: Copy Fail, Dirty Frag, and Fragnesia Kernel Vulnerabilities

**原文链接**: [https://www.gentoo.org/news/2026/05/19/copy-fail-fragnesia-vulnerabilities.html](https://www.gentoo.org/news/2026/05/19/copy-fail-fragnesia-vulnerabilities.html)

Gentoo Linux has issued an advisory regarding several recent privilege escalation vulnerabilities discovered in the Linux kernel, specifically **Copy Fail**, **Dirty Frag**, and **Fragnesia**. This is part of an increasing trend of rapid vulnerability disclosures that the Gentoo Kernel and Distribution Kernel teams are actively managing through fast-tracked updates and backported mitigations.

Key points include:

*   **Proactive Patching:** While some upstream kernels remain vulnerable to the "Fragnesia" flaw, Gentoo kernels already include the latest v5 patch. 
*   **Security-Supported Packages:** Users are urged to use official security-supported packages, specifically `sys-kernel/gentoo-kernel`, `sys-kernel/gentoo-kernel-bin`, or `sys-kernel/gentoo-sources`. 
*   **Vulnerable Versions:** The `vanilla-kernel` packages and other minor kernel variants are currently vulnerable or slower to receive updates.
*   **Recommendations:** Gentoo strongly advises users to automate their kernel upgrade process and run the latest versions (either ~arch or the newest stable LTS). This is necessary because upstream developers do not reliably backport security fixes to older kernel versions. 

Overall, the distribution emphasizes staying current with official Gentoo-maintained kernels to mitigate these evolving privilege escalation risks.

---

## 7. Gemini 3.5 Flash: frontier intelligence with action

**原文标题**: Gemini 3.5 Flash: frontier intelligence with action

**原文链接**: [https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)

生成摘要时出错

---

## 8. Show HN: Superlog (YC P26) – Observability that installs itself and fixes bugs

**原文标题**: Show HN: Superlog (YC P26) – Observability that installs itself and fixes bugs

**原文链接**: [https://superlog.sh/](https://superlog.sh/)

生成摘要时出错

---

## 9. CISA Admin Leaked AWS GovCloud Keys on GitHub

**原文标题**: CISA Admin Leaked AWS GovCloud Keys on GitHub

**原文链接**: [https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/](https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/)

生成摘要时出错

---

## 10. Intro to TLA+ for the LLM Era: Prompt Your Way to Victory

**原文标题**: Intro to TLA+ for the LLM Era: Prompt Your Way to Victory

**原文链接**: [https://emptysqua.re/blog/intro-to-tla-plus-for-the-llm-era/](https://emptysqua.re/blog/intro-to-tla-plus-for-the-llm-era/)

生成摘要时出错

---

## 11. Cursor Cloud Agents Down

**原文标题**: Cursor Cloud Agents Down

**原文链接**: [https://forum.cursor.com/t/cloud-agents-broken-ii/161036](https://forum.cursor.com/t/cloud-agents-broken-ii/161036)

生成摘要时出错

---

## 12. Hanoi’s humble beer glass and the memory of a nation

**原文标题**: Hanoi’s humble beer glass and the memory of a nation

**原文链接**: [https://sundaylongread.com/2026/05/15/hanois-humble-beer-glass-and-the-memory-of-a-nation/](https://sundaylongread.com/2026/05/15/hanois-humble-beer-glass-and-the-memory-of-a-nation/)

生成摘要时出错

---

## 13. Gemini Omni

**原文标题**: Gemini Omni

**原文链接**: [https://deepmind.google/models/gemini-omni/](https://deepmind.google/models/gemini-omni/)

生成摘要时出错

---

## 14. The last six months in LLMs in five minutes

**原文标题**: The last six months in LLMs in five minutes

**原文链接**: [https://simonwillison.net/2026/May/19/5-minute-llms/](https://simonwillison.net/2026/May/19/5-minute-llms/)

生成摘要时出错

---

## 15. I Found Ultra-Pure Quantum Crystals in an Abandoned Mine in the Atacama Desert

**原文标题**: I Found Ultra-Pure Quantum Crystals in an Abandoned Mine in the Atacama Desert

**原文链接**: [https://medium.com/@breid.at/ultra-pure-quantum-crystals-from-an-abandoned-mine-in-a-mysterious-desert-93cc87d12314](https://medium.com/@breid.at/ultra-pure-quantum-crystals-from-an-abandoned-mine-in-a-mysterious-desert-93cc87d12314)

生成摘要时出错

---

## 16. Mini Shai-Hulud Strikes Again: 314 npm Packages Compromised

**原文标题**: Mini Shai-Hulud Strikes Again: 314 npm Packages Compromised

**原文链接**: [https://safedep.io/mini-shai-hulud-strikes-again-314-npm-packages-compromised/](https://safedep.io/mini-shai-hulud-strikes-again-314-npm-packages-compromised/)

生成摘要时出错

---

## 17. KV Sharing, MHC, and Compressed Attention

**原文标题**: KV Sharing, MHC, and Compressed Attention

**原文链接**: [https://magazine.sebastianraschka.com/p/recent-developments-in-llm-architectures](https://magazine.sebastianraschka.com/p/recent-developments-in-llm-architectures)

生成摘要时出错

---

## 18. Peter Neumann has died

**原文标题**: Peter Neumann has died

**原文链接**: [https://www.tuhs.org/pipermail/tuhs/2026-May/033748.html](https://www.tuhs.org/pipermail/tuhs/2026-May/033748.html)

生成摘要时出错

---

## 19. Google Search as you know it is over

**原文标题**: Google Search as you know it is over

**原文链接**: [https://techcrunch.com/2026/05/19/google-search-as-you-know-it-is-over/](https://techcrunch.com/2026/05/19/google-search-as-you-know-it-is-over/)

生成摘要时出错

---

## 20. Show HN: I made a 3D pose maker for artists

**原文标题**: Show HN: I made a 3D pose maker for artists

**原文链接**: [https://setpose.com/](https://setpose.com/)

生成摘要时出错

---

## 21. An Apple (II) for Teacher

**原文标题**: An Apple (II) for Teacher

**原文链接**: [https://technicshistory.com/2026/05/19/an-apple-ii-for-teacher/](https://technicshistory.com/2026/05/19/an-apple-ii-for-teacher/)

生成摘要时出错

---

## 22. Show HN: Haystack – Review the PRs that need human attention

**原文标题**: Show HN: Haystack – Review the PRs that need human attention

**原文链接**: [https://haystackeditor.com/](https://haystackeditor.com/)

生成摘要时出错

---

## 23. Deciphering the Hashihara Castle Town Map

**原文标题**: Deciphering the Hashihara Castle Town Map

**原文链接**: [https://www.obayashi.co.jp/en/kikan_obayashi/detail/kikan_64_project.html](https://www.obayashi.co.jp/en/kikan_obayashi/detail/kikan_64_project.html)

生成摘要时出错

---

## 24. Google I/O

**原文标题**: Google I/O

**原文链接**: [https://io.google/2026/](https://io.google/2026/)

生成摘要时出错

---

## 25. Polypad

**原文标题**: Polypad

**原文链接**: [https://polypad.amplify.com/](https://polypad.amplify.com/)

生成摘要时出错

---

## 26. OpenBSD 7.9

**原文标题**: OpenBSD 7.9

**原文链接**: [https://www.openbsd.org/79.html](https://www.openbsd.org/79.html)

生成摘要时出错

---

## 27. Cursor Introduces Composer 2.5

**原文标题**: Cursor Introduces Composer 2.5

**原文链接**: [https://cursor.com/blog/composer-2-5](https://cursor.com/blog/composer-2-5)

生成摘要时出错

---

## 28. Kv4p HT – A homebrew 1W radio (VHF or UHF) that plugs into an Android phone

**原文标题**: Kv4p HT – A homebrew 1W radio (VHF or UHF) that plugs into an Android phone

**原文链接**: [https://www.kv4p.com/](https://www.kv4p.com/)

生成摘要时出错

---

## 29. Click (2016)

**原文标题**: Click (2016)

**原文链接**: [https://clickclickclick.click/](https://clickclickclick.click/)

生成摘要时出错

---

## 30. Nim-Presto – REST API Framework for Nim Language (2024)

**原文标题**: Nim-Presto – REST API Framework for Nim Language (2024)

**原文链接**: [https://github.com/status-im/nim-presto](https://github.com/status-im/nim-presto)

生成摘要时出错

---

## 31. 'Comically bad' datasets used to train clinical models for stroke and diabetes

**原文标题**: 'Comically bad' datasets used to train clinical models for stroke and diabetes

**原文链接**: [https://retractionwatch.com/2026/05/18/kaggle-dataset-clinical-models-stroke-diabetes/](https://retractionwatch.com/2026/05/18/kaggle-dataset-clinical-models-stroke-diabetes/)

生成摘要时出错

---

## 32. Anthropic acquires Stainless

**原文标题**: Anthropic acquires Stainless

**原文链接**: [https://www.anthropic.com/news/anthropic-acquires-stainless](https://www.anthropic.com/news/anthropic-acquires-stainless)

生成摘要时出错

---

## 33. Google Changes Its Search Box for the First Time in 25 Years

**原文标题**: Google Changes Its Search Box for the First Time in 25 Years

**原文链接**: [https://www.nytimes.com/2026/05/19/business/google-seach-bar-ai-gemini.html](https://www.nytimes.com/2026/05/19/business/google-seach-bar-ai-gemini.html)

生成摘要时出错

---

## 34. 1024000^2 Blocks, 2B2T Minecraft Server World Download Project, and Discoveries

**原文标题**: 1024000^2 Blocks, 2B2T Minecraft Server World Download Project, and Discoveries

**原文链接**: [https://github.com/2b2tplace/1m_release](https://github.com/2b2tplace/1m_release)

生成摘要时出错

---

## 35. Photo GIMP – A Patch for GIMP 3 for Photoshop Users

**原文标题**: Photo GIMP – A Patch for GIMP 3 for Photoshop Users

**原文链接**: [https://github.com/Diolinux/PhotoGIMP](https://github.com/Diolinux/PhotoGIMP)

生成摘要时出错

---

## 36. We let AIs run radio stations

**原文标题**: We let AIs run radio stations

**原文链接**: [https://andonlabs.com/blog/andon-fm](https://andonlabs.com/blog/andon-fm)

生成摘要时出错

---

## 37. PyTorch Landscape

**原文标题**: PyTorch Landscape

**原文链接**: [https://pytorch.landscape2.io](https://pytorch.landscape2.io)

生成摘要时出错

---

## 38. 'Capitalism has to become more humane': a Stanford economist on big tech

**原文标题**: 'Capitalism has to become more humane': a Stanford economist on big tech

**原文链接**: [https://www.theguardian.com/books/2026/may/18/big-tech-monopolies-democracy-mordecai-kurz](https://www.theguardian.com/books/2026/may/18/big-tech-monopolies-democracy-mordecai-kurz)

生成摘要时出错

---

## 39. Disney Erased FiveThirtyEight

**原文标题**: Disney Erased FiveThirtyEight

**原文链接**: [https://www.natesilver.net/p/disney-erased-fivethirtyeight](https://www.natesilver.net/p/disney-erased-fivethirtyeight)

生成摘要时出错

---

## 40. The lasting influence of Netscape Time

**原文标题**: The lasting influence of Netscape Time

**原文链接**: [https://thehistoryoftheweb.com/the-lasting-influence-of-netscape-time/](https://thehistoryoftheweb.com/the-lasting-influence-of-netscape-time/)

生成摘要时出错

---

## 41. Regex Chess: A 2-ply minimax chess engine in 84,688 regular expressions

**原文标题**: Regex Chess: A 2-ply minimax chess engine in 84,688 regular expressions

**原文链接**: [https://nicholas.carlini.com/writing/2025/regex-chess.html](https://nicholas.carlini.com/writing/2025/regex-chess.html)

生成摘要时出错

---

## 42. Graduates are booing pep talks on AI at college commencements

**原文标题**: Graduates are booing pep talks on AI at college commencements

**原文链接**: [https://www.boston25news.com/news/business/graduates-are-booing/A42H2XSTVQ2ZHHVBCKC3X7P32Y/](https://www.boston25news.com/news/business/graduates-are-booing/A42H2XSTVQ2ZHHVBCKC3X7P32Y/)

生成摘要时出错

---

## 43. Show HN: Number Gacha, a gacha game distilled to its essence

**原文标题**: Show HN: Number Gacha, a gacha game distilled to its essence

**原文链接**: [https://isabisabel.com/gacha/](https://isabisabel.com/gacha/)

生成摘要时出错

---

## 44. War game exposed U.S. vulnerability to low-tech warfare

**原文标题**: War game exposed U.S. vulnerability to low-tech warfare

**原文链接**: [https://nsarchive.gwu.edu/news/2024-11-01/rigged-war-game-exposed-us-vulnerability-low-tech-warfare](https://nsarchive.gwu.edu/news/2024-11-01/rigged-war-game-exposed-us-vulnerability-low-tech-warfare)

生成摘要时出错

---

## 45. Hyperpolyglot Lisp: Common Lisp, Racket, Clojure, Emacs Lisp

**原文标题**: Hyperpolyglot Lisp: Common Lisp, Racket, Clojure, Emacs Lisp

**原文链接**: [https://hyperpolyglot.org/lisp](https://hyperpolyglot.org/lisp)

生成摘要时出错

---

## 46. Stop 'tokenmaxxing' and deploy AI sensibly instead

**原文标题**: Stop 'tokenmaxxing' and deploy AI sensibly instead

**原文链接**: [https://www.nature.com/articles/s42256-026-01253-5](https://www.nature.com/articles/s42256-026-01253-5)

生成摘要时出错

---

## 47. Show HN: Hsrs – Type-Safe Haskell Bindings Generator for Rust

**原文标题**: Show HN: Hsrs – Type-Safe Haskell Bindings Generator for Rust

**原文链接**: [https://github.com/harmont-dev/hsrs](https://github.com/harmont-dev/hsrs)

生成摘要时出错

---

## 48. Colonization of Venus

**原文标题**: Colonization of Venus

**原文链接**: [https://en.wikipedia.org/wiki/Colonization_of_Venus](https://en.wikipedia.org/wiki/Colonization_of_Venus)

生成摘要时出错

---

## 49. Graduates are booing pep talks on AI at college commencements

**原文标题**: Graduates are booing pep talks on AI at college commencements

**原文链接**: [https://apnews.com/article/ai-college-commencement-anxiety-boo-35aec9bac660eaeb05c5b8d392db2cac](https://apnews.com/article/ai-college-commencement-anxiety-boo-35aec9bac660eaeb05c5b8d392db2cac)

生成摘要时出错

---

## 50. The Programming Language for Agents

**原文标题**: The Programming Language for Agents

**原文链接**: [https://zerolang.ai](https://zerolang.ai)

生成摘要时出错

---

## 51. AI eats the world (Spring 26) [pdf]

**原文标题**: AI eats the world (Spring 26) [pdf]

**原文链接**: [https://static1.squarespace.com/static/50363cf324ac8e905e7df861/t/6a0af5d0484fbf5fe9a7743e/1779103184855/2026-Spring-AI.pdf](https://static1.squarespace.com/static/50363cf324ac8e905e7df861/t/6a0af5d0484fbf5fe9a7743e/1779103184855/2026-Spring-AI.pdf)

生成摘要时出错

---

## 52. Anyone on the Internet Can Ring Your Doorbell

**原文标题**: Anyone on the Internet Can Ring Your Doorbell

**原文链接**: [https://www.abgeo.dev/blog/anyone-can-ring-your-doorbell](https://www.abgeo.dev/blog/anyone-can-ring-your-doorbell)

生成摘要时出错

---

## 53. Growing tribe of jobless techies is stuck in Silicon Valley's new reality

**原文标题**: Growing tribe of jobless techies is stuck in Silicon Valley's new reality

**原文链接**: [https://www.latimes.com/business/story/2026-05-19/ai-layoffs-jobless-tech-workers-silicon-valley](https://www.latimes.com/business/story/2026-05-19/ai-layoffs-jobless-tech-workers-silicon-valley)

生成摘要时出错

---

## 54. Elon Musk has lost his lawsuit against Sam Altman and OpenAI

**原文标题**: Elon Musk has lost his lawsuit against Sam Altman and OpenAI

**原文链接**: [https://techcrunch.com/2026/05/18/elon-musk-has-lost-his-lawsuit-against-sam-altman-and-openai/](https://techcrunch.com/2026/05/18/elon-musk-has-lost-his-lawsuit-against-sam-altman-and-openai/)

生成摘要时出错

---

## 55. Two computers, one monitor, zero fiddling (2025)

**原文标题**: Two computers, one monitor, zero fiddling (2025)

**原文链接**: [https://alexplescan.com/posts/2025/08/16/kvm/](https://alexplescan.com/posts/2025/08/16/kvm/)

生成摘要时出错

---

## 56. Tagging Blog Posts with BERTopic and LLMs

**原文标题**: Tagging Blog Posts with BERTopic and LLMs

**原文链接**: [https://vickiboykis.com/2026/05/18/tagging-my-blog-posts-with-bertopic-and-llms/](https://vickiboykis.com/2026/05/18/tagging-my-blog-posts-with-bertopic-and-llms/)

生成摘要时出错

---

## 57. Alignment pretraining: AI discourse creates self-fulfilling (mis)alignment

**原文标题**: Alignment pretraining: AI discourse creates self-fulfilling (mis)alignment

**原文链接**: [https://arxiv.org/abs/2601.10160](https://arxiv.org/abs/2601.10160)

生成摘要时出错

---

## 58. Show HN: Files.md – Open-source alternative to Obsidian

**原文标题**: Show HN: Files.md – Open-source alternative to Obsidian

**原文链接**: [https://github.com/zakirullin/files.md](https://github.com/zakirullin/files.md)

生成摘要时出错

---

## 59. Pope Leo XIV’s first encyclical Magnifica humanitas to be published May 25

**原文标题**: Pope Leo XIV’s first encyclical Magnifica humanitas to be published May 25

**原文链接**: [https://www.vaticannews.va/en/pope/news/2026-05/pope-leo-xiv-first-encyclical-magnifica-humanitas.html](https://www.vaticannews.va/en/pope/news/2026-05/pope-leo-xiv-first-encyclical-magnifica-humanitas.html)

生成摘要时出错

---

## 60. The Fil-C Optimized Calling Convention

**原文标题**: The Fil-C Optimized Calling Convention

**原文链接**: [https://fil-c.org/calling_convention](https://fil-c.org/calling_convention)

生成摘要时出错

---

## 61. Agora-1: The Multi-Agent World Model

**原文标题**: Agora-1: The Multi-Agent World Model

**原文链接**: [https://odyssey.ml/introducing-agora-1](https://odyssey.ml/introducing-agora-1)

生成摘要时出错

---

## 62. The quiet renovation at Bitwarden

**原文标题**: The quiet renovation at Bitwarden

**原文链接**: [https://blog.ppb1701.com/the-quiet-renovation-at-bitwarden](https://blog.ppb1701.com/the-quiet-renovation-at-bitwarden)

生成摘要时出错

---

## 63. Google Search is getting its biggest changes

**原文标题**: Google Search is getting its biggest changes

**原文链接**: [https://www.theverge.com/tech/932970/google-search-ai-update-io-2026](https://www.theverge.com/tech/932970/google-search-ai-update-io-2026)

生成摘要时出错

---

## 64. We stopped AI bot spam in our GitHub repo using Git's –author flag

**原文标题**: We stopped AI bot spam in our GitHub repo using Git's –author flag

**原文链接**: [https://archestra.ai/blog/only-responsible-ai](https://archestra.ai/blog/only-responsible-ai)

生成摘要时出错

---

## 65. Peter Salus has died

**原文标题**: Peter Salus has died

**原文链接**: [https://www.tuhs.org/pipermail/tuhs/2026-May/033750.html](https://www.tuhs.org/pipermail/tuhs/2026-May/033750.html)

生成摘要时出错

---

## 66. StanChart CEO: AI to Replace "Lower-Value Human Capital"

**原文标题**: StanChart CEO: AI to Replace "Lower-Value Human Capital"

**原文链接**: [https://www.bloomberg.com/news/videos/2026-05-19/stanchart-ceo-ai-to-replace-lower-value-human-capital-video](https://www.bloomberg.com/news/videos/2026-05-19/stanchart-ceo-ai-to-replace-lower-value-human-capital-video)

生成摘要时出错

---

## 67. We used Quint to find over 10 bugs in SQLite while hardening Turso

**原文标题**: We used Quint to find over 10 bugs in SQLite while hardening Turso

**原文链接**: [https://turso.tech/blog/how-we-used-quint-to-find-over-10-bugs-in-sqlite](https://turso.tech/blog/how-we-used-quint-to-find-over-10-bugs-in-sqlite)

生成摘要时出错

---

## 68. It is time to give up the dualism introduced by the debate on consciousness

**原文标题**: It is time to give up the dualism introduced by the debate on consciousness

**原文链接**: [https://www.noemamag.com/there-is-no-hard-problem-of-consciousness/](https://www.noemamag.com/there-is-no-hard-problem-of-consciousness/)

生成摘要时出错

---

## 69. Why is it called Kent House?

**原文标题**: Why is it called Kent House?

**原文链接**: [https://diamondgeezer.blogspot.com/2026/05/kent-house.html](https://diamondgeezer.blogspot.com/2026/05/kent-house.html)

生成摘要时出错

---

## 70. Andrej Karpathy Joins Anthropic

**原文标题**: Andrej Karpathy Joins Anthropic

**原文链接**: [https://twitter.com/i/status/2056753169888334312](https://twitter.com/i/status/2056753169888334312)

生成摘要时出错

---

## 71. Loopmaster – Livecoding Music IDE

**原文标题**: Loopmaster – Livecoding Music IDE

**原文链接**: [https://loopmaster.xyz/](https://loopmaster.xyz/)

生成摘要时出错

---

## 72. What Is Date:Italy?

**原文标题**: What Is Date:Italy?

**原文链接**: [http://aesthetikx.info/blog/date_italy.html](http://aesthetikx.info/blog/date_italy.html)

生成摘要时出错

---

## 73. Voice AI Systems Are Vulnerable to Hidden Audio Attacks

**原文标题**: Voice AI Systems Are Vulnerable to Hidden Audio Attacks

**原文链接**: [https://spectrum.ieee.org/voice-ai-audio-attacks](https://spectrum.ieee.org/voice-ai-audio-attacks)

生成摘要时出错

---

## 74. The FBI Wants to Buy Nationwide Access to License Plate Readers

**原文标题**: The FBI Wants to Buy Nationwide Access to License Plate Readers

**原文链接**: [https://www.404media.co/the-fbi-wants-to-buy-nationwide-access-to-license-plate-readers/](https://www.404media.co/the-fbi-wants-to-buy-nationwide-access-to-license-plate-readers/)

生成摘要时出错

---

## 75. Show HN: InsForge – Open-source Heroku for coding agents

**原文标题**: Show HN: InsForge – Open-source Heroku for coding agents

**原文链接**: [https://github.com/InsForge/InsForge](https://github.com/InsForge/InsForge)

生成摘要时出错

---

## 76. Project Glasswing: what Mythos showed us

**原文标题**: Project Glasswing: what Mythos showed us

**原文链接**: [https://blog.cloudflare.com/cyber-frontier-models/](https://blog.cloudflare.com/cyber-frontier-models/)

生成摘要时出错

---

## 77. The Futility of Lava Lamps: What Random Means

**原文标题**: The Futility of Lava Lamps: What Random Means

**原文链接**: [https://loup-vaillant.fr/articles/lava-lamps-and-randomness](https://loup-vaillant.fr/articles/lava-lamps-and-randomness)

生成摘要时出错

---

## 78. Consider the Sister

**原文标题**: Consider the Sister

**原文链接**: [https://www.thesmallbow.com/p/consider-the-sister-2b94](https://www.thesmallbow.com/p/consider-the-sister-2b94)

生成摘要时出错

---

## 79. Iran starts Bitcoin-backed ship insurance for Hormuz strait

**原文标题**: Iran starts Bitcoin-backed ship insurance for Hormuz strait

**原文链接**: [https://www.bloomberg.com/news/articles/2026-05-18/iran-starts-bitcoin-backed-shipping-insurance-for-hormuz-strait](https://www.bloomberg.com/news/articles/2026-05-18/iran-starts-bitcoin-backed-shipping-insurance-for-hormuz-strait)

生成摘要时出错

---

## 80. Cutting inference cold starts by 40x with LP, FUSE, C/R, and CUDA-checkpoint

**原文标题**: Cutting inference cold starts by 40x with LP, FUSE, C/R, and CUDA-checkpoint

**原文链接**: [https://modal.com/blog/truly-serverless-gpus](https://modal.com/blog/truly-serverless-gpus)

生成摘要时出错

---

## 81. Strange crystals found inside wreckage from the first nuclear bomb test

**原文标题**: Strange crystals found inside wreckage from the first nuclear bomb test

**原文链接**: [https://www.scientificamerican.com/article/strange-crystals-found-inside-wreckage-from-the-first-nuclear-bomb-test/](https://www.scientificamerican.com/article/strange-crystals-found-inside-wreckage-from-the-first-nuclear-bomb-test/)

生成摘要时出错

---

## 82. Coding on Paper

**原文标题**: Coding on Paper

**原文链接**: [https://wickstrom.tech/2026-05-16-coding-on-paper.html](https://wickstrom.tech/2026-05-16-coding-on-paper.html)

生成摘要时出错

---

## 83. When can the C++ compiler devirtualize a call?

**原文标题**: When can the C++ compiler devirtualize a call?

**原文链接**: [https://quuxplusone.github.io/blog/2021/02/15/devirtualization/](https://quuxplusone.github.io/blog/2021/02/15/devirtualization/)

生成摘要时出错

---

## 84. Badger Badger Badger Video Officially Preserved by British Film Institute

**原文标题**: Badger Badger Badger Video Officially Preserved by British Film Institute

**原文链接**: [https://petapixel.com/2026/05/18/badger-badger-badger-video-officially-preserved-by-british-film-institute/](https://petapixel.com/2026/05/18/badger-badger-badger-video-officially-preserved-by-british-film-institute/)

生成摘要时出错

---

## 85. Designing an FPGA Calculator from Scratch

**原文标题**: Designing an FPGA Calculator from Scratch

**原文链接**: [https://baltazarstudios.com/calculator/](https://baltazarstudios.com/calculator/)

生成摘要时出错

---

## 86. I 3D Printed Origami [video]

**原文标题**: I 3D Printed Origami [video]

**原文链接**: [https://www.youtube.com/watch?v=FNVBK7-h9Fs](https://www.youtube.com/watch?v=FNVBK7-h9Fs)

生成摘要时出错

---

## 87. The Aperiodic Table

**原文标题**: The Aperiodic Table

**原文链接**: [https://blog.jgc.org/2026/05/the-aperiodic-table.html](https://blog.jgc.org/2026/05/the-aperiodic-table.html)

生成摘要时出错

---

## 88. Minnesota passes the nation's first ban on 'nudification' apps

**原文标题**: Minnesota passes the nation's first ban on 'nudification' apps

**原文链接**: [https://19thnews.org/2026/04/minnesota-nudification-ban-ai-deepfake/](https://19thnews.org/2026/04/minnesota-nudification-ban-ai-deepfake/)

生成摘要时出错

---

## 89. Earth's Radio Bubble: Every signal we've ever sent into space

**原文标题**: Earth's Radio Bubble: Every signal we've ever sent into space

**原文链接**: [https://www.thescientificdrop.com/2026/05/earths-radio-bubble-every-signal-weve.html](https://www.thescientificdrop.com/2026/05/earths-radio-bubble-every-signal-weve.html)

生成摘要时出错

---

## 90. AI system fails during Glendale Community College graduation ceremony

**原文标题**: AI system fails during Glendale Community College graduation ceremony

**原文链接**: [https://www.azfamily.com/2026/05/19/ai-system-fails-during-glendale-community-college-graduation-ceremony/](https://www.azfamily.com/2026/05/19/ai-system-fails-during-glendale-community-college-graduation-ceremony/)

生成摘要时出错

---

## 91. Learn Harness Engineering

**原文标题**: Learn Harness Engineering

**原文链接**: [https://walkinglabs.github.io/learn-harness-engineering/en/](https://walkinglabs.github.io/learn-harness-engineering/en/)

生成摘要时出错

---

## 92. Shutterstock to pay $35M over hard-to-cancel subscriptions

**原文标题**: Shutterstock to pay $35M over hard-to-cancel subscriptions

**原文链接**: [https://www.ftc.gov/news-events/news/press-releases/2026/05/shutterstock-pay-35-million-settle-ftc-allegations-over-illegal-subscription-cancellation-practices](https://www.ftc.gov/news-events/news/press-releases/2026/05/shutterstock-pay-35-million-settle-ftc-allegations-over-illegal-subscription-cancellation-practices)

生成摘要时出错

---

## 93. Understanding Singleflight in Go

**原文标题**: Understanding Singleflight in Go

**原文链接**: [https://www.codingexplorations.com/blog/understanding-singleflight-in-golang-a-solution-for-eliminating-redundant-work](https://www.codingexplorations.com/blog/understanding-singleflight-in-golang-a-solution-for-eliminating-redundant-work)

生成摘要时出错

---

## 94. Aether: High-performance, formally-verified storage engine written in Rust

**原文标题**: Aether: High-performance, formally-verified storage engine written in Rust

**原文链接**: [https://codeberg.org/gregburd/aether](https://codeberg.org/gregburd/aether)

生成摘要时出错

---

## 95. New York to tax luxury second homes in NYC

**原文标题**: New York to tax luxury second homes in NYC

**原文链接**: [https://apnews.com/article/mamdani-nyc-hochul-tax-rich-a30833850bfdbd638634def266ca76dd](https://apnews.com/article/mamdani-nyc-hochul-tax-rich-a30833850bfdbd638634def266ca76dd)

生成摘要时出错

---

## 96. BambuStudio has been violating PrusaSlicer AGPL license since their fork

**原文标题**: BambuStudio has been violating PrusaSlicer AGPL license since their fork

**原文链接**: [https://github.com/jarczakpawel/OrcaSlicer-bambulab/blob/main/bambu_agpl.md](https://github.com/jarczakpawel/OrcaSlicer-bambulab/blob/main/bambu_agpl.md)

生成摘要时出错

---

## 97. Haiku OS runs on M1 Macs now

**原文标题**: Haiku OS runs on M1 Macs now

**原文链接**: [https://discuss.haiku-os.org/t/my-haiku-arm64-progress/19044?page=2](https://discuss.haiku-os.org/t/my-haiku-arm64-progress/19044?page=2)

生成摘要时出错

---

## 98. Make zip files smaller with zip shrinker

**原文标题**: Make zip files smaller with zip shrinker

**原文链接**: [https://evanhahn.com/make-zip-files-smaller-with-zip-shrinker/](https://evanhahn.com/make-zip-files-smaller-with-zip-shrinker/)

生成摘要时出错

---

## 99. Going Analog

**原文标题**: Going Analog

**原文链接**: [https://www.natemeyvis.com/going-analog/](https://www.natemeyvis.com/going-analog/)

生成摘要时出错

---

## 100. Kyber (YC W23) Is Hiring a Founding Marketer

**原文标题**: Kyber (YC W23) Is Hiring a Founding Marketer

**原文链接**: [https://www.ycombinator.com/companies/kyber/jobs/1rLQAro-founding-marketer-content-community](https://www.ycombinator.com/companies/kyber/jobs/1rLQAro-founding-marketer-content-community)

生成摘要时出错

---

