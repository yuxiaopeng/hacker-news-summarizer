# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-01-17.md)

*最后自动更新时间: 2026-01-17 17:45:35*
## 1. ASCII字符不是像素：深入解析ASCII渲染

**原文标题**: ASCII characters are not pixels: a deep dive into ASCII rendering

**原文链接**: [https://alexharri.com/blog/ascii-rendering](https://alexharri.com/blog/ascii-rendering)

在《**ASCII 字符并非像素：深入探讨 ASCII 渲染**》一文中，作者探讨了为何传统的图像转 ASCII 转换效果通常显得模糊或有锯齿感，并提出了一种基于字符**形状**而非仅基于密度的优化方法。

普通 ASCII 渲染器的根本问题在于将字符视为像素，即将网格单元的平均亮度映射为字符的视觉密度。无论是使用简单的降采样还是超采样（抗锯齿），这种方法都忽略了字符内部的几何结构，导致形状边缘出现“锯齿”或缺乏清晰度。

为了获得更清晰的效果，作者通过以下流程引入了**基于形状的渲染**：

*   **量化形状**：作者不再使用单一的亮度值，而是利用“采样圆”（例如在单元格的上半部分和下半部分各设一个）为每个 ASCII 字符创建多维**形状向量**。该向量代表了字符密度最高的分布位置。
*   **归一化**：对这些向量进行归一化处理，以确保在检索过程中能够覆盖更广泛的字符选择。
*   **采样与匹配**：渲染图像时，系统通过测量局部亮度为每个网格单元计算出相应的“采样向量”，随后通过最近邻搜索，找到形状向量与图像几何结构最匹配的 ASCII 字符。

这种技术使字符能够遵循物体的实际轮廓（如圆形的弧线或立方体的边缘），从而显著提升了有效分辨率。作者还结合了**赛璐璐着色效果**来增强不同颜色区域之间的对比度。虽然这种基于二维（上/下）向量的方法大幅提升了质量，但作者也指出，它在处理中间密集或左右分布的字符细节时仍存在局限性。

---

## 2. 我们把 Claude Code 接入了《模拟过山车》

**原文标题**: We Put Claude Code in Rollercoaster Tycoon

**原文链接**: [https://labs.ramp.com/rct](https://labs.ramp.com/rct)

根据提供的标题和内容，以下是该项目的简要总结：

**总结：我们将 Claude Code 接入了《过山车大亨》**

该项目探索了将 Claude Code（Anthropic 开发的基于终端的智能体工具）集成到经典模拟经营游戏《过山车大亨》（很可能是通过 OpenRCT2 开源项目实现）的过程。

其核心目标是测试 AI 智能体在处理复杂的实时模拟环境时的能力。与遵循预设脚本的传统“游戏 AI”不同，Claude Code 作为一个自主智能体运行。它通过与游戏底层逻辑交互来建造游乐设施、管理公园财务，并响应虚拟游客的需求。

**核心亮点：**
*   **智能体化的问题解决**：该实验展示了 Claude 在沙盒环境中进行多步规划和迭代决策的能力。
*   **遗留系统交互**：它展示了现代基于大语言模型（LLM）的工具如何与遗留软件衔接，从而有效地解析数据并执行指令。
*   **创造性建设**：AI 不仅仅是在管理菜单，它还承担了设计和布置游乐设施及基础设施所需的空间推理任务。

该项目作为一次实践演示，展现了 AI 的进化——即从简单的文本生成器转变为能够操作复杂软件环境的功能性智能体。

---

## 3. 伊丽莎白时期府邸的保暖秘诀

**原文标题**: An Elizabethan mansion's secrets for staying warm

**原文链接**: [https://www.bbc.com/future/article/20260116-an-elizabethan-mansions-secrets-for-staying-warm](https://www.bbc.com/future/article/20260116-an-elizabethan-mansions-secrets-for-staying-warm)

在14至19世纪的极寒时期——小冰期——建筑师们开发出了创新的保暖方法。其中一个典型的例子是位于英格兰德比郡的哈德威克庄园（Hardwick Hall），由哈德威克的贝丝于16世纪90年代建造。虽然现代建筑通常依赖高耗能技术来调节温度，但哈德威克庄园采用了即便在今天仍具参考价值的“被动式”设计策略。

关键设计特征包括：
*   **建筑朝向：** 房屋沿南北轴线建造，以最大限度地获取阳光。居民们追随太阳的轨迹活动，早晨使用朝东的长廊，傍晚则使用西南方向的卧室。
*   **热蓄能：** 壁炉设置在厚达4.5英尺的巨大中心脊柱上。石材吸收壁炉产生的热量，并在数小时后将其辐射回房间。
*   **策略性窗户布局：** 尽管有俏皮话称该建筑“窗多于墙”，但北向窗户通常是“盲窗”（从内部封堵），以防止在没有太阳能收益的地方流失热量。
*   **室内保温：** 使用厚挂毯、床幔和多层衣物，为抵御穿堂风提供了额外保护。

这些方法使庄园内的温度能比室外高出多达10°C，表现显著优于同时期的其他房屋。

文章指出，现代建筑在很大程度上抛弃了这些原则，转而青睐需要大量能源进行采暖和制冷的“玻璃盒子”式摩天大楼。通过重新审视伊丽莎白时代的秘密——例如优先考虑建筑朝向和热蓄能——现代设计师可以减少对化石燃料的依赖。在较小的规模上，个人可以通过追随太阳路径或利用自然遮荫来提高房屋效率，这证明了过去是应对当今气候挑战的重要工具。

---

## 4. 八个欧洲国家因反对美国控制格陵兰岛而面临10%关税。

**原文标题**: Eight European countries face 10% tariff for opposing US control of Greenland

**原文链接**: [https://apnews.com/article/denmark-greenland-us-trump-4ad99ea3975a8b62d37bd04961feda55](https://apnews.com/article/denmark-greenland-us-trump-4ad99ea3975a8b62d37bd04961feda55)

唐纳德·特朗普总统宣布计划从2月开始对来自丹麦、挪威、瑞典、法国、德国、英国、荷兰和芬兰这八个欧洲国家的商品征收10%的关税。此举是针对这些国家反对美国获取格陵兰岛控制权的报复性措施。特朗普进一步威胁称，如果无法就“完全且彻底购买”该岛达成协议，到6月1日关税将上调至25%。

特朗普为此次收购辩解称，格陵兰岛对美国导弹防御系统至关重要，并指称俄罗斯和中国对该领土有所觊觎。然而，丹麦军方官员和美国参议员克里斯·库恩斯对此提出了质疑，指出并无证据表明存在此类威胁。

这一声明引发了北约内部的外交危机，使这一自1949年以来建立的盟友关系陷入紧张。虽然白宫并未排除武力夺取该领土的可能性，但丹麦少将索伦·安德森强调，丹麦并不预想会遭到北约盟国的攻击，但他指出丹麦法律要求士兵在受到攻击时必须予以反击。

针对这些威胁，数千名抗议者聚集在努克和哥本哈根，坚称格陵兰岛是自治领土且“非卖品”。与此同时，一个美国两党国会代表团访问了丹麦，以安抚盟友并试图缓和局势。尽管美国、丹麦和格陵兰官员近期举行了高层会晤，但各方分歧依然严重，欧洲领导人坚持认为，只有格陵兰和丹麦才能决定该岛的未来。

---

## 5. “Hello”一词的600年起源

**原文标题**: The 600-year-old origins of the word 'hello'

**原文链接**: [https://www.bbc.com/culture/article/20260113-hello-hiya-aloha-what-our-greetings-reveal](https://www.bbc.com/culture/article/20260113-hello-hiya-aloha-what-our-greetings-reveal)

本文探讨了“hello”一词600年来的演变历程，它已从最初的一种功能性呼喊转变为全球通用的社交必备语。尽管该词直到200年前（即1826年康涅狄格州的一份报纸）才首次出现在印刷品中，但其根源可以追溯到15世纪。

**起源与标准化**
从词源学角度看，“hello”可能演变自古高地德语的“halâ”（用于呼唤渡船夫）或法语的“holla”（意为“停止”）。几个世纪以来，“hullo”和“halloo”等变体一直被用作狩猎时的呼喊或引起注意的信号。该词作为问候语的统治地位随电话的发明而得以巩固；托马斯·爱迪生因其在通话线路中的清晰度而推崇“hello”，最终胜过了亚历山大·格拉汉姆·贝尔更偏好的“ahoy”。

**语言的细微差别**
语言学家指出，“hello”具有极强的可塑性。语调、元音长度以及拼写方式（如“heyyy”或“hi”）的变化，都能传达说话者的年龄、国籍、心情或调情意味。在英语之外，问候语也承载着文化身份。例如，某些语言的问候语旨在祝福健康（希腊语）或和平（希伯来语），而另一些语言则利用问候语来界定社会等级和亲疏关系。

**数字化转型**
在现代，科技正再次重塑我们相互问候的方式。通过短信和社交媒体实现的持续互联，导致正式问候语被“修剪”或省略，转而由表情符号和缩写形式所取代。

**结论**
尽管其表现形式不断更迭——从15世纪的呐喊演变为现代的挥手表情符号——“hello”的核心价值始终如一：宣告自身存在并寻求相互认可，这是人类的一种基本本能。

---

## 6. 地图海报——为您喜爱的城市创作艺术品

**原文标题**: Map To Poster – Create Art of your favourite city

**原文链接**: [https://github.com/originalankur/maptoposter](https://github.com/originalankur/maptoposter)

**Map To Poster** 是一款基于 Python 的实用工具，旨在为全球任何城市生成极简主义风格的艺术地图海报。该工具利用来自 OpenStreetMap 的地理数据（通过 OSMnx 库）和 Nominatim 的地理编码功能，将城市布局转化为高质量的 PNG 艺术作品。

**核心功能与用法**
该工具通过命令行界面 (CLI) 运行，允许用户通过指定城市、国家、主题和地图半径（距离）来自定义海报。它内置了一份“距离指南”，帮助用户选择合适的比例——范围涵盖从威尼斯等建筑密集区域的 4,000 米，到东京等大都市全景的 20,000 米。

**主题与自定义**
该项目内置了 17 种主题，包括：
*   **Noir (暗黑):** 高对比度黑白风格。
*   **Neon Cyberpunk (霓虹赛博朋克):** 电光粉与青色调。
*   **Japanese Ink (和风水墨):** 极简水墨美学。
*   **Warm Beige (暖米色):** 复古怀旧色调。

用户还可以通过简单的 JSON 格式定义背景、水体、公园及各类道路（高速公路、住宅区等）的颜色，从而创建自定义主题。

**技术架构**
其渲染流程遵循特定的层级结构：
1.  **数据获取：** 检索道路网络、水体和公园数据。
2.  **样式设置：** 根据 OpenStreetMap 标签应用层级化的道路宽度和颜色。
3.  **渲染：** 使用 Matplotlib 进行元素分层（背景 > 水体 > 公园 > 道路 > 渐变 > 排版）。
4.  **排版：** 利用归一化坐标自动添加城市名称、经纬坐标及装饰性元素。

对于开发者，“黑客指南 (Hacker’s Guide)”提供了扩展脚本的说明，例如添加铁路或建筑轮廓等新图层，并分享了通过缓存坐标来规避请求频率限制等性能优化建议。最终生成的海报将带有时间戳，便于管理归档。

---

## 7. 呆伯特的来世

**原文标题**: The Dilbert Afterlife

**原文链接**: [https://www.astralcodexten.com/p/the-dilbert-afterlife](https://www.astralcodexten.com/p/the-dilbert-afterlife)

在《呆伯特死后》（The Dilbert Afterlife）中，斯科特·亚历山大（Scott Alexander）反思了《呆伯特》创作者斯科特·亚当斯（Scott Adams）的职业生涯与心理驱动力（文章背景设定在亚当斯于2026年去世的虚构预言之后）。亚历山大认为，《呆伯特》之所以能成为一种文化现象，是因为它完美捕捉了“极客体验”：即在一个由无能且“尖头发”老板统治的企业世界里，作为唯一清醒、聪明的人所感到的挫败感。

文章探讨了亚当斯人生中的核心悖论：尽管身为“莫扎特级别”的漫画家，他却从未对这份成功感到满足。他受困于一种“极客潜意识”，认为智力理应是获取权力的工具，并因智力鲜能转化为权力而深感沮丧。为了证明自己不仅仅是个幽默作家，亚当斯曾发起数次失败的商业冒险，包括“呆伯特卷饼”（一种强化维生素的卷饼）和一家名为Stacey’s的餐厅。讽刺的是，在这些角色中，亚当斯往往变成了他讽刺了几十年的那种爱管闲事、低效无能的管理者。

亚历山大将亚当斯与埃隆·马斯克进行了类比，认为两人都体现了天赋与欲望之间的“心理错位”：亚当斯是一位极度渴望成为商业大亨的喜剧天才，而马斯克则是一位极度渴望成为喜剧天才的商业大亨。

文章总结道，亚当斯晚年向商业、技术和哲学领域（如其著作《上帝的残骸》）的转型，都是在试图“摇晃自身天赋的栅栏”。他洞察了“呆伯特法则”，却一生都在徒劳地尝试通过“破解”路径来通往另一种伟大。最终，亚历山大将亚当斯描绘成一个才华横溢却又躁动不安的人物，他永远无法调和自己在讽刺文学上的世界级天赋与对严肃智力认可的渴求。

---

## 8. ClickHouse acquires Langfuse

**原文标题**: ClickHouse acquires Langfuse

**原文链接**: [https://langfuse.com/blog/joining-clickhouse](https://langfuse.com/blog/joining-clickhouse)

生成摘要时出错

---

## 9. 东德气球逃亡

**原文标题**: East Germany balloon escape

**原文链接**: [https://en.wikipedia.org/wiki/East_Germany_balloon_escape](https://en.wikipedia.org/wiki/East_Germany_balloon_escape)

生成摘要时出错

---

## 10. Show HN: Streaming gigabyte medical images from S3 without downloading them

**原文标题**: Show HN: Streaming gigabyte medical images from S3 without downloading them

**原文链接**: [https://github.com/PABannier/WSIStreamer](https://github.com/PABannier/WSIStreamer)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 2 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 3 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 4 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 5 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 6 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 7 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 8 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 9 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 10 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 11 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 12 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 13 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 14 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 15 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 16 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 17 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 18 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 19 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 20 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 21 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 22 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 23 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 24 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 25 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 26 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 27 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 28 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 29 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 30 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 31 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 32 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 33 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 34 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 35 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 36 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 37 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 38 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 39 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 40 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 41 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 42 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 43 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 44 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 45 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 46 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 47 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 48 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 49 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 50 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 51 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 52 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 53 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 54 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 55 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 56 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 57 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 58 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 59 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 60 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 61 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 62 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 63 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 64 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 65 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 66 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 67 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 68 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 69 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 70 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 71 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 72 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 73 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 74 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 75 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 76 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 77 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 78 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 79 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 80 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 81 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 82 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 83 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 84 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 85 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 86 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 87 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 88 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 89 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 90 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 91 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 92 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 93 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 94 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 95 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 96 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 97 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 98 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 99 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 100 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 101 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 102 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 103 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 104 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 105 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 106 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 107 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 108 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 109 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 110 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 111 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 112 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 113 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 114 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 115 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 116 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 117 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 118 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 119 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 120 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 121 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 122 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 123 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 124 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 125 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 126 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 127 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 128 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 129 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 130 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 131 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 132 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 133 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 134 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 135 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 136 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 137 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 138 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 139 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 140 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 141 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 142 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 143 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 144 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 145 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 146 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 147 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 148 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 149 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 150 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 151 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 152 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 153 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 154 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 155 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 156 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 157 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 158 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 159 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 160 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 161 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 162 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 163 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 164 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 165 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 166 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 167 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 168 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 169 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 170 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 171 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 172 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 173 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 174 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 175 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 176 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 177 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 178 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 179 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 180 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 181 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 182 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 183 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 184 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 185 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 186 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 187 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 188 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 189 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 190 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 191 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 192 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 193 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 194 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 195 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 196 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 197 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 198 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 199 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 200 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 201 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 202 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 203 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 204 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 205 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 206 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 207 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 208 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 209 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 210 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 211 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 212 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 213 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 214 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 215 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 216 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 217 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 218 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 219 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 220 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 221 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 222 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 223 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 224 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 225 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 226 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 227 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 228 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 229 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 230 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 231 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 232 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 233 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 234 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 235 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 236 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 237 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 238 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 239 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 240 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 241 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 242 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 243 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 244 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 245 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 246 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 247 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 248 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 249 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 250 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 251 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 252 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 253 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 254 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 255 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 256 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 257 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 258 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 259 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 260 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 261 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 262 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 263 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 264 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 265 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 266 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 267 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 268 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 269 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 270 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 271 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 272 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 273 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 274 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 275 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 276 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 277 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 278 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 279 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 280 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 281 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 282 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 283 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 284 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 285 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 286 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 287 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 288 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 289 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 290 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 291 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 292 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 293 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 294 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 295 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 296 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 297 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 298 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 299 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 300 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 301 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 302 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 303 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
