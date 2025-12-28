# Hacker News 热门文章摘要 (2025-12-28)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 成长于“404 Not Found”：戈壁沙漠中的中国核城

**原文标题**: Growing up in “404 Not Found”: China's nuclear city in the Gobi Desert

**原文链接**: [https://substack.com/inbox/post/182743659](https://substack.com/inbox/post/182743659)

《在“404”长大》探讨了位于甘肃戈壁滩上的秘密核基地——404城的历史与传承。该城市始建于1958年，在地图上消失了数十年，是中国核武器计划的隐秘中心，也是中国第一颗原子弹的诞生地。

在鼎盛时期，404城是一个自给自足的微型社会，容纳了包括科学家、工程师及其家属在内的近10万人口。尽管地处偏远且沙漠气候恶劣，国家仍为居民提供了高质量的生活设施，包括学校、医院、剧院，甚至还有一座带动物园的公园。文章重点讲述了在那里长大的孩子独特的童年经历：这种生活既受限于极度的保密和地理隔绝，又充满深厚的社区归属感和安全感。

随着冷战结束和核计划重心的转移，这座城市开始衰落。2000年代中期，大部分居民搬迁到了附近的嘉峪关市。如今，404城在很大程度上已成为一座“鬼城”，随处可见破败的社会主义风格建筑和荒废的游乐场。

最终，这个故事捕捉到了对中国历史上一个“迷失”时代的怀旧情怀。它向“三线”一代致敬——成千上万的建设者隐姓埋名，为提升中国的军事和科研地位做出了巨大的个人牺牲。这座城市依然是国家机密的特殊象征，也见证了国家雄心背后所付出的个人代价。

---

## 2. 用质数构成的 Hacker News

**原文标题**: Hacker News made out of prime numbers

**原文链接**: [https://dosaygo-studio.github.io/prime-news/index.html](https://dosaygo-studio.github.io/prime-news/index.html)

**Hacker News Prime** 是一个概念性恶搞项目，它从数论和数学的角度重新构思了知名科技新闻聚合网站 Hacker News 的界面。

其内容模仿了该网站熟悉的页眉和页脚布局，但将标准分类替换为与素数相关的术语。关键导航链接包括**梅森素数**、**索菲·热尔曼素数**、**费马素数**和**回文素数**等分类。典型的新闻列表被数字序列和数学符号（如 $e \leq k^2$）所取代。

页脚延续了这一主题，将标准的创业相关链接替换为数学替代方案。例如，“申请 YC”（Y Combinator）链接被替换为“申请 $\zeta$”（引用黎曼 ζ 函数），而其他链接则改为“纯数学”、“确定性”和“安全”。

总的来说，本文呈现了一个风格独特的“数学主题”版 Hacker News 平台，迎合了纯数学和素数理论爱好者的兴趣。

---

## 3. 日历

**原文标题**: Calendar

**原文链接**: [https://neatnik.net/calendar/?year=2026](https://neatnik.net/calendar/?year=2026)

本文介绍了一款由 Neatnik 设计的 2026 年极简可打印日历。该工具的核心特点是无论纸张尺寸如何，都能将全年的日期展示在单张纸上。

**关键信息与使用提示：**
*   **最佳打印效果：** 为了获得最佳视觉效果，建议用户将打印方向设置为**横向**，并禁用页眉和页脚。
*   **设计理念：** 该版式旨在提供全年的整体视图，方便用户追踪时间流逝、记录笔记并提前规划。其紧凑的设计使其易于折叠和携带。
*   **补充内容：** 页面包含了 2026 年全部 12 个月的完整日期和星期网格，并以一句简短的寄语“善待他人”作为结尾。

本质上，该页面为那些寻求实体的、单页式全年概览的用户提供了一个功能性强且简洁实用的工具。

---

## 4. tc-ematch(8) 用于 "basic"、"cgroup" 或 "flow" 过滤器的扩展匹配

**原文标题**: tc-ematch(8) extended matches for use with "basic", "cgroup" or "flow" filters

**原文链接**: [https://man7.org/linux/man-pages/man8/tc-ematch.8.html](https://man7.org/linux/man-pages/man8/tc-ematch.8.html)

**tc-ematch(8)** 手册页描述了“扩展匹配”（extended matches），这是一种用于 Linux 流量控制（`tc`）的灵活架构，旨在增强 **basic**、**cgroup** 和 **flow** 过滤器的过滤能力。这些匹配允许通过逻辑运算符（**and**、**or**、**not**）和括号组合多个条件，从而实现复杂的报文分类。

主要匹配模块包括：

*   **cmp**：在特定偏移量和层（链路层、网络层或传输层）上对报文数据进行算术比较（eq、lt、gt）。
*   **meta**：匹配报文元数据，例如 Netfilter 标记（`nf_mark`）、VLAN 标签、接口索引、系统平均负载或内核套接字缓冲区属性。
*   **nbyte**：在报文内指定的偏移量处搜索特定的字节序列或字符串。
*   **u32**：对报文数据提供基于位掩码的匹配，类似于独立的 u32 过滤器。
*   **ipset**：检查报文头（如源或目的 IP）是否属于定义的 `ipset`。
*   **ipt**：允许在 `tc` 框架内使用标准的 `xtables` (iptables) 匹配扩展。
*   **canid**：专门用于匹配控制器局域网 (CAN) 帧标识符。

**使用注意事项：**
由于 ematch 语法使用括号对表达式进行分组，用户必须在 shell 中对其进行转义，以避免命令行解析错误。该实用程序是 **iproute2** 套件的一部分，对于高级网络流量整形至关重要，它允许管理员根据报文内容和系统元数据制定极具针对性的报文处理规则。

---

## 5. Hungry Fat Cells Could Someday Starve Cancer to Death

**原文标题**: Hungry Fat Cells Could Someday Starve Cancer to Death

**原文链接**: [https://www.ucsf.edu/news/2025/01/429411/how-hungry-fat-cells-could-someday-starve-cancer-death](https://www.ucsf.edu/news/2025/01/429411/how-hungry-fat-cells-could-someday-starve-cancer-death)

生成摘要时出错

---

## 6. 用纯 HTML 替换 JavaScript

**原文标题**: Replacing JavaScript with Just HTML

**原文链接**: [https://www.htmhell.dev/adventcalendar/2025/27/](https://www.htmhell.dev/adventcalendar/2025/27/)

在《仅用 HTML 替代 JavaScript》一文中，Aaron T. Grogg 指出，虽然 JavaScript (JS) 传统上一直是实现网页交互的核心工具，但开发者现在应优先为常见 UI 组件采用原生的 HTML 和 CSS 特性。减少对 JS 的依赖可以通过降低浏览器的下载、解压和内存处理负担来提升性能。

Grogg 重点介绍了原生 HTML 可以替代 JS 的四个具体领域：

*   **手风琴/可展开内容：** `<details>` 和 `<summary>` 元素提供了内置的显示/隐藏功能。通过使用 `name` 属性，开发者可以创建“排他性手风琴”（即一次只能打开一个面板），从而模拟单选按钮的行为。
*   **自动筛选建议：** 将 `<input>` 与 `<datalist>` 结合使用，可以创建一个在用户输入时自动过滤选项的功能性下拉框。这适用于文本、数字和时间输入，无需编写自定义筛选脚本。
*   **模态框与弹出框：** 新的 `popover` 和 `popovertarget` 属性支持轻松切换元素状态。它们支持“轻量化关闭”（通过 Esc 键或点击外部关闭），并提供 `auto`、`hint` 和 `manual` 等模式来控制覆盖层之间的交互。
*   **离屏导航：** 通过结合使用 Popover API 和 CSS 变换（如 `translate`），开发者可以创建侧边菜单和抽屉组件。这种方法利用了浏览器的原生定位能力，并能方便地设置背景遮罩样式。

Grogg 总结道，虽然 JS 对于处理复杂任务仍然必不可少，但将 UI 管理交给原生 HTML 和 CSS 可以构建出更精简、更高效的网站。通过充分利用浏览器的原生能力，开发者可以用更少的代码提供更好的用户体验。

---

## 7. 开发一个 macOS 应用，用于监测 Mac 何时出现过热降频

**原文标题**: Building a macOS app to know when my Mac is thermal throttling

**原文链接**: [https://stanislas.blog/2025/12/macos-thermal-throttling-app/](https://stanislas.blog/2025/12/macos-thermal-throttling-app/)

无法访问文章链接。

---

## 8. 记录 tada 清单的一年

**原文标题**: One year of keeping a tada list

**原文链接**: [https://www.ducktyped.org/p/one-year-of-keeping-a-tada-list](https://www.ducktyped.org/p/one-year-of-keeping-a-tada-list)

In "One year of keeping a tada list," Aditya Bhargava reflects on his experience maintaining a "to-done" list—a daily log of accomplishments designed to shift focus from pending tasks to completed successes. Bhargava’s method involved daily entries on monthly pages, capped off with a summary drawing of his achievements.

**Key Benefits:**
The practice provided a psychological counterweight to the "what's next?" mentality, forcing the author to celebrate milestones he would otherwise overlook. Most importantly, the list helped him visualize the "why" behind his progress. For example, he realized that the successful creation of Minnesota landscape cards was only possible because of months spent on pigment mixing and value studies. Similarly, his software projects were built upon libraries he had developed earlier in the year. The list served as a reminder that learning new skills is a cumulative process.

**Drawbacks:**
The practice was not without stress. Bhargava noted that the list created a "pressure to perform" every day just to have something to record. Furthermore, maintaining the habit for a full year led to burnout; by the end of the year, his entries became less frequent, and he stopped creating the monthly summary drawings.

**Conclusion:**
While the tada list acts as a valuable archive of forgotten efforts and helps reinforce the value of the learning process, the author is undecided about continuing it. He concludes that the motivational benefits must be weighed against the effort required to maintain the habit.

---

## 9. Designing Predictable LLM-Verifier Systems for Formal Method Guarantee

**原文标题**: Designing Predictable LLM-Verifier Systems for Formal Method Guarantee

**原文链接**: [https://arxiv.org/abs/2512.02080](https://arxiv.org/abs/2512.02080)

生成摘要时出错

---

## 10. Floor796

**原文标题**: Floor796

**原文链接**: [https://floor796.com/](https://floor796.com/)

生成摘要时出错

---

## 11. Never Use Pixelation to Hide Sensitive Text (2014)

**原文标题**: Never Use Pixelation to Hide Sensitive Text (2014)

**原文链接**: [https://dheera.net/posts/20140725-why-you-should-never-use-pixelation/](https://dheera.net/posts/20140725-why-you-should-never-use-pixelation/)

生成摘要时出错

---

## 12. Rex is a safe kernel extension framework that allows Rust in the place of eBPF

**原文标题**: Rex is a safe kernel extension framework that allows Rust in the place of eBPF

**原文链接**: [https://github.com/rex-rs/rex](https://github.com/rex-rs/rex)

生成摘要时出错

---

## 13. How we lost communication to entertainment

**原文标题**: How we lost communication to entertainment

**原文链接**: [https://ploum.net/2025-12-15-communication-entertainment.html](https://ploum.net/2025-12-15-communication-entertainment.html)

生成摘要时出错

---

## 14. Langfuse (YC W23) Is Hiring in Berlin, Germany

**原文标题**: Langfuse (YC W23) Is Hiring in Berlin, Germany

**原文链接**: [https://langfuse.com/careers](https://langfuse.com/careers)

生成摘要时出错

---

## 15. Scientists discover beer bottle in the Mariana Trench (2024)

**原文标题**: Scientists discover beer bottle in the Mariana Trench (2024)

**原文链接**: [https://www.unilad.com/news/scientist-beer-bottle-deepest-point-ocean-mariana-trench-667878-20240213](https://www.unilad.com/news/scientist-beer-bottle-deepest-point-ocean-mariana-trench-667878-20240213)

生成摘要时出错

---

## 16. Fathers’ choices may be packaged and passed down in sperm RNA

**原文标题**: Fathers’ choices may be packaged and passed down in sperm RNA

**原文链接**: [https://www.quantamagazine.org/how-dads-fitness-may-be-packaged-and-passed-down-in-sperm-rna-20251222/](https://www.quantamagazine.org/how-dads-fitness-may-be-packaged-and-passed-down-in-sperm-rna-20251222/)

生成摘要时出错

---

## 17. Dialtone – AOL 3.0 Server

**原文标题**: Dialtone – AOL 3.0 Server

**原文链接**: [https://dialtone.live/](https://dialtone.live/)

生成摘要时出错

---

## 18. Gpg.fail

**原文标题**: Gpg.fail

**原文链接**: [https://gpg.fail](https://gpg.fail)

生成摘要时出错

---

## 19. Functional programming and reliability: ADTs, safety, critical infrastructure

**原文标题**: Functional programming and reliability: ADTs, safety, critical infrastructure

**原文链接**: [https://blog.rastrian.dev/post/why-reliability-demands-functional-programming-adts-safety-and-critical-infrastructure](https://blog.rastrian.dev/post/why-reliability-demands-functional-programming-adts-safety-and-critical-infrastructure)

生成摘要时出错

---

## 20. Rainbow Six Siege hacked as players get billions of credits and random bans

**原文标题**: Rainbow Six Siege hacked as players get billions of credits and random bans

**原文链接**: [https://www.shanethegamer.com/esports-news/rainbow-six-siege-hacked-global-server-outage/](https://www.shanethegamer.com/esports-news/rainbow-six-siege-hacked-global-server-outage/)

生成摘要时出错

---

## 21. Streaming Uploads with LiveView

**原文标题**: Streaming Uploads with LiveView

**原文链接**: [https://fly.io/phoenix-files/streaming-uploads-with-liveview/](https://fly.io/phoenix-files/streaming-uploads-with-liveview/)

生成摘要时出错

---

## 22. The Origins of APL (1974) [video]

**原文标题**: The Origins of APL (1974) [video]

**原文链接**: [https://www.youtube.com/watch?v=8kUQWuK1L4w](https://www.youtube.com/watch?v=8kUQWuK1L4w)

生成摘要时出错

---

## 23. Project Vend: Phase Two

**原文标题**: Project Vend: Phase Two

**原文链接**: [https://www.anthropic.com/research/project-vend-2](https://www.anthropic.com/research/project-vend-2)

生成摘要时出错

---

## 24. Last Year on My Mac: Look Back in Disbelief

**原文标题**: Last Year on My Mac: Look Back in Disbelief

**原文链接**: [https://eclecticlight.co/2025/12/28/last-year-on-my-mac-look-back-in-disbelief/](https://eclecticlight.co/2025/12/28/last-year-on-my-mac-look-back-in-disbelief/)

生成摘要时出错

---

## 25. 2 in 3 Americans think AI will cause major harm to humans in the next 20 years [pdf]

**原文标题**: 2 in 3 Americans think AI will cause major harm to humans in the next 20 years [pdf]

**原文链接**: [https://www.pewresearch.org/wp-content/uploads/sites/20/2025/03/pi_2025.04.03_us-public-and-ai-experts_topline.pdf](https://www.pewresearch.org/wp-content/uploads/sites/20/2025/03/pi_2025.04.03_us-public-and-ai-experts_topline.pdf)

生成摘要时出错

---

## 26. Text rendering hates you (2019)

**原文标题**: Text rendering hates you (2019)

**原文链接**: [https://faultlore.com/blah/text-hates-you/](https://faultlore.com/blah/text-hates-you/)

生成摘要时出错

---

## 27. Windows 2 for the Apricot PC/Xi

**原文标题**: Windows 2 for the Apricot PC/Xi

**原文链接**: [https://www.ninakalinina.com/notes/win2apri/](https://www.ninakalinina.com/notes/win2apri/)

生成摘要时出错

---

## 28. Immer – A library of persistent and immutable data structures written in C++

**原文标题**: Immer – A library of persistent and immutable data structures written in C++

**原文链接**: [https://github.com/arximboldi/immer](https://github.com/arximboldi/immer)

生成摘要时出错

---

## 29. Liberating Bluetooth on the ESP32

**原文标题**: Liberating Bluetooth on the ESP32

**原文链接**: [https://exquisite.tube/w/mEzF442Q4hUXnhQ8HmfZuq](https://exquisite.tube/w/mEzF442Q4hUXnhQ8HmfZuq)

生成摘要时出错

---

## 30. Show HN: Ez FFmpeg – Video editing in plain English

**原文标题**: Show HN: Ez FFmpeg – Video editing in plain English

**原文链接**: [http://npmjs.com/package/ezff](http://npmjs.com/package/ezff)

生成摘要时出错

---

## 31. 'PromptQuest' is the worst game of 2025 (trying to make chatbots work)

**原文标题**: 'PromptQuest' is the worst game of 2025 (trying to make chatbots work)

**原文链接**: [https://www.theregister.com/2025/12/26/ai_is_like_adventure_games/](https://www.theregister.com/2025/12/26/ai_is_like_adventure_games/)

生成摘要时出错

---

## 32. Say No to Palantir in the NHS

**原文标题**: Say No to Palantir in the NHS

**原文链接**: [https://notopalantir.goodlawproject.org/email-to-target/stop-palantir-in-the-nhs/](https://notopalantir.goodlawproject.org/email-to-target/stop-palantir-in-the-nhs/)

生成摘要时出错

---

## 33. An experiment in separating identity, memory, and tools

**原文标题**: An experiment in separating identity, memory, and tools

**原文链接**: [https://RCRDBL.com](https://RCRDBL.com)

生成摘要时出错

---

## 34. C++ says “We have try. . . finally at home”

**原文标题**: C++ says “We have try. . . finally at home”

**原文链接**: [https://devblogs.microsoft.com/oldnewthing/20251222-00/?p=111890](https://devblogs.microsoft.com/oldnewthing/20251222-00/?p=111890)

生成摘要时出错

---

## 35. Nvidia's $20B antitrust loophole

**原文标题**: Nvidia's $20B antitrust loophole

**原文链接**: [https://ossa-ma.github.io/blog/groq](https://ossa-ma.github.io/blog/groq)

生成摘要时出错

---

## 36. Public Domain Day 2026

**原文标题**: Public Domain Day 2026

**原文链接**: [https://web.law.duke.edu/cspd/publicdomainday/2026/](https://web.law.duke.edu/cspd/publicdomainday/2026/)

生成摘要时出错

---

## 37. OrangePi 6 Plus Review

**原文标题**: OrangePi 6 Plus Review

**原文链接**: [https://boilingsteam.com/orange-pi-6-plus-review/](https://boilingsteam.com/orange-pi-6-plus-review/)

生成摘要时出错

---

## 38. Clock synchronization is a nightmare

**原文标题**: Clock synchronization is a nightmare

**原文链接**: [https://arpitbhayani.me/blogs/clock-sync-nightmare/](https://arpitbhayani.me/blogs/clock-sync-nightmare/)

生成摘要时出错

---

## 39. The Dangers of SSL Certificates

**原文标题**: The Dangers of SSL Certificates

**原文链接**: [https://surfingcomplexity.blog/2025/12/27/the-dangers-of-ssl-certificates/](https://surfingcomplexity.blog/2025/12/27/the-dangers-of-ssl-certificates/)

生成摘要时出错

---

## 40. Show HN: Mysti – Claude, Codex, and Gemini debate your code, then synthesize

**原文标题**: Show HN: Mysti – Claude, Codex, and Gemini debate your code, then synthesize

**原文链接**: [https://github.com/DeepMyst/Mysti](https://github.com/DeepMyst/Mysti)

生成摘要时出错

---

## 41. Janet Jackson had the power to crash laptop computers (2022)

**原文标题**: Janet Jackson had the power to crash laptop computers (2022)

**原文链接**: [https://devblogs.microsoft.com/oldnewthing/20220816-00/?p=106994](https://devblogs.microsoft.com/oldnewthing/20220816-00/?p=106994)

生成摘要时出错

---

## 42. Pre-commit hooks are broken

**原文标题**: Pre-commit hooks are broken

**原文链接**: [https://jyn.dev/pre-commit-hooks-are-fundamentally-broken/](https://jyn.dev/pre-commit-hooks-are-fundamentally-broken/)

生成摘要时出错

---

## 43. Multiscale Aperture Synthesis Imager

**原文标题**: Multiscale Aperture Synthesis Imager

**原文链接**: [https://www.nature.com/articles/s41467-025-65661-8](https://www.nature.com/articles/s41467-025-65661-8)

生成摘要时出错

---

## 44. Ubuntu 26.04 LTS – The Roadmap

**原文标题**: Ubuntu 26.04 LTS – The Roadmap

**原文链接**: [https://discourse.ubuntu.com/t/ubuntu-26-04-lts-the-roadmap/72740](https://discourse.ubuntu.com/t/ubuntu-26-04-lts-the-roadmap/72740)

生成摘要时出错

---

## 45. Plugins case study: mdBook preprocessors

**原文标题**: Plugins case study: mdBook preprocessors

**原文链接**: [https://eli.thegreenplace.net/2025/plugins-case-study-mdbook-preprocessors/](https://eli.thegreenplace.net/2025/plugins-case-study-mdbook-preprocessors/)

生成摘要时出错

---

## 46. Mruby: Ruby for Embedded Systems

**原文标题**: Mruby: Ruby for Embedded Systems

**原文链接**: [https://github.com/mruby/mruby](https://github.com/mruby/mruby)

生成摘要时出错

---

## 47. How uv got so fast

**原文标题**: How uv got so fast

**原文链接**: [https://nesbitt.io/2025/12/26/how-uv-got-so-fast.html](https://nesbitt.io/2025/12/26/how-uv-got-so-fast.html)

生成摘要时出错

---

## 48. Toll roads are spreading in America

**原文标题**: Toll roads are spreading in America

**原文链接**: [https://www.economist.com/united-states/2025/12/18/toll-roads-are-spreading-in-america](https://www.economist.com/united-states/2025/12/18/toll-roads-are-spreading-in-america)

生成摘要时出错

---

## 49. Wooden compass with single red arrow leads people with dementia to their homes

**原文标题**: Wooden compass with single red arrow leads people with dementia to their homes

**原文链接**: [https://www.designboom.com/technology/wooden-compass-single-red-arrow-leads-people-with-dementia-homes-aumens-12-28-2025/](https://www.designboom.com/technology/wooden-compass-single-red-arrow-leads-people-with-dementia-homes-aumens-12-28-2025/)

生成摘要时出错

---

## 50. Learn computer graphics from scratch and for free

**原文标题**: Learn computer graphics from scratch and for free

**原文链接**: [https://www.scratchapixel.com](https://www.scratchapixel.com)

生成摘要时出错

---

## 51. Splice a Fibre

**原文标题**: Splice a Fibre

**原文链接**: [https://react-networks-lib.rackout.net/fibre](https://react-networks-lib.rackout.net/fibre)

生成摘要时出错

---

## 52. Langjam-Gamejam Devlog: Making a language, compiler, VM and 5 games in 52 hours

**原文标题**: Langjam-Gamejam Devlog: Making a language, compiler, VM and 5 games in 52 hours

**原文链接**: [https://github.com/Syn-Nine/gar-lang/blob/main/DEVLOG.md](https://github.com/Syn-Nine/gar-lang/blob/main/DEVLOG.md)

生成摘要时出错

---

## 53. Intertapes – collection of found cassette tapes from different locations

**原文标题**: Intertapes – collection of found cassette tapes from different locations

**原文链接**: [https://intertapes.net/](https://intertapes.net/)

生成摘要时出错

---

## 54. T-Ruby is Ruby with syntax for types

**原文标题**: T-Ruby is Ruby with syntax for types

**原文链接**: [https://type-ruby.github.io/](https://type-ruby.github.io/)

生成摘要时出错

---

## 55. Interton Video Computer 4000

**原文标题**: Interton Video Computer 4000

**原文链接**: [https://en.wikipedia.org/wiki/Interton_Video_Computer_4000](https://en.wikipedia.org/wiki/Interton_Video_Computer_4000)

生成摘要时出错

---

## 56. Nvidia deal a big win for Groq employees

**原文标题**: Nvidia deal a big win for Groq employees

**原文链接**: [https://www.axios.com/2025/12/28/nvidia-groq-shareholders](https://www.axios.com/2025/12/28/nvidia-groq-shareholders)

生成摘要时出错

---

## 57. Pfizer ended up passing on my GLP-1 work back in the early '90s (2024)

**原文标题**: Pfizer ended up passing on my GLP-1 work back in the early '90s (2024)

**原文链接**: [https://www.statnews.com/2024/09/09/glp-1-history-pfizer-john-baxter-jeffrey-flier-calbio-metabio/](https://www.statnews.com/2024/09/09/glp-1-history-pfizer-john-baxter-jeffrey-flier-calbio-metabio/)

生成摘要时出错

---

## 58. People Who Drink Bottled Water Daily Get 90k More Microplastic Particles a Year

**原文标题**: People Who Drink Bottled Water Daily Get 90k More Microplastic Particles a Year

**原文链接**: [https://www.wired.com/story/people-who-drink-bottled-water-on-a-daily-basis-ingest-90000-more-microplastics-per-year/](https://www.wired.com/story/people-who-drink-bottled-water-on-a-daily-basis-ingest-90000-more-microplastics-per-year/)

生成摘要时出错

---

## 59. Why is calling my asm function from Rust slower than calling it from C?

**原文标题**: Why is calling my asm function from Rust slower than calling it from C?

**原文链接**: [https://ohadravid.github.io/posts/2025-12-rav1d-faster-asm/](https://ohadravid.github.io/posts/2025-12-rav1d-faster-asm/)

生成摘要时出错

---

## 60. USD share as global reserve currency drops to lowest since 1994

**原文标题**: USD share as global reserve currency drops to lowest since 1994

**原文链接**: [https://wolfstreet.com/2025/12/26/status-of-the-us-dollar-as-global-reserve-currency-usd-share-drops-to-lowest-since-1994/](https://wolfstreet.com/2025/12/26/status-of-the-us-dollar-as-global-reserve-currency-usd-share-drops-to-lowest-since-1994/)

生成摘要时出错

---

## 61. Inside the proton, the ‘most complicated thing you could possibly imagine’ (2022)

**原文标题**: Inside the proton, the ‘most complicated thing you could possibly imagine’ (2022)

**原文链接**: [https://www.quantamagazine.org/inside-the-proton-the-most-complicated-thing-imaginable-20221019/](https://www.quantamagazine.org/inside-the-proton-the-most-complicated-thing-imaginable-20221019/)

生成摘要时出错

---

## 62. Fabrice Bellard Releases MicroQuickJS

**原文标题**: Fabrice Bellard Releases MicroQuickJS

**原文链接**: [https://github.com/bellard/mquickjs/blob/main/README.md](https://github.com/bellard/mquickjs/blob/main/README.md)

生成摘要时出错

---

## 63. One million (small web) screenshots

**原文标题**: One million (small web) screenshots

**原文链接**: [https://nry.me/posts/2025-10-09/small-web-screenshots/](https://nry.me/posts/2025-10-09/small-web-screenshots/)

生成摘要时出错

---

## 64. Detect memory leaks of C extensions with psutil and psleak

**原文标题**: Detect memory leaks of C extensions with psutil and psleak

**原文链接**: [https://gmpy.dev/blog/2025/psutil-heap-introspection-apis](https://gmpy.dev/blog/2025/psutil-heap-introspection-apis)

生成摘要时出错

---

## 65. Some Junk Theorems in Lean

**原文标题**: Some Junk Theorems in Lean

**原文链接**: [https://github.com/James-Hanson/junk-theorems-in-lean](https://github.com/James-Hanson/junk-theorems-in-lean)

生成摘要时出错

---

## 66. They made me an offer I couldn't refuse (1997)

**原文标题**: They made me an offer I couldn't refuse (1997)

**原文链接**: [https://jens.mooseyard.com/1997/04/13/they-made-me-an-offer-i-couldnt-refuse/](https://jens.mooseyard.com/1997/04/13/they-made-me-an-offer-i-couldnt-refuse/)

生成摘要时出错

---

## 67. Experts explore new mushroom which causes fairytale-like hallucinations

**原文标题**: Experts explore new mushroom which causes fairytale-like hallucinations

**原文链接**: [https://nhmu.utah.edu/articles/experts-explore-new-mushroom-which-causes-fairytale-hallucinations](https://nhmu.utah.edu/articles/experts-explore-new-mushroom-which-causes-fairytale-hallucinations)

生成摘要时出错

---

## 68. NMH BASIC

**原文标题**: NMH BASIC

**原文链接**: [https://t3x.org/nmhbasic/index.html](https://t3x.org/nmhbasic/index.html)

生成摘要时出错

---

## 69. Rust the Process

**原文标题**: Rust the Process

**原文链接**: [https://www.amalbansode.com/writing/2025-12-24-rust-the-process/](https://www.amalbansode.com/writing/2025-12-24-rust-the-process/)

生成摘要时出错

---

## 70. Package managers keep using Git as a database, it never works out

**原文标题**: Package managers keep using Git as a database, it never works out

**原文链接**: [https://nesbitt.io/2025/12/24/package-managers-keep-using-git-as-a-database.html](https://nesbitt.io/2025/12/24/package-managers-keep-using-git-as-a-database.html)

生成摘要时出错

---

## 71. Faster practical modular inversion

**原文标题**: Faster practical modular inversion

**原文链接**: [https://purplesyringa.moe/blog/faster-practical-modular-inversion/](https://purplesyringa.moe/blog/faster-practical-modular-inversion/)

生成摘要时出错

---

## 72. Richard Stallman at the First Hackers Conference in 1984 [video]

**原文标题**: Richard Stallman at the First Hackers Conference in 1984 [video]

**原文链接**: [https://www.youtube.com/watch?v=Hf2pfzzWPYE](https://www.youtube.com/watch?v=Hf2pfzzWPYE)

生成摘要时出错

---

## 73. Who Cares about the Baltic Jammer? Terrestrial Navigation in Baltic Sea Region [video]

**原文标题**: Who Cares about the Baltic Jammer? Terrestrial Navigation in Baltic Sea Region [video]

**原文链接**: [https://media.ccc.de/v/39c3-who-cares-about-the-baltic-jammer-terrestrial-navigation-in-the-baltic-sea-region](https://media.ccc.de/v/39c3-who-cares-about-the-baltic-jammer-terrestrial-navigation-in-the-baltic-sea-region)

生成摘要时出错

---

## 74. Show HN: Xcc700: Self-hosting mini C compiler for ESP32 (Xtensa) in 700 lines

**原文标题**: Show HN: Xcc700: Self-hosting mini C compiler for ESP32 (Xtensa) in 700 lines

**原文链接**: [https://github.com/valdanylchuk/xcc700](https://github.com/valdanylchuk/xcc700)

生成摘要时出错

---

## 75. Italians celebrate village's first baby in 30 years

**原文标题**: Italians celebrate village's first baby in 30 years

**原文链接**: [https://www.theguardian.com/world/2025/dec/26/italian-village-first-baby-in-30-years](https://www.theguardian.com/world/2025/dec/26/italian-village-first-baby-in-30-years)

生成摘要时出错

---

## 76. Exe.dev

**原文标题**: Exe.dev

**原文链接**: [https://exe.dev/](https://exe.dev/)

生成摘要时出错

---

## 77. The Algebra of Loans in Rust

**原文标题**: The Algebra of Loans in Rust

**原文链接**: [https://nadrieril.github.io/blog/2025/12/21/the-algebra-of-loans-in-rust.html](https://nadrieril.github.io/blog/2025/12/21/the-algebra-of-loans-in-rust.html)

生成摘要时出错

---

## 78. What happened to all the gold Spain got from the New World? (1985)

**原文标题**: What happened to all the gold Spain got from the New World? (1985)

**原文链接**: [https://www.straightdope.com/21341789/what-happened-to-all-the-gold-spain-got-from-the-new-world](https://www.straightdope.com/21341789/what-happened-to-all-the-gold-spain-got-from-the-new-world)

生成摘要时出错

---

## 79. Always bet on text (2014)

**原文标题**: Always bet on text (2014)

**原文链接**: [https://graydon2.dreamwidth.org/193447.html](https://graydon2.dreamwidth.org/193447.html)

生成摘要时出错

---

## 80. More dynamic cronjobs

**原文标题**: More dynamic cronjobs

**原文链接**: [https://george.mand.is/2025/09/more-dynamic-cronjobs/](https://george.mand.is/2025/09/more-dynamic-cronjobs/)

生成摘要时出错

---

## 81. The best things and stuff of 2025

**原文标题**: The best things and stuff of 2025

**原文链接**: [https://blog.fogus.me/2025/12/23/the-best-things-and-stuff-of-2025.html](https://blog.fogus.me/2025/12/23/the-best-things-and-stuff-of-2025.html)

生成摘要时出错

---

## 82. Verdichtung

**原文标题**: Verdichtung

**原文链接**: [https://alexeygy.github.io/blog/verdichtung/](https://alexeygy.github.io/blog/verdichtung/)

生成摘要时出错

---

## 83. Unix "find" expressions compiled to bytecode

**原文标题**: Unix "find" expressions compiled to bytecode

**原文链接**: [https://nullprogram.com/blog/2025/12/23/](https://nullprogram.com/blog/2025/12/23/)

生成摘要时出错

---

## 84. RoboCop – Breaking the Law. H0ffman Cracks RoboCop Arcade from DataEast

**原文标题**: RoboCop – Breaking the Law. H0ffman Cracks RoboCop Arcade from DataEast

**原文链接**: [https://hoffman.home.blog/2025/12/26/robocop-breaking-the-law/](https://hoffman.home.blog/2025/12/26/robocop-breaking-the-law/)

生成摘要时出错

---

## 85. Scientists edited genes in a living person and saved his life

**原文标题**: Scientists edited genes in a living person and saved his life

**原文链接**: [https://www.popularmechanics.com/science/health/a64815804/crispr-therapy/](https://www.popularmechanics.com/science/health/a64815804/crispr-therapy/)

生成摘要时出错

---

## 86. Moravec's Paradox and the Robot Olympics

**原文标题**: Moravec's Paradox and the Robot Olympics

**原文链接**: [https://www.physicalintelligence.company/blog/olympics](https://www.physicalintelligence.company/blog/olympics)

生成摘要时出错

---

## 87. TIL: Restarting systemd services on sustained CPU abuse

**原文标题**: TIL: Restarting systemd services on sustained CPU abuse

**原文链接**: [https://taoofmac.com/space/til/2025/12/28/1400](https://taoofmac.com/space/til/2025/12/28/1400)

生成摘要时出错

---

## 88. QNX Self-Hosted Developer Desktop

**原文标题**: QNX Self-Hosted Developer Desktop

**原文链接**: [https://devblog.qnx.com/qnx-self-hosted-developer-desktop-initial-release/](https://devblog.qnx.com/qnx-self-hosted-developer-desktop-initial-release/)

生成摘要时出错

---

## 89. Publishing your work increases your luck

**原文标题**: Publishing your work increases your luck

**原文链接**: [https://github.com/readme/guides/publishing-your-work](https://github.com/readme/guides/publishing-your-work)

生成摘要时出错

---

## 90. Maybe the default settings are too high

**原文标题**: Maybe the default settings are too high

**原文链接**: [https://www.raptitude.com/2025/12/maybe-the-default-settings-are-too-high/](https://www.raptitude.com/2025/12/maybe-the-default-settings-are-too-high/)

生成摘要时出错

---

## 91. MiniMax M2.1: Built for Real-World Complex Tasks, Multi-Language Programming

**原文标题**: MiniMax M2.1: Built for Real-World Complex Tasks, Multi-Language Programming

**原文链接**: [https://www.minimaxi.com/news/minimax-m21](https://www.minimaxi.com/news/minimax-m21)

生成摘要时出错

---

## 92. How We Found Out About COINTELPRO (2014)

**原文标题**: How We Found Out About COINTELPRO (2014)

**原文链接**: [https://monthlyreview.org/articles/how-we-found-out-about-cointelpro/](https://monthlyreview.org/articles/how-we-found-out-about-cointelpro/)

生成摘要时出错

---

## 93. Researchers develop a camera that can focus on different distances at once

**原文标题**: Researchers develop a camera that can focus on different distances at once

**原文链接**: [https://engineering.cmu.edu/news-events/news/2025/12/19-perfect-shot.html](https://engineering.cmu.edu/news-events/news/2025/12/19-perfect-shot.html)

生成摘要时出错

---

## 94. My insulin pump controller uses the Linux kernel. It also violates the GPL

**原文标题**: My insulin pump controller uses the Linux kernel. It also violates the GPL

**原文链接**: [https://old.reddit.com/r/linux/comments/1puojsr/the_device_that_controls_my_insulin_pump_uses_the/](https://old.reddit.com/r/linux/comments/1puojsr/the_device_that_controls_my_insulin_pump_uses_the/)

生成摘要时出错

---

## 95. MongoBleed

**原文标题**: MongoBleed

**原文链接**: [https://github.com/joe-desimone/mongobleed/blob/main/mongobleed.py](https://github.com/joe-desimone/mongobleed/blob/main/mongobleed.py)

生成摘要时出错

---

## 96. Rob Pike goes nuclear over GenAI

**原文标题**: Rob Pike goes nuclear over GenAI

**原文链接**: [https://skyview.social/?url=https%3A%2F%2Fbsky.app%2Fprofile%2Frobpike.io%2Fpost%2F3matwg6w3ic2s&viewtype=tree](https://skyview.social/?url=https%3A%2F%2Fbsky.app%2Fprofile%2Frobpike.io%2Fpost%2F3matwg6w3ic2s&viewtype=tree)

生成摘要时出错

---

## 97. Show HN: Witr – Explain why a process is running on your Linux system

**原文标题**: Show HN: Witr – Explain why a process is running on your Linux system

**原文链接**: [https://github.com/pranshuparmar/witr](https://github.com/pranshuparmar/witr)

生成摘要时出错

---

## 98. FFmpeg has issued a DMCA takedown on GitHub

**原文标题**: FFmpeg has issued a DMCA takedown on GitHub

**原文链接**: [https://twitter.com/FFmpeg/status/2004599109559496984](https://twitter.com/FFmpeg/status/2004599109559496984)

生成摘要时出错

---

## 99. Overlooked No More: Inge Lehmann, Who Discovered the Earth's Inner Core

**原文标题**: Overlooked No More: Inge Lehmann, Who Discovered the Earth's Inner Core

**原文链接**: [https://www.nytimes.com/2025/12/20/obituaries/inge-lehmann-overlooked.html](https://www.nytimes.com/2025/12/20/obituaries/inge-lehmann-overlooked.html)

生成摘要时出错

---

## 100. Study: Everyday conversations can delay eye movement, essential for safe driving

**原文标题**: Study: Everyday conversations can delay eye movement, essential for safe driving

**原文链接**: [https://www.fujita-hu.ac.jp/news/vsfo8q20251226.html](https://www.fujita-hu.ac.jp/news/vsfo8q20251226.html)

生成摘要时出错

---

