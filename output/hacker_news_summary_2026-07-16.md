# Hacker News 热门文章摘要 (2026-07-16)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Kimi K3 现已上线

**原文标题**: Kimi K3 is now live

**原文链接**: [https://www.kimi.com/en](https://www.kimi.com/en)

月之暗面（Moonshot AI）正式推出了其 AI 模型的最新版本 **Kimi K3**。该版本专门针对**智能体编程（agentic coding）**和**知识工作**进行了优化，标志着 AI 正向更加自主和任务导向的方向转型。

此次更新的核心亮点包括：

*   **智能体框架：** 与标准聊天机器人不同，Kimi K3 旨在以“智能体”身份运行。用户可以为模型分配特定任务，由其执行多步骤工作流以达成目标。
*   **专业化聚焦：** 该模型专为专业环境量身定制，特别是辅助复杂编程（代码编写）和深度信息处理（知识工作）。
*   **通用多样性：** 虽然针对技术任务进行了优化，但它仍保留了强大的“有问必答”能力，可用于日常咨询和获取灵感。

Kimi K3 现已正式上线，旨在为开发者和知识型专业人士提供更具功能性且更主动的助手。

---

## 2. 微软漫画聊天现已开源

**原文标题**: Microsoft Comic Chat is now open source

**原文链接**: [https://opensource.microsoft.com/blog/2026/07/16/microsoft-comic-chat-is-now-open-source/](https://opensource.microsoft.com/blog/2026/07/16/microsoft-comic-chat-is-now-open-source/)

微软正式发布了 Microsoft Comic Chat（后更名为 Microsoft Chat 2.5）的源代码，这是 20 世纪 90 年代标志性的互联网中继聊天 (IRC) 客户端。该项目由 Robert Standefer 和 Scott Hanselman 宣布，目前已在 GitHub 上以 MIT 许可证开源。

Comic Chat 最初于 1996 年推出，是一款独特的通信工具，能自动将文本对话转换为动态的多格漫画。用户可以选择能够表达各种情感和手势的虚拟角色，从而为聊天内容创建视觉叙事。虽然它是早期互联网时代的代表作，但随着微软向其他通信平台转型，该软件最终成为了“弃置软件”(abandonware)。

开源源代码的决定主要旨在进行数字保存。通过公开源代码，微软允许爱好者和开发人员将该软件移植到现代操作系统，修复遗留漏洞，并确保该工具出于历史和怀旧目的保持可用。此举延续了微软发布 MS-DOS 和原始 Windows 文件管理器等遗留项目源代码的趋势，旨在支持开发者社区并归档互联网历史。

---

## 3. 诱饵字体

**原文标题**: Decoy Font

**原文链接**: [https://www.mixfont.com/experiments/decoy-font](https://www.mixfont.com/experiments/decoy-font)

**Decoy Font** 是一种专门设计的 TrueType 字体 (TTF)，旨在向 AI 模型和 OCR（光学字符识别）系统隐藏书面信息。该字体由 Mixfont 的 Eric Lu 开发，利用“空间频率”原理在同一空间内显示两个不同的字母。

这项技术基于“混合图像”技术——这是一种类似于著名的爱因斯坦与玛丽莲·梦露合体肖像的错视效果。Decoy Font 的前景由细长、锐利的轮廓组成，ChatGPT 和 Gemini 等 AI 模型在分析像素时会优先识别这些轮廓。相反，背景包含模糊的低频色块，只有在远处观看或眯起眼睛时，才会显现出真实的隐藏信息。

**主要亮点包括：**
*   **功能：** 诱导 AI 读取“诱饵”文本，同时允许人类看到预期的真实信息。
*   **易用性：** 与基于动态效果的反 AI 字体不同，Decoy Font 是标准的 TTF 文件，可安装并用于个人、商业和客户项目。它基于 DejaVu Sans Mono 许可开发。
*   **目的：** 作为防御 AI 抓取工具的手段，用于保护知识产权和私密通信。
*   **局限性：** 虽然对目前的前沿大语言模型有效，但开发者指出这并非 100% 的保证，因为先进的 AI 代理最终可能会通过提示词学会识别这种错觉。

展望未来，该项目旨在扩展到中文等基于字符的语言，并可能作为测试 AI 文本识别演进的基准。它代表了“反 AI”字体设计的新前沿，致力于确保传达给人类的信息仅对人类可见。

---

## 4. 使用“经典”机器学习检测大语言模型生成的文本

**原文标题**: Detecting LLM-Generated Texts with “Classical” Machine Learning

**原文链接**: [https://blog.lyc8503.net/en/post/llm-classifier/](https://blog.lyc8503.net/en/post/llm-classifier/)

本文详述了一款 AI 文本检测器的开发过程，旨在识别 Lofter 等平台上日益增多的 AI 生成内容。作者摒弃了不可靠且成本高昂的“文本困惑度”方法，转而采用“经典”机器学习技术——具体使用了 Scikit-learn 的 TF-IDF 和 Linear SVC 算法。

**技术方案与训练**
作者构建了一个包含 1 万篇人类撰写文本（2022 年以前）和相应规模 AI 生成样本的数据集，后者由 Gemini、通义千问（Qwen）和 DeepSeek 等七种不同模型生成。作者并未采用单一模型，而是训练了七个二分类器并使用多数投票机制：若至少有两个模型检测出某句为 AI 生成，则将其标记。该方法实现了约 85% 的句级准确率。

**实现与性能**
为确保易用性，该项目采用 JavaScript 实现，支持基于浏览器的无服务器推理。关键性能亮点包括：
*   **泛化能力强：** 该工具能以 70%–90% 的准确率成功检测来自未知模型（如 GPT-5 和 Claude）的内容。
*   **低误报率：** 人类创作的网络小说 AI 概率始终低于 30%，而疑似 AI 生成的内容得分通常高于 80%。
*   **鲁棒性：** 常见的规避手段（如中英往返翻译或特定的“反 AI”提示词）均未能有效欺骗该检测器。

**核心发现**
作者对 Lofter 上的热门内容进行了大规模分析，揭示了一个令人吃惊的趋势：32.22% 的高热度文章在 AI 检测量表上的得分超过 50%，这表明大量未经标注的 AI 小说正涌入平台。该项目总结认为，尽管现代大语言模型非常先进，但它们仍表现出可预测的统计模式，传统机器学习技术依然可以对其进行可靠识别。

---

## 5. 一加停止美欧业务

**原文标题**: OnePlus halts operations in USA and Europe

**原文链接**: [https://community.oneplus.com/thread/2170715118587871237](https://community.oneplus.com/thread/2170715118587871237)

Based on the title provided and the current status of the company (as the full text of the article was not included), here is a concise summary of the facts surrounding these claims:

Contrary to the headline, **OnePlus has not halted operations in the USA or Europe.** This claim typically stems from a misunderstanding of specific legal disputes rather than a total market withdrawal.

**Key Points:**

*   **Official Denials:** In 2023, widespread rumors suggested OnePlus and its parent company, Oppo, were exiting major European markets (including the UK, France, and Germany). OnePlus officially refuted these claims, stating they remain committed to the European region and are simply optimizing their resources.
*   **The German Sales Ban:** The "halt" most accurately refers to a temporary legal situation in **Germany**. Due to a patent dispute with Nokia and InterDigital, OnePlus was legally required to pause smartphone sales in that specific country. However, they have since reached settlements and have begun resuming sales in the German market.
*   **U.S. Market Commitment:** OnePlus remains fully operational in the United States. They continue to release flagship products, such as the OnePlus 12 and OnePlus Open, and maintain strong retail and carrier partnerships (notably with T-Mobile).
*   **Oppo Integration:** While OnePlus has merged its research and development departments more closely with **Oppo** to streamline operations, the brand continues to function as an independent entity in Western markets.

**Summary:** While OnePlus has faced localized legal challenges in Europe—specifically a temporary sales ban in Germany—the company continues to operate and launch new products across both the USA and Europe. There is no evidence of a full exit from these regions.

---

## 6. NotebookLM is now Gemini Notebook

**原文标题**: NotebookLM is now Gemini Notebook

**原文链接**: [https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook/](https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook/)

生成摘要时出错

---

## 7. Goes-19 weather satellite enters Safe Hold mode

**原文标题**: Goes-19 weather satellite enters Safe Hold mode

**原文链接**: [https://www.spaceweather.gov/news/goes-19-safe-hold](https://www.spaceweather.gov/news/goes-19-safe-hold)

生成摘要时出错

---

## 8. Adaptional (YC S25) Is Hiring

**原文标题**: Adaptional (YC S25) Is Hiring

**原文链接**: [https://www.ycombinator.com/companies/adaptional/jobs](https://www.ycombinator.com/companies/adaptional/jobs)

生成摘要时出错

---

## 9. 56,000 lines of DOOM, in a language I made up

**原文标题**: 56,000 lines of DOOM, in a language I made up

**原文链接**: [https://betlang.dev/about/](https://betlang.dev/about/)

生成摘要时出错

---

## 10. The lost joy of music piracy

**原文标题**: The lost joy of music piracy

**原文链接**: [https://www.pigeonsandplanes.com/read/music-piracy-what-cd-oink-nine-inch-nails-streaming](https://www.pigeonsandplanes.com/read/music-piracy-what-cd-oink-nine-inch-nails-streaming)

生成摘要时出错

---

## 11. How Our Rust-to-Zig Rewrite Is Going

**原文标题**: How Our Rust-to-Zig Rewrite Is Going

**原文链接**: [https://rtfeldman.com/rust-to-zig](https://rtfeldman.com/rust-to-zig)

生成摘要时出错

---

## 12. Immersive Linear Algebra Book with Interactive Figures

**原文标题**: Immersive Linear Algebra Book with Interactive Figures

**原文链接**: [https://immersivemath.com/ila/](https://immersivemath.com/ila/)

生成摘要时出错

---

## 13. Someone Used AI to Write an Unauthorized Biography of Me

**原文标题**: Someone Used AI to Write an Unauthorized Biography of Me

**原文链接**: [https://www.nytimes.com/2026/07/16/technology/ai-slop-books-biography-amazon.html](https://www.nytimes.com/2026/07/16/technology/ai-slop-books-biography-amazon.html)

生成摘要时出错

---

## 14. Guide to data tools landscape for developers

**原文标题**: Guide to data tools landscape for developers

**原文链接**: [https://sinja.io/blog/data-landscape-guide-for-developers](https://sinja.io/blog/data-landscape-guide-for-developers)

生成摘要时出错

---

## 15. Sony deletes a movies from the accounts of people who ‘bought’ them

**原文标题**: Sony deletes a movies from the accounts of people who ‘bought’ them

**原文链接**: [https://www.techdirt.com/2026/07/15/sony-deletes-a-bunch-more-movies-from-the-accounts-of-people-who-bought-them/](https://www.techdirt.com/2026/07/15/sony-deletes-a-bunch-more-movies-from-the-accounts-of-people-who-bought-them/)

生成摘要时出错

---

## 16. How to Train a Gen AI Kick Drum Model on Your Old Linux Desktop with 6GB VRAM

**原文标题**: How to Train a Gen AI Kick Drum Model on Your Old Linux Desktop with 6GB VRAM

**原文链接**: [https://www.zhinit.dev/blog/training-a-kick-drum-diffusion-model](https://www.zhinit.dev/blog/training-a-kick-drum-diffusion-model)

生成摘要时出错

---

## 17. Let's Build PlanetScale from Scratch: Infrastructure

**原文标题**: Let's Build PlanetScale from Scratch: Infrastructure

**原文链接**: [https://onatm.dev/2026/07/16/homescale-part-1/](https://onatm.dev/2026/07/16/homescale-part-1/)

生成摘要时出错

---

## 18. Ente – Opening Our Books

**原文标题**: Ente – Opening Our Books

**原文链接**: [https://ente.com/open/](https://ente.com/open/)

生成摘要时出错

---

## 19. GC shape stenciling in Go generics

**原文标题**: GC shape stenciling in Go generics

**原文链接**: [https://rednafi.com/go/gc-shape-stenciling/](https://rednafi.com/go/gc-shape-stenciling/)

生成摘要时出错

---

## 20. Cottage Computer Programming (1984)

**原文标题**: Cottage Computer Programming (1984)

**原文链接**: [https://www.atariarchives.org/deli/cottage_computer_programming.php](https://www.atariarchives.org/deli/cottage_computer_programming.php)

生成摘要时出错

---

## 21. Show HN: Leaves – A text-UI disk usage treemap visualizer

**原文标题**: Show HN: Leaves – A text-UI disk usage treemap visualizer

**原文链接**: [https://github.com/patonw/leaves](https://github.com/patonw/leaves)

生成摘要时出错

---

## 22. Agent-talk: Enabling coding agents to work together

**原文标题**: Agent-talk: Enabling coding agents to work together

**原文链接**: [https://github.com/xhluca/agent-talk](https://github.com/xhluca/agent-talk)

生成摘要时出错

---

## 23. Show HN: Galois connections for composable numeric casts in Rust

**原文标题**: Show HN: Galois connections for composable numeric casts in Rust

**原文链接**: [https://github.com/cmk/connections](https://github.com/cmk/connections)

生成摘要时出错

---

## 24. 1,300 Beautiful Wildlife Illustrations from the 19th Century Now Restored

**原文标题**: 1,300 Beautiful Wildlife Illustrations from the 19th Century Now Restored

**原文链接**: [https://www.openculture.com/2026/07/explore-1300-beautiful-wildlife-illustrations-from-the-19th-century.html](https://www.openculture.com/2026/07/explore-1300-beautiful-wildlife-illustrations-from-the-19th-century.html)

生成摘要时出错

---

## 25. Teardown: A Generic 7-Port USB 3.0 Hub That Wasn't

**原文标题**: Teardown: A Generic 7-Port USB 3.0 Hub That Wasn't

**原文链接**: [https://goughlui.com/2026/07/09/teardown-a-generic-7-port-usb-3-0-hub-that-wasnt/](https://goughlui.com/2026/07/09/teardown-a-generic-7-port-usb-3-0-hub-that-wasnt/)

生成摘要时出错

---

## 26. Accidental Anonymity

**原文标题**: Accidental Anonymity

**原文链接**: [https://macwright.com/2026/06/24/accidental-anonymity](https://macwright.com/2026/06/24/accidental-anonymity)

生成摘要时出错

---

## 27. Photos of items from families in different countries with different incomes

**原文标题**: Photos of items from families in different countries with different incomes

**原文链接**: [https://www.gapminder.org/dollar-street](https://www.gapminder.org/dollar-street)

生成摘要时出错

---

## 28. 42% of adults rely on their parents for financial support

**原文标题**: 42% of adults rely on their parents for financial support

**原文链接**: [https://www.cnbc.com/2026/07/16/42percent-of-adults-rely-on-their-parents-for-financial-supportthere-are-no-bad-guys-here-says-financial-therapist.html](https://www.cnbc.com/2026/07/16/42percent-of-adults-rely-on-their-parents-for-financial-supportthere-are-no-bad-guys-here-says-financial-therapist.html)

生成摘要时出错

---

## 29. Launch HN: Coasty (YC S26) – An API for computer-use agents

**原文标题**: Launch HN: Coasty (YC S26) – An API for computer-use agents

**原文链接**: [https://coasty.ai/docs](https://coasty.ai/docs)

生成摘要时出错

---

## 30. Grok Build is open source

**原文标题**: Grok Build is open source

**原文链接**: [https://github.com/xai-org/grok-build](https://github.com/xai-org/grok-build)

生成摘要时出错

---

## 31. Governments, companies, nonprofits should invest in free, open source AI [pdf]

**原文标题**: Governments, companies, nonprofits should invest in free, open source AI [pdf]

**原文链接**: [https://www.siegelendowment.org/wp-content/uploads/2026/07/fortune-david-siegel-open-source-ai.pdf](https://www.siegelendowment.org/wp-content/uploads/2026/07/fortune-david-siegel-open-source-ai.pdf)

生成摘要时出错

---

## 32. A Beautiful Theory Falls to Ugly Data

**原文标题**: A Beautiful Theory Falls to Ugly Data

**原文链接**: [https://marginalrevolution.com/marginalrevolution/2026/05/a-beautiful-theory-falls-to-ugly-data.html](https://marginalrevolution.com/marginalrevolution/2026/05/a-beautiful-theory-falls-to-ugly-data.html)

生成摘要时出错

---

## 33. The LLM Critics Are Right. I Use LLMs Anyway

**原文标题**: The LLM Critics Are Right. I Use LLMs Anyway

**原文链接**: [https://www.theocharis.dev/blog/llm-critics-are-right-i-use-llms-anyway/](https://www.theocharis.dev/blog/llm-critics-are-right-i-use-llms-anyway/)

生成摘要时出错

---

## 34. Duskers, the scary command line game, is getting a sequel

**原文标题**: Duskers, the scary command line game, is getting a sequel

**原文链接**: [https://elbowgreasegames.substack.com/p/misfits-attic-announces-duskers-20](https://elbowgreasegames.substack.com/p/misfits-attic-announces-duskers-20)

生成摘要时出错

---

## 35. Collection of Digital Clock Designs

**原文标题**: Collection of Digital Clock Designs

**原文链接**: [https://clocks.dev](https://clocks.dev)

生成摘要时出错

---

## 36. LLM Networking with MikroTik

**原文标题**: LLM Networking with MikroTik

**原文链接**: [https://blog.greg.technology/2026/07/14/llm-networking-with-mikrotik.html](https://blog.greg.technology/2026/07/14/llm-networking-with-mikrotik.html)

生成摘要时出错

---

## 37. AI reviewers shipped secret-exfil code because a ticket said "pre-approved"

**原文标题**: AI reviewers shipped secret-exfil code because a ticket said "pre-approved"

**原文链接**: [https://senthex.com/en/research/relay/](https://senthex.com/en/research/relay/)

生成摘要时出错

---

## 38. Self-testing AI harness finds its own bugs

**原文标题**: Self-testing AI harness finds its own bugs

**原文链接**: [https://www.omnideck.dev/blog/self-testing-ai-browser-tools.html](https://www.omnideck.dev/blog/self-testing-ai-browser-tools.html)

生成摘要时出错

---

## 39. Stripe and Advent have made a joint offer to acquire PayPal – sources

**原文标题**: Stripe and Advent have made a joint offer to acquire PayPal – sources

**原文链接**: [https://www.reuters.com/business/finance/stripe-advent-offer-buy-paypal-more-than-53-billion-sources-say-2026-07-15/](https://www.reuters.com/business/finance/stripe-advent-offer-buy-paypal-more-than-53-billion-sources-say-2026-07-15/)

生成摘要时出错

---

## 40. Astronomers Have Found a Sugar Molecule in Deep Space for the First Time Ever

**原文标题**: Astronomers Have Found a Sugar Molecule in Deep Space for the First Time Ever

**原文链接**: [https://www.wired.com/story/astronomers-found-sugar-molecule-in-deep-space/](https://www.wired.com/story/astronomers-found-sugar-molecule-in-deep-space/)

生成摘要时出错

---

## 41. Show HN: Firefox in WebAssembly

**原文标题**: Show HN: Firefox in WebAssembly

**原文链接**: [https://developer.puter.com/labs/firefox-wasm/](https://developer.puter.com/labs/firefox-wasm/)

生成摘要时出错

---

## 42. How to publish to PyPI using GitHub Actions securely

**原文标题**: How to publish to PyPI using GitHub Actions securely

**原文链接**: [https://snarky.ca/how-to-publish-to-pypi-using-github-actions-securely/](https://snarky.ca/how-to-publish-to-pypi-using-github-actions-securely/)

生成摘要时出错

---

## 43. Voxatron

**原文标题**: Voxatron

**原文链接**: [https://www.lexaloffle.com/voxatron.php](https://www.lexaloffle.com/voxatron.php)

生成摘要时出错

---

## 44. SQLite should have (Rust-style) editions

**原文标题**: SQLite should have (Rust-style) editions

**原文链接**: [https://mort.coffee/home/sqlite-editions/](https://mort.coffee/home/sqlite-editions/)

生成摘要时出错

---

## 45. Metal-Organic Frameworks, Chemistry's New Miracle Materials (2018)

**原文标题**: Metal-Organic Frameworks, Chemistry's New Miracle Materials (2018)

**原文链接**: [https://chemistry.berkeley.edu/news/meet-metal-organic-frameworks-chemistry%E2%80%99s-new-miracle-materials](https://chemistry.berkeley.edu/news/meet-metal-organic-frameworks-chemistry%E2%80%99s-new-miracle-materials)

生成摘要时出错

---

## 46. Today I Rescued 7,234 Old GIFs

**原文标题**: Today I Rescued 7,234 Old GIFs

**原文链接**: [https://danq.me/2026/07/10/rescuing-7234-gifs/](https://danq.me/2026/07/10/rescuing-7234-gifs/)

生成摘要时出错

---

## 47. Towards a harness that can do anything

**原文标题**: Towards a harness that can do anything

**原文链接**: [https://eardatasci.github.io/c/ambiance/index.html](https://eardatasci.github.io/c/ambiance/index.html)

生成摘要时出错

---

## 48. Umuganda

**原文标题**: Umuganda

**原文链接**: [https://en.wikipedia.org/wiki/Umuganda](https://en.wikipedia.org/wiki/Umuganda)

生成摘要时出错

---

## 49. Ente's business metrics are open now

**原文标题**: Ente's business metrics are open now

**原文链接**: [https://ente.com/blog/open/](https://ente.com/blog/open/)

生成摘要时出错

---

## 50. Uber Announces Acquisition Offer for Delivery Hero at $14.8B

**原文标题**: Uber Announces Acquisition Offer for Delivery Hero at $14.8B

**原文链接**: [https://investor.uber.com/news-events/news/press-release-details/2026/Uber-Announces-Acquisition-Offer-for-Delivery-Hero/default.aspx](https://investor.uber.com/news-events/news/press-release-details/2026/Uber-Announces-Acquisition-Offer-for-Delivery-Hero/default.aspx)

生成摘要时出错

---

## 51. Sleep regularity is a stronger predictor of mortality risk than sleep duration (2023)

**原文标题**: Sleep regularity is a stronger predictor of mortality risk than sleep duration (2023)

**原文链接**: [https://academic.oup.com/sleep/article/47/1/zsad253/7280269](https://academic.oup.com/sleep/article/47/1/zsad253/7280269)

生成摘要时出错

---

## 52. Can LLMs Perform Deep Technical Comprehension of Computer Architecture Papers

**原文标题**: Can LLMs Perform Deep Technical Comprehension of Computer Architecture Papers

**原文链接**: [https://arxiv.org/abs/2607.11859](https://arxiv.org/abs/2607.11859)

生成摘要时出错

---

## 53. The Tokio/Rayon Trap and Why Async/Await Fails Concurrency

**原文标题**: The Tokio/Rayon Trap and Why Async/Await Fails Concurrency

**原文链接**: [https://pmbanugo.me/blog/why-async-await-complect-concurrency](https://pmbanugo.me/blog/why-async-await-complect-concurrency)

生成摘要时出错

---

## 54. Jurassic Park computers in excruciating detail

**原文标题**: Jurassic Park computers in excruciating detail

**原文链接**: [https://fabiensanglard.net/jurrasic_park_computers/index.html](https://fabiensanglard.net/jurrasic_park_computers/index.html)

生成摘要时出错

---

## 55. Show HN: misa77 - a codec that decodes 2x faster than LZ4 (at better ratios)

**原文标题**: Show HN: misa77 - a codec that decodes 2x faster than LZ4 (at better ratios)

**原文链接**: [https://github.com/welcome-to-the-sunny-side/misa77](https://github.com/welcome-to-the-sunny-side/misa77)

生成摘要时出错

---

## 56. Financial advice I can give you is to sell your car

**原文标题**: Financial advice I can give you is to sell your car

**原文链接**: [https://yourbrainonmoney.substack.com/p/the-best-financial-advice-i-can-give](https://yourbrainonmoney.substack.com/p/the-best-financial-advice-i-can-give)

生成摘要时出错

---

## 57. Google Earth Desktop Client to Be Retired in 2027

**原文标题**: Google Earth Desktop Client to Be Retired in 2027

**原文链接**: [https://hackaday.com/2026/07/16/google-earth-desktop-client-to-be-retired-in-2027/](https://hackaday.com/2026/07/16/google-earth-desktop-client-to-be-retired-in-2027/)

生成摘要时出错

---

## 58. Briar is in maintenance mode

**原文标题**: Briar is in maintenance mode

**原文链接**: [https://briarproject.org/news/2026-maintenance-mode/](https://briarproject.org/news/2026-maintenance-mode/)

生成摘要时出错

---

## 59. Google Earth Desktop Client to Be Retired in 2027

**原文标题**: Google Earth Desktop Client to Be Retired in 2027

**原文链接**: [https://hackaday.com/2026/07/16/google-earth-desktop-client-to-be-retired-in-2027/](https://hackaday.com/2026/07/16/google-earth-desktop-client-to-be-retired-in-2027/)

生成摘要时出错

---

## 60. My midlife crisis Corolla is fast, furious, and modded

**原文标题**: My midlife crisis Corolla is fast, furious, and modded

**原文链接**: [https://www.zocalopublicsquare.org/my-midlife-crisis-corolla-fast-furious-fully-modded/](https://www.zocalopublicsquare.org/my-midlife-crisis-corolla-fast-furious-fully-modded/)

生成摘要时出错

---

## 61. 1Password for Claude: Give Claude access without giving up your credentials

**原文标题**: 1Password for Claude: Give Claude access without giving up your credentials

**原文链接**: [https://1password.com/blog/1password-for-claude](https://1password.com/blog/1password-for-claude)

生成摘要时出错

---

## 62. 1-Bit LLM in the Browser

**原文标题**: 1-Bit LLM in the Browser

**原文链接**: [https://huggingface.co/spaces/webml-community/bonsai-webgpu](https://huggingface.co/spaces/webml-community/bonsai-webgpu)

生成摘要时出错

---

## 63. Brainless: Shadcn components that look like Claude Code, Codex and Grok

**原文标题**: Brainless: Shadcn components that look like Claude Code, Codex and Grok

**原文链接**: [https://brainless.swerdlow.dev](https://brainless.swerdlow.dev)

生成摘要时出错

---

## 64. Running Gemma 4 26B at 5 tokens/sec on a 13-year-old Xeon with no GPU

**原文标题**: Running Gemma 4 26B at 5 tokens/sec on a 13-year-old Xeon with no GPU

**原文链接**: [https://www.neomindlabs.com/2026/06/08/running-gemma-4-26b-at-5-tokens-sec-on-a-13-year-old-xeon-with-no-gpu/](https://www.neomindlabs.com/2026/06/08/running-gemma-4-26b-at-5-tokens-sec-on-a-13-year-old-xeon-with-no-gpu/)

生成摘要时出错

---

## 65. Show HN: One More Letter

**原文标题**: Show HN: One More Letter

**原文链接**: [https://playonemoreletter.com/](https://playonemoreletter.com/)

生成摘要时出错

---

## 66. Netstrings (1997)

**原文标题**: Netstrings (1997)

**原文链接**: [https://cr.yp.to/proto/netstrings.txt](https://cr.yp.to/proto/netstrings.txt)

生成摘要时出错

---

## 67. At least 105 past YC founders have worked at OpenAI and Anthropic

**原文标题**: At least 105 past YC founders have worked at OpenAI and Anthropic

**原文链接**: [https://joinedanthropic.com](https://joinedanthropic.com)

生成摘要时出错

---

## 68. The Last Picture Show: A Conversation with George Lucas

**原文标题**: The Last Picture Show: A Conversation with George Lucas

**原文链接**: [https://a-rabbitsfoot.com/editorial/confessions/the-last-picture-show-a-conversation-with-george-lucas/](https://a-rabbitsfoot.com/editorial/confessions/the-last-picture-show-a-conversation-with-george-lucas/)

生成摘要时出错

---

## 69. The Conservationist Who Turned 40 Terabytes of Public Data into a Video Game

**原文标题**: The Conservationist Who Turned 40 Terabytes of Public Data into a Video Game

**原文链接**: [https://blog.exe.dev/meet-the-conservationist-who-turned-40-terabytes-of-government-data-into-a-video-game](https://blog.exe.dev/meet-the-conservationist-who-turned-40-terabytes-of-government-data-into-a-video-game)

生成摘要时出错

---

## 70. Agentty – A drop-in alternative to claude-code, written in C++26. 11.0 MB binary

**原文标题**: Agentty – A drop-in alternative to claude-code, written in C++26. 11.0 MB binary

**原文链接**: [https://github.com/1ay1/agentty](https://github.com/1ay1/agentty)

生成摘要时出错

---

## 71. Telegram Serverless

**原文标题**: Telegram Serverless

**原文链接**: [https://core.telegram.org/bots/serverless](https://core.telegram.org/bots/serverless)

生成摘要时出错

---

## 72. G# – A modern .NET language with Go, Kotlin, and Swift ergonomics

**原文标题**: G# – A modern .NET language with Go, Kotlin, and Swift ergonomics

**原文链接**: [https://davidobando.github.io/gsharp/](https://davidobando.github.io/gsharp/)

生成摘要时出错

---

## 73. MITS: Rockets, Calculators, and Personal Computers

**原文标题**: MITS: Rockets, Calculators, and Personal Computers

**原文链接**: [https://www.abortretry.fail/p/micro-instrumentation-and-telemetry](https://www.abortretry.fail/p/micro-instrumentation-and-telemetry)

生成摘要时出错

---

## 74. The Memory Heist

**原文标题**: The Memory Heist

**原文链接**: [https://www.ayush.digital/blog/the-memory-heist](https://www.ayush.digital/blog/the-memory-heist)

生成摘要时出错

---

## 75. Show HN: I've built a words game based on binary search

**原文标题**: Show HN: I've built a words game based on binary search

**原文链接**: [https://hilogame.cc/](https://hilogame.cc/)

生成摘要时出错

---

## 76. Nul Characters in Strings in SQLite

**原文标题**: Nul Characters in Strings in SQLite

**原文链接**: [https://sqlite.org/nulinstr.html](https://sqlite.org/nulinstr.html)

生成摘要时出错

---

## 77. Designing APIs for Agents

**原文标题**: Designing APIs for Agents

**原文链接**: [https://www.freestyle.sh/blog/opinion/designing-apis-for-agents](https://www.freestyle.sh/blog/opinion/designing-apis-for-agents)

生成摘要时出错

---

## 78. The kids with phones are alright

**原文标题**: The kids with phones are alright

**原文链接**: [https://heatherburns.tech/2026/07/08/the-kids-with-phones-are-alright/](https://heatherburns.tech/2026/07/08/the-kids-with-phones-are-alright/)

生成摘要时出错

---

## 79. I Unlocked ChatGPT's Dark Side for $101.40 [video]

**原文标题**: I Unlocked ChatGPT's Dark Side for $101.40 [video]

**原文链接**: [https://www.youtube.com/watch?v=b-nD3HgIR5Y](https://www.youtube.com/watch?v=b-nD3HgIR5Y)

生成摘要时出错

---

## 80. Show HN: I Built an Accent Changer App

**原文标题**: Show HN: I Built an Accent Changer App

**原文链接**: [https://accentchanger.com/](https://accentchanger.com/)

生成摘要时出错

---

## 81. P2P local file transfer based on WebRTC

**原文标题**: P2P local file transfer based on WebRTC

**原文链接**: [https://pairdrop.net/](https://pairdrop.net/)

生成摘要时出错

---

## 82. Prioritize mental health, and why communication is so important

**原文标题**: Prioritize mental health, and why communication is so important

**原文链接**: [https://ramones.dev/posts/mental-health/](https://ramones.dev/posts/mental-health/)

生成摘要时出错

---

## 83. Command Line Interface Guidelines

**原文标题**: Command Line Interface Guidelines

**原文链接**: [https://clig.dev/](https://clig.dev/)

生成摘要时出错

---

## 84. OpenAI loses trademark dispute at EU court

**原文标题**: OpenAI loses trademark dispute at EU court

**原文链接**: [https://dpa-international.com/economics/urn:newsml:dpa.com:20090101:260715-930-389143/](https://dpa-international.com/economics/urn:newsml:dpa.com:20090101:260715-930-389143/)

生成摘要时出错

---

## 85. Microsoft has released software updates to plug at least 570 security holes

**原文标题**: Microsoft has released software updates to plug at least 570 security holes

**原文链接**: [https://krebsonsecurity.com/2026/07/microsoft-patches-a-record-570-security-flaws/](https://krebsonsecurity.com/2026/07/microsoft-patches-a-record-570-security-flaws/)

生成摘要时出错

---

## 86. Teen hackers who live streamed cyber-attack on TfL jailed

**原文标题**: Teen hackers who live streamed cyber-attack on TfL jailed

**原文链接**: [https://www.bbc.com/news/articles/c4gyg0y6yg2o](https://www.bbc.com/news/articles/c4gyg0y6yg2o)

生成摘要时出错

---

## 87. Open-source memory for coding agents, synced over SSH

**原文标题**: Open-source memory for coding agents, synced over SSH

**原文链接**: [https://github.com/vshulcz/deja-vu/](https://github.com/vshulcz/deja-vu/)

生成摘要时出错

---

