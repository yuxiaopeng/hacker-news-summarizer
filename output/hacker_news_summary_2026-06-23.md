# Hacker News 热门文章摘要 (2026-06-23)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 杰瑞的地图

**原文标题**: Jerry's Map

**原文链接**: [http://www.jerrysmap.com/the-map](http://www.jerrysmap.com/the-map)

《杰里的地图》（Jerry’s Map）是由杰里·格雷辛格（Jerry Gretzinger）于1963年启动的一项宏大且不断演进的艺术项目。最初只是对一座虚构城市的涂鸦，如今已演变成一个庞大的“虚拟世界”，由4,000多块8×10英寸的独立画板组成。这些画板按坐标排列，组装后构成一个近似的圆。在1983年至2003年经历了20年的中断后，该项目得以重启，目前作为一个复杂的、基于规则的系统运行。

其创作过程由一套约100张定制的指令卡主导。这些卡片规定了地图演变的方方面面，包括工作量（以“工作单位”衡量）、进展方向（顺时针或逆时针），以及绘画、拼贴或生成新画板等具体任务。地图永远没有“终点”，而是以连续的图层形式存在。画板会经历不同的阶段，从基础的上色和城市密度演变为更抽象的维度，如“虚空”、“红色维度”和“洪水”。

该项目分为两个截然不同的阶段。第一阶段（1963–1983年）的特点是写实的手绘地形特征和手工记录。第二阶段（2003年至今）引入了数字工具、电子表格和更抽象的美学风格。在当前的阶段，格雷辛格往往将自己视为观察者而非主导者，遵循着卡组的“意志”。在负责扫描和存档的“助手”的协助下，该地图已从个人爱好转型为在博物馆展出的著名艺术装置，并得到了专门在线社区的支持。它始终是一个充满生命力的、自我延续的系统，在不断的修订中持续生长。

---

## 2. Swift Package Index 加入苹果

**原文标题**: Swift Package Index joins Apple

**原文链接**: [https://swiftpackageindex.com/blog/swift-package-index-joins-apple](https://swiftpackageindex.com/blog/swift-package-index-joins-apple)

Swift Package Index (SPI) 是一个用于发现和评估 Swift 软件包的关键社区驱动资源，现已正式加入 Apple。

该平台由 Dave Verwer 和 Sven A. Schmidt 创立，最初是一个旨在帮助开发者探索日益壮大的 Swift 库生态系统的业余项目。此次并入 Apple 旨在通过提供 Swift 语言背后公司的正式支持和资源，确保该服务的长期可持续性与发展。

公告的关键点包括：

*   **团队过渡：** 两位创始人 Verwer 和 Schmidt 都将作为全职员工加入 Apple，继续负责该索引的开发工作。
*   **使命延续：** 核心目标保持不变，即为 Swift 软件包提供全面、高质量的搜索和元数据引擎，帮助开发者做出明智的决策。
*   **开源承诺：** 该项目将保持开源，团队计划继续与开发者社区保持透明且协作的工作模式。
*   **稳定性：** 此举保障了这一许多开发者日常工作所依赖的工具的未来，使其从社区资助模式转变为 Apple 开发者工具基础设施的永久组成部分。

创始人表示，加入 Apple 是扩展该平台并随着 Swift 生态系统在不同平台持续扩张而更好地服务于该生态系统的最佳途径。

---

## 3. 三级方程式

**原文标题**: F3

**原文链接**: [https://github.com/future-file-format/f3](https://github.com/future-file-format/f3)

**F3 (面向未来的文件格式)** 是一种下一代开源列式存储格式，旨在通过解决 Parquet 和 ORC 等陈旧格式的局限性，推动数据分析的现代化。F3 由包括 Wes McKinney 和 Andrew Pavlo 在内的行业领袖所组成的科研团队创建，旨在为现代硬件和工作负载提供一个更高效、互操作性更强且更具扩展性的替代方案。

F3 的核心创新在于直接在数据文件中嵌入 **WebAssembly (Wasm) 解码器**。这种“用户定义编码”（UDE）方法允许开发人员轻松引入新的编码方案。由于解码数据的逻辑与数据本身封装在一起，F3 确保了通用的兼容性，并使其格式具有“面向未来”的特性；即使在没有原生解码器的情况下，任何系统都可以通过内置的 Wasm 二进制文件读取文件。

关键特性和细节包括：
*   **效率与布局：** 纠正了上一代格式的结构性缺陷，以优化在现代硬件上的性能。
*   **自描述特性：** 每个文件都包含数据、元数据以及解码所需的 Wasm 二进制文件，仅增加极小的存储开销（以 KB 计）。
*   **研究状态：** 目前仍处于研究原型阶段，尚未用于生产环境。该项目使用 Rust 语言实现，并采用 FlatBuffers 进行格式定义。
*   **学术验证：** 详见 2025 年发表在《ACM 数据管理学会会刊》（Proceedings of the ACM on Management of Data）上的一篇论文。研究表明，F3 在存储布局效率和解码灵活性方面均优于传统格式。

该项目采用 MIT 许可证，目前仍是数据互操作性未来发展的一个活跃研究领域。

---

## 4. Show HN: TikZ Editor – LaTeX 绘图所见即所得编辑器

**原文标题**: Show HN: TikZ Editor – WYSIWYG editor for figures in LaTeX

**原文链接**: [https://tikz.dev/editor/](https://tikz.dev/editor/)

生成摘要时出错

---

## 5. Unlimited OCR: One-shot long-horizon parsing

**原文标题**: Unlimited OCR: One-shot long-horizon parsing

**原文链接**: [https://github.com/baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR)

生成摘要时出错

---

## 6. San Diego photologs from the 1970s

**原文标题**: San Diego photologs from the 1970s

**原文链接**: [https://www.beautifulpublicdata.com/san-diego-photologs-from-the-1970s/](https://www.beautifulpublicdata.com/san-diego-photologs-from-the-1970s/)

生成摘要时出错

---

## 7. The truth about being a manager

**原文标题**: The truth about being a manager

**原文链接**: [https://sofiakodar.github.io/posts/becomingmanager/](https://sofiakodar.github.io/posts/becomingmanager/)

生成摘要时出错

---

## 8. Five monitors on a Commodore 128 [video]

**原文标题**: Five monitors on a Commodore 128 [video]

**原文链接**: [https://www.youtube.com/watch?v=ul5hC3PY1Yg](https://www.youtube.com/watch?v=ul5hC3PY1Yg)

生成摘要时出错

---

## 9. Lift4D: Harmonizing Single-View 3D Estimation for 4D Reconstruction In-the-Wild

**原文标题**: Lift4D: Harmonizing Single-View 3D Estimation for 4D Reconstruction In-the-Wild

**原文链接**: [https://lift4d.github.io/](https://lift4d.github.io/)

生成摘要时出错

---

## 10. The Coming Loop

**原文标题**: The Coming Loop

**原文链接**: [https://lucumr.pocoo.org/2026/6/23/the-coming-loop/](https://lucumr.pocoo.org/2026/6/23/the-coming-loop/)

生成摘要时出错

---

## 11. Samsung Demonstrates 3D Stacked FETs with Triple Nanosheet Channels at 42nm

**原文标题**: Samsung Demonstrates 3D Stacked FETs with Triple Nanosheet Channels at 42nm

**原文链接**: [https://semiconductor.samsung.com/news-events/tech-blog/from-gaa-to-3d-stacked-fet-expanding-the-transistor-into-the-third-dimension/](https://semiconductor.samsung.com/news-events/tech-blog/from-gaa-to-3d-stacked-fet-expanding-the-transistor-into-the-third-dimension/)

生成摘要时出错

---

## 12. Claude Tag

**原文标题**: Claude Tag

**原文链接**: [https://www.anthropic.com/news/introducing-claude-tag](https://www.anthropic.com/news/introducing-claude-tag)

生成摘要时出错

---

## 13. The deadly rise of giant trucks and SUVs

**原文标题**: The deadly rise of giant trucks and SUVs

**原文链接**: [https://www.nytimes.com/interactive/2026/06/21/us/trucks-suv-pedestrian-crashes.html](https://www.nytimes.com/interactive/2026/06/21/us/trucks-suv-pedestrian-crashes.html)

生成摘要时出错

---

## 14. Mistral OCR 4

**原文标题**: Mistral OCR 4

**原文链接**: [https://mistral.ai/news/ocr-4/](https://mistral.ai/news/ocr-4/)

生成摘要时出错

---

## 15. Modal Auto Endpoints: Optimized inference you own

**原文标题**: Modal Auto Endpoints: Optimized inference you own

**原文链接**: [https://modal.com/blog/introducing-auto-endpoints](https://modal.com/blog/introducing-auto-endpoints)

生成摘要时出错

---

## 16. Plotnine

**原文标题**: Plotnine

**原文链接**: [https://plotnine.org/](https://plotnine.org/)

生成摘要时出错

---

## 17. Solving Wordle using information theory

**原文标题**: Solving Wordle using information theory

**原文链接**: [https://www.binghamton.edu/news/story/6327/s-m-a-r-t-these-researchers-used-math-to-crack-wordle](https://www.binghamton.edu/news/story/6327/s-m-a-r-t-these-researchers-used-math-to-crack-wordle)

生成摘要时出错

---

## 18. The worthlessness of Vitamin D is mildly exaggerated

**原文标题**: The worthlessness of Vitamin D is mildly exaggerated

**原文链接**: [https://dynomight.net/vitamin-d/](https://dynomight.net/vitamin-d/)

生成摘要时出错

---

## 19. Fired by Google for Creating the Google Workspace CLI

**原文标题**: Fired by Google for Creating the Google Workspace CLI

**原文链接**: [https://twitter.com/JPoehnelt/status/2069482265953087602](https://twitter.com/JPoehnelt/status/2069482265953087602)

生成摘要时出错

---

## 20. Performance Improvements in Libffi

**原文标题**: Performance Improvements in Libffi

**原文链接**: [https://atgreen.github.io/repl-yell/posts/libffi-plan-cache/](https://atgreen.github.io/repl-yell/posts/libffi-plan-cache/)

生成摘要时出错

---

## 21. Elevated error rate across multiple models

**原文标题**: Elevated error rate across multiple models

**原文链接**: [https://status.claude.com/incidents/jbhf20wjmzrf](https://status.claude.com/incidents/jbhf20wjmzrf)

生成摘要时出错

---

## 22. MSG Made Dossier on Activists Who Opposed Facial Recognition

**原文标题**: MSG Made Dossier on Activists Who Opposed Facial Recognition

**原文链接**: [https://www.404media.co/madison-square-garden-made-dossier-on-activists-who-opposed-facial-recognition/](https://www.404media.co/madison-square-garden-made-dossier-on-activists-who-opposed-facial-recognition/)

生成摘要时出错

---

## 23. Show HN: Bun-sqlgen – Type-safe raw SQL for Bun, no ORM

**原文标题**: Show HN: Bun-sqlgen – Type-safe raw SQL for Bun, no ORM

**原文链接**: [https://github.com/ilbertt/bun-sqlgen](https://github.com/ilbertt/bun-sqlgen)

生成摘要时出错

---

## 24. The Low-Tech AI of Elden Ring

**原文标题**: The Low-Tech AI of Elden Ring

**原文链接**: [https://nega.tv/posts/low-tech-ai-of-elden-ring.html](https://nega.tv/posts/low-tech-ai-of-elden-ring.html)

生成摘要时出错

---

## 25. Will It Mythos?

**原文标题**: Will It Mythos?

**原文链接**: [https://swelljoe.com/post/will-it-mythos/](https://swelljoe.com/post/will-it-mythos/)

生成摘要时出错

---

## 26. Finding the best dog treat with statistics

**原文标题**: Finding the best dog treat with statistics

**原文链接**: [https://www.wespiser.com/posts/2026-06-19-best-dog-treat.html](https://www.wespiser.com/posts/2026-06-19-best-dog-treat.html)

生成摘要时出错

---

## 27. What we call "age verification" is actually mass surveillance

**原文标题**: What we call "age verification" is actually mass surveillance

**原文链接**: [https://pluralistic.net/2026/06/23/destroy-the-village/](https://pluralistic.net/2026/06/23/destroy-the-village/)

生成摘要时出错

---

## 28. Lossless GIF recompression via exhaustive search

**原文标题**: Lossless GIF recompression via exhaustive search

**原文链接**: [https://blog.arusekk.pl/posts/lossless-gif-recompression/](https://blog.arusekk.pl/posts/lossless-gif-recompression/)

生成摘要时出错

---

## 29. Open Source for IBM Z and LinuxONE

**原文标题**: Open Source for IBM Z and LinuxONE

**原文链接**: [https://community.ibm.com/community/user/blogs/elizabeth-k-joseph1/2026/06/18/linuxone-open-source-report-may-2026](https://community.ibm.com/community/user/blogs/elizabeth-k-joseph1/2026/06/18/linuxone-open-source-report-may-2026)

生成摘要时出错

---

## 30. VibeThinker: 3B param model that beats Opus 4.5 on reasoning with novel SFT+GRPO

**原文标题**: VibeThinker: 3B param model that beats Opus 4.5 on reasoning with novel SFT+GRPO

**原文链接**: [https://arxiv.org/abs/2606.16140](https://arxiv.org/abs/2606.16140)

生成摘要时出错

---

## 31. Show HN: Treedocs: Documentation that automatically checks for staleness

**原文标题**: Show HN: Treedocs: Documentation that automatically checks for staleness

**原文链接**: [https://dandylyons.github.io/treedocs/](https://dandylyons.github.io/treedocs/)

生成摘要时出错

---

## 32. 80386 Early Start Memory Access

**原文标题**: 80386 Early Start Memory Access

**原文链接**: [https://nand2mario.github.io/posts/2026/80386_early_start/](https://nand2mario.github.io/posts/2026/80386_early_start/)

生成摘要时出错

---

## 33. Steam Machine launches today

**原文标题**: Steam Machine launches today

**原文链接**: [https://store.steampowered.com/news/group/45479024/view/685257114654870245](https://store.steampowered.com/news/group/45479024/view/685257114654870245)

生成摘要时出错

---

## 34. Crypto in 2026: Oh, This Is the Bad Place

**原文标题**: Crypto in 2026: Oh, This Is the Bad Place

**原文链接**: [https://www.stephendiehl.com/posts/bad_place_2026/](https://www.stephendiehl.com/posts/bad_place_2026/)

生成摘要时出错

---

## 35. In praise of memcached

**原文标题**: In praise of memcached

**原文链接**: [https://jchri.st/blog/in-praise-of-memcached/](https://jchri.st/blog/in-praise-of-memcached/)

生成摘要时出错

---

## 36. Rethinking Modularity in Ruby Applications

**原文标题**: Rethinking Modularity in Ruby Applications

**原文链接**: [https://noteflakes.com/articles/2026-06-18-syntropy-modules](https://noteflakes.com/articles/2026-06-18-syntropy-modules)

生成摘要时出错

---

## 37. Giant Banana Pulled Over: Driver Says Cops Have Stopped Him 100s of Times

**原文标题**: Giant Banana Pulled Over: Driver Says Cops Have Stopped Him 100s of Times

**原文链接**: [https://cowboystatedaily.com/2026/06/18/giant-banana-pulled-over-in-montana-driver-says-cops-have-stopped-him-100s-of-times/](https://cowboystatedaily.com/2026/06/18/giant-banana-pulled-over-in-montana-driver-says-cops-have-stopped-him-100s-of-times/)

生成摘要时出错

---

## 38. Show HN: Neural Particle Automata

**原文标题**: Show HN: Neural Particle Automata

**原文链接**: [https://selforg-npa.github.io/](https://selforg-npa.github.io/)

生成摘要时出错

---

## 39. Digital euro clears key hurdle as EU seeks to break free from U.S. credit cards

**原文标题**: Digital euro clears key hurdle as EU seeks to break free from U.S. credit cards

**原文链接**: [https://finance.yahoo.com/markets/currencies/articles/ecb-secures-key-parliamentary-backing-102718449.html](https://finance.yahoo.com/markets/currencies/articles/ecb-secures-key-parliamentary-backing-102718449.html)

生成摘要时出错

---

## 40. Millions in UK could claim share of £3B after Apple case given green light

**原文标题**: Millions in UK could claim share of £3B after Apple case given green light

**原文链接**: [https://www.bbc.co.uk/news/articles/c932d1r0p96o](https://www.bbc.co.uk/news/articles/c932d1r0p96o)

生成摘要时出错

---

## 41. Pact: Anonymous Credentials for the Web

**原文标题**: Pact: Anonymous Credentials for the Web

**原文链接**: [https://hacks.mozilla.org/2026/06/pact-anonymous-credentials-for-the-web/](https://hacks.mozilla.org/2026/06/pact-anonymous-credentials-for-the-web/)

生成摘要时出错

---

## 42. Show HN: Shumai – open-source Frame.io alternative for creative work

**原文标题**: Show HN: Shumai – open-source Frame.io alternative for creative work

**原文链接**: [https://github.com/shumaiOne/shumai](https://github.com/shumaiOne/shumai)

生成摘要时出错

---

## 43. I am a person who will look at the Steam Machine and cry

**原文标题**: I am a person who will look at the Steam Machine and cry

**原文链接**: [https://blog.zarfhome.com/2026/06/steam-machine-oh-no](https://blog.zarfhome.com/2026/06/steam-machine-oh-no)

生成摘要时出错

---

## 44. Kyber (YC W23) Is Hiring a Head of Engineering

**原文标题**: Kyber (YC W23) Is Hiring a Head of Engineering

**原文链接**: [https://www.ycombinator.com/companies/kyber/jobs/FGmI8mx-head-of-engineering](https://www.ycombinator.com/companies/kyber/jobs/FGmI8mx-head-of-engineering)

生成摘要时出错

---

## 45. The Traditional Vi (2007)

**原文标题**: The Traditional Vi (2007)

**原文链接**: [https://ex-vi.sourceforge.net/](https://ex-vi.sourceforge.net/)

生成摘要时出错

---

## 46. Israel targeted Gaza children resulting in genocide, UN inquiry says

**原文标题**: Israel targeted Gaza children resulting in genocide, UN inquiry says

**原文链接**: [https://www.reuters.com/world/middle-east/israel-targeted-gaza-children-resulting-genocide-un-inquiry-says-2026-06-23/](https://www.reuters.com/world/middle-east/israel-targeted-gaza-children-resulting-genocide-un-inquiry-says-2026-06-23/)

生成摘要时出错

---

## 47. OpenAI DayBreak – GPT-5.5-Cyber

**原文标题**: OpenAI DayBreak – GPT-5.5-Cyber

**原文链接**: [https://openai.com/index/daybreak-securing-the-world/](https://openai.com/index/daybreak-securing-the-world/)

生成摘要时出错

---

## 48. 8086 Segmented Memory was a good idea

**原文标题**: 8086 Segmented Memory was a good idea

**原文链接**: [https://owl.billpg.com/8086-segmented-memory-was-a-good-idea-almost/](https://owl.billpg.com/8086-segmented-memory-was-a-good-idea-almost/)

生成摘要时出错

---

## 49. GLM-5.2 – How to Run Locally

**原文标题**: GLM-5.2 – How to Run Locally

**原文链接**: [https://unsloth.ai/docs/models/glm-5.2](https://unsloth.ai/docs/models/glm-5.2)

生成摘要时出错

---

## 50. Optocam Zero: a Pi Zero based digital camera made using off the shelf components

**原文标题**: Optocam Zero: a Pi Zero based digital camera made using off the shelf components

**原文链接**: [https://github.com/dorukkumkumoglu/optocamzero](https://github.com/dorukkumkumoglu/optocamzero)

生成摘要时出错

---

## 51. AI's Affordability Crisis

**原文标题**: AI's Affordability Crisis

**原文链接**: [https://blog.dshr.org/2026/06/ais-affordability-crisis.html](https://blog.dshr.org/2026/06/ais-affordability-crisis.html)

生成摘要时出错

---

## 52. Backblaze Announces Five-Year Multi-Exabyte Agreement with CoreWeave

**原文标题**: Backblaze Announces Five-Year Multi-Exabyte Agreement with CoreWeave

**原文链接**: [https://www.businesswire.com/news/home/20260622788628/en/Backblaze-Announces-Five-Year-Multi-Exabyte-Data-Storage-Agreement-with-CoreWeave](https://www.businesswire.com/news/home/20260622788628/en/Backblaze-Announces-Five-Year-Multi-Exabyte-Data-Storage-Agreement-with-CoreWeave)

生成摘要时出错

---

## 53. An Introduction to YOLO26

**原文标题**: An Introduction to YOLO26

**原文链接**: [https://blog.roboflow.com/yolo26/](https://blog.roboflow.com/yolo26/)

生成摘要时出错

---

## 54. A Man Was Gifted His Dream Car by the Notorious Hacker He Put in Prison

**原文标题**: A Man Was Gifted His Dream Car by the Notorious Hacker He Put in Prison

**原文链接**: [https://www.thedrive.com/news/this-man-was-gifted-his-dream-car-by-the-notorious-hacker-he-put-in-prison](https://www.thedrive.com/news/this-man-was-gifted-his-dream-car-by-the-notorious-hacker-he-put-in-prison)

生成摘要时出错

---

## 55. Show HN: Oak – Git alternative designed for agents

**原文标题**: Show HN: Oak – Git alternative designed for agents

**原文链接**: [https://oak.space/oak/oak](https://oak.space/oak/oak)

生成摘要时出错

---

## 56. SpaceX launches $25B notes offering, source says

**原文标题**: SpaceX launches $25B notes offering, source says

**原文链接**: [https://www.reuters.com/legal/transactional/spacex-launches-25-billion-notes-offering-source-says-2026-06-23/](https://www.reuters.com/legal/transactional/spacex-launches-25-billion-notes-offering-source-says-2026-06-23/)

生成摘要时出错

---

## 57. Wikipedia cofounder Larry Sanger blocked from editing Wikipedia

**原文标题**: Wikipedia cofounder Larry Sanger blocked from editing Wikipedia

**原文链接**: [https://en.wikipedia.org/wiki/User:Larry_Sanger](https://en.wikipedia.org/wiki/User:Larry_Sanger)

生成摘要时出错

---

## 58. Help I accidentally a wigglegram

**原文标题**: Help I accidentally a wigglegram

**原文链接**: [https://lmao.center/blog/wiggle-accidents/](https://lmao.center/blog/wiggle-accidents/)

生成摘要时出错

---

## 59. Canada plans 'nuclear renaissance' with up to 10 reactors built by 2040

**原文标题**: Canada plans 'nuclear renaissance' with up to 10 reactors built by 2040

**原文链接**: [https://www.cbc.ca/news/politics/federal-nuclear-strategy-9.7244509](https://www.cbc.ca/news/politics/federal-nuclear-strategy-9.7244509)

生成摘要时出错

---

## 60. The new HTTP QUERY method explained

**原文标题**: The new HTTP QUERY method explained

**原文链接**: [https://kreya.app/blog/new-http-query-method-explained/](https://kreya.app/blog/new-http-query-method-explained/)

生成摘要时出错

---

## 61. British Columbia, Time Zones, and Postgres

**原文标题**: British Columbia, Time Zones, and Postgres

**原文链接**: [https://www.crunchydata.com/blog/british-columbia-and-time-zone-changes](https://www.crunchydata.com/blog/british-columbia-and-time-zone-changes)

生成摘要时出错

---

## 62. Show HN: Got sick of ads, so I made my own logic puzzle site

**原文标题**: Show HN: Got sick of ads, so I made my own logic puzzle site

**原文链接**: [https://puzzlelair.com/](https://puzzlelair.com/)

生成摘要时出错

---

## 63. Show HN: A pure ARM64 Assembly web server, now on Linux with CGI for no reason

**原文标题**: Show HN: A pure ARM64 Assembly web server, now on Linux with CGI for no reason

**原文链接**: [https://github.com/imtomt/ymawky/tree/linux](https://github.com/imtomt/ymawky/tree/linux)

生成摘要时出错

---

## 64. CL-BBS: the schemeBBS-like textboard rewritten in Common Lisp

**原文标题**: CL-BBS: the schemeBBS-like textboard rewritten in Common Lisp

**原文链接**: [https://github.com/ryukinix/cl-bbs](https://github.com/ryukinix/cl-bbs)

生成摘要时出错

---

## 65. Performance of WebAssembly Runtimes in 2026

**原文标题**: Performance of WebAssembly Runtimes in 2026

**原文链接**: [https://00f.net/2026/06/23/webassembly-runtimes-2026/](https://00f.net/2026/06/23/webassembly-runtimes-2026/)

生成摘要时出错

---

## 66. Deno Desktop

**原文标题**: Deno Desktop

**原文链接**: [https://docs.deno.com/runtime/desktop/](https://docs.deno.com/runtime/desktop/)

生成摘要时出错

---

## 67. Why Windows 95 Was Tech's Last True Revolution

**原文标题**: Why Windows 95 Was Tech's Last True Revolution

**原文链接**: [https://comuniq.xyz/post.php?t=1307](https://comuniq.xyz/post.php?t=1307)

生成摘要时出错

---

## 68. Matrix and Quaternion FAQ

**原文标题**: Matrix and Quaternion FAQ

**原文链接**: [https://j3d.org/matrix_faq/matrfaq_latest.html](https://j3d.org/matrix_faq/matrfaq_latest.html)

生成摘要时出错

---

## 69. Package Managers need global hooks

**原文标题**: Package Managers need global hooks

**原文链接**: [https://captnemo.in/blog/2026/06/17/package-managers-need-hooks/](https://captnemo.in/blog/2026/06/17/package-managers-need-hooks/)

生成摘要时出错

---

## 70. Who Does What? Team Topologies for the Agentic Platform

**原文标题**: Who Does What? Team Topologies for the Agentic Platform

**原文链接**: [https://blog.owulveryck.info/2026/06/22/who-does-what-team-topologies-for-the-agentic-platform.html](https://blog.owulveryck.info/2026/06/22/who-does-what-team-topologies-for-the-agentic-platform.html)

生成摘要时出错

---

## 71. Improvements to Std:Format in C++26

**原文标题**: Improvements to Std:Format in C++26

**原文链接**: [https://mariusbancila.ro/blog/2026/06/19/improvements-to-stdformat-in-c26/](https://mariusbancila.ro/blog/2026/06/19/improvements-to-stdformat-in-c26/)

生成摘要时出错

---

## 72. Flock-Powered Police Chiefs Stalking Women Shows Why Warrants Are Needed

**原文标题**: Flock-Powered Police Chiefs Stalking Women Shows Why Warrants Are Needed

**原文链接**: [https://ipvm.com/reports/police-chiefs-track](https://ipvm.com/reports/police-chiefs-track)

生成摘要时出错

---

## 73. Prompt Injection as Role Confusion

**原文标题**: Prompt Injection as Role Confusion

**原文链接**: [https://role-confusion.github.io](https://role-confusion.github.io)

生成摘要时出错

---

## 74. LastPass confirms data breach in Klue supply chain attack

**原文标题**: LastPass confirms data breach in Klue supply chain attack

**原文链接**: [https://www.bleepingcomputer.com/news/security/lastpass-confirms-data-breach-in-klue-supply-chain-attack/](https://www.bleepingcomputer.com/news/security/lastpass-confirms-data-breach-in-klue-supply-chain-attack/)

生成摘要时出错

---

## 75. Is it time for a new Embedded Linux build system?

**原文标题**: Is it time for a new Embedded Linux build system?

**原文链接**: [https://yoebuild.org/blog/time-for-a-new-build-system/](https://yoebuild.org/blog/time-for-a-new-build-system/)

生成摘要时出错

---

## 76. Cyberdecks, going analog, and convivial technology

**原文标题**: Cyberdecks, going analog, and convivial technology

**原文链接**: [https://blog.hydroponictrash.solar/cyberdecks-going-analog-and-convivial-technology/](https://blog.hydroponictrash.solar/cyberdecks-going-analog-and-convivial-technology/)

生成摘要时出错

---

## 77. Chevron signs 20-year power agreement with Microsoft for West Texas data center

**原文标题**: Chevron signs 20-year power agreement with Microsoft for West Texas data center

**原文链接**: [https://www.chevron.com/newsroom/2026/q2/chevron-signs-20-year-power-agreement-with-microsoft-for-west-texas-data-center](https://www.chevron.com/newsroom/2026/q2/chevron-signs-20-year-power-agreement-with-microsoft-for-west-texas-data-center)

生成摘要时出错

---

## 78. Windows NT for GameCube/Wii

**原文标题**: Windows NT for GameCube/Wii

**原文链接**: [https://github.com/Wack0/entii-for-workcubes](https://github.com/Wack0/entii-for-workcubes)

生成摘要时出错

---

## 79. Polymarket has flooded social media with deceptive videos by paid creators

**原文标题**: Polymarket has flooded social media with deceptive videos by paid creators

**原文链接**: [https://www.wsj.com/business/media/polymarket-social-media-bets-prediction-market-441cdeb5?st=HhTZY2](https://www.wsj.com/business/media/polymarket-social-media-bets-prediction-market-441cdeb5?st=HhTZY2)

生成摘要时出错

---

## 80. Canyon HUD helmet for road riding

**原文标题**: Canyon HUD helmet for road riding

**原文链接**: [https://media-centre.canyon.com/en-INT/266866-new-canyon-heads-up-display-helmet-could-be-a-safety-gamechanger-for-road-riding/](https://media-centre.canyon.com/en-INT/266866-new-canyon-heads-up-display-helmet-could-be-a-safety-gamechanger-for-road-riding/)

生成摘要时出错

---

## 81. My Mathematical Regression

**原文标题**: My Mathematical Regression

**原文链接**: [https://blog.dahl.dev/posts/my-mathematical-regression/](https://blog.dahl.dev/posts/my-mathematical-regression/)

生成摘要时出错

---

## 82. Die analysis of the 8087 math coprocessor's fast bit shifter (2020)

**原文标题**: Die analysis of the 8087 math coprocessor's fast bit shifter (2020)

**原文链接**: [https://www.righto.com/2020/05/die-analysis-of-8087-math-coprocessors.html](https://www.righto.com/2020/05/die-analysis-of-8087-math-coprocessors.html)

生成摘要时出错

---

## 83. Pledging another $400k to the Zig software foundation

**原文标题**: Pledging another $400k to the Zig software foundation

**原文链接**: [https://mitchellh.com/writing/zig-donation-2026](https://mitchellh.com/writing/zig-donation-2026)

生成摘要时出错

---

## 84. Show HN: CleverCrow: give tokens to your favorite projects

**原文标题**: Show HN: CleverCrow: give tokens to your favorite projects

**原文链接**: [https://clevercrow.io](https://clevercrow.io)

生成摘要时出错

---

## 85. Munich 1991: The Roots of the Current AI Boom

**原文标题**: Munich 1991: The Roots of the Current AI Boom

**原文链接**: [https://people.idsia.ch/~juergen/ai-boom-roots-munich-1991.html](https://people.idsia.ch/~juergen/ai-boom-roots-munich-1991.html)

生成摘要时出错

---

## 86. DisplayMate

**原文标题**: DisplayMate

**原文链接**: [https://www.displaymate.com/](https://www.displaymate.com/)

生成摘要时出错

---

## 87. Self-Attention Solved the Sequential Bottleneck

**原文标题**: Self-Attention Solved the Sequential Bottleneck

**原文链接**: [https://www.pathtostaff.com/p/everything-a-senior-engineer-needs](https://www.pathtostaff.com/p/everything-a-senior-engineer-needs)

生成摘要时出错

---

## 88. Apple is going to raise device prices, but when?

**原文标题**: Apple is going to raise device prices, but when?

**原文链接**: [https://daringfireball.net/linked/2026/06/22/apple-device-prices-when](https://daringfireball.net/linked/2026/06/22/apple-device-prices-when)

生成摘要时出错

---

## 89. Epidurals are a miracle technology

**原文标题**: Epidurals are a miracle technology

**原文链接**: [https://worksinprogress.co/issue/the-wonder-of-epidurals/](https://worksinprogress.co/issue/the-wonder-of-epidurals/)

生成摘要时出错

---

## 90. The text in Claude Code’s “Extended Thinking” output

**原文标题**: The text in Claude Code’s “Extended Thinking” output

**原文链接**: [https://patrickmccanna.net/the-text-in-claude-codes-extended-thinking-output-is-not-authentic/](https://patrickmccanna.net/the-text-in-claude-codes-extended-thinking-output-is-not-authentic/)

生成摘要时出错

---

## 91. ytr: YouTube Radio for Emacs

**原文标题**: ytr: YouTube Radio for Emacs

**原文链接**: [https://xenodium.com/ytr-youtube-radio-for-emacs](https://xenodium.com/ytr-youtube-radio-for-emacs)

生成摘要时出错

---

## 92. Job application asked for my SAT scores

**原文标题**: Job application asked for my SAT scores

**原文链接**: [https://mrmarket.lol/job-application-asked-for-my-sat-scores/](https://mrmarket.lol/job-application-asked-for-my-sat-scores/)

生成摘要时出错

---

## 93. Moebius: 0.2B image inpainting model with 10B-level performance

**原文标题**: Moebius: 0.2B image inpainting model with 10B-level performance

**原文链接**: [https://hustvl.github.io/Moebius/](https://hustvl.github.io/Moebius/)

生成摘要时出错

---

## 94. Sakana Fugu

**原文标题**: Sakana Fugu

**原文链接**: [https://sakana.ai/fugu/](https://sakana.ai/fugu/)

生成摘要时出错

---

## 95. Japanese symbols that speak without words

**原文标题**: Japanese symbols that speak without words

**原文链接**: [https://arun.is/blog/japan-symbols/](https://arun.is/blog/japan-symbols/)

生成摘要时出错

---

## 96. Nintendo Wii U games running from a 1980's Bernoulli disk [video]

**原文标题**: Nintendo Wii U games running from a 1980's Bernoulli disk [video]

**原文链接**: [https://www.youtube.com/watch?v=8GZDOpV2OXk](https://www.youtube.com/watch?v=8GZDOpV2OXk)

生成摘要时出错

---

## 97. Show HN: Pagecast – Publish Markdown/HTML Reports to Cloudflare Pages

**原文标题**: Show HN: Pagecast – Publish Markdown/HTML Reports to Cloudflare Pages

**原文链接**: [https://github.com/Amal-David/pagecast](https://github.com/Amal-David/pagecast)

生成摘要时出错

---

## 98. Ultralytics YOLO26: Unified Real-Time End-to-End Vision Models

**原文标题**: Ultralytics YOLO26: Unified Real-Time End-to-End Vision Models

**原文链接**: [https://arxiv.org/abs/2606.03748](https://arxiv.org/abs/2606.03748)

生成摘要时出错

---

## 99. GLM 5.2 vs. Opus

**原文标题**: GLM 5.2 vs. Opus

**原文链接**: [https://techstackups.com/comparisons/glm-5.2-vs-opus/](https://techstackups.com/comparisons/glm-5.2-vs-opus/)

生成摘要时出错

---

## 100. window.showDirectoryPicker opens up a whole new world

**原文标题**: window.showDirectoryPicker opens up a whole new world

**原文链接**: [https://steveharrison.dev/showdirectorypicker-opens-up-a-whole-new-world/](https://steveharrison.dev/showdirectorypicker-opens-up-a-whole-new-world/)

生成摘要时出错

---

