# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-03-14.md)

*最后自动更新时间: 2026-03-14 17:57:08*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 2 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 3 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 4 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 5 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 6 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 7 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 8 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 9 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 10 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 11 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 12 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 13 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 14 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 15 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 16 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 17 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 18 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 19 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 20 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 21 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 22 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 23 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 24 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 25 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 26 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 27 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 28 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 29 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 30 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 31 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 32 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 33 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 34 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 35 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 36 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 37 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 38 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 39 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 40 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 41 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 42 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 43 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 44 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 45 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 46 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 47 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 48 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 49 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 50 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 51 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 52 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 53 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 54 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 55 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 56 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 57 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 58 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 59 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 60 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 61 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 62 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 63 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 64 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 65 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 66 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 67 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 68 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 69 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 70 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 71 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 72 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 73 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 74 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 75 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 76 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 77 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 78 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 79 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 80 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 81 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 82 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 83 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 84 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 85 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 86 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 87 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 88 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 89 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 90 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 91 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 92 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 93 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 94 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 95 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 96 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 97 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 98 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 99 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 100 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 101 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 102 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 103 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 104 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 105 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 106 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 107 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 108 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 109 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 110 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 111 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 112 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 113 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 114 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 115 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 116 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 117 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 118 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 119 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 120 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 121 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 122 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 123 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 124 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 125 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 126 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 127 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 128 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 129 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 130 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 131 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 132 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 133 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 134 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 135 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 136 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 137 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 138 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 139 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 140 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 141 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 142 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 143 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 144 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 145 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 146 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 147 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 148 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 149 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 150 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 151 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 152 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 153 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 154 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 155 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 156 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 157 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 158 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 159 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 160 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 161 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 162 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 163 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 164 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 165 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 166 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 167 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 168 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 169 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 170 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 171 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 172 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 173 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 174 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 175 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 176 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 177 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 178 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 179 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 180 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 181 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 182 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 183 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 184 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 185 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 186 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 187 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 188 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 189 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 190 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 191 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 192 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 193 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 194 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 195 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 196 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 197 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 198 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 199 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 200 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 201 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 202 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 203 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 204 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 205 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 206 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 207 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 208 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 209 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 210 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 211 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 212 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 213 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 214 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 215 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 216 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 217 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 218 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 219 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 220 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 221 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 222 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 223 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 224 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 225 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 226 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 227 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 228 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 229 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 230 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 231 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 232 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 233 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 234 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 235 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 236 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 237 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 238 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 239 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 240 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 241 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 242 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 243 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 244 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 245 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 246 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 247 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 248 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 249 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 250 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 251 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 252 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 253 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 254 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 255 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 256 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 257 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 258 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 259 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 260 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 261 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 262 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 263 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 264 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 265 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 266 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 267 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 268 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 269 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 270 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 271 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 272 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 273 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 274 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 275 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 276 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 277 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 278 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 279 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 280 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 281 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 282 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 283 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 284 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 285 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 286 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 287 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 288 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 289 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 290 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 291 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 292 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 293 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 294 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 295 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 296 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 297 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 298 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 299 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 300 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 301 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 302 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 303 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 304 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 305 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 306 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 307 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 308 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 309 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 310 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 311 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 312 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 313 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 314 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 315 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 316 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 317 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 318 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 319 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 320 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 321 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 322 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 323 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 324 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 325 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 326 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 327 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 328 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 329 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 330 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 331 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 332 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 333 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 334 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 335 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 336 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 337 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 338 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 339 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 340 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 341 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 342 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 343 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 344 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 345 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 346 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 347 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 348 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 349 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 350 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 351 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 352 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 353 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 354 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 355 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 356 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 357 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 358 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 359 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
