# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-09-20.md)

*最后自动更新时间: 2026-09-20 19:41:28*
## 1. 三星预计将其 HBM4 和 HBM4E DRAM 的产量提高一倍以上。

**原文标题**: Samsung is expected to more than double output of its HBM4 and HBM4E DRAM

**原文链接**: [https://en.sedaily.com/finance/2026/09/20/samsung-to-double-hbm4-output-next-year-sources-say](https://en.sedaily.com/finance/2026/09/20/samsung-to-double-hbm4-output-next-year-sources-say)

三星电子计划在明年将其第六代 (HBM4) 和第七代 (HBM4E) 高带宽内存芯片的产量提高一倍以上。这一扩张体现在该公司的计划中，即将其每月玻璃载板清洗量增加 2.5 倍——从今年的 2 万片增加到 2025 年的 5 万片。玻璃载板是在堆叠过程中用于稳定和减薄晶圆的关键部件，对于 12 层及更高规格的 HBM 配置至关重要。

产能提升的核心要点包括：

*   **生产重心转移：** 尽管 HBM 晶圆总投入量预计将增长 40%（达到每月 25 万片），但先进 HBM4 系列的出货占比预计将从今年的 40% 跃升至明年的 80%。
*   **产品里程碑：** 三星于 2 月份开始量产出货 HBM4，并于 5 月份向包括英伟达在内的主要客户提供了 12 层 HBM4E 样品。
*   **技术重点：** HBM4 产品线采用了 10 纳米级第六代 (1c) DRAM，以及基于 4 纳米工艺构建的基础底片 (base die)。

行业分析人士认为，玻璃载板需求的显著增加表明，这些高价值、高堆叠产品的产量将至少翻倍。这一战略凸显了三星致力于优先发展高性能 AI 内存，以满足全球激增的需求。

---

## 2. ChatGPT 现可通过广告收集器获悉你在其他网站上的行为

**原文标题**: ChatGPT now knows what you do on other websites via ad collector

**原文链接**: [https://www.buchodi.com/chatgpt-now-knows-what-you-do-on-other-websites-via-ad-collector/](https://www.buchodi.com/chatgpt-now-knows-what-you-do-on-other-websites-via-ad-collector/)

OpenAI has implemented a cross-site tracking mechanism that links users' ChatGPT accounts to their activity on external websites. According to a technical investigation, OpenAI uses an ad collector (`bzr.openai.com`) to set a persistent cookie named `__obi`. This cookie, tied to either a specific ChatGPT account or a stable anonymous device ID, is configured to be sent during cross-site requests.

When a user visits a website that has installed OpenAI’s tracking pixel (similar to Meta or Google pixels), the browser automatically transmits the `__obi` cookie to OpenAI. This allows the company to associate off-site behaviors—such as product searches, article views, and purchases—directly with a user’s ChatGPT identity. The tracking script also scrapes data from form fields and tag managers, collecting hashed emails, phone numbers, and cleartext location data.

**Key findings include:**
*   **Consent Bypass:** OpenAI classifies `__obi` as an "analytics" cookie. Consequently, users who opt out of marketing tracking but accept analytics are still monitored.
*   **Persistent Tracking:** The tracking remains active for logged-out users via a stable anonymous identifier that persists for weeks.
*   **Data Reach:** The mechanism was verified across numerous major retailers (e.g., Wayfair, Chewy, Eventbrite). While Safari and iOS browsers block the cookie due to privacy protections, it remains functional on Chrome for Android.
*   **Sensitive Information:** The collector was observed capturing URLs related to medical conditions, debt solutions, and legal forms.

The report notes that while this "standard adtech" behavior is common for social media giants, it is unprecedented for AI platforms. Because users often share highly personal information with AI that they would not post publicly, linking that profile to broad web-browsing habits creates significant new privacy risks.

---

## 3. Pirate Face Rescues LLM Models from Deletion

**原文标题**: Pirate Face Rescues LLM Models from Deletion

**原文链接**: [https://pirateface.co/](https://pirateface.co/)

生成摘要出错

---

## 4. Qwen 图像 2.1

**原文标题**: Qwen Image 2.1

**原文链接**: [https://qwen.ai/blog?id=qwen-image-2.1](https://qwen.ai/blog?id=qwen-image-2.1)

**Qwen Image 2.1 概要**

Qwen Image 2.1 代表了阿里巴巴云多模态 AI 系列的最新演进，专门旨在填补视觉感知与语言理解之间的鸿沟。作为一款尖端的视觉语言模型，它显著增强了 AI 解释视觉数据以及与之交互的能力。

**关键信息与特性：**

*   **先进的视觉理解：** 该模型在复杂图像识别、精细物体定位以及高精度光学字符识别（OCR）方面表现卓越，能够从密集的文档和标识中提取文本。
*   **动态分辨率支持：** 与将图像调整为固定正方形的传统模型不同，Qwen 2.1 支持各种长宽比和分辨率的图像，确保在处理过程中保留微小细节。
*   **视频分析：** 该模型具备处理视频帧序列的能力，使其能够总结视频内容、追踪时间变化，并回答有关随时间推移而发生的事件的问题。
*   **卓越的多语言能力：** 依托 Qwen 语言基座的强大优势，该模型支持多种语言，成为面向全球多元用户群体的通用工具。
*   **复杂推理：** 除了简单的识别，2.1 版本还展现了更强的逻辑推理能力。它可以解析图表、解决以视觉形式呈现的数学问题，并对现实场景提供细腻的描述。

综上所述，Qwen Image 2.1 是一款功能全面、性能卓越的多模态模型，为需要复杂视觉推理和文档处理能力的开发者提供了一个强大的开源权重解决方案。

---

## 5. 新加坡国家图书馆管理局推出微支付奖励以培养阅读习惯

**原文标题**: Singapore’s National Library Board offers micropayments to build reading habits

**原文链接**: [https://www.gadgetreview.com/singapore-is-paying-people-to-put-down-their-phones-and-read-books](https://www.gadgetreview.com/singapore-is-paying-people-to-put-down-their-phones-and-read-books)

Singapore’s National Library Board (NLB) has launched **ReadSG**, a five-year pilot program designed to cultivate daily reading habits through gamification and micropayments. Launched in September 2026, the initiative targets a "phone-first" population by offering financial incentives to encourage people to put down their devices and pick up books.

**How the Program Works:**
*   **Individual Rewards:** Participants log at least 15 minutes of reading daily via the CrowdTaskSG platform to earn 20 virtual coins.
*   **Payout:** The rewards are deliberately modest, intended as a "behavioral nudge" rather than a side hustle. With 1,000 coins equaling S$1, a participant must read for 50 days to earn one Singapore dollar.
*   **Communal Goals:** A parallel track called "Read for Good" aims for a collective 7.5 million reading minutes. Reaching this milestone unlocks a S$150,000 charitable donation.

**Context and Significance:**
The program builds on a decade of literacy initiatives, including the 2016 National Reading Movement. By using mechanics similar to fitness apps—such as closing rings or earning points—the NLB hopes to compete with the addictive nature of social media feeds. 

While critics suggest the financial reward is too small to change the behavior of non-readers, supporters point to behavioral economics research suggesting that low-friction, trivial incentives can effectively establish new habits. Governments and educators worldwide are monitoring ReadSG as a case study to determine if gamification and micropayments can successfully shift public behavior and improve literacy at a national scale.

---

## 6. 最奇特字母 W 的必要历史

**原文标题**: A Necessary History of the Oddest Letter: W

**原文链接**: [https://lithub.com/a-necessary-history-of-the-oddest-letter-w/](https://lithub.com/a-necessary-history-of-the-oddest-letter-w/)

在《最奇特字母“W”的必要历史》中，丹尼·贝特（Danny Bate）追溯了字母“W”从罗马帝国衰落至今的语言演化过程。这一字母的出现是为了填补语音上的空白：拉丁字母中缺乏一个能代表 /w/ 音的字符，而这一发音在罗马继承者的日耳曼语言中十分常见。为了弥补这一缺陷，6世纪法兰克的抄写员开始双写“U”（*UU*），并最终在11世纪将其融合成单个字符“W”。

在英格兰，“W”早期曾面临卢恩文字 *wynn* (ƿ) 的竞争。然而，在诺曼征服之后，受法语和拉丁语拼写的影响，“W”成为了标准。该字母的历史也解释了英语中若干奇特的拼写现象。例如，中世纪的抄写员在 *wolf* 和 *wonder* 等单词中用“o”代替“u”，以避免手稿中因“三连 U”笔画而产生的视觉混淆。此外，“W”还作为大元音推移中元音变化的标记（如 *town*），并偶尔取代古英语中的“G”（使 *fugol* 演变为 *fowl*）。

最后，贝特强调了“W”在语音上“顽皮”的影响。由于该音是通过圆唇发出的，它往往会使其后的元音发生“圆唇化”并移位。这解释了为什么 *was* 与 *has* 不同韵，而 *wand* 与 *hand* 也不押韵。这种语音漂移是相对晚近的发展；贝特指出，晚至莎士比亚和拜伦时期的诗人仍在使用诸如 *was* 与 *glass* 押韵的用法，这表明当时“W-圆唇化”尚未成为标准。最终，“W”作为语言迁徙中的独特幸存者，成功保留了一个在许多其他印欧语言中已经消失的发音。

---

## 7. Sherline Tools 即将结业

**原文标题**: Sherline Tools Is Going Out of Business

**原文链接**: [https://toolguyd.com/sherline-tools-shutting-down-usa-production/](https://toolguyd.com/sherline-tools-shutting-down-usa-production/)

Sherline Tools是一家久负盛名的美国精密微型加工车床、铣床及数控机床制造商，现已宣布将逐步停止生产业务。尽管自2017年以来一直致力于推进公司现代化，但所有者指出，后疫情时代挑战重重的制造环境、不断上升的运营成本以及消费者习惯的改变是导致结业的主要原因。

公司计划在2026年10月之前，或在现有库存、人员和材料允许的情况下，继续组装并销售机器、刀具及备件。然而，涉及大型生产设备的制造活动将提早停止，且所有者的最新消息显示，业务可能在今年年底前全面关闭。

Sherline承诺将负责任地退出，并表示将：
*   继续履行保修义务。
*   在库存允许的情况下提供备件。
*   维护其在线平台，并为机械加工社区保留丰富的技术和教育资源存档。

目前设备清算工作已经展开，标志着美国小型工具制造领域一个重要时代的终结。

---

## 8. 我把 Jev 变成了一个（差劲的）聊天机器人

**原文标题**: I turned Jev into a (lousy) chatbot

**原文链接**: [https://github.com/kyle-pena-nlp/jevchat/](https://github.com/kyle-pena-nlp/jevchat/)

生成摘要时出错

---

## 9. I am often wrong

**原文标题**: I am often wrong

**原文链接**: [https://borischerny.com/management,/product/2026/09/19/I-am-often-wrong.html](https://borischerny.com/management,/product/2026/09/19/I-am-often-wrong.html)

In this article, the author outlines a systematic, iterative framework for problem-solving and product development, particularly relevant in the rapidly evolving age of AI. The process consists of six key steps:

1.  Understanding available information.
2.  Gathering missing data.
3.  Defining the problem.
4.  Creating a clear, simple approach.
5.  Defining a goal.
6.  Acting with urgency.

The core of this philosophy is the necessity of updating one’s "priors" when new information emerges. This often requires revisiting and redefining the problem or approach. While this constant adjustment can feel "thrashy" or create a sense of churn, the author argues it is a healthy and necessary part of solving complex problems.

The author identifies the most common failure modes as a lack of clarity in defining the problem and the creation of overly complex solutions. To combat this, they emphasize the importance of real-time, mutual feedback between leaders and teams to ensure plans remain simple and goals remain clear.

Ultimately, the author reframes being "wrong" not as a failure, but as a vital tool for growth. Embracing mistakes and being open to changing course allows for faster learning, better problem definition, and the eventual discovery of the right solution.

---

## 10. Show HN: Radius – A Meetup.com Alternative

**原文标题**: Show HN: Radius – A Meetup.com Alternative

**原文链接**: [https://radius.to/](https://radius.to/)

**Radius** is a new community-building platform introduced as a streamlined alternative to Meetup.com. The platform is designed to facilitate local event organization and group management.

The provided content illustrates the platform's interface through a specific example: an event created by "Sarah K." for the **London Run Club**. Key features highlighted by the event listing include:

*   **Event Scheduling:** Clear display of the event title ("Saturday Morning 10K"), location (Hyde Park, London), and specific timing (Saturday, April 12 at 8:00 AM).
*   **Social Engagement:** A real-time tracker showing participant interest (e.g., "23 going").
*   **Categorization:** Tags such as "Sports & Fitness" help users filter activities based on their interests.
*   **Activity Updates:** Timestamps indicating when events were created to keep the community feed current.

Overall, Radius positions itself as a functional tool for organizers to coordinate local gatherings and for users to discover active communities within their geographic "radius."

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 2 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 3 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 4 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 5 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 6 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 7 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 8 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 9 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 10 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 11 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 12 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 13 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 14 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 15 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 16 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 17 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 18 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 19 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 20 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 21 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 22 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 23 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 24 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 25 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 26 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 27 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 28 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 29 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 30 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 31 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 32 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 33 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 34 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 35 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 36 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 37 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 38 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 39 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 40 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 41 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 42 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 43 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 44 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 45 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 46 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 47 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 48 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 49 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 50 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 51 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 52 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 53 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 54 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 55 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 56 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 57 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 58 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 59 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 60 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 61 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 62 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 63 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 64 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 65 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 66 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 67 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 68 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 69 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 70 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 71 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 72 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 73 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 74 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 75 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 76 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 77 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 78 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 79 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 80 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 81 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 82 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 83 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 84 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 85 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 86 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 87 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 88 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 89 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 90 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 91 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 92 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 93 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 94 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 95 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 96 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 97 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 98 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 99 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 100 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 101 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 102 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 103 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 104 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 105 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 106 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 107 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 108 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 109 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 110 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 111 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 112 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 113 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 114 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 115 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 116 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 117 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 118 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 119 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 120 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 121 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 122 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 123 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 124 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 125 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 126 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 127 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 128 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 129 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 130 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 131 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 132 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 133 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 134 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 135 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 136 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 137 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 138 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 139 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 140 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 141 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 142 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 143 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 144 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 145 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 146 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 147 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 148 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 149 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 150 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 151 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 152 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 153 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 154 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 155 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 156 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 157 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 158 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 159 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 160 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 161 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 162 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 163 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 164 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 165 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 166 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 167 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 168 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 169 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 170 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 171 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 172 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 173 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 174 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 175 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 176 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 177 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 178 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 179 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 180 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 181 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 182 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 183 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 184 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 185 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 186 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 187 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 188 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 189 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 190 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 191 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 192 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 193 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 194 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 195 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 196 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 197 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 198 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 199 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 200 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 201 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 202 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 203 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 204 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 205 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 206 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 207 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 208 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 209 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 210 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 211 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 212 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 213 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 214 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 215 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 216 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 217 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 218 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 219 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 220 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 221 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 222 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 223 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 224 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 225 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 226 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 227 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 228 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 229 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 230 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 231 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 232 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 233 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 234 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 235 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 236 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 237 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 238 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 239 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 240 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 241 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 242 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 243 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 244 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 245 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 246 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 247 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 248 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 249 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 250 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 251 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 252 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 253 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 254 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 255 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 256 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 257 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 258 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 259 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 260 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 261 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 262 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 263 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 264 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 265 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 266 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 267 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 268 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 269 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 270 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 271 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 272 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 273 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 274 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 275 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 276 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 277 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 278 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 279 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 280 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 281 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 282 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 283 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 284 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 285 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 286 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 287 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 288 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 289 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 290 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 291 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 292 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 293 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 294 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 295 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 296 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 297 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 298 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 299 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 300 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 301 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 302 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 303 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 304 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 305 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 306 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 307 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 308 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 309 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 310 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 311 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 312 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 313 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 314 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 315 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 316 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 317 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 318 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 319 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 320 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 321 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 322 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 323 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 324 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 325 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 326 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 327 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 328 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 329 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 330 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 331 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 332 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 333 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 334 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 335 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 336 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 337 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 338 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 339 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 340 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 341 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 342 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 343 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 344 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 345 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 346 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 347 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 348 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 349 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 350 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 351 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 352 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 353 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 354 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 355 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 356 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 357 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 358 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 359 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 360 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 361 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 362 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 363 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 364 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 365 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 366 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 367 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 368 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 369 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 370 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 371 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 372 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 373 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 374 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 375 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 376 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 377 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 378 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 379 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 380 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 381 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 382 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 383 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 384 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 385 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 386 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 387 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 388 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 389 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 390 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 391 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 392 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 393 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 394 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 395 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 396 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 397 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 398 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 399 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 400 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 401 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 402 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 403 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 404 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 405 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 406 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 407 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 408 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 409 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 410 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 411 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 412 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 413 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 414 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 415 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 416 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 417 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 418 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 419 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 420 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 421 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 422 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 423 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 424 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 425 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 426 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 427 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 428 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 429 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 430 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 431 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 432 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 433 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 434 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 435 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 436 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 437 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 438 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 439 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 440 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 441 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 442 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 443 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 444 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 445 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 446 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 447 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 448 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 449 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 450 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 451 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 452 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 453 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 454 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 455 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 456 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 457 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 458 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 459 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 460 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 461 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 462 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 463 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 464 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 465 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 466 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 467 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 468 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 469 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 470 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 471 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 472 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 473 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 474 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 475 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 476 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 477 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 478 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 479 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 480 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 481 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 482 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 483 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 484 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 485 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 486 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 487 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 488 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 489 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 490 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 491 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 492 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 493 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 494 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 495 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 496 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 497 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 498 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 499 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 500 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 501 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 502 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 503 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 504 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 505 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 506 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 507 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 508 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 509 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 510 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 511 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 512 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 513 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 514 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 515 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 516 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 517 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 518 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 519 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 520 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 521 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 522 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 523 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 524 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 525 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 526 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 527 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 528 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 529 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 530 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 531 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 532 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 533 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 534 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 535 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 536 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 537 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 538 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 539 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 540 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 541 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 542 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 543 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 544 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 545 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 546 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 547 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
