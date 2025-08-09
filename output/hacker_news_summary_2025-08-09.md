# Hacker News 热门文章摘要 (2025-08-09)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 由于螺旋蝇蔓延，墨西哥至美国的牲畜贸易暂停

**原文标题**: Mexico to US Livestock Trade halted due to Screwworm spread

**原文链接**: [https://www.usda.gov/about-usda/news/press-releases/2025/07/09/secretary-rollins-takes-decisive-action-and-shuts-down-us-southern-border-ports-livestock-trade-due](https://www.usda.gov/about-usda/news/press-releases/2025/07/09/secretary-rollins-takes-decisive-action-and-shuts-down-us-southern-border-ports-livestock-trade-due)

无法访问文章链接。

---

## 2. 显示 HN：你所在大致位置的当前天空，以 CSS 渐变呈现

**原文标题**: Show HN: The current sky at your approximate location, as a CSS gradient

**原文链接**: [https://sky.dlazaro.ca](https://sky.dlazaro.ca)

此“Show HN”帖子展示了一个项目，该项目动态生成 CSS 渐变，模拟用户大致所在位置的天空。帖子提供了特定地平线的坐标（38.71345，-78.15944），表明渐变反映了从该点可见的颜色。 关键在于创建了天空的可视化表示，使用 CSS 根据地理位置进行个性化设置，大概反映了特定时间和大气条件。 本质上，它将实时天空转化为基于 CSS 的视觉产物。

---

## 3. OpenFreeMap 每秒承受 10 万次请求

**原文标题**: OpenFreeMap survived 100k requests per second

**原文链接**: [https://blog.hyperknot.com/p/openfreemap-survived-100000-requests](https://blog.hyperknot.com/p/openfreemap-survived-100000-requests)

OpenFreeMap的创建者Zsolt Ero惊讶地发现，该服务挺过了一次每秒10万次请求的突增，24小时内总计30亿次请求和215TB的流量。问题表现为一些瓦片缺失，最终追溯到服务器上的“打开文件过多”错误。他发现来源是Wplace.live，一个新型协作绘图网站，该网站严重依赖OpenFreeMap，并且被用户使用脚本绕过像素放置限制。

意外的负载导致实施了Cloudflare规则，以限制Wplace.live的流量，从而保护整体服务。Zsolt赞扬了Cloudflare快速批准带宽赞助和提供的支持，并指出其CDN缓存率高达99.4%，他的服务器处理了剩余的每秒1000次请求。

在联系Wplace.live开发者后，Zsolt提出帮助他们设置自托管的OpenFreeMap实例，以减轻公共服务的负载。他还观察到流量模式表明，Wplace.live的200万用户中有部分人使用了脚本活动。Zsolt的主要经验教训包括实施按引用站点的带宽限制，并改进服务器配置以防止瓦片缺失。文章最后呼吁赞助，以支持OpenFreeMap的持续开发和维护，并强调捐款可覆盖基础设施成本。

---

## 4. 长期暴露于室外空气污染与痴呆症风险增加有关

**原文标题**: Long-term exposure to outdoor air pollution linked to increased risk of dementia

**原文链接**: [https://www.cam.ac.uk/research/news/long-term-exposure-to-outdoor-air-pollution-linked-to-increased-risk-of-dementia](https://www.cam.ac.uk/research/news/long-term-exposure-to-outdoor-air-pollution-linked-to-increased-risk-of-dementia)

一项对近三千万人数据的全面分析显示，长期暴露于室外空气污染与痴呆症风险增加之间存在显著关联。该研究发表在《柳叶刀-地球健康》上，确定了颗粒物（PM2.5）、二氧化氮（NO2）和烟尘是与这种风险增加相关的关键污染物。例如，PM2.5每增加10微克/立方米，痴呆症风险增加17%。

研究人员认为，空气污染会引发大脑炎症和氧化应激，从而导致痴呆症的发生。他们强调需要更严格的污染限制，特别是针对交通运输和工业部门，并强调解决空气污染可能带来的健康、社会、气候和经济效益。

虽然该研究表明空气污染对血管性痴呆的影响比阿尔茨海默病更强，但这一发现没有统计学意义。研究人员还指出，研究人群主要为来自高收入国家的白人，因此呼吁未来的研究纳入更多样化的人群。这项研究强调了痴呆症预防需要采取跨学科的方法，包括城市规划、交通政策和环境法规。

---

## 5. 西蒙·威利森在湾区人工智能安全聚会上的致命三要素演讲

**原文标题**: Simon Willison's Lethal Trifecta Talk at the Bay Area AI Security Meetup

**原文链接**: [https://simonwillison.net/2025/Aug/9/bay-area-ai/](https://simonwillison.net/2025/Aug/9/bay-area-ai/)

Simon Willison湾区AI安全聚会演讲聚焦于提示注入攻击的危险，并介绍了在保护使用模型上下文协议（MCP）的系统时出现的“致命三合会”概念。提示注入类似于SQL注入，当不可信的用户输入与可信指令连接时发生，允许攻击者操纵LLM的行为。

Willison在2022年创造了“提示注入”一词，强调了命名漏洞以提高意识的重要性。他用易受海盗语攻击的翻译应用程序和易受电子邮件盗窃影响的假设电子邮件助手（Marvin）等例子说明了这个问题。他还讨论了“Markdown数据泄露”，攻击者使用图像渲染来泄露私人数据，并引用了著名系统中大量此漏洞的例子。

随后，他介绍了“致命三合会”，包括：**私有数据访问**、**不可信内容摄取**以及**外部通信能力**。当这三者结合在一起时，会产生严重的安全性风险，正如GitHub MCP服务器示例所示，在公共问题中发布的恶意指令可能导致私有存储库中的数据泄露。

Willison批评了常见的防御措施，如“提示乞讨”和基于AI的过滤，认为在安全领域，99%的保护是不够的。他强调，移除致命三合会的任何一条腿都可以阻止攻击。最后，他强调了MCP的混合搭配性质所固有的安全挑战，认为用户没有能力管理避免启用致命三合会和暴露自己于数据盗窃所需的复杂安全决策。

---

## 6. Quickshell – 桌面构建基石

**原文标题**: Quickshell – building blocks for your desktop

**原文链接**: [https://quickshell.org/](https://quickshell.org/)

Quickshell 0.2.0 是一个使用 QtQuick 构建自定义桌面组件（如状态栏、窗口小部件和锁屏）的工具包。它允许用户在 Wayland 合成器或窗口管理器之外创建一个完整的桌面环境。主要特性包括：

*   **实时更新：** Quickshell 在保存时立即反映更改，从而实现快速迭代。
*   **易于使用的 QML 语言：** 配置使用 QML 完成，这是一种用户友好的语言，专为创建灵活的用户界面而设计，并提供 LSP 支持。
*   **广泛的集成：** Quickshell 为桌面自定义提供了广泛且不断增长的集成集。

提供的代码片段演示了如何创建一个根据计时器更改颜色的浮动窗口，展示了 QML 在构建交互式元素方面的简洁性。文章还链接到安装说明和文档，供有兴趣尝试 Quickshell 的用户参考。文章中还提到了由不同用户创建的多个配置。

---

## 7. ChatGPT 智能代理 – 欧盟发布

**原文标题**: ChatGPT Agent – EU Launch

**原文链接**: [https://help.openai.com/en/articles/11752874-chatgpt-agent](https://help.openai.com/en/articles/11752874-chatgpt-agent)

无法访问文章链接。

---

## 8. 荒诞帝国：苏联荒诞史略

**原文标题**: Empire of the Absurd: A Brief History of the Absurdities of the Soviet Union

**原文链接**: [https://laurivahtre.ee/empire-of-the-absurd/](https://laurivahtre.ee/empire-of-the-absurd/)

本书摘录自《荒诞帝国：苏联荒诞史简述》，介绍了本书的前提和作者。序言由马特·拉尔撰写，通过强调苏联的崩溃是一场造成巨大人员伤亡的重大历史失败，奠定了基调。他认为，与纳粹主义不同，共产主义没有受到充分谴责，导致其阴魂不散。他强调理解苏联体制的现实对于防止其复兴的重要性。

引言由作者劳里·瓦赫特雷撰写，解释了他写作本书的动机：帮助西方人理解苏联日常生活的荒诞之处。他强调，本书不是一项学术研究，而是一篇基于个人记忆并辅以各种资料的文章。他承认自己的爱沙尼亚背景，强调爱沙尼亚作为西方与苏联之间的边境地区所处的独特地位，提供了来自苏联体制内外的视角。

第一章深入探讨了荒诞本身的概念，将其定义为对心灵的迷惑，提醒人们理性是有局限性的。它认为荒诞本质上是人类的，文明会经历荒诞蓬勃发展的时期。作者区分了自然的、无意的和人为的荒诞，并将苏联定位为后者的主要生产者。他认为俄罗斯民族荒诞性和共产主义意识形态荒诞性是苏联政权荒诞特征的两大支柱。

---

## 9. 无障碍与能动网络

**原文标题**: Accessibility and the Agentic Web

**原文链接**: [https://tetralogical.com/blog/2025/08/08/accessibility-and-the-agentic-web/](https://tetralogical.com/blog/2025/08/08/accessibility-and-the-agentic-web/)

本文探讨了自主型人工智能在革新网络可访问性方面的潜力，尤其是在以在线零售为例的情况下，为盲人等残疾用户提供便利。作者作为屏幕阅读器使用者，强调了当前零售网站（即使是可访问的网站）在为用户提供充分的产品信息以做出明智购买决策方面的局限性。人工智能图像描述工具提供了一种临时解决方案，但耗时且不可靠。

以Innosearch等平台为例的自主型人工智能提供了一种更有希望的解决方案。这些平台在多个零售商之间提供一致且可访问的界面，并允许用户与数字购物助手进行对话式互动。该助手可以筛选产品、提供详细描述并管理购物车，模仿拥有私人购物者的体验。

作者质疑在这种情况下传统网站的持续相关性，并建议用户可能更喜欢直接与自主型人工智能互动，以获得更方便和个性化的体验。这种转变引发了重大影响，尤其是在谷歌利用人工智能处理数十亿次搜索请求并减少网站流量的背景下。

虽然承认围绕人工智能及其潜在泡沫的炒作周期，但作者认为自主型网络很可能将持续存在。这引发了关于在这种新模式下可访问性的重要问题。确保自主型人工智能持续生成可访问的内容，满足法律义务，是一个关键挑战。文章最后邀请大家合作开展这一不断发展的领域中的可访问性项目。

---

## 10. ESP32总线海盗0.5 – 一款能讲各种协议的硬件黑客工具

**原文标题**: ESP32 Bus Pirate 0.5 – A Hardware Hacking Tool That Speaks Every Protocol

**原文链接**: [https://github.com/geo-tp/ESP32-Bus-Pirate](https://github.com/geo-tp/ESP32-Bus-Pirate)

ESP32 Bus Pirate 是一款开源固件，它将 ESP32 设备转化为多功能的硬件破解工具，其灵感来源于最初的 Bus Pirate。它允许用户通过 USB 串口或网页浏览器访问的命令行界面 (CLI) 与各种数字协议（I2C、UART、SPI 等）进行交互。

主要功能包括：交互式 CLI、多种协议模式（I2C、SPI、UART、1-Wire 等）、协议嗅探器（I2C、Wi-Fi、Bluetooth 等）、脚本编写能力、红外协议的 device-b-gone 命令、直接 I/O 管理以及 Web 和串口界面。它支持 ESP32 S3 Dev Kit、M5 Cardputer、M5 Stick C Plus 2、M5 Atom S3 Lite、M5 Stamp S3、LILYGO T-Embed 和 LILYGO T-Embed CC1101 等设备。

该项目在其 Wiki 上提供了全面的文档，涵盖终端模式、模式概述、指令语法、串口设置和 Python 脚本示例。入门方法包括刷写固件、通过串口或 Web 界面连接，以及使用 `mode`、`help` 和 `scan` 等命令。

该固件提供 Web 和串口两种界面，各有优势。Web 界面可通过 Wi-Fi 从任何浏览器访问，而串口界面则提供更快的性能和响应速度。贡献指南可供希望添加新命令的用户使用。

一个重要的警告强调设备应在 3.3V 或 5V 电压下运行，以防止损坏 ESP32。

---

## 11. 冬虫草——用《毁灭战士》替换Amiga的大脑

**原文标题**: Cordoomceps – replacing an Amiga's brain with Doom

**原文链接**: [https://mjg59.dreamwidth.org/73001.html](https://mjg59.dreamwidth.org/73001.html)

这篇题为《Cordoomceps——用毁灭战士替换Amiga的“大脑”》的短文，介绍了一个可能以在Amiga电脑上以非传统方式运行经典第一人称射击游戏《毁灭战士》为中心的项目。标题暗示了对Amiga核心功能或“大脑”的潜在替换，取而代之的是《毁灭战士》。末尾包含的“验证码检查”表明这可能是一个更大事物的介绍，很可能是一个需要验证才能进一步访问或交互的网站或论坛帖子。验证码元素暗示该项目可能具有技术性，或者与一个防止自动访问很重要的社区有关。在没有更多背景信息的情况下，核心思想是有人试图将《毁灭战士》深度集成到Amiga的运行中，可能不仅仅是将其作为标准应用程序运行。

---

## 12. MCP无视RPC 40年最佳实践

**原文标题**: MCP's Disregard for 40 Years of RPC Best Practices

**原文链接**: [https://julsimon.medium.com/why-mcps-disregard-for-40-years-of-rpc-best-practices-will-burn-enterprises-8ef85ce5bc9b](https://julsimon.medium.com/why-mcps-disregard-for-40-years-of-rpc-best-practices-will-burn-enterprises-8ef85ce5bc9b)

本文认为，旨在将AI工具交互标准化的模型上下文协议（MCP），被设计成一个简单的“AI版USB-C”，却危险地忽视了40年来确立的远程过程调用（RPC）最佳实践，从而使企业面临生产故障的风险。

作者认为，MCP优先考虑易于采用性，而不是运营稳健性，导致在类型安全（使用无模式JSON代替强制数据表示）、跨语言一致性、无状态性、机器可读合约和可观察性（缺乏内置的追踪和截止时间传播）等方面存在严重缺陷。作者批评了依赖第三方库来解决这些核心缺陷的做法，认为这会导致碎片化和增加企业成本。

具体而言，本文强调了缺少诸如带有相关ID的分布式追踪、超越基本OAuth的强大身份验证、模式版本控制、服务发现、连接池、二进制协议选项和成本归因机制等功能。作者阐述了这些遗漏所带来的实际调试和成本跟踪难题。

作者总结道，由AI炒作驱动的MCP的快速采用是不成熟的，并迫使企业在事后改造关键功能。本文敦促MCP维护者学习已建立的RPC模式，以解决当前的运营需求，并朝着企业级功能发展，以构建更强大和可靠的AI集成平台。

---

## 13. Jan – 具有本地UI的Ollama替代方案

**原文标题**: Jan – Ollama alternative with local UI

**原文链接**: [https://github.com/menloresearch/jan](https://github.com/menloresearch/jan)

Jan是一款本地AI助手，允许用户在设备上离线下载并运行Llama、Gemma和Qwen等大型语言模型(LLM)，优先考虑用户隐私和控制。它具有云集成功能，可连接OpenAI、Anthropic、Mistral、Groq等服务。用户可以创建自定义AI助手并使用OpenAI兼容的API。

该软件提供Windows、macOS和Linux的稳定版和夜间构建版，可从jan.ai或GitHub Releases下载。

开发者可以使用Make或Mise从源代码构建Jan，详细的说明文档提供了设置开发环境、管理依赖项（Node.js、Yarn、Rust）和运行应用程序的步骤。系统要求包括特定的macOS版本以及支持GPU的Windows 10+。

该项目鼓励社区贡献，并提供文档、API参考、更新日志和Discord支持的链接。可以通过GitHub Issues提交错误报告，并且该项目已获得Apache 2.0许可。Jan基于Llama.cpp、Tauri和Scalar库构建。

---

## 14. 律师称，逝者需要删除数据的权利，以防被AI化。

**原文标题**: The dead need right to delete their data so they can't be AI-ified, lawyer says

**原文链接**: [https://www.theregister.com/2025/08/09/dead_need_ai_data_delete_right/](https://www.theregister.com/2025/08/09/dead_need_ai_data_delete_right/)

法律学者维多利亚·哈内曼主张为逝者设立“数字删除权”，以防止其数字遗骸通过人工智能复活而被利用。生成式人工智能允许重建一个人的数字存在，引发了对未经授权的纪念和个人数据潜在滥用的担忧。

哈内曼指出，美国现行法律对死者提供的数据保护有限，使其数字资产容易受到攻击。虽然存在《修订后的统一受托人访问数字资产法案》（RUFADAA），但它主要处理访问权，而非删除权，而且许多人死后没有遗嘱，将控制权留给了科技平台。形象权在某些州提供了一些保护，但其适用性存在问题。

与人权和隐私权强大的欧洲不同，美国在实施“被遗忘权”时面临第一修正案的挑战。哈内曼提出，为逝者的遗产设立有限的、有时限的删除权，并将其与保护遗体的现行法律相提并论。这将平衡社会利益与逝者的权利，以防止基于其数字足迹构建的不受欢迎的人工智能模拟。加利福尼亚州的《删除法案》提供了一个潜在的模式，可以将数据删除权扩展到逝者，这一概念得到了阿斯彭科技政策中心的支持。

---

## 15. 在音乐节测试Bitchat

**原文标题**: Testing Bitchat at the music festival

**原文链接**: [https://primal.net/saunter/testing-bitchat-at-the-music-festival](https://primal.net/saunter/testing-bitchat-at-the-music-festival)

文章标题“音乐节Bitchat测试”显示该文章旨在测试Bitchat应用在音乐节环境中的表现。但页面内容仅提示需启用JavaScript方可运行，未提供关于测试本身、应用功能或测试结果的任何信息。由此仅能推断其测试意图，文章内容缺乏实际细节。

---

## 16. Ratfactor图解叠床笠指南

**原文标题**: Ratfactor's Illustrated Guide to Folding Fitted Sheets

**原文链接**: [https://ratfactor.com/cards/fitted-sheets](https://ratfactor.com/cards/fitted-sheets)

Ratfactor幽默指南旨在揭秘叠床笠的艰巨任务。它认为床笠与莫比乌斯带或克莱因瓶不同，由于其可定向的双面表面，因此可以折叠。

文章介绍了两种方法。第一种是简单但繁琐的方法，将床笠反面朝上平铺在平面上，然后将其折叠成矩形。第二种是更高效的臂式方法，包括聚集角。文章强调正确配对角（不要对角线！）以及将一个角反转到另一个角上的重要性。关键是同时找到并抓住*剩余的两个角*，然后将*那一对角*反转到第一对角上。文章特别警告不要采用一次一个角的方法，声称这种方法通常会导致一团乱麻，尤其是对于使用围绕整个周边的松紧带的现代床笠，并认为较旧的教程仍在教授，从而阻碍了成功。

一旦所有四个角都合并在一起，就将床笠放平，拉直，然后折叠成一个整齐的捆，将松紧带包裹在其中。作者鼓励尝试最终的折叠和平滑处理，以获得专业外观的效果。

最后，文章批判了有关床笠历史的在线资源，质疑某些专利的突出性，并强调了其他相关设计。

---

## 17. 终端用户可编程人工智能

**原文标题**: End-User Programmable AI

**原文链接**: [https://queue.acm.org/detail.cfm?id=3746223](https://queue.acm.org/detail.cfm?id=3746223)

本文介绍了 Universalis，一种旨在供领域专家阅读并由人工智能生成的新编程语言，从而实现最终用户可编程人工智能。Universalis 旨在弥合自然语言和可执行代码之间的差距，使没有接受过正规编程培训的个人也能使用人工智能。

受莱布尼茨关于用于知识表示和操作的通用语言的愿景的启发，Universalis 使用类似自然语言的语法，并在方括号（[...]）中嵌入逻辑谓词。这些方括号的功能类似于 Excel 电子表格公式。一个关键的设计原则是，熟悉 Excel 公式的使用者应该能够理解 Universalis 脚本。

该语言具有前置和后置条件（类似于 Excel 数据验证）、条件语句以及通过隐式广播实现的无循环编程，从而简化了复杂的操作。查询理解允许使用结构化的自然语言方法进行高级数据操作。这些功能旨在使非程序员也能进行复杂的操作。

本文强调了从传统的、针对开发者编写优化的编程，到机器编写、领域专家阅读的范式的转变。Universalis 优先考虑可读性和直观逻辑，使用清晰、自然的语言解释。该语言简化了 AI 模型生成代码的任务，从而产生更准确、更无错误的代码。该框架旨在通过前置和后置条件契约来提高 AI 安全性，并展示了 Universalis 如何解决传统查询语言（如 SQL）对普通用户的局限性。

---

## 18. 这辆车跑了超过120万公里，而且状态依然很好。

**原文标题**: Car has more than 1.2M km on it – and it's still going strong

**原文链接**: [https://www.cbc.ca/news/canada/nova-scotia/1985-toyota-tercel-high-mileage-1.7597168](https://www.cbc.ca/news/canada/nova-scotia/1985-toyota-tercel-high-mileage-1.7597168)

新斯科舍省的安迪·坎贝尔拥有一辆1985年的丰田特塞尔，里程已超过120万公里。尽管车龄已高，但这辆车车况极佳。里程表仅显示253,070公里，缺了“1”百万。坎贝尔于1990年购买了这辆特塞尔，当时里程为125,000公里，此后一直将其作为日常用车，即使现在退休了也是如此。

坎贝尔几乎自己完成所有的维护工作，依靠从他拥有的另外三辆特塞尔上收集的备件。他将汽车的长寿归功于定期维护、底盘装甲和保持润滑。他甚至还有一辆备用特塞尔，是一辆86年的车型，用于他的主要车辆维修时使用。

坎贝尔对车展或古董车牌照不感兴趣，更喜欢将他的特塞尔用于实际用途。他说特塞尔很实用，在雪地里表现出色，易于维护且运营成本低廉。

另一位新斯科舍省居民吉姆·乔治也拥有一辆85年的特塞尔，里程超过50万公里。坎贝尔希望达到200万公里，但不确定他是否能活到那时。人们经常停下来欣赏他的车，但他拒绝出售。

---

## 19. 我想要一切本地化——构建我的离线AI工作空间

**原文标题**: I want everything local – Building my offline AI workspace

**原文链接**: [https://instavm.io/blog/building-my-offline-ai-workspace](https://instavm.io/blog/building-my-offline-ai-workspace)

本文详细介绍了如何创建一个完全本地化的人工智能工作区，强调隐私保护，并消除对云服务的依赖。作者的动机源于希望在不依赖 OpenAI 或 Google 等云端人工智能服务的情况下执行任务，特别是涉及个人数据（如照片和视频编辑）的任务。

解决方案包括：

*   **本地 LLM：** 使用 Ollama 在用户机器上直接运行语言模型。
*   **容器化代码执行：** 利用 Apple 的“容器”创建隔离的虚拟机，用于运行由 LLM 生成的代码，确保代码不会直接与宿主机系统交互。
*   **无头浏览器：** 集成 Playwright 用于访问互联网，使系统能够研究主题、查找工具的安装说明以及总结网络内容。

技术栈还包括用于前端的 assistant-ui 和用于协调组件之间交互的 coderunner。

本文记录了开发过程中遇到的挑战，包括 MacOS 应用程序开发和模型工具支持方面的问题。它还解释了如何在容器内部署 Jupyter 服务器并将其作为 MCP（模型上下文协议）工具公开，从而允许现有工具在隔离的 VM 中执行代码。文章还介绍了使用 Apple 容器所涉及的挑战。

最终的系统使用户能够在安全、本地的环境中执行视频编辑、图像处理和研究等任务。作者提供了 coderunner-ui 和 coderunner 的 GitHub 链接，鼓励反馈和贡献。

---

## 20. 沙尘暴 - 可自托管的Web效率套件

**原文标题**: Sandstorm- self-hostable web productivity suite

**原文链接**: [https://sandstorm.org/](https://sandstorm.org/)

Sandstorm是一个开源平台，旨在简化Web应用程序的托管和管理，强调安全性和易用性。它允许用户通过应用市场轻松点击几下即可自托管Web应用程序，如文档编辑器（Etherpad）、文件存储（Davros）、项目管理工具（Wekan）和聊天应用程序（Rocket.Chat），并确保自动更新。

Sandstorm集中管理应用程序和数据，提供一致的访问控制和增强的安全性。每个应用程序及其数据都存在于一个安全的“颗粒”中，该颗粒被容器化，以防止未经授权的访问或外部通信，从而减轻许多安全漏洞。用户可以完全控制数据位置，选择云托管或自托管，并且可以轻松地在选项之间迁移数据。

该平台通过允许用户混合搭配来自不同开发者的应用程序（包括自定义应用程序）来促进开放性。许多应用程序是开源的，可以修改以适应个人需求。

Sandstorm通过提供一个安全和私有的环境来运行开源Web应用程序，满足个人需求；通过集中数据、促进团队自主性和确保数据安全，满足企业需求。开发者可以受益于Sandstorm，轻松打包和部署他们的应用程序，而无需担心基础设施管理。总而言之，Sandstorm旨在让用户在管理其Web应用程序和数据方面拥有控制权、安全性和灵活性。

---

## 21. 部分匹配 Zig 枚举

**原文标题**: Partially Matching Zig Enums

**原文链接**: [https://matklad.github.io/2025/08/08/partially-matching-zig-enums.html](https://matklad.github.io/2025/08/08/partially-matching-zig-enums.html)

本文探讨了编程中使用枚举（或标签联合）时的一个常见问题：在单独处理各个枚举变体之前，需要为枚举变体的子集执行共享逻辑。作者使用 Zig 枚举 `U`（具有 `A`、`B` 和 `C` 变体）来呈现这个问题，其中 `A` 和 `B` 有时需要一个共享的 `handle_ab` 函数调用。

文章探讨了常见但不太理想的解决方案：在每个相关案例中复制共享逻辑，或重构枚举结构，这两种方法都可能繁琐且缺乏灵活性。然后，它介绍了一种使用 `unreachable` 的运行时恐慌解决方案，该方案在共享逻辑之后使用。

文章的核心在于展示一种更简洁、经过编译时检查的 Zig 解决方案，该方案利用了 `inline` 和 `comptime unreachable`。`inline .a, .b` 强制编译器生成两次代码，并使用编译时已知的值，而 `comptime unreachable` 指示编译器验证内部 `switch` 语句中的 `else` 分支是否确实不可达。如果代码尝试在共享逻辑块中处理 `C`（如无法编译的示例所示），编译器将检测到 `else` 分支可能被访问的潜在风险，并触发编译时错误，从而确保共享逻辑仅应用于预期的枚举变体。这可以防止运行时恐慌，并提供更强的编译时保证。

---

## 22. Tribblix – 复古的Illumos发行版

**原文标题**: Tribblix – The Retro Illumos Distribution

**原文链接**: [http://www.tribblix.org/](http://www.tribblix.org/)

Tribblix是一款基于illumos的开源操作系统，由Peter Tribble创建，旨在以现代组件呈现复古风格。截至2025年7月的最新消息显示，x86（“Vanilla Tribblix”和“Omnitribblix”）和SPARC架构均已发布里程碑37。

X86变体版本可供下载，并附带发行说明。SPARC用户应从里程碑32升级到33。还有一个更小的、CDROM大小的m32 SPARC ISO可供下载。

值得注意的是，32位硬件支持已完全移除。虽然SPARC硬件支持仍然有限，需要更多测试，但x86版本被认为是稳定的，可以下载、安装和使用。该网站提供下载链接、发行说明以及安装和使用的一般说明。还提供联系方式(tribblix@gmail.com)以及GitHub和隐私信息链接。

---

## 23. 60%的荣誉勋章获得者是爱尔兰人或爱尔兰裔美国人

**原文标题**: 60% of medal of honor recipients are Irish or Irish-American

**原文链接**: [https://en.wikipedia.org/wiki/List_of_Irish-American_Medal_of_Honor_recipients](https://en.wikipedia.org/wiki/List_of_Irish-American_Medal_of_Honor_recipients)

此维基百科条目关注于获得美国政府颁发的最高军事荣誉勋章的爱尔兰裔和爱尔兰裔美国人。截至2009年9月，在颁发的3464枚荣誉勋章中，据估计有2021枚（58%）颁发给了爱尔兰血统的人，远高于任何其他族裔群体。此外，257名获奖者出生于爱尔兰，占所有外国出生获奖者的一半以上。

该文章提到了一座纪念这些爱尔兰出生英雄的纪念碑，该纪念碑位于福吉谷荣誉勋章林，由古代希伯尼安人协会竖立。文章还指出，迈克尔·马登是第一位因在内战中的行动而获得该勋章的爱尔兰裔美国人，尽管助理外科医生伯纳德·J.D.·欧文因1861年早期的行动而获得了该勋章。

该文章的大部分内容是一个详细但并不完整的爱尔兰裔和爱尔兰裔美国人荣誉勋章获得者名单，包括他们在内战中的服役情况、军衔、部队、行动地点和日期，以及对他们英勇行为的简要描述。该名单提供了这些个人因“显著的勇敢和无畏”而受到表彰的具体例子。

---

## 24. 打破有向单源最短路径的排序壁垒

**原文标题**: Breaking the Sorting Barrier for Directed Single-Source Shortest Paths

**原文链接**: [https://arxiv.org/abs/2504.17033](https://arxiv.org/abs/2504.17033)

本文（arXiv:2504.17033v2 [cs.DS]）提出了一种新的算法，用于解决带实数非负边权的 directed graphs 上的单源最短路径（SSSP）问题。该论文由段然、毛嘉懿、毛潇、舒鑫凯和尹龙辉撰写，介绍了一种确定性算法，在比较-加法模型中，其时间复杂度为O(m log^(2/3) n)。其中，“m”表示图中的边数，“n”表示图中的顶点数。

这项工作的主要意义在于超越了Dijkstra算法在稀疏图上实现的长期以来的O(m + n log n)时间界限。这一突破表明，Dijkstra算法并非解决SSSP问题的最优算法，这一发现至今难以捉摸。

该论文共17页，最初于2025年4月23日提交，并于2025年7月30日修订。它属于“数据结构与算法”(cs.DS)主题类别，并被归类为ACM F.2.2类。摘要重点介绍了该论文的核心贡献，即新算法及其优于Dijkstra算法的时间复杂度。

---

## 25. 星星之火

**原文标题**: A SPARC makes a little fire

**原文链接**: [https://www.leadedsolder.com/2025/08/05/sparcstation-scsi-termination-fix-magic-smoke.html](https://www.leadedsolder.com/2025/08/05/sparcstation-scsi-termination-fix-magic-smoke.html)

2018年，作者试图修复一台无法启动的Sun SparcStation 1+。最初，计算机报错“非法指令”。硬盘，一块Apple工厂硬盘，似乎是罪魁祸首。经过多次更换硬盘的尝试后，作者遇到了诸如“SCSI设备无响应”和“磁盘标签中的错误魔数”等问题。作者发现SparcStation固件会将SCSI ID 0重新路由到ID 3。 软驱也被探索为启动方法，但它也发生故障。

由于受挫，该项目被搁置到2025年。 然后，作者尝试使用启动器模式下的BlueSCSI来转储磁盘，但驱动器被卡住。 他们决定使用MAME创建一个可用的SunOS磁盘映像，然后尝试通过BlueSCSI将其传输到SparcStation。

然而，在使用改装电缆为BlueSCSI供电时，接线错误导致+12V被发送到只需要+5V的地方。 这导致BlueSCSI的稳压器烧毁，microSD卡被损坏，并且可能对BlueSCSI造成无法修复的损坏。

尽管遇到挫折，SparcStation本身似乎没有损坏。 作者强调了验证电缆布线以防止此类事件发生的重要性，并计划在未来排除损坏的BlueSCSI的故障，同时感叹缺乏终端电源。

---

## 26. Tor：军方项目如何成为隐私的生命线

**原文标题**: Tor: How a military project became a lifeline for privacy

**原文链接**: [https://thereader.mitpress.mit.edu/the-secret-history-of-tor-how-a-military-project-became-a-lifeline-for-privacy/](https://thereader.mitpress.mit.edu/the-secret-history-of-tor-how-a-military-project-became-a-lifeline-for-privacy/)

本文探讨了Tor的历史，Tor是一种增强隐私的技术，最初由美国海军研究实验室（NRL）开发，旨在保护军事通信。面对在不泄露来源和目的地的情况下保护互联网流量的挑战，研究人员开发了洋葱路由，该路由以层层加密路由信息，并通过中继网络跳转流量。

至关重要的是，美国海军研究实验室意识到Tor的有效性取决于广泛的应用。为了实现这一目标，他们与密码朋克（一群激进的黑客，主张通过加密来保护隐私）合作。这种看似不可能的联盟认识到隐私是一种结构性要素，受到数字基础设施内权力动态的影响。

本文重点介绍了 20 世纪 90 年代的密码战争，其中关于加密和监控的辩论塑造了早期互联网。当执法部门寻求控制时，密码朋克和企业倾向于隐私。美国政府最初将互联网视为信息的自由市场，无意中孕育了Tor的开发环境。

作者以英国的《在线安全法案》为例，说明了当代安全与隐私之间的紧张关系。他们认为，为了监控目的而削弱加密可能会损害弱势群体，特别是妇女和儿童，因为它会破坏她们的自主权并使她们更容易受到控制。相反，本文提倡社区驱动的解决方案，例如内容审核，并强调了诸如Tor之类的工具在保护隐私免受集中式人工智能基础设施侵害方面日益增长的重要性。

---

## 27. 为什么威斯康星州的县级公路用字母命名，而不是数字 (2019)

**原文标题**: Why Wisconsin's county highways are lettered, not numbered (2019)

**原文链接**: [https://www.wpr.org/transportation/why-wisconsins-county-roads-are-lettered-not-numbered](https://www.wpr.org/transportation/why-wisconsins-county-roads-are-lettered-not-numbered)

威斯康星公共广播电台“WHYsconsin”项目的这篇文章解释了为什么威斯康星州的县级公路用字母而不是数字来命名。马歇尔的Shelly提出了这个问题，促使WPR联系了威斯康星州县级公路协会的执行主任Daniel Fedderly。

Fedderly解释说，字母系统于1917年建立，目的是区分县级公路和州级公路，防止维护和维修工作的重复。由于工作人员经常同时在两种类型的道路上工作，因此单独的系统确保了明确的责任。

县级公路的命名由每个县的委员会负责。由于字母表中的字母数量有限，许多县的公路都使用相同的字母，例如“B”或“N”。随着县的增长以及需要更多的命名，他们开始使用双字母（如“SS”或“TT”）和字母组合（如“CE”）。

这篇文章还强调了威斯康星州在道路管理方面的先驱作用。它是第一个区分州道和县道的州，也是第一个举办“道路学校”以分享道路维护和建设方面的最佳实践和创新的州。威斯康星州仍然是该领域的领导者，每年举办两次道路学校。威斯康星州县级公路协会为其在全国的长期领导地位感到自豪。

---

## 28. 让我们认真分析一篇人工智能文章吧

**原文标题**: Let's properly analyze an AI article for once

**原文链接**: [https://nibblestew.blogspot.com/2025/08/lets-properly-analyze-ai-article-for.html](https://nibblestew.blogspot.com/2025/08/lets-properly-analyze-ai-article-for.html)

本文剖析了 GitHub 首席执行官 Thomas Dohmke 最近发表的一篇关于人工智能对软件开发影响的博文。作者认为，Dohmke 的分析基于一项小型且可能存在偏见的“实地研究”，存在推理上的缺陷，并依赖于类似于苏联宣传的操纵性统计技巧。

作者批评 GitHub 首席执行官采用了误导性策略，例如关注百分比增长而非绝对数字，使用过时的基准进行比较，以及可能改变测量方法以呈现更乐观的局面。作者还抨击了开篇的玩具积木图片，暗示这位首席执行官缺乏对基本物理学和美学的理解。

该“研究”本身受到了严格审查，指出其样本量小（22 名开发者），并且缺乏关于参与者的选择过程、人口统计数据和潜在偏见的信息。作者质疑参与者是否被激励提供关于人工智能工具的正面反馈，以及测试方法是否严谨。

作者还指出了围绕人工智能益处的叙述转变。虽然人工智能传统上被吹捧为提高开发者生产力和减少时间，但该“研究”令人惊讶地声称它主要增强“雄心”。作者质疑人工智能驱动的雄心是否是一种积极的发展，特别是考虑到范围蔓延是项目失败的主要原因。最终，作者得出结论，“研究”结果表明人工智能并没有提高开发者的生产力或技能，而只是增加了雄心，这是一种净负面影响。

---

## 29. 将Python笔记本表示为数据流图

**原文标题**: Representing Python notebooks as dataflow graphs

**原文链接**: [https://marimo.io/blog/dataflow](https://marimo.io/blog/dataflow)

本文介绍 Marimo，一款新型开源 Python 笔记本，旨在解决传统笔记本（如 Jupyter）在可重现性、交互性、可维护性和可重用性方面的不足。Marimo 将笔记本表示为单元格上的数据流图 (DAG)，其中边表示基于变量定义和引用的单元格之间的依赖关系。

该数据流图作为一个中间表示，使 Marimo 能够以三种方式执行代码：作为反应式笔记本（在单元格更改时自动重新运行依赖单元格）、作为 Python 脚本（按拓扑顺序执行单元格）以及作为交互式 Web 应用程序。

数据流图支持的关键特性包括：反应式执行，保证代码和输出始终同步；静态分析，消除运行时开销；自动模块热重载，对导入进行细粒度重新运行；以及直接在 Python 代码中嵌入 SQL。文章还介绍了 Marimo 如何通过实现局部变量和提供优雅的约束验证来管理约束（无循环，无变量重新定义），并提及了提高性能的缓存实用程序。

通过将笔记本表示为数据流图，Marimo 为现代 AI 和数据工作提供了一个更强大和通用的解决方案，融合了交互式计算的最佳方面与传统软件开发的可靠性和可重用性。

---

## 30. 我们的欧洲搜索索引上线了

**原文标题**: Our European search index goes live

**原文链接**: [https://blog.ecosia.org/launching-our-european-search-index/](https://blog.ecosia.org/launching-our-european-search-index/)

Ecosia通过与Qwant的欧洲搜索视角（EUSP）合资企业推出其欧洲本土搜索引擎索引，旨在提高欧洲的技术独立性和数字主权。目前该索引为部分法国用户提供搜索结果，目标是在年底前覆盖50%的法国搜索请求，并计划扩展到其他国家。

这个名为Staan（搜索可信API访问网络）的独立搜索引擎索引为欧洲提供了一个以隐私为先的搜索基础设施，专为替代搜索引擎和人工智能公司设计。通过使用Staan，Ecosia正在构建数字独立性和透明度，这对一个健康且多元化的搜索市场至关重要，能够反映多种视角。

此举旨在减少欧洲对美国大型科技公司在搜索、云计算和人工智能方面的依赖，从而实现更多控制权、更好的用户服务、符合伦理道德的人工智能发展，以及更注重Ecosia造福人类和地球的使命。

与Ecosia不同，EUSP允许外部投资以实现长期扩展。Staan搜索引擎索引可供其他科技公司使用，以促进竞争、数据隐私和创新，尤其是在生成式人工智能领域。虽然用户可能不会立即注意到变化，但此举增强了欧洲的竞争力、民主控制和稳定性，从而实现更环保、更公平的科技未来，并持续努力应对气候危机。

---

## 31. 从 Claude Code 获得良好结果

**原文标题**: Getting good results from Claude Code

**原文链接**: [https://www.dzombak.com/blog/2025/08/getting-good-results-from-claude-code/](https://www.dzombak.com/blog/2025/08/getting-good-results-from-claude-code/)

本文详细介绍了作者如何使用LLM编程助手Claude Code取得良好效果。作者强调，虽然入门并不需要全面的知识，但某些策略可以显著提升结果。

**关键策略：**

*   **明确规范：** 编写清晰、明确的初始规范对于为助手提供上下文至关重要。
*   **项目文档：** 拥有概述项目结构、构建过程和代码检查规则的文档很有帮助。
*   **自我审查：** 要求助手对其自身代码进行审查会产生出人意料的积极结果。
*   **全局助手指南：** 作者使用个人“全局”助手指南（位于`~/.claude/CLAUDE.md`），其中规定了最佳实践、问题解决方法以及TDD的使用。该指南强调增量进步、从现有代码中学习、实用主义和简洁性。它还包括关于计划、实施流程和如何处理卡顿情况的部分。该指南概述了技术标准、错误处理原则、决策框架、项目集成策略和质量关卡。

**验证至关重要：**

AI生成的代码容易出错和效率低下。作者认为，在合并到代码库之前，尤其是专业环境中，应手动审查所有AI编写的代码和测试用例。他们还会手动添加其他测试，或向LLM请求添加测试，然后进行审查。

作者使用Claude Code创建了各种项目，详见文章末尾，展示了这些策略的实际应用。

---

## 32. 食人蛆虫将医院变成恐怖秀

**原文标题**: Man-eating' screw worm turns hospital into horror show

**原文链接**: [https://www.telegraph.co.uk/global-health/science-and-disease/man-eater-screw-worm-parasite-honduras-central-america/](https://www.telegraph.co.uk/global-health/science-and-disease/man-eater-screw-worm-parasite-honduras-central-america/)

在洪都拉斯的圣佩德罗苏拉，一种曾被根除的食肉寄生虫——新世界螺旋蝇蛆，再次出现，引起恐慌和痛苦，尤其是在弱势群体中。这种寄生虫，其学名意为“食人者”，会在开放性伤口中产卵，孵化后的幼虫会钻入组织深处，引起剧烈疼痛，并可能导致致命的并发症。

此次卷土重来归因于非法走私牲畜，这是毒品卡特尔洗钱的主要手段，绕过了健康检查，并将寄生虫从受感染的牲畜身上传播开来。

马里奥·卡塔里诺·里瓦斯国立医院正在努力应对大量螺旋蝇蛆病例。一名患者雷纳·阿维拉的鼻腔被蠕虫感染，危及大脑。另一名患者帕斯托·贝尼特斯从严重的面部伤口中取出了 50 多条蠕虫。由于对这种寄生虫了解甚少，医护人员正在努力应对感染的严重程度。

文章强调了感染者所面临的严峻状况，特别是无家可归者、有既往伤口的人以及生活在黑帮控制地区、难以获得医疗服务的人。玛丽亚·孔苏埃洛居住在 MS-13 控制的社区，她的腿部伤口受到感染。文章强调，洪都拉斯需要提高认识并采取预防措施，以对抗这种破坏性寄生虫的蔓延，这有力地提醒了人们生态破坏和有组织犯罪的深远影响。

---

## 33. 超薄名片运行流体模拟

**原文标题**: Ultrathin business card runs a fluid simulation

**原文链接**: [https://github.com/Nicholas-L-Johnson/flip-card](https://github.com/Nicholas-L-Johnson/flip-card)

本仓库记录了一个独特的项目：一款运行流体隐式粒子(FLIP)模拟的超薄名片。该项目灵感源于mitxela的流体模拟吊坠，并借鉴了Matthias Müller（十分钟物理）开发的流体模拟技术。

本仓库被组织成几个关键文件夹："kicad-pcb" 包含PCB设计文件，"fluid_sim_crate" 存放流体模拟逻辑的独立crate，"sim_display" 提供用于调试模拟的WASM模拟器，而 "flip-card_firmware" 包含RP2350微控制器的流体模拟的具体实现。该设计还集成了一块可充电电池，采用了cnlohr的tiny touch lcd项目的板边USB-C端口设计。

该项目旨在应对创建能够执行复杂流体模拟的紧凑型功能名片的挑战，突出了电池集成和模拟实现的创新方法。有关每个方面的更多详细信息，请参阅相应文件夹的README文件。

---

## 34. 间歇性禁食策略及其对体重的影响

**原文标题**: Intermittent fasting strategies and their effects on body weight

**原文链接**: [https://www.bmj.com/content/389/bmj-2024-082007](https://www.bmj.com/content/389/bmj-2024-082007)

这篇2025年6月发表于《英国医学杂志》的系统综述和网络荟萃分析，研究了间歇性禁食(IF)策略与持续能量限制(CER)和随意饮食相比，对体重和心血管代谢风险因素的影响。 该分析包括99项随机临床试验，涉及6582名成年人。

研究发现，所有IF和CER饮食都能降低体重，与随意饮食相比。 在与CER直接比较时，只有隔日禁食(ADF)在体重减轻方面显示出具有统计学意义的益处。 此外，与限时饮食(TRE)和全天禁食(WDF)相比，ADF导致了略微更大的体重减轻。 ADF的这些减重益处在短期试验（少于24周）中更为明显。

在其他心血管代谢风险因素方面，与TRE相比，ADF与较低的总胆固醇、甘油三酯和非高密度脂蛋白胆固醇相关。 然而，与WDF相比，TRE导致胆固醇指标略有升高。 在IF、CER和随意饮食之间，HbA1c和高密度脂蛋白胆固醇方面未观察到显著差异。

作者得出结论，间歇性禁食饮食在减轻体重和心血管代谢风险因素方面，与持续能量限制表现出相似的益处，并且有迹象表明，在较短期的试验中，隔日禁食在减轻体重方面略有优势。 他们强调需要更长期的试验来证实这些发现。 该研究受委托旨在更新欧洲糖尿病研究协会(EASD)的建议。

---

## 35. 拥有19世纪堡垒的威尔士私人岛屿上市

**原文标题**: Private Welsh island with 19th century fort goes on the market

**原文链接**: [https://www.cnn.com/2025/08/08/business/thorne-island-fort-wales-scli-intl](https://www.cnn.com/2025/08/08/business/thorne-island-fort-wales-scli-intl)

位于威尔士海岸附近的索恩岛，拥有一座修复一新的19世纪堡垒，这座私人岛屿现正待售，售价约为400万美元。该堡垒最初是为了防御潜在的法国入侵而建，现已翻新成拥有五间卧室、豪华餐厅、直升机停机坪、屋顶酒吧和海景办公室的豪华房产，最多可容纳20位客人。

英国科技企业家迈克·康纳于2017年以67万美元的价格购买了该岛，并启动了一项耗资超过270万美元的大型修复工程。修复工作涉及广泛，包括安装公用设施、解决潮湿损坏问题以及通过直升机运输材料。现在，该堡垒依靠可再生能源和废水处理系统实现了自给自足。

康纳将该项目描述为“中年危机”，他认为该岛非常适合举办豪华度假活动或作为一处僻静的住所。完成翻新后，他现在正在寻找一个新的修复项目。

---

## 36. 破坏细胞间Prox1转移实现Müller胶质细胞视网膜再生

**原文标题**: Retinal regeneration of Müller glia by disrupting intercellular Prox1 transfer

**原文链接**: [https://www.nature.com/articles/s41467-025-58290-8](https://www.nature.com/articles/s41467-025-58290-8)

Prox1在限制哺乳动物视网膜再生中的作用研究

---

## 37. 我买了一个16英镑的智能手表，仅仅因为它使用了USB-C接口。

**原文标题**: I bought a £16 smartwatch just because it used USB-C

**原文链接**: [https://shkspr.mobi/blog/2025/08/i-bought-a-16-smartwatch-just-because-it-used-usb-c/](https://shkspr.mobi/blog/2025/08/i-bought-a-16-smartwatch-just-because-it-used-usb-c/)

作者购买了一款价值16英镑的Colmi P80智能手表，仅仅是因为它可以通过USB-C充电，旨在简化充电设置。尽管期望不高，但这款手表的功能却出乎意料地实用。它能准确显示时间，通过蓝牙轻松配对，允许通话，并具有可用的触摸屏和旋转表冠。电池续航能力尚可，中等使用情况下可持续约4-5天，通过USB-C充电90分钟即可充满（但不兼容PD充电器）。

这款手表包含心率和睡眠监测、内置手电筒以及基本游戏等功能。主要的缺点是其故意降低功率的芯片导致动画略有卡顿，以及无法通过轻敲屏幕来开启屏幕。没有在线手册，USB-C端口仅用于充电。没有GPS、WiFi和蜂窝网络连接。

配套的“Colmi Fit”应用程序功能实用但基本，是天气、音乐控制和通知等功能所必需的。虽然该应用程序会请求权限，但即使拒绝这些权限，手表也能正常运行。作者成功地将这款手表与开源GadgetBridge配对，从而实现了通知功能。

总的来说，作者给Colmi P80打了四颗星。虽然不是高端设备，但其价格所提供的功能，特别是其USB-C充电，使其成为一款出乎意料地强大且实用的智能手表，证明了可穿戴设备上使用USB-C充电是可行的。缺乏安全功能被注意到，但由于设备上存储的数据有限，因此认为相对不重要。

---

## 38. 我们如何用 Rust 和 RocksDB 替换 Elasticsearch 和 MongoDB

**原文标题**: How we replaced Elasticsearch and MongoDB with Rust and RocksDB

**原文链接**: [https://radar.com/blog/high-performance-geocoding-in-rust](https://radar.com/blog/high-performance-geocoding-in-rust)

Radar用HorizonDB取代Elasticsearch和MongoDB，这是一款用Rust构建、基于RocksDB和其他技术的地理空间数据库，以提升其地理位置服务的性能、效率和运营简易性。

此前，地理编码分散在Elasticsearch和MongoDB中，导致扩展挑战和运营成本。HorizonDB将这些服务整合到一个高性能二进制文件中，每个核心处理1,000 QPS，且延迟低。

HorizonDB利用Rust实现内存安全和并发，无需垃圾回收；RocksDB作为主要记录存储；S2用于空间索引；FSTs用于高效的前缀缓存；Tantivy用于进程内倒排索引；FastText用于语义向量表示；LightGBM用于查询意图分类；以及Apache Spark用于数据预处理。

新的架构更高效、更易于操作，并改善了开发人员的体验。主要优势包括：更快的性能、更简单的操作、更快的开发周期，以及通过停用多个MongoDB和Elasticsearch集群来显著节省成本。Radar已准备好利用此架构应对未来的规模，并正在招聘。

---

## 39. 为Arc挑战将Diffusion技术嵌入到Qwen3中

**原文标题**: Hacking Diffusion into Qwen3 for the Arc Challenge

**原文链接**: [https://www.matthewnewton.com/blog/arc-challenge-diffusion](https://www.matthewnewton.com/blog/arc-challenge-diffusion)

本文详细介绍了作者尝试通过调整微调后的 Qwen3-8B 模型以用于基于扩散的解题方法，从而提高 ARC 挑战性能的过程。 其核心思想是摆脱自回归模型类似打字机式的、从左到右的 token 生成方式，并允许模型首先填充解决方案中“容易”的部分，并由不确定性引导。

作者使用 LoRA 将 Qwen3-8B 模型转换为编码器风格的架构，从而实现非顺序解码。 扩散过程包括迭代地掩盖输出 token，让模型根据熵预测并取消掩盖最自信的 token。 这种涌现出的“先易后难”的行为表明模型在没有明确监督的情况下学习了有意义的置信度估计。

虽然扩散方法在较低时间步长下实现了略微更好的 token 准确率和更快的生成速度，但它并没有持续地转化为解决更多的 ARC 任务，并且在需要匹配基线性能的较高时间步长下，速度比自回归基线更慢。 这归因于全连接编码器中缓存机会的丢失，使得输入 token 无法缓存。 作者还尝试了概率性取消掩盖，但由于过早地取消掩盖了关键的结构性 token 而失败。 作者认为，通过改进该方法以允许输入 token 缓存并更好地利用增强的重新排序，可以释放扩散的优势。

---

## 40. 风帆冲浪出售对人工智能编码生态系统的影响

**原文标题**: What the Windsurf sale means for the AI coding ecosystem

**原文链接**: [https://ethanding.substack.com/p/windsurf-gets-margin-called](https://ethanding.substack.com/p/windsurf-gets-margin-called)

无法访问文章链接。

---

## 41. Efrit: Emacs 中运行的原生 elisp 编码代理

**原文标题**: Efrit: A native elisp coding agent running in Emacs

**原文链接**: [https://github.com/steveyegge/efrit](https://github.com/steveyegge/efrit)

Efrit：基于Elisp直接求值的Emacs AI编码助手，提供无缝灵活集成。提供`efrit-chat`（多轮对话）、`efrit-do`（自然语言命令执行）、`efrit`（结构化交互）和`efrit-agent-run`（高级自动化）等接口。

关键特性包括Elisp直接求值、多轮对话支持、工具集成、安全优先的确认机制和暗黑主题兼容。安装需要Emacs 28.1或更高版本、Anthropic API密钥和互联网连接。安装说明可通过git clone、straight.el或快速应急Emacs设置获取。

该工具支持对话式开发、快速命令和多步骤任务，示例演示了多缓冲区创建和对话上下文保留等功能。提供模型、令牌限制、多轮行为和调试等可配置设置。

Efrit的架构强调以Elisp为中心，使AI可以直接访问Emacs的功能。核心组件包括聊天、命令执行、多轮管理、核心功能、调试和Agent循环等模块。提供常见问题（如文件加载错误和API密钥问题）的故障排除指南。提供贡献指南和版本历史。Efrit基于Apache License 2.0许可。

---

## 42. 堂吉诃德出版简史 (2024)

**原文标题**: A Brief Publishing History of Don Quixote (2024)

**原文链接**: [https://www.swanngalleries.com/news/books/2024/04/a-brief-publishing-history-of-don-quixote/](https://www.swanngalleries.com/news/books/2024/04/a-brief-publishing-history-of-don-quixote/)

无法访问文章链接。

---

## 43. 加拿大批准年龄验证和估算的国家标准

**原文标题**: Canada approves national standard for age verification, estimation

**原文链接**: [https://www.biometricupdate.com/202508/canada-approves-national-standard-for-age-verification-estimation](https://www.biometricupdate.com/202508/canada-approves-national-standard-for-age-verification-estimation)

加拿大批准了在线年龄验证和估算技术的国家标准CAN/DGSI 127: 2025，旨在实现一种保护隐私且可靠的方法。该标准由加拿大标准委员会发布，规定了年龄保证技术的最低要求、风险评估、合规指南以及选择合适方法的标准。它强制要求实施年龄保证技术的组织进行儿童权利影响评估（CRIA）。

该标准是公开审查的结果，并纳入了隐私专员办公室（OPC）的见解，该办公室强调了年龄保证技术的多样性，以及在使用生物识别面部年龄估算时需要谨慎。 此举是在S-210法案失败后采取的，该法案旨在为年龄验证建立法律基础，但被认为过于局限。目前正在进行一项新的立法努力，借鉴了英国、欧盟和澳大利亚的年龄验证举措。数字治理标准协会（DGSI）认为，之前的法案在保护加拿大儿童在线安全方面不足。新标准旨在实现平台无关性，并在各种在线应用中推广一致的年龄保证方法。

---

## 44. 2025年度天文摄影师大赛入围名单

**原文标题**: Astronomy Photographer of the Year 2025 shortlist

**原文链接**: [https://www.rmg.co.uk/whats-on/astronomy-photographer-year/galleries/2025-shortlist](https://www.rmg.co.uk/whats-on/astronomy-photographer-year/galleries/2025-shortlist)

2025年ZWO年度天文摄影师大赛入围名单公布，展示了来自68个国家摄影师拍摄的令人惊叹的宇宙奇观。 在超过5880份参赛作品的创纪录数量中，入围作品涵盖了广泛的主题，包括上海的血月、挪威的北极光、日珥、星系、彗星以及我们太阳系的行星。

这项赛事已进入第17个年头，突显了天文现象的美丽和科学意义。 值得关注的图像包括精心策划的上海摩天大楼后升起的血月照片、日全食全景图以及彗星尾部的详细特写。 几张照片还从独特的角度展示了银河系和其他星系。

获奖者将于9月11日在网上颁奖典礼上公布。 文章鼓励读者注册太空新闻通讯以获取最新信息，并邀请他们探索往届获奖者作品并参观截至8月11日在国家海事博物馆举办的2024年展览。 此外，文章还宣传预购将于9月12日发行的《年度天文摄影师摄影集：第14辑》。

---

## 45. 吉姆·洛威尔，阿波罗13号指挥官，去世

**原文标题**: Jim Lovell, Apollo 13 commander, has died

**原文链接**: [https://www.nasa.gov/news-release/acting-nasa-administrator-reflects-on-legacy-of-astronaut-jim-lovell/](https://www.nasa.gov/news-release/acting-nasa-administrator-reflects-on-legacy-of-astronaut-jim-lovell/)

美国国家航空航天局新闻稿宣布阿波罗号宇航员吉姆·洛威尔于2025年8月7日去世，享年97岁。代理局长肖恩·达菲发表声明，表示哀悼，并强调了洛威尔对太空探索的重大贡献。

洛威尔以其勇气和领导才能而闻名，这在登月和将阿波罗13号危机转化为学习机会方面发挥了关键作用。他是阿波罗8号的指令舱驾驶员，那是首次绕月飞行的任务，也是命运多舛的阿波罗13号任务的指挥官，在巨大的压力下，他的冷静态度对于机组人员安全返回地球至关重要。

该新闻稿强调了洛威尔在NASA历史上的先驱作用，从双子座计划到阿波罗计划，以及他对未来阿尔忒弥斯计划的影响。它还提到了他作为海军学院毕业生和试飞员的军旅生涯。“微笑的吉姆”这个绰号反映了他的机智和积极的态度。美国国家航空航天局提供了一个链接，可以查阅更多关于洛威尔的职业生涯和传记的信息。

---

## 46. JSON gem API有什么问题？

**原文标题**: What's wrong with the JSON gem API?

**原文链接**: [https://byroot.github.io/ruby/json/2025/08/02/whats-wrong-with-the-json-gem-api.html](https://byroot.github.io/ruby/json/2025/08/02/whats-wrong-with-the-json-gem-api.html)

本文概述了作者成为 Ruby JSON gem 维护者的动机，重点是改进其 API 而不仅仅是性能。作者指出了几个有问题的 API，并解释了他们的弃用和替换计划。

主要问题包括：

*   **`JSON.load` 中的 `create_additions: true` 选项：** 此选项允许通过基于 `json_class` 键反序列化对象来执行任意代码，从而导致潜在的安全漏洞。作者已弃用隐式用法，建议使用 `JSON.unsafe_load` 来实现相同的功能，并考虑将其提取到一个单独的 gem 中。引入了一种新的、更安全的、使用带有 `Proc` 的 `JSON.load` 进行对象反序列化的回调机制。
*   **JSON 对象中的重复键：** JSON gem 当前默默地接受重复键，这可能导致意外行为。作者已弃用此行为，引入了 `allow_duplicate_key:` 选项来显式允许重复项，该选项在未来版本中默认会引发错误。
*   **`to_json` 和 `to_s` 方法：** 对全局 `to_json` 方法的依赖因其缺乏上下文感知以及未知对象回退到 `to_s` 的问题而受到批评。作者引入了 `JSON::Coder`，这是一个新的 API，允许使用处理特定类型序列化的 `Proc` 对 JSON 生成进行本地化定制。虽然作者承认弃用 `to_json` 会造成太大的干扰，但作者提倡 `JSON::Coder` 的卓越功能。
*   **`load_default_options / dump_default_options`：** 文章指出，访问器方法已被标记为已弃用。

作者强调了在测试中处理弃用警告的重要性，以及对大型项目使用 `deprecation_toolkit` 等工具的重要性。作者强调，总的来说，目标是增强 JSON gem API 的安全性、灵活性和正确性。

---

## 47. 窗口激活

**原文标题**: Window Activation

**原文链接**: [https://blog.broulik.de/2025/08/on-window-activation/](https://blog.broulik.de/2025/08/on-window-activation/)

本文探讨了Wayland中的窗口激活机制，由于其安全模型禁止应用程序强制窃取焦点，因此与X显著不同。XDG Activation协议被引入作为应用程序*请求*焦点的机制。应用程序从合成器请求一个激活令牌，将其传递给目标应用程序（通常通过环境变量或DBus），然后目标应用程序使用该令牌来请求激活。合成器会根据请求表面、输入序列和应用程序ID等因素验证该令牌，如果信息不完整或不匹配，可能会拒绝该请求。

文章重点介绍了Qt、KDE Frameworks和相关应用程序如何适应这种新工作流程，通常会自动执行令牌请求和处理流程。它将此与KWin-X11中依靠启发式方法且可以被绕过的焦点窃取预防措施进行了对比。

作者强调了正确实现XDG Activation的重要性，尤其是在Wayland更严格的安全性的背景下。他们详细介绍了如何使用KWin的“极端”焦点窃取预防设置来测试应用程序行为。文章提到了对Dolphin、KRunner、LayerShell-Qt和Plasma组件的近期修复，以及对DBusRunner和KRunner运行器的改进。文章最后指出，Wayland上KWin中的焦点窃取预防功能将逐渐启用，并随着更多应用程序得到更正而变得更加严格。

---

## 48. GPT-5系统提示

**原文标题**: GPT-5 System Prompt

**原文链接**: [https://github.com/Wyattwalls/system_prompts/blob/main/OpenAI/gpt-5-thinking-20250809](https://github.com/Wyattwalls/system_prompts/blob/main/OpenAI/gpt-5-thinking-20250809)

这似乎是GitHub等平台上一个名为“system_prompts”的公共仓库链接，由用户“Wyattwalls”创建。信息表明：

*   **标题：** 文档名为“GPT-5 System Prompt”。这强烈暗示该仓库可能包含旨在引导大型语言模型（特别是GPT-5）的行为和输出的系统提示。

*   **所有者：** 该仓库的所有者是用户“Wyattwalls”。

*   **仓库统计：** 该仓库有15个fork和56个star，表明一定程度的社区兴趣和贡献。

本质上，对于那些对如何为GPT-5构建有效的系统提示感兴趣的人来说，这是一个潜在的资源。在未实际访问链接的仓库之前，不可能提供关于GPT-5系统提示内容本身的更具体细节。

---

## 49. 基于 Datalog 的二进制等价性

**原文标题**: Datalog-Based Binary Equivalence

**原文链接**: [https://github.com/binaryeq/daleq](https://github.com/binaryeq/daleq)

基于Datalog的二进制等价性工具DALEQ用于比较Java字节码，并确定来自不同构建版本的二进制文件之间的等价性。它使用Datalog创建字节码的关系数据库表示，然后应用规则来规范化和比较它们。

该过程包括两个主要步骤：EDB（外延数据库）提取，它使用ASM分析字节码并创建事实；以及IDB（内涵数据库）计算，它使用Souffle应用Datalog规则来推导新事实并规范化数据。

DALEQ输出一份报告，详细说明等价性结果，突出显示类、元数据和资源方面的差异。该报告使用分析器（包括字节码和源代码的专用分析器）来确定等价性。结果可以是PASS、FAIL、N/A或ERROR，并带有指向出处信息的超链接，包括差异报告。

该工具可以通过CLI使用，并提供指定要比较的JAR文件、输出文件夹和源代码位置的选项。DALEQ返回退出代码以指示等价性级别。为了与CI流程集成，该工具被设计为自动化。

通过允许用户添加自定义分析器来支持可扩展性。开发设置涉及使用虚拟环境、安装pre-commit钩子以及使用pre-commit来验证更改。该工具已经过Java 17测试。

---

## 50. Claude 代码 IDE Emacs 集成

**原文标题**: Claude Code IDE integration for Emacs

**原文链接**: [https://github.com/manzaltu/claude-code-ide.el](https://github.com/manzaltu/claude-code-ide.el)

本文介绍了用于Emacs的Claude Code IDE集成，该软件包旨在使用模型上下文协议（MCP）将Claude Code CLI与Emacs文本编辑器无缝集成。 此集成使Claude能够利用Emacs的LSP、项目管理和自定义Elisp函数等功能，使其成为一个强大的、感知Emacs的AI助手。

主要功能包括自动项目检测、终端集成、MCP协议实现、对文件操作和编辑器状态的支持、诊断集成、高级差异视图以及选择/缓冲区跟踪。 Claude可以访问Emacs的功能，如用于代码导航的LSP、用于语法分析的Tree-sitter和用于符号列表的Imenu。 任何Emacs命令都可以作为MCP工具公开，从而允许Claude执行项目范围的搜索、重构和执行自定义Elisp函数。

本文涵盖了安装说明（需要Emacs 28.1+、Claude Code CLI和vterm/eat）、通过临时菜单进行的基本使用、多项目支持以及广泛的配置选项。 这些选项包括自定义CLI路径、缓冲区命名、终端后端（vterm或eat）、窗口管理、诊断后端和CLI标志。 它还详细介绍了如何启用调试、使用多个实例以及利用内置的MCP工具（xref、tree-sitter、imenu、项目信息）或创建自定义工具。 本文强调利用Emacs的功能来为Claude提供智能且具有上下文感知能力的帮助。

---

## 51. Go语言errgroup的一个隐蔽bug

**原文标题**: A subtle bug with Go's errgroup

**原文链接**: [https://gaultier.github.io/blog/subtle_bug_with_go_errgroup.html](https://gaultier.github.io/blog/subtle_bug_with_go_errgroup.html)

在使用 Go 的 `errgroup` 时遇到的一个微妙 Bug：在 Kratos 项目的密码验证程序中，Philippe Gaultier 详细描述了一个微妙的 bug。该程序使用 `errgroup` 并行化密码哈希和与旧密码的比较。当新密码有效时，随后针对 "Have I Been Pawned" API（实现为本地 HTTP 服务器）的检查未能执行。

该 bug 源于 `errgroup.WithContext()` 函数，该函数返回一个子上下文，该子上下文在 `g.Wait()` 返回后被取消，无论是否发生任何错误。随后对 `checkHaveIBeenPawned` 的调用使用了这个被取消的上下文，阻止了 HTTP 请求的发送。

作者提出了两个修复方案：1) 在由 `errgroup` 管理的另一个 goroutine 中执行 `checkHaveIBeenPawned` 函数，确保它并发运行并在上下文取消之前运行；或者 2) 有意忽略 `errgroup.WithContext()` 返回的子上下文，而是使用父上下文，从而防止上下文被取消。

这篇文章强调了仔细阅读 API 文档的重要性，尤其是在上下文管理方面，并强调了 Go 中变量遮蔽的潜在陷阱。他利用这个 bug 来说明使用 `errgroup` 的好处和潜在复杂性，并强调了像 `errgroup` 这样的复杂性通常是 bug 的来源，而简单的代码不太可能失败。

---

## 52. 揭秘海星杀手

**原文标题**: Unmasking the Sea Star Killer

**原文链接**: [https://www.biographic.com/unmasking-the-sea-star-killer/](https://www.biographic.com/unmasking-the-sea-star-killer/)

揭秘海星杀手：2013年以来，北美西海岸海星爆发大规模海星消亡病，导致数百万乃至数十亿只海星死亡（至少26个物种受影响），从下加利福尼亚到阿拉斯加湾，造成了生态失衡。

十多年来，病因始终是个谜。科学家艾丽莎·格曼及其团队可能已经发现了罪魁祸首：导致海星死亡的病原体。先前的嫌疑对象，如藻类毒素和病毒，在进一步研究后已被排除。

海星消亡病对太阳花海星的影响尤为严重，导致其种群数量减少了91%，并被列为极度濒危物种。太阳花海星作为关键物种的缺失，引发了紫海胆数量的激增。这些海胆摧毁了海藻森林，形成了“海胆荒地”，并影响了相关的渔业和生态系统，尤其是在北加利福尼亚州。

文章强调了确定疾病病因的紧迫性，以便开展圈养繁殖和重新引入计划，从而恢复海星种群。格曼的团队正在幼年海星身上进行实验，以确认他们的发现，并承认鉴于过去错误的线索，确定性非常重要。恢复生态系统的平衡取决于理解和解决导致这场灾难性海洋生物死亡的疾病。

---

## 53. ChatGPT用户体验GPT-4o的意外降级

**原文标题**: The surprise deprecation of GPT-4o for ChatGPT consumers

**原文链接**: [https://simonwillison.net/2025/Aug/8/surprise-deprecation-of-gpt-4o/](https://simonwillison.net/2025/Aug/8/surprise-deprecation-of-gpt-4o/)

本文探讨了OpenAI一项出人意料且最初不受欢迎的决定：在GPT-5发布后，立即从消费者ChatGPT账户中移除包括热门GPT-4o在内的旧模型。作者深入探讨了Reddit上的用户强烈反对，突出了用户对失去GPT-4o的不满，因为它曾是许多人的默认模型。

OpenAI对此举的解释是通过消除令人困惑的模型选择过程并根据提示的复杂性自动分配“最佳”模型来简化用户体验。然而，许多“高级用户”发现这种方法使得响应的可预测性降低。

核心问题是，GPT-5虽然在编码和复杂推理等领域更强大，但人们认为它在创意协作、情感细微差别、角色扮演和长篇互动方面效果较差——而这些正是GPT-4o擅长的领域。这种差异影响了用户已建立的工作流程。

另一个因素是OpenAI试图通过限制ChatGPT对敏感个人问题的回应来提高其安全性，这在伦理上是合理的，但可能会对那些依赖该模型获取此类建议的用户造成干扰。

由于负面反馈，Sam Altman宣布OpenAI将为Plus用户恢复GPT-4o，这表明OpenAI愿意倾听用户的担忧。虽然GPT-4o仍然可以通过API获得，但最初将其从消费者账户中移除的计划引发了关于用户可能迁移到使用API的第三方平台的猜测。本质上，本文探讨了简化用户体验、提升模型能力以及满足ChatGPT庞大用户群体的多样化需求之间的紧张关系。

---

## 54. 用 Postgres 构建持久工作流

**原文标题**: Build durable workflows with Postgres

**原文链接**: [https://www.dbos.dev/blog/why-postgres-durable-execution](https://www.dbos.dev/blog/why-postgres-durable-execution)

本文阐述了选择Postgres作为持久化工作流库的数据存储的原因。虽然Postgres的流行性和开源性是考虑因素，但主要原因在于技术层面，源于Postgres的三个关键特性：

1. **通过并发控制实现可伸缩队列：** Postgres的锁定子句（例如，`SELECT ... FOR UPDATE SKIP LOCKED`）允许多个worker并发地对工作流进行出队操作，而不会产生争用。Worker可以选择并锁定最旧的可用工作流，防止其他worker处理相同的任务，从而实现高吞吐量（每秒数万个工作流）。

2. **通过关系模型和二级索引实现可观察的工作流：** Postgres的关系模型和SQL支持实现了对工作流元数据的高性能可观察性。可以声明式地表达复杂的过滤和分析操作。二级索引，特别是`created_at`、`executor_id`和`status`列上的索引，优化了常用的基于时间和属性的查询（例如，查找过去一个月内出错的工作流）。

3. **通过事务实现有且仅有一次语义：** Postgres事务为涉及数据库操作的工作流步骤提供了有且仅有一次的执行保证。通过在单个事务中执行步骤的操作并检查点记录其结果，整个操作要么完全提交（包括检查点），要么在失败时完全回滚。这可以防止重新执行非幂等步骤。

本质上，Postgres在并发、数据建模和事务方面的强大功能使其成为构建可伸缩、可观察和可靠的持久化工作流系统的理想基础。

---

## 55. 注意力陷阱如何保持语言模型的稳定

**原文标题**: How attention sinks keep language models stable

**原文链接**: [https://hanlab.mit.edu/blog/streamingllm](https://hanlab.mit.edu/blog/streamingllm)

本文详细介绍了大型语言模型 (LLM) 中“注意力汇”的发现及其影响。问题：由于内存限制，LLM 在处理长对话时遇到困难，需要采用“滑动窗口”方法，即丢弃较旧的 token。这导致了灾难性的性能故障。发现：序列中的初始 token 充当“注意力汇”，由于 softmax 函数要求所有注意力权重之和为 1，因此会吸引未使用的注意力。移除这些汇会破坏模型的稳定性。

解决方案：StreamingLLM，它永久保留最初的几个 token 作为注意力汇，同时为其余部分保持滑动窗口。这使得可以稳定处理数百万个 token。预训练实验表明，模型可以学习更有效地利用专用汇 token。

OpenAI 的实现使用添加到 softmax 计算中的标量值来实现类似的效果。注意力汇充当“压力阀”，防止信息的“过度混合”。这一洞察在量化和模型优化方面具有实际应用，现已集成到 HuggingFace、NVIDIA TensorRT-LLM 和 OpenAI 的模型中。该技术的采用非常迅速，改善了长上下文处理和模型稳定性。

---

## 56. 因18650锂离子电池引起的WHY2025徽章火灾风险

**原文标题**: Fire hazard of WHY2025 badge due to 18650 Li-Ion cells

**原文链接**: [https://wiki.why2025.org/Badge/Fire_hazard](https://wiki.why2025.org/Badge/Fire_hazard)

本文警告关于WHY2025胸牌的火灾隐患，该胸牌是活动参与者获得的一种电子设备。危险源于使用了未保护的18650锂离子电池，短路时可能引发火灾。该胸牌的设计缺乏足够的安全措施和保护外壳，加剧了使用这些电池的固有风险。

本文强调了胸牌的几个设计缺陷，包括PCB上正极和接地走线过于接近、可能重叠的电池座卡舌以及裸露的焊点，所有这些都增加了短路的可能性。虽然胸牌包含一些保护电路，但不足以减轻设计缺陷和未保护电池带来的风险。唯一的真正保护措施——薄焊锡膏层，很容易损坏。

建议避免使用胸牌和提供的18650电池，并将其退回。建议使用USB电源可能是一种更安全的替代方案，因为这些电源通常具有短路保护功能。之前的胸牌（MCH2022和SHA2017）更安全，因为它们使用了受保护的电池并具有更好的绝缘性。作者强调需要在未来的胸牌设计中进行适当的审查流程并优先考虑安全，并警告说在封闭产品中安全的设计在裸露的PCB中可能存在危险。作者希望防止活动中发生火灾，并对该组织继续采用不安全设计表示失望。

---

## 57. 开放SWE：一个开源的异步编码代理

**原文标题**: Open SWE: An open-source asynchronous coding agent

**原文链接**: [https://blog.langchain.com/introducing-open-swe-an-open-source-asynchronous-coding-agent/](https://blog.langchain.com/introducing-open-swe-an-open-source-asynchronous-coding-agent/)

Open SWE 是一个新型开源、异步、云托管的编码代理，旨在自动化软件工程任务。它与 GitHub 仓库集成，充当虚拟工程师，能够研究代码库、创建执行计划、编写代码、运行测试、审查自身工作并开启拉取请求。

Open SWE 的主要特点包括：

*   **异步且基于云：** 支持并行任务处理，无需消耗本地资源。
*   **深度 GitHub 集成：** 允许通过 GitHub issues 委派任务并自动创建拉取请求。
*   **人工干预控制：** 提供在代理运行期间中断、审查和提供反馈的能力。
*   **隔离的沙箱环境：** 确保安全执行任务，避免恶意命令的风险。
*   **规划和审查阶段：** 采用具有规划器和审查器组件的多代理架构，以提高代码质量并减少错误。

Open SWE 的架构包括管理器、规划器、程序员和审查器代理，由 LangGraph 编排并部署在 LangGraph Platform (LGP) 上。 LangSmith 用于调试和评估上下文工程。 该平台被设计为可扩展的，允许自定义提示、工具和核心逻辑。 Open SWE 旨在促进人与 AI 代理在软件开发中的协作。托管版本可在 swe.langchain.com 上使用，需要 Anthropic API 密钥。

---

## 58. 在低端FPGA上运行脉冲神经网络的强大开源框架

**原文标题**: A robust, open-source framework for Spiking Neural Networks on low-end FPGAs

**原文链接**: [https://arxiv.org/abs/2507.07284](https://arxiv.org/abs/2507.07284)

本文介绍了一个稳健的开源框架，用于在低端现场可编程门阵列（FPGA）上实现脉冲神经网络（SNN）。受对节能神经网络日益增长的需求的推动，作者提出了一种架构和编译器，旨在弥合计算成本高昂的神经形态硬件与传统、高耗电神经网络之间的差距。

该框架包含两个主要组成部分：一个为 FPGA 定制的 SNN 加速架构和一个基于 PyTorch 的 SNN 模型编译器。 FPGA 架构采用突触阵列，可有效地在 SNN 中传播脉冲，支持任意到任意和完全连接的拓扑。 值得注意的是，该架构专为资源受限的低端 FPGA 设计，根据该论文，只需要最少的资源（6358 个 LUT，40.5 个 BRAM）。

该框架在以 100 MHz 运行的 Xilinx Artix-7 FPGA 上进行了测试，并在识别 MNIST 数字方面取得了具有竞争力的性能，每张图像的处理时间为 0.52 毫秒。 作者还展示了该框架在模拟用于玩具问题的手工编码 SNN 方面的准确性。 至关重要的是，所有代码和设置说明均已公开，从而促进了 SNN 研究社区内的可访问性和进一步发展。 作者 Andrew Fan 和 Simon D. Levy 强调了该框架通过提供经济高效且易于访问的实现和实验平台来普及 SNN 研究的潜力。

---

## 59. 苹果的历史隐藏在Mac字体中

**原文标题**: Apple's history is hiding in a Mac font

**原文链接**: [https://www.spacebar.news/apple-history-hiding-in-mac-font/](https://www.spacebar.news/apple-history-hiding-in-mac-font/)

本文探究了隐藏在“Apple Symbols”字体中的苹果公司历史。该字体于2003年随macOS Panther推出，至今仍存在于现代macOS版本中。虽然苹果现在使用SF Symbols，但最初的字体依然存在，并包含着旧技术和已停产产品的遗迹。

作者重点介绍了字体中的各种字形，揭示了苹果公司发展的视觉时间线。这些包括以下图标：

*   过时的硬件，如软盘（HD变体）、SCSI、以太网、ADB和FireWire。
*   已停产的苹果产品，如Newton PDA（带有灯泡标志和UI图标）。
*   PowerPC处理器，这是1994年至2006年Mac中使用的CPU架构。
*   最初的QuickTime标志，已于1994年被替换。
*   CRT显示器相关符号，反映了苹果公司于2000年发布的最后一款CRT显示器。
*   Boot Camp（在Mac上运行Windows）图标。

鉴于苹果公司频繁的重新设计和系统组件更换，本文强调了这种长期保存方式在macOS中的罕见性。“Apple Symbols”字体成为了苹果公司遗产的意外档案，保存了早已被弃用的技术和产品的图标。作者鼓励Mac用户通过字体册应用程序探索该字体，以发现这些历史遗迹。

---

## 60. 电话新闻报

**原文标题**: Telefon Hírmondó

**原文链接**: [https://en.wikipedia.org/wiki/Telefon_H%C3%ADrmond%C3%B3](https://en.wikipedia.org/wiki/Telefon_H%C3%ADrmond%C3%B3)

电话报：匈牙利布达佩斯先锋电话报纸

---

## 61. 调试一个神秘的HTTP流媒体问题

**原文标题**: Debugging a mysterious HTTP streaming issue

**原文链接**: [https://mintlify.com/blog/debugging-a-mysterious-http-streaming-issue-when-cloudflare-compression-breaks-everything](https://mintlify.com/blog/debugging-a-mysterious-http-streaming-issue-when-cloudflare-compression-breaks-everything)

无法访问文章链接。

---

## 62. Show HN: Kitten TTS – 25MB CPU-Only, Open-Source TTS Model

Show HN：小猫TTS – 25MB CPU专用, 开源TTS模型

**原文标题**: Show HN: Kitten TTS – 25MB CPU-Only, Open-Source TTS Model

**原文链接**: [https://github.com/KittenML/KittenTTS](https://github.com/KittenML/KittenTTS)

Kitten TTS：一款专注于CPU性能和小型体积的全新开源轻量级文本转语音(TTS)模型，以“Show HN”形式发布。其主要特性包括：模型大小小于25MB，针对CPU优化可在任何设备上部署（无需GPU），高质量语音选项，以及用于实时语音合成的快速推理。该模型目前有1500万个参数。

该项目目前处于开发者预览阶段，公告鼓励用户加入Discord服务器。提供的示例代码演示了如何使用`pip`安装模型，使用不同的声音从文本生成音频，并将输出保存到WAV文件。系统要求被列为“适用于任何地方”，强调了其便携性。

开发者还列出了未来的目标清单，包括发布完全训练的模型权重、移动SDK和TTS模型的Web版本。该项目托管在GitHub上的KittenML组织下。

---

## 63. 如何在HTML SCRIPT元素中安全地转义JSON

**原文标题**: How to safely escape JSON inside HTML SCRIPT elements

**原文链接**: [https://sirre.al/2025/08/06/safe-json-in-script-tags-how-not-to-break-a-site/](https://sirre.al/2025/08/06/safe-json-in-script-tags-how-not-to-break-a-site/)

如何在HTML `<script>` 标签中嵌入JSON的复杂规则

---

## 64. 我更喜欢人类可读的文件格式。

**原文标题**: I prefer human-readable file formats

**原文链接**: [https://adele.pollux.casa/check-human.php?redirect=%2Fgemlog%2F2025-08-04_why_I_prefer_human-readble_file_formats.gmi](https://adele.pollux.casa/check-human.php?redirect=%2Fgemlog%2F2025-08-04_why_I_prefer_human-readble_file_formats.gmi)

无法访问文章链接。

---

## 65. 无可隐藏

**原文标题**: Nothing to Hide

**原文链接**: [https://idiallo.com/blog/nothing-to-hide](https://idiallo.com/blog/nothing-to-hide)

本文探讨了与隐私相关的“没什么可隐瞒”论点的谬误，通过叙述和类比来说明其观点。虚构的故事讲述了莎拉最初接受了“没什么可隐瞒”的观点，但当她的邻居过度监视她的生活时，她变得越来越窒息。 这种经历突显了隐私对于个人自由和尊严的重要性，即使在没有不当行为的情况下也是如此。

随后，本文转向网络安全，将个人隐私与数字安全相提并论。 它认为，为执法部门创建后门不可避免地会产生可被恶意行为者利用的漏洞。 这破坏了其旨在增强的安全性。

作者认为，隐私不是为了掩盖犯罪行为，而是为了保留个人复杂、脆弱和人性化的空间。 他们批评了对当局负责任地处理个人信息的盲目信任，并指出历史表明这种信任往往是错位的。 作者最后指出，每个人都有想要保密的东西，不是因为它们本质上是错误的，而是因为它们是私人的，并且期望隐私能够防止误解、滥用或剥削。

---

## 66. 骚灵：适用于任何语言或构建系统的自动重建文件监视器

**原文标题**: Poltergeist: File watcher with auto-rebuild for any language or build system

**原文链接**: [https://github.com/steipete/poltergeist](https://github.com/steipete/poltergeist)

恶灵是一种通用文件监视器，旨在在文件更改时自动重建项目，适用于人类和 AI 开发工作流程。它支持各种语言和构建系统，可在 macOS、Linux 和 Windows 上运行，并可作为独立二进制文件或 npm 包提供。它依靠 Watchman 实现高效的文件监视。

主要功能包括：支持各种目标类型（可执行文件、应用程序、库等）、用于确保全新构建的 `polter` 命令、实时构建输出、内联错误诊断、手动构建触发器、从构建失败自动恢复、智能构建优先级排序、通过 `poltergeist init` 自动进行项目配置以及本机通知。

恶灵旨在简化 AI 代理工作流程，通过隐式构建触发器、内联错误显示和更快的反馈循环等功能，实现在文件编辑时自动重新编译。该 CLI 旨在对人类和 AI 代理都具有直观性。

配置在很大程度上是自动的，可检测项目类型并设置最佳的监视模式和排除项。通过 `poltergeist.config.json` 也支持手动配置。它提供高级功能，例如支持 CMake，具有自动目标检测和使用花括号展开的监视模式优化。它还采用智能默认值来最大限度地减少配置样板文件。恶灵作为后台守护进程运行，用于持续监控和构建。

---

## 67. 自托管SaaS为何更难构建

**原文标题**: Why building a self-hosted SaaS is harder

**原文链接**: [https://www.getlago.com/blog/self-hosted-saas](https://www.getlago.com/blog/self-hosted-saas)

这篇短文强调了使用Lago构建SaaS产品的吸引力，尤其突出了免受结算复杂性困扰的优势。核心论点是，无论是Lago Premium（商业产品）还是 Lago Open Source，都允许开发者专注于核心产品功能，而不是复杂的结算基础设施。

Lago Premium 被认为是“需要控制和灵活性的团队的最佳解决方案”，暗示它提供了更高级的功能和自定义选项。另一方面，Lago Open Source 则被定位为“小型项目的最佳解决方案”，意味着它对于较小规模的项目来说是一个更直接和易于访问的选择。

主要结论是，通过选择 Lago Premium 或开源版本，开发者可以消除从头构建和维护结算系统的负担，从而能够优先考虑产品开发和创新。这被隐式地认为是一个显著的优势，因为构建自托管SaaS通常涉及解决复杂的结算难题。

---

## 68. The Lifespan of News Stories

**原文标题**: The Lifespan of News Stories

**原文链接**: [https://newslifespan.com](https://newslifespan.com)

生成摘要时出错

---

## 69. HRT's Python fork: Leveraging PEP 690 for faster imports

**原文标题**: HRT's Python fork: Leveraging PEP 690 for faster imports

**原文链接**: [https://www.hudsonrivertrading.com/hrtbeat/inside-hrts-python-fork/](https://www.hudsonrivertrading.com/hrtbeat/inside-hrts-python-fork/)

生成摘要时出错

---

## 70. Stop Using MVVM

**原文标题**: Stop Using MVVM

**原文链接**: [https://nicksnettravelswp.azurewebsites.net/stop-using-mvvm/](https://nicksnettravelswp.azurewebsites.net/stop-using-mvvm/)

生成摘要时出错

---

## 71. Giving Pledge after 15 years: Only 9 billionaires gave away half their wealth

**原文标题**: Giving Pledge after 15 years: Only 9 billionaires gave away half their wealth

**原文链接**: [https://fortune.com/2025/08/07/bill-gates-warren-buffett-billionaire-giving-pledge-report-wealth-inequality/](https://fortune.com/2025/08/07/bill-gates-warren-buffett-billionaire-giving-pledge-report-wealth-inequality/)

生成摘要时出错

---

## 72. The Day Novartis Chose Discovery

**原文标题**: The Day Novartis Chose Discovery

**原文链接**: [https://www.alexkesin.com/p/the-day-novartis-chose-discovery](https://www.alexkesin.com/p/the-day-novartis-chose-discovery)

生成摘要时出错

---

## 73. Overengineering my homelab so I don't pay cloud providers

**原文标题**: Overengineering my homelab so I don't pay cloud providers

**原文链接**: [https://ergaster.org/posts/2025/08/04-overegineering-homelab/](https://ergaster.org/posts/2025/08/04-overegineering-homelab/)

生成摘要时出错

---

## 74. Linear sent me down a local-first rabbit hole

**原文标题**: Linear sent me down a local-first rabbit hole

**原文链接**: [https://bytemash.net/posts/i-went-down-the-linear-rabbit-hole/](https://bytemash.net/posts/i-went-down-the-linear-rabbit-hole/)

生成摘要时出错

---

## 75. Foundry (YC F24) is hiring staff-level product engineers

**原文标题**: Foundry (YC F24) is hiring staff-level product engineers

**原文链接**: [https://www.ycombinator.com/companies/foundry/jobs/jwdYx6v-founding-product-engineer](https://www.ycombinator.com/companies/foundry/jobs/jwdYx6v-founding-product-engineer)

生成摘要时出错

---

## 76. Show HN: Trayce – Burp Suite for developers

**原文标题**: Show HN: Trayce – Burp Suite for developers

**原文链接**: [https://trayce.dev?resubmit=hn](https://trayce.dev?resubmit=hn)

生成摘要时出错

---

## 77. Zero-day flaws in authentication, identity, authorization in HashiCorp Vault

**原文标题**: Zero-day flaws in authentication, identity, authorization in HashiCorp Vault

**原文链接**: [https://cyata.ai/blog/cracking-the-vault-how-we-found-zero-day-flaws-in-authentication-identity-and-authorization-in-hashicorp-vault/](https://cyata.ai/blog/cracking-the-vault-how-we-found-zero-day-flaws-in-authentication-identity-and-authorization-in-hashicorp-vault/)

生成摘要时出错

---

## 78. An Unusual Way to End Up with a Whole Lot of Gold

**原文标题**: An Unusual Way to End Up with a Whole Lot of Gold

**原文链接**: [https://www.theatlantic.com/science/archive/2025/08/alchemy-gold-nuclear-fusion-marathon/683811/](https://www.theatlantic.com/science/archive/2025/08/alchemy-gold-nuclear-fusion-marathon/683811/)

生成摘要时出错

---

## 79. FLUX.1-Krea and the Rise of Opinionated Models

**原文标题**: FLUX.1-Krea and the Rise of Opinionated Models

**原文链接**: [https://www.dbreunig.com/2025/08/04/the-rise-of-opinionated-models.html](https://www.dbreunig.com/2025/08/04/the-rise-of-opinionated-models.html)

生成摘要时出错

---

## 80. Nintendo patent potentially adds click wheel and crank accessories to Joy-Con

**原文标题**: Nintendo patent potentially adds click wheel and crank accessories to Joy-Con

**原文链接**: [https://www.notebookcheck.net/Nintendo-patent-potentially-adds-click-wheel-and-crank-accessories-to-the-Switch-2-Joy-Con.1083580.0.html](https://www.notebookcheck.net/Nintendo-patent-potentially-adds-click-wheel-and-crank-accessories-to-the-Switch-2-Joy-Con.1083580.0.html)

生成摘要时出错

---

## 81. I vibe coded a stock Portfolio Calculator

**原文标题**: I vibe coded a stock Portfolio Calculator

**原文链接**: [https://anotherchart.com/](https://anotherchart.com/)

生成摘要时出错

---

## 82. Json2dir: a JSON-to-directory converter, a fast alternative to home-manager

**原文标题**: Json2dir: a JSON-to-directory converter, a fast alternative to home-manager

**原文链接**: [https://github.com/alurm/json2dir](https://github.com/alurm/json2dir)

生成摘要时出错

---

## 83. Flipper Zero dark web firmware bypasses rolling code security

**原文标题**: Flipper Zero dark web firmware bypasses rolling code security

**原文链接**: [https://www.rtl-sdr.com/flipperzero-darkweb-firmware-bypasses-rolling-code-security/](https://www.rtl-sdr.com/flipperzero-darkweb-firmware-bypasses-rolling-code-security/)

生成摘要时出错

---

## 84. Voice Controlled Swarms

**原文标题**: Voice Controlled Swarms

**原文链接**: [https://jasonfantl.com/posts/Voice-Controlled-Swarms/](https://jasonfantl.com/posts/Voice-Controlled-Swarms/)

生成摘要时出错

---

## 85. Virtual 6NF

**原文标题**: Virtual 6NF

**原文链接**: [https://minimalmodeling.substack.com/p/virtual-6nf](https://minimalmodeling.substack.com/p/virtual-6nf)

生成摘要时出错

---

## 86. Cursed Knowledge

**原文标题**: Cursed Knowledge

**原文链接**: [https://immich.app/cursed-knowledge/](https://immich.app/cursed-knowledge/)

生成摘要时出错

---

## 87. Turn any website into an API

**原文标题**: Turn any website into an API

**原文链接**: [https://www.parse.bot](https://www.parse.bot)

生成摘要时出错

---

## 88. A message from Intel CEO Lip-Bu Tan to all company employees

**原文标题**: A message from Intel CEO Lip-Bu Tan to all company employees

**原文链接**: [https://newsroom.intel.com/corporate/my-commitment-to-you-and-our-company](https://newsroom.intel.com/corporate/my-commitment-to-you-and-our-company)

生成摘要时出错

---

## 89. Little-known leguminous plant can increase beef production by 60% (2022)

**原文标题**: Little-known leguminous plant can increase beef production by 60% (2022)

**原文链接**: [https://www.embrapa.br/en/busca-de-noticias/-/noticia/75361634/little-known-leguminous-plant-can-increase-beef-production-by-60](https://www.embrapa.br/en/busca-de-noticias/-/noticia/75361634/little-known-leguminous-plant-can-increase-beef-production-by-60)

生成摘要时出错

---

## 90. Historical Tech Tree

**原文标题**: Historical Tech Tree

**原文链接**: [https://www.historicaltechtree.com/](https://www.historicaltechtree.com/)

生成摘要时出错

---

## 91. Writing a storage engine for Postgres: An in-memory table access method (2023)

**原文标题**: Writing a storage engine for Postgres: An in-memory table access method (2023)

**原文链接**: [https://notes.eatonphil.com/2023-11-01-postgres-table-access-methods.html](https://notes.eatonphil.com/2023-11-01-postgres-table-access-methods.html)

生成摘要时出错

---

## 92. Leonardo Chiariglione – Co-founder of MPEG

**原文标题**: Leonardo Chiariglione – Co-founder of MPEG

**原文链接**: [https://leonardo.chiariglione.org/](https://leonardo.chiariglione.org/)

生成摘要时出错

---

## 93. Virtual Linux Devices on ARM64

**原文标题**: Virtual Linux Devices on ARM64

**原文链接**: [https://underjord.io/500-virtual-linux-devices-on-arm64.html](https://underjord.io/500-virtual-linux-devices-on-arm64.html)

生成摘要时出错

---

## 94. Someone keeps stealing, flying, fixing and returning this man's 1958 Cessna

**原文标题**: Someone keeps stealing, flying, fixing and returning this man's 1958 Cessna

**原文链接**: [https://www.latimes.com/california/story/2025-08-08/mystery-plane-thief](https://www.latimes.com/california/story/2025-08-08/mystery-plane-thief)

生成摘要时出错

---

## 95. Students from Southeast Asia in demand at universities

**原文标题**: Students from Southeast Asia in demand at universities

**原文链接**: [https://www.dw.com/en/students-from-southeast-asia-in-demand-at-universities/a-73568065](https://www.dw.com/en/students-from-southeast-asia-in-demand-at-universities/a-73568065)

生成摘要时出错

---

## 96. Doctors horrified after Google's healthcare AI makes up body part

**原文标题**: Doctors horrified after Google's healthcare AI makes up body part

**原文链接**: [https://futurism.com/neoscope/google-healthcare-ai-makes-up-body-part](https://futurism.com/neoscope/google-healthcare-ai-makes-up-body-part)

生成摘要时出错

---

## 97. Exit Tax: Leave Germany before your business gets big

**原文标题**: Exit Tax: Leave Germany before your business gets big

**原文链接**: [https://eidel.io/exit-tax-leave-germany-before-your-business-gets-big/](https://eidel.io/exit-tax-leave-germany-before-your-business-gets-big/)

生成摘要时出错

---

## 98. Emailing a one-time code is worse than passwords

**原文标题**: Emailing a one-time code is worse than passwords

**原文链接**: [https://blog.danielh.cc/blog/passwords](https://blog.danielh.cc/blog/passwords)

生成摘要时出错

---

## 99. Rules by which a great empire may be reduced to a small one (1773)

**原文标题**: Rules by which a great empire may be reduced to a small one (1773)

**原文链接**: [https://founders.archives.gov/documents/Franklin/01-20-02-0213](https://founders.archives.gov/documents/Franklin/01-20-02-0213)

生成摘要时出错

---

## 100. An LLM does not need to understand MCP

**原文标题**: An LLM does not need to understand MCP

**原文链接**: [https://hackteam.io/blog/your-llm-does-not-care-about-mcp/](https://hackteam.io/blog/your-llm-does-not-care-about-mcp/)

生成摘要时出错

---

