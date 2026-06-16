# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-06-16.md)

*最后自动更新时间: 2026-06-16 20:36:40*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 2 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 3 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 4 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 5 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 6 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 7 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 8 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 9 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 10 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 11 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 12 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 13 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 14 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 15 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 16 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 17 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 18 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 19 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 20 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 21 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 22 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 23 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 24 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 25 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 26 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 27 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 28 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 29 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 30 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 31 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 32 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 33 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 34 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 35 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 36 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 37 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 38 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 39 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 40 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 41 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 42 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 43 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 44 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 45 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 46 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 47 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 48 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 49 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 50 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 51 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 52 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 53 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 54 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 55 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 56 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 57 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 58 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 59 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 60 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 61 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 62 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 63 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 64 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 65 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 66 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 67 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 68 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 69 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 70 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 71 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 72 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 73 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 74 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 75 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 76 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 77 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 78 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 79 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 80 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 81 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 82 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 83 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 84 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 85 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 86 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 87 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 88 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 89 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 90 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 91 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 92 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 93 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 94 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 95 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 96 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 97 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 98 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 99 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 100 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 101 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 102 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 103 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 104 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 105 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 106 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 107 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 108 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 109 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 110 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 111 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 112 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 113 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 114 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 115 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 116 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 117 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 118 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 119 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 120 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 121 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 122 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 123 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 124 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 125 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 126 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 127 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 128 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 129 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 130 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 131 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 132 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 133 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 134 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 135 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 136 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 137 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 138 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 139 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 140 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 141 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 142 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 143 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 144 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 145 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 146 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 147 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 148 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 149 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 150 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 151 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 152 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 153 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 154 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 155 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 156 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 157 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 158 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 159 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 160 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 161 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 162 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 163 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 164 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 165 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 166 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 167 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 168 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 169 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 170 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 171 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 172 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 173 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 174 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 175 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 176 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 177 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 178 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 179 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 180 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 181 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 182 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 183 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 184 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 185 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 186 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 187 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 188 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 189 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 190 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 191 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 192 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 193 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 194 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 195 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 196 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 197 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 198 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 199 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 200 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 201 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 202 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 203 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 204 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 205 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 206 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 207 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 208 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 209 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 210 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 211 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 212 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 213 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 214 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 215 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 216 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 217 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 218 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 219 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 220 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 221 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 222 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 223 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 224 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 225 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 226 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 227 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 228 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 229 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 230 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 231 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 232 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 233 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 234 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 235 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 236 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 237 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 238 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 239 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 240 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 241 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 242 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 243 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 244 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 245 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 246 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 247 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 248 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 249 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 250 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 251 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 252 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 253 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 254 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 255 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 256 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 257 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 258 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 259 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 260 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 261 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 262 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 263 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 264 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 265 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 266 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 267 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 268 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 269 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 270 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 271 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 272 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 273 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 274 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 275 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 276 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 277 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 278 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 279 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 280 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 281 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 282 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 283 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 284 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 285 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 286 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 287 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 288 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 289 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 290 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 291 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 292 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 293 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 294 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 295 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 296 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 297 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 298 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 299 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 300 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 301 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 302 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 303 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 304 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 305 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 306 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 307 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 308 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 309 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 310 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 311 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 312 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 313 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 314 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 315 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 316 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 317 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 318 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 319 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 320 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 321 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 322 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 323 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 324 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 325 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 326 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 327 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 328 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 329 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 330 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 331 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 332 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 333 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 334 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 335 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 336 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 337 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 338 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 339 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 340 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 341 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 342 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 343 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 344 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 345 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 346 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 347 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 348 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 349 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 350 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 351 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 352 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 353 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 354 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 355 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 356 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 357 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 358 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 359 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 360 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 361 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 362 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 363 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 364 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 365 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 366 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 367 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 368 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 369 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 370 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 371 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 372 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 373 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 374 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 375 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 376 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 377 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 378 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 379 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 380 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 381 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 382 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 383 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 384 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 385 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 386 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 387 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 388 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 389 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 390 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 391 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 392 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 393 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 394 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 395 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 396 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 397 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 398 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 399 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 400 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 401 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 402 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 403 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 404 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 405 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 406 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 407 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 408 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 409 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 410 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 411 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 412 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 413 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 414 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 415 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 416 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 417 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 418 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 419 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 420 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 421 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 422 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 423 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 424 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 425 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 426 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 427 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 428 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 429 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 430 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 431 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 432 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 433 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 434 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 435 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 436 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 437 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 438 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 439 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 440 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 441 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 442 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 443 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 444 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 445 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 446 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 447 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 448 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 449 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 450 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 451 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 452 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 453 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
