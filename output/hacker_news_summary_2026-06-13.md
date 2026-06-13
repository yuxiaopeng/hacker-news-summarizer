# Hacker News 热门文章摘要 (2026-06-13)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 美国禁止在人口普查数据中使用差分隐私。

**原文标题**: US bans differential privacy in Census data

**原文链接**: [https://desfontain.es/blog/banning-noise.html](https://desfontain.es/blog/banning-noise.html)

美国商务部最近发布了一项禁令，禁止人口普查局和经济分析局发布的统计产品使用“噪声注入”（特别是差分隐私）。这标志着政府在权衡公共数据效用与个人隐私保护方面发生了重大转变。

2020年人口普查采用了差分隐私技术，因为研究人员发现此前采用的“数据交换”等方法可能会导致个人记录被重构，从而违反联邦保密法。虽然差分隐私因其量化和缓解隐私风险的能力被科学家视为“金标准”，但它引入的透明“噪声”降低了数据的准确性。这令人口统计学家、社会科学家以及利用精确数据进行选区划分等任务的政治操盘手感到沮丧。

新指令要求回归“粗化”（数据泛化）和“抑制”（不公开小型数据集）等手段。作者认为这些工具既生硬又过时。对于人口普查等复杂数据集，这些技术往往会导致“双输”局面：要么破坏了数据的效用（尤其是对少数群体而言），要么使个人面临重新识别攻击的风险。如果没有噪声注入所提供的数学不确定性，攻击者想要破解个人身份将变得轻而易举。

该禁令背后的动机尚不明确。这可能是在尝试为政治目的提供重新识别的便利，也可能是为了隐瞒人口差异数据，或者仅仅是官僚机构试图忽视数据准确性与隐私之间固有的权衡。无论意图如何，作者警告称，这一决定可能导致未来发布的统计数据要么“极其危险”，要么“毫无用处”。

---

## 2. 治疗胰腺肿瘤可能已揭示癌症的总开关

**原文标题**: Treating pancreatic tumours may have revealed cancer's master switch

**原文链接**: [https://economist.com/science-and-technology/2026/06/12/treating-pancreatic-tumours-may-have-revealed-cancers-master-switch](https://economist.com/science-and-technology/2026/06/12/treating-pancreatic-tumours-may-have-revealed-cancers-master-switch)

无法访问文章链接。

---

## 3. 每一帧都完美

**原文标题**: Every Frame Perfect

**原文链接**: [https://tonsky.me/blog/every-frame-perfect/](https://tonsky.me/blog/every-frame-perfect/)

生成摘要时出错

---

## 4. 领略 Exif

**原文标题**: Appreciating Exif

**原文链接**: [https://brentfitzgerald.com/posts/appreciating-exif/](https://brentfitzgerald.com/posts/appreciating-exif/)

《深入理解 Exif》对**可交换图像文件格式 (Exif)** 进行了技术与实践层面的概述，该格式是数字图像中嵌入元数据的标准。Exif 创立于 1995 年，允许相机直接在图像文件中存储关键数据，如时间戳、GPS 坐标、相机设置和方向。

文章强调了几个关键技术方面：
*   **结构：** Exif 是一种嵌套在其他文件格式中的 TIFF 型数据结构。在 JPEG 文件中，它通常位于文件开头附近的 **APP1 标记段**。
*   **方向：** Exif 最关键的用途之一是**方向标签 (Orientation tag)**（取值为 1–8）。大多数相机不会旋转实际的像素矩阵，而是写入一个标签告知查看器如何显示像素。开发者在处理像素前应进行“归一化”或“自动旋转”，以避免显示错误。
*   **工具：** 作者将 **exiftool** 视为检查、编辑和清除元数据的行业标准，并指出它能够揭示厂商注释 (MakerNotes) 和嵌入缩略图等隐藏细节。
*   **更广泛的背景：** Exif 有别于其他元数据标准，如 **XMP**（Adobe 工作流）、**IPTC**（新闻摄影）、**ICC 配置文件**（色彩管理）以及较新的 **C2PA**（来源/AI 签名）。
*   **隐私与安全：** 操作系统或浏览器很少会自动清除元数据。如果用户和开发者希望保护位置或设备隐私，必须主动将其删除。

作者总结道，虽然 Exif 是一个带有一些局限性的“老旧”标准，但它仍然是一个稳健且必要的解决方案，确保图像携带必要的上下文信息，以便现代软件能对其进行正确的显示和组织。

---

## 5. Show HN: Verso – A $14.99 Mac word processor with no subscription

**原文标题**: Show HN: Verso – A $14.99 Mac word processor with no subscription

**原文链接**: [https://www.versowriter.app](https://www.versowriter.app)

**Verso** is a native macOS word processor designed as a lightweight, subscription-free alternative to bloated software like Microsoft Word. Available for a one-time purchase of **$14.99** (with a 7-day free trial), it targets writers who want a fast, "no-nonsense" experience without recurring fees or tracking.

**Key Features:**
*   **Focus & UI:** A "Focus Mode" that fades out everything except the current paragraph, alongside five page colors (including dark mode) and a customizable toolbar.
*   **Compatibility:** Full support for opening and saving `.docx` files without formatting breaks. It also handles `.odt`, `.rtf`, and `.pdf` exports.
*   **Editing Tools:** Includes a "Track Changes" system with a sidebar for managing edits, comments, footnotes, auto-generated Tables of Contents, and LaTeX math support.
*   **Developer-Friendly:** Unique "round-trip" Markdown support allows users to edit `.md` files as rich text. It includes syntax highlighting for 22 programming languages and live-rendering for Mermaid diagrams.
*   **Performance:** Built specifically for Mac (macOS 14+), the app features instant launch times, offline functionality, and native localization in 16 languages.

Created by developer Tomasz, Verso positions itself between over-engineered office suites and overly simplistic text editors. By offering a permanent license for a fraction of the cost of competitors like Ulysses or iA Writer, Verso aims to provide a high-value, privacy-conscious tool for the modern Mac writer.

---

## 6. 阿拉伯语排版渲染经验与技术债简介

**原文标题**: Introduction to the experience of rendering Arabic typography&its technical debt

**原文链接**: [https://lr0.org/blog/p/arabic/](https://lr0.org/blog/p/arabic/)

本文探讨了在数字平台上渲染阿拉伯语排版的巨大技术与历史挑战，强调了将复杂的文字系统强行套入为拉丁文字设计的标准所造成的“技术债”。

作者指出了数字阿拉伯语渲染中的三个核心问题：

1. **对齐逻辑：** 拉丁文字通过拉伸单词间的间距来实现两端对齐，而古典阿拉伯语排版则使用“喀希达”（kashida，又称 tatwīl）——即拉伸字母本身的笔画。现代网络标准（CSS）往往不支持这一特性，导致文本边缘参差不齐，或者出现视觉上虽通顺但在传统上错误的词间距。
2. **塑形引擎：** 阿拉伯语天生具有连写性；字母会根据相邻字符改变形状（分为词首、词中、词尾或独立形式）。这意味着阿拉伯语文本是在渲染时由“塑形引擎”实时生成的。当软件缺乏这种引擎时（常见于旧版 PDF 库或简单的图形工具），字母会呈现断开状态，无法阅读。
3. **遗留编码与技术债：** 作者解释了由 Unicode “阿拉伯语表现形式”（Arabic Presentation Forms）引起的一种常见数据库“漏洞”。这些是 20 世纪 90 年代遗留下来的旧码位，编码的是具体的字母形状而非抽象字母。虽然它们在外观上与现代 Unicode 相同，但数字签名不同，除非经过适当的标准化（NFKC）处理，否则会导致搜索失败和数据不匹配。

阿拉伯语书法根植于由伊本·穆格莱（Ibn Muqla）等书法家制定的、拥有千年历史的比例系统（al-khaṭṭ al-mansūb），该系统将对齐视为一种“塑形”问题而非“间距”问题。作者总结道，阿拉伯语在网络上呈现出的“破碎”状态——从字母无法连接到错误的对齐方式——本质上是数百年的书法传统与并未考虑其独特逻辑的数字工具之间碰撞的结果。

---

## 7. 基于废旧手机的低碳计算平台

**原文标题**: A low-carbon computing platform from your retired phones

**原文链接**: [https://research.google/blog/a-low-carbon-computing-platform-from-your-retired-phones/](https://research.google/blog/a-low-carbon-computing-platform-from-your-retired-phones/)

为了应对硬件制造对环境的影响——特别是“隐含碳”排放——加州大学圣迭戈分校的研究人员在谷歌的支持下，正在开发一个“手机集群计算”平台。该项目将退役智能手机改造为低碳、低成本的云计算基础设施。

由于消费者通常每四年更换一次手机，许多拥有高性能且完好处理器的设备被过早弃用。研究人员发现，现代智能手机核心的单线程性能往往可以与服务器级处理器相媲美。通过提取占设备隐含碳约50%的主板，并拆除电池和屏幕等不必要或危险的组件，团队能够构建出高效的计算集群。

该项目的关键技术点包括：
*   **操作系统：** 采用通用Linux发行版取代面向移动端的安卓系统，以提高可编程性并消除针对消费者的特定限制。
*   **编排：** 使用Kubernetes管理跨集群的容器化应用。
*   **规模：** 基准测试表明，25至50部手机即可提供相当于一台现代服务器的算力。

加州大学圣迭戈分校计划在2026年秋季前部署一个包含2,000部手机的数据中心，提供相当于50台传统服务器的算力。该平台将为计算机科学专业的学生和研究人员提供支持，用于自动评分和托管Jupyter Notebook等任务。一个20部手机集群的早期实验成功处理了超过75名学生班级的峰值作业提交，性能达到甚至超过了传统的云端后端。该项目既是一个实用的计算资源，也是测试消费级硬件在持续运行的数据中心环境中可靠性的试验场。

---

## 8. Intel 8087 浮点芯片的核心加法器

**原文标题**: The adder at the heart of Intel's 8087 floating-point chip

**原文链接**: [https://www.righto.com/2026/06/intel-8087-adder-reverse-engineered.html](https://www.righto.com/2026/06/intel-8087-adder-reverse-engineered.html)

生成摘要时出错

---

## 9. GLM 5.2 Is Out

**原文标题**: GLM 5.2 Is Out

**原文链接**: [https://digg.com/tech/ii9xibgn](https://digg.com/tech/ii9xibgn)

Z.ai has announced the launch of **GLM-5.2**, its new flagship AI model designed to provide open and accessible intelligence for developers. 

Key details of the release include:

*   **Immediate Availability:** The model is currently accessible to all GLM Coding Plan users, including those on Lite, Pro, Max, and Team plans.
*   **Technical Capabilities:** GLM-5.2 features advanced coding power, a massive **1-million-token context window**, and high performance in complex, long-horizon tasks.
*   **Upcoming Services:** API access and dedicated chatbot services are scheduled to launch next week.
*   **Open Source Commitment:** In line with Z.ai’s mission to democratize AI, the model will be officially open-sourced next week under the **MIT License**.

This release positions GLM-5.2 as a major tool for the global developer community, emphasizing high-capacity performance and an open-source philosophy.

---

## 10. AI OSS tool repo goes archived over night after raising $7.3M Seed

**原文标题**: AI OSS tool repo goes archived over night after raising $7.3M Seed

**原文链接**: [https://github.com/tensorzero/tensorzero](https://github.com/tensorzero/tensorzero)

生成摘要时出错

---

## 11. Amazon CEO's Talks with U.S. Officials Triggered Crackdown on Anthropic Models

**原文标题**: Amazon CEO's Talks with U.S. Officials Triggered Crackdown on Anthropic Models

**原文链接**: [https://www.wsj.com/tech/ai/amazon-ceos-talks-with-u-s-officials-triggered-crackdown-on-anthropic-models-dcc90578](https://www.wsj.com/tech/ai/amazon-ceos-talks-with-u-s-officials-triggered-crackdown-on-anthropic-models-dcc90578)

生成摘要时出错

---

## 12. Electric motors with no rare earths

**原文标题**: Electric motors with no rare earths

**原文链接**: [https://www.renaultgroup.com/en/magazine/energy-and-powertrains/all-about-electric-motors-with-no-rare-earths/](https://www.renaultgroup.com/en/magazine/energy-and-powertrains/all-about-electric-motors-with-no-rare-earths/)

生成摘要时出错

---

## 13. Show HN: I am building a map of people who lived in the Roman Empire

**原文标题**: Show HN: I am building a map of people who lived in the Roman Empire

**原文链接**: [https://new.roman-names.com/](https://new.roman-names.com/)

生成摘要时出错

---

## 14. RTX 5080 and RTX 3090 Setup: 80 Tok/s on Qwen 3.6 27B Q8

**原文标题**: RTX 5080 and RTX 3090 Setup: 80 Tok/s on Qwen 3.6 27B Q8

**原文链接**: [https://imil.net/blog/posts/2026/rtx-5080-+-rtx-3090-setup-80+-tok-s-on-qwen-3.6-27b-q8/](https://imil.net/blog/posts/2026/rtx-5080-+-rtx-3090-setup-80+-tok-s-on-qwen-3.6-27b-q8/)

生成摘要时出错

---

## 15. The state of building user interfaces in Rust

**原文标题**: The state of building user interfaces in Rust

**原文链接**: [https://areweguiyet.com/#ecosystem](https://areweguiyet.com/#ecosystem)

生成摘要时出错

---

## 16. Show HN: Paca – Lightweight Jira alternative for human-AI collaboration

**原文标题**: Show HN: Paca – Lightweight Jira alternative for human-AI collaboration

**原文链接**: [https://github.com/Paca-AI/paca](https://github.com/Paca-AI/paca)

生成摘要时出错

---

## 17. An Interview with Intel's Kira Boyko: Xeon 6's Product Director

**原文标题**: An Interview with Intel's Kira Boyko: Xeon 6's Product Director

**原文链接**: [https://chipsandcheese.com/p/an-interview-with-intels-kira-boyko](https://chipsandcheese.com/p/an-interview-with-intels-kira-boyko)

生成摘要时出错

---

## 18. Statement on US government directive to suspend access to Fable 5 and Mythos 5

**原文标题**: Statement on US government directive to suspend access to Fable 5 and Mythos 5

**原文链接**: [https://www.anthropic.com/news/fable-mythos-access](https://www.anthropic.com/news/fable-mythos-access)

生成摘要时出错

---

## 19. Trophic memory, deer, and a unique scientific object

**原文标题**: Trophic memory, deer, and a unique scientific object

**原文链接**: [https://thoughtforms.life/trophic-memory-deer-and-a-truly-unique-scientific-object/](https://thoughtforms.life/trophic-memory-deer-and-a-truly-unique-scientific-object/)

生成摘要时出错

---

## 20. AI Coding at Home Without Going Broke

**原文标题**: AI Coding at Home Without Going Broke

**原文链接**: [https://stephen.bochinski.dev/blog/2026/06/13/ai-coding-at-home-without-going-broke/](https://stephen.bochinski.dev/blog/2026/06/13/ai-coding-at-home-without-going-broke/)

生成摘要时出错

---

## 21. Arch Linux Now Believes Malware Incident Under Control: More Than 1,500 Packages

**原文标题**: Arch Linux Now Believes Malware Incident Under Control: More Than 1,500 Packages

**原文链接**: [https://www.phoronix.com/news/Arch-Linux-AUR-More-Than-1500](https://www.phoronix.com/news/Arch-Linux-AUR-More-Than-1500)

生成摘要时出错

---

## 22. Open source AI must win

**原文标题**: Open source AI must win

**原文链接**: [https://opensourceaimustwin.com/?share=v2](https://opensourceaimustwin.com/?share=v2)

生成摘要时出错

---

## 23. The computer science degree isn’t dead

**原文标题**: The computer science degree isn’t dead

**原文链接**: [https://spectrum.ieee.org/computer-science-degree-isnt-dead](https://spectrum.ieee.org/computer-science-degree-isnt-dead)

生成摘要时出错

---

## 24. How to setup a local coding agent on macOS

**原文标题**: How to setup a local coding agent on macOS

**原文链接**: [https://ikyle.me/blog/2026/how-to-setup-a-local-coding-agent-on-macos](https://ikyle.me/blog/2026/how-to-setup-a-local-coding-agent-on-macos)

生成摘要时出错

---

## 25. Show HN: Putt.day a daily mini golf game

**原文标题**: Show HN: Putt.day a daily mini golf game

**原文链接**: [https://putt.day/](https://putt.day/)

生成摘要时出错

---

## 26. Shepherd's Dog: A Game by the Most Dangerous AI Model

**原文标题**: Shepherd's Dog: A Game by the Most Dangerous AI Model

**原文链接**: [https://koenvangilst.nl/lab/claude-fable-shepherds-dog](https://koenvangilst.nl/lab/claude-fable-shepherds-dog)

生成摘要时出错

---

## 27. Show HN: 2 Weeks of Hallucinate – The Photo Gallery

**原文标题**: Show HN: 2 Weeks of Hallucinate – The Photo Gallery

**原文链接**: [https://hallucinate.site/gallery](https://hallucinate.site/gallery)

生成摘要时出错

---

## 28. Malware developers added nuclear and biological weapons text to to their spyware

**原文标题**: Malware developers added nuclear and biological weapons text to to their spyware

**原文链接**: [https://twitter.com/jsrailton/status/2064661778978533571](https://twitter.com/jsrailton/status/2064661778978533571)

生成摘要时出错

---

## 29. Leaving Mozilla

**原文标题**: Leaving Mozilla

**原文链接**: [https://blog.unitedheroes.net/5751](https://blog.unitedheroes.net/5751)

生成摘要时出错

---

## 30. PwC Report: AI Making Medical Bills Higher

**原文标题**: PwC Report: AI Making Medical Bills Higher

**原文链接**: [https://fortune.com/2026/06/12/ai-making-medical-bills-higher/](https://fortune.com/2026/06/12/ai-making-medical-bills-higher/)

生成摘要时出错

---

## 31. H.R. 6028 would fundamentally change the U.S. Copyright Office

**原文标题**: H.R. 6028 would fundamentally change the U.S. Copyright Office

**原文链接**: [https://www.eff.org/deeplinks/2026/06/congress-just-rushed-through-disastrous-copyright-office-overhaul](https://www.eff.org/deeplinks/2026/06/congress-just-rushed-through-disastrous-copyright-office-overhaul)

生成摘要时出错

---

## 32. Twenty One Zero-Days in FFmpeg

**原文标题**: Twenty One Zero-Days in FFmpeg

**原文链接**: [https://depthfirst.com/research/21-zero-days-in-ffmpeg](https://depthfirst.com/research/21-zero-days-in-ffmpeg)

生成摘要时出错

---

## 33. Swift at Apple: Migrating the TrueType hinting interpreter

**原文标题**: Swift at Apple: Migrating the TrueType hinting interpreter

**原文链接**: [https://www.swift.org/blog/migrating-truetype-hinting-to-swift/](https://www.swift.org/blog/migrating-truetype-hinting-to-swift/)

生成摘要时出错

---

## 34. There is a shadow hanging over this Fable thing

**原文标题**: There is a shadow hanging over this Fable thing

**原文链接**: [https://12gramsofcarbon.com/p/tech-things-there-is-a-massive-shadow](https://12gramsofcarbon.com/p/tech-things-there-is-a-massive-shadow)

生成摘要时出错

---

## 35. CRISPR tech selectively shreds cancer cells, including "undruggable" cancers

**原文标题**: CRISPR tech selectively shreds cancer cells, including "undruggable" cancers

**原文链接**: [https://innovativegenomics.org/news/crispr-technique-selectively-shreds-cancer-cells/](https://innovativegenomics.org/news/crispr-technique-selectively-shreds-cancer-cells/)

生成摘要时出错

---

## 36. Pirates, a naval warfare game inspired by Sid Meier's Pirates

**原文标题**: Pirates, a naval warfare game inspired by Sid Meier's Pirates

**原文链接**: [https://piwodlaiwo.github.io/pirates/](https://piwodlaiwo.github.io/pirates/)

生成摘要时出错

---

## 37. Launch HN: BitBoard (YC P25) – Analytics Workspace for Agents

**原文标题**: Launch HN: BitBoard (YC P25) – Analytics Workspace for Agents

**原文链接**: [https://bitboard.work/](https://bitboard.work/)

生成摘要时出错

---

## 38. Sam Bankman-Fried loses bid to appeal against fraud conviction in FTX case

**原文标题**: Sam Bankman-Fried loses bid to appeal against fraud conviction in FTX case

**原文链接**: [https://www.theguardian.com/business/2026/jun/12/sam-bankman-fried-loses-appeal](https://www.theguardian.com/business/2026/jun/12/sam-bankman-fried-loses-appeal)

生成摘要时出错

---

## 39. Solar Overtakes Coal in US Electricity for the First Month on Record`

**原文标题**: Solar Overtakes Coal in US Electricity for the First Month on Record`

**原文链接**: [https://ember-energy.org/latest-updates/solar-overtakes-coal-in-us-electricity-for-the-first-month-on-record/](https://ember-energy.org/latest-updates/solar-overtakes-coal-in-us-electricity-for-the-first-month-on-record/)

生成摘要时出错

---

## 40. Orthodox C++

**原文标题**: Orthodox C++

**原文链接**: [https://bkaradzic.github.io/posts/orthodoxc++/](https://bkaradzic.github.io/posts/orthodoxc++/)

生成摘要时出错

---

## 41. What about OpenCL and CUDA C++ alternatives?

**原文标题**: What about OpenCL and CUDA C++ alternatives?

**原文链接**: [https://www.modular.com/blog/democratizing-ai-compute-part-5-what-about-cuda-c-alternatives](https://www.modular.com/blog/democratizing-ai-compute-part-5-what-about-cuda-c-alternatives)

生成摘要时出错

---

## 42. Slightly reducing the sloppiness of AI generated front end

**原文标题**: Slightly reducing the sloppiness of AI generated front end

**原文链接**: [https://envs.net/~volpe/blog/posts/reduce-slop.html](https://envs.net/~volpe/blog/posts/reduce-slop.html)

生成摘要时出错

---

## 43. Show HN: Lightweight Task queue on Erlang/OTP, SQLite-backed, no overengineering

**原文标题**: Show HN: Lightweight Task queue on Erlang/OTP, SQLite-backed, no overengineering

**原文链接**: [https://github.com/entGriff/ezra](https://github.com/entGriff/ezra)

生成摘要时出错

---

## 44. Tectonic: A modernized, complete, self-contained TeX/LaTeX engine

**原文标题**: Tectonic: A modernized, complete, self-contained TeX/LaTeX engine

**原文链接**: [https://tectonic-typesetting.github.io/en-US/](https://tectonic-typesetting.github.io/en-US/)

生成摘要时出错

---

## 45. If you are asking for human attention, demonstrate human effort

**原文标题**: If you are asking for human attention, demonstrate human effort

**原文链接**: [https://tombedor.dev/human-attention-and-human-effort/](https://tombedor.dev/human-attention-and-human-effort/)

生成摘要时出错

---

## 46. Stanford Scientists Regrow Lost Cartilage and Reverse Arthritis

**原文标题**: Stanford Scientists Regrow Lost Cartilage and Reverse Arthritis

**原文链接**: [https://www.sciencedaily.com/releases/2026/06/260612021604.htm](https://www.sciencedaily.com/releases/2026/06/260612021604.htm)

生成摘要时出错

---

## 47. Show HN: Quant Picker – which GGUF file fits your model and machine

**原文标题**: Show HN: Quant Picker – which GGUF file fits your model and machine

**原文链接**: [https://vettedconsumer.com/quant-picker/](https://vettedconsumer.com/quant-picker/)

生成摘要时出错

---

## 48. US ban on Mythos is related to a jailbreak research by Amazon researchers

**原文标题**: US ban on Mythos is related to a jailbreak research by Amazon researchers

**原文链接**: [https://timesofindia.indiatimes.com/technology/tech-news/us-ban-on-anthropics-fable-5-and-mythos-5-has-amazon-link-researchers-from-amazon-used-a-series-of-prompts-to-/articleshow/131701361.cms](https://timesofindia.indiatimes.com/technology/tech-news/us-ban-on-anthropics-fable-5-and-mythos-5-has-amazon-link-researchers-from-amazon-used-a-series-of-prompts-to-/articleshow/131701361.cms)

生成摘要时出错

---

## 49. France's Own Hack Is the Best Argument Against Its War on Encryption

**原文标题**: France's Own Hack Is the Best Argument Against Its War on Encryption

**原文链接**: [https://reclaimthenet.org/france-tchap-breach-undermines-encryption-backdoor-push](https://reclaimthenet.org/france-tchap-breach-undermines-encryption-backdoor-push)

生成摘要时出错

---

## 50. A dumpster arrived behind my university's library

**原文标题**: A dumpster arrived behind my university's library

**原文链接**: [https://yalereview.org/article/sheila-liming-the-end-of-books](https://yalereview.org/article/sheila-liming-the-end-of-books)

生成摘要时出错

---

## 51. Google proposes Open Knowledge Format based on Markdown

**原文标题**: Google proposes Open Knowledge Format based on Markdown

**原文链接**: [https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing/](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing/)

生成摘要时出错

---

## 52. On CPU Physics and CPU Cycles

**原文标题**: On CPU Physics and CPU Cycles

**原文链接**: [https://6it.dev/blog/on-cpu-physics-and-cpu-cycles-80730](https://6it.dev/blog/on-cpu-physics-and-cpu-cycles-80730)

生成摘要时出错

---

## 53. Claude Fable 5 vs. GPT-5.5: Better Planning, Similar Execution

**原文标题**: Claude Fable 5 vs. GPT-5.5: Better Planning, Similar Execution

**原文链接**: [https://blog.kilo.ai/p/claude-fable-5-vs-gpt-5-5](https://blog.kilo.ai/p/claude-fable-5-vs-gpt-5-5)

生成摘要时出错

---

## 54. Hazel (YC W24) Is Hiring a Full Stack Engineer

**原文标题**: Hazel (YC W24) Is Hiring a Full Stack Engineer

**原文链接**: [https://www.ycombinator.com/companies/hazel-2/jobs/3epPWgu-full-stack-engineer-ts-sci](https://www.ycombinator.com/companies/hazel-2/jobs/3epPWgu-full-stack-engineer-ts-sci)

生成摘要时出错

---

## 55. Automating Myself Out of Development

**原文标题**: Automating Myself Out of Development

**原文链接**: [https://www.thoughtfultechnologist.com/p/automating-myself-out-of-development](https://www.thoughtfultechnologist.com/p/automating-myself-out-of-development)

生成摘要时出错

---

## 56. Palantir loses legal challenge against Swiss investigative magazine

**原文标题**: Palantir loses legal challenge against Swiss investigative magazine

**原文链接**: [https://www.ft.com/content/7ffcace7-9dc0-4e7e-9912-895ac073f979](https://www.ft.com/content/7ffcace7-9dc0-4e7e-9912-895ac073f979)

生成摘要时出错

---

## 57. The Future of wasi-gfx and wasi:webgpu

**原文标题**: The Future of wasi-gfx and wasi:webgpu

**原文链接**: [https://wasi-gfx.dev/blog/posts/future-of-wasi-gfx/](https://wasi-gfx.dev/blog/posts/future-of-wasi-gfx/)

生成摘要时出错

---

## 58. Nearly Everyone, Everywhere, Veers Left When Walking

**原文标题**: Nearly Everyone, Everywhere, Veers Left When Walking

**原文链接**: [https://www.nytimes.com/2026/06/10/science/humans-walking-veer-left-counterclockwise.html](https://www.nytimes.com/2026/06/10/science/humans-walking-veer-left-counterclockwise.html)

生成摘要时出错

---

## 59. Gas Prices Wipe Out More Than a Year of Wage Gains

**原文标题**: Gas Prices Wipe Out More Than a Year of Wage Gains

**原文链接**: [https://www.wsj.com/economy/inflation-wages-american-workers-cbe3f187](https://www.wsj.com/economy/inflation-wages-american-workers-cbe3f187)

生成摘要时出错

---

## 60. Fudgetown, USA (2024)

**原文标题**: Fudgetown, USA (2024)

**原文链接**: [https://tastecooking.com/fudgetown-usa/](https://tastecooking.com/fudgetown-usa/)

生成摘要时出错

---

## 61. GLM 5.2 Released

**原文标题**: GLM 5.2 Released

**原文链接**: [https://twitter.com/i/status/2065704919299235870](https://twitter.com/i/status/2065704919299235870)

生成摘要时出错

---

## 62. Apple didn't revolutionize power supplies; new transistors did (2012)

**原文标题**: Apple didn't revolutionize power supplies; new transistors did (2012)

**原文链接**: [https://www.righto.com/2012/02/apple-didnt-revolutionize-power.html](https://www.righto.com/2012/02/apple-didnt-revolutionize-power.html)

生成摘要时出错

---

## 63. Reuse Less Software

**原文标题**: Reuse Less Software

**原文链接**: [https://wiki.alopex.li/ReuseLessSoftware](https://wiki.alopex.li/ReuseLessSoftware)

生成摘要时出错

---

## 64. Rejected Emoji Proposals

**原文标题**: Rejected Emoji Proposals

**原文链接**: [https://charlottebuff.com/unicode/misc/rejected-emoji-proposals/](https://charlottebuff.com/unicode/misc/rejected-emoji-proposals/)

生成摘要时出错

---

## 65. WASI 0.3

**原文标题**: WASI 0.3

**原文链接**: [https://bytecodealliance.org/articles/WASI-0.3](https://bytecodealliance.org/articles/WASI-0.3)

生成摘要时出错

---

## 66. Claude Fable is relentlessly proactive

**原文标题**: Claude Fable is relentlessly proactive

**原文链接**: [https://simonwillison.net/2026/Jun/11/fable-is-relentlessly-proactive/](https://simonwillison.net/2026/Jun/11/fable-is-relentlessly-proactive/)

生成摘要时出错

---

## 67. A greyscale iPhone setup that works in everyday life

**原文标题**: A greyscale iPhone setup that works in everyday life

**原文链接**: [https://www.fabianhemmert.com/opinions/a-greyscale-iphone-setup-that-works-in-everyday-life](https://www.fabianhemmert.com/opinions/a-greyscale-iphone-setup-that-works-in-everyday-life)

生成摘要时出错

---

## 68. Show HN: Turn your name into a tree in an infinite procedural shanshui landscape

**原文标题**: Show HN: Turn your name into a tree in an infinite procedural shanshui landscape

**原文链接**: [https://landscape.bairui.dev/](https://landscape.bairui.dev/)

生成摘要时出错

---

## 69. Show HN: FablePool – pool money behind a prompt, and Fable builds it in public

**原文标题**: Show HN: FablePool – pool money behind a prompt, and Fable builds it in public

**原文链接**: [https://fablepool.com](https://fablepool.com)

生成摘要时出错

---

## 70. Anthropic apologizes for invisible Claude Fable guardrails

**原文标题**: Anthropic apologizes for invisible Claude Fable guardrails

**原文链接**: [https://www.theverge.com/ai-artificial-intelligence/948280/anthropic-claude-fable-invisible-distillation-guardrail](https://www.theverge.com/ai-artificial-intelligence/948280/anthropic-claude-fable-invisible-distillation-guardrail)

生成摘要时出错

---

## 71. Discovery of Cold War-era rare Eastern Bloc computers in a German hangar

**原文标题**: Discovery of Cold War-era rare Eastern Bloc computers in a German hangar

**原文链接**: [https://computerhistory.org/stories/explorers-of-the-lost-computers/](https://computerhistory.org/stories/explorers-of-the-lost-computers/)

生成摘要时出错

---

## 72. Claude Fable 5

**原文标题**: Claude Fable 5

**原文链接**: [https://www.anthropic.com/news/claude-fable-5-mythos-5](https://www.anthropic.com/news/claude-fable-5-mythos-5)

生成摘要时出错

---

## 73. CSS: Unavoidable Bad Parts

**原文标题**: CSS: Unavoidable Bad Parts

**原文链接**: [https://matklad.github.io/2026/06/04/css-unavoidable-bad-parts.html](https://matklad.github.io/2026/06/04/css-unavoidable-bad-parts.html)

生成摘要时出错

---

## 74. MiMo Code is now released and open-source

**原文标题**: MiMo Code is now released and open-source

**原文链接**: [https://mimo.xiaomi.com/mimocode](https://mimo.xiaomi.com/mimocode)

生成摘要时出错

---

## 75. Pokémon Go Scans Trained the Navigation Tech for Military Drones

**原文标题**: Pokémon Go Scans Trained the Navigation Tech for Military Drones

**原文链接**: [https://dronexl.co/2026/06/09/pokemon-go-scans-niantic-vantor-military-drone-navigation/](https://dronexl.co/2026/06/09/pokemon-go-scans-niantic-vantor-military-drone-navigation/)

生成摘要时出错

---

## 76. OpenCV 5 Is Here: The Biggest Leap in Years for Computer Vision

**原文标题**: OpenCV 5 Is Here: The Biggest Leap in Years for Computer Vision

**原文链接**: [https://opencv.org/opencv-5/](https://opencv.org/opencv-5/)

生成摘要时出错

---

## 77. How we made hit video game Prince of Persia

**原文标题**: How we made hit video game Prince of Persia

**原文链接**: [https://www.theguardian.com/culture/2026/jan/05/raiders-of-the-lost-ark-hit-video-game-prince-of-persia](https://www.theguardian.com/culture/2026/jan/05/raiders-of-the-lost-ark-hit-video-game-prince-of-persia)

生成摘要时出错

---

## 78. /architect: Reduce Fable tokens by 80%, Fable orchestrates/reviews, Codex builds

**原文标题**: /architect: Reduce Fable tokens by 80%, Fable orchestrates/reviews, Codex builds

**原文链接**: [https://github.com/DanMcInerney/architect-loop](https://github.com/DanMcInerney/architect-loop)

生成摘要时出错

---

## 79. Flew: Emulated WiFi on Bluetooth Hardware

**原文标题**: Flew: Emulated WiFi on Bluetooth Hardware

**原文链接**: [https://dl.acm.org/doi/10.1145/3495243.3517030](https://dl.acm.org/doi/10.1145/3495243.3517030)

生成摘要时出错

---

## 80. A new era for software testing

**原文标题**: A new era for software testing

**原文链接**: [https://antirez.com/news/168](https://antirez.com/news/168)

生成摘要时出错

---

## 81. A jacket that harvests drinking water from the air

**原文标题**: A jacket that harvests drinking water from the air

**原文链接**: [https://news.utexas.edu/2026/06/11/this-jacket-pulls-drinking-water-from-thin-air/](https://news.utexas.edu/2026/06/11/this-jacket-pulls-drinking-water-from-thin-air/)

生成摘要时出错

---

## 82. What Would It Look Like If the AI Bubble Popped?

**原文标题**: What Would It Look Like If the AI Bubble Popped?

**原文链接**: [https://www.thebignewsletter.com/p/what-would-it-look-like-if-the-ai](https://www.thebignewsletter.com/p/what-would-it-look-like-if-the-ai)

生成摘要时出错

---

## 83. AUR packages compromised with Infostealer and Rootkit

**原文标题**: AUR packages compromised with Infostealer and Rootkit

**原文链接**: [https://discourse.ifin.network/t/400-aur-packages-compromised-with-infostealer-and-rootkit/577](https://discourse.ifin.network/t/400-aur-packages-compromised-with-infostealer-and-rootkit/577)

生成摘要时出错

---

## 84. Petition to Withdraw Canada's Bill C-22

**原文标题**: Petition to Withdraw Canada's Bill C-22

**原文链接**: [https://www.ourcommons.ca/petitions/en/Petition/Sign/e-7416](https://www.ourcommons.ca/petitions/en/Petition/Sign/e-7416)

生成摘要时出错

---

## 85. macOS 27 Beta breaks the ability to boot Asahi Linux

**原文标题**: macOS 27 Beta breaks the ability to boot Asahi Linux

**原文链接**: [https://www.phoronix.com/news/macOS-27-Beta-Breaks-Asahi](https://www.phoronix.com/news/macOS-27-Beta-Breaks-Asahi)

生成摘要时出错

---

## 86. OpenAI mulls slashing prices as it competes with Anthropic for users

**原文标题**: OpenAI mulls slashing prices as it competes with Anthropic for users

**原文链接**: [https://www.cnbc.com/2026/06/11/openai-mulls-slashing-prices-ahead-of-competition-from-anthropic-wsj.html](https://www.cnbc.com/2026/06/11/openai-mulls-slashing-prices-ahead-of-competition-from-anthropic-wsj.html)

生成摘要时出错

---

## 87. Claude Fable 5: mid-tier results on coding tasks

**原文标题**: Claude Fable 5: mid-tier results on coding tasks

**原文链接**: [https://www.endorlabs.com/learn/claude-fable-5-mythos-grade-hype](https://www.endorlabs.com/learn/claude-fable-5-mythos-grade-hype)

生成摘要时出错

---

## 88. Using the Epson Perfection V39 II Scanner on Ubuntu

**原文标题**: Using the Epson Perfection V39 II Scanner on Ubuntu

**原文链接**: [https://patches.joao.town/using-epson-perfection-v39ii-scanner-ubuntu/](https://patches.joao.town/using-epson-perfection-v39ii-scanner-ubuntu/)

生成摘要时出错

---

## 89. Web Browsers on Video Game Consoles

**原文标题**: Web Browsers on Video Game Consoles

**原文链接**: [https://vale.rocks/posts/game-console-browsers](https://vale.rocks/posts/game-console-browsers)

生成摘要时出错

---

## 90. Lines of code got a better publicist

**原文标题**: Lines of code got a better publicist

**原文链接**: [https://curlewis.co.nz/posts/lines-of-code-got-a-better-publicist/](https://curlewis.co.nz/posts/lines-of-code-got-a-better-publicist/)

生成摘要时出错

---

