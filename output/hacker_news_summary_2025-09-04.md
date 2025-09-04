# Hacker News 热门文章摘要 (2025-09-04)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. 在英国，仲裁庭裁定称老板是“混蛋”并非可被解雇的罪行。

**原文标题**: Calling your boss a dickhead is not a sackable offence, UK tribunal rules

**原文链接**: [https://www.theguardian.com/money/2025/sep/04/calling-your-boss-a-dickhead-is-not-a-sackable-offence-tribunal-rules](https://www.theguardian.com/money/2025/sep/04/calling-your-boss-a-dickhead-is-not-a-sackable-offence-tribunal-rules)

英国就业仲裁庭裁定，称呼老板为“蠢货”不一定构成立即解雇的理由，判决柯丽·赫伯特因不公平解雇获得近3万英镑的赔偿金和法律费用。赫伯特是Main Group Services的办公室经理，在与经理托马斯·斯瓦内尔和另一位董事发生激烈争吵时使用了该词，随后被立即解雇。

由索尼娅·博伊斯法官领导的仲裁庭发现，该公司未能遵守适当的纪律程序，并且赫伯特的一次性评论虽然不可接受，但并未构成严重不当行为，以致需要立即解雇。赫伯特的合同规定，虽然侮辱性语言可能导致解雇，但与“威胁和恐吓性语言”不同，它需要事先警告。

事发原因是赫伯特发现文件表明她可能被裁员，随后又受到斯瓦内尔的绩效批评。她承认在回应中称斯瓦内尔和他的妻子为“蠢货”，导致她被立即解雇。仲裁庭最终裁定，使用“蠢货”一词不足以构成立即解雇的充分理由，并命令Main Group Services支付赔偿金并承担赫伯特的法律费用。

---

## 12. WiFi信号可以测量心率——无需可穿戴设备

**原文标题**: WiFi signals can measure heart rate–no wearables needed

**原文链接**: [https://news.ucsc.edu/2025/09/pulse-fi-wifi-heart-rate/](https://news.ucsc.edu/2025/09/pulse-fi-wifi-heart-rate/)

加州大学圣克鲁兹分校的研究人员开发了一种名为“脉冲Fi”的系统，该系统利用WiFi信号精确测量人的心率，无需佩戴可穿戴设备。该系统在2025年IEEE DCOSS-IoT会议论文集中进行了详细介绍，它利用低成本的WiFi设备，如ESP32芯片（5-10美元）和树莓派芯片，以及一种机器学习算法来检测由心跳引起的WiFi信号的微小变化。

脉冲Fi过滤掉环境噪声和运动，专门关注由心脏引起的信号变化。在对118名参与者进行的实验中，该系统仅需五秒的信号处理即可达到临床级别的精度，误差率仅为每分钟半次心跳。无论人的姿势如何（坐着、站着、躺着、走路），该系统的准确性都保持一致，并且在10英尺范围内有效工作。

研究人员使用ESP32设备和一个标准血氧仪创建了自己的数据集来训练机器学习算法。他们的发现表明，基于WiFi的非侵入式健康监测具有在家中应用的潜力，特别是在低资源环境中，因为所需硬件的成本很低。未来的研究旨在扩展脉冲Fi以检测呼吸频率和睡眠呼吸暂停等疾病。该大学也对该技术的商业用途持开放态度。

---

## 13. 如何从零开始构建矢量瓦片

**原文标题**: How to build vector tiles from scratch

**原文链接**: [https://www.debuisne.com/writing/geo-tiles/](https://www.debuisne.com/writing/geo-tiles/)

本文详细介绍了如何从零开始构建矢量瓦片，以提高 Web 应用程序中的地图渲染性能。作者探讨了使用 GeoJSON 处理大型数据集的局限性，并提出了矢量瓦片作为一种更有效的解决方案，类似于 SVG 比 JPEG 更高效。

矢量瓦片是代表特定扇区（瓦片）中特定缩放级别的地理要素的小文件。与将所有要素存储在一个文件中的 GeoJSON 不同，矢量瓦片存储绘图指令，从而允许动态自定义。本文重点介绍使用 Mapbox 矢量瓦片 (MVT) 标准，利用 Protobuf 进行二进制数据编码。

创建矢量瓦片的过程包括：根据要素的坐标和缩放级别确定要素属于哪个瓦片，使用 Protobuf 定义创建瓦片，添加几何信息，以及将要素属性作为标签包含在内。作者提供了 Go 代码片段，用于在 EPSG:4326（度）和 EPSG:3857（Web 墨卡托）之间转换坐标，计算瓦片坐标，以及创建基于 Protobuf 的 MVT 文件。该说明涵盖了如何使用官方 Mapbox 矢量瓦片规范，以及如何在瓦片内构建数据，包括图层、要素和几何类型。

---

## 14. 好莱坞不再制作的手绘热门动画

**原文标题**: The Hand-Drawn Hits That Hollywood Isn't Making

**原文链接**: [https://animationobsessive.substack.com/p/the-hand-drawn-hits-that-hollywood](https://animationobsessive.substack.com/p/the-hand-drawn-hits-that-hollywood)

无法访问文章链接。

---

## 15. 告别Meshnet

**原文标题**: Farewell to Meshnet

**原文链接**: [https://nordvpn.com/blog/meshnet-shutdown/](https://nordvpn.com/blog/meshnet-shutdown/)

无法访问文章链接。

---

## 16. 年龄模拟套装

**原文标题**: Age Simulation Suit

**原文链接**: [https://www.age-simulation-suit.com/](https://www.age-simulation-suit.com/)

老年体验模拟器GERT是一种年龄模拟套装，旨在让年轻人体验与衰老相关的身体障碍。该套装模拟了诸如眼球晶状体混浊、视野缩小、高频听力损失、头部活动受限、关节僵硬、力量丧失、抓握能力下降以及协调能力降低等状况。

GERT套装售价为1390欧元或1250英镑，外加运费和增值税。它包含如图所示的完整套装，现在包含两副眼镜，而不是旧型号中的一副。由于处理工作量增加，订单金额必须至少为300欧元或300英镑。

客户评论强调了该套装的高质量、在模拟老年人行为方面的有效性、耐用性和易用性。评论者发现它对教育目的非常有价值。

---

## 17. 空洞骑士：丝之歌 引发 Xbox、Steam 和任天堂服务器混乱

**原文标题**: Hollow Knight: Silksong Causes Server Chaos on Xbox, Steam, and Nintendo

**原文链接**: [https://www.eurogamer.net/silksong-causes-server-chaos-on-xbox-steam-and-nintendo-as-platforms-grind-to-a-halt](https://www.eurogamer.net/silksong-causes-server-chaos-on-xbox-steam-and-nintendo-as-platforms-grind-to-a-halt)

备受期待的《空洞骑士：丝之歌》发布引发了各大游戏平台（包括Steam、Xbox、PlayStation和任天堂Switch）的混乱。报告显示，Steam出现了严重问题，因玩家蜂拥购买而速度变慢。用户在使用PayPal付款时遇到错误，并且难以将游戏添加到购物车。

Xbox用户遇到黑屏和“丝之歌不可用”的消息，导致他们无法访问游戏。PlayStation用户发现《丝之歌》卡在他们的愿望单上，无法购买。任天堂Switch上也出现了未指明的与《丝之歌》相关的问题。该文章包含来自Eurogamer的截图，展示了用户在这些平台上尝试购买《丝之歌》时遇到的各种问题。总而言之，《丝之歌》的发布饱受技术问题困扰，阻碍了玩家购买和游玩游戏。

---

## 18. 反转Xorshift128随机数生成器

**原文标题**: Inverting the Xorshift128 random number generator

**原文链接**: [https://littlemaninmyhead.wordpress.com/2025/08/31/inverting-the-xorshift128-random-number-generator/](https://littlemaninmyhead.wordpress.com/2025/08/31/inverting-the-xorshift128-random-number-generator/)

这篇博文详细介绍了一种高效的算法，用于反转 Xorshift128+ 随机数生成器，该算法是 JavaScript 的 `Math.random()` 函数的底层实现。作者旨在改进依赖 z3 等工具的现有方法，认为确定内部状态所需的输出更少即可。

该算法的核心仅需要 Xorshift128+ 生成器的两个完整的 64 位输出。它将搜索空间从 2^128（暴力破解）减少到 2^64，然后进一步减少到 2^26 次运算。这种 2^26 算法专注于猜测一个状态 (R1) 的最低有效 26 位，然后使用一个归纳方程来推导出其他状态（L1 和 R2）的剩余位。通过计算候选状态并将它们与观察到的输出 (x1) 进行比较，该算法验证其猜测，迭代可能的 R1 值直到找到解决方案。作者还提出了速度优化建议，并讨论了将该算法转化为与 `Math.random()` 函数一起使用的可能性，`Math.random()` 函数仅提供 52 位输出，可能需要三个输出和更大的 2^50 搜索空间。作者还分享了他们使用 ChatGPT 进行代码生成的负面经验，同时承认它作为研究助手的价值。源代码可在 Github 上获得。

---

## 19. Atlassian收购浏览器公司

**原文标题**: Atlassian is acquiring the Browser Company

**原文链接**: [https://www.cnbc.com/2025/09/04/atlassian-the-browser-company-deal.html](https://www.cnbc.com/2025/09/04/atlassian-the-browser-company-deal.html)

Atlassian拟以6.1亿美元现金收购Arc和Dia浏览器开发商The Browser Company，预计12月完成交易。The Browser Company的Arc浏览器以其可定制界面和标签组织功能而闻名，而Dia则是一款更简单的AI驱动浏览器。

Atlassian首席执行官Mike Cannon-Brookes认为当前浏览器未针对工作进行优化，并计划将Arc的应用程序体验和Dia的AI功能与Atlassian的企业专业知识相结合，以改善其用户的浏览器体验。此前，OpenAI和Perplexity也曾对收购The Browser Co.表示出兴趣。

尽管Arc因其专业功能而备受关注，但难以成为大众市场产品，这引发了对其未来的质疑，包括可能开源该浏览器。此次收购对Atlassian具有战略意义，因为其Jira项目管理软件严重依赖于Web浏览器。该公司旨在利用The Browser Co.的技术来增强其产品，并为其企业用户创造更高效的浏览体验。Perplexity也在开发一款名为Comet的AI浏览器。The Browser Co.之前的估值为5.5亿美元，投资者包括Atlassian Ventures和Salesforce Ventures。

---

## 20. 维基百科屹立不倒，互联网其余部分崩溃瓦解。

**原文标题**: Wikipedia survives while the rest of the internet breaks

**原文链接**: [https://www.theverge.com/cs/features/717322/wikipedia-attacks-neutrality-history-jimmy-wales](https://www.theverge.com/cs/features/717322/wikipedia-attacks-neutrality-history-jimmy-wales)

本文探讨了维基百科在日益碎片化和不可靠的互联网环境中，作为可靠信息来源所展现出的惊人韧性。尽管面临来自权势人物和政府的攻击，指责其存在偏见，但维基百科凭借其独特的协作编辑模式和致力于基于共识呈现事实信息的精神，依然蓬勃发展。

文章重点介绍了维基百科编辑通过严谨（尽管有时充满争议）的流程来辩论和提炼信息的机制，例如围绕埃隆·马斯克涉嫌行纳粹礼的争议。这个过程虽然不完美，但促进了共享的共识现实，并抵制了其他在线平台上普遍存在的“回声室”效应。

作者认为，维基百科的优势在于其对中立的承诺，以及避免主动站队或参与党派辩论。文章强调，在虚假信息和宣传泛滥的世界中，维基百科作为事实“压舱石”的作用至关重要。文章最后指出，维基百科的持续成功取决于其保持“无聊”和可靠的信息来源的能力，从而证明了集体知识共享的力量，并与现代互联网的混乱形成了鲜明对比。

---

## 21. 撰写优秀谜题寻宝谜题入门

**原文标题**: Introduction to Writing Good Puzzle Hunt Puzzles

**原文链接**: [https://www.mit.edu/~dwilson/puzzles/puzzlewriting.html](https://www.mit.edu/~dwilson/puzzles/puzzlewriting.html)

本文档旨在为编写有效的谜题寻宝游戏谜题提供建议，主要面向麻省理工学院神秘寻宝游戏，最终目标是为解谜者创造有趣的体验。它强调，谜题编写者应致力于创造可解决的挑战，让解谜者感到成就感，而不是试图过于困难或晦涩。

本文档建议新手编写者从一开始就考虑谜题机制和主题，从而创造出更有趣的谜题。它告诫不要过度依赖“ISIS”（识别、排序、索引、解决）谜题，因为它们很常见，但也承认它们作为快速替代方案的有用性。如果编写 ISIS 谜题，请专注于让识别步骤变得有趣，并融入曲折以获得原创性。

本文档鼓励编写者从过去的谜题以及现实生活中的物体和事件中寻找灵感，以生成独特的谜题机制。与他人合作也可能是有益的，尤其是在个人拥有互补技能的情况下。

关于谜题难度，本文档强调，模糊不清与难度不同。包含导致错误路径的多余信息的谜题令人沮丧。相反，目标是创建一条通往解决方案的清晰路径的谜题，即使具有挑战性。最终，谜题的成功取决于其为解谜者提供有趣且有益体验的能力。

---

## 22. Thunk：构建Rust程序以支持Windows XP、Vista等

**原文标题**: Thunk: Build Rust program to support Windows XP, Vista and more

**原文链接**: [https://github.com/felixmaker/thunk](https://github.com/felixmaker/thunk)

本文介绍了Thunk，一个用于构建与XP和Vista等较旧Windows版本兼容的Rust程序的工具。它利用VC-LTL5和YY-Thunks来实现这一点。VC-LTL被添加到库搜索路径中，而YY-Thunks为较旧系统中缺少的API提供解决方法。

Thunk有两种形式：命令行工具和Rust库。作为CLI，它要求用户下载并配置VC-LTL5和YY-Thunks，并相应地设置环境变量。`cargo install thunk-cli` 安装该工具，并使用诸如`thunk --os xp --arch x86 -- --release`之类的命令调用它来为特定的操作系统和架构构建。

作为库，它使用`cargo add thunk-rs --build`作为构建依赖项添加。一个简单的带有`thunk::thunk()`的`build.rs`文件启动构建过程，以实现旧Windows兼容性。

本文强调Thunk不保证在旧平台上实现完美的功能，并警告用户自行承担风险。它提供了当前支持的Windows版本列表，并且未来的计划包括支持更多架构并添加Scoop bucket。

---

## 23. Polars云和分布式Polars现已可用

**原文标题**: Polars Cloud and Distributed Polars now available

**原文链接**: [https://pola.rs/posts/polars-cloud-launch/](https://pola.rs/posts/polars-cloud-launch/)

Polars已推出Polars Cloud，现已在AWS上全面可用，其分布式引擎在Polars Cloud上开启公开测试。这旨在弥合Pandas本地数据处理与PySpark等大规模云处理工具之间的差距，提供一个单一、可扩展的API。

Polars Cloud是一个用于大规模远程运行Polars查询、管理云基础设施和扩展的托管平台。分布式引擎利用Polars的流式架构进行横向、纵向和对角扩展，从而优化成本、复杂性和性能。当分布式支持不可用时，它会自动回退到单节点执行。

主要优势包括原生的远程执行体验和无摩擦的分布式处理。该引擎擅长将可分区查询与依赖顺序的数据处理相结合。

近期未来的功能将包括本地支持、具有详细跟踪和利用率洞察的实时集群仪表板、基本任务编排功能、自动伸缩（纵向、对角和横向）、目录支持（具有原生和分布式Iceberg支持）以及多区域可用性。

用户可以通过注册链接开始在AWS上使用Polars Cloud。

---

## 24. Stripe推出L1区块链：Tempo

**原文标题**: Stripe Launches L1 Blockchain: Tempo

**原文链接**: [https://tempo.xyz](https://tempo.xyz)

Stripe和Paradigm推出Tempo，专为支付设计的新Layer 1区块链。Tempo旨在解决现有区块链过于通用或侧重交易的局限性，为现实世界的支付流程提供定制化解决方案。

Tempo拥有高吞吐量（10万+ TPS）、亚秒级最终确认时间、可预测的近零费用（可用任何稳定币支付）以及内置隐私功能。关键设计特性包括专用支付通道、稳定币互操作性、批量转账、用于合规的黑名单/白名单以及符合ISO 20022标准的备忘录字段。

该项目已收到来自多家公司的设计输入，包括Anthropic、Coupang、德意志银行、DoorDash、Lead Bank、Mercury、Nubank、OpenAI、Revolut、Shopify、渣打银行和Visa。Tempo的目标是广泛的支付用例，如汇款、全球支付、嵌入式金融、微交易、代理商务和代币化存款。

该区块链与EVM兼容且无需许可，允许任何人在此基础上进行构建。Stripe目前正在为特定合作伙伴提供对其私有测试网的访问权限，并计划将来过渡到无需许可的验证器模型。此次发布旨在通过提高支付处理的速度、效率和可靠性，改变企业在全球范围内转移资金的方式。

---

## 25. 给你的警察局使用Flock Safety踩刹车

**原文标题**: Pump the Brakes on Your Police Department's Use of Flock Safety

**原文链接**: [https://www.aclu.org/news/privacy-technology/how-to-pump-the-brakes-on-your-police-departments-use-of-flocks-mass-surveillance-license-plate-readers](https://www.aclu.org/news/privacy-technology/how-to-pump-the-brakes-on-your-police-departments-use-of-flocks-mass-surveillance-license-plate-readers)

美国公民自由联盟警告：Flock安全公司的车牌自动识别摄像头正迅速构建全国性大规模监控系统，应警惕其危害。与目标明确的车牌识别系统不同，Flock收集人们的出行数据，并向包括联邦机构在内的众多执法客户开放。这造成了一种“奥威尔式”的系统，侵犯隐私，并可能助长未经个别怀疑就跟踪个人的滥用行为。

作者敦促彻底反对Flock系统。但考虑到这并非总是可行，他们提供了减轻危害的指导。谈判和监管的关键领域包括：

*   **数据保留：** 倡导尽可能缩短车牌识别数据的保留期限。
*   **数据共享/使用：** 限制车牌识别数据用于本地，防止外部执法部门将其用于执行反堕胎法律或协助外国政权等目的。
*   **数据库使用：** 阻止车牌识别数据与不可靠的国家数据库（如NCIC）进行比对，这可能导致不合理的逮捕，尤其是针对弱势群体。

文章强调，警察部门和地方领导人不应仅仅因为该公司获益或因为其他辖区这样做就盲目采用Flock系统。即使无法完全阻止Flock系统，也应努力将其使用范围限制在当地社区，并防止其成为国家和国际大规模监控网络的一部分。

---

## 26. 克劳德代码：现已在 Zed 中开启 Beta 测试

**原文标题**: Claude Code: Now in Beta in Zed

**原文链接**: [https://zed.dev/blog/claude-code-via-acp](https://zed.dev/blog/claude-code-via-acp)

Zed集成了Claude Code作为公开测试版，响应了众多用户需求。Zed没有采用简单的集成方式，而是开发了代理客户端协议（ACP），这是一个开放标准，允许任何AI代理连接Zed和其他编辑器。

Claude Code集成提供：

*   在Zed中原生集成，提供比终端界面更好的性能。
*   跨多个文件的实时代码编辑，具有语法高亮显示。
*   细粒度的更改审查，能够接受或拒绝代码块。
*   侧边栏任务列表，用于跟踪代理的进度。
*   使用Claude Code斜杠命令的自定义工作流程。

此集成利用ACP，使用适配器将Claude Code的SDK转换为ACP的JSON RPC格式，从而实现代理和编辑器之间的无缝通信。Zed正在Apache许可证下开源Claude Code适配器，使其可用于其他兼容ACP的编辑器，例如Neovim（通过CodeCompanion插件）。

Zed鼓励开发人员使用ACP将其他代理引入Zed、Gemini CLI和Neovim。 Zed正在积极开发更多Claude Code功能，如Plan模式，并要求社区倡导Anthropic提供与Claude Code的SDK同等功能，或直接采用ACP。 行动号召包括为ACP和Claude Code适配器存储库做出贡献。

---

## 27. Étoilé – 基于GNUStep的桌面环境

**原文标题**: Étoilé – desktop built on GNUStep

**原文链接**: [http://etoileos.com/](http://etoileos.com/)

Étoilé 是一个基于 GNUstep 的开源桌面环境，旨在创建以创造、协作和学习为中心的用户友好体验。它致力于抽象化文件和操作系统进程等实现细节，让用户专注于他们的任务。主要功能包括所有对象的修订历史、协作文档编辑（文本、绘图、代码等）、通过提供的服务实现可定制的工作流程，以及更直观的用户界面，反映人们与计算机的自然交互方式。该项目以 MIT/BSD 许可协议授权，使其可移植到大多数操作系统。最近的新闻亮点包括 CoreObject、Smalltalk 和 C 集成、XMPPKit 和 StepChat 开发以及 Étoilé 0.4.2 版本的更新。

---

## 28. 未来的颜色：蓝色的历史

**原文标题**: The Color of the Future: A history of blue

**原文链接**: [https://www.hopefulmons.com/p/the-color-of-the-future](https://www.hopefulmons.com/p/the-color-of-the-future)

未来的颜色：蓝色简史

本文探讨了蓝色颜色的历史发展和文化意义，认为其人为的稀缺性导致了它与技术和未来的联系。文章追溯了各种蓝色颜料的起源，从天然来源（如从全球各地植物中提取的靛蓝）开始。它重点介绍了埃及人早期创造的合成埃及蓝，这项技术后来失传，并在中国被独立重新发现，即汉蓝。

文章随后深入探讨了青金石的重要性，青金石是一种稀有矿物，在中世纪的欧洲被用来制造备受推崇的群青颜料，文章强调了其高昂的成本以及在宗教艺术中的专属用途，例如绘制圣母玛利亚的袍子。

叙述过渡到现代，详细介绍了 18 世纪意外发现的普鲁士蓝，这是第一种现代合成颜料，及其随后对艺术和工业的影响，包括蓝图。文章进一步讨论了其他合成蓝色的发展，如蔚蓝、钴蓝和合成群青，以及在人造靛蓝、食用色素（蓝色 1 号和 2 号）和酞菁蓝等方面的应用。

文章最后提到了最近发现的 YInMn 蓝，并考虑了蓝色在科幻界面中的广泛使用，这可能是由于蓝色 LED 的普及以及其与寒冷、知识和超凡脱俗的联想所驱动的。总的来说，文章认为蓝色的技术起源和文化内涵巩固了其作为“未来颜色”的角色。

---

## 29. 扫雷热力学

**原文标题**: Minesweeper thermodynamics

**原文链接**: [https://oscarcunningham.com/792/minesweeper-thermodynamics/](https://oscarcunningham.com/792/minesweeper-thermodynamics/)

奥斯卡·坎宁安探索了一种利用热力学原理，特别是玻尔兹曼分布，来改进扫雷策略的方法。文章提出，当面临没有明显安全走法的情况时，可以计算每个格子安全的概率，并根据剩余地雷和格子的数量，考虑不同地雷排列的可能性。

核心思想是将扫雷游戏中未解开的部分视为一个处于“地雷浴”中的热力学系统。特定地雷排列的概率类似于物理系统处于特定能量状态的概率。通过应用玻尔兹曼定律的改进版本，文章展示了如何对这些可能性进行加权，从而与简单地平均可能性相比，能够更准确地评估每个格子的安全概率。

文章引入了“地雷温度”的概念，以量化不同地雷排列的相对可能性。虽然承认这种近似对于标准扫雷棋盘来说并不完美，但作者认为，随着地雷数量的增加，这种方法会得到改善，从而模拟宏观物理系统的行为。最终，这篇文章提供了一种新颖的扫雷方法，利用统计力学的概念，在面对不确定性时做出更明智的决策。

---

## 30. 机电重塑带来更安全的眼科手术

**原文标题**: Electromechanical Reshaping Offers Safer Eye Surgery

**原文链接**: [https://spectrum.ieee.org/electrochemistry-for-eye-surgeries](https://spectrum.ieee.org/electrochemistry-for-eye-surgeries)

一种新型机电重塑技术为LASIK眼科手术提供了一种潜在的、更安全的替代方案。据《生物医学新闻》报道，梅吉·罗德里格斯撰写的这篇发表于2025年9月2日的文章强调了该技术通过调整pH值来矫正角膜的能力。文章指出，重塑已成功在兔角膜上进行，使其从原始形状变平至矫正后的形状。这种机电方法似乎是眼科手术领域的一项有前景的进展，有可能取代更具侵入性的LASIK手术。这篇文章篇幅短小，只需阅读3分钟。

---

## 31. Neovim 插件包

**原文标题**: Neovim Pack

**原文链接**: [https://neovim.io/doc/user/pack.html#vim.pack](https://neovim.io/doc/user/pack.html#vim.pack)

本文档介绍了如何在 Neovim 中使用“包”来管理插件。“包”是包含插件的目录，具有易于下载、更新（尤其是从 Git 等仓库）和组织等优点。它们可以包含多个相互依赖的插件，并可自动在启动时加载（`pack/*/start/*` 中的“start”包）或按需使用 `:packadd` 加载（`pack/*/opt/*` 中的“opt”包）。

Neovim 在这些包目录中搜索运行时文件。可以使用 `nvim_list_runtime_paths()` 和 `nvim_get_runtime_file()` 来列出目录和查找文件。`:packloadall` 会提前加载所有 start 包。

本文档详细介绍了如何安装和构建包，包括单个插件，以及如何通过 `:packadd`（或使用 `packadd!` 在启动时加载）使用可选插件。它建议将配色方案放在 `pack/*/opt` 中，将文件类型插件放在 `pack/*/start` 中。

它进一步解释了如何创建用于分发的包，建议将插件组织到具有适当文件结构的 start 和 opt 目录中，以存放插件、自动加载函数和文档。`:helptags` 命令对于生成帮助标签非常重要。

最后，本文档介绍了 `vim.pack`，Neovim 内置的插件管理器（正在开发中）。该工具使用 Git 在专用目录中管理插件，至少需要 Git 2.36。它包括用于添加 (`vim.pack.add()`)、删除 (`vim.pack.del()`) 和更新 (`vim.pack.update()`) 插件的函数，并提供用于基本管理、版本切换和冻结插件的示例工作流程。该管理器可以挂钩到插件状态更改前后的事件。

---

## 32. 苦涩的教训被误解了

**原文标题**: The Bitter Lesson Is Misunderstood

**原文链接**: [https://obviouslywrong.substack.com/p/the-bitter-lesson-is-misunderstood](https://obviouslywrong.substack.com/p/the-bitter-lesson-is-misunderstood)

无法访问该文章链接。

---

## 33. AR流体模拟演示

**原文标题**: AR Fluid Simulation Demo

**原文链接**: [https://danybittel.ch/fluid](https://danybittel.ch/fluid)

丹尼·比特尔的“AR流体模拟演示”探索了计算机生成的流体模拟与增强现实中真实世界物体的互动。比特尔使用安装在屏幕上方的网络摄像头，并配有偏振滤镜以防止反馈，来捕捉放置在屏幕前真实物体的形状。捕捉到的视频流随后与计算机生成的模拟对齐，使流体能够对这些物体做出动态反应，从而有效地创造出AR体验。

值得注意的是，该装置能够识别手作为障碍物，比特尔最初认为这是一个副作用，但最终发现这是互动中一个令人愉快的元素。流体模拟本身是基于风洞式模型，灵感来自Tidepodious的解释和演示。该项目有效地展示了一种融合虚拟和现实世界环境的新颖方法，允许用户通过真实物体和手势与流体模拟进行互动。该演示的版权归丹尼·比特尔所有，2025年。

---

## 34. 330+数据团队分享有效（和无效）的方法

**原文标题**: 330+ data teams share what's working (and what's not)

**原文链接**: [https://www.metabase.com/data-stack-report-2025](https://www.metabase.com/data-stack-report-2025)

本文档是《2025年Metabase社区数据栈报告》的摘要，利用了来自超过330个数据团队的数据。该报告旨在深入了解现代数据栈的优点和不足。它允许读者探索详细结果，并鼓励在其网络内分享该报告。虽然摘要未明确具体发现，但该报告可能涵盖以下内容：

*   **流行且有效的数据工具：** 识别数据生态系统中各种工具的采用和满意度趋势。
*   **挑战和痛点：** 突出数据团队在构建、维护和利用其数据基础设施时面临的常见困难。
*   **最佳实践和策略：** 分享高绩效数据团队采用的成功方法和策略。
*   **未来趋势：** 提供有关数据栈不断变化的趋势的预测和观察。

该报告的价值在于提供社区来源的数据栈视角，使数据专业人员能够评估自己的设置，学习他人的经验，并就其工具和策略做出明智的决策。

---

## 35. 逆向工程Solos智能眼镜

**原文标题**: Reverse engineering Solos smart glasses

**原文链接**: [https://jfloren.net/b/2025/8/28/0](https://jfloren.net/b/2025/8/28/0)

约翰·弗洛伦逆向工程了一副原本面向自行车手和跑步者销售的Solos智能眼镜，使其能够显示自定义图像。由于该眼镜缺乏市场欢迎度，他以低廉的价格购得，并在向Solos公司索取文档未果后，决定对其进行破解。

他的方法包括捕获眼镜和配套应用程序之间的蓝牙流量。通过分析捕获的数据，他识别出包含使用行程长度编码（RLE）和RGB 5:6:5颜色编码的图像数据的包的模式。他破译了数据包的结构，识别出幻数、绘图模式选择、RLE数据长度、x/y偏移量和x/y尺寸。

弗洛伦发现数据传输存在一种奇特的加倍现象，并在他的逆向工程中对此进行了调整。然后，他开发了一个Python脚本，将图像文件转换为RLE编码的数据，并通过蓝牙将其传输到眼镜。

他成功地显示了自定义图像，包括家庭环境状况的显示，甚至是一张完整的照片，证明了他可以控制显示。他认为他的工作可以用来显示有用的信息，如电子邮件主题、天气预报或服务器状态。他的下一步计划包括建立管道以自动生成和推送图像。他还注意到设备中存在麦克风和扬声器，他希望在未来的实验中激活它们。重要的是，他强调他的破解是非破坏性的。

---

## 36. Show HN: 在Notepad++中运行的Roguelike游戏

**原文标题**: Show HN: A roguelike game that runs inside Notepad++

**原文链接**: [https://github.com/thelowsunoverthemoon/NeuroPriest](https://github.com/thelowsunoverthemoon/NeuroPriest)

此“Show HN”帖子介绍了一款作为Notepad++插件构建的roguelike/rogue-lite游戏。该游戏包含六个关卡的回合制游戏玩法，允许玩家收集圣物、击败Boss、避开陷阱，并包含故事情节和音频。

该帖子包含关于潜在数据丢失或设置损坏的警告，指出它仅在安装了Notepad++ 8.6.8版本的64位Windows 10和11上进行了测试。

提供了安装说明，要求用户：

1. 下载并解压缩最新版本。
2. 安装提供的字体。
3. 将提供的主题添加到Notepad++。
4. 将插件添加到Notepad++。
5. 在插件菜单中按“PLAY”（可能需要管理员模式）。

---

## 37. Nuclear：专注于从免费源流媒体播放的桌面音乐播放器

**原文标题**: Nuclear: Desktop music player focused on streaming from free sources

**原文链接**: [https://github.com/nukeop/nuclear](https://github.com/nukeop/nuclear)

Nuclear：一款免费开源的桌面音乐播放器，旨在从互联网上的免费资源流式传输音乐。它类似于mps-youtube，但具有GUI，提供类似Spotify的体验，无需订阅。

**重要提示：**当前版本已停止维护，可能存在功能失效。一个名为Nuclear-XRD的完整重写项目正在进行中，以解决这些问题，并带来以下改进：

*   播放器和插件的自动更新。
*   从Electron迁移到Tauri。
*   使用Rust进行性能增强。
*   主题支持。
*   强大的插件系统。
*   为插件开发者提供更好的工具。
*   扩展对元数据和流媒体提供商的支持。

**当前版本的关键特性包括：**

*   从YouTube、Jamendo、Audius和SoundCloud流式传输音乐。
*   专辑搜索（由Last.fm和Discogs提供支持）。
*   播放列表管理（保存/加载）。
*   Last.fm记录。
*   带有评论的新版本发现。
*   流派浏览。
*   电台模式（自动相似曲目队列）。
*   从YouTube无限下载。
*   实时歌词。
*   按受欢迎程度浏览。
*   收藏曲目列表。
*   本地库支持。
*   音频标准化。

该项目欢迎贡献，并提供贡献指南。社区维护的软件包适用于各种软件包管理器（AUR、Choco、Homebrew、Snap、Flatpak等）。社区翻译通过Crowdin进行管理。该软件在GNU Affero通用公共许可证v3下获得许可。

---

## 38. 使用极简示例理解Transformer

**原文标题**: Understanding Transformers Using a Minimal Example

**原文链接**: [https://rti.github.io/gptvis/](https://rti.github.io/gptvis/)

本文通过可视化一个在极简的水果口味关系数据集上训练的，经过大幅简化的仅解码器模型的内部状态，来解释 Transformer 的工作原理。简化涉及训练数据（94 个训练词，7 个验证词）、分词（简单的单词分割，产生 19 个词汇）和模型架构（2 层，2 个注意力头，20 维的绑定嵌入）。这使得可以对模型的内部过程进行详细的、逐步的可视化。

文章重点介绍了模型如何学习标记之间的语义联系，例如，在验证集中，它成功地在 "i like spicy so i like" 提示后预测了 "chili"。

可视化包括用堆叠的盒子表示的标记嵌入，显示了相关标记之间的独特和共享的视觉属性（例如，口味标记）。文章还可视化了前向传递，跟踪标记向量如何通过层转换，最终使最终 "like" 标记的向量与 "chili" 嵌入非常相似。

最后，文章解释并可视化了注意力机制，展示了标记如何选择性地关注前面的标记以纳入相关的上下文。例如，标记 "spicy" 关注 "i"，输入序列中的最后一个 "like" 强烈关注 "spicy"，从而使模型能够预测 "chili"。这种简化提供了对 Transformer 内部信息流和上下文理解的有价值的见解。

---

## 39. 用500行Python代码编写C编译器 (2023)

**原文标题**: Writing a C compiler in 500 lines of Python (2023)

**原文链接**: [https://vgel.me/posts/c500/](https://vgel.me/posts/c500/)

本文详细介绍了作者用 500 行 Python 代码创建 C 编译器 c500 的项目。作者为了控制代码行数，选择了单遍编译方法，在解析过程中生成代码，而不是构建抽象语法树。该编译器以 WebAssembly 为目标，这个决定带来了一些独特的挑战，包括缺少 `goto` 指令和由于 WebAssembly 堆栈的限制，需要管理一个单独的 C 堆栈。

错误处理非常简单，使用一个简单的 `die` 函数来报告错误。该编译器实现了一部分 C 语言特性，包括算术运算、`int`、`short` 和 `char` 类型、字符串常量、指针、单级数组、函数和 typedef，同时省略了结构体、枚举、预处理器指令、浮点类型和某些其他次要特性。

本文重点介绍了使用的关键数据结构和类：用于生成 WebAssembly 代码的 `Emitter`，用于管理字符串常量的 `StringPool`，用于标记输入（包括处理类型信息的“lexer hack”）的 `Lexer`，用于表示 C 类型的 `CType`，用于管理 C 堆栈的 `FrameVar` 和 `StackFrame`，以及用于跟踪表达式是值还是位置（地址）的 `ExprMeta`，从而能够正确处理 `&` 和 `+` 等操作。该编译器成功编译并运行了一个简单的斐波那契数列程序，证明了其功能。

---

## 40. 新的结理论发现推翻长期以来的数学假设

**原文标题**: New knot theory discovery overturns long-held mathematical assumption

**原文链接**: [https://www.scientificamerican.com/article/new-knot-theory-discovery-overturns-long-held-mathematical-assumption/](https://www.scientificamerican.com/article/new-knot-theory-discovery-overturns-long-held-mathematical-assumption/)

《科学美国人》文章讨论了纽结理论的最新突破，该突破推翻了一个长期存在的猜想。 近一个世纪以来，数学家们一直认为，由两个较小纽结连接而成的纽结的复杂性（用“解结数”衡量，即解开一个纽结所需的最少切割和重新连接次数）将是各个纽结复杂性的总和。

研究人员马克·布里滕汉姆和苏珊·赫米勒通过构建一个由两个较简单纽结组成的纽结，证明了这一猜想是错误的，其中组合纽结的解结数低于其各部分的总和。 他们将解结数为 3 的纽结与其镜像连接起来，预计组合解结数为 6。 然而，他们证明只需五步甚至更少的步骤就可以解开它。

这一发现挑战了现有的纽结复杂性概念，并对更广泛的拓扑学领域产生了影响，拓扑学在理解 DNA 缠绕、蛋白质结构和分子稳定性方面具有实际应用。 这项工作强调了看似简单的结构，例如纽结，也可能蕴藏着意想不到的数学复杂性。

---

## 41. 开发Dia和Arc浏览器的公司将被收购。

**原文标题**: The company behind the Dia and Arc browsers is being acquired

**原文链接**: [https://www.theverge.com/web/770947/browser-company-arc-dia-acquired-atlassian](https://www.theverge.com/web/770947/browser-company-arc-dia-acquired-atlassian)

Atlassian将以6.1亿美元现金收购Arc和Dia浏览器的制造商The Browser Company。这笔交易源于Atlassian认为人工智能和浏览器对于未来的工作至关重要。虽然Arc广受欢迎，但此次收购主要集中于The Browser Company的新型人工智能浏览器Dia。Dia将聊天机器人直接集成到浏览体验中，允许用户以新的方式与标签和应用程序互动，这与Atlassian的Jira和Confluence等工作应用程序套件相一致。

The Browser Company首席执行官Josh Miller表示，Atlassian的兴趣源于企业准备需求和人工智能集成的潜力。虽然Dia将专注于与工作相关的任务，但Miller保证它仍将面向个人用户，而不仅仅是企业IT管理。他认为人工智能浏览器领域的竞争将在未来12-24个月内决出胜负，而Atlassian的资源提供了竞争所需的必要分销和规模。

虽然有些人可能将此次收购视为一种退却，但Miller认为这是在激烈竞争中确保Dia未来的方式。Atlassian的稳定性使The Browser Company能够专注于用户增长。虽然Arc将被维护，但随着重点转移到Dia，其开发可能会放缓。最终，The Browser Company认为浏览器是与计算机交互的强大方式，这一概念得到了谷歌和OpenAI等主要参与者对人工智能驱动浏览器日益增长的兴趣的证实。此次收购为The Browser Company提供了在这个快速发展的市场中获胜所需的销售和支持基础设施。

---

## 42. 人工智能目前对就业市场影响不大，纽约联储称

**原文标题**: AI Not Affecting Job Market Much So Far, New York Fed Says

**原文链接**: [https://money.usnews.com/investing/news/articles/2025-09-04/ai-not-affecting-job-market-much-so-far-new-york-fed-says](https://money.usnews.com/investing/news/articles/2025-09-04/ai-not-affecting-job-market-much-so-far-new-york-fed-says)

无法访问文章链接。

---

## 43. 鳗鱼是鱼

**原文标题**: Eels are fish

**原文链接**: [https://eocampaign1.com/web-version?p=495827fa-8295-11f0-8687-8f5da38390bd&pt=campaign&t=1756227062&s=033ffe0494c7a7084332eb6e164c4feeeb6b4612e0de0df1aa1bf5fd59ce2d08](https://eocampaign1.com/web-version?p=495827fa-8295-11f0-8687-8f5da38390bd&pt=campaign&t=1756227062&s=033ffe0494c7a7084332eb6e164c4feeeb6b4612e0de0df1aa1bf5fd59ce2d08)

鳗鱼奇妙而神秘的生命周期：弗兰克·奇梅罗的 newsletter 探索了鳗鱼奇妙而神秘的生命周期，揭示了它们确实是鱼类，尽管是非常奇特的鱼类。几个世纪以来，它们的起源一直不为人知，导致了各种神话，包括亚里士多德认为它们是从泥土中产生的。该 newsletter 重点介绍了西格蒙德·弗洛伊德寻找鳗鱼睾丸的未果之旅，这是对他后来揭示隐藏的人类性行为的一种喜剧性和讽刺性的先兆。

意大利动物学家乔瓦尼·巴蒂斯塔·格拉西将柳叶鳗幼虫与鳗鱼联系起来，鳗鱼繁殖的秘密才开始解开。现在，科学家们认为鳗鱼出生时是微小的、玻璃状的幼虫，生活在马尾藻海，漂流数年，然后变成玻璃鳗并逆流而上进入欧洲河流。然后它们变成鳗线，接着是黄鳗，在淡水环境中成熟数十年。最后，它们经历银化转变，发育出繁殖器官和更大的眼睛，并踏上返回马尾藻海产卵和死亡的漫长旅程。

作者将鳗鱼和鲑鱼的生命周期进行了比较，对比了它们在河流和海洋之间相反的迁徙。鳗鱼的一生充满了不断的转变和隐藏的深度，难以简单解释，最终回归大海，守护着它的秘密。

---

## 44. Hledger 1.50

**原文标题**: Hledger 1.50

**原文链接**: [https://github.com/simonmichael/hledger/releases/tag/1.50](https://github.com/simonmichael/hledger/releases/tag/1.50)

本文档详细介绍了命令行会计工具Hledger 1.50版本的发布。主要亮点包括：为了提高准确性，对交易平衡进行了重大更改，需要通过调整精度或添加舍入条目来修复现有的账簿。旧的平衡行为可以通过一个标志临时使用。时间时钟语法和解析更加稳健。此版本还需要 GHC 9.6 或更高版本。

修复包括分页错误、查询逻辑、包含指令错误、CSV规则中的大小写不敏感问题以及正确的历史余额报告。

新功能包括在CSV规则中运行shell命令以进行数据清理和自动归档导入的CSV数据文件。改进涵盖命令行帮助、插件命令用法、智能日期、使用标签进行帐户匹配、稳健的包含指令glob模式、自动过账帐户插值以及对各种命令（如`aregister`、`commodities`、`payees`和`tags`）的增强。

此版本还将Hledger-UI和Hledger-Web更新到1.50版本，包括Hledger-Web中图表日期选择的拖动改进。项目变更包括文档更新和基础设施改进，以及对贡献者的鸣谢。提供了适用于各种平台（包括GNU/Linux、Mac和Windows）的安装说明。

---

## 45. 谷歌在东欧和土耳其宕机

**原文标题**: Google was down in eastern EU and Turkey

**原文链接**: [https://www.novinite.com/articles/234225/Google+Down+in+Eastern+Europe+%28UPDATED%29](https://www.novinite.com/articles/234225/Google+Down+in+Eastern+Europe+%28UPDATED%29)

2025年9月4日，谷歌服务大范围中断，影响了东欧和土耳其的用户。来自保加利亚、土耳其和希腊等国的报告涌入，表明重要的谷歌产品出现大范围中断。

受影响的服务包括YouTube（无法加载视频）、谷歌地图（无法加载数据、搜索或计算路线）、谷歌搜索（返回错误或无法完成搜索）、Gmail（发送/接收电子邮件出现问题）以及Google Drive（访问文件中断）。用户遇到“5xx服务器错误”，表明问题出在谷歌方面。

本次中断并非普遍影响所有谷歌服务，而是针对那些对工作和日常生活至关重要的服务。文章建议使用必应、雅虎、DuckDuckGo和Brave Search等替代搜索引擎作为临时解决方案。文章提到该事件仍在发展中，并承诺随着更多信息和谷歌的官方回应发布，会提供更新。一篇相关文章强调了影响包括保加利亚在内的47个国家的大规模谷歌中断，服务正在缓慢恢复。

---

## 46. 成为一只蝙蝠是怎样的体验？

**原文标题**: What is it like to be a bat?

**原文链接**: [https://en.wikipedia.org/wiki/What_Is_It_Like_to_Be_a_Bat%3F](https://en.wikipedia.org/wiki/What_Is_It_Like_to_Be_a_Bat%3F)

托马斯·内格尔1974年的论文《成为一只蝙蝠是什么感觉？》是意识研究的基石，探讨了经验的主观本质并挑战了还原论的唯物主义。内格尔认为，意识的定义是“成为该生物是怎样的”，这是一种主观特征，无法完全用客观的物理过程来解释。

他以蝙蝠为例，这种生物具有独特的感官体验（回声定位），来说明即使我们完全了解蝙蝠大脑的物理结构，我们也无法真正知道*成为*一只蝙蝠的*感受*是什么。这突出了客观和主观视角的差异，客观性寻求一种公正的视角，但人类天生受到主观经验的限制。

内格尔认为，经验的这种主观性破坏了通过还原论手段解释意识的尝试。物理主义认为精神状态是物理状态，也因其对客观和主观经验的不完整描述而受到质疑。

这篇论文影响深远，但也面临批评。丹尼尔·丹尼特认为，通过第三人称观察可以获得蝙蝠意识在理论上重要的特征。其他人则认为，内格尔过快地否定了神经科学细节回答他问题的潜力，或者问题本身就存在缺陷。尽管存在批评，内格尔的论文仍然是对理解意识的复杂性和身心问题的重要贡献。

---

## 47. 在 Alpine 上半年：除了 musl 之外

**原文标题**: Half an year on Alpine: just musl aside

**原文链接**: [https://blog.jutty.dev/posts/half-an-year-on-alpine/](https://blog.jutty.dev/posts/half-an-year-on-alpine/)

作者回顾了他们使用 Alpine Linux 作为日常操作系统六个月的经历，并将其与之前的 Void Linux 系统进行了比较。 最初，他们寻求一个稳定、非滚动更新的发行版，其 init 系统比 systemd 更简单，这使得他们选择了使用 OpenRC init 的 Alpine。

虽然作者称赞 Alpine 的速度、精简的资源占用、优秀的包管理器和整体设计原则，但他们主要担心的是它使用了 musl libc，这导致了与为 glibc 设计的软件的兼容性问题。 尽管尝试了诸如 gcompat、Flatpak 和手动编译等解决方法，但与这些方法相关的摩擦最终证明令人疲惫，特别是对于实验性和新颖的软件使用而言。

作者承认，由于其小尺寸以及 musl 在这些环境中的优势，Alpine 在虚拟化和嵌入式系统中表现出色，但对于他们的桌面需求而言，这种兼容性牺牲是不值得的。 尽管对 Alpine 本身没有任何具体的抱怨，但他们表达了对基于 glibc 的 Alpine 的渴望，但这并不存在。

作者最后强调了从使用 Alpine 中获得的学习经验，特别是对 OpenRC、BusyBox 以及所需最小设置的理解。 他们计划重新使用 Void Linux，如果稳定性问题持续存在，则考虑切换到 Debian，并可能为了更大的兼容性和稳定性而放弃对 systemd 的厌恶。 作者强调希望有一个实用、不那么耗时的设置来促进其他操作系统任务。

---

## 48. 使用AI生成的Metal内核加速在Apple设备上的PyTorch推理

**原文标题**: Speeding up PyTorch inference on Apple devices with AI-generated Metal kernels

**原文链接**: [https://gimletlabs.ai/blog/ai-generated-metal-kernels](https://gimletlabs.ai/blog/ai-generated-metal-kernels)

本文探讨了使用AI生成的Metal内核来加速苹果设备上PyTorch推理的潜力。作者研究了前沿AI模型是否能自动为苹果的Metal框架编写优化的GPU内核，从而克服手动调整内核的挑战，尤其是在CUDA生态系统之外。

结果令人鼓舞：与苹果M4 Max芯片上的基线PyTorch实现相比，AI生成的Metal内核在215个PyTorch模块上平均实现了87%的加速（快1.87倍）。在某些情况下，速度提升幅度从10倍到100倍不等。这些模型甚至在某些情况下识别并消除了算法上不必要的操作。

该研究涉及来自Anthropic、DeepSeek和OpenAI的八个前沿模型，并使用KernelBench数据集进行测试。研究人员最初实现了一个简单的迭代代理，该代理生成Metal内核，检查其正确性，并根据错误反馈重新尝试。正确率随着多次尝试而提高，GPT-5在生成更快的Level 2内核实现方面表现出特别的成功。文章还重点介绍了一个案例，GPT-5通过融合内核，使Mamba状态空间模型实现了4.65倍的加速。该研究表明，AI可以自动化各种平台的内核优化，从而可能显著提高苹果设备的性能。

---

## 49. 我本应热爱电气工程

**原文标题**: I Should Have Loved Electrical Engineering

**原文链接**: [https://blog.tdhttt.com/post/love-ee/](https://blog.tdhttt.com/post/love-ee/)

本文讲述了作者本科期间学习计算机科学与工程（CSE）的经历，以及最终转向计算机科学与物理的转变。最初，受SixthSense项目和改进人机交互的愿望所启发，作者选择了CSE，希望学习硬件和软件。

然而，作者发现工程课程枯燥乏味，侧重于死记硬背，这与他们最初对突破性创新的期望形成鲜明对比。受挫之下，他们挂了两门工程课。课外的工程项目，如遥控车套件和微型鼠，也没能点燃他们的热情。

另一方面，作者在软件开发方面表现出色，发现它具有立竿见影的效果和可扩展性。他们创建了一个课程注册工具，并为研究项目做出了贡献，精通了Docker等工具，甚至与NASA和CERN合作。这种成功激发了他们对物理学的热情，并让他们清楚地认识到：学术工程与现实创新之间存在着“高墙”。作者认为，软件提供了更多使用尖端技术和创造切实影响的机会。

最终，作者将专业转为计算机科学和物理学，从软件开发的自由和即时反馈以及物理学的理论深度中找到了满足感。虽然他们承认本可以探索更多令人兴奋的工程机会，但他们最终对自己的决定感到满意，仍然相信改进人机交互的重要性，但选择通过软件的视角来实现。

---

## 50. 大型语言模型面临的壁垒

**原文标题**: The wall confronting large language models

**原文链接**: [https://arxiv.org/abs/2507.19703](https://arxiv.org/abs/2507.19703)

Peter V. Coveney 和 Sauro Succi 发表在 arXiv 上的文章 (2507.19703v2) 题为“大型语言模型面临的壁垒”，认为大型语言模型 (LLM) 缩放规律的根本局限性严重限制了它们提高预测不确定性和达到科学探究所需可靠性的能力。作者认为，赋能 LLM 的机制——从高斯输入生成非高斯输出分布——很可能是误差累积、信息灾难和退化性 AI 行为的根本原因。

他们认为，学习和准确性之间的这种张力导致了观察到的缩放分量的低值。此外，正如 Calude 和 Longo 所强调的那样，大型数据集中虚假相关性的增加加剧了这个问题，这些虚假相关性仅仅是由于数据的大小而产生，与数据的质量无关。

作者强调，LLM 领域内退化性 AI 的可能性并不意味着它在未来的 AI 研究中不可避免。他们提倡转向优先考虑洞察力，并更深入地理解所解决问题的结构特征，以此来避免这种退化性途径。本质上，该论文认为，简单地扩大 LLM 规模并不是通往可靠 AI 的可持续道路，需要一种更加细致、以洞察力驱动的方法。

---

## 51. 多环芳烃

**原文标题**: Polycyclic Aromatic Hydrocarbons

**原文链接**: [https://johncarlosbaez.wordpress.com/2025/09/01/polycyclic-aromatic-hydrocarbons/](https://johncarlosbaez.wordpress.com/2025/09/01/polycyclic-aromatic-hydrocarbons/)

本文探讨了多环芳烃（PAHs），这是一种由六边形碳环和连接的氢原子组成的复杂分子。多环芳烃最初是在太空中的红矩形星云中发现的，红矩形星云是由两颗恒星释放冰尘和碳氢化合物形成的结构。它们是通过含碳材料的不完全燃烧形成的，存在于地球上的烟尘和焦油中，也存在于外太空。

本文首先提供了简单的多环芳烃的例子，如苯和萘，然后介绍了更复杂的结构，如蒽、芘和屈。作者强调了多环芳烃在星际空间中的丰富性和重要性，估计它们约占星际碳的10%。它们的稳定性使它们即使在超新星冲击波等极端环境中也能存在。多环芳烃也存在于碳质球粒陨石中，在这些陨石中，它们占碳含量的80%。

本文最后提到了“多环芳烃世界假说”，该假说认为多环芳烃可能作为地球生命的先驱发挥了关键作用，并引用了对Pascale Ehrenfreund关于该主题的采访。

---

## 52. 梅尔文·布拉格卸任《我们的时代》主持人

**原文标题**: Melvyn Bragg steps down from presenting In Our Time

**原文链接**: [https://www.bbc.co.uk/mediacentre/2025/melvyn-bragg-decides-to-step-down-from-presenting-in-our-time/](https://www.bbc.co.uk/mediacentre/2025/melvyn-bragg-decides-to-step-down-from-presenting-in-our-time/)

梅尔文·布拉格将卸任BBC Radio 4“我们的时代”节目主持人，此前他主持了自1998年开播以来的每一集。2025年9月3日发布的这一消息标志着布拉格长达四分之一个世纪的主持生涯结束，他主持了该热门节目的1000多集。

布拉格对BBC的贡献超过60年，始于1961年。他还曾在1988-1998年间主持Radio 4的“一周开始”节目，并参与了众多艺术和文化节目的制作。他将继续与BBC合作未来的项目，包括2026年的新系列节目。

BBC总干事蒂姆·戴维赞扬了布拉格的求知欲和对公共服务广播的承诺，强调了他为广播带来的深度和见解。Radio 4总监莫希特·巴卡亚指出了布拉格独特的遗产和他留下的宝贵的存档节目。

“我们的时代”是一档非常受欢迎的BBC节目和播客，即使在年轻听众中也很受欢迎。该节目以与顶尖学者就各种话题进行的对话为特色。

为了庆祝布拉格的任期，Radio 4将播出他最喜欢的一些剧集，并且精选内容将在BBC Sounds上提供。“我们的时代”节目将由一位新主持人回归，主持人将在稍后公布。

---

## 53. 威廉·华兹华斯的信：“版权法”（1838）

**原文标题**: William Wordsworth's letter: "The Law of Copyright" (1838)

**原文链接**: [https://gutenberg.org/cache/epub/76806/pg76806-images.html](https://gutenberg.org/cache/epub/76806/pg76806-images.html)

本文档是威廉·华兹华斯于1838年4月18日所写的一封信，题为“著作权法”。此信写给议员塞尔吉特·塔尔福德，以支持塔尔福德提出的修订著作权法的议案。该信最初于1838年4月23日发表在《晨邮报》上，后被重新发现。信中表达了华兹华斯对延长作者及其继承人著作权保护期的支持。

华兹华斯解释说，有人敦促他向议会请愿支持该议案，但他由于厌恶公众关注以及认为该事业的正义性应该是不言自明的，因此犹豫不决。他认为，作者应该永久拥有著作权，他认为这是英国普通法所承认的权利。他批评那些反对该议案的印刷商和出版商，认为他们的体面和存在归功于作者。

华兹华斯断言，文学财产的权利比其他形式的财产更为内在。虽然他拒绝正式向议会请愿，但他公开声明支持塔尔福德的努力。他强调了塔尔福德的演讲以及在公共期刊上提出的论点，认为这些都是对该议案的有效辩护。他最后表示感谢塔尔福德及其同事，无论该议案的结果如何，他都相信正义最终会获胜。

---

## 54. 我们已经生活在社会信用体系中了，只是我们不这么称呼它。

**原文标题**: We already live in social credit, we just don't call it that

**原文链接**: [https://www.thenexus.media/your-phone-already-has-social-credit-we-just-lie-about-it/](https://www.thenexus.media/your-phone-already-has-social-credit-we-just-lie-about-it/)

本文认为，尽管西方社会并未明确称之为“社会信用体系”，但实际上已经以某种形式运行着类似的系统。作者指出，优步、Instagram、领英、亚马逊和银行应用程序等平台上的算法，都在不断地追踪、评分，并根据用户的行为奖励或惩罚他们，从而影响他们获得服务、机会和社会地位。

文章将此与人们普遍认为的中国社会信用体系形成对比，后者通常被描绘成奥威尔式的噩梦。作者认为，中国的现实更为复杂，大多数全国范围内的私人评分系统已被关闭，个人评分仅限于小型试点城市。此外，中国在评分标准方面更加透明，而西方系统则依赖于“黑盒”算法。

作者指出，西方体系虽然是分散的，但它们之间的联系日益紧密，并可能演变成全面的社会信用体系。作者在承认与政府控制系统相关的风险的同时，认为由于高转换成本、数据共享和政府访问权限，企业系统已经非常强大。文章最后得出结论：关键问题不是西方社会是否会采用社会信用，而是它们是否会对此保持透明和负责任，而不是假装这些系统仅仅是中立的技术。作者建议，即使受到中国做法的启发，提高透明度最终可以通过让游戏规则可见来赋予个人权力。

---

## 55. 空客B612驾驶舱字体

**原文标题**: Airbus B612 Cockpit Font

**原文链接**: [https://github.com/polarsys/b612](https://github.com/polarsys/b612)

PolarSys B612字体家族是一款开源字体，专为在飞机驾驶舱屏幕上实现最佳易读性而设计。它由空中客车公司、法国国立民航大学和图卢兹第三大学合作创建，旨在提高驾驶舱信息显示的清晰度和同质性。

Intactile DESIGN开发了B612的八种字体变体，确保所有字符都具有完整的微调。该字体的设计优先考虑最大化字符间距、尊重字母原型以及协调形状和间距。

发布新版本的流程包括更新源文件中的版本号、合并交叉点、生成TTF文件，以及使用构建脚本修复数字签名。

该字体由空中客车公司 (airbus-group.com) 拥有版权，并根据 Eclipse Public License v2.0、Eclipse Distribution License v1.0 和 SIL Open Font License v1.1 许可，允许根据这些许可的条款使用和修改。

---

## 56. ReMarkable 纸张专业版移动方案

**原文标题**: ReMarkable Paper Pro Move

**原文链接**: [https://remarkable.com/products/remarkable-paper/pro-move](https://remarkable.com/products/remarkable-paper/pro-move)

reMarkable Paper Pro Move 是一款便携式“纸质平板电脑”，专为无干扰的笔记记录和文档管理而设计。它配备 7.3 英寸彩色显示屏，具有类似纸张的书写触感，阅读灯适用于任何光照条件，电池续航时间长达两周。

该设备强调自然的书写体验，模仿笔和纸，并提供数字工具，如手写转换、作品的选择/移动和图层。它与磁性吸附的 Marker (单独出售) 集成，并提供文件夹和标签等组织功能，以实现高效的文件管理和快速搜索。Connect 订阅提供云存储、跨设备（笔记本电脑和移动应用程序）访问笔记和文档、手写搜索、独家模板以及 Slack 集成。

Paper Pro Move 采用耐用的铝制框架和纹理玻璃显示屏，并注重环保，使用回收材料并设计为可维修。它包含数据加密以确保安全。该设备随附 Marker、USB-C 充电线和替换笔尖。保护套和其他配件可供购买。

文章还解答了关于支付/运输、支持/退货（包括 100 天满意保证）、使用和规格的常见问题。它强调了 Paper Pro Move 与其他 reMarkable 设备之间的区别。

---

## 57. 打造世界上最精确的自制数控车床[视频]

**原文标题**: Building the most accurate DIY CNC lathe in the world [video]

**原文链接**: [https://www.youtube.com/watch?v=vEr2CJruwEM](https://www.youtube.com/watch?v=vEr2CJruwEM)

文章是一个YouTube视频，标题为“打造世界上最精确的DIY CNC车床”。可用内容极少，仅包含通常位于网站底部的标准YouTube样板文字。这些样板文字包括指向版权、新闻、广告、开发者资源、服务条款、隐私政策、安全性以及有关YouTube运作方式等各种主题的链接。它还提到了NFL Sunday Ticket和Google LLC。

由于除了标题和YouTube样板文字之外缺乏实质性内容，因此无法进行真正的总结。我们知道该视频的主题是构建高度精确的DIY CNC车床，暗示着对工程、机械加工以及可能的开源硬件的关注。但是，在没有更多信息的情况下，总结仅限于说明该视频旨在展示据称高度精确的DIY CNC车床的构建。其余的只是标准的YouTube法律和信息文本。

---

## 58. Lit：构建快速、轻量级 Web 组件的库

**原文标题**: Lit: a library for building fast, lightweight web components

**原文链接**: [https://lit.dev](https://lit.dev)

Lit 是一个轻量级的 JavaScript 库，用于构建快速且可互操作的 Web 组件。它利用 Web 组件标准，并增加了诸如响应式、声明式模板和作用域样式等功能，以简化开发并减少样板代码。

使用 Lit 的主要优势包括：

*   **体积小，渲染快：** Lit 占用空间小（约 5KB），并使用高效渲染，仅更新 UI 的动态部分，从而实现更快的性能。
*   **符合 Web 组件标准：** Lit 组件是原生 Web 组件，确保与任何框架或完全没有框架的互操作性，使其成为可共享组件和设计系统的理想选择。
*   **易于使用：** Lit 提供基于 JavaScript 标记模板字面量的声明式模板，可以轻松创建带有内联 JavaScript 表达式的 HTML 标记。
*   **作用域样式：** Lit 自动使用 Shadow DOM 来限定样式的作用域，防止 CSS 冲突并简化 CSS 管理。
*   **响应式属性：** 响应式属性允许组件在其数据更改时高效地重新渲染。

Lit 适用于构建可共享组件、设计系统以及整个网站和应用程序。它被许多组织和开源项目使用。教程、文档和 Playground 等资源可帮助开发者入门。Lit 社区可以通过 Discord、Bluesky、Github 和 Stack Overflow 进行互动。

---

## 59. 我们将加入 OpenAI。

**原文标题**: We're Joining OpenAI

**原文链接**: [https://www.alexcodes.app/blog/alex-team-joins-openai](https://www.alexcodes.app/blog/alex-team-joins-openai)

iOS & MacOS应用AI编程助手"Alex"的开发者Daniel宣布其团队加入OpenAI的Codex团队。Daniel对打造Alex深感自豪，尤其是在Xcode缺乏AI能力之初。他很高兴能以更大规模为OpenAI的使命做出贡献，帮助人们创造。

公告阐述了Alex的未来：现有用户服务将继续，但新下载将于10月1日停止，且不再发布新功能。

Daniel感谢早期测试用户、客户、投资者和Apple开发社区的支持。他最后鼓励读者探索Codex CLI，并重申了“创造美好事物”的愿望。本质上，Alex将被整合到OpenAI的工作中，利用现有的代码库和专业知识来增强Codex的AI编程能力。

---

## 60. 使用贝叶斯法则机械地解决概率谜题

**原文标题**: Use Bayes rule to mechanically solve probability riddles

**原文链接**: [https://cloud.disroot.org/s/Ec4xTMFDteTrFio](https://cloud.disroot.org/s/Ec4xTMFDteTrFio)

根据标题“用贝叶斯定理机械地解决概率谜题”以及只有一个看似空白的文件“bayes1.md”的事实，我们可以推断出其可能的内容，并概括如下：

本文可能旨在演示如何系统地应用贝叶斯定理来解决概率谜题和文字问题。核心思想是提供一种结构化的方法来应用贝叶斯公式，超越直觉，从而实现更可靠、更不易出错的方法。

本文可能会解释：

*   **贝叶斯定理：** 简要回顾贝叶斯定理公式：P(A|B) = [P(B|A) * P(A)] / P(B)。解释了如何在给定证据（B）的情况下更新假设（A）的概率。

*   **识别组成部分：** 一个关键步骤包括从谜题的上下文中识别先验概率 (P(A))、似然度 (P(B|A))、边缘概率 (P(B)) 和后验概率 (P(A|B))。

*   **机械应用：** 该方法可能会提倡一种“机械”应用，即将问题分解为清晰的步骤：
    1.  精确地定义事件 A 和 B。
    2.  识别并赋值 P(A)、P(B|A) 和 P(B)。
    3.  将这些值代入贝叶斯定理公式。
    4.  计算结果。

*   **例题：** 本文很可能会提供概率谜题的例子，并演示如何使用贝叶斯定理的结构化方法来解决这些问题。

*   **优点：** 本文可能会强调使用这种机械方法的优点，例如减少错误、提高对问题的理解以及解决更复杂的概率问题的能力。

鉴于标题，主要目的可能是通过一个清晰的、循序渐进的过程，使读者能够有条不紊地应用贝叶斯定理来解决概率问题。

---

## 61. 英国电力生产地图

**原文标题**: UK Electricity Generation Map

**原文链接**: [https://www.energydashboard.co.uk/map](https://www.energydashboard.co.uk/map)

无法访问文章链接。

---

## 62. SQLite 和 Clojure 中的简易双时态数据系统

**原文标题**: Poor man's bitemporal data system in SQLite and Clojure

**原文链接**: [https://www.evalapply.org/posts/poor-mans-time-oriented-data-system/index.html](https://www.evalapply.org/posts/poor-mans-time-oriented-data-system/index.html)

本文介绍了双时态数据系统的概念，强调了追踪事实被记录的时间（事务时间）和事实实际为真的时间（有效时间）的重要性。作者认为，这些系统对于准确表示实体随时间演变的状态以及从中学习状态如何变化至关重要。

作者使用会计实践的比喻，即更改被记录为新交易而不是修改现有条目，来说明追加新信息而不删除或修改旧数据的核心原则。这创建了一个所有更改的不可变记录，允许进行历史重建和分析。

本文将数据分解为实体-属性-值 (EAV) 三元组，并添加时间维度以捕获实体在特定时间点的状态。它强调了理解事件作为过程以及持续观察和记录实体状态变化的重要性。作者还讨论了事实在不同时间点为真或假的概念，要求系统处理冲突的断言并跟踪知识的演变。

双时态系统旨在回答的关键问题是：“它实际何时发生？”（有效时间）和“我们何时正式记录它？”（事务时间）。文章最后强调，只有事实发送者可以声明有效时间，只有数据存储可以声明事务时间，突出了记录和验证信息中的关注点分离。

---

## 63. 十维空间中的随机漫步 (2021)

**原文标题**: A Random Walk in 10 Dimensions (2021)

**原文链接**: [https://galileo-unbound.blog/2021/06/28/a-random-walk-in-10-dimensions/](https://galileo-unbound.blog/2021/06/28/a-random-walk-in-10-dimensions/)

这篇文章《十维空间中的随机游走》探讨了高维空间系统中违反直觉的行为，这与物理学、进化生物学和机器学习等领域相关。文章强调了基于三维经验的直觉在高维空间中往往会失效，这种现象被称为“维度诅咒”。

文章以十维空间中的随机游走为例，说明了关键差异。虽然可视化这样的空间几乎是不可能的，但它的维度已经足够高，可以展示非常高维的行为。与可能被困住的低维空间不同，高维景观由山脊主导，而不是孤立的山峰。

这具有重大意义。在进化生物学中，高维空间代表可能的基因突变，而景观代表适应度，这意味着进化可以沿着这些山脊进行，从而在不陷入局部最优的情况下实现显著的改变和适应。同样，在机器学习中，优化算法在高维损失函数中寻找最小值，山脊的普遍存在使得探索和优化更加高效。

文章解释了渗透阈值的概念，即随机网络中的连通性发生巨大变化的点。高维度允许随机游走者通过山脊连通性的高概率在空间中穿梭。

本质上，文章认为，高维度虽然难以可视化，但它通过提供众多相互连接的路径，促进了进化和优化等动态过程，强调了理解这些动态过程对各个科学学科的重要性。

---

## 64. 劣质软件在哪？为何人工智能编码的主张并不成立

**原文标题**: Where's the shovelware? Why AI coding claims don't add up

**原文链接**: [https://mikelovesrobots.substack.com/p/wheres-the-shovelware-why-ai-coding](https://mikelovesrobots.substack.com/p/wheres-the-shovelware-why-ai-coding)

无法访问文章链接。

---

## 65. 用于6502微处理器的微软BASIC – 1.1版

**原文标题**: Microsoft BASIC for 6502 Microprocessor – Version 1.1

**原文链接**: [https://github.com/microsoft/BASIC-M6502](https://github.com/microsoft/BASIC-M6502)

本文着重介绍了1976-1978年间发布的用于6502微处理器的Microsoft BASIC 1.1版源代码的历史意义。它论证了该BASIC解释器通过普及编程并驱动像Apple II和Commodore PET等具有影响力的早期计算机，对个人电脑革命至关重要。将其授权给各制造商奠定了微软早期的成功和商业模式，早于MS-DOS和Windows。

该代码的关键特性是通过条件编译实现的多平台兼容性，支持Apple II、Commodore PET、OSI、KIM-1以及PDP-10模拟等系统。本文档详细介绍了技术规格，包括其8KB ROM占用空间、包含浮点运算的完整BASIC语言实现、字符串处理和高效的内存管理。修订历史记录显示了持续的开发工作。

除了技术方面，本文档还强调了此BASIC解释器的文化影响。它向数百万人介绍了编程，成为事实上的标准，并开创了多平台方法。它还强调了其在建立软件许可商业模式中的作用。本文档指出BASIC解释器对MS-DOS、标准化编程语言以及计算机编程大众化等后续发展的影响，强调了其作为现代软件行业基石的遗产。“m6502.asm”文件包含6,955行6502汇编代码。

---

## 66. 叛逆作家的首次反抗

**原文标题**: A Rebel Writer's First Revolt

**原文链接**: [https://www.vulture.com/article/arundhati-roy-mother-mary-comes-to-me-review.html](https://www.vulture.com/article/arundhati-roy-mother-mary-comes-to-me-review.html)

This article reviews Arundhati Roy's new memoir, *Mother Mary Comes to Me*, framing it as a reflection on her life and career in the context of her complex relationship with her mother, Mary Roy. The piece examines Roy's shift from celebrated novelist (author of *The God of Small Things*) to outspoken political commentator and activist, exploring how her mother's influence shaped her rebellious spirit and outsider perspective.

The review highlights the tension between Roy's literary talent and her increasingly didactic political writing, arguing that her later works lack the immersive quality and discipline of her debut novel. While acknowledging Roy's consistent political stance and her role as a critical voice against the Indian government, the article suggests her memoir is strongest when focused on personal details and the dynamics with her mother.

Mary Roy is portrayed as a powerful and unconventional figure, both a hero and a source of trauma for Arundhati. The memoir reveals the impact of Mary's strict and sometimes cruel parenting on Roy's sense of self and her later life. The article ultimately suggests that Roy's constant need for a worthy opponent, evident in her political activism, stems from her lifelong wrestling match with her formidable mother. While acknowledging Roy's privileged background, the review emphasizes her self-identification as an outsider and the lasting influence of her mother's defiance.


---

## 67. John Coltrane's Tone Circle

**原文标题**: John Coltrane's Tone Circle

**原文链接**: [https://roelsworld.eu/blog-saxophone/coltrane-tone-circle/](https://roelsworld.eu/blog-saxophone/coltrane-tone-circle/)

Unable to access the article link.


---

## 68. The Wetware Crisis: The Thermocline of Truth (2008)

**原文标题**: The Wetware Crisis: The Thermocline of Truth (2008)

**原文链接**: [https://brucefwebster.com/2008/04/15/the-wetware-crisis-the-themocline-of-truth/](https://brucefwebster.com/2008/04/15/the-wetware-crisis-the-themocline-of-truth/)

生成摘要时出错

---

## 69. Kernel-hack-drill and exploiting CVE-2024-50264 in the Linux kernel

**原文标题**: Kernel-hack-drill and exploiting CVE-2024-50264 in the Linux kernel

**原文链接**: [https://a13xp0p0v.github.io/2025/09/02/kernel-hack-drill-and-CVE-2024-50264.html](https://a13xp0p0v.github.io/2025/09/02/kernel-hack-drill-and-CVE-2024-50264.html)

生成摘要时出错

---

## 70. We Found the Hidden Cost of Data Centers. It's in Your Electric Bill [video]

**原文标题**: We Found the Hidden Cost of Data Centers. It's in Your Electric Bill [video]

**原文链接**: [https://www.youtube.com/watch?v=YN6BEUA4jNU](https://www.youtube.com/watch?v=YN6BEUA4jNU)

生成摘要时出错

---

## 71. VibeVoice：前沿开源文本转语音模型

**原文标题**: VibeVoice: A Frontier Open-Source Text-to-Speech Model

**原文链接**: [https://microsoft.github.io/VibeVoice/](https://microsoft.github.io/VibeVoice/)

生成摘要时出错

---

## 72. Lively Linear Lisp (1992) [pdf]

**原文标题**: Lively Linear Lisp (1992) [pdf]

**原文链接**: [https://www.cs.utexas.edu/users/hunt/research/hash-cons/hash-cons-papers/BakerLinearLisp.pdf](https://www.cs.utexas.edu/users/hunt/research/hash-cons/hash-cons-papers/BakerLinearLisp.pdf)

I am sorry, I lack the ability to process PDF documents. Therefore, I am unable to summarize the Lively Linear Lisp article.


---

## 73. Tufte CSS

**原文标题**: Tufte CSS

**原文链接**: [https://edwardtufte.github.io/tufte-css/](https://edwardtufte.github.io/tufte-css/)

生成摘要时出错

---

## 74. Comic Sans typeball designed to work with the IBM Selectric typewriters

**原文标题**: Comic Sans typeball designed to work with the IBM Selectric typewriters

**原文链接**: [https://www.printables.com/model/441233-comic-sans-typeball-for-the-ibm-selectric-typewrit](https://www.printables.com/model/441233-comic-sans-typeball-for-the-ibm-selectric-typewrit)

生成摘要时出错

---

## 75. 6NF File Format

**原文标题**: 6NF File Format

**原文链接**: [https://habr.com/en/articles/942516/](https://habr.com/en/articles/942516/)

生成摘要时出错

---

## 76. Rivian CEO: 'blows my mind' to see US auto makers shifting back to ICE vehicles

**原文标题**: Rivian CEO: 'blows my mind' to see US auto makers shifting back to ICE vehicles

**原文链接**: [https://www.businessinsider.com/rivian-ceo-us-investment-internal-combustion-engines-gas-vehicles-2025-8](https://www.businessinsider.com/rivian-ceo-us-investment-internal-combustion-engines-gas-vehicles-2025-8)

生成摘要时出错

---

## 77. Voyager – An interactive video generation model with realtime 3D reconstruction

**原文标题**: Voyager – An interactive video generation model with realtime 3D reconstruction

**原文链接**: [https://github.com/Tencent-Hunyuan/HunyuanWorld-Voyager](https://github.com/Tencent-Hunyuan/HunyuanWorld-Voyager)

生成摘要时出错

---

## 78. Spec-Driven Development Toolkit from GitHub

**原文标题**: Spec-Driven Development Toolkit from GitHub

**原文链接**: [https://github.com/github/spec-kit](https://github.com/github/spec-kit)

生成摘要时出错

---

## 79. Evaluating Agents

**原文标题**: Evaluating Agents

**原文链接**: [https://aunhumano.com/index.php/2025/09/03/on-evaluating-agents/](https://aunhumano.com/index.php/2025/09/03/on-evaluating-agents/)

生成摘要时出错

---

## 80. Finding thousands of exposed Ollama instances using Shodan

**原文标题**: Finding thousands of exposed Ollama instances using Shodan

**原文链接**: [https://blogs.cisco.com/security/detecting-exposed-llm-servers-shodan-case-study-on-ollama](https://blogs.cisco.com/security/detecting-exposed-llm-servers-shodan-case-study-on-ollama)

生成摘要时出错

---

## 81. TPDE-LLVM: Faster LLVM -O0 Back-End

**原文标题**: TPDE-LLVM: Faster LLVM -O0 Back-End

**原文链接**: [https://discourse.llvm.org/t/tpde-llvm-10-20x-faster-llvm-o0-back-end/86664](https://discourse.llvm.org/t/tpde-llvm-10-20x-faster-llvm-o0-back-end/86664)

生成摘要时出错

---

## 82. Best printer 2025: just buy a Brother laser printer

**原文标题**: Best printer 2025: just buy a Brother laser printer

**原文链接**: [https://www.theverge.com/tech/641940/best-printer-2025-just-buy-a-brother-laser-printer-middle-finger-in-the-air](https://www.theverge.com/tech/641940/best-printer-2025-just-buy-a-brother-laser-printer-middle-finger-in-the-air)

生成摘要时出错

---

## 83. Why Rewriting Emacs Is Hard

**原文标题**: Why Rewriting Emacs Is Hard

**原文链接**: [https://kyo.iroiro.party/en/posts/why-rewriting-emacs-is-hard/](https://kyo.iroiro.party/en/posts/why-rewriting-emacs-is-hard/)

生成摘要时出错

---

## 84. Say Bye with JavaScript Beacon

**原文标题**: Say Bye with JavaScript Beacon

**原文链接**: [https://hemath.dev/blog/say-bye-with-javascript-beacon/](https://hemath.dev/blog/say-bye-with-javascript-beacon/)

生成摘要时出错

---

## 85. The Theoretical Limitations of Embedding-Based Retrieval

**原文标题**: The Theoretical Limitations of Embedding-Based Retrieval

**原文链接**: [https://www.alphaxiv.org/abs/2508.21038v1](https://www.alphaxiv.org/abs/2508.21038v1)

生成摘要时出错

---

## 86. Abstract Machine Models (2022)

**原文标题**: Abstract Machine Models (2022)

**原文链接**: [https://dr-knz.net/abstract-machine-models.html](https://dr-knz.net/abstract-machine-models.html)

生成摘要时出错

---

## 87. Show HN: Prototyper – AI design platform with its own compiler and runtime

**原文标题**: Show HN: Prototyper – AI design platform with its own compiler and runtime

**原文链接**: [https://www.getaprototype.com](https://www.getaprototype.com)

生成摘要时出错

---

## 88. This Page Is a Quine (2021)

**原文标题**: This Page Is a Quine (2021)

**原文链接**: [https://pranavg.me/](https://pranavg.me/)

生成摘要时出错

---

## 89. The Rust Innovation Lab

**原文标题**: The Rust Innovation Lab

**原文链接**: [https://rustfoundation.org/rust-innovation-lab/](https://rustfoundation.org/rust-innovation-lab/)

生成摘要时出错

---

## 90. Lessons from building an AI data analyst

**原文标题**: Lessons from building an AI data analyst

**原文链接**: [https://www.pedronasc.com/articles/lessons-building-ai-data-analyst](https://www.pedronasc.com/articles/lessons-building-ai-data-analyst)

生成摘要时出错

---

## 91. The 16-year odyssey it took to emulate the Pioneer LaserActive

**原文标题**: The 16-year odyssey it took to emulate the Pioneer LaserActive

**原文链接**: [https://www.readonlymemo.com/this-is-the-first-the-16-year-odyssey-of-time-money-wrong-turns-and-frustration-it-took-to-finally-emulate-the-pioneer-laseractive/](https://www.readonlymemo.com/this-is-the-first-the-16-year-odyssey-of-time-money-wrong-turns-and-frustration-it-took-to-finally-emulate-the-pioneer-laseractive/)

生成摘要时出错

---

## 92. Magic Lantern Is Back

**原文标题**: Magic Lantern Is Back

**原文链接**: [https://www.magiclantern.fm/forum/index.php?topic=27315.0](https://www.magiclantern.fm/forum/index.php?topic=27315.0)

生成摘要时出错

---

## 93. Glow-in-the-dark houseplants shine in rainbow of colours

**原文标题**: Glow-in-the-dark houseplants shine in rainbow of colours

**原文链接**: [https://www.nature.com/articles/d41586-025-02740-2](https://www.nature.com/articles/d41586-025-02740-2)

生成摘要时出错

---

## 94. Microsoft's Root Program and the 1.1.1.1 Certificate Slip

**原文标题**: Microsoft's Root Program and the 1.1.1.1 Certificate Slip

**原文链接**: [https://unmitigatedrisk.com/?p=1092](https://unmitigatedrisk.com/?p=1092)

生成摘要时出错

---

## 95. Warp Code: the fastest way from prompt to production

**原文标题**: Warp Code: the fastest way from prompt to production

**原文链接**: [https://www.warp.dev/blog/introducing-warp-code-prompt-to-prod](https://www.warp.dev/blog/introducing-warp-code-prompt-to-prod)

生成摘要时出错

---

## 96. How to Give a Good Talk

**原文标题**: How to Give a Good Talk

**原文链接**: [https://blog.sigplan.org/2025/03/31/how-to-give-a-good-talk/](https://blog.sigplan.org/2025/03/31/how-to-give-a-good-talk/)

生成摘要时出错

---

## 97. The Browser Company (Arc, Dia) Has Been Acquired by Atlassian

**原文标题**: The Browser Company (Arc, Dia) Has Been Acquired by Atlassian

**原文链接**: [https://www.atlassian.com/blog/announcements/atlassian-acquires-the-browser-company](https://www.atlassian.com/blog/announcements/atlassian-acquires-the-browser-company)

生成摘要时出错

---

## 98. The AI breakthrough that uses almost no power to create images

**原文标题**: The AI breakthrough that uses almost no power to create images

**原文链接**: [https://techxplore.com/news/2025-08-ai-breakthrough-power-images.html](https://techxplore.com/news/2025-08-ai-breakthrough-power-images.html)

生成摘要时出错

---

## 99. Amazonq.nvim: Official AWS AI Assistant Plugin for Neovim

**原文标题**: Amazonq.nvim: Official AWS AI Assistant Plugin for Neovim

**原文链接**: [https://github.com/awslabs/amazonq.nvim](https://github.com/awslabs/amazonq.nvim)

生成摘要时出错

---

## 100. CalCheck – Your Calendar's Safety Net – Verifies that your calendar is syncing

**原文标题**: CalCheck – Your Calendar's Safety Net – Verifies that your calendar is syncing

**原文链接**: [https://cal-check.com/](https://cal-check.com/)

生成摘要时出错

---

