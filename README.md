# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-09-04.md)

*最后自动更新时间: 2025-09-04 17:46:07*
## 1. 几乎任何你持续关注的事物都会开始循环往复。

**原文标题**: Almost anything you give sustained attention to will begin to loop on itself

**原文链接**: [https://www.henrikkarlsson.xyz/p/attention](https://www.henrikkarlsson.xyz/p/attention)

亨利克·卡尔松认为，持续的注意力，无论指向何处，都能导致强化体验和意识状态的改变。他将性爱中延迟满足的愉悦与深入参与生活其他方面的潜力相提并论。作者解释了持续的注意力如何使身体系统同步，创造反馈回路来放大感觉和情绪，最终重塑我们的注意力场。

他警告说，过于频繁地切换注意力会导致“注意力残留”，阻碍深度连贯性。相反，长时间的专注可以让身体的子系统对齐，从而带来更高的体验。这一原则不仅适用于快乐，也适用于负面情绪，如焦虑（惊恐发作）和正面情绪，如喜悦（禅那）。

卡尔松认为，艺术，如果以持续的注意力来欣赏，可以作为一种引导冥想，触发深刻的情感和视觉体验。他以聆听西贝柳斯第五交响曲为例，音乐促进了生动的白日梦和情感处理。最终，这篇文章倡导持续注意力的力量，以解锁各个领域的变革性体验，敦促读者探索专注观察中隐藏的潜力。

---

## 2. 缓存

**原文标题**: Cache

**原文链接**: [https://developer.mozilla.org/en-US/docs/Web/API/Cache](https://developer.mozilla.org/en-US/docs/Web/API/Cache)

Cache接口为浏览器内的 Request/Response 对象对提供持久存储机制。 这些缓存由源站脚本（通常在 ServiceWorker 中）命名和管理。 缓存条目不会自动更新或过期；开发人员负责更新和清除它们。 每个浏览器都对每个源站强制执行存储配额，使用 `StorageManager.estimate()` 可以提供使用情况估算。 按名称进行缓存版本控制对于跨脚本版本的安全操作至关重要。

Cache接口提供了管理缓存响应的方法。 `Cache.match()` 和 `Cache.matchAll()` 从缓存中检索匹配的响应。 `Cache.add()` 和 `Cache.addAll()` 获取响应并将其添加到缓存中，而 `Cache.put()` 直接添加请求/响应对。 `Cache.delete()` 根据其请求删除条目。 `Cache.keys()` 返回缓存键的数组。

提供的代码示例演示了 Service Worker 对字体资源的缓存。 它打开一个版本化的字体缓存，检查是否存在现有的缓存响应，如果未找到，则从网络获取资源，并缓存有效的字体响应。 它还包括在 Service Worker 激活期间删除旧的、过时缓存的逻辑。 值得注意的是，该示例展示了如何使用 `Request.clone()` 和 `Response.clone()` 来确保 Request/Response 对象可以多次使用（例如，既可以将原始对象返回给用户，又可以将副本添加到缓存）。

重要注意事项：缓存键匹配考虑了 VARY 标头，缓存 API 忽略 HTTP 缓存标头，并且存储在缓存中的 Response 对象将不包含 Set-Cookie 标头。 此功能需要安全上下文 (HTTPS)，并且在 Web Worker 中可用。

---

## 3. Le Chat. 定制MCP连接器. 回忆

**原文标题**: Le Chat. Custom MCP Connectors. Memories

**原文链接**: [https://mistral.ai/news/le-chat-mcp-connectors-memories](https://mistral.ai/news/le-chat-mcp-connectors-memories)

Mistral AI升级Le Chat，推出两大功能：通过自定义MCP连接器增强连接性，以及用于个性化AI辅助的“记忆”功能。

Le Chat现在通过MCP（Mistral连接器平台）与超过20个企业平台集成，允许用户在Databricks、Snowflake、GitHub等工具中搜索、总结和执行操作。用户还可以添加自定义MCP连接器来集成独特的系统和工作流程。部署选项包括移动端、浏览器、本地或云端。“记忆”功能使Le Chat能够记住用户偏好和信息，从而提供更相关的响应和建议。用户可以完全控制存储的记忆，可以选择添加、编辑或删除条目。现有记忆可以从ChatGPT导入。

连接器涵盖数据、生产力、开发、自动化和商业等重要类别。连接器使用示例包括总结来自Databricks的客户评论和创建Asana工单，审查GitHub拉取请求和创建Jira问题，以及比较Box中的财务文档。用户还可以连接到任何远程MCP服务器，即使它未在目录中列出。

连接器和记忆功能均在免费的Le Chat计划中提供。Mistral AI将于9月9日举办网络研讨会，并于9月13日至14日举办黑客马拉松，以展示这些新的MCP功能。Le Chat可通过Web、App Store和Google Play商店访问。

---

## 4. 与陌生人的三十分钟

**原文标题**: 30 minutes with a stranger

**原文链接**: [https://pudding.cool/2025/06/hello-stranger/](https://pudding.cool/2025/06/hello-stranger/)

本文探讨了一个名为CANDOR语料库的研究项目，该项目将陌生人配对进行30分钟的视频通话，以研究对话动态。研究人员从大约1500人那里收集了近1700个对话，这些人的年龄、种族、教育程度和政治意识形态等人口统计数据各不相同。

最初，许多参与者感觉和通话前一样，甚至更糟。这与一些研究结果一致，这些研究表明，人们在与陌生人互动时，往往会预测到负面体验。然而，本文强调这种看法往往是不准确的。一项2014年的研究发现，被要求在公共交通工具上与陌生人交谈的通勤者报告了积极的体验，这与他们最初的预期相反。

随着CANDOR项目中30分钟对话的进行，很大一部分参与者表示感觉比开始时更好。这表明与不熟悉的人互动可以改善情绪。作者还观察到，许多对话触及了亲密话题，展现了与陌生人之间令人惊讶的开放程度。虽然一些对话因分歧而脱轨，但大多数参与者都喜欢听取和分享他们的生活，即使是那些共同点很少的人也是如此。这篇文章强调了“桥梁”社会资本——与不同个体建立关系——的重要性，而这种资本在我们日益同质化的社交圈中往往缺失。

---

## 5. 展示一下：一张所有YC公司地图（按批次和地点划分的5300家初创公司）

**原文标题**: Show HN: A Map of All YC Companies (5,300 Startups by Batch and Location)

**原文链接**: [https://yc.foundersaround.com/](https://yc.foundersaround.com/)

“Show HN”发布：YC公司地图上线，一款由FoundersAround驱动的Web应用，可视化展示全球超过5300家Y Combinator初创公司的地理分布。该地图允许用户按批次和国家浏览公司，直观呈现YC生态系统的全球影响力。目前，地图显示“0家公司”，表明数据可能尚未加载或过滤。该平台还提供赞助机会，每月350美元即可在地图上获得醒目的“UFO”图标。最后，该帖子宣传可供其他加速器、大学和风险投资公司使用的地图定制版本，推广FoundersAround平台作为可视化和探索创始人生态系统的工具。帖子提供foundersaround.com链接，以便探索YC网络以外的创始人。

---

## 6. Artie (YC S23) 招聘工程师、应用工程师和资深产品营销经理

**原文标题**: Artie (YC S23) Is Hiring Engineers, AES, and Senior PMM

**原文链接**: [https://www.ycombinator.com/companies/artie/jobs](https://www.ycombinator.com/companies/artie/jobs)

Artie，一家 Y Combinator S23 公司，正在招聘多个关键职位：**创始客户主管 (Account Executive)**、**资深产品营销经理**、**创始产品工程师**，以及**创始工程师 (分布式系统)**。所有职位均位于旧金山，要求 3 年以上经验。

Artie 正在构建一个专注于数据库和数据仓库的实时数据流解决方案。他们旨在通过利用变更数据捕获 (CDC) 和流处理来实现亚分钟级延迟的数据同步，从而克服传统 ETL 解决方案的局限性，这比面向批处理的流程有了显著的改进。

该公司成立于 2023 年，目前由 8 人团队组成，状态为“活跃”。创始人是 Jacqueline Cheong 和 Robin Tang。

薪酬方案包括工资和股权，客户主管职位的薪资范围为 11 万美元至 13 万美元，股权为 0.10%；资深产品营销经理职位的薪资范围为 14.5 万美元至 18.5 万美元，股权为 0.20% 至 0.40%；两个工程师职位的薪资范围均为 15 万美元至 21.5 万美元，股权为 0.50% 至 1.00%。

---

## 7. 浏览器公司（Arc浏览器制造商）被Atlassian以6.1亿美元收购

**原文标题**: Browser Company (makers of Arc browser) Acquired By Atlassian for $610M

**原文链接**: [https://browsercompany.substack.com/p/your-tuesday-in-2030](https://browsercompany.substack.com/p/your-tuesday-in-2030)

无法访问文章链接。

---

## 8. 谷歌从可持续发展网站上删除净零排放承诺

**原文标题**: Google deletes net-zero pledge from sustainability website

**原文链接**: [https://www.nationalobserver.com/2025/09/04/investigations/google-net-zero-sustainability](https://www.nationalobserver.com/2025/09/04/investigations/google-net-zero-sustainability)

2020年，谷歌承诺到2030年实现净零排放，该承诺曾醒目地展示在其可持续发展网站上。然而，加拿大国家观察报发现，谷歌已于2025年6月下旬悄然从其网站上撤下了这一承诺，将其降级至公司可持续发展报告的附录中。

谷歌承认，由于需要大量能源的人工智能数据中心的快速扩张，实现其净零排放目标变得更加复杂。该公司2024年的电力消耗量增加了26%，几乎与爱尔兰的总消耗量持平。麦肯锡公司的一份报告预测，人工智能将推动电力需求的显著增长，到2030年可能占美国能源总需求的12%。

一些专家认为，撤销该承诺也受到了特朗普政府可能回归的影响，该政府以反对气候政策和企业可持续发展努力而闻名。尽管撤下了头条承诺，谷歌仍坚称其仍然致力于2030年的目标，该目标在很大程度上依赖于碳抵消。

专家对此反应不一。一些人认为谷歌的举动是更广泛的“净零衰退”的一部分，而另一些人则认为这是对更现实目标的重新调整。人们担心这些行动可能会削弱人们对净零承诺的信心。虽然谷歌继续投资于可再生能源，但人工智能日益增长的能源需求对其可持续发展承诺提出了重大挑战。

---

## 9. Show HN：我做了FlipCards – 一款利用多种变化来提高学习效果的抽认卡应用

**原文标题**: Show HN: I built FlipCards – a flashcard app with variations to improve learning

**原文链接**: [https://flipcardsapp.vercel.app/](https://flipcardsapp.vercel.app/)

此帖为“Show HN”提交，介绍 FlipCards，一款旨在提高学习效率的新型抽认卡应用。核心概念是使用抽认卡，但标语“用抽认卡学得更聪明”表明 FlipCards 可能包含超越传统抽认卡应用的功能或变体，以增强学习过程。帖子内容简短，使得具体功能和改进成为谜团，鼓励读者探索该应用并了解更多信息。

---

## 10. 使用微流体技术的可编程显示器

**原文标题**: A programmable display using microfluidics

**原文链接**: [https://www.youtube.com/watch?v=rf-efIZI_Dg](https://www.youtube.com/watch?v=rf-efIZI_Dg)

此片段结合了两个看似无关的事物：“使用微流体技术的可编程显示器”和 YouTube 的标准页脚信息。 核心主题是**一种利用微流体技术的可编程显示器**。 这意味着一种使用微小通道来控制和操作流体的显示器，可能用于创建像素或光图案。

YouTube 的内容是与版权、内容创作者、广告、服务条款、隐私以及 YouTube 平台的其他法律和运营方面相关的标准样板文本。 它与文章的实际主题无关，除非可能突出显示文章/内容的来源地或可能找到的地方。

因此，相关信息是该文章讨论了**一种基于微流体技术的新型显示技术。 该技术允许通过在微观层面操纵流体来创建可编程显示器**。 片段中没有提供关于微流体如何工作的具体细节，但它表明该技术是创新的，并利用流体控制进行视觉输出。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 2 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 3 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 4 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 5 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 6 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 7 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 8 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 9 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 10 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 11 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 12 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 13 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 14 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 15 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 16 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 17 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 18 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 19 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 20 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 21 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 22 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 23 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 24 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 25 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 26 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 27 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 28 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 29 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 30 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 31 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 32 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 33 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 34 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 35 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 36 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 37 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 38 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 39 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 40 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 41 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 42 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 43 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 44 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 45 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 46 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 47 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 48 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 49 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 50 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 51 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 52 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 53 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 54 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 55 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 56 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 57 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 58 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 59 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 60 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 61 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 62 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 63 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 64 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 65 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 66 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 67 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 68 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 69 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 70 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 71 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 72 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 73 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 74 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 75 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 76 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 77 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 78 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 79 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 80 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 81 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 82 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 83 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 84 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 85 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 86 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 87 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 88 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 89 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 90 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 91 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 92 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 93 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 94 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 95 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 96 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 97 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 98 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 99 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 100 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 101 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 102 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 103 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 104 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 105 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 106 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 107 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 108 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 109 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 110 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 111 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 112 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 113 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 114 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 115 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 116 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 117 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 118 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 119 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 120 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 121 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 122 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 123 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 124 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 125 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 126 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 127 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 128 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 129 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 130 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 131 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 132 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 133 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 134 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 135 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 136 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 137 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 138 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 139 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 140 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 141 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 142 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 143 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 144 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 145 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 146 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 147 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 148 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 149 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 150 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 151 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 152 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 153 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 154 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 155 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 156 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 157 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 158 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 159 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 160 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 161 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 162 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 163 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 164 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 165 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 166 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 167 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 168 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 169 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
