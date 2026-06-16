# Hacker News 热门文章摘要 (2026-06-16)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 厄尔尼诺临近，美国撤回海洋传感器令加拿大科研界倍感“震惊”

**原文标题**: U.S. pulling ocean sensors a 'shock' for Canadian research as El Niño nears

**原文链接**: [https://www.timescolonist.com/local-news/us-pulling-ocean-sensors-a-shock-for-canadian-research-as-el-nino-nears-12422874](https://www.timescolonist.com/local-news/us-pulling-ocean-sensors-a-shock-for-canadian-research-as-el-nino-nears-12422874)

美国国家海洋和大气管理局（NOAA）已开始移除东北太平洋的一个关键海洋监测传感器网络，这一举动令加拿大科学界措手不及并深感担忧。

**背景**
几十年来，这些锚定浮标提供了有关不同深度海洋温度、盐度和洋流的“地面实况”数据。这些信息对于预测天气模式、海洋热浪（如“暖团”）以及太平洋鲑鱼种群的行为至关重要。

**时机**
此次拆除正值重大厄尔尼诺现象临近的危险时刻。维多利亚大学和加拿大海洋网络中心（ONC）的科学家认为，失去这些传感器会导致北太平洋出现巨大的数据缺口。虽然卫星技术可以监测海洋表面，但它无法提供这些浮标所捕捉的水柱垂直“剖面图”，而这对于了解深海储存了多少热量至关重要。

**对加拿大的影响**
不列颠哥伦比亚省尤其容易受到这些传感器所监测变化的影响。相关数据被用于预测从冬季积雪到沿海风暴强度的各种信息。加拿大研究人员对这一决定表示“震惊”，并指出尽管该数据具有跨界重要性，但美方并未与其协商。

**行动原因**
NOAA 将拆除传感器的主要原因归结为预算限制和基础设施老化。据报道，该机构正将重点转向其他技术和地区。然而，加拿大专家警告称，如果没有这个网络，准确预测气候变化和厄尔尼诺现象对区域影响的能力将大幅削弱，使沿海社区在应对极端环境转变时准备不足。

---

## 2. 现在运行本地模型体验已经很好了。

**原文标题**: Running local models is good now

**原文链接**: [https://vickiboykis.com/2026/06/15/running-local-models-is-good-now/](https://vickiboykis.com/2026/06/15/running-local-models-is-good-now/)

在《现在运行本地模型已经很不错了》一文中，作者探讨了本地大语言模型（LLM）如何从缓慢且不准确的工具演变为复杂软件开发的切实可行之选。在配备 64GB 内存的 2022 款 M2 Mac 上，作者指出随着 OpenAI OSS-20B 和 **Gemma 4** 系列等模型的发布，性能发生了显著转变。

作者认为，本地模型已经达到了一个“氛围”阈值（"vibe" threshold），即不再需要频繁通过云端 API 进行二次核对。利用 **Gemma-4-12b-qat** 和 **26b-a4b**，作者成功实现了“代理式编程”（agentic coding）——即由 AI 循环执行重构代码、编写单元测试和快速构建仓库等任务。目前，这些本地工作流的准确率和速度约为顶尖云端模型的 **75%**。

文中介绍的技术方案使用 **LM Studio** 作为推理服务器，并使用 **Pi** 作为代理框架。出于安全性考虑，作者在 **Docker 容器**中运行这些工作流，以防止代理执行未经授权的系统操作。这种环境允许对推理过程进行内省、自定义量化以及调整上下文窗口。

尽管作者承认仍存在一些障碍——如硬件限制的上下文窗口、较低的推理速度以及偶尔的生态系统“失配”——但其结论是，本地模型现在已成为云端 API 的强大、私密且可定制的替代方案。在本地执行复杂编程任务的能力较六个月前实现了巨大飞跃，这标志着本地大语言模型正成为开发者的一项重要投资。

---

## 3. 苹果即将让“隐藏邮件地址”功能变得毫无用处。

**原文标题**: Apple is about to make Hide My Email useless

**原文链接**: [https://arseniyshestakov.com/2026/06/16/apple-is-about-to-make-hide-my-email-useless/](https://arseniyshestakov.com/2026/06/16/apple-is-about-to-make-hide-my-email-useless/)

生成摘要时出错

---

## 4. SpaceX将以600亿美元收购Cursor

**原文标题**: SpaceX to buy Cursor for $60B

**原文链接**: [https://www.reuters.com/legal/transactional/spacex-buy-anysphere-60-billion-2026-06-16/](https://www.reuters.com/legal/transactional/spacex-buy-anysphere-60-billion-2026-06-16/)

无法访问文章链接。

---

## 5. TIL：无需 curl，利用 Bash /dev/tcp 即可发起 HTTP 请求

**原文标题**: TIL: You can make HTTP requests without curl using Bash /dev/TCP

**原文链接**: [https://mareksuppa.com/til/bash-dev-tcp-http-without-curl/](https://mareksuppa.com/til/bash-dev-tcp-http-without-curl/)

本文介绍如何仅使用 Bash 执行基础 HTTP 请求，这在调试缺少 `curl` 或 `wget` 等工具的极简 Docker 容器时特别有用。

**原理**
Bash 内部可以处理指向 `/dev/tcp/host/port` 的重定向。虽然这些并不是磁盘上的真实文件，但 Bash 会将其解析为打开网络套接字。通过使用命令 `exec 3<>/dev/tcp/service/port`，你可以在文件描述符 3 上打开一个双向套接字。随后，你可以使用 `printf` 向其写入原始 HTTP 请求，并使用 `cat <&3` 读取响应。

**关键技术细节**
*   **Connection: close：** 在请求中包含 `Connection: close` 请求头至关重要。如果没有它，服务器可能会保持连接开启，导致 `cat` 在等待更多数据时无限期挂起。
*   **格式化：** 请求必须手动使用 `\r\n` 换行符进行格式化，并在请求末尾包含一个空行。

**限制与要求**
*   **不支持 TLS：** 此方法仅支持原始 TCP 套接字。它适用于明文 HTTP，但无法处理 HTTPS。
*   **Bash 特有：** 这是 Bash 的功能，而非 POSIX 标准。它无法在 `sh`、`dash` 或 `zsh` 中运行。
*   **编译时选项：** 这要求 Bash 在构建时启用了 `--enable-net-redirections`。虽然这在大多数发行版中是标准配置，但某些极简系统可能会将其禁用。
*   **手动处理：** 它缺少真实客户端的健壮功能，例如处理重定向、重试或分块传输编码。

总之，虽然 `curl` 是日常任务的首选工具，但 Bash 的 `/dev/tcp` 功能是一个强大的“隐藏”特性，可用于在受限环境中进行快速连通性检查。

---

## 6. 《卡尔文与霍布斯》与正直的代价

**原文标题**: Calvin and Hobbes and the price of integrity

**原文链接**: [https://therepublicofletters.substack.com/p/calvin-and-hobbes-and-the-price-of](https://therepublicofletters.substack.com/p/calvin-and-hobbes-and-the-price-of)

《〈卡尔文与霍布斯〉与操守的代价》

在《〈卡尔文与霍布斯〉与操守的代价》一文中，作者探讨了比尔·沃特森拒绝将其标志性连环漫画商业化的传奇事迹。尽管同时代的《花生漫画》和《加菲猫》通过授权赚取了数十亿美元，但沃特森却因坚决抵制将“卡尔文与霍布斯”制成毛绒玩具、咖啡杯或动画特辑而闻名。

核心主题是沃特森坚信授权会使艺术作品“廉价化”。他认为商业化会产生利益冲突，导致角色不再受叙事或哲学的驱动，而是取决于其推销产品的能力。对沃特森而言，连环画是艺术家与读者共享的私人世界；引入周边商品会破坏这种亲密感，并淡化角色的个性。

这种对操守的坚持付出了巨大的经济代价。由于拒绝授权其创作，沃特森放弃了估计高达3亿至4亿美元的收入。他与所属的环球报业联合会进行了多年激烈的博弈，最终赢得了版权的完全控制权——这在行业内是一次罕见的胜利。

文章最终指出，正是沃特森所付出的“操守的代价”，才让《卡尔文与霍布斯》得以历久弥新。通过让漫画远离商业主义的干扰，沃特森确保了其长久的生命力并保留了情感共鸣。在1995年最后一期漫画出版数十年后，这部作品依然是纯粹的艺术表达，未受那些常令其他流行文化标志失色的庸俗化影响。沃特森留下的遗产，是一位艺术家选择创作纯粹而非巨额财富的深刻典范。

---

## 7. 机械表 (2022)

**原文标题**: Mechanical Watch (2022)

**原文链接**: [https://ciechanow.ski/mechanical-watch/](https://ciechanow.ski/mechanical-watch/)

《机械表》（2022）解释了机械表复杂的“机芯”原理，它利用物理学原理而非电池来记录时间。其机械结构由四个主要系统组成：

**1. 动力系统（发条）**
能量储存在一个被称为“发条”的螺旋扭力弹簧中，它被安置在“条盒”内。当手表上弦时，发条被卷紧。随着发条释放，它带动条盒转动，为设备运行提供所需的机械能。

**2. 传动轮系（齿轮）**
为了确保手表在秒针快速走动的同时能维持较长的运行时间（约40小时），一系列齿轮和齿轮轴被用来提升转速。这一“传动轮系”将条盒缓慢、高扭矩的转动，转化为指针计时所需的快速、低扭矩转动。

**3. 擒纵机构**
如果没有调节，发条的能量会瞬间释放殆尽。擒纵机构由“擒纵轮”和“擒纵叉”组成，起到了制动器的作用。擒纵叉利用低摩擦的人造红宝石，以受控的增量锁定和解锁擒纵轮，从而在“滴答”声中节奏性地释放能量。

**4. 摆轮系统**
手表的“心跳”是“摆轮”和“游丝”。该系统以精确的频率摆动，其频率由游丝的刚度和摆轮的转动惯量决定。当摆轮摆动时，圆盘钉撞击擒纵叉以解锁擒纵机构。与此同时，擒纵轮向摆轮回馈微小的动力，以维持其持续摆动。

这些组件共同构成了一个自我维持的循环：能量被储存、倍增，并以精准调节的速率释放，从而实现准确的时间计量。

---

## 8. But yak shaving is fun

**原文标题**: But yak shaving is fun

**原文链接**: [https://parksb.github.io/en/article/32.html](https://parksb.github.io/en/article/32.html)

“Yak shaving” refers to the process of performing a chain of increasingly unrelated tasks to achieve a single goal, often leading the person far from their original objective. Coined by Carlin Vieri at the MIT AI Lab and inspired by a bizarre episode of *The Ren & Stimpy Show*, the term describes the "scope creep" that occurs when one decides to build a solution from scratch rather than using off-the-shelf tools.

While project managers often view yak shaving as a waste of time and resources, the author argues that it is inherently fun and intellectually stimulating. For engineers, the process provides the joy of creation, the fascination of solving complex puzzles, and the opportunity for constant learning. 

The ultimate success story of yak shaving is Donald Knuth’s creation of TeX. What began as an attempt to typeset his own book series resulted in a ten-year detour during which Knuth invented a digital typesetting system, the WEB programming language, the "literate programming" paradigm, and the METAFONT language.

The article concludes that while professional projects require knowing when to stop to avoid failure, yak shaving is a remarkably effective educational tool. It forces a deep dive into the underlying layers of technology—from logic circuits to operating systems. Even if the original goal is never reached, the knowledge gained along the way makes the "shave" worthwhile. For those driven by curiosity, the journey through the rabbit hole is often more valuable than the destination.

---

## 9. GPT‑NL: a sovereign language model for the Netherlands

**原文标题**: GPT‑NL: a sovereign language model for the Netherlands

**原文链接**: [https://www.tno.nl/en/digital/artificial-intelligence/gpt-nl/](https://www.tno.nl/en/digital/artificial-intelligence/gpt-nl/)

生成摘要时出错

---

## 10. 10Gb/s Ethernet: switching to a Broadcom SFP+ module

**原文标题**: 10Gb/s Ethernet: switching to a Broadcom SFP+ module

**原文链接**: [https://www.gilesthomas.com/2026/06/10g-ethernet-switching-to-broadcom-sfp-plus](https://www.gilesthomas.com/2026/06/10g-ethernet-switching-to-broadcom-sfp-plus)

生成摘要时出错

---

## 11. Claude: Elevated errors across many models

**原文标题**: Claude: Elevated errors across many models

**原文链接**: [https://status.claude.com/incidents/xmhsglsz3h3w](https://status.claude.com/incidents/xmhsglsz3h3w)

生成摘要时出错

---

## 12. Apple's weird anti-nausea dots cured my car sickness

**原文标题**: Apple's weird anti-nausea dots cured my car sickness

**原文链接**: [https://www.theverge.com/tech/942854/apple-vehicle-motion-cues-review-really-work](https://www.theverge.com/tech/942854/apple-vehicle-motion-cues-review-really-work)

生成摘要时出错

---

## 13. Nobody clicks your share buttons

**原文标题**: Nobody clicks your share buttons

**原文链接**: [https://ankursethi.com/links/nobody-clicks-your-share-buttons/](https://ankursethi.com/links/nobody-clicks-your-share-buttons/)

生成摘要时出错

---

## 14. I admire Fabrice Bellard. He is almost certainly a better overall programmer

**原文标题**: I admire Fabrice Bellard. He is almost certainly a better overall programmer

**原文链接**: [https://twitter.com/ID_AA_Carmack/status/2064095424420487226](https://twitter.com/ID_AA_Carmack/status/2064095424420487226)

生成摘要时出错

---

## 15. Correlated randomness in Slay the Spire 2

**原文标题**: Correlated randomness in Slay the Spire 2

**原文链接**: [https://tck.mn/blog/correlated-randomness-sts2/](https://tck.mn/blog/correlated-randomness-sts2/)

生成摘要时出错

---

## 16. Making ast.walk 220x Faster

**原文标题**: Making ast.walk 220x Faster

**原文链接**: [https://reflex.dev/blog/why-ast-walk-when-you-can-ast-sprint/](https://reflex.dev/blog/why-ast-walk-when-you-can-ast-sprint/)

生成摘要时出错

---

## 17. The time the x86 emulator team found code so bad they fixed it during emulation

**原文标题**: The time the x86 emulator team found code so bad they fixed it during emulation

**原文链接**: [https://devblogs.microsoft.com/oldnewthing/20260615-00/?p=112419](https://devblogs.microsoft.com/oldnewthing/20260615-00/?p=112419)

生成摘要时出错

---

## 18. SubQ 1.1 Small

**原文标题**: SubQ 1.1 Small

**原文链接**: [https://subq.ai/subq-1-1-small-technical-report](https://subq.ai/subq-1-1-small-technical-report)

生成摘要时出错

---

## 19. Formal Methods and the Future of Programming

**原文标题**: Formal Methods and the Future of Programming

**原文链接**: [https://blog.janestreet.com/formal-methods-at-jane-street-index/](https://blog.janestreet.com/formal-methods-at-jane-street-index/)

生成摘要时出错

---

## 20. Qwen-Robot Suite: A Foundation Model Suite for Physical World Intelligence

**原文标题**: Qwen-Robot Suite: A Foundation Model Suite for Physical World Intelligence

**原文链接**: [https://qwen.ai/blog?id=qwen-robotsuite](https://qwen.ai/blog?id=qwen-robotsuite)

生成摘要时出错

---

## 21. Stop Using JWTs

**原文标题**: Stop Using JWTs

**原文链接**: [https://gist.github.com/samsch/0d1f3d3b4745d778f78b230cf6061452](https://gist.github.com/samsch/0d1f3d3b4745d778f78b230cf6061452)

生成摘要时出错

---

## 22. Specs Augmented Reality Glasses

**原文标题**: Specs Augmented Reality Glasses

**原文链接**: [https://newsroom.snap.com/introducing-specs-augmented-reality-glasses](https://newsroom.snap.com/introducing-specs-augmented-reality-glasses)

生成摘要时出错

---

## 23. An interview with an Apple emoji designer

**原文标题**: An interview with an Apple emoji designer

**原文链接**: [https://shadycharacters.co.uk/2026/06/ollie-wagner/](https://shadycharacters.co.uk/2026/06/ollie-wagner/)

生成摘要时出错

---

## 24. Show HN: Pen and paper resource development game with an emergent world

**原文标题**: Show HN: Pen and paper resource development game with an emergent world

**原文链接**: [https://www.jameshylands.co.uk/2026/06/sortis-paper-empire-game.html](https://www.jameshylands.co.uk/2026/06/sortis-paper-empire-game.html)

生成摘要时出错

---

## 25. Why is Meta destroying its engineering organization?

**原文标题**: Why is Meta destroying its engineering organization?

**原文链接**: [https://newsletter.pragmaticengineer.com/p/why-is-meta-destroying-its-engineering](https://newsletter.pragmaticengineer.com/p/why-is-meta-destroying-its-engineering)

生成摘要时出错

---

## 26. 'Ghost jobs' could soon be illegal in New York

**原文标题**: 'Ghost jobs' could soon be illegal in New York

**原文链接**: [https://www.fastcompany.com/91558427/ghost-jobs-could-soon-be-illegal-in-new-york](https://www.fastcompany.com/91558427/ghost-jobs-could-soon-be-illegal-in-new-york)

生成摘要时出错

---

## 27. Getting Creative with Perlin Noise Fields

**原文标题**: Getting Creative with Perlin Noise Fields

**原文链接**: [https://sighack.com/post/getting-creative-with-perlin-noise-fields](https://sighack.com/post/getting-creative-with-perlin-noise-fields)

生成摘要时出错

---

## 28. Show HN: Sabela – A Reactive Notebook for Haskell

**原文标题**: Show HN: Sabela – A Reactive Notebook for Haskell

**原文链接**: [https://sabela.datahaskell.com/](https://sabela.datahaskell.com/)

生成摘要时出错

---

## 29. Unicorn – The Ultimate CPU Emulator

**原文标题**: Unicorn – The Ultimate CPU Emulator

**原文链接**: [https://www.unicorn-engine.org/](https://www.unicorn-engine.org/)

生成摘要时出错

---

## 30. Cooling at the Speed of Light

**原文标题**: Cooling at the Speed of Light

**原文链接**: [https://cacm.acm.org/news/cooling-at-the-speed-of-light/](https://cacm.acm.org/news/cooling-at-the-speed-of-light/)

生成摘要时出错

---

## 31. Show HN: Azure DevOps TUI Management Style

**原文标题**: Show HN: Azure DevOps TUI Management Style

**原文链接**: [https://github.com/elpulgo/azdo](https://github.com/elpulgo/azdo)

生成摘要时出错

---

## 32. The Manhoff Archives: Color photos of Stalin-era USSR taken by a US diplomat

**原文标题**: The Manhoff Archives: Color photos of Stalin-era USSR taken by a US diplomat

**原文链接**: [https://www.rferl.org/a/the-manhoff-archive/28359558.html](https://www.rferl.org/a/the-manhoff-archive/28359558.html)

生成摘要时出错

---

## 33. I hacked into the worst e-bike and fixed it [video]

**原文标题**: I hacked into the worst e-bike and fixed it [video]

**原文链接**: [https://www.youtube.com/watch?v=hPrtVGimBYs](https://www.youtube.com/watch?v=hPrtVGimBYs)

生成摘要时出错

---

## 34. Feds freaked over Fable 5 after 'fix this code', not jailbreak, say researchers

**原文标题**: Feds freaked over Fable 5 after 'fix this code', not jailbreak, say researchers

**原文链接**: [https://www.theregister.com/security/2026/06/15/feds-freaked-over-fable-5-after-simple-fix-this-code-prompt-not-jailbreak-says-researcher/5255827](https://www.theregister.com/security/2026/06/15/feds-freaked-over-fable-5-after-simple-fix-this-code-prompt-not-jailbreak-says-researcher/5255827)

生成摘要时出错

---

## 35. A backdoor in a LinkedIn job offer

**原文标题**: A backdoor in a LinkedIn job offer

**原文链接**: [https://roman.pt/posts/linkedin-backdoor/](https://roman.pt/posts/linkedin-backdoor/)

生成摘要时出错

---

## 36. Making espresso with ultrasound

**原文标题**: Making espresso with ultrasound

**原文链接**: [https://www.unsw.edu.au/newsroom/news/2026/06/New-way-making-espresso](https://www.unsw.edu.au/newsroom/news/2026/06/New-way-making-espresso)

生成摘要时出错

---

## 37. Understanding the rationale behind a rule when trying to circumvent it

**原文标题**: Understanding the rationale behind a rule when trying to circumvent it

**原文链接**: [https://devblogs.microsoft.com/oldnewthing/20260611-00/?p=112415](https://devblogs.microsoft.com/oldnewthing/20260611-00/?p=112415)

生成摘要时出错

---

## 38. Nearly a million passports and photo IDs were unprotected on the public internet

**原文标题**: Nearly a million passports and photo IDs were unprotected on the public internet

**原文链接**: [https://www.theverge.com/tech/947157/passports-data-breach-cannabis-club-systems-nefos-puffpal](https://www.theverge.com/tech/947157/passports-data-breach-cannabis-club-systems-nefos-puffpal)

生成摘要时出错

---

## 39. Flip TABLE: storing arbitrary data in iNaturalist

**原文标题**: Flip TABLE: storing arbitrary data in iNaturalist

**原文链接**: [https://exclav.es/2026/06/13/flip-table-storing-arbitrary-data-in-inaturalist/](https://exclav.es/2026/06/13/flip-table-storing-arbitrary-data-in-inaturalist/)

生成摘要时出错

---

## 40. After AI Takes Everything

**原文标题**: After AI Takes Everything

**原文链接**: [https://ursb.me/en/posts/after-ai-takes-everything/](https://ursb.me/en/posts/after-ai-takes-everything/)

生成摘要时出错

---

## 41. I Love the Computer

**原文标题**: I Love the Computer

**原文链接**: [https://michaelenger.com/blog/i-love-the-computer/](https://michaelenger.com/blog/i-love-the-computer/)

生成摘要时出错

---

## 42. Users cry foul after AMD stripped memory crypto from its consumer CPUs

**原文标题**: Users cry foul after AMD stripped memory crypto from its consumer CPUs

**原文链接**: [https://arstechnica.com/security/2026/06/users-cry-foul-after-amd-stripped-memory-crypto-from-its-consumer-cpus/](https://arstechnica.com/security/2026/06/users-cry-foul-after-amd-stripped-memory-crypto-from-its-consumer-cpus/)

生成摘要时出错

---

## 43. Reservations are open for XREAL AURA

**原文标题**: Reservations are open for XREAL AURA

**原文链接**: [https://www.xreal.com/aura](https://www.xreal.com/aura)

生成摘要时出错

---

## 44. AI is potentially a Dunning-Kruger effect amplifier

**原文标题**: AI is potentially a Dunning-Kruger effect amplifier

**原文链接**: [https://twitter.com/i/status/2066825204207091926](https://twitter.com/i/status/2066825204207091926)

生成摘要时出错

---

## 45. GateGPT: 56k tokens per second Transformer (KV cache) on FPGA at 80 MHz

**原文标题**: GateGPT: 56k tokens per second Transformer (KV cache) on FPGA at 80 MHz

**原文链接**: [https://twitter.com/fguzmanai/status/2065832668172845209](https://twitter.com/fguzmanai/status/2065832668172845209)

生成摘要时出错

---

## 46. The Web We Know Is Going to Disappear

**原文标题**: The Web We Know Is Going to Disappear

**原文链接**: [https://www.minid.net/2026/6/15/the-web-is-going-to-dissapear](https://www.minid.net/2026/6/15/the-web-is-going-to-dissapear)

生成摘要时出错

---

## 47. KDE Plasma 6.7 Released

**原文标题**: KDE Plasma 6.7 Released

**原文链接**: [https://lwn.net/Articles/1078160/](https://lwn.net/Articles/1078160/)

生成摘要时出错

---

## 48. Trinket.io shutting down, so we saved it and hosted it a trinket.strivemath.org

**原文标题**: Trinket.io shutting down, so we saved it and hosted it a trinket.strivemath.org

**原文链接**: [https://trinket.strivemath.org/](https://trinket.strivemath.org/)

生成摘要时出错

---

## 49. The octopus architecture for AI agents

**原文标题**: The octopus architecture for AI agents

**原文链接**: [https://blog.goodman.dev/blog/octopus-agent-architecture/](https://blog.goodman.dev/blog/octopus-agent-architecture/)

生成摘要时出错

---

## 50. Peopleless economy? Not technically impossible

**原文标题**: Peopleless economy? Not technically impossible

**原文链接**: [https://gmalandrakis.com/writings/ad-economicum.html](https://gmalandrakis.com/writings/ad-economicum.html)

生成摘要时出错

---

## 51. Iroh 1.0

**原文标题**: Iroh 1.0

**原文链接**: [https://www.iroh.computer/blog/v1](https://www.iroh.computer/blog/v1)

生成摘要时出错

---

## 52. The history of butterfly swimming

**原文标题**: The history of butterfly swimming

**原文链接**: [https://www.swimming.org/sport/history-of-butterfly/](https://www.swimming.org/sport/history-of-butterfly/)

生成摘要时出错

---

## 53. Why I email complete strangers

**原文标题**: Why I email complete strangers

**原文链接**: [https://www.goodinternetmagazine.com/why-i-email-complete-strangers/](https://www.goodinternetmagazine.com/why-i-email-complete-strangers/)

生成摘要时出错

---

## 54. SpaceX to acquire Cursor for $60B in stock, days after blockbuster IPO

**原文标题**: SpaceX to acquire Cursor for $60B in stock, days after blockbuster IPO

**原文链接**: [https://techcrunch.com/2026/06/16/spacex-to-acquire-cursor-for-60b-in-stock-days-after-blockbuster-ipo/](https://techcrunch.com/2026/06/16/spacex-to-acquire-cursor-for-60b-in-stock-days-after-blockbuster-ipo/)

生成摘要时出错

---

## 55. What job interviews taught me about Kubernetes

**原文标题**: What job interviews taught me about Kubernetes

**原文链接**: [https://notnotp.com/notes/what-job-interviews-taught-me-about-kubernetes/](https://notnotp.com/notes/what-job-interviews-taught-me-about-kubernetes/)

生成摘要时出错

---

## 56. Google Chrome update will close the door on ad blockers

**原文标题**: Google Chrome update will close the door on ad blockers

**原文链接**: [https://9to5google.com/2026/06/15/google-chromes-next-update-will-mark-the-end-of-popular-ad-blockers/](https://9to5google.com/2026/06/15/google-chromes-next-update-will-mark-the-end-of-popular-ad-blockers/)

生成摘要时出错

---

## 57. Banned book library in a wi-fi smart light bulb

**原文标题**: Banned book library in a wi-fi smart light bulb

**原文链接**: [https://www.richardosgood.com/posts/banned-book-library/](https://www.richardosgood.com/posts/banned-book-library/)

生成摘要时出错

---

## 58. TinyWind: A pixel pirate sailing game with real wind physics (380k+ kms sailed)

**原文标题**: TinyWind: A pixel pirate sailing game with real wind physics (380k+ kms sailed)

**原文链接**: [https://tinywind.io](https://tinywind.io)

生成摘要时出错

---

## 59. Humanity isn't ready for the coming intelligence explosion

**原文标题**: Humanity isn't ready for the coming intelligence explosion

**原文链接**: [https://www.economist.com/by-invitation/2026/06/15/humanity-isnt-ready-for-the-coming-intelligence-explosion](https://www.economist.com/by-invitation/2026/06/15/humanity-isnt-ready-for-the-coming-intelligence-explosion)

生成摘要时出错

---

## 60. Cohere's First Model for Developers

**原文标题**: Cohere's First Model for Developers

**原文链接**: [https://cohere.com/blog/north-mini-code](https://cohere.com/blog/north-mini-code)

生成摘要时出错

---

## 61. Dalus (YC W25) Is Hiring a Senior Software Engineer in Germany

**原文标题**: Dalus (YC W25) Is Hiring a Senior Software Engineer in Germany

**原文链接**: [https://www.ycombinator.com/companies/dalus/jobs/5IDmKJt-senior-software-frontend-engineer-germany-office](https://www.ycombinator.com/companies/dalus/jobs/5IDmKJt-senior-software-frontend-engineer-germany-office)

生成摘要时出错

---

## 62. How TimescaleDB compresses time-series data

**原文标题**: How TimescaleDB compresses time-series data

**原文链接**: [https://roszigit.com/en/blog/timescaledb-compression-hypercore](https://roszigit.com/en/blog/timescaledb-compression-hypercore)

生成摘要时出错

---

## 63. Game Engine White Papers: Commander Keen

**原文标题**: Game Engine White Papers: Commander Keen

**原文链接**: [https://forgottenbytes.net/commander_keen.html](https://forgottenbytes.net/commander_keen.html)

生成摘要时出错

---

## 64. Claude Corps

**原文标题**: Claude Corps

**原文链接**: [https://www.anthropic.com/news/claude-corps](https://www.anthropic.com/news/claude-corps)

生成摘要时出错

---

## 65. What every coder should know about gamma (2016)

**原文标题**: What every coder should know about gamma (2016)

**原文链接**: [https://blog.johnnovak.net/2016/09/21/what-every-coder-should-know-about-gamma/](https://blog.johnnovak.net/2016/09/21/what-every-coder-should-know-about-gamma/)

生成摘要时出错

---

## 66. 'Wow, it really worked ': 70s TV show causing worldwide panic today

**原文标题**: 'Wow, it really worked ': 70s TV show causing worldwide panic today

**原文链接**: [https://www.theguardian.com/tv-and-radio/2026/jun/16/alternative-3-mockumentary-missing-scientists-conspiracy-50-years-later](https://www.theguardian.com/tv-and-radio/2026/jun/16/alternative-3-mockumentary-missing-scientists-conspiracy-50-years-later)

生成摘要时出错

---

## 67. Swish – Jupyter-like computational notebook for SWI-Prolog

**原文标题**: Swish – Jupyter-like computational notebook for SWI-Prolog

**原文链接**: [https://swish.swi-prolog.org/](https://swish.swi-prolog.org/)

生成摘要时出错

---

## 68. Show HN: Fata – Spaced repetition to fight skill rot from AI coding

**原文标题**: Show HN: Fata – Spaced repetition to fight skill rot from AI coding

**原文链接**: [https://fata.dev](https://fata.dev)

生成摘要时出错

---

## 69. A 1969 camera operators' strike created Upstairs Downstairs multiverse

**原文标题**: A 1969 camera operators' strike created Upstairs Downstairs multiverse

**原文链接**: [https://ironicsans.ghost.io/the-color-strike/](https://ironicsans.ghost.io/the-color-strike/)

生成摘要时出错

---

## 70. How we run Firecracker VMs inside EC2 and start browsers in <1s

**原文标题**: How we run Firecracker VMs inside EC2 and start browsers in <1s

**原文链接**: [https://browser-use.com/posts/firecracker-browser-infra](https://browser-use.com/posts/firecracker-browser-infra)

生成摘要时出错

---

## 71. Making glass-to-metal seals for home­made vacuum tubes

**原文标题**: Making glass-to-metal seals for home­made vacuum tubes

**原文链接**: [https://maurycyz.com/projects/glass/1/](https://maurycyz.com/projects/glass/1/)

生成摘要时出错

---

## 72. Show HN: Veterinarian turned founder, AI lawn diagnosis

**原文标题**: Show HN: Veterinarian turned founder, AI lawn diagnosis

**原文链接**: [https://grassdx.com/](https://grassdx.com/)

生成摘要时出错

---

## 73. Openrouter Fusion API

**原文标题**: Openrouter Fusion API

**原文链接**: [https://openrouter.ai/openrouter/fusion](https://openrouter.ai/openrouter/fusion)

生成摘要时出错

---

## 74. Hetzner Price Adjustment

**原文标题**: Hetzner Price Adjustment

**原文链接**: [https://docs.hetzner.com/general/infrastructure-and-availability/price-adjustment/#cloud-servers](https://docs.hetzner.com/general/infrastructure-and-availability/price-adjustment/#cloud-servers)

生成摘要时出错

---

## 75. British Colombia, Time Zones, and Postgres

**原文标题**: British Colombia, Time Zones, and Postgres

**原文链接**: [https://www.crunchydata.com/blog/british-columbia-and-time-zone-changes](https://www.crunchydata.com/blog/british-columbia-and-time-zone-changes)

生成摘要时出错

---

## 76. Boot Naked Linux

**原文标题**: Boot Naked Linux

**原文链接**: [https://nick.zoic.org/art/boot-naked-linux/](https://nick.zoic.org/art/boot-naked-linux/)

生成摘要时出错

---

## 77. US battery manufacturing output continues to break records

**原文标题**: US battery manufacturing output continues to break records

**原文链接**: [https://fred.stlouisfed.org/series/IPG33591S](https://fred.stlouisfed.org/series/IPG33591S)

生成摘要时出错

---

## 78. How memory safety CVEs differ between Rust and C/C++

**原文标题**: How memory safety CVEs differ between Rust and C/C++

**原文链接**: [https://kobzol.github.io/rust/2026/06/15/how-memory-safety-cves-differ-between-rust-and-c-cpp.html](https://kobzol.github.io/rust/2026/06/15/how-memory-safety-cves-differ-between-rust-and-c-cpp.html)

生成摘要时出错

---

## 79. Commodore announces Linux-based flip phone with 'no social media, no browser'

**原文标题**: Commodore announces Linux-based flip phone with 'no social media, no browser'

**原文链接**: [https://www.tomshardware.com/phones/commodore-announces-linux-based-flip-phone-with-no-social-media-no-browser-the-callback-8020-will-be-available-in-five-retro-colorways-starting-at-usd499-runs-99-percent-of-android-apps](https://www.tomshardware.com/phones/commodore-announces-linux-based-flip-phone-with-no-social-media-no-browser-the-callback-8020-will-be-available-in-five-retro-colorways-starting-at-usd499-runs-99-percent-of-android-apps)

生成摘要时出错

---

## 80. Teenagers Stayed Overnight at Their School and Found Hidden Ancient Roman Ruins

**原文标题**: Teenagers Stayed Overnight at Their School and Found Hidden Ancient Roman Ruins

**原文链接**: [https://www.smithsonianmag.com/smart-news/these-italian-teenagers-stayed-overnight-at-their-school-they-found-ancient-roman-ruins-hidden-in-the-basement-180988917/](https://www.smithsonianmag.com/smart-news/these-italian-teenagers-stayed-overnight-at-their-school-they-found-ancient-roman-ruins-hidden-in-the-basement-180988917/)

生成摘要时出错

---

## 81. CJEU: Social networks are the 'publishers' of algorithmically-altered feeds

**原文标题**: CJEU: Social networks are the 'publishers' of algorithmically-altered feeds

**原文链接**: [https://bsky.app/profile/stevepeers.bsky.social/post/3mofdspytds2l](https://bsky.app/profile/stevepeers.bsky.social/post/3mofdspytds2l)

生成摘要时出错

---

## 82. Factoring "short-sleeve" RSA keys with polynomials

**原文标题**: Factoring "short-sleeve" RSA keys with polynomials

**原文链接**: [https://blog.trailofbits.com/2026/06/12/factoring-short-sleeve-rsa-keys-with-polynomials/](https://blog.trailofbits.com/2026/06/12/factoring-short-sleeve-rsa-keys-with-polynomials/)

生成摘要时出错

---

## 83. The 90-year-old idea behind JEPA models: Canonical Correlation Analysis

**原文标题**: The 90-year-old idea behind JEPA models: Canonical Correlation Analysis

**原文链接**: [https://shonczinner.github.io/posts/embedding-prediction/](https://shonczinner.github.io/posts/embedding-prediction/)

生成摘要时出错

---

## 84. My Homelab AI Dev Platform

**原文标题**: My Homelab AI Dev Platform

**原文链接**: [https://rsgm.dev/post/ai-dev-platform/](https://rsgm.dev/post/ai-dev-platform/)

生成摘要时出错

---

## 85. Improvement in advanced Alzheimer’s disease following high-dose psilocybin

**原文标题**: Improvement in advanced Alzheimer’s disease following high-dose psilocybin

**原文链接**: [https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2026.1813281/full](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2026.1813281/full)

生成摘要时出错

---

## 86. Fox to buy Roku

**原文标题**: Fox to buy Roku

**原文链接**: [https://www.wsj.com/business/deals/fox-roku-deal-f6e564f9](https://www.wsj.com/business/deals/fox-roku-deal-f6e564f9)

生成摘要时出错

---

## 87. Has AI already killed self-help nonfiction books?

**原文标题**: Has AI already killed self-help nonfiction books?

**原文链接**: [https://tim.blog/2026/06/12/has-ai-already-killed-nonfiction/](https://tim.blog/2026/06/12/has-ai-already-killed-nonfiction/)

生成摘要时出错

---

## 88. An O(x)Caml book that runs

**原文标题**: An O(x)Caml book that runs

**原文链接**: [https://kcsrk.info/ocaml/oxcaml/teaching/nptel/llm/2026/06/13/an-oxcaml-book-that-runs/](https://kcsrk.info/ocaml/oxcaml/teaching/nptel/llm/2026/06/13/an-oxcaml-book-that-runs/)

生成摘要时出错

---

## 89. An O(x)Caml book that runs

**原文标题**: An O(x)Caml book that runs

**原文链接**: [https://kcsrk.info/ocaml/oxcaml/teaching/nptel/llm/2026/06/13/an-oxcaml-book-that-runs/](https://kcsrk.info/ocaml/oxcaml/teaching/nptel/llm/2026/06/13/an-oxcaml-book-that-runs/)

生成摘要时出错

---

## 90. Europe Wants Digital Sovereignty. 2,165 Polish Organisations Show the Gap

**原文标题**: Europe Wants Digital Sovereignty. 2,165 Polish Organisations Show the Gap

**原文链接**: [https://ciphercue.com/blog/polish-cdn-email-traffic-american-companies-2026](https://ciphercue.com/blog/polish-cdn-email-traffic-american-companies-2026)

生成摘要时出错

---

## 91. Your ePub Is fine

**原文标题**: Your ePub Is fine

**原文链接**: [https://andreklein.net/your-epub-is-fine-kobo-disagrees-blame-adobe/](https://andreklein.net/your-epub-is-fine-kobo-disagrees-blame-adobe/)

生成摘要时出错

---

## 92. Copper transport drug restores memory and clears toxic Alzheimer's proteins

**原文标题**: Copper transport drug restores memory and clears toxic Alzheimer's proteins

**原文链接**: [https://www.monash.edu/news/articles/copper-drug-restores-memory-and-clears-toxic-alzheimers-proteins](https://www.monash.edu/news/articles/copper-drug-restores-memory-and-clears-toxic-alzheimers-proteins)

生成摘要时出错

---

## 93. SpaceX Set to Overtake Amazon in Value as It Soars for Third Day

**原文标题**: SpaceX Set to Overtake Amazon in Value as It Soars for Third Day

**原文链接**: [https://www.bloomberg.com/news/articles/2026-06-16/spacex-spcx-stock-set-for-more-than-50-jump-in-just-three-sessions](https://www.bloomberg.com/news/articles/2026-06-16/spacex-spcx-stock-set-for-more-than-50-jump-in-just-three-sessions)

生成摘要时出错

---

## 94. Hans Schulz – The father of the VEF Minox lens?

**原文标题**: Hans Schulz – The father of the VEF Minox lens?

**原文链接**: [https://moments-of-now.com/hans-schulz-the-father-of-the-vef-minox-riga-lens/](https://moments-of-now.com/hans-schulz-the-father-of-the-vef-minox-riga-lens/)

生成摘要时出错

---

## 95. Ported my C game to WASM, here's every bug that I hit

**原文标题**: Ported my C game to WASM, here's every bug that I hit

**原文链接**: [http://ernesernesto.github.io/writes/portingmatchmorphosistowasm/](http://ernesernesto.github.io/writes/portingmatchmorphosistowasm/)

生成摘要时出错

---

## 96. Linux kernel 7.1 sends Intel 486 support to silicon heaven

**原文标题**: Linux kernel 7.1 sends Intel 486 support to silicon heaven

**原文链接**: [https://www.theregister.com/os-platforms/2026/06/16/linux-kernel-71-sends-intel-486-support-to-silicon-heaven/5256260](https://www.theregister.com/os-platforms/2026/06/16/linux-kernel-71-sends-intel-486-support-to-silicon-heaven/5256260)

生成摘要时出错

---

## 97. Earth's underground fungal network would span 10% of the Milky Way

**原文标题**: Earth's underground fungal network would span 10% of the Milky Way

**原文链接**: [https://www.livescience.com/planet-earth/plants/earths-underground-fungal-network-is-so-massive-it-would-span-10-percent-of-the-milky-way-map-reveals](https://www.livescience.com/planet-earth/plants/earths-underground-fungal-network-is-so-massive-it-would-span-10-percent-of-the-milky-way-map-reveals)

生成摘要时出错

---

## 98. Can Europe train a frontier AI model on the compute it owns?

**原文标题**: Can Europe train a frontier AI model on the compute it owns?

**原文链接**: [https://github.com/sammysltd/euromesh](https://github.com/sammysltd/euromesh)

生成摘要时出错

---

## 99. Show HN: machine0 – Persistent NixOS VMs You Control from the CLI

**原文标题**: Show HN: machine0 – Persistent NixOS VMs You Control from the CLI

**原文链接**: [https://machine0.io](https://machine0.io)

生成摘要时出错

---

## 100. Show HN: SharkClean MCP

**原文标题**: Show HN: SharkClean MCP

**原文链接**: [https://github.com/a-funk/sharkclean-mcp](https://github.com/a-funk/sharkclean-mcp)

生成摘要时出错

---

