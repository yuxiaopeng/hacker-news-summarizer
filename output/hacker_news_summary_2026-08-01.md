# Hacker News 热门文章摘要 (2026-08-01)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Cursor 从使用页面和 CSV 导出中移除了成本信息。

**原文标题**: Cursor removed cost information from the usage page and CSV export

**原文链接**: [https://forum.cursor.com/t/usage-page-to-token-amount-what/167153](https://forum.cursor.com/t/usage-page-to-token-amount-what/167153)

本摘要基于 Cursor 论坛题为“Usage page to token amount - what?”（使用页面变为 Token 数量——怎么回事？）的讨论帖。

讨论的核心是 Cursor 使用情况仪表板最近的一项变化：此前用于显示 AI 使用金额的“Cost”（成本）列已从 Web 界面和可下载的 CSV 导出文件中移除。

**关键点：**

*   **移除货币指标：** 用户注意到，使用页面不再显示请求所花费的美元金额。该信息已被 Token 计数或请求量取代，在某些情况下，导出数据中则完全省略了此项内容。
*   **对 API 用户的影响：** 这一变化对于使用自带 API 密钥（如 OpenAI 或 Anthropic）的用户来说尤为不便。没有了成本列，这些用户很难直接在 Cursor 界面内追踪实际支出并管理预算。
*   **缺乏透明度：** 论坛成员对缺乏透明度表示不满，指出他们现在必须根据 Token 计数和当前模型定价手动计算成本，这一过程既繁琐又容易出错。
*   **业务与团队审计：** 对于管理团队账户或专业项目的用户而言，成本数据的移除使审计使用情况以及将费用分配给特定客户或部门的过程变得复杂化。
*   **用户诉求：** 社区呼吁恢复成本列，或者至少提供更详细的 Token 细分数据，以匹配供应商对输入、输出和缓存 Token 的计费方式。

总之，虽然 Cursor 似乎正在将重心转向使用量（Token/请求数），但直接成本信息的缺失给依赖该平台进行 AI 支出精确财务追踪的用户带来了显著困扰。

---

## 2. 64位汇编艺术

**原文标题**: The Art of 64-bit Assembly

**原文链接**: [https://nostarch.com/art-64-bit-assembly-v2](https://nostarch.com/art-64-bit-assembly-v2)

《64位汇编语言艺术》是一本专注于使用64位汇编语言（特别是针对微软宏汇编器 MASM）进行高级底层编程技术的技术指南。本书并非侧重于基础语法，而是深入探讨了如何在机器层面直接实现复杂的高级编程概念。

核心内容分为以下几个关键领域：

*   **高级工程：** 涵盖了复杂的结构，如高级宏、专门的过程以及复杂的参数实现。
*   **数据与数学：** 介绍了如何在汇编中处理 Unicode 字符串并执行超越函数（如三角函数或对数等复杂数学运算）。
*   **现代编程范式：** 大量篇幅致力于在底层环境中实现高级概念，包括面向对象编程 (OOP)、异常处理和并发编程。
*   **高级控制流：** 作者探讨了复杂的执行模型，如 thunk、闭包、迭代器、协程、生成器和纤程 (fibers)。

本书还包括用于搭建 Visual Studio 环境的实用附录，以及 ASCII 字符集和术语表等快速参考资料。总而言之，本书为希望在高性能 64 位汇编语言环境中应用现代软件工程原则（如模块化和抽象化）的开发者提供了沟通的桥梁。

---

## 3. Kaisel – 路由即值。基于 Dart 3 的 Flutter 原生路由。

**原文标题**: Kaisel – Routes as Values. Dart 3 Native Router for Flutter

**原文链接**: [https://kaisel.dev/](https://kaisel.dev/)

**Kaisel** 是一个专为 Dart 3 构建的原生 Flutter 路由库，它引入了“**路由即值**（Routes as Values）”的概念。通过利用现代 Dart 特性——特别是**密封类（sealed classes）**和**穷举匹配（exhaustive switches）**——它提供了一种类型安全的导航方式，确保应用逻辑涵盖了所有定义的路由。

该库专注于开发效率和代码可靠性。其配置过程非常快捷，使开发者能够在几分钟内完成从安装（`flutter pub add kaisel`）到使用全类型路由进行导航的过渡。通过将路由视为值而非简单的字符串，Kaisel 减少了样板代码，并最大限度地降低了传统路由方法中常见的运行时错误。

总之，Kaisel 提供了一种精简且“Dart 原生”的 Flutter 导航处理方式，强调类型安全和快速集成。

---

## 4. RipGrep musl binaries occasionally segfault during very-large searches

**原文标题**: RipGrep musl binaries occasionally segfault during very-large searches

**原文链接**: [https://github.com/BurntSushi/ripgrep/issues/3494](https://github.com/BurntSushi/ripgrep/issues/3494)

生成摘要时出错

---

## 5. 探索性建模：在 K 个猜测的最佳结果上进行训练

**原文标题**: Explorative modeling: Train on the best of K guesses

**原文链接**: [https://alexiglad.github.io/blog/2026/explorative_modeling/](https://alexiglad.github.io/blog/2026/explorative_modeling/)

探索性建模（XM）是生成式建模的一种新范式，旨在解决“多解”问题：即模型在通过直接回归训练时，往往会预测所有有效输出的平均值（例如，产生“模糊”图像而非清晰图像）。虽然大语言模型（LLM）和扩散模型（Diffusion）等现有模型通过将生成过程分解为多个小步骤（即“生成分解”）来解决这一问题，但这种方法会导致曝光偏差并阻碍端到端训练。

相比之下，XM 通过让模型对单个输入产生 $K$ 个猜测来实现“训练分解”。在该过程中，只有最佳猜测会获得梯度，这一机制被称为**模态强制（Mode Forcing）**。这使得模型能够专注于特定的数据点，而非它们的平均值。作者将这种能力定义为**生成表达力（generative expressivity）**，并认为它是继参数和数据之后，衡量预训练能力的第三个关键维度。

**核心结果：**
*   **效率：** 与现有最先进的基准相比，XM 的样本效率提升了 6.2 倍，FLOP（浮点运算）效率提升了 4.1 倍，参数效率提升了 47%。
*   **扩展性：** 探索带来的收益随规模增长而增加：随着数据量增加，收益从 7% 升至 36%；随着参数量增加，收益从 13% 升至 23%。
*   **性能：** XM 在 ImageNet 256 数据集上达到了 1.43 FID 的领先水平。同时，它在视频和语言建模领域也展现出持续的改进。
*   **推理：** 作为一种端到端模型，XM 在控制任务上的表现与扩散模型相当，但由于其采用单步生成方式，所需的推理计算量最高可降低 256 倍。

通过将复杂性从生成过程转移到训练循环中，XM 使模型能够保持端到端特性（即训练方式与推理运行完全一致），同时为在各个生成领域实现更高保真度提供了一条可扩展的路径。

---

## 6. Pgtestdb 基于模板克隆的测试方法速度很快。

**原文标题**: Pgtestdb's template cloning approach to testing is fast

**原文链接**: [https://brandur.org/fragments/pgtestdb](https://brandur.org/fragments/pgtestdb)

在本文中，Brandur 探讨了 **pgtestdb**，这是一个利用 Postgres 内置模板数据库特性的 Go/Postgres 测试包。通过使用 `CREATE DATABASE ... TEMPLATE` 命令，该工具以 8 kB 数据块的形式复制物理文件，从而克隆已预迁移的数据库。相比于从头运行迁移或使用笨重的 Docker 设置，这提供了一个更快的替代方案。

Brandur 将 `pgtestdb` 与他在其项目 **River** 中使用的基于 schema 的测试方法进行了对比。尽管他此前认为创建新数据库会很慢，但结果显示，两种方法的启动时间相近，每个测试大约只需 **100 毫秒**。这使得 `pgtestdb` 成为开发者的一个可行选择，特别是当需要测试数据库全局特性（如 `LISTEN/NOTIFY`）或传统测试事务无法处理的多事务交互时。

然而，对比也揭示了在总耗时上的显著差异：River 的测试套件在 14.5 秒内完成，而 `pgtestdb` 的实现则耗时 51 秒。这一差距源于**重用**。River 对其测试 schema 进行了池化，通过清理并重用它们来执行后续测试，而不是每次都重新创建。

Brandur 总结道，虽然他为了验证特定配置将继续在 River 中使用 schema，但他强烈推荐将 `pgtestdb` 用于端到端测试。他指出，如果 `pgtestdb` 或其用户实现类似的池化/重用策略，启动时间可能会降至 10–20 毫秒，使完整数据库隔离的速度接近测试事务的水平。

---

## 7. A Surveillance Treaty in Disguise: Canada Signs UN Cybercrime Convention

**原文标题**: A Surveillance Treaty in Disguise: Canada Signs UN Cybercrime Convention

**原文链接**: [https://www.michaelgeist.ca/2026/07/a-surveillance-treaty-in-disguise-the-trouble-with-canadas-quiet-decision-to-sign-the-un-cybercrime-convention/](https://www.michaelgeist.ca/2026/07/a-surveillance-treaty-in-disguise-the-trouble-with-canadas-quiet-decision-to-sign-the-un-cybercrime-convention/)

生成摘要时出错

---

## 8. RSS 爱好者名录

**原文标题**: A directory of people who love RSS

**原文链接**: [https://andrewshell.org/2026/07/i-%e2%99%a5-rss/](https://andrewshell.org/2026/07/i-%e2%99%a5-rss/)

2026年7月30日，作者宣布推出 **I ♥ RSS**，这是一个专为 RSS 爱好者打造的新目录。该平台允许用户提交自己的网站，并在首页展示由 FeedLand 驱动的实时博客列表。作者已在自己的网站上集成了该目录的徽章，并鼓励广大 RSS 爱好者探索该目录，将自己的网站也加入其中。

---

## 9. Register deprivation: spills and runtime under forced register scarcity

**原文标题**: Register deprivation: spills and runtime under forced register scarcity

**原文链接**: [https://rjp.io/blog/2026-07-19-register-deprivation](https://rjp.io/blog/2026-07-19-register-deprivation)

生成摘要时出错

---

## 10. Charlie Stross – On the non-use of AI in my writing process

**原文标题**: Charlie Stross – On the non-use of AI in my writing process

**原文链接**: [https://www.antipope.org/charlie/blog-static/2026/08/on-the-non-use-of-ai-in-my-wri.html](https://www.antipope.org/charlie/blog-static/2026/08/on-the-non-use-of-ai-in-my-wri.html)

生成摘要时出错

---

## 11. Study uncovers lost 'golden age' of languages

**原文标题**: Study uncovers lost 'golden age' of languages

**原文链接**: [https://news.yale.edu/2026/07/23/study-uncovers-lost-golden-age-languages](https://news.yale.edu/2026/07/23/study-uncovers-lost-golden-age-languages)

生成摘要时出错

---

## 12. Rear center fuel tank adds roughly 20k liters and extends range by 1k NM

**原文标题**: Rear center fuel tank adds roughly 20k liters and extends range by 1k NM

**原文链接**: [https://www.airbus.com/en/newsroom/press-releases/2026-06-worlds-longest-range-aircraft-the-airbus-a350-1000ulr-takes-to-the-skies](https://www.airbus.com/en/newsroom/press-releases/2026-06-worlds-longest-range-aircraft-the-airbus-a350-1000ulr-takes-to-the-skies)

生成摘要时出错

---

## 13. Manual: •.,:;?·

**原文标题**: Manual: •.,:;?·

**原文链接**: [https://type.today/en/journal/dots](https://type.today/en/journal/dots)

生成摘要时出错

---

## 14. Flint: A Visualization Language for the AI Era

**原文标题**: Flint: A Visualization Language for the AI Era

**原文链接**: [https://microsoft.github.io/flint-chart/](https://microsoft.github.io/flint-chart/)

生成摘要时出错

---

## 15. RamenHaus

**原文标题**: RamenHaus

**原文链接**: [https://ramen.haus/](https://ramen.haus/)

生成摘要时出错

---

## 16. qm – Multiplayer agent harness for work

**原文标题**: qm – Multiplayer agent harness for work

**原文链接**: [https://github.com/yc-software/qm](https://github.com/yc-software/qm)

生成摘要时出错

---

## 17. Solid Queue 1.6.0 now supports fiber workers

**原文标题**: Solid Queue 1.6.0 now supports fiber workers

**原文链接**: [https://github.com/rails/solid_queue/releases/tag/v1.6.0](https://github.com/rails/solid_queue/releases/tag/v1.6.0)

生成摘要时出错

---

## 18. Kontigo (YC S24) Is Hiring

**原文标题**: Kontigo (YC S24) Is Hiring

**原文链接**: [https://www.ycombinator.com/companies/kontigo/jobs/xAo6tMt-founding-engineer](https://www.ycombinator.com/companies/kontigo/jobs/xAo6tMt-founding-engineer)

生成摘要时出错

---

## 19. Linux on ESP32

**原文标题**: Linux on ESP32

**原文链接**: [https://github.com/GrieferPig/esp32-s31-linux](https://github.com/GrieferPig/esp32-s31-linux)

生成摘要时出错

---

## 20. A tiny holdout building in the middle of Macy’s is back in view

**原文标题**: A tiny holdout building in the middle of Macy’s is back in view

**原文链接**: [https://ephemeralnewyork.wordpress.com/2026/07/27/hidden-by-billboards-for-over-100-years-the-tiny-holdout-building-in-the-middle-of-macys-is-back-in-view/](https://ephemeralnewyork.wordpress.com/2026/07/27/hidden-by-billboards-for-over-100-years-the-tiny-holdout-building-in-the-middle-of-macys-is-back-in-view/)

生成摘要时出错

---

## 21. Toast IDE Gets Markdown Spell Checking

**原文标题**: Toast IDE Gets Markdown Spell Checking

**原文链接**: [https://github.com/paradise-runner/toast](https://github.com/paradise-runner/toast)

生成摘要时出错

---

## 22. The development pipeline is a production system

**原文标题**: The development pipeline is a production system

**原文链接**: [https://sundry.jerryorr.com/2026/07/31/development-pipeline-is-a-production-system](https://sundry.jerryorr.com/2026/07/31/development-pipeline-is-a-production-system)

生成摘要时出错

---

## 23. Elevators

**原文标题**: Elevators

**原文链接**: [https://john.fun/elevators](https://john.fun/elevators)

生成摘要时出错

---

## 24. Software for One

**原文标题**: Software for One

**原文链接**: [https://www.ajwaxman.com/writing/software-for-one](https://www.ajwaxman.com/writing/software-for-one)

生成摘要时出错

---

## 25. Run Kimi K3 using 29 GB of RAM at 0.50 tok/s

**原文标题**: Run Kimi K3 using 29 GB of RAM at 0.50 tok/s

**原文链接**: [https://github.com/sqliteai/waste](https://github.com/sqliteai/waste)

生成摘要时出错

---

## 26. Astro Loop

**原文标题**: Astro Loop

**原文链接**: [https://pubdeer.com/](https://pubdeer.com/)

生成摘要时出错

---

## 27. How to Exist

**原文标题**: How to Exist

**原文链接**: [https://www.raptitude.com/2026/07/how-to-exist/](https://www.raptitude.com/2026/07/how-to-exist/)

生成摘要时出错

---

## 28. G'mic 4.0: Squaring the Pixel, Easier

**原文标题**: G'mic 4.0: Squaring the Pixel, Easier

**原文链接**: [https://gmic.eu/gmic40/](https://gmic.eu/gmic40/)

生成摘要时出错

---

## 29. BMW Is Showing Commercials on Their Car's Dash Screens as a Treat

**原文标题**: BMW Is Showing Commercials on Their Car's Dash Screens as a Treat

**原文链接**: [https://www.theautopian.com/bmw-is-showing-commercials-on-their-cars-dash-screens-and-they-want-you-to-think-its-a-treat/](https://www.theautopian.com/bmw-is-showing-commercials-on-their-cars-dash-screens-and-they-want-you-to-think-its-a-treat/)

生成摘要时出错

---

## 30. Ten advances in mathematics and theoretical computer science

**原文标题**: Ten advances in mathematics and theoretical computer science

**原文链接**: [https://openai.com/index/ten-advances-in-mathematics/](https://openai.com/index/ten-advances-in-mathematics/)

生成摘要时出错

---

## 31. Twenty-five years ago it was cryptography, today it's model weights

**原文标题**: Twenty-five years ago it was cryptography, today it's model weights

**原文链接**: [https://weeraman.com/because-we-can/](https://weeraman.com/because-we-can/)

生成摘要时出错

---

## 32. DeepSeek V4 Flash 0731 Intelligence, Performance and Price Analysis

**原文标题**: DeepSeek V4 Flash 0731 Intelligence, Performance and Price Analysis

**原文链接**: [https://artificialanalysis.ai/models/deepseek-v4-flash](https://artificialanalysis.ai/models/deepseek-v4-flash)

生成摘要时出错

---

## 33. Using the railway network as a flatbed scanner [video]

**原文标题**: Using the railway network as a flatbed scanner [video]

**原文链接**: [https://media.ccc.de/v/emf2026-74-1-using-the-railway-network-as-a-flatbed-scanner](https://media.ccc.de/v/emf2026-74-1-using-the-railway-network-as-a-flatbed-scanner)

生成摘要时出错

---

## 34. Authorize, don't authenticate

**原文标题**: Authorize, don't authenticate

**原文链接**: [https://blog.marcua.net/2026/07/31/authorize-dont-authenticate.html](https://blog.marcua.net/2026/07/31/authorize-dont-authenticate.html)

生成摘要时出错

---

## 35. Show HN: What should the GUI for AI agents look like?

**原文标题**: Show HN: What should the GUI for AI agents look like?

**原文链接**: [https://marbleos.com/demo](https://marbleos.com/demo)

生成摘要时出错

---

## 36. The End of an Era

**原文标题**: The End of an Era

**原文链接**: [https://hughhowey.com/the-end-of-an-era/](https://hughhowey.com/the-end-of-an-era/)

生成摘要时出错

---

## 37. Dubious research tied to Red Bull has shaped energy drink policy

**原文标题**: Dubious research tied to Red Bull has shaped energy drink policy

**原文链接**: [https://www.theexamination.org/articles/red-bull-funded-research-energy-drinks-alcohol](https://www.theexamination.org/articles/red-bull-funded-research-energy-drinks-alcohol)

生成摘要时出错

---

## 38. The Bedrock of Software Design

**原文标题**: The Bedrock of Software Design

**原文链接**: [https://alex.draftist.io/blog/the-bedrock-of-software-design-ycqvcedsj](https://alex.draftist.io/blog/the-bedrock-of-software-design-ycqvcedsj)

生成摘要时出错

---

## 39. Anti-fraud tools can't keep pace with robocall scammers

**原文标题**: Anti-fraud tools can't keep pace with robocall scammers

**原文链接**: [https://broadbandbreakfast.com/how-to-fight-back-against-fraudulent-robocalls/](https://broadbandbreakfast.com/how-to-fight-back-against-fraudulent-robocalls/)

生成摘要时出错

---

## 40. Morten Linderud resigning from Arch Linux development team

**原文标题**: Morten Linderud resigning from Arch Linux development team

**原文链接**: [https://lists.archlinux.org/archives/list/arch-dev-public@lists.archlinux.org/thread/2AX2BCJ3EQX7G3YXSDX73BR4NCAWXXBZ/](https://lists.archlinux.org/archives/list/arch-dev-public@lists.archlinux.org/thread/2AX2BCJ3EQX7G3YXSDX73BR4NCAWXXBZ/)

生成摘要时出错

---

## 41. Nano Banana 2 removed from Google Earth

**原文标题**: Nano Banana 2 removed from Google Earth

**原文链接**: [https://www.digitaldigging.org/p/nano-banana-2-removed-from-google](https://www.digitaldigging.org/p/nano-banana-2-removed-from-google)

生成摘要时出错

---

## 42. Everyone is building LLM routers, we deprecated ours

**原文标题**: Everyone is building LLM routers, we deprecated ours

**原文链接**: [https://manifest.build/blog/why-we-deprecated-our-llm-router/](https://manifest.build/blog/why-we-deprecated-our-llm-router/)

生成摘要时出错

---

## 43. Algorithms on billion-scale graph using 10GB RAM: I love DataFusion

**原文标题**: Algorithms on billion-scale graph using 10GB RAM: I love DataFusion

**原文链接**: [https://semyonsinchenko.github.io/ssinchenko/post/datafusion-graphs-cc-2/](https://semyonsinchenko.github.io/ssinchenko/post/datafusion-graphs-cc-2/)

生成摘要时出错

---

## 44. The Religion of Speed

**原文标题**: The Religion of Speed

**原文链接**: [https://graybeard.ing/the-religion-of-speed/](https://graybeard.ing/the-religion-of-speed/)

生成摘要时出错

---

## 45. Solving poker in custom WebGPU kernels

**原文标题**: Solving poker in custom WebGPU kernels

**原文链接**: [https://phulin.me/blog/poker/](https://phulin.me/blog/poker/)

生成摘要时出错

---

## 46. AI doesn't generate working products, that's still your job

**原文标题**: AI doesn't generate working products, that's still your job

**原文链接**: [https://weeraman.com/the-prototype-isnt-the-product/](https://weeraman.com/the-prototype-isnt-the-product/)

生成摘要时出错

---

## 47. Clockwise/Spiral Rule (1994)

**原文标题**: Clockwise/Spiral Rule (1994)

**原文链接**: [https://c-faq.com/decl/spiral.anderson.html](https://c-faq.com/decl/spiral.anderson.html)

生成摘要时出错

---

## 48. Severance

**原文标题**: Severance

**原文链接**: [https://lcamtuf.substack.com/p/severance](https://lcamtuf.substack.com/p/severance)

生成摘要时出错

---

## 49. Show HN: Gander, an Android file viewer that asks for no permissions

**原文标题**: Show HN: Gander, an Android file viewer that asks for no permissions

**原文链接**: [https://github.com/mokshablr/gander](https://github.com/mokshablr/gander)

生成摘要时出错

---

## 50. Predictive Speculative KV Replication for Bursty LLM Inference

**原文标题**: Predictive Speculative KV Replication for Bursty LLM Inference

**原文链接**: [https://jwlabs.vercel.app/post/biting-the-bullet](https://jwlabs.vercel.app/post/biting-the-bullet)

生成摘要时出错

---

## 51. Show HN: BitBang – Reach machines behind NAT from a browser, no account

**原文标题**: Show HN: BitBang – Reach machines behind NAT from a browser, no account

**原文链接**: [https://github.com/richlegrand/bitbang-cli](https://github.com/richlegrand/bitbang-cli)

生成摘要时出错

---

## 52. Termixer (TUI DJ Mixer)

**原文标题**: Termixer (TUI DJ Mixer)

**原文链接**: [https://github.com/l00sed/termixer](https://github.com/l00sed/termixer)

生成摘要时出错

---

## 53. The session you cannot take with you

**原文标题**: The session you cannot take with you

**原文链接**: [https://earendil.com/posts/session-portability/](https://earendil.com/posts/session-portability/)

生成摘要时出错

---

## 54. A past and future of trade secrets

**原文标题**: A past and future of trade secrets

**原文链接**: [https://www.cabinetmagazine.org/issues/70/kofen.php](https://www.cabinetmagazine.org/issues/70/kofen.php)

生成摘要时出错

---

## 55. Unearthing my 1996 windowed OS in machine code for Am29000 homebrew computer

**原文标题**: Unearthing my 1996 windowed OS in machine code for Am29000 homebrew computer

**原文链接**: [https://nanochess.org/the_am29000_computer.html](https://nanochess.org/the_am29000_computer.html)

生成摘要时出错

---

## 56. Plug-In Solar Panels Are Starting to Sprout in U.S. Backyards

**原文标题**: Plug-In Solar Panels Are Starting to Sprout in U.S. Backyards

**原文链接**: [https://www.nytimes.com/2026/07/31/business/energy-environment/plug-in-balcony-solar.html](https://www.nytimes.com/2026/07/31/business/energy-environment/plug-in-balcony-solar.html)

生成摘要时出错

---

## 57. Ron Gilbert started production on Thimbleweed Park 2

**原文标题**: Ron Gilbert started production on Thimbleweed Park 2

**原文链接**: [https://www.grumpygamer.com/twp2_announce/](https://www.grumpygamer.com/twp2_announce/)

生成摘要时出错

---

## 58. Legendary Mountaineer Nirmal Purja Killed in Broad Peak Avalanche in Pakistan

**原文标题**: Legendary Mountaineer Nirmal Purja Killed in Broad Peak Avalanche in Pakistan

**原文链接**: [https://www.theguardian.com/world/2026/aug/01/top-mountaineer-nirmal-purja-confirmed-dead-after-11-hit-by-avalanche-in-pakistan](https://www.theguardian.com/world/2026/aug/01/top-mountaineer-nirmal-purja-confirmed-dead-after-11-hit-by-avalanche-in-pakistan)

生成摘要时出错

---

## 59. Show HN: Wisp – a Linux shell with Lua scripting and structured pipelines

**原文标题**: Show HN: Wisp – a Linux shell with Lua scripting and structured pipelines

**原文链接**: [https://github.com/Hinikaa/wisp](https://github.com/Hinikaa/wisp)

生成摘要时出错

---

## 60. Stacked PRs are now live on GitHub

**原文标题**: Stacked PRs are now live on GitHub

**原文链接**: [https://github.blog/changelog/2026-07-30-stacked-pull-requests-are-now-in-public-preview/](https://github.blog/changelog/2026-07-30-stacked-pull-requests-are-now-in-public-preview/)

生成摘要时出错

---

## 61. Why is everyone trying to build a solid-state battery?

**原文标题**: Why is everyone trying to build a solid-state battery?

**原文链接**: [https://www.construction-physics.com/p/why-is-everyone-trying-to-build-a](https://www.construction-physics.com/p/why-is-everyone-trying-to-build-a)

生成摘要时出错

---

## 62. 13 Models and 4 Agents on SWE Tasks: Go, Java, Python, Rust, TS

**原文标题**: 13 Models and 4 Agents on SWE Tasks: Go, Java, Python, Rust, TS

**原文链接**: [https://swe-rebench.com](https://swe-rebench.com)

生成摘要时出错

---

## 63. The lost civic life of movie rental stores

**原文标题**: The lost civic life of movie rental stores

**原文链接**: [https://thereader.mitpress.mit.edu/the-lost-civic-life-of-movie-rental-stores/](https://thereader.mitpress.mit.edu/the-lost-civic-life-of-movie-rental-stores/)

生成摘要时出错

---

## 64. The mean means nothing: data visualization to debug a latency problem

**原文标题**: The mean means nothing: data visualization to debug a latency problem

**原文链接**: [https://fzakaria.com/2026/07/27/the-mean-means-nothing](https://fzakaria.com/2026/07/27/the-mean-means-nothing)

生成摘要时出错

---

## 65. Not just Neanderthals: Ghost lineage in Africa left its mark on our DNA

**原文标题**: Not just Neanderthals: Ghost lineage in Africa left its mark on our DNA

**原文链接**: [https://arstechnica.com/science/2026/07/not-just-neanderthals-ghost-lineage-in-africa-left-its-mark-on-our-dna/](https://arstechnica.com/science/2026/07/not-just-neanderthals-ghost-lineage-in-africa-left-its-mark-on-our-dna/)

生成摘要时出错

---

## 66. Show HN: Distilling DeepSeek into GPT-OSS doesn't transfer censorship. Try it

**原文标题**: Show HN: Distilling DeepSeek into GPT-OSS doesn't transfer censorship. Try it

**原文链接**: [https://www.ctgt.ai/research/distillation-censorship-transfer](https://www.ctgt.ai/research/distillation-censorship-transfer)

生成摘要时出错

---

## 67. PostgreSQL and the Linux OOM Killer: A Better Default

**原文标题**: PostgreSQL and the Linux OOM Killer: A Better Default

**原文链接**: [https://clickhouse.com/blog/strict-memory-overcommit-for-postgres](https://clickhouse.com/blog/strict-memory-overcommit-for-postgres)

生成摘要时出错

---

## 68. Just brute force your embeddings

**原文标题**: Just brute force your embeddings

**原文链接**: [https://softwaredoug.com/blog/2026/07/29/just-brute-force-embeddings](https://softwaredoug.com/blog/2026/07/29/just-brute-force-embeddings)

生成摘要时出错

---

## 69. Show HN: Kedge – Full-stack cloud with forkable VM snapshots and global SQLite

**原文标题**: Show HN: Kedge – Full-stack cloud with forkable VM snapshots and global SQLite

**原文链接**: [https://kedge.dev/](https://kedge.dev/)

生成摘要时出错

---

## 70. A California aquifer may have crossed the point of no return

**原文标题**: A California aquifer may have crossed the point of no return

**原文链接**: [https://www.science.org/content/article/california-aquifer-may-have-crossed-point-no-return](https://www.science.org/content/article/california-aquifer-may-have-crossed-point-no-return)

生成摘要时出错

---

## 71. Orca-Bench: How Ready Are Language Model Agents for Oncall?

**原文标题**: Orca-Bench: How Ready Are Language Model Agents for Oncall?

**原文链接**: [https://arxiv.org/abs/2607.28545](https://arxiv.org/abs/2607.28545)

生成摘要时出错

---

## 72. "Bettering Myself" by Ottessa Moshfegh

**原文标题**: "Bettering Myself" by Ottessa Moshfegh

**原文链接**: [https://electricliterature.com/bettering-myself-ottessa-moshfegh/](https://electricliterature.com/bettering-myself-ottessa-moshfegh/)

生成摘要时出错

---

## 73. Upper stage impacting the moon on 2026 August 5

**原文标题**: Upper stage impacting the moon on 2026 August 5

**原文链接**: [https://www.projectpluto.com/25010d.htm](https://www.projectpluto.com/25010d.htm)

生成摘要时出错

---

## 74. Memo-1: A 6502 computer built from scratch, using a Minitel as its terminal

**原文标题**: Memo-1: A 6502 computer built from scratch, using a Minitel as its terminal

**原文链接**: [https://github.com/MemoireMorte/Memo-1](https://github.com/MemoireMorte/Memo-1)

生成摘要时出错

---

## 75. Show HN: I worked on a new browser for 2 years, today it passed Acid 3

**原文标题**: Show HN: I worked on a new browser for 2 years, today it passed Acid 3

**原文链接**: [https://code.intellios.ai/cwbrowser/](https://code.intellios.ai/cwbrowser/)

生成摘要时出错

---

## 76. A GTK4 SSH-askpass in Zig

**原文标题**: A GTK4 SSH-askpass in Zig

**原文链接**: [https://xn--gckvb8fzb.com/a-gtk4-ssh-askpass-in-zig/](https://xn--gckvb8fzb.com/a-gtk4-ssh-askpass-in-zig/)

生成摘要时出错

---

## 77. JEP 401: Value Objects (Preview) merged to OpenJDK master

**原文标题**: JEP 401: Value Objects (Preview) merged to OpenJDK master

**原文链接**: [https://github.com/openjdk/jdk/pull/31120](https://github.com/openjdk/jdk/pull/31120)

生成摘要时出错

---

## 78. The Maxwell Conjecture Is False (GPT 5.6 Sol)

**原文标题**: The Maxwell Conjecture Is False (GPT 5.6 Sol)

**原文链接**: [https://arxiv.org/abs/2607.27197](https://arxiv.org/abs/2607.27197)

生成摘要时出错

---

## 79. UEFA and its national associations will not participate in FIFA competitions

**原文标题**: UEFA and its national associations will not participate in FIFA competitions

**原文链接**: [https://www.uefa.com/news-media/news/02a7-213a92896eb0-54dfbf454e3b-1000--statement-on-behalf-of-uefa-and-its-55-national-associations/](https://www.uefa.com/news-media/news/02a7-213a92896eb0-54dfbf454e3b-1000--statement-on-behalf-of-uefa-and-its-55-national-associations/)

生成摘要时出错

---

## 80. Gemini Robotics 2 brings whole body intelligence to robots

**原文标题**: Gemini Robotics 2 brings whole body intelligence to robots

**原文链接**: [https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/](https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/)

生成摘要时出错

---

## 81. The Art of Decision-Making (2019)

**原文标题**: The Art of Decision-Making (2019)

**原文链接**: [https://www.newyorker.com/magazine/2019/01/21/the-art-of-decision-making](https://www.newyorker.com/magazine/2019/01/21/the-art-of-decision-making)

生成摘要时出错

---

## 82. CodePen 2.0

**原文标题**: CodePen 2.0

**原文链接**: [https://chriscoyier.net/2026/07/30/codepen-2-0/](https://chriscoyier.net/2026/07/30/codepen-2-0/)

生成摘要时出错

---

## 83. TV Pickup

**原文标题**: TV Pickup

**原文链接**: [https://en.wikipedia.org/wiki/TV_pickup](https://en.wikipedia.org/wiki/TV_pickup)

生成摘要时出错

---

## 84. Hacker Public Radio

**原文标题**: Hacker Public Radio

**原文链接**: [https://hackerpublicradio.org/](https://hackerpublicradio.org/)

生成摘要时出错

---

## 85. Scope of Hacks on U.S. Water Supply Widens as Evidence Points to Iran

**原文标题**: Scope of Hacks on U.S. Water Supply Widens as Evidence Points to Iran

**原文链接**: [https://www.nytimes.com/2026/08/01/us/politics/iran-cyberattack-water-systems.html](https://www.nytimes.com/2026/08/01/us/politics/iran-cyberattack-water-systems.html)

生成摘要时出错

---

## 86. Arch Linux disables AUR package adoption

**原文标题**: Arch Linux disables AUR package adoption

**原文链接**: [https://lwn.net/Articles/1086489/](https://lwn.net/Articles/1086489/)

生成摘要时出错

---

## 87. Where USB Memory Sticks are Born (2013)

**原文标题**: Where USB Memory Sticks are Born (2013)

**原文链接**: [https://www.bunniestudios.com/blog/2013/where-usb-memory-sticks-are-born/](https://www.bunniestudios.com/blog/2013/where-usb-memory-sticks-are-born/)

生成摘要时出错

---

## 88. Launch HN: Prized (YC S26) – Let non-engineer staff build secure internal tools

**原文标题**: Launch HN: Prized (YC S26) – Let non-engineer staff build secure internal tools

**原文链接**: [https://prized.dev](https://prized.dev)

生成摘要时出错

---

## 89. Advancing the price-performance frontier with GPT‑5.6

**原文标题**: Advancing the price-performance frontier with GPT‑5.6

**原文链接**: [https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/](https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/)

生成摘要时出错

---

## 90. We Gave GPT 5.6 Sol a Real Business. It Lied, Spammed, and Lost $447

**原文标题**: We Gave GPT 5.6 Sol a Real Business. It Lied, Spammed, and Lost $447

**原文链接**: [https://www.bottlenecklabs.com/blog/autonomously-run-businesses](https://www.bottlenecklabs.com/blog/autonomously-run-businesses)

生成摘要时出错

---

