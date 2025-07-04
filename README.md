# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-07-04.md)

*最后自动更新时间: 2025-07-04 17:47:30*
## 1. 迷你NAS将NVMe与英特尔高效芯片相结合

**原文标题**: Mini NASes marry NVMe to Intel's efficient chip

**原文链接**: [https://www.jeffgeerling.com/blog/2025/mini-nases-marry-nvme-intels-efficient-chip](https://www.jeffgeerling.com/blog/2025/mini-nases-marry-nvme-intels-efficient-chip)

本文评测了三款迷你NAS设备——GMKtec G9、Aiffro K100和Beelink ME mini，它们都采用英特尔N100/N150芯片和NVMe固态硬盘存储，面向缩减存储需求的用户。作者不再采用大型数据囤积方案，只需要6TB的可用空间，并寻求紧凑的解决方案。

这三款NAS都具有相似之处：英特尔N100/N150、2.5 Gbps网络（GMKtec和Beelink为双口）以及多个M.2 NVMe插槽。然而，每个产品都有不足之处。

GMKtec G9是预算型选择，但最初版本存在散热问题，新版本已解决（未经测试）。Aiffro K100体积小、效率高且散热良好，但缺少eMMC和WiFi，且只有一个2.5 Gbps端口。Beelink ME mini安静，并具有6个NVMe插槽（但多数为x1带宽）、内置eMMC和内置电源，但运行温度略高。

在性能方面，这三款设备都达到约250 MB/秒的读/写速度，尽管Beelink的带宽分配导致了一些速度下降。K100由于其平衡的功耗曲线以及缺少WiFi和eMMC等功能，因此是最节能的。

作者总结说，没有完美的选择。G9经济实惠，K100紧凑高效，Beelink则提供更多扩展性。如果能负担得起NVMe固态硬盘，作者倾向于选择K100，以实现6 TB的RAIDZ1设置。

---

## 2. 我为什么离开科技行业去研究慢性疼痛

**原文标题**: Why I left my tech job to work on chronic pain

**原文链接**: [https://sailhealth.substack.com/p/why-i-left-my-tech-job-to-work-on](https://sailhealth.substack.com/p/why-i-left-my-tech-job-to-work-on)

无法访问文章链接。

---

## 3. 曼哈顿里程碑：一对郊狼已定居中央公园

**原文标题**: In a Milestone for Manhattan, a Pair of Coyotes Has Made Central Park Their Home

**原文链接**: [https://www.smithsonianmag.com/science-nature/in-a-milestone-for-manhattan-a-pair-of-coyotes-has-made-central-park-their-home-180986892/](https://www.smithsonianmag.com/science-nature/in-a-milestone-for-manhattan-a-pair-of-coyotes-has-made-central-park-their-home-180986892/)

在纽约市一项引人注目的发展中，一对名为罗密欧和朱丽叶的郊狼已在中央公园安家落户。郊狼在曼哈顿的出现是一个相对较新的现象，罗密欧于2019年抵达，朱丽叶随后加入。野生动物专家认为，它们很可能是通过火车轨道从布朗克斯区迁徙而来。

这篇文章记录了戴维·雷和杰奎琳·埃默里的观察，他们一直在记录郊狼的行为，包括交配仪式和狩猎。它还突出了纽约市对城市野生动物不断变化的看法。虽然早期的郊狼目击事件导致了捕获和搬迁，但该市现在通过诸如WildlifeNYC之类的举措来促进共存。

郊狼在公园的生态系统中发挥着关键作用，有助于控制啮齿动物和鹅的数量。然而，一些居民对安全表示担忧，尽管尚未有中央公园的郊狼伤害人或宠物的报告。

作者们希望罗密欧和朱丽叶能在公园里成功繁殖，这对该物种来说是一个重要的里程碑。尽管观察到交配行为，但这对郊狼尚未产下幼崽，可能是由于干扰或不育。专家强调，公园游客需要通过保持距离和拴好狗来尊重野生动物。这个故事强调了郊狼的适应性和韧性，以及在城市环境中培养人类与野生动物之间积极关系的重要性。

---

## 4. Kepler.gl

**原文标题**: Kepler.gl

**原文链接**: [https://kepler.gl/](https://kepler.gl/)

本文重点在于Kepler.gl，很可能意在引起对它的关注或引用，暗示其可能与读者相关。在缺乏更多背景信息的情况下，本文主要作为Kepler.gl软件或平台本身的指引。鉴于标题和内容的性质，本文更像是进一步探索该主题的标题或参考点。

---

## 5. Show HN: 我用AI写了个塔防游戏，并记录了整个过程

**原文标题**: Show HN: I AI-coded a tower defense game and documented the whole process

**原文链接**: [https://github.com/maciej-trebacz/tower-of-time-game](https://github.com/maciej-trebacz/tower-of-time-game)

Show HN：AI辅助开发的穿越时空塔防游戏“时间之塔”

---

## 6. 压缩字典传输

**原文标题**: Compression Dictionary Transport

**原文链接**: [https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Compression_dictionary_transport](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Compression_dictionary_transport)

压缩字典传输是一种实验性的HTTP优化技术，它利用共享的压缩字典来显著减少传输资源的大小。它建立在Brotli和Zstandard等现有压缩算法的基础上，允许开发者提供针对特定资源定制的自定义字典。

与仅依赖于内置字典或单个资源内的冗余不同，此方法允许压缩算法引用自定义字典中的常用字符串，从而减小文件大小。这对于跨版本具有相似内容的资源（如JavaScript库）尤其有用。例如，可以使用`my-library.v1.js`作为字典来压缩`my-library.v2.js`，仅发送版本之间的差异。

服务器使用`Use-As-Dictionary`标头指示资源可以用作字典。客户端通过`Accept-Encoding`和`Available-Dictionary`标头分别表明它们使用字典的能力并提供其SHA-256哈希值。然后，服务器响应字典压缩的内容，并在`Content-Encoding`标头中指定压缩算法（Brotli为`dcb`，ZStandard为`dcz`）。`Vary`标头对于缓存至关重要。或者，可以通过带有`rel="compression-dictionary"`的`<link>`标签或`Link`标头提供字典。

安全限制包括字典和资源的同源策略、CORS要求以及HTTP缓存分区。尽管存在这些限制，与标准方法相比，压缩字典传输提供了显著的压缩改进，尤其是在具有共享内容的资源方面。

---

## 7. UpCodes (YC S17) 正在招聘运营负责人，以实现建筑合规自动化。

**原文标题**: UpCodes (YC S17) is hiring a Head of Ops to automate construction compliance

**原文链接**: [https://up.codes/careers?utm_source=HN](https://up.codes/careers?utm_source=HN)

UpCodes (Y Combinator S17孵化公司) 招聘运营主管。UpCodes的核心使命是实现建筑合规自动化。这意味着他们可能正在开发软件或平台，以帮助建筑专业人士理解并遵守建筑规范和规章。运营主管的职责很可能是简化流程、优化效率，并确保公司平稳运营，尤其是在实现建筑合规自动化目标方面。

由于仅提供了职位名称和招聘页面的第一部分，因此无法获得有关所需技能、职责或公司文化的更具体细节。但是，我们可以推断出该职位需要运营方面的经验，最好是在建筑或合规领域的科技驱动型公司工作过。

---

## 8. 无尽的任务

**原文标题**: EverQuest

**原文链接**: [https://www.filfre.net/2025/07/everquest/](https://www.filfre.net/2025/07/everquest/)

本文探讨了《无尽的任务》(EverQuest)的起源，强调了它作为一款成功的MMORPG，从其前身《网络创世纪》(Ultima Online)的错误中吸取了教训。虽然《网络创世纪》开创了这一类型，但《无尽的任务》利用其竞争对手的失误，取得了主流成功。

文章详细介绍了索尼互动专注于体育游戏的制作人约翰·斯梅德利(John Smedley)如何设想一款在线《龙与地下城》风格的游戏。斯梅德利说服了他的老板资助该项目，这促使他发现了布拉德·麦奎德(Brad McQuaid)和史蒂夫·克洛弗(Steve Clover)，这两位程序员正在开发一款单人CRPG。受到开源MUD工具包DikuMUD的启发，并亲眼目睹了《子午线59》(Meridian 59)的开发，麦奎德和克洛弗为《无尽的任务》创建了一份详细的设计文档。

与《网络创世纪》的社会学实验方法不同，《无尽的任务》优先考虑乐趣和可访问性。这款游戏被设计成一个游戏化的虚拟世界，玩家可以在其中与朋友们一起享受直接甚至愚蠢的冒险。这种设计理念，结合沉浸式的3D图形和对简化战斗的关注，使《无尽的任务》从其同时代游戏中脱颖而出，并为其广泛流行做出了贡献。罗西·科斯格罗夫(Rosie Cosgrove)的美术指导进一步增强了游戏的视觉吸引力，选择了异想天开的美学而非照片写实主义。

---

## 9. 拉里 (猫)

**原文标题**: Larry (cat)

**原文链接**: [https://en.wikipedia.org/wiki/Larry_(cat)](https://en.wikipedia.org/wiki/Larry_(cat))

拉里：唐宁街10号首席捕鼠官

---

## 10. 我们不是在创新，只是遗忘得更慢。

**原文标题**: We're Not Innovating, We're Just Forgetting Slower

**原文链接**: [https://www.elektormagazine.com/articles/opinion-no-innovation-forgetting-slower](https://www.elektormagazine.com/articles/opinion-no-innovation-forgetting-slower)

布莱恩·特里斯特姆·威廉姆斯认为，现代“创新”往往只是用新品牌重新发现旧概念，导致系统不可靠且复杂，用户既不理解也无法维修。他将他用了41年的TI-99/4A家用电脑的简单和可靠性，与现代“智能”设备（例如他的Google Nest Wi-Fi路由器）令人沮丧的复杂性进行了对比。

威廉姆斯批评了在硬件和软件中分层抽象的趋势，这导致了电子垃圾，并使调试成为噩梦。他还抨击了人工智能炒作机器，声称令人屏息的报道将统计上的改进误认为是真正的意识。

他进一步批评“创客运动”优先考虑美学而不是真正的工程理解和技能。文章总结说，我们正在培养一代工程师，他们可以使用工具而不了解其基本原理，从而导致技术上的习得性无助。

威廉姆斯呼吁回归强调基础知识、理论和原则的教育和技术写作，而不仅仅是最新的工具和功能。他提倡简单、可靠和易于理解的工程解决方案，这些解决方案优先考虑寿命而不是不断更新和数据收集。他强调，真正的创新在于理解我们已经知道的东西并在此基础上有效地构建。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 2 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 3 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 4 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 5 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 6 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 7 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 8 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 9 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 10 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 11 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 12 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 13 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 14 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 15 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 16 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 17 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 18 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 19 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 20 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 21 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 22 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 23 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 24 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 25 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 26 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 27 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 28 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 29 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 30 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 31 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 32 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 33 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 34 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 35 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 36 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 37 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 38 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 39 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 40 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 41 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 42 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 43 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 44 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 45 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 46 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 47 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 48 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 49 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 50 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 51 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 52 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 53 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 54 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 55 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 56 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 57 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 58 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 59 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 60 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 61 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 62 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 63 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 64 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 65 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 66 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 67 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 68 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 69 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 70 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 71 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 72 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 73 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 74 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 75 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 76 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 77 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 78 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 79 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 80 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 81 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 82 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 83 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 84 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 85 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 86 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 87 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 88 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 89 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 90 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 91 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 92 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 93 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 94 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 95 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 96 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 97 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 98 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 99 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 100 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 101 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 102 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 103 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 104 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 105 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 106 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 107 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
