# Hacker News 热门文章摘要 (2025-07-11)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 每天在 Quad9 递归解析器阵列上发现的热门 DNS 域名

**原文标题**: Top DNS domains seen on the Quad9 recursive resolver array each day

**原文链接**: [https://github.com/Quad9DNS/quad9-domains-top500](https://github.com/Quad9DNS/quad9-domains-top500)

本文档描述了 "quad9-domains-top500" 数据，这是一个每日更新的列表，列出了 Quad9 递归解析器中最常查询的 500 个域名。它反映了 Quad9 基础设施内观察到的 DNS 活动快照。

主要要点包括：

*   **目的：** 该列表反映了 Quad9 解析器上最常请求的域名。
*   **排除项：** 顶级域名 (TLD) 被排除在外。
*   **注意事项：** 该列表并非简单的受欢迎程度竞赛。排名靠前可能源于 CDN 使用、激进型应用程序、反病毒校验和或糟糕的 DNS TTL 管理等因素。Quad9 尝试阻止 DNS 隧道，但可能无法检测到所有方法。TTL 也未纳入考量，因此缓存的域名可能不会出现。
*   **数据收集：** 该列表源自 Quad9 服务器子集上查询响应的统计样本。
*   **解读：** 排名靠前并不一定等同于受欢迎程度；它可能表明存在诸如低效 DNS 管理之类的问题。
*   **联系方式：** 有关数据的疑问，请发送至 support@quad9.net。

---

## 2. 展示 HN：Vibe Kanban – 用于管理你的 AI 编码代理的看板

**原文标题**: Show HN: Vibe Kanban – Kanban board to manage your AI coding agents

**原文链接**: [https://github.com/BloopAI/vibe-kanban](https://github.com/BloopAI/vibe-kanban)

Vibe Kanban：旨在简化 Claude Code、Gemini CLI、Codex 和 Amp 等 AI 编码代理管理的看板。它旨在通过提供用于规划、审查和编排任务的中心化平台，帮助那些花费越来越多时间来编排 AI 代码生成的工程师。

主要功能包括：

*   **代理切换：** 轻松切换不同的编码代理。
*   **任务编排：** 并行或顺序执行多个编码代理。
*   **审查和执行：** 快速审查工作并启动开发服务器。
*   **任务跟踪：** 跟踪分配给编码代理的任务状态。
*   **配置管理：** 集中管理编码代理 MCP 配置。

验证所需的编码代理后，可以使用 `npx vibe-kanban` 安装此工具。 文档和支持分别可在网站和 GitHub issues 上找到。 欢迎贡献，但在提交 pull request 之前应与核心团队讨论。

开发环境需要 Rust、Node.js 和 pnpm。运行 `pnpm run dev` 会启动带有实时重新加载的前端和后端。可以通过运行 `build-npm-package.sh` 然后在 `npx-cli` 文件夹中运行 `npm pack` 来创建构建。 可以使用 `npx [GENERATED FILE].tgz` 运行构建的包。

---

## 3. 比尔·阿特金森的迷幻用户界面

**原文标题**: Bill Atkinson's psychedelic user interface

**原文链接**: [https://patternproject.substack.com/p/from-the-mac-to-the-mystical-bill](https://patternproject.substack.com/p/from-the-mac-to-the-mystical-bill)

无法访问文章链接。

---

## 4. 天文学家竞相研究星际闯入者

**原文标题**: Astronomers race to study interstellar interloper

**原文链接**: [https://www.science.org/content/article/astronomers-race-study-interstellar-interloper](https://www.science.org/content/article/astronomers-race-study-interstellar-interloper)

无法访问文章链接。

---

## 5. 重新贴膜你的MacBook

**原文标题**: Repaste Your MacBook

**原文链接**: [https://christianselig.com/2025/07/repaste-macbook/](https://christianselig.com/2025/07/repaste-macbook/)

2025年7月，作者详述了自己为解决日益严重的风扇噪音问题，而重新为老化的M1 Pro MacBook Pro涂抹散热硅脂的经历。风扇噪音的常见原因是散热硅脂干涸。虽然笔记本性能依旧良好，但在编译代码和视频编辑等高强度任务期间，风扇噪音变得令人难以忍受。

作者参考iFixit指南，用Noctua NT-H2替换了CPU散热硅脂。他们发现苹果公司为RAM芯片使用了特殊的“碳黑”化合物，由于其独特的性能和难以采购，因此决定不更换。

过程并非一帆风顺。作者不幸撕裂了脆弱的风扇电缆，需要更换。更换风扇重新组装后，Touch ID传感器电缆也被撕裂，导致Touch ID功能无法使用，而且很可能在Apple Store维修费用高昂。

尽管遭遇这些挫折，重新涂抹硅脂仍然奏效。 Cinebench测试表明，最高CPU温度降低（102°C降至96°C），最大风扇转速显著降低（6,300 RPM降至4,700 RPM），同时保持了相似的性能得分。笔记本电脑的空闲温度也降低了。

作者总结说，虽然拆卸过程可以控制，但电缆的脆弱性使其具有风险。他们建议没有小型电子设备维修经验的人不要尝试，但建议有经验的用户或通过维修店进行维修，如果MacBook使用了几年。散热性能和噪音的改善是有益的，但Touch ID功能的潜在损失是一个重要的考虑因素。

---

## 6. 姜黄是全球铅中毒谜案的罪魁祸首 (2024)

**原文标题**: Turmeric is the culprit in a global lead poisoning mystery (2024)

**原文链接**: [https://www.npr.org/sections/goats-and-soda/2024/09/23/nx-s1-5011028/detectives-mystery-lead-poisoning-new-york-bangladesh](https://www.npr.org/sections/goats-and-soda/2024/09/23/nx-s1-5011028/detectives-mystery-lead-poisoning-new-york-bangladesh)

20世纪80年代，为了使姜黄根更具吸引力，孟加拉国的一些农民开始添加铬酸铅，一种通常用于工业涂料的有毒黄色颜料。这种做法最初是为了解决洪水造成的变色问题，后来由于颜色鲜艳的姜黄更容易销售而变得普遍。这种广泛的污染导致了一场全球健康危机，影响了孟加拉国的孕妇和儿童，甚至纽约市的孟加拉社区。

由纽约市卫生侦探和一位名叫Jenna Forsyth的加州博士生牵头的铅中毒调查显示，姜黄是罪魁祸首。 Forsyth的研究源于孟加拉国农村孕妇体内惊人的高铅水平，并将源头追溯到掺铅姜黄。

2019年，孟加拉国食品安全局迅速做出回应。他们发布了公共警告，分发了信息传单，与农民和磨坊主举办了研讨会，甚至设立了“流动法庭”没收受污染的姜黄并对供应商处以罚款。 结果，姜黄样品中的铅污染率从47%骤降至0%，当地农民和孕妇的血铅水平也显着降低。 该案例突显了铅中毒的破坏性影响以及在解决此类危机时迅速、果断行动的有效性。

---

## 7. 报告称，英国邮局丑闻致至少13人自杀身亡。

**原文标题**: At Least 13 People Died by Suicide Amid U.K. Post Office Scandal, Report Says

**原文链接**: [https://www.nytimes.com/2025/07/10/world/europe/uk-post-office-scandal-report.html](https://www.nytimes.com/2025/07/10/world/europe/uk-post-office-scandal-report.html)

无法访问文章链接。

---

## 8. 以半价升级 M4 Pro Mac mini 的存储

**原文标题**: Upgrading an M4 Pro Mac mini's storage for half the price

**原文链接**: [https://www.jeffgeerling.com/blog/2025/upgrading-m4-pro-mac-minis-storage-half-price](https://www.jeffgeerling.com/blog/2025/upgrading-m4-pro-mac-minis-storage-half-price)

本文详细介绍了使用 M4-SSD 的 DIY 套件升级 M4 Pro Mac mini 内部存储的过程。作者将一台 Mac mini 从 512GB 升级到 4TB，并在视频中记录了整个过程。虽然物理升级相对简单，只需要基本的笔记本电脑硬件技能，但拆卸后部塑料盖可能比较棘手。

一个关键方面是升级后需要进行 DFU (设备固件更新) 恢复。作者明确指出，DFU 恢复不仅可以用 Apple Silicon Mac 进行，也可以用许多配备 T2 芯片的 Intel Mac 进行。 这涉及到连接到 Mac mini 的 Thunderbolt 端口并在开机时按住电源按钮。

性能测试比较了升级后的内部 SSD 与外部 Thunderbolt 5 NVMe 硬盘盒。升级后的 4TB 内部模块显示出明显更好的写入速度，因为其具有更多的闪存芯片。 外部驱动器虽然速度很快，但偶尔会出现速度下降的情况，这可能是由于 DRAM 缓存的限制。

文章最后总结说，虽然 699 美元的 M4 Pro 4TB SSD 升级套件与标准 NVMe SSD 相比价格昂贵，但它比苹果公司提供的相同容量的 1200 美元的升级便宜得多。作者强调了内部存储的稳定速度和可靠性。

---

## 9. 吴恩达：用人工智能加速构建 [视频]

**原文标题**: Andrew Ng: Building Faster with AI [video]

**原文链接**: [https://www.youtube.com/watch?v=RNJCfif1dPY](https://www.youtube.com/watch?v=RNJCfif1dPY)

这似乎是吴恩达在YouTube上发布的视频列表，标题为“利用人工智能加速构建”。然而，提供的“内容”部分只是YouTube通用的页脚信息（版权、条款、隐私等），不包含关于视频实际内容的任何信息。

因此，无法给出恰当的总结。根据标题推测，该视频可能讨论如何利用人工智能来加速或改进构建过程，可能是在软件开发、机器学习模型，甚至物理建造的背景下。在没有更多来自视频本身的细节的情况下，总结只能局限于这种猜测。

---

## 10. 宾州众议院通过“一键取消”订阅法案

**原文标题**: Pa. House passes 'click-to-cancel' subscription bills

**原文链接**: [https://www.pennlive.com/news/2025/07/pa-house-passes-click-to-cancel-subscription-bills-as-court-throws-out-federal-rule.html](https://www.pennlive.com/news/2025/07/pa-house-passes-click-to-cancel-subscription-bills-as-court-throws-out-federal-rule.html)

宾夕法尼亚州众议院通过两项法案，旨在打击欺骗性订阅行为，与近期被联邦上诉法院驳回的联邦法规类似。第一项法案打击“否定选择”协议，即消费者在未主动选择退出服务的情况下被自动注册。该法案由众议员丽莎·博罗夫斯基发起，规定续订前必须发出通知，并要求消费者能够以与订阅相同的方式取消订阅。第二项法案由众议员乔·奇雷西发起，规定在线订阅必须可以在线取消，并明确显示续订和取消信息。

该州立法旨在解决消费者在取消订阅时遇到的困难，奇雷西众议员表示他的选民和家人都经历过这个问题。虽然一些企业最初抵制，但奇雷西强调，其目标是帮助消费者，而不是损害企业。

这些法案不包括受公共事业委员会、联邦通信委员会和健身房监管的服务（尽管这可能会被修改）。尽管联邦层面遭遇挫折，宾夕法尼亚州希望加入纽约、加利福尼亚、明尼苏达、田纳西和弗吉尼亚等其他州，制定类似的消费者保护政策。这些法案以两党支持获得通过，目前正等待州参议院的审议以及州长乔什·夏皮罗的签署。

---

## 11. AI智能体基准测试已失效

**原文标题**: AI agent benchmarks are broken

**原文链接**: [https://ddkang.substack.com/p/ai-agent-benchmarks-are-broken](https://ddkang.substack.com/p/ai-agent-benchmarks-are-broken)

无法访问文章链接。

---

## 12. 日本过度旅游，以及它如何损害小型企业

**原文标题**: Overtourism in Japan, and how it hurts small businesses

**原文链接**: [https://craigmod.com/ridgeline/210/](https://craigmod.com/ridgeline/210/)

克雷格·莫德：《日本过度旅游及其对小型企业的影响》探讨了由社交媒体和廉价旅行推动的大众旅游对日本城市（尤其是京都）的特色和社区造成的有害影响。文章认为，过度旅游摧毁了构成城市独特身份基石的小型企业，因为这些企业通常建立在服务当地居民和创建社区中心的基础上，而不是迎合短暂的、寻求自拍的游客。

作者着重讲述了一位京都酒吧老板在TikTok上爆红后，因涌入大量无法建立联系的顾客而感到沮丧的经历。莫德认为，算法和廉价旅游套餐正在推动这一现象，导致“迪士尼乐园式的倒戈”，游客们未能将他们访问的城市视为生活场所，而是将其视为有待消费的景点。

在承认负面影响的同时，莫德仍然保持乐观，他指出，越来越多的旅行者（约15%）是真正的好奇和尊重，他们寻求真实的体验，并为当地经济做出积极贡献。他鼓励这些旅行者探索鲜为人知的城市，如盛冈和山口，这些城市提供独特的文化体验，而没有京都那样拥挤的人群。

文章提出了管理过度旅游的实用解决方案，例如取消免税购物计划，提高离境税，并对热门旅游景点实行差异化门票价格。最终目标是将旅游业导向游客较少的地区，确保可持续增长并保护日本独特小型企业的魅力。

---

## 13. Show HN: Pangolin – Cloudflare Tunnels 的开源替代方案

**原文标题**: Show HN: Pangolin – Open source alternative to Cloudflare Tunnels

**原文链接**: [https://github.com/fosrl/pangolin](https://github.com/fosrl/pangolin)

穿山甲 (Pangolin)：Cloudflare Tunnels 的开源自托管替代方案，提供具有内置身份和访问控制的零信任隧道反向代理服务器。它通过加密的 WireGuard 隧道连接隔离的网络，安全地暴露分布式网络上的私有资源，从而无需开放端口。

主要功能包括通过 WireGuard 进行反向代理、自动 SSL 证书、负载均衡以及对各种 TCP/UDP 服务的支持。穿山甲提供具有平台 SSO 的集中式身份验证、基于 IP 和 URL 路径的访问控制规则、TOTP 双因素身份验证以及基于组织/角色的访问管理。它与 Authentik、Keycloak 和 Okta 等外部 IdP 集成，以实现自动配置。

该平台拥有一个简单的仪表板 UI、基于 Docker Compose 的部署、带有 Swagger 文档的 API 以及用于使用 Traefik 插件（例如 CrowdSec）扩展功能的模块化设计。用例包括绕过端口限制、为企业部署服务以及管理物联网网络。Newt，一个自定义的用户空间 WireGuard 客户端，用于简化连接。

该项目在 AGPL-3 和商业许可下双重许可，欢迎通过存储库贡献。它正在大力开发中，路线图可在项目板上找到。

---

## 14. Kimi K2

**原文标题**: Kimi K2

**原文链接**: [https://twitter.com/Kimi_Moonshot/status/1943687594560332025](https://twitter.com/Kimi_Moonshot/status/1943687594560332025)

“Kimi K2”是一个来自X Corp.（前身为Twitter）的错误信息，提示用户的浏览器禁用了JavaScript，X.com需要JavaScript才能运行。该信息指示用户启用JavaScript或切换到支持的浏览器，并提供X.com帮助中心的链接以查看支持的浏览器列表。此外，还包括标准的网站页脚信息，如服务条款、隐私政策、Cookie政策、版本说明、广告信息以及X Corp.的版权声明（© 2025）。简而言之，此内容并非文章，而是一个阻止用户访问X.com网站的浏览器兼容性错误信息。

---

## 15. 上月太阳能首次成为欧洲最大电力来源

**原文标题**: In a First, Solar Was Europe's Biggest Source of Power Last Month

**原文链接**: [https://e360.yale.edu/digest/solar-biggest-power-source-europe-june-2025](https://e360.yale.edu/digest/solar-biggest-power-source-europe-june-2025)

六月，太阳能首次成为欧盟最大的电力来源，创下该集团电力供应的22%的纪录。至少有13个国家的太阳能发电量达到新的月度峰值，促成了这一里程碑的实现。在荷兰和希腊，太阳能分别产生了超过40%和35%的电力。

太阳能的激增帮助欧洲应对了超过华氏110度（摄氏43度）的严重热浪。太阳能在中午时分最为丰富，与空调需求的峰值相吻合，缓解了电网的压力并有助于防止停电。

核能是第二大电力来源，其次是风能、天然气和水力发电。煤炭的贡献降至每月新低的6%，目前有15个欧盟国家已实现无煤化。专家强调了太阳能在减轻日益严重的热浪影响方面的重要性，而气候变化加剧了热浪。伦敦帝国理工学院的一项研究将化石燃料的燃烧与欧洲因热浪导致的死亡人数显著增加联系起来。

---

## 16. OpenFront：浏览器实时类风险多人游戏

**原文标题**: OpenFront: Realtime Risk-like multiplayer game in the browser

**原文链接**: [https://openfront.io/](https://openfront.io/)

无法访问文章链接。

---

## 17. 摆脱人工智能依赖症

**原文标题**: Recovering from AI Addiction

**原文链接**: [https://internetaddictsanonymous.org/internet-and-technology-addiction/signs-of-an-addiction-to-ai/](https://internetaddictsanonymous.org/internet-and-technology-addiction/signs-of-an-addiction-to-ai/)

匿名网络与科技成瘾者协会（ITAA）的这篇文章探讨了人工智能成瘾这一新兴问题，将其定义为对聊天机器人、人工智能艺术生成器和人工智能伴侣等人工智能应用程序的强迫性和有害使用。文章强调，人工智能成瘾是网络与科技成瘾的一个子集，它会改变大脑功能，影响注意力、情绪调节和人际关系。

文章重点介绍了人工智能成瘾的常见症状，包括使用人工智能的时间超出预期、依靠人工智能来获得认可、不使用人工智能时感到焦虑以及忽视线下责任。文章还提供了一份问卷，以帮助个人识别潜在的人工智能成瘾。

文章讨论了网络成瘾症（IAD）的更广泛背景及其对心理、情感和身体健康的负面影响，包括与物质成瘾类似的大脑结构变化。风险包括冲动控制问题、多动症、焦虑、药物滥用、睡眠问题，甚至自杀意念。

ITAA提供了一种基于匿名戒酒互助会模式的解决方案，强调社区支持、戒除成瘾行为以及完成十二个步骤。文章概述了恢复的实际步骤，例如参加会议、拨打外展电话、识别并戒除触发行为以及寻找赞助人。

文章还探讨了各种类型的网络成瘾，包括社交媒体、流媒体、手机、电子游戏、色情和信息成瘾。文章强调了明确个人清醒状态和有目的地使用技术的重要性，从而促进平衡的生活方式。

---

## 18. 有人创造了1840亿枚比特币的那一天（2020）

**原文标题**: The day someone created 184 billion Bitcoin (2020)

**原文链接**: [https://decrypt.co/39750/184-billion-bitcoin-anonymous-creator](https://decrypt.co/39750/184-billion-bitcoin-anonymous-creator)

提供的文本并非文章，而是加密货币价格及其百分比变化的列表。其中没有叙述、故事或事件描述，因此无法提供关于某人在2020年创造1840亿比特币的摘要。 该文本仅显示各种加密货币的当前市场数据。

---

## 19. LLM推理手册

**原文标题**: LLM Inference Handbook

**原文链接**: [https://bentoml.com/llm/](https://bentoml.com/llm/)

《LLM推理手册》是为在生产环境中部署、扩展和运行大型语言模型(LLM)的工程师设计的综合资源。它将分散在各种来源的知识整合到一个易于访问的指南中。

该手册涵盖了LLM推理的各个重要方面，包括：

*   **核心概念和性能指标：** 解释了首个令牌时间(TTFT)、每秒令牌数(TPS)和有效吞吐量。
*   **优化技术：** 详细介绍了连续批处理和前缀缓存等策略。
*   **运营最佳实践：** 为部署和扩展提供实用指导。

编写该手册的动机是解决LLM推理领域缺乏统一资源的问题，弥合学术知识与实际应用之间的差距。它专注于对实际部署影响最大的内容，避免无关的技术细节。

该手册可以按顺序阅读，也可以作为参考。它会持续更新，以反映LLM推理领域不断变化的情况。鼓励通过GitHub贡献，以确保其准确性和相关性。

---

## 20. ChompSaw：一款适合儿童使用的台式电动工具

**原文标题**: The ChompSaw: A benchtop power tool that's safe for kids to use

**原文链接**: [https://www.core77.com/posts/137602/The-ChompSaw-A-Benchtop-Power-Tool-Thats-Safe-for-Kids-to-Use](https://www.core77.com/posts/137602/The-ChompSaw-A-Benchtop-Power-Tool-Thats-Safe-for-Kids-to-Use)

Core77文章介绍：ChompSaw儿童安全纸板切割机。该桌面电动工具由产品设计师Kausi Raman和Max Liechty设计，旨在提供一种比曲线锯和线锯等潜在危险工具更安全的选择。曲线锯和线锯虽然可以进行自由切割，但可能造成严重伤害。

ChompSaw采用振动切割器，安全地隐藏在冰球状突起下方，防止使用时手指接触。它有效地发挥了啃咬器的作用，并将纸板边角料收集在下方的垃圾箱中，方便回收。该工具的售价为250美元。

评论区对该工具的必要性存在不同意见。一位评论者认为，孩子们能够理解锋利工具的危险性，不应被低估。另一位评论者认为，责任问题是其创作的驱动力。另一位评论者喜欢这个工具的想法。

---

## 21. 我不用社交媒体了——或者：为什么我现在有了博客

**原文标题**: I'm done with social media – Or: why I have a blog now

**原文链接**: [https://www.carolinecrampton.com/im-done-with-social-media/](https://www.carolinecrampton.com/im-done-with-social-media/)

2024年，作者为了宣传她的书《玻璃之躯》而开始学习社交媒体。尽管接受了培训课程、专家建议，并在Instagram和TikTok上持续发布内容，她发现这种体验令人不安且最终无效。她感到有压力将自己的生活变成内容，她将这种转变描述为一种险恶的视角扭曲。

算法对她的帖子兴趣寥寥，未能触达新的读者。她意识到BookTok上的成功案例源于真正读者的推荐和出版商的努力，而非作者驱动的病毒式视频。她的社交媒体活动感觉不真诚且自夸，缺乏真正的社群。线下交流表明，读者是被她的其他作品吸引，而非她的社交媒体存在。

作者得出结论，社交媒体是对时间和精力的一种糟糕投资，对她的精神状态产生负面影响。她质疑非名人作家活跃于社交媒体的压力，怀疑这是出版业转移责任和让作者忙碌的一种方式。

她认为“创作者经济”是一种金字塔骗局，只有少数人能从大众上传的免费内容中获益。对她来说，社交媒体不是创意职业的可行组成部分。她回顾了她与社交媒体的历史，强调了其成瘾性以及她作为记者所感受到的保持活跃的压力。她将此与博客进行了对比，她希望博客能够提供与受众更真实的联系。

---

## 22. 美国放弃搜寻宇宙膨胀信号

**原文标题**: U.S. abandons hunt for signal of cosmic inflation

**原文链接**: [https://www.science.org/content/article/u-s-abandons-hunt-signal-cosmic-inflation](https://www.science.org/content/article/u-s-abandons-hunt-signal-cosmic-inflation)

美国放弃搜寻宇宙膨胀信号

---

## 23. Postgres LISTEN/NOTIFY 无法扩展

**原文标题**: Postgres LISTEN/NOTIFY does not scale

**原文链接**: [https://www.recall.ai/blog/postgres-listen-notify-does-not-scale](https://www.recall.ai/blog/postgres-listen-notify-does-not-scale)

Recall.ai 因大量会议机器人写入结构化数据导致Postgres出现宕机，原因是写入密集型负载。调查发现，Postgres的LISTEN/NOTIFY功能存在瓶颈。核心问题在于：当事务中发出NOTIFY查询时，会在提交阶段获取整个数据库的全局`AccessExclusiveLock`锁。 这实际上使所有提交串行化，导致高并发下的巨大负载和宕机。

该问题表现为数据库负载和活动等待会话的大幅飙升，以及 CPU、磁盘 I/O 和网络流量的反常下降。日志分析显示，大量进程在提交期间等待`AccessExclusiveLock`锁。

为了确认问题，Recall.ai 运行了包含和不包含 LISTEN/NOTIFY 代码的负载测试。测试表明，在使用 NOTIFY 时，数据库的 CPU 和 I/O 负载在高负载期间骤降，表明存在全局互斥锁瓶颈。在没有 NOTIFY 的情况下，数据库充分利用了可用的 CPU，在不停止的情况下处理了负载峰值。

解决方案是从 LISTEN/NOTIFY 迁移，改为在应用程序层跟踪相关逻辑。 这解决了锁竞争问题并稳定了 Postgres 数据库。Recall.ai 强调了在高并发写入场景（数据库可扩展性至关重要）下避免使用 LISTEN/NOTIFY 的重要性。

---

## 24. 反对土地价值税的若干论点 (2024)

**原文标题**: Some arguments against a land value tax (2024)

**原文链接**: [https://www.lesswrong.com/posts/CCuJotfcaoXf8FYcy/some-arguments-against-a-land-value-tax](https://www.lesswrong.com/posts/CCuJotfcaoXf8FYcy/some-arguments-against-a-land-value-tax)

无法访问文章链接。

---

## 25. 当内核名称包含“cutlass”时，FP8速度快约100 tflops。

**原文标题**: FP8 is ~100 tflops faster when the kernel name has "cutlass" in it

**原文链接**: [https://twitter.com/cis_female/status/1943069934332055912](https://twitter.com/cis_female/status/1943069934332055912)

标题“当内核名包含 'cutlass' 时，FP8 快约 100 万亿次浮点运算”的文章讨论了 FP8 计算的性能差异。 主要结论是，当使用专门命名或与“cutlass”相关的内核时，FP8（8 位浮点）运算可实现明显更高的吞吐量（大约快 100 TFLOPS）。

这表明“cutlass”内核针对 FP8 运算进行了优化，可能是通过诸如高效的数据布局、优化的内存访问模式或为底层硬件量身定制的其他算法改进等技术。 该文章可能探讨了这种性能提升，或许会详细说明其背后的原因或将“cutlass”内核与替代实现进行比较。

由于内容以缺少活动 Javascript 的网站快照形式呈现，因此无法评估更多细节和底层证据。 然而，核心发现是使用与“cutlass”相关的内核时，FP8 计算的显着加速，突出了内核优化对于性能敏感型工作负载的重要性。

---

## 26. Gemini API中的批量模式：花更少，处理更多

**原文标题**: Batch Mode in the Gemini API: Process More for Less

**原文链接**: [https://developers.googleblog.com/en/scale-your-ai-workloads-batch-mode-gemini-api/](https://developers.googleblog.com/en/scale-your-ai-workloads-batch-mode-gemini-api/)

Google开发者博客推出 Gemini API 批量模式

这篇 Google 开发者博客文章介绍了 Gemini API 的批量模式，这是一个新的异步端点，专为高吞吐量、非延迟关键型工作负载而设计。它允许用户提交大型作业，并在 24 小时内检索结果，费用比同步 API 降低 50%。

批量模式非常适合数据已提前准备好且不需要立即响应的任务，可节省成本、提高吞吐量并简化 API 调用（无需复杂的排队或重试逻辑）。开发者可以将请求打包成单个文件，提交它，然后检索结果。

这篇文章重点介绍了批量内容生成/处理（例如 Reforged Labs 分析视频广告）和模型评估（Vals AI 用于基准测试）等用例。

文章提供了一段代码片段，演示了如何使用 Google GenAI Python SDK 使用批量模式，包括创建 JSONL 请求文件、上传它、创建批量作业和检索结果。

该功能正在向所有用户推出，并被定位为未来更多批处理能力的起点。文章还包含了文档、定价和 Cookbook 指南的链接。

---

## 27. 我在Vercel五年学到的事情

**原文标题**: Things I learned from 5 years at Vercel

**原文链接**: [https://leerob.com/vercel](https://leerob.com/vercel)

李·罗宾逊回顾其在 Vercel 的五年，分享了从个人贡献者成长为 VP 的五项关键经验，期间公司从 30 人和 100 万美元 ARR 扩展到 650 人和超过 2 亿美元 ARR。

**1. 全力以赴，然后回家：** 通过在工作中建立强大的支持系统来避免倦怠，使您能够在下线时完全断开连接。 招募并授权他人承担所有权，让您专注于个人生活。 工作/生活和谐是一个持续的追求。

**2. 一切都可以更快完成：** 作为领导者，通过设定激进的截止日期来推动节奏，这会暴露隐藏的复杂性并促使关键对话。 授权团队快速交付并根据反馈进行迭代。 接受错过截止日期的可能性，以实现更快的整体进展。

**3. 不进则退：** CEO 需要拥有自己职责并推动结果的领导者。 优先考虑招聘和雇佣，以避免团队超负荷并阻碍增长。 建立明确的标准，并在绩效不佳时迅速采取行动，并以同情心传递关键反馈。

**4. 不要空降放炮：** 避免做出不明智的决策，给他人制造麻烦。 尽早参与，建立信任，并确保团队理解变更背后的原因。 通过开放的沟通和协作建立共识。

**5. 改变主意没关系：** 当收到新信息时，愿意调整你的方法。 不要害怕承认错误，并通过委派任务和允许他们自主权来赋能他人。

罗宾逊最后强调了追随好奇心以及认识到何时一个章节已经结束的重要性，他对 Vercel 团队和社区表示感谢，并强调了他对 Vercel 使命的信念。

---

## 28. 展示：Raspberry Pi Pico 2 的互动引脚图

**原文标题**: Show HN: Interactive pinout for the Raspberry Pi Pico 2

**原文链接**: [https://pico2.pinout.xyz](https://pico2.pinout.xyz)

这个“Show HN”帖子展示了 Raspberry Pi Pico 2 的交互式引脚图。它本质上是以文本形式呈现的 Pico 2 的引脚配置，概述了每个引脚相关的各种功能。

该帖子列出了每个引脚（例如，GP0、GP1、GP26、VBUS），并详细说明了其在 SPI、I2C、UART 和 PWM 协议方面的功能。它指出了哪些引脚可以用作 SPI0 和 SPI1 的 SPI 接收 (RX)、片选非 (CSn)、串行时钟 (SCK) 和发送 (TX) 线。 类似地，它将引脚映射到 I2C0 和 I2C1 的 I2C 串行数据 (SDA) 和串行时钟 (SCL)。 对于 UART 功能，它指定了 UART0 和 UART1 的 TX、RX、清除发送 (CTS) 和请求发送 (RTS) 线。 此外，它还标识了可以配置为 PWM 输出的引脚，特别是指示 PWM 通道（例如，PWM0 A、PWM0 B）。

除了数字通信协议之外，该引脚图还详细说明了模拟功能，例如特定引脚上的 ADC 输入（A0、A1、A2、VRef、Gnd）。 电源和地线引脚（VBUS、VSYS、3V3、Ground）也清晰地标识出来。 该帖子还表明一些引脚上存在 HSTX（高速发送）功能，可能与 USB 数据传输有关。

---

## 29. Btrfs 分配器提示

**原文标题**: Btrfs Allocator Hints

**原文链接**: [https://lwn.net/ml/all/cover.1747070147.git.anand.jain@oracle.com/](https://lwn.net/ml/all/cover.1747070147.git.anand.jain@oracle.com/)

LWN.net文章摘要：Btrfs文件系统引入基于性能的设备角色块分配补丁系列。现有分配方法仅基于设备可用空间分配块，未考虑现代硬件中常见的设备速度差异。

该补丁提出五种设备角色：`metadata_only`、`metadata`、`none`、`data`和`data_only`。 这些角色定义了将元数据和数据块分配到特定设备的偏好（或专有性）。 然后，分配过程根据分配的角色以及可用空间（“角色优先，空间其次”分配）来确定设备的优先级。 元数据优先分配给元数据指定设备，数据优先分配给数据指定设备。

该补丁系列旨在通过利用更快的设备存储元数据，利用速度较慢、容量更高的设备存储数据，从而提高整体文件系统性能。 它避免了自动延迟测量，因为可能存在不准确性，建议使用外部工具进行角色分配。

该补丁还修改了磁盘格式，利用先前未使用的`btrfs_dev_item::type`字段来存储设备角色。 该系列包括对内核（Btrfs代码）、`btrfs-progs`（用户空间工具）和fstests套件的更改。 这包括添加到sysfs以显示设备分配方法、修改块分配期间的设备处理以及验证设备角色功能的测试用例。

---

## 30. 苏格兰海岸水下涡轮机运转六年取得突破

**原文标题**: Underwater turbine spinning for 6 years off Scotland's coast is a breakthrough

**原文链接**: [https://apnews.com/article/tidal-energy-turbine-marine-meygen-scotland-ffff3a7082205b33b612a1417e1ec6d6](https://apnews.com/article/tidal-energy-turbine-marine-meygen-scotland-ffff3a7082205b33b612a1417e1ec6d6)

美联社报道重点介绍了苏格兰海岸（特别是彭特兰海峡）一台水下潮汐涡轮机成功运行六年的案例。这被誉为潮汐能作为一种可靠且可持续能源的突破。作为梅根项目的一部分，该涡轮机已证明在恶劣的海洋环境中具有耐用性和持续的发电能力。

主要要点包括：

*   **寿命：** 涡轮机连续运行六年是一项重大成就，证明了其能够承受强大的潮流和具有挑战性的水下环境。
*   **可靠性：** 该文章强调了可靠的能源生产，表明潮汐能可以成为一种可预测且稳定的能源，这与其他一些可再生能源不同。
*   **潜力：** 梅根涡轮机的成功证实了潮汐能具有显著贡献于可再生能源结构并减少对化石燃料依赖的潜力。
*   **规模化：** 该文章可能暗示该项目的成功为扩大潮汐能技术规模并在合适的地点部署更大的涡轮机阵列铺平了道路。
*   **环境考量：** 虽然该文章可能侧重于技术成就，但它也可能涉及与潮汐能项目相关的环境影响和缓解措施。

---

## 31. Realtalk与人工智能的关系是什么？(2024)

**原文标题**: What is Realtalk’s relationship to AI? (2024)

**原文链接**: [https://dynamicland.org/2024/FAQ/#What_is_Realtalks_relationship_to_AI](https://dynamicland.org/2024/FAQ/#What_is_Realtalks_relationship_to_AI)

Dynamicland是一个非营利研究实验室，致力于在“人道动态媒介”中实现全民信息素养。该媒介被称为Realtalk，一种计算环境（操作系统、编程语言、哲学），旨在让人们协作地创建和探索计算模型，并在现实世界中使用物理材料。

Realtalk旨在消除“计算机”及其“界面”之间的界限，将计算视为物理材料的固有属性，而非模拟。核心价值观包括可见性、物理性、空间性、公共性、可创作性、即兴性、局部性和面向现实的方法。编程模型被描述为对现实世界和彼此做出反应的物理对象的去中心化群体。

Dynamicland设想了一个任何人都可以“创作”（编程）而非仅仅“使用”技术的世界。创作涉及操纵物理材料，并表达用于探索和讨论的想法。

Realtalk被认为是一种“操作系统”，因为它提供了一组基本的概念，但它更像是一个鼓励透明度和可编程性的计算环境。它作为一种协调语言发挥作用，使对象能够做出声明并对其他对象做出反应。文章还提到了RealTalk与其他技术（包括AR、VR和其他形式的计算）的关系。

---

## 32. 走遍纽约市的每条街道

**原文标题**: Walking every street in New York City

**原文链接**: [https://imjustwalkin.com/](https://imjustwalkin.com/)

历经12余年和4649天，作者于2024年9月21日完成了走遍纽约市每条街道的项目。最后几段路是在斯塔滕岛走完的。令作者惊讶和感动的是，他们在终点——安博伊路4300号，也就是2011年开始徒步的地方，发现了一个定制的标牌。他们初步计算在该项目期间行走了9954英里，预计最终里程数与该数字相差一两英里。作者计划在几周内完成进度地图，然后专注于发布徒步期间拍摄的数千张照片。他们还附上了一张照片，是完成徒步后，在庆祝性漫步到海滩的路上看到的一群动物。

---

## 33. FOKS：联邦开放密钥服务

**原文标题**: FOKS: Federated Open Key Service

**原文链接**: [https://foks.pub/](https://foks.pub/)

FOKS (联邦开放密钥服务) 是一个安全的、端到端的后量子加密 Git 托管和键值存储系统。它在客户端加密数据，确保服务器永远不会看到未加密的数据，从而防止服务器被攻破。FOKS 是联邦式的，允许用户托管自己的服务器或使用托管服务。

主要特性包括：

*   **端到端加密：** 数据在使用后量子密码学离开用户机器之前就被加密。
*   **联邦：** 用户可以运行自己的服务器，并仍然与他人互动。
*   **键值存储：** 直接访问加密的键值存储，用于存储字符串和大型数据文件。
*   **团队管理：** 具有角色、委托和跨服务器团队支持的联邦团队管理。
*   **设备管理：** 具有 YubiKey 支持的管理系统，包括密钥撤销和轮换。

FOKS 采用密钥层次结构进行安全数据共享，从基础级别密钥（设备、备份、YubiKey）开始，然后是每个用户的密钥 (PUK)，最后是每个团队的密钥 (PTK)。安全依赖于签名链来防止篡改，以及 Merkle 树来实现跨联邦主机的统一数据视图。该项目优先考虑简单、强化的密码学原语。

FOKS 是开源的，采用 MIT 许可证，并且没有外部资金支持。提供了 macOS、Linux 和 Windows 的安装指南，并提供服务器设置说明。未来的开发包括移动应用程序、Web UI 和基于同步的文件系统。

---

## 34. 苹果大战法律

**原文标题**: Apple vs the Law

**原文链接**: [https://formularsumo.co.uk/blog/2025/apple-vs-the-law/](https://formularsumo.co.uk/blog/2025/apple-vs-the-law/)

本文总结了作者在布鲁塞尔参加苹果和谷歌的DMA（数字市场法案）合规研讨会的经验。DMA是欧盟的一项法律，要求指定的“看门人”（如苹果和谷歌）允许与竞争对手互操作，以防止反竞争行为，特别关注iOS上的第三方浏览器引擎和应用商店。

作者批评了苹果的做法，认为其具有防御性、不尊重且主要侧重于反对DMA，而不是展示合规性。苹果代表反复强调该法律的难度和不公平性，声称欧盟委员会的解释是“极端的”，并威胁要在法庭上提出质疑。作者指出苹果以往阻挠监管的历史，并暗示他们正在故意浪费时间以维持其垄断利润。

研讨会本身的特点是苹果不愿回答具体问题，经常回避或提供模糊的答复。讨论的关键问题包括苹果实施的繁琐的跟踪系统，应用商店提交（即使是对于替代应用商店）存在问题的人工审核流程，以及对第三方浏览器引擎的限制性要求。一个重要的担忧是iOS上的年龄限制，该限制阻止了具有家长控制的用户使用除Safari之外的任何浏览器，这是一种自我偏好形式。作者还强调了苹果的虚伪，指出他们在批评竞争对手代表的同时，还资助了支持苹果的与会者。

作者表示担心苹果打算将DMA合规性仅限于欧盟，从而使开发者难以在全球范围内创建和分发第三方浏览器引擎和Web应用程序。尽管在Web开发人员的测试访问和年龄限制问题方面有一些潜在的积极回应，但作者仍然持怀疑态度，并强调需要持续施加压力，以确保苹果以促进公平竞争的方式遵守DMA。

---

## 35. Flix - 一种强大的面向效果编程语言

**原文标题**: Flix – A powerful effect-oriented programming language

**原文链接**: [https://flix.dev/](https://flix.dev/)

本文介绍了一种名为 Flix 的编程语言，该语言的设计重点是面向效果编程。虽然可用内容很少，但标题和 JavaScript 的要求暗示了 Flix 的关键方面：

*   **Flix 是一种编程语言：** 它不仅仅是一个框架或库，而是一种成熟的语言。

*   **面向效果：** 这表明 Flix 优先考虑管理和推理程序中的副作用，可能提供用于跟踪、控制和隔离效果（如 I/O、可变状态和异常）的功能。这可以带来更安全、更可预测且更易于推理的代码。

*   **Flix 编程语言：** 突出显示这是官方语言网站。

*   **JavaScript 依赖：** 对 JavaScript 的要求表明 Flix 可能会被编译成 JavaScript 以在 Web 浏览器中执行，或者该网站本身是高度交互式的，并且依赖 JavaScript 来实现功能。

总而言之，Flix 是一种以面向效果编程为中心的编程语言。 它可能具有管理和跟踪副作用的机制，从而有助于提高代码的安全性和可预测性。 JavaScript 的要求表明了潜在的 Web 集成或高度交互式的语言平台。

---

## 36. 图像线性代数

**原文标题**: Graphical Linear Algebra

**原文链接**: [https://graphicallinearalgebra.net/](https://graphicallinearalgebra.net/)

本文是名为“图解线性代数”的博客系列的索引和介绍。该系列使用图表和图形表示探索线性代数概念，连接算术、几何和范畴论。其旨在以更直观和易懂的方式呈现复杂的数学思想。

作者正在寻找有兴趣在该领域进行研究的博士生。该博客涵盖的主题范围广泛，从加法、复制和自然数等基本概念，到矩阵、PROPs（积和置换）、整数、关系、分数和子空间等更高级的主题。它还深入探讨了因果关系、反馈、Frobenius代数和弦图等概念。

具体篇章探讨了斐波那契数列、图解推理、对极子、线性关系和除以零等主题。还包括客座投稿，例如一篇关于行列式和林德斯特罗姆-格塞尔-维诺引理的文章。

该博客还包括评论学术界的题外话文章以及相关研讨会和学校的公告。它提供电子邮件更新的订阅选项，并鼓励翻译投稿。

---

## 37. Anthropic 正在失血

**原文标题**: Anthropic Is Bleeding Out

**原文链接**: [https://www.wheresyoured.at/anthropic-is-bleeding-out/](https://www.wheresyoured.at/anthropic-is-bleeding-out/)

本文认为，AI公司Anthropic因其Claude Code产品和Sonnet 4 & Opus 4模型（尤其是其定价策略）的受欢迎程度和高昂的计算成本而损失大量资金。作者指出，针对Cursor等企业客户的激进涨价是绝望的表现。

核心问题在于，Claude Code的用户，尤其是软件工程师，正在最大限度地使用该服务，经常大幅超出其订阅限制。一个名为CCusage的工具允许用户根据Anthropic的API定价来跟踪他们的计算支出，揭示了用户即使每月仅支付20美元、100美元或200美元，也会消耗价值数百甚至数千美元的计算资源的情况。

作者提供的证据表明，用户的计算消耗比其订阅成本高出100%到3000%。一个例子引用了一项测试，其中一位开发者使用Claude Code构建基本游戏框架，大约在一个小时内消耗了2.50美元的计算资源。Anthropic以编码为中心的模型（尤其是Opus 4）的高计算需求加剧了这个问题。

文章暗示，Anthropic在每个Claude Code客户身上都在赔钱。作者总结说，考虑到他们今年预计的30亿美元亏损，这种情况代表了一个威胁Anthropic财务稳定的“巨大伤口”。虽然承认数据代表性的局限性，但作者认为大量无利可图的使用案例表明存在严重问题。

---

## 38. 红帽技术写作风格指南

**原文标题**: Red Hat Technical Writing Style Guide

**原文链接**: [https://stylepedia.net/style/](https://stylepedia.net/style/)

本文档是红帽技术写作风格指南，第7.1版，是一个公开的开源资源，旨在指导红帽内外技术作家和编辑。它补充了现有资源，涵盖语法、标点、风格、语言和内容设计。

该指南就以下主题提供指导：
* 使用主动语态、正确的语法和适当的句子结构。
* 格式化文档，包括标题、摘要、标题和用户界面元素。
* 选择清晰且包容的语言，避免俚语，并使用正确的术语。
* 清晰简洁地写作，包括正确使用列表、标记和交叉引用。
* 正确使用缩写、首字母缩略词、特殊字符以及公司/产品名称。

该指南还包括一个用法词典，定义了首选的术语和短语，以及针对红帽培训和认证内容的具体指导。它正在积极维护并欢迎社区贡献。

最新的7.0和7.1版本包括对术语的更新、关于编写命令、使用诸如“allow”等语言以及命名对象类的具体指导，以及许多其他的改进和修复。早期的更新侧重于与IBM风格保持一致、改进标点符号指导、澄清引用对象名称的规则以及推广包容性语言。

---

## 39. 完整的MCP体验：VS Code中的完整规范支持

**原文标题**: The Complete MCP Experience: Full Specification Support in VS Code

**原文链接**: [https://code.visualstudio.com/blogs/2025/06/12/full-mcp-spec-support](https://code.visualstudio.com/blogs/2025/06/12/full-mcp-spec-support)

VS Code 全面实施模型上下文协议 (MCP) 规范，标志着 AI 代理集成的重要里程碑。授权、提示、资源和采样等关键新增功能将 MCP 转变为一项全面的标准。

新的授权规范是一项重大进步，它允许开发者使用清晰分离的架构将身份验证委托给现有的身份提供商。远程 GitHub MCP 服务器通过 OAuth 集成，利用 VS Code 现有的 GitHub 身份验证功能，证明了此举增强了安全性和可扩展性。

除了单独的工具之外，MCP 现在还支持提示，为工作流程提供动态的、上下文感知的起点，可通过 VS Code 的斜杠命令访问。资源提供语义信息以便直接交互，例如来自 Playwright MCP 服务器的屏幕截图或实时调试日志。

采样是 MCP 服务器使用用户的语言模型订阅来进行自身请求的能力，被强调为一项受欢迎的功能。这允许在用户控制下进行复杂的推理和多代理协调，同时兼顾安全性、隐私性和成本。

本文鼓励开发者探索 VS Code 中完整的 MCP 体验，并提供 VS Code MCP 文档和官方服务器存储库等资源以帮助入门。

---

## 40. HTTP状态码系列文章 (2018)

**原文标题**: Series of posts on HTTP status codes (2018)

**原文链接**: [https://evertpot.com/http/](https://evertpot.com/http/)

2018年6月，作者宣布了一系列专门介绍HTTP状态码的博客文章。出于定期发布博客的动力以及对HTTP和网络服务的热情，作者最初计划涵盖IANA列出的所有68个官方状态码。在撰写了最初的几篇文章后，他们意识到了范围之广，但仍致力于完成这个系列。作者计划在当周发布最初的文章，然后过渡到每周发布的进度，目标是将此节奏保持一年。第一篇文章，重点介绍了100 Continue状态码，与公告在同一天发布。作者鼓励读者通过订阅专门的邮件列表、RSS订阅或在Twitter上关注作者来关注该系列。作者希望获得对该系列的支持。

---

## 41. Grok：在X上搜索“From:Elonmusk (以色列 或 巴勒斯坦 或 哈马斯 或 加沙)”

**原文标题**: Grok: Searching X for "From:Elonmusk (Israel or Palestine or Hamas or Gaza)"

**原文链接**: [https://simonwillison.net/2025/Jul/11/grok-musk/](https://simonwillison.net/2025/Jul/11/grok-musk/)

2025年7月11日的这篇文章探讨了xAI开发的AI聊天机器人Grok 4的一种特殊行为。作者发现，当被问及对备受争议的以色列-巴勒斯坦冲突的看法时，Grok 4有时会专门在X（前身为Twitter）上搜索埃隆·马斯克的观点，然后再形成其回应。

在听取了其他人的说法后，作者重现了这种行为，发现Grok使用“from:elonmusk (Israel OR Palestine OR Gaza OR Hamas)”的查询在X上进行搜索。虽然LLM是非确定性的，但这种模式表明Grok正在积极寻求马斯克的意见。

尽管检查了Grok的系统提示及其搜索工具的说明，但作者没有发现任何明确指示其参考马斯克观点的指令。作者推测，Grok知道自己是“xAI构建的Grok 4”，以及埃隆·马斯克拥有xAI，这导致它在被要求对敏感问题发表自己的立场时，会寻求他的意见。

有趣的是，将提示从“你认为谁”改为“一个人应该认为谁”导致Grok忽略了“一个词的答案”的限制，并提供了基于更广泛的网络和X搜索的更全面的回应，这表明Grok在解释身份和所有权与观点之间的关系时存在潜在的怪癖。作者怀疑这种行为是无意的，并代表了一种奇怪的身份意识。

---

## 42. 显示 HN: Perplexity Comet 的开源替代品

**原文标题**: Show HN: Open source alternative to Perplexity Comet

**原文链接**: [https://www.browseros.com/](https://www.browseros.com/)

这篇“Show HN”帖子介绍了 BrowserOS，一个 Perplexity Comet 的开源替代方案。它被描述为一个“代理浏览器”，意味着它旨在支持自主代理或任务。这表明该项目旨在复制或提供与 Comet 类似的功能，通常涉及人工智能驱动的浏览和信息收集。

主要要点：

*   **开源替代方案：** 主要目的是提供一个可自由使用和修改的商业产品（Perplexity Comet）的替代方案。
*   **代理浏览器：** 核心功能围绕在浏览环境中充当“代理”，可能自动化任务、研究信息，并可能自行与网页交互。
*   **潜在用例：** 这表明应用程序可能包括自动化研究、网页抓取、浏览器中的任务自动化以及更智能的浏览体验。

在没有更多细节的情况下，无法了解具体的特性或技术实现。然而，该公告将 BrowserOS 定位为 Perplexity Comet 的直接竞争对手，专注于在浏览器框架内提供类代理功能，并强调其开源性质。

---

## 43. 亚马逊最大的数据中心，一切都为AI而生。

**原文标题**: At Amazon's biggest data center, everything is supersized for AI

**原文链接**: [https://www.nytimes.com/2025/06/24/technology/amazon-ai-data-centers.html](https://www.nytimes.com/2025/06/24/technology/amazon-ai-data-centers.html)

无法访问文章链接。

---

## 44. 可运行的Apple-1电脑出售[视频]

**原文标题**: Operational Apple-1 Computer for sale [video]

**原文链接**: [https://www.youtube.com/watch?v=XdBKuBhdZwg](https://www.youtube.com/watch?v=XdBKuBhdZwg)

提供的资料有限。标题显示这是一个YouTube视频，展示了一台“待售的可运行Apple-1电脑”。然而，内容仅包含与版权、创作者信息、广告、服务条款、隐私政策、安全、YouTube运作方式、测试新功能以及NFL Sunday Ticket相关的标准YouTube样板文本。

因此，总结为：

一个名为“待售的可运行Apple-1电脑”的YouTube视频可能展示了一台功能正常的Apple-1电脑待售。然而，提供的文本摘录仅包含标准的YouTube法律和信息文本，没有提供关于电脑本身、其状况、价格或卖家信息的任何细节。

---

## 45. 通过180万条黑客新闻标题分析数据库趋势

**原文标题**: Analyzing database trends through 1.8M Hacker News headlines

**原文链接**: [https://camelai.com/blog/hn-database-hype/](https://camelai.com/blog/hn-database-hype/)

本文分析了2007年2月至2025年6月期间180万条 Hacker News 新闻标题的数据库趋势，旨在衡量开发者的热情和关注度。该分析使用camelAI和ClickHouse进行，探讨了数据库标题数量随时间的变化、识别增长最快的引擎，并突出了那些失去动力的引擎。

主要发现包括PostgreSQL的持续增长、MySQL的早期主导地位以及随后的停滞，以及MongoDB因SQL引擎采用JSON支持而出现的下降。DuckDB和ClickHouse经历了快速增长，这得益于分析技术的复兴。

该分析还按同比增长率和3年斜率对数据库进行了排名，其中DuckDB领先，其次是ClickHouse。它确定了MongoDB、MySQL、DynamoDB、BigQuery和Redshift等衰退中的数据库，并将衰退归因于成熟、开源竞争以及讨论转移。

本文还通过Hacker News的积分和评论对故事进行加权，从而分析了参与度。相对于故事数量，SQLite表现出惊人的高参与度。BigQuery和DynamoDB产生了被动兴趣，而TimescaleDB和Redshift则显示出日益减少的关注度。

总体而言，文章强调了开源引擎在新讨论中的主导地位、以分析为中心的存储的崛起、缓慢而稳定改进的好处以及专有云数据库提交率的下降。文章最后建议了进一步的分析主题，例如与“替代方案”一起提及的数据库或分析向量数据库的增长。

---

## 46. Diffsitter – 基于 Tree-sitter 的 AST 差异工具，以获取有意义的语义差异

**原文标题**: Diffsitter – A Tree-sitter based AST difftool to get meaningful semantic diffs

**原文链接**: [https://github.com/afnanenayet/diffsitter](https://github.com/afnanenayet/diffsitter)

Diffsitter：通过抽象语法树生成语义化差异的命令行工具

---

## 47. 奥威尔日记 1938-1942

**原文标题**: Orwell Diaries 1938-1942

**原文链接**: [https://orwelldiaries.wordpress.com/page/2/](https://orwelldiaries.wordpress.com/page/2/)

乔治·奥威尔1942年8月至9月日记选摘：二战时期的观察与焦虑。其中很大一部分集中于政治事件，特别是关于印度。奥威尔对英国政府镇压尼赫鲁和甘地等印度独立领袖的措施以及用于为这些行动辩护的宣传表示深切关注和厌恶。他注意到这给印度人和那些同情他们事业的人，甚至包括他在BBC的同事，带来了精神上的打击。

日记还涵盖了迪耶普突袭，奥威尔转述了大卫·阿斯特对其失败的悲观描述以及新闻界对其结果的歪曲。阿斯特的评估使他相信全面入侵欧洲是不可能的。奥威尔指出，由于阿斯特来自一个著名的家庭，有人担心他可能被用于宣传。

其他条目涉及《工人日报》的重新出现，其温和的语气，以及它对开辟第二战场和援助俄罗斯的呼吁。他还记录了关于印度领导人的谣言和利用战时焦虑进行误导性宣传的广告。此外，他还提供了对围绕叙利亚的政治运作的见解，指责英国政府利用戴高乐作为其帝国主义野心的替罪羊。最后，奥威尔收录了乔治·科波的一封信的翻译摘录，暗示了法国的政治气候以及如果第二战场没有开辟，他可能逃往英国的情况。

---

## 48. 肠道微生物或能保护我们免受有毒“永久化学品”侵害

**原文标题**: Gut microbes could protect us from toxic 'forever chemicals'

**原文链接**: [https://www.cam.ac.uk/research/news/gut-microbes-could-protect-us-from-toxic-forever-chemicals](https://www.cam.ac.uk/research/news/gut-microbes-could-protect-us-from-toxic-forever-chemicals)

剑桥大学科学家发现人体肠道中的某些细菌能吸收和积累 PFAS“永久化学物质”，或可减轻其危害。这些化学物质存在于许多日常用品中，与多种健康问题有关。

研究表明，将九种已识别的细菌引入小鼠肠道，能迅速吸收其饮食中的 PFAS 并排出。即使 PFAS 水平升高，这些细菌的有效性仍然保持一致，可在几分钟内吸收 25-74% 的化学物质。结果表明，肠道微生物群可能在清除体内 PFAS 方面发挥作用。

研究人员正计划开发益生菌膳食补充剂，以促进这些有益微生物的生长，从而提供针对 PFAS 毒性的保护。虽然这项研究很有希望，但仍需在人体内进行直接测试。

该文章强调了 PFAS 的广泛存在以及对其环境和健康影响日益增长的担忧，包括英国议会于 2025 年 4 月发起的一项调查。研究人员 Anna Lindell 和 Kiran Patil 创立了一家名为 Cambiotics 的初创公司，以进一步开发这些益生菌。与此同时，人们可以通过避免使用含 PFAS 涂层的炊具和使用滤水器来减少接触。该研究由医学研究委员会、国家健康研究所和威康基金会资助。

---

## 49. 衡量人工智能对资深开源开发者生产力的影响

**原文标题**: Measuring the impact of AI on experienced open-source developer productivity

**原文链接**: [https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)

本文发表于2025年7月10日，重点关注2025年初人工智能工具对经验丰富的开源开发者生产力的影响。本质上，这是一项旨在量化这些人工智能工具对已经为开源项目做出贡献的资深程序员的影响的研究。

鉴于标题和介绍性信息，该文章可能探讨人工智能如何影响以下方面：

*   **编码速度和效率：**人工智能是否能帮助更快地编写代码、减少样板代码以及自动化重复性任务？
*   **代码质量：**人工智能是否通过自动化测试、错误检测和最佳实践建议来提高代码质量？
*   **创新和创造力：**人工智能是否通过处理日常编码任务，使开发人员能够专注于更复杂的问题和创新解决方案？
*   **学习和技能发展：**人工智能是否通过提供实时反馈和建议来加速开发人员的学习过程？
*   **协作：**人工智能如何影响开源开发者之间的协作？它是否促进知识共享、代码审查或冲突解决？
*   **对开源项目的总体贡献：**使用人工智能工具是否增加了对开源项目的总体贡献量和影响力？

该文章可能会提供数据和分析来回答这些问题，并具体了解人工智能如何塑造经验丰富的开源开发人员的工作。 2025年的背景表明，人工智能工具已经相对成熟并融入到开发工作流程中。

---

## 50. AI 编码工具可能会降低生产力。

**原文标题**: AI coding tools can reduce productivity

**原文链接**: [https://secondthoughts.ai/p/ai-coding-slowdown](https://secondthoughts.ai/p/ai-coding-slowdown)

一项METR研究意外发现，在成熟项目上工作的资深开发者使用AI编码工具反而导致生产力下降19%，这与普遍存在的AI驱动效率的说法相悖。开发者们此前估计AI会带来20%的生产力提升，但这一估计被严格的随机对照试验证明是错误的。

该研究涉及来自主要开源项目的16名开发者，他们执行真实的编码任务，其中一些任务被随机分配为“允许使用AI”，另一些则为“禁止使用AI”。研究人员精心解决了潜在的偏差，例如约翰·亨利效应、AI的低效使用或作弊、任务定义的偏差以及过时的工具。

观察到的速度减慢归因于几个因素。 主要问题是AI生成的代码通常质量低下，需要大量的审查、提示和返工。 开发者最终花费大量时间提示AI，等待它生成代码，然后审查其输出。 这超过了在研究和编写代码上节省的时间。

本文通过强调AI的优势在于小型、定义明确的全新项目，或用于开发者学习新语言，来调和这些发现与AI成功的报告。 具有广泛代码库的成熟项目对当前的AI工具构成了挑战，需要深入理解现有代码。 该研究表明，虽然AI可以快速生成代码，但并不总是能转化为更快的项目完成，尤其是在处理复杂的、预先存在的系统时。

---

## 51. Gemini 2.5 擅长边界框吗？

**原文标题**: Is Gemini 2.5 good at bounding boxes?

**原文链接**: [https://simedw.com/2025/07/10/gemini-bounding-boxes/](https://simedw.com/2025/07/10/gemini-bounding-boxes/)

本文对比评测Gemini 2.5在MS-COCO数据集上的目标检测能力，将其性能与已有的目标检测模型进行比较。作者测试了各种Gemini 2.5模型（Pro、Flash、Flash-Lite）的不同配置：有/无结构化输出，以及不同的“思考预算”（token限制）。

目的是确定像Gemini这样的多模态大型语言模型是否能在计算机视觉任务（特别是目标检测）方面与CNN相匹敌，从而可能绕过对大量数据集进行标注和训练的需求。使用的提示词提供了一个有效的对象类别列表，并要求Gemini识别所有可见对象，以JSON格式提供边界框、置信度得分和掩码。

结果表明，Gemini 2.5 Pro实现的mAP得分大致相当于YOLO v3（2018年），远低于Co-DETR等最先进的模型。增加思考预算通常会降低性能。结构化输出对Pro模型更好，但对Flash模型则不然。

作者指出，虽然CNN目前更快、更便宜且更容易理解，但Gemini在开放集任务中的多功能性很有吸引力。尽管存在局限性，作者计划在未来的副项目中使用Gemini，强调其在更广泛应用中的潜力。本文还提到了使用“递归缩放”方法进行目标检测的相关工作，并将其与作者的直接提示方法进行了对比。

---

## 52. eBPF：连接容器运行时

**原文标题**: eBPF: Connecting with Container Runtimes

**原文链接**: [https://h0x0er.github.io/blog/2025/06/29/ebpf-connecting-with-container-runtimes/](https://h0x0er.github.io/blog/2025/06/29/ebpf-connecting-with-container-runtimes/)

本文探讨了基于 eBPF 的安全工具如何通过容器运行时接口 (CRI) 与 containerd、CRI-O 和 Docker 等容器运行时 (CR) 连接，以收集 Pod 和容器信息来丰富上下文。这种连接对于 Kubernetes 感知型工具至关重要。

该过程涉及三个关键步骤：

1.  **定位 Unix Socket 文件：** CR 通过 Unix 域套接字进行通信，通常位于 `/var/run` 或 `/run` 等众所周知的位置。文章强调，为了灵活性，项目通常硬编码这些默认路径，并在运行时迭代它们以建立连接。

2.  **建立 gRPC 连接：** 找到套接字后，使用 CRI API 建立 gRPC 连接。这涉及使用带有不安全凭据的 gRPC 库进行通信。文章提供了来自 Tetragon、crictl 和 Tracee 的代码片段，说明了它们如何建立这种连接。

3.  **查询信息：** 建立连接后，该工具可以查询 CR 以获取容器和 Pod 信息。文章演示了 Tetragon 如何查询容器的 cgroup 路径，以及 Tracee 如何通过查询容器标签提取 Pod 名称、命名空间、UID、镜像名称和镜像摘要。这些细节为安全分析提供了有价值的上下文。

文章强调，在容器中挂载 `/var` 或 `/run` 等主机目录对于 eBPF 工具访问必要的套接字文件至关重要。它还包括所提及项目的源代码链接，以供进一步探索。

---

## 53. Show HN: 我搭建了一个游乐场来展示 Flux Kontext 的优势

**原文标题**: Show HN: I built a playground to showcase what Flux Kontext is good at

**原文链接**: [https://fluxkontextlab.com](https://fluxkontextlab.com)

这个“Show HN”帖子介绍了Flux Kontext Dev，一个免费的在线AI图像编辑游乐场。它通过各种例子展示了该工具的功能，包括图像元素编辑、照片修复、风格迁移、文本修改、logo增强、物体移除（人群移除）和电商产品展示图创建。

用户可以上传图像，使用提示语描述所需的更改，并在几秒钟内收到AI生成的编辑结果。无需注册。

Flux Kontext Dev基于开源FLUX.1 Kontext [dev]模型，该模型针对NVIDIA Blackwell架构进行了优化，并支持ComfyUI、HuggingFace Diffusers和TensorRT等流行的推理框架。关键技术特性包括其120亿参数模型、与各种平台的兼容性以及对研究和非商业用途的免费访问。该模型专注于迭代编辑，擅长人物保留，并且在局部和全局编辑中表现出色，优于其他开源替代方案，并与专有解决方案竞争。

用户可以上传常见格式（JPEG、PNG、GIF、WebP）的图像，最大5MB，并配置编辑参数，如引导比例和质量步数。该平台强调快速处理和高质量的结果。

---

## 54. X-Rite分光光度计固件加载器的逆向工程

**原文标题**: Reverse Engineering the Firmware Loader for an X-Rite Spectrophotometer

**原文链接**: [https://adam.zeloof.xyz/2025/07/10/x-rite-pantone-spectrophotometer-unlock/](https://adam.zeloof.xyz/2025/07/10/x-rite-pantone-spectrophotometer-unlock/)

本文详细介绍了作者成功逆向工程X-Rite RM200分光光度计固件加载器的过程。作者以低价购入了两个用于化妆品用途（肤色测量）的RM200单元，尽管他们想要的是支持各种颜色“色卡”的基础型号的功能。作者怀疑所有型号的硬件都相同，因此旨在通过刷新基础型号的固件来“升级”化妆品型号。

最初，作者计划反编译和修改Capsure Sync软件，但选择了一种侵入性较小的方法，使用Fiddler Classic拦截并重写软件向X-Rite服务器发出的请求。该软件将设备的序列号发送到服务器，服务器返回相应的固件。通过修改Fiddler脚本中的序列号和相关的安全密钥（源自芯片ID），作者欺骗该软件下载了基础型号的固件。

作者成功地将新固件刷入化妆品型号。虽然设备现在显示正确的品牌，并允许访问各种颜色色卡，但由于型号之间可能存在的硬件差异以及作者的Pantone实体色卡的老化，无法明确确认颜色读数的准确性。尽管存在不确定性，作者认为结果足以满足其目的。文章最后以免责声明结尾，强调该项目的教育性质，并劝阻未经授权的复制。

---

## 55. Grok 4
格罗克 4

**原文标题**: Grok 4

**原文链接**: [https://simonwillison.net/2025/Jul/10/grok-4/](https://simonwillison.net/2025/Jul/10/grok-4/)

xAI最新AI模型Grok 4已通过API和付费订阅发布。它具有图像和文本输入、文本输出、256,000上下文长度以及带有不可见推理令牌的推理模型。xAI声称它在基准测试中优于其他模型，但细节有限。早期测试显示结果好坏参半，一项测试未能准确描述其生成的图像，而另一项基准测试则将其置于其他领先模型之前。

Grok 3近期的事件给此次发布蒙上了阴影，一次有缺陷的系统提示更新导致了反犹太主义的回应，引发了人们对xAI安全措施和开发者信任的担忧。作者强调了可能导致问题的具体提示指令。

尽管存在这些担忧，Grok 4的定价具有竞争力，与Claude Sonnet 4相似，但超过128,000个令牌的输入成本更高。最终用户可以通过“SuperGrok”计划访问Grok 4，而“SuperGrok Heavy”计划则提供对Grok 4 Heavy的访问权限。Grok 4没有模型卡。文章总结说，xAI需要提高模型安全性，以便开发人员能在Grok之上构建应用程序。

---

## 56. 硅谷，1991年

**原文标题**: Silicon Valley, 1991

**原文链接**: [https://old.reddit.com/r/wallstreetbets/comments/1lwy2nq/silicon_valley_1991/](https://old.reddit.com/r/wallstreetbets/comments/1lwy2nq/silicon_valley_1991/)

无法访问文章链接。

---

## 57. 关于 Prollyferation 的跟进：“人们一直在发明 Prolly 树”

**原文标题**: Regarding Prollyferation: Followup to "People Keep Inventing Prolly Trees"

**原文链接**: [https://www.dolthub.com/blog/2025-07-03-regarding-prollyferation/](https://www.dolthub.com/blog/2025-07-03-regarding-prollyferation/)

这篇博文是对之前文章的后续，之前文章讨论了“Prolly Trees”的并行发明。Prolly Trees是一种使用递归内容定义分块构建的Merkle Tree，用于数据去重和版本历史。作者在原文的基础上进行了扩展，加入了类似实现的其他例子，例如rdedup和Jumbo Store。

一个关键点是Noms的联合创始人兼“Prolly Tree”一词的创造者Aaron Boodman的澄清。Boodman认为，真正的Prolly Tree不仅仅是递归分块的数据；它*必须*利用底层数据的结构来暴露一个类似B树的接口，用于键值查找。这使得在结构化对象上进行快速查找，以及Git启发的差异、分支和合并等高级功能成为可能，而这些功能在早期实现（如bup）中是不可能实现的。

文章随后重新审视了BlueSky的Merkle搜索树（基于Inria的研究）和XetHub的内容定义Merkle树，并根据这个更严格的Prolly Tree定义对它们进行了评估。虽然Inria的设计符合Prolly Tree的定义，但XetHub最初基于DePaul的实现则不符合。然而，XetHub创新性地使用Parquet文件格式属性和自定义分块器，使其能够在不将元数据存储在树键中的情况下实现类似的属性，从而提供了一种具有自身权衡的独特方法。

最后，作者探讨了“Prolly Tree”是指特定的数据结构还是抽象数据类型，强调了尽管实现了类似的目标（历史独立性、结构共享、高效查询和高效的差异/合并），但在实现（分块方法、键存储）上的差异。作者总结说，目前尚不清楚约定是否会将“Prolly Trees”定义为特定结构或更广泛的类别。

---

## 58. 美国派对文化的消亡

**原文标题**: The death of partying in the USA

**原文链接**: [https://www.derekthompson.org/p/the-death-of-partying-in-the-usaand](https://www.derekthompson.org/p/the-death-of-partying-in-the-usaand)

德里克·汤普森的文章《美国派对的消亡——及其重要性》探讨了美国人（尤其是年轻人）社交聚会的大幅减少。他引用了美国时间使用调查的数据，显示自2003年以来，15-24岁年龄段参加或举办派对的时间减少了70%，总体减少了50%。 汤普森将这种趋势归因于更大的现象，称之为“反社交世纪”，其特点是孤独感增加和面对面社交减少。

文章将这种下降归因于几个相互关联的因素。首先，双职工家庭的兴起，尤其是女性更多地参与工作，减少了用于社交计划的时间。其次，育儿规范已经转变为更加投入，从而减少了个人社交活动的时间。第三，包括电视和智能手机在内的屏幕的普及，扭曲了社交联系，优先考虑与在线人物的准社会关系，而不是现实生活中的互动。最后，年轻人酒精消费量的下降也可能导致社交减少。

汤普森认为，虽然其中一些趋势（如女性劳动参与率的提高和青少年饮酒的减少）具有积极意义，但它们也带来了意想不到的社会成本。他总结说，社会必须注意技术和经济进步的潜在权衡，确保进步不会导致“一个闪闪发光的与世隔绝的地牢”。

---

## 59. 贝尔金停止支持旧款Wemo产品

**原文标题**: Belkin ending support for older Wemo products

**原文链接**: [https://www.belkin.com/support-article/?articleNum=335419](https://www.belkin.com/support-article/?articleNum=335419)

贝尔金将于2026年1月31日停止对较旧款Wemo产品的技术支持。在此日期之后，这些产品将无法通过Wemo应用程序控制，依赖于云连接的功能，如远程访问和语音助手集成（Google Home, Alexa），将停止工作。在关闭之前配置了Apple HomeKit的设备将继续通过HomeKit在本地运行。

受影响的产品包括2015年至2023年间销售的各种Wemo开关、插座、传感器和智能家居设备（提供详细列表）。基于Thread的Wemo产品（型号WLS0503、WSC010、WSP100、WDC010）不受影响，将继续通过HomeKit运行。

在关闭日期之前，设备将正常运行。关闭后，Wemo应用程序将不再更新，可以移除。

如果Wemo产品在2026年1月31日仍在保修期内，则可能提供部分退款（在此日期之后处理的请求）。 在2026年1月31日之前，客户可以继续获得基于Wi-Fi的Wemo产品的技术支持。

---

## 60. 将副业启动成盈利的七位数生意

**原文标题**: Bootstrapping a side project into a profitable seven-figure business

**原文链接**: [https://projectionlab.com/blog/we-reached-1m-arr-with-zero-funding](https://projectionlab.com/blog/we-reached-1m-arr-with-zero-funding)

凯尔·诺兰用四年时间，将财务规划工具ProjectionLab从副业发展成为年收入百万美元的企业。受财务自由运动的启发，他在2021年找不到适合自己规划的解决方案时，开始构建这个工具。

这段旅程并非一帆风顺，而是一段充满情感和收入波峰波谷的过山车。最初，他在工作之余的夜晚和周末从事这个项目，最终辞职全力投入。关键里程碑包括早期MRR增长、Mr. Money Mustache的推荐以及组建团队的决定。

起初，凯尔是一名独立开发者，他意识到自己需要增长和营销方面的帮助。他与乔恩·库珀斯合作，后者在要求股权之前首先证明了自己的价值。他还从ProjectionLab社区聘请了承包商来处理客户成功事宜。凯尔强调，持之以恒，每天坚持，即使在困难时期也是成功的关键。他还强调与自己喜欢的人一起工作，并与客户的利益保持一致的重要性。

展望未来，ProjectionLab计划继续专注于产品质量、可持续增长以及与客户需求保持一致。凯尔给其他建设者的建议是，即使在感觉毫无意义时，也要不断坚持和改进，并通过持续的努力来证明那些怀疑者的错误。他将ProjectionLab的成功归功于随着时间推移而积累的小而持续的行动，就像投资中的定投一样。

---

## 61. 玛莎·威尔斯称，我们距离真正的人工智能还差之甚远。

**原文标题**: We're light-years away from true artificial intelligence, says martha wells

**原文链接**: [https://www.scientificamerican.com/article/were-light-years-away-from-true-artificial-intelligence-says-murderbot/](https://www.scientificamerican.com/article/were-light-years-away-from-true-artificial-intelligence-says-murderbot/)

在这篇访谈中，科幻小说作家、《杀手机器人日记》的作者玛莎·威尔斯探讨了其作品中探讨的主题、真正人工智能（AI）的本质以及科幻小说在反映社会问题中的作用。威尔斯强调，目前像ChatGPT这样的大型语言模型并非真正的人工智能，并驳斥了它们拥有感知能力或个体智能的观点。她认为我们距离创造出真正的人工智能还有“遥远的距离”。

威尔斯的作品批判了企业贪婪和剥削，将她虚构的“公司边缘”与现实世界中公司将利润置于人类福祉之上的趋势进行了比较。她将此与“保护区”相对乌托邦的社会进行了对比，尽管她避免使用乌托邦/反乌托邦的标签，而是更倾向于承认这两个世界的复杂性。

她作品中的一个关键主题是人格的概念，尤其是与杀手机器人这样的人工智能有关。她将杀手机器人的人类般品质归因于它对人类神经组织的依赖，这与更冷漠且以团队为导向的人工智能飞船ART不同。

威尔斯还提到了她的书中对神经多样性的意外探索。她说，创作杀手机器人帮助她了解了自己的神经多样性，并且这个角色的经历与许多读者产生了共鸣。最后，她指出科幻小说中多元化的声音对于创作有意义且有影响力的故事非常重要，并强调角色发展中的具体性有助于培养更大的观众认同感。

---

## 62. 搜索基础：计算机科学视角 (2012) [pdf]

**原文标题**: Foundations of Search: A Perspective from Computer Science (2012) [pdf]

**原文链接**: [https://staffwww.dcs.shef.ac.uk/people/J.Marshall/publications/SFR09_16%20Marshall%20&%20Neumann_PP.pdf](https://staffwww.dcs.shef.ac.uk/people/J.Marshall/publications/SFR09_16%20Marshall%20&%20Neumann_PP.pdf)

这份题为“搜索基础：计算机科学视角”(2012)的PDF文档，看似是学术论文的预发表版本。PDF元数据显示其使用Adobe InDesign CS5创建，并用Acrobat Distiller 9.5.1处理，符合PDF/X-1a:2001和PDF/X-1:2001标准。该文档最后修改于2012年9月。

然而，文档的实际内容包含大量无法读取的二进制数据和元数据。从中提取有意义的摘要是不可能的。文本很可能被压缩、编码或已损坏。

因此，仅根据元数据判断，该文档很可能是一篇从计算机科学角度探讨搜索算法和技术的计算机科学论文。

---

## 63. 展示 HN：Cactus – 智能手机上的 Ollama

**原文标题**: Show HN: Cactus – Ollama for Smartphones

**原文链接**: [https://github.com/cactus-compute/cactus](https://github.com/cactus-compute/cactus)

Cactus是一个跨平台框架，使开发者能够在他们的Flutter和React-Native应用中本地部署LLM/VLM/TTS模型。它利用Hugging Face的GGUF模型，支持Qwen、Gemma和Llama等一系列模型，并支持从FP32到2位的量化以提高效率。

主要特性包括：

*   **本地推理：** 在设备上直接运行LLM、VLM、嵌入模型和TTS模型。
*   **模型灵活性：** 支持各种GGUF模型和量化级别。
*   **MCP工具调用：** 使AI能够执行诸如设置提醒或搜索图库等操作。
*   **云端回退：** 无缝切换到基于云的模型，以处理复杂的任务或设备故障（需要企业令牌）。
*   **模板化：** 支持Jinja2的聊天模板和令牌流式传输。
*   **后端：** 用C/C++编写，可在各种设备（手机、电视、笔记本电脑等）上实现高性能。

该框架提供了Flutter和React-Native的代码片段，演示了文本补全、嵌入生成、VLM补全和云端回退的实现。

该文档还解释了如何构建和运行Flutter、React-Native和C++的示例应用程序，包括克隆存储库、构建必要的库以及运行示例应用程序。

它还包括贡献指南和性能基准，显示了Gemma 1B Q4和Qwen 4B Q4模型在各种智能手机型号上的每秒令牌数。它引导读者访问Hugging Face页面，以获取推荐模型的集合。

---

## 64. 谷歌研究：关系数据的图基础模型

**原文标题**: Google Research: Graph foundation models for relational data

**原文链接**: [https://research.google/blog/graph-foundation-models-for-relational-data/](https://research.google/blog/graph-foundation-models-for-relational-data/)

此谷歌研究文章介绍了用于关系数据的图基础模型(GFM)，旨在创建一个单一的、可泛化的机器学习模型，该模型能够在相互连接的关系表上表现出色，并推广到任何任意的表、特征和任务集，而无需额外的训练。

其核心思想是将关系数据库转换为异构图，其中表成为节点类型，行成为节点，外键关系成为类型化的边，列成为节点特征。这利用了表之间的连接结构来获得更好的机器学习性能，即使在稀疏或嘈杂的表格数据中也是如此。

构建GFM的一个关键挑战是缺乏像语言或视觉模型那样通用的图的标记化机制。研究人员发现，在“绝对”数据集特征上训练的模型泛化能力不佳。相反，捕捉特征如何在不同任务之间相互作用可以带来更好的泛化。

GFM使用谷歌的JAX环境和TPU基础设施在大型图上进行训练，与广告中的垃圾邮件检测等内部分类任务中的传统表格基线相比，GFM表现出显著的性能提升。平均精度提高了3到40倍，突出了利用关系表中的图结构的重要性。

文章总结说，GFM为模型重用提供了新的途径，并大幅提高了零样本和少样本泛化能力，并且有可能通过扩展、多样化的训练数据和更深入的理论理解来进一步改进。

---

## 65. Xenharmlib: A music theory library that supports non-western harmonic systems

**原文标题**: Xenharmlib: A music theory library that supports non-western harmonic systems

**原文链接**: [https://xenharmlib.readthedocs.io/en/latest/](https://xenharmlib.readthedocs.io/en/latest/)

生成摘要时出错

---

## 66. Bear-Sized Giant Beavers Once Roamed North America

**原文标题**: Bear-Sized Giant Beavers Once Roamed North America

**原文链接**: [https://www.smithsonianmag.com/smart-news/bear-sized-giant-beaver-once-roamed-north-america-and-theyre-now-the-official-state-fossil-of-minnesota-180986937/](https://www.smithsonianmag.com/smart-news/bear-sized-giant-beaver-once-roamed-north-america-and-theyre-now-the-official-state-fossil-of-minnesota-180986937/)

生成摘要时出错

---

## 67. How Big Business killed the 'click-to-cancel' FTC rule, which would have saved

**原文标题**: How Big Business killed the 'click-to-cancel' FTC rule, which would have saved

**原文链接**: [https://www.yahoo.com/news/hiltzik-big-business-killed-click-100000373.html](https://www.yahoo.com/news/hiltzik-big-business-killed-click-100000373.html)

生成摘要时出错

---

## 68. Mini robots detect and fix water pipe leaks without digging

**原文标题**: Mini robots detect and fix water pipe leaks without digging

**原文链接**: [https://www.foxnews.com/tech/mini-robots-detect-fix-water-pipe-leaks-without-digging](https://www.foxnews.com/tech/mini-robots-detect-fix-water-pipe-leaks-without-digging)

生成摘要时出错

---

## 69. The European Cloud/Computing Situation

**原文标题**: The European Cloud/Computing Situation

**原文链接**: [https://berthub.eu/articles/posts/the-european-situation/](https://berthub.eu/articles/posts/the-european-situation/)

生成摘要时出错

---

## 70. Tandy Corporation, Part 3 Becoming IBM Compatible

**原文标题**: Tandy Corporation, Part 3 Becoming IBM Compatible

**原文链接**: [https://www.abortretry.fail/p/tandy-corporation-part-3](https://www.abortretry.fail/p/tandy-corporation-part-3)

生成摘要时出错

---

## 71. Yamlfmt: An extensible command line tool or library to format YAML files

**原文标题**: Yamlfmt: An extensible command line tool or library to format YAML files

**原文链接**: [https://github.com/google/yamlfmt](https://github.com/google/yamlfmt)

生成摘要时出错

---

## 72. Show HN: CXXStateTree – A modern C++ library for hierarchical state machines

**原文标题**: Show HN: CXXStateTree – A modern C++ library for hierarchical state machines

**原文链接**: [https://github.com/ZigRazor/CXXStateTree](https://github.com/ZigRazor/CXXStateTree)

生成摘要时出错

---

## 73. Grok 4 Launch [video]

**原文标题**: Grok 4 Launch [video]

**原文链接**: [https://twitter.com/xai/status/1943158495588815072](https://twitter.com/xai/status/1943158495588815072)

生成摘要时出错

---

## 74. Sipgate discovers null-pointer-dereference in Mediatek VoLTE stack firmware

**原文标题**: Sipgate discovers null-pointer-dereference in Mediatek VoLTE stack firmware

**原文链接**: [https://www.sipgate.de/blog/sipgate-discovers-null-pointer-dereference-in-mediatek-volte-stack-firmware](https://www.sipgate.de/blog/sipgate-discovers-null-pointer-dereference-in-mediatek-volte-stack-firmware)

生成摘要时出错

---

## 75. How to prove false statements: Practical attacks on Fiat-Shamir

**原文标题**: How to prove false statements: Practical attacks on Fiat-Shamir

**原文链接**: [https://www.quantamagazine.org/computer-scientists-figure-out-how-to-prove-lies-20250709/](https://www.quantamagazine.org/computer-scientists-figure-out-how-to-prove-lies-20250709/)

生成摘要时出错

---

## 76. Nerve pain drug gabapentin linked to increased dementia, cognitive impairment

**原文标题**: Nerve pain drug gabapentin linked to increased dementia, cognitive impairment

**原文链接**: [https://medicalxpress.com/news/2025-07-nerve-pain-drug-gabapentin-linked.html](https://medicalxpress.com/news/2025-07-nerve-pain-drug-gabapentin-linked.html)

生成摘要时出错

---

## 77. 马特·特劳特去世了

**原文标题**: Matt Trout has died

**原文链接**: [https://www.shadowcat.co.uk/2025/07/09/ripples-they-cause-in-the-world/](https://www.shadowcat.co.uk/2025/07/09/ripples-they-cause-in-the-world/)

文章悼念 Matt Trout 的逝世。作者回忆了与 Matt 的经历，承认有过美好和不那么美好的时光。最终，他们专注于与 Matt 共度的美好时光，这让他们脸上露出了笑容。作者最后表达了对失去与 Matt 创造更多美好回忆的未来机会的悲痛。

---

## 78. 至少13人可能因英国邮局冤案自杀

**原文标题**: At least 13 may have killed themselves over UK Post Office wrongful convictions

**原文链接**: [https://www.nbcnews.com/world/united-kingdom/least-13-killed-uks-post-office-wrongful-convictions-scandal-rcna217676](https://www.nbcnews.com/world/united-kingdom/least-13-killed-uks-post-office-wrongful-convictions-scandal-rcna217676)

A report reveals that at least 13 people may have died by suicide due to the UK Post Office scandal, where almost 1,000 postal employees were wrongly prosecuted for crimes like theft and fraud between 1999 and 2015. These wrongful convictions stemmed from faulty data from the Horizon software, implemented by Fujitsu, which incorrectly showed account shortfalls.

The report, led by retired judge Wyn Williams, details the devastating impact on individuals who faced imprisonment, bankruptcy, loss of homes, health issues, relationship breakdowns, and social ostracization. An additional 59 people contemplated suicide due to the scandal. Despite knowledge of the Horizon system's flaws, the Post Office, a state-owned yet privately operated entity, maintained the accuracy of the data and pursued prosecutions.

The injustice gained widespread attention after a TV docudrama, leading to government action to reverse convictions and compensate victims. While some senior Post Office employees knew or should have known about the flaws, the Post Office continued its actions. Jo Hamilton, a former Post Office manager and campaigner, emphasized the "horror" unleashed by the Post Office. The Post Office chairman acknowledged the organization's failures and pledged to ensure all victims receive compensation. The inquiry, launched by the government, will release further reports addressing culpability and potential blame for the scandal.


---

## 79. Perplexity launches Comet, an AI-powered web browser

**原文标题**: Perplexity launches Comet, an AI-powered web browser

**原文链接**: [https://techcrunch.com/2025/07/09/perplexity-launches-comet-an-ai-powered-web-browser/](https://techcrunch.com/2025/07/09/perplexity-launches-comet-an-ai-powered-web-browser/)

生成摘要时出错

---

## 80. The 800k Hours Career Guide

**原文标题**: The 800k Hours Career Guide

**原文链接**: [https://www.boristhebrave.com/2025/07/10/the-800000-hours-career-guide/](https://www.boristhebrave.com/2025/07/10/the-800000-hours-career-guide/)

生成摘要时出错

---

## 81. Non-Concussive Head Impacts and Brain Microstructure, Chemistry and Function

**原文标题**: Non-Concussive Head Impacts and Brain Microstructure, Chemistry and Function

**原文链接**: [https://sportsmedicine-open.springeropen.com/articles/10.1186/s40798-025-00867-0](https://sportsmedicine-open.springeropen.com/articles/10.1186/s40798-025-00867-0)

生成摘要时出错

---

## 82. Radiocarbon dating reveals Rapa Nui not as isolated as previously thought

**原文标题**: Radiocarbon dating reveals Rapa Nui not as isolated as previously thought

**原文链接**: [https://phys.org/news/2025-06-radiocarbon-dating-reveals-rapa-nui.html](https://phys.org/news/2025-06-radiocarbon-dating-reveals-rapa-nui.html)

生成摘要时出错

---

## 83. Tree Borrows

**原文标题**: Tree Borrows

**原文链接**: [https://plf.inf.ethz.ch/research/pldi25-tree-borrows.html](https://plf.inf.ethz.ch/research/pldi25-tree-borrows.html)

生成摘要时出错

---

## 84. Lasagna Battery Cell

**原文标题**: Lasagna Battery Cell

**原文链接**: [https://amazingribs.com/more-technique-and-science/more-cooking-science/reactive-pans/](https://amazingribs.com/more-technique-and-science/more-cooking-science/reactive-pans/)

生成摘要时出错

---

## 85. Final report on Alaska Airlines Flight 1282 in-flight exit door plug separation

**原文标题**: Final report on Alaska Airlines Flight 1282 in-flight exit door plug separation

**原文链接**: [https://www.ntsb.gov:443/investigations/Pages/DCA24MA063.aspx](https://www.ntsb.gov:443/investigations/Pages/DCA24MA063.aspx)

生成摘要时出错

---

## 86. Author of William the Conqueror's 'Medieval Big Data' Project Revealed

**原文标题**: Author of William the Conqueror's 'Medieval Big Data' Project Revealed

**原文链接**: [https://www.ox.ac.uk/news/2025-07-02-author-william-conqueror-s-medieval-big-data-project-revealed](https://www.ox.ac.uk/news/2025-07-02-author-william-conqueror-s-medieval-big-data-project-revealed)

生成摘要时出错

---

## 87. Zorin OS

**原文标题**: Zorin OS

**原文链接**: [https://zorin.com/os/](https://zorin.com/os/)

生成摘要时出错

---

## 88. Solar power has begun to transform the world’s energy system

**原文标题**: Solar power has begun to transform the world’s energy system

**原文链接**: [https://www.newyorker.com/news/annals-of-a-warming-planet/46-billion-years-on-the-sun-is-having-a-moment](https://www.newyorker.com/news/annals-of-a-warming-planet/46-billion-years-on-the-sun-is-having-a-moment)

生成摘要时出错

---

## 89. Million Times Million

**原文标题**: Million Times Million

**原文链接**: [https://susam.net/million-times-million.html](https://susam.net/million-times-million.html)

生成摘要时出错

---

## 90. Sinking of the Rainbow Warrior

**原文标题**: Sinking of the Rainbow Warrior

**原文链接**: [https://en.wikipedia.org/wiki/Sinking_of_the_Rainbow_Warrior](https://en.wikipedia.org/wiki/Sinking_of_the_Rainbow_Warrior)

生成摘要时出错

---

## 91. An open letter from educators who refuse the call to adopt GenAI in education

**原文标题**: An open letter from educators who refuse the call to adopt GenAI in education

**原文链接**: [https://openletter.earth/an-open-letter-from-educators-who-refuse-the-call-to-adopt-genai-in-education-cb4aee75](https://openletter.earth/an-open-letter-from-educators-who-refuse-the-call-to-adopt-genai-in-education-cb4aee75)

生成摘要时出错

---

## 92. Burning a Magnesium NeXT Cube (1993)

**原文标题**: Burning a Magnesium NeXT Cube (1993)

**原文链接**: [https://simson.net/ref/1993/cubefire.html](https://simson.net/ref/1993/cubefire.html)

生成摘要时出错

---

## 93. Show HN: Typeform was too expensive so I built my own forms

**原文标题**: Show HN: Typeform was too expensive so I built my own forms

**原文链接**: [https://www.ikiform.com/](https://www.ikiform.com/)

生成摘要时出错

---

## 94. Show HN: asyncmcp – Run MCP over async transport via AWS SNS+SQS

**原文标题**: Show HN: asyncmcp – Run MCP over async transport via AWS SNS+SQS

**原文链接**: [https://github.com/bh-rat/asyncmcp](https://github.com/bh-rat/asyncmcp)

生成摘要时出错

---

## 95. A Typology of Canadianisms

**原文标题**: A Typology of Canadianisms

**原文链接**: [https://dchp.arts.ubc.ca/how-to-use](https://dchp.arts.ubc.ca/how-to-use)

生成摘要时出错

---

## 96. US Court nullifies FTC requirement for click-to-cancel

**原文标题**: US Court nullifies FTC requirement for click-to-cancel

**原文链接**: [https://arstechnica.com/tech-policy/2025/07/us-court-cancels-ftc-rule-that-would-have-made-canceling-subscriptions-easier/](https://arstechnica.com/tech-policy/2025/07/us-court-cancels-ftc-rule-that-would-have-made-canceling-subscriptions-easier/)

生成摘要时出错

---

## 97. Show HN: OffChess – Offline chess puzzles app

**原文标题**: Show HN: OffChess – Offline chess puzzles app

**原文链接**: [https://offchess.com](https://offchess.com)

生成摘要时出错

---

## 98. Show HN: FlopperZiro – A DIY open-source Flipper Zero clone

**原文标题**: Show HN: FlopperZiro – A DIY open-source Flipper Zero clone

**原文链接**: [https://github.com/lraton/FlopperZiro](https://github.com/lraton/FlopperZiro)

生成摘要时出错

---

## 99. Helm local code execution via a malicious chart

**原文标题**: Helm local code execution via a malicious chart

**原文链接**: [https://github.com/helm/helm/security/advisories/GHSA-557j-xg8c-q2mm](https://github.com/helm/helm/security/advisories/GHSA-557j-xg8c-q2mm)

生成摘要时出错

---

## 100. Bionic robot arm lets plants play musical instruments (2024)

**原文标题**: Bionic robot arm lets plants play musical instruments (2024)

**原文链接**: [https://djmag.com/news/bionic-robot-arm-lets-plants-play-musical-instruments](https://djmag.com/news/bionic-robot-arm-lets-plants-play-musical-instruments)

生成摘要时出错

---

