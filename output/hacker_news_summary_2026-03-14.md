# Hacker News 热门文章摘要 (2026-03-14)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 当美国经济数据变得不可靠时会发生什么

**原文标题**: What happens when US economic data becomes unreliable

**原文链接**: [https://mitsloan.mit.edu/ideas-made-to-matter/what-happens-when-us-economic-data-becomes-unreliable](https://mitsloan.mit.edu/ideas-made-to-matter/what-happens-when-us-economic-data-becomes-unreliable)

由13家主要统计机构管理的美国经济数据系统正面临可靠性危机，威胁到公共和私营部门的明智决策。麻省理工学院教授罗伯托·里戈本（Roberto Rigobon）和哈佛大学教授阿尔贝托·卡瓦略（Alberto Cavallo）指出了削弱该系统完整性的三大主要挑战：

*   **调查响应率下降：** 家庭和企业参与度的急剧下降削弱了就业和通胀等关键指标的代表性，导致了偏差和数据修正的延迟。
*   **资金限制：** 人口普查局和劳工统计局（BLS）等机构的预算缩减阻碍了技术进步。一个显著的后果是，美国农业部（USDA）最近因成本问题决定停止其年度粮食不安全状况调查。
*   **政治干预：** 政府停摆、统计机构负责人被解雇，以及针对常规数据修正的公开抨击，损害了机构的透明度和公信力。

作者警告称，这些“裂痕”会导致政策误判、投资者信心丧失和公众参与度降低。为了缓解这些风险，作者为商界领袖提出了两项主要的行动建议：

1.  **将私营部门数据作为补充：** 虽然私营部门数据可以提供有用的独立核查并填补空白，但它无法取代官方统计数据。私营数据往往缺乏政府数据固有的广度、透明度和对社会问题的关注。
2.  **倡导机构独立性：** 商界领袖应积极抵制对数据的政治操弄，并公开反对威胁市场稳定的政策。

文章最后指出，可靠的统计数据是民主治理的基石。加强美国统计体系对于确保决策者、企业和家庭能够基于对经济现实的共同理解做出明智决策至关重要。

---

## 2. 蒙大拿州通过《计算权法案》(2025)

**原文标题**: Montana passes Right to Compute act (2025)

**原文链接**: [https://www.westernmt.news/2025/04/21/montana-leads-the-nation-with-groundbreaking-right-to-compute-act/](https://www.westernmt.news/2025/04/21/montana-leads-the-nation-with-groundbreaking-right-to-compute-act/)

无法访问文章链接。

---

## 3. 1M context is now generally available for Opus 4.6 and Sonnet 4.6

**原文标题**: 1M context is now generally available for Opus 4.6 and Sonnet 4.6

**原文链接**: [https://claude.com/blog/1m-context-ga](https://claude.com/blog/1m-context-ga)

生成摘要时出错

---

## 4. Baochip-1x：它是什么，我为什么现在做它，以及它是如何诞生的

**原文标题**: Baochip-1x: What it is, why I'm doing it now and how it came about

**原文链接**: [https://www.crowdsupply.com/baochip/dabao/updates/what-it-is-why-im-doing-it-now-and-how-it-came-about](https://www.crowdsupply.com/baochip/dabao/updates/what-it-is-why-im-doing-it-now-and-how-it-came-about)

在本次项目更新中，Andrew ‘bunnie’ Huang 介绍了 Baochip-1x，这是一款搭载于大宝（Dabao）评估板上的 RISC-V 微控制器。该芯片的主要特色在于内置了内存管理单元（MMU），这一功能在小型嵌入式 SoC 中传统上会被省略，以避免与高端处理器竞争。MMU 实现了安全、隔离的虚拟内存空间，使芯片能够运行 Linux 或基于 Rust 的 Xous 等复杂操作系统。

Baochip-1x 采用了“大部分开源 RTL”的设计方案。虽然 USB PHY 和模拟焊盘等某些组件仍是闭源的“连线”，但所有负责计算或转换数据的逻辑均公开可查。Huang 认为，这种务实的方法对于在当下构建成熟的开源软件栈至关重要，而非苦等十年以期实现完全开源的芯片生态系统。

该芯片的生产是通过在 Crossbar 公司设计的 22nm RRAM（阻变存储器）芯片上“搭便车”实现的。通过在芯片布局的闲置空间中置入开源的 Vexriscv CPU 核心，Huang 创造了一款具有“双重人格”的芯片，可在专有 ARM 核心与开源 RISC-V 核心之间切换。此次合作还利用了 RRAM 技术，其扩展性优于传统闪存，且写入速度更快。

该项目目前正在 Crowd Supply 上进行众筹，并已提供经手工筛选的工程样品。预计随后将进行合格芯片的量产，并于 2026 年底实现更广泛的供货。其目标是通过在当下提供可获取的硬件安全原语，赋能开发者构建一个更可信、架构更开放的未来。

---

## 5. Bzip 颂

**原文标题**: An Ode to Bzip

**原文链接**: [https://purplesyringa.moe/blog/an-ode-to-bzip/](https://purplesyringa.moe/blog/an-ode-to-bzip/)

在《Bzip 颂》中，作者认为 bzip 系列算法在压缩代码方面——特别是在 Minecraft 的 ComputerCraft 模组应用场景中——优于 gzip、zstd 和 xz 等现代标准。

虽然大多数流行的压缩算法依赖于 LZ77（通过后向引用替换重复文本），但 bzip 使用的是 Burrows-Wheeler 变换 (BWT)。BWT 通过重新排列字符并按上下文进行分组，作者证明这种方法在处理 Lua 代码和英文文本时显著更有效。在对一个 327 KB 文件的测试中，bzip2 和 bzip3 的表现优于所有其他编码器，包括像 lzip 和 brotli 这种通常以高压缩比著称的算法。

作者强调了 bzip 方法的几个关键优势：
*   **确定性逻辑：** 与基于 LZ77 的格式不同（这类格式需要复杂耗时的启发式算法和“暴力”搜索来寻找最佳匹配），BWT 是确定性的。这使得编写高效的编码器变得更加容易，且无需反复微调。
*   **极小的解码器体积：** 在 Lua 中创建自解压归档文件时，解码器的体积至关重要。作者指出，一个精简的 bzip2 风格解码器可以小到 1.5 KB，比几乎任何替代方案都更紧凑、更高效。
*   **特定场景下的速度：** 尽管由于反向 BWT 的内存密集型特性，bzip 通常比 gzip 慢，但在像 Lua 这样的高级语言中，这种性能差距可以忽略不计，因为此时的首要目标是满足严格的磁盘空间限制。

最后，作者得出结论：bzip 是处理文本类数据时一颗被忽视的瑰宝。通过放弃标准格式的兼容性并专注于核心 BWT 流水线，开发者可以获得比“现代”替代方案更高的压缩比和更小的解码器占用空间。

---

## 6. Python：优化阶梯

**原文标题**: Python: The Optimization Ladder

**原文链接**: [https://cemrehancavdar.com/2026/03/10/optimization-ladder/](https://cemrehancavdar.com/2026/03/10/optimization-ladder/)

《优化阶梯》探讨了 Python 为何天生运行缓慢，以及开发者如何利用各种工具系统地提升性能。Python 的缓慢不仅是因为 GIL 或解释执行，更是其**动态设计**的结果。这种设计导致了昂贵的运行时分派和巨大的对象开销（例如，一个 4 字节的整数竟需要 28 字节的内存）。

作者将优化划分为一个难度递增的“阶梯”：

*   **第 0 阶：CPython 升级**：从 3.10 升级到 3.13，通过自适应特化（adaptive specialization）可获得高达 1.4 倍的“免费”加速。
*   **第 1 阶：替代运行时**：像 **PyPy** 和 **GraalPy** 这样的 JIT 编译运行时在无需更改代码的情况下可提供 6–66 倍的加速，但面临生态系统兼容性障碍。
*   **第 2 阶：Mypyc**：将带有类型注解的 Python 编译为 C 扩展，以极小的代价实现 2–14 倍的性能提升。
*   **第 3 阶：NumPy & JAX**：这些库将数学运算委托给编译后的后端（BLAS/XLA）。**JAX** 实现了最惊人的结果（超过 1,600 倍加速），证明了即便 Python 运行循环很慢，它也是编译代码的顶级调度者。
*   **第 4 和 5 阶：Numba & Cython**：这些工具通过 LLVM 或 C 编译代码，使速度接近原生水平（最高 135 倍）。然而，它们需要将数据重构为数组，或需要开发者避开隐性性能损耗的“雷区”。
*   **第 6 阶：新兴工具**：像 **Mojo、Codon 和 Taichi** 这样新的语言和编译器展现了巨大的潜力（最高 198 倍），但目前仍存在“磨合期”且库支持有限。

文章总结道，虽然 Python 的默认计算速度较慢，但“优化阶梯”让开发者能够绕过其动态开销。关键在于根据具体问题匹配合适的工具，在开发成本与所需的性能收益之间取得平衡。

---

## 7. 电影中的 NMAP

**原文标题**: NMAP in the Movies

**原文链接**: [https://nmap.org/movies/](https://nmap.org/movies/)

文章《电影中的 Nmap》记录了现实世界的网络扫描工具 Nmap 频繁作为电影道具使用，为黑客场景增添技术真实感。作者 Nmap 创始人 Fyodor 指出，好莱坞正逐渐摒弃不切实际的 3D 动画，转而通过展示 Nmap 的实际界面来描绘数字入侵。

该工具最著名的出镜是在《黑客帝国2：重装上阵》中，崔妮蒂（Trinity）使用特定版本的 Nmap 和真实的 SSH 漏洞利用程序入侵了电网。这为随后众多知名电影的技术准确性奠定了先例，包括：

*   **《瞒天过海：美人计》**：蕾哈娜饰演的角色使用 Nmap 进行与抢劫相关的侦察。
*   **《斯诺登》**：描绘了在 CIA 培训期间使用 Nmap 及其脚本引擎（NSE）的情景。
*   **《谍影重重3》**：展示了使用 Zenmap（Nmap 的图形界面）入侵邮件服务器。
*   **《虎胆龙威4》**：展示了主角的黑客盟友在国家级网络攻击期间使用该工具。
*   **科幻与超级英雄电影**：Nmap 出现在《特警判官》、《极乐空间》（扫描人类大脑）、《神奇四侠》以及《正义联盟：毁灭》（由蝙蝠侠使用）中。

文章还强调了该工具在国际影片中的亮相，如瑞典的《龙纹身的女孩》、德国的《我是谁：没有绝对安全的系统》以及日本的《大逃杀》。

Fyodor 维护这一名录以纪念这些客串，并为寻求提升黑客场景真实感的电影制作人提供专业指导。最终，Nmap 在电影中的出现是对网络安全界的一种“致敬”，用全球安全专业人士使用的正规工具取代了那些华而不实的视觉特效。

---

## 8. 饼干罐里的美国媚俗美学 (2023)

**原文标题**: Cookie jars capture American kitsch (2023)

**原文链接**: [https://www.eater.com/23651631/cookie-jar-trend-appreciation-collecting-history](https://www.eater.com/23651631/cookie-jar-trend-appreciation-collecting-history)

《“饼干罐捕捉美式媚俗艺术”》探讨了陶瓷饼干罐作为雕塑艺术和文化时代印记的长久魅力及其现代复兴。虽然其传统功能是存放甜点，但许多当代收藏家和艺术家（如 Hazy Mae）却用它们来存放食谱、金钱或办公用品等“零碎物件”，而非饼干。糕点师们也佐证了这种讽刺现象，他们指出陶瓷罐的保鲜性能通常较差，因此更适合短期储存或纯粹装饰。

文章强调了受怀旧情结和现代陶艺兴趣驱动，这类物品正迎来一股欣赏“新浪潮”。高端品牌和艺术家正在助推这一趋势：Supreme 与 Pillsbury 合作推出了“面团宝宝”（Doughboy）饼干罐；Williams-Sonoma 重新设计的米老鼠饼干罐出现在了蕾哈娜（Rihanna）的厨房里；而 Hazy Mae 制作的手工角色罐——包含蒂娜·特纳和猫王等偶像造型——单价超过 800 美元。

历史上，饼干罐在 20 世纪 50 年代成为美国厨房的必备品。收藏市场在 1988 年达到巅峰，当时安迪·沃霍尔的藏品在苏富比拍卖行以近 25 万美元的价格成交。尽管此后市场因仿制品而降温，但据“饼干罐夫人”梅赛德斯·迪伦佐·博尔杜克等专家称，在 90 年代复兴风潮和复古二手购物兴起的带动下，市场需求正再次攀升。

归根结底，饼干罐仍是自我表达的载体。无论是奇思妙想的森林生物、极简主义的中世纪复制品，还是反映更广泛社会历史（包括具冒犯性的历史成见）的人工制品，这些罐子都是能够彰显主人个性的“谈资”，并在复古媚俗艺术与当代设计之间架起了一座桥梁。

---

## 9. Megadev: A Development Kit for the Sega Mega Drive and Mega CD Hardware

**原文标题**: Megadev: A Development Kit for the Sega Mega Drive and Mega CD Hardware

**原文链接**: [https://github.com/drojaazu/megadev](https://github.com/drojaazu/megadev)

生成摘要时出错

---

## 10. AI Gets Wrong Woman Jailed for Six Months, Life Ruined

**原文标题**: AI Gets Wrong Woman Jailed for Six Months, Life Ruined

**原文链接**: [https://www.youtube.com/watch?v=mzS7dmCUzcQ](https://www.youtube.com/watch?v=mzS7dmCUzcQ)

生成摘要时出错

---

## 11. 9 Mothers Defense (YC P26) Is Hiring in Austin

**原文标题**: 9 Mothers Defense (YC P26) Is Hiring in Austin

**原文链接**: [https://jobs.ashbyhq.com/9-mothers?utm_source=x8pZ4B3P3Q](https://jobs.ashbyhq.com/9-mothers?utm_source=x8pZ4B3P3Q)

生成摘要时出错

---

## 12. UBI Is Your Productivity Dividend – The Only Way to All Share What We All Built

**原文标题**: UBI Is Your Productivity Dividend – The Only Way to All Share What We All Built

**原文链接**: [https://scottsantens.substack.com/p/universal-basic-income-is-your-productivity](https://scottsantens.substack.com/p/universal-basic-income-is-your-productivity)

生成摘要时出错

---

## 13. Wired headphone sales are exploding

**原文标题**: Wired headphone sales are exploding

**原文链接**: [https://www.bbc.com/future/article/20260310-wired-headphones-are-better-than-bluetooth](https://www.bbc.com/future/article/20260310-wired-headphones-are-better-than-bluetooth)

生成摘要时出错

---

## 14. Show HN: GitAgent – An open standard that turns any Git repo into an AI agent

**原文标题**: Show HN: GitAgent – An open standard that turns any Git repo into an AI agent

**原文链接**: [https://www.gitagent.sh/](https://www.gitagent.sh/)

生成摘要时出错

---

## 15. Philosoph Jürgen Habermas Gestorben

**原文标题**: Philosoph Jürgen Habermas Gestorben

**原文链接**: [https://www.spiegel.de/kultur/philosoph-juergen-habermas-mit-96-jahren-gestorben-a-8be73ac7-e722-4543-8344-4515c4040363](https://www.spiegel.de/kultur/philosoph-juergen-habermas-mit-96-jahren-gestorben-a-8be73ac7-e722-4543-8344-4515c4040363)

生成摘要时出错

---

## 16. Everything you never wanted to know about visually-hidden

**原文标题**: Everything you never wanted to know about visually-hidden

**原文链接**: [https://dbushell.com/2026/02/20/visually-hidden/](https://dbushell.com/2026/02/20/visually-hidden/)

生成摘要时出错

---

## 17. Online astroturfing: A problem beyond disinformation

**原文标题**: Online astroturfing: A problem beyond disinformation

**原文链接**: [https://journals.sagepub.com/doi/10.1177/01914537221108467](https://journals.sagepub.com/doi/10.1177/01914537221108467)

生成摘要时出错

---

## 18. RAM kits are now sold with one fake RAM stick alongside a real one

**原文标题**: RAM kits are now sold with one fake RAM stick alongside a real one

**原文链接**: [https://www.tomshardware.com/pc-components/ram/fake-ram-bundled-with-real-ram-to-create-a-performance-illusion-for-amd-users-1-1-value-pack-offers-desperate-psychological-relief-as-the-memory-shortage-worsens](https://www.tomshardware.com/pc-components/ram/fake-ram-bundled-with-real-ram-to-create-a-performance-illusion-for-amd-users-1-1-value-pack-offers-desperate-psychological-relief-as-the-memory-shortage-worsens)

生成摘要时出错

---

## 19. XML Is a Cheap DSL

**原文标题**: XML Is a Cheap DSL

**原文链接**: [https://unplannedobsolescence.com/blog/xml-cheap-dsl/](https://unplannedobsolescence.com/blog/xml-cheap-dsl/)

生成摘要时出错

---

## 20. Nominal Types in WebAssembly

**原文标题**: Nominal Types in WebAssembly

**原文链接**: [https://wingolog.org/archives/2026/03/10/nominal-types-in-webassembly](https://wingolog.org/archives/2026/03/10/nominal-types-in-webassembly)

生成摘要时出错

---

## 21. Show HN: Channel Surfer – Watch YouTube like it’s cable TV

**原文标题**: Show HN: Channel Surfer – Watch YouTube like it’s cable TV

**原文链接**: [https://channelsurfer.tv](https://channelsurfer.tv)

生成摘要时出错

---

## 22. The Isolation Trap: Erlang

**原文标题**: The Isolation Trap: Erlang

**原文链接**: [https://causality.blog/essays/the-isolation-trap/](https://causality.blog/essays/the-isolation-trap/)

生成摘要时出错

---

## 23. Mouser: An open source alternative to Logi-Plus mouse software

**原文标题**: Mouser: An open source alternative to Logi-Plus mouse software

**原文链接**: [https://github.com/TomBadash/MouseControl](https://github.com/TomBadash/MouseControl)

生成摘要时出错

---

## 24. Digg is gone again

**原文标题**: Digg is gone again

**原文链接**: [https://digg.com/](https://digg.com/)

生成摘要时出错

---

## 25. Hammerspoon

**原文标题**: Hammerspoon

**原文链接**: [https://github.com/Hammerspoon/hammerspoon](https://github.com/Hammerspoon/hammerspoon)

生成摘要时出错

---

## 26. Can I run AI locally?

**原文标题**: Can I run AI locally?

**原文链接**: [https://www.canirun.ai/](https://www.canirun.ai/)

生成摘要时出错

---

## 27. I found 39 Algolia admin keys exposed across open source documentation sites

**原文标题**: I found 39 Algolia admin keys exposed across open source documentation sites

**原文链接**: [https://benzimmermann.dev/blog/algolia-docsearch-admin-keys](https://benzimmermann.dev/blog/algolia-docsearch-admin-keys)

生成摘要时出错

---

## 28. Secure Secrets Management for Cursor Cloud Agents

**原文标题**: Secure Secrets Management for Cursor Cloud Agents

**原文链接**: [https://infisical.com/blog/secure-secrets-management-for-cursor-cloud-agents](https://infisical.com/blog/secure-secrets-management-for-cursor-cloud-agents)

生成摘要时出错

---

## 29. Recursive Problems Benefit from Recursive Solutions

**原文标题**: Recursive Problems Benefit from Recursive Solutions

**原文链接**: [https://jnkr.tech/blog/recursive-benefits-recursive](https://jnkr.tech/blog/recursive-benefits-recursive)

生成摘要时出错

---

## 30. Atari 2600 BASIC Programming (2015)

**原文标题**: Atari 2600 BASIC Programming (2015)

**原文链接**: [https://huguesjohnson.com/programming/atari-2600-basic/](https://huguesjohnson.com/programming/atari-2600-basic/)

生成摘要时出错

---

## 31. Starlink Militarization and Its Impact on Global Strategic Stability

**原文标题**: Starlink Militarization and Its Impact on Global Strategic Stability

**原文链接**: [https://interpret.csis.org/translations/starlink-militarization-and-its-impact-on-global-strategic-stability/](https://interpret.csis.org/translations/starlink-militarization-and-its-impact-on-global-strategic-stability/)

生成摘要时出错

---

## 32. Show HN: Ink – Deploy full-stack apps from AI agents via MCP or Skills

**原文标题**: Show HN: Ink – Deploy full-stack apps from AI agents via MCP or Skills

**原文链接**: [https://ml.ink/](https://ml.ink/)

生成摘要时出错

---

## 33. Coding after coders: The end of computer programming as we know it?

**原文标题**: Coding after coders: The end of computer programming as we know it?

**原文链接**: [https://www.nytimes.com/2026/03/12/magazine/ai-coding-programming-jobs-claude-chatgpt.html?smid=url-share](https://www.nytimes.com/2026/03/12/magazine/ai-coding-programming-jobs-claude-chatgpt.html?smid=url-share)

生成摘要时出错

---

## 34. Michael Faraday: Scientist and Nonconformist (1996)

**原文标题**: Michael Faraday: Scientist and Nonconformist (1996)

**原文链接**: [http://silas.psfc.mit.edu/Faraday/](http://silas.psfc.mit.edu/Faraday/)

生成摘要时出错

---

## 35. I beg you to follow Crocker's Rules, even if you will be rude to me

**原文标题**: I beg you to follow Crocker's Rules, even if you will be rude to me

**原文链接**: [https://lr0.org/blog/p/crocker/](https://lr0.org/blog/p/crocker/)

生成摘要时出错

---

## 36. A Survival Guide to a PhD (2016)

**原文标题**: A Survival Guide to a PhD (2016)

**原文链接**: [http://karpathy.github.io/2016/09/07/phd/](http://karpathy.github.io/2016/09/07/phd/)

生成摘要时出错

---

## 37. Games with loot boxes to get minimum 16 age rating across Europe

**原文标题**: Games with loot boxes to get minimum 16 age rating across Europe

**原文链接**: [https://www.bbc.com/news/articles/cge84xqjg5lo](https://www.bbc.com/news/articles/cge84xqjg5lo)

生成摘要时出错

---

## 38. You gotta think outside the hypercube

**原文标题**: You gotta think outside the hypercube

**原文链接**: [https://lcamtuf.substack.com/p/you-gotta-think-outside-the-hypercube](https://lcamtuf.substack.com/p/you-gotta-think-outside-the-hypercube)

生成摘要时出错

---

## 39. Qatar helium shutdown puts chip supply chain on a two-week clock

**原文标题**: Qatar helium shutdown puts chip supply chain on a two-week clock

**原文链接**: [https://www.tomshardware.com/tech-industry/qatar-helium-shutdown-puts-chip-supply-chain-on-a-two-week-clock](https://www.tomshardware.com/tech-industry/qatar-helium-shutdown-puts-chip-supply-chain-on-a-two-week-clock)

生成摘要时出错

---

## 40. Jürgen Habermas, influential German philosopher, dies at 96

**原文标题**: Jürgen Habermas, influential German philosopher, dies at 96

**原文链接**: [https://apnews.com/article/juergen-habermas-dead-germany-2b541721af6cb19abfaa923359d091b5](https://apnews.com/article/juergen-habermas-dead-germany-2b541721af6cb19abfaa923359d091b5)

生成摘要时出错

---

## 41. The Forth Language [Byte Magazine Volume 05 Number 08]

**原文标题**: The Forth Language [Byte Magazine Volume 05 Number 08]

**原文链接**: [https://archive.org/details/byte-magazine-1980-08](https://archive.org/details/byte-magazine-1980-08)

生成摘要时出错

---

## 42. AEP (API Design Standard and Tooling Ecosystem)

**原文标题**: AEP (API Design Standard and Tooling Ecosystem)

**原文链接**: [https://aep.dev/](https://aep.dev/)

生成摘要时出错

---

## 43. Optimizing Content for Agents

**原文标题**: Optimizing Content for Agents

**原文链接**: [https://cra.mr/optimizing-content-for-agents/](https://cra.mr/optimizing-content-for-agents/)

生成摘要时出错

---

## 44. New 'negative light' technology hides data transfers in plain sight

**原文标题**: New 'negative light' technology hides data transfers in plain sight

**原文链接**: [https://www.unsw.edu.au/newsroom/news/2026/03/New-negative-light-technology-hides-data-transfers-in-plain-sight](https://www.unsw.edu.au/newsroom/news/2026/03/New-negative-light-technology-hides-data-transfers-in-plain-sight)

生成摘要时出错

---

## 45. Elon Musk pushes out more xAI founders as AI coding effort falters

**原文标题**: Elon Musk pushes out more xAI founders as AI coding effort falters

**原文链接**: [https://www.ft.com/content/e5fbc6c2-d5a6-4b97-a105-6a96ea849de5](https://www.ft.com/content/e5fbc6c2-d5a6-4b97-a105-6a96ea849de5)

生成摘要时出错

---

## 46. Using Thunderbird for RSS

**原文标题**: Using Thunderbird for RSS

**原文链接**: [https://rubenerd.com/using-thunderbird-for-rss/](https://rubenerd.com/using-thunderbird-for-rss/)

生成摘要时出错

---

## 47. HP has new incentive to stop blocking third-party ink in its printers

**原文标题**: HP has new incentive to stop blocking third-party ink in its printers

**原文链接**: [https://arstechnica.com/gadgets/2026/03/hp-has-new-incentive-to-stop-blocking-third-party-ink-in-its-printers/](https://arstechnica.com/gadgets/2026/03/hp-has-new-incentive-to-stop-blocking-third-party-ink-in-its-printers/)

生成摘要时出错

---

## 48. The most SHAMELESS structural manipulation of a index I've ever seen

**原文标题**: The most SHAMELESS structural manipulation of a index I've ever seen

**原文链接**: [https://substack.com/@georgenoble/note/c-226667679](https://substack.com/@georgenoble/note/c-226667679)

生成摘要时出错

---

## 49. Launch HN: Spine Swarm (YC S23) – AI agents that collaborate on a visual canvas

**原文标题**: Launch HN: Spine Swarm (YC S23) – AI agents that collaborate on a visual canvas

**原文链接**: [https://www.getspine.ai/](https://www.getspine.ai/)

生成摘要时出错

---

## 50. Temperatures expected to remain at or near record levels in coming five years

**原文标题**: Temperatures expected to remain at or near record levels in coming five years

**原文链接**: [https://www.metoffice.gov.uk/about-us/news-and-media/media-centre/weather-and-climate-news/2025/global-temperatures-expected-to-remain-at-or-near-record-levels](https://www.metoffice.gov.uk/about-us/news-and-media/media-centre/weather-and-climate-news/2025/global-temperatures-expected-to-remain-at-or-near-record-levels)

生成摘要时出错

---

## 51. Parsing semiconductor datasheets into structured register maps for under $0.25

**原文标题**: Parsing semiconductor datasheets into structured register maps for under $0.25

**原文链接**: [https://regforge.dev/blog/datasheet-parsing](https://regforge.dev/blog/datasheet-parsing)

生成摘要时出错

---

## 52. Show HN: Context Gateway – Compress agent context before it hits the LLM

**原文标题**: Show HN: Context Gateway – Compress agent context before it hits the LLM

**原文链接**: [https://github.com/Compresr-ai/Context-Gateway](https://github.com/Compresr-ai/Context-Gateway)

生成摘要时出错

---

## 53. Our Experience with I-Ready

**原文标题**: Our Experience with I-Ready

**原文链接**: [https://moultano.wordpress.com/2026/03/12/our-experience-with-i-ready/](https://moultano.wordpress.com/2026/03/12/our-experience-with-i-ready/)

生成摘要时出错

---

## 54. ArXiv is establishing itself as an independent nonprofit organization

**原文标题**: ArXiv is establishing itself as an independent nonprofit organization

**原文链接**: [https://jobs.chronicle.com/job/37961678/chief-executive-officer](https://jobs.chronicle.com/job/37961678/chief-executive-officer)

生成摘要时出错

---

## 55. Emacs and Vim in the Age of AI

**原文标题**: Emacs and Vim in the Age of AI

**原文链接**: [https://batsov.com/articles/2026/03/09/emacs-and-vim-in-the-age-of-ai/](https://batsov.com/articles/2026/03/09/emacs-and-vim-in-the-age-of-ai/)

生成摘要时出错

---

## 56. How Lego builds a new Lego set

**原文标题**: How Lego builds a new Lego set

**原文链接**: [https://www.theverge.com/c/23991049/lego-ideas-polaroid-onestep-behind-the-scenes-price](https://www.theverge.com/c/23991049/lego-ideas-polaroid-onestep-behind-the-scenes-price)

生成摘要时出错

---

## 57. The Browser Becomes Your WordPress

**原文标题**: The Browser Becomes Your WordPress

**原文链接**: [https://wordpress.org/news/2026/03/announcing-my-wordpress/](https://wordpress.org/news/2026/03/announcing-my-wordpress/)

生成摘要时出错

---

## 58. Gigabyte MZ33-AR1: A Unique AMD EPYC 9005 Motherboard for Open-Source Firmware

**原文标题**: Gigabyte MZ33-AR1: A Unique AMD EPYC 9005 Motherboard for Open-Source Firmware

**原文链接**: [https://www.phoronix.com/review/gigabyte-mz33-ar1](https://www.phoronix.com/review/gigabyte-mz33-ar1)

生成摘要时出错

---

## 59. The Wyden Siren Goes Off Again: We’ll Be “Stunned” By What the NSA Is Doing

**原文标题**: The Wyden Siren Goes Off Again: We’ll Be “Stunned” By What the NSA Is Doing

**原文链接**: [https://www.techdirt.com/2026/03/12/the-wyden-siren-goes-off-again-well-be-stunned-by-what-the-nsa-is-doing-under-section-702/](https://www.techdirt.com/2026/03/12/the-wyden-siren-goes-off-again-well-be-stunned-by-what-the-nsa-is-doing-under-section-702/)

生成摘要时出错

---

## 60. Parallels confirms MacBook Neo can run Windows in a virtual machine

**原文标题**: Parallels confirms MacBook Neo can run Windows in a virtual machine

**原文链接**: [https://www.macrumors.com/2026/03/13/macbook-neo-runs-windows-11-vm/](https://www.macrumors.com/2026/03/13/macbook-neo-runs-windows-11-vm/)

生成摘要时出错

---

## 61. TUI Studio – visual terminal UI design tool

**原文标题**: TUI Studio – visual terminal UI design tool

**原文链接**: [https://tui.studio/](https://tui.studio/)

生成摘要时出错

---

## 62. Launch HN: Captain (YC W26) – Automated RAG for Files

**原文标题**: Launch HN: Captain (YC W26) – Automated RAG for Files

**原文链接**: [https://www.runcaptain.com/](https://www.runcaptain.com/)

生成摘要时出错

---

## 63. Restoring the first recording of computer music (2018)

**原文标题**: Restoring the first recording of computer music (2018)

**原文链接**: [https://www.bl.uk/stories/blogs/posts/restoring-the-first-recording-of-computer-music](https://www.bl.uk/stories/blogs/posts/restoring-the-first-recording-of-computer-music)

生成摘要时出错

---

## 64. An old photo of a large BBS (2022)

**原文标题**: An old photo of a large BBS (2022)

**原文链接**: [https://rachelbythebay.com/w/2022/01/26/swcbbs/](https://rachelbythebay.com/w/2022/01/26/swcbbs/)

生成摘要时出错

---

## 65. John Carmack about open source and anti-AI activists

**原文标题**: John Carmack about open source and anti-AI activists

**原文链接**: [https://twitter.com/id_aa_carmack/status/2032460578669691171](https://twitter.com/id_aa_carmack/status/2032460578669691171)

生成摘要时出错

---

## 66. Arizona's Meteor Crater is still revealing new secrets 50k years later

**原文标题**: Arizona's Meteor Crater is still revealing new secrets 50k years later

**原文链接**: [https://www.space.com/stargazing/meteor-showers/arizonas-meteor-crater-is-still-revealing-new-secrets-50-000-years-later](https://www.space.com/stargazing/meteor-showers/arizonas-meteor-crater-is-still-revealing-new-secrets-50-000-years-later)

生成摘要时出错

---

## 67. Please Do Not A/B Test My Workflow

**原文标题**: Please Do Not A/B Test My Workflow

**原文链接**: [https://backnotprop.com/blog/do-not-ab-test-my-workflow/](https://backnotprop.com/blog/do-not-ab-test-my-workflow/)

生成摘要时出错

---

## 68. Your phone is an entire computer

**原文标题**: Your phone is an entire computer

**原文链接**: [https://medhir.com/blog/your-phone-is-an-entire-computer](https://medhir.com/blog/your-phone-is-an-entire-computer)

生成摘要时出错

---

## 69. Gvisor on Raspbian

**原文标题**: Gvisor on Raspbian

**原文链接**: [https://nubificus.co.uk/blog/gvisor-rpi5/](https://nubificus.co.uk/blog/gvisor-rpi5/)

生成摘要时出错

---

## 70. Malus – Clean Room as a Service

**原文标题**: Malus – Clean Room as a Service

**原文链接**: [https://malus.sh](https://malus.sh)

生成摘要时出错

---

## 71. Open-source, low-cost 10.5 GHz PLFM phased array RADAR system

**原文标题**: Open-source, low-cost 10.5 GHz PLFM phased array RADAR system

**原文链接**: [https://github.com/NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR)

生成摘要时出错

---

## 72. Lost Doctor Who episodes found

**原文标题**: Lost Doctor Who episodes found

**原文链接**: [https://www.bbc.co.uk/news/articles/c4g7kwq1k11o](https://www.bbc.co.uk/news/articles/c4g7kwq1k11o)

生成摘要时出错

---

## 73. E2E encrypted messaging on Instagram will no longer be supported after 8 May

**原文标题**: E2E encrypted messaging on Instagram will no longer be supported after 8 May

**原文链接**: [https://help.instagram.com/491565145294150](https://help.instagram.com/491565145294150)

生成摘要时出错

---

## 74. Stanford researchers report first recording of a blue whale's heart rate (2019)

**原文标题**: Stanford researchers report first recording of a blue whale's heart rate (2019)

**原文链接**: [https://news.stanford.edu/stories/2019/11/first-ever-recording-blue-whales-heart-rate](https://news.stanford.edu/stories/2019/11/first-ever-recording-blue-whales-heart-rate)

生成摘要时出错

---

## 75. Artificial intelligence-associated delusions and large language models

**原文标题**: Artificial intelligence-associated delusions and large language models

**原文链接**: [https://www.thelancet.com/journals/lanpsy/article/PIIS2215-0366(25)00396-7/abstract](https://www.thelancet.com/journals/lanpsy/article/PIIS2215-0366(25)00396-7/abstract)

生成摘要时出错

---

## 76. Direnv Is All You Need to Parallelize Agentic Programming with Git Worktrees

**原文标题**: Direnv Is All You Need to Parallelize Agentic Programming with Git Worktrees

**原文链接**: [https://waldencui.com/post/direnv_is_all_you_need_to_parallelize_claude_code_with_git_worktrees/](https://waldencui.com/post/direnv_is_all_you_need_to_parallelize_claude_code_with_git_worktrees/)

生成摘要时出错

---

## 77. AI didn't simplify software engineering: It just made bad engineering easier

**原文标题**: AI didn't simplify software engineering: It just made bad engineering easier

**原文链接**: [https://robenglander.com/writing/ai-did-not-simplify/](https://robenglander.com/writing/ai-did-not-simplify/)

生成摘要时出错

---

## 78. Space Exploration Logo Archive

**原文标题**: Space Exploration Logo Archive

**原文链接**: [https://spaceexplorationlogoarchive.webflow.io/](https://spaceexplorationlogoarchive.webflow.io/)

生成摘要时出错

---

## 79. JPEG Compression

**原文标题**: JPEG Compression

**原文链接**: [https://www.sophielwang.com/blog/jpeg](https://www.sophielwang.com/blog/jpeg)

生成摘要时出错

---

## 80. Confidential health records from UK BioBank project exposed online

**原文标题**: Confidential health records from UK BioBank project exposed online

**原文链接**: [https://www.theguardian.com/science/2026/mar/14/confidential-health-records-exposed-online-uk-biobank](https://www.theguardian.com/science/2026/mar/14/confidential-health-records-exposed-online-uk-biobank)

生成摘要时出错

---

## 81. The Silicon Hegemon

**原文标题**: The Silicon Hegemon

**原文链接**: [https://www.eetimes.com/the-silicon-hegemon/](https://www.eetimes.com/the-silicon-hegemon/)

生成摘要时出错

---

## 82. Grief and the AI split

**原文标题**: Grief and the AI split

**原文链接**: [https://blog.lmorchard.com/2026/03/11/grief-and-the-ai-split/](https://blog.lmorchard.com/2026/03/11/grief-and-the-ai-split/)

生成摘要时出错

---

## 83. Ceno, browse the web without internet access

**原文标题**: Ceno, browse the web without internet access

**原文链接**: [https://ceno.app/en/index.html?](https://ceno.app/en/index.html?)

生成摘要时出错

---

## 84. Are LLM merge rates not getting better?

**原文标题**: Are LLM merge rates not getting better?

**原文链接**: [https://entropicthoughts.com/no-swe-bench-improvement](https://entropicthoughts.com/no-swe-bench-improvement)

生成摘要时出错

---

## 85. Bucketsquatting is finally dead

**原文标题**: Bucketsquatting is finally dead

**原文链接**: [https://onecloudplease.com/blog/bucketsquatting-is-finally-dead](https://onecloudplease.com/blog/bucketsquatting-is-finally-dead)

生成摘要时出错

---

## 86. Source code of Swedish e-government services has been leaked

**原文标题**: Source code of Swedish e-government services has been leaked

**原文链接**: [https://darkwebinformer.com/full-source-code-of-swedens-e-government-platform-leaked-from-compromised-cgi-sverige-infrastructure/](https://darkwebinformer.com/full-source-code-of-swedens-e-government-platform-leaked-from-compromised-cgi-sverige-infrastructure/)

生成摘要时出错

---

## 87. Exploring JEPA for real-time speech translation

**原文标题**: Exploring JEPA for real-time speech translation

**原文链接**: [https://www.startpinch.com/research/en/jepa-encoder-translation/](https://www.startpinch.com/research/en/jepa-encoder-translation/)

生成摘要时出错

---

## 88. Show HN: What was the world listening to? Music charts, 20 countries (1940–2025)

**原文标题**: Show HN: What was the world listening to? Music charts, 20 countries (1940–2025)

**原文链接**: [https://88mph.fm/](https://88mph.fm/)

生成摘要时出错

---

## 89. Vite 8.0 Is Out

**原文标题**: Vite 8.0 Is Out

**原文链接**: [https://vite.dev/blog/announcing-vite8](https://vite.dev/blog/announcing-vite8)

生成摘要时出错

---

## 90. Bringing Chrome to ARM64 Linux Devices

**原文标题**: Bringing Chrome to ARM64 Linux Devices

**原文链接**: [https://blog.chromium.org/2026/03/bringing-chrome-to-arm64-linux-devices.html](https://blog.chromium.org/2026/03/bringing-chrome-to-arm64-linux-devices.html)

生成摘要时出错

---

## 91. Google Fiber will be sold to private equity firm and merge with cable company

**原文标题**: Google Fiber will be sold to private equity firm and merge with cable company

**原文链接**: [https://arstechnica.com/tech-policy/2026/03/google-fiber-will-be-sold-to-private-equity-firm-and-merge-with-cable-company/](https://arstechnica.com/tech-policy/2026/03/google-fiber-will-be-sold-to-private-equity-firm-and-merge-with-cable-company/)

生成摘要时出错

---

## 92. Iran-backed hackers claim wiper attack on medtech firm Stryker

**原文标题**: Iran-backed hackers claim wiper attack on medtech firm Stryker

**原文链接**: [https://krebsonsecurity.com/2026/03/iran-backed-hackers-claim-wiper-attack-on-medtech-firm-stryker/](https://krebsonsecurity.com/2026/03/iran-backed-hackers-claim-wiper-attack-on-medtech-firm-stryker/)

生成摘要时出错

---

## 93. What changes happen in the aging brain?

**原文标题**: What changes happen in the aging brain?

**原文链接**: [https://www.salk.edu/news-release/what-changes-happen-in-the-aging-brain/](https://www.salk.edu/news-release/what-changes-happen-in-the-aging-brain/)

生成摘要时出错

---

## 94. Runners who churn butter on their runs

**原文标题**: Runners who churn butter on their runs

**原文链接**: [https://www.runnersworld.com/news/a70683169/how-to-make-butter-while-running/](https://www.runnersworld.com/news/a70683169/how-to-make-butter-while-running/)

生成摘要时出错

---

## 95. $2B nonprofit grants traced to find who's behind age verification bills

**原文标题**: $2B nonprofit grants traced to find who's behind age verification bills

**原文链接**: [https://old.reddit.com/r/linux/comments/1rshc1f/i_traced_2_billion_in_nonprofit_grants_and_45/](https://old.reddit.com/r/linux/comments/1rshc1f/i_traced_2_billion_in_nonprofit_grants_and_45/)

生成摘要时出错

---

## 96. Long overlooked as crucial to life, fungi start to get their due

**原文标题**: Long overlooked as crucial to life, fungi start to get their due

**原文链接**: [https://e360.yale.edu/features/fungi-kingdom](https://e360.yale.edu/features/fungi-kingdom)

生成摘要时出错

---

## 97. OpenTelemetry for Rust Developers

**原文标题**: OpenTelemetry for Rust Developers

**原文链接**: [https://signoz.io/blog/opentelemetry-rust/](https://signoz.io/blog/opentelemetry-rust/)

生成摘要时出错

---

## 98. Militaries are scrambling to create their own Starlink

**原文标题**: Militaries are scrambling to create their own Starlink

**原文链接**: [https://www.newscientist.com/article/2517766-why-the-worlds-militaries-are-scrambling-to-create-their-own-starlink/](https://www.newscientist.com/article/2517766-why-the-worlds-militaries-are-scrambling-to-create-their-own-starlink/)

生成摘要时出错

---

## 99. Show HN: Axe – A 12MB binary that replaces your AI framework

**原文标题**: Show HN: Axe – A 12MB binary that replaces your AI framework

**原文链接**: [https://github.com/jrswab/axe](https://github.com/jrswab/axe)

生成摘要时出错

---

## 100. Show HN: SupplementDEX – The Evidence-Based Supplement Database

**原文标题**: Show HN: SupplementDEX – The Evidence-Based Supplement Database

**原文链接**: [https://supplementdex.com/](https://supplementdex.com/)

生成摘要时出错

---

