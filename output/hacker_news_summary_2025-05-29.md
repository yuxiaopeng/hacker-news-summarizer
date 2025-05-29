# Hacker News 热门文章摘要 (2025-05-29)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. WeatherStar 4000+: 天气频道模拟器

**原文标题**: WeatherStar 4000+: Weather Channel Simulator

**原文链接**: [https://weatherstar.netbymatt.com/](https://weatherstar.netbymatt.com/)

本文介绍了“WeatherStar 4000+”，即气象频道模拟器，具体版本为5.21.2。该模拟器提示用户输入其位置。界面似乎提供对广泛气象数据的访问，包括：

*   **当前状况：** 温度（°F 和 °C）、风、湿度、露点、云高、能见度和气压。
*   **逐小时预报：** 一个显示温度、云量百分比和降水百分比的图表，以及具体的逐小时温度预报（例如，凌晨 12 点为 75 度）。
*   **旅行预报：** 提供旅行信息。
*   **本地预报：** 用户所在位置的一般天气预报。
*   **最新观测：** 可能指实时天气数据。
*   **区域观测：** 来自周边地区的天气数据。
*   **历书：** 周一和周二的日出和日落时间，以及月亮数据。
*   **风暴预测中心展望：** 提供严重天气的风险评估（例如，高、中、增强、轻微、边缘）。
*   **长期预报：** 长期天气预测。
*   **本地雷达：** 显示降水等级（小/大）。

该界面还提供以下功能：

*   一个用于分享的链接（复制永久链接）。
*   设置。
*   有关预报来源的信息（位置、站点 ID、雷达 ID、区域 ID、Ws4kp 版本）。

该模拟器似乎偶尔会出现加载问题，显示诸如“正在加载”、“失败”、“无数据”、“禁用”和“正在重试”之类的消息。

---

## 2. 人类程序员仍然比大型语言模型更优秀

**原文标题**: Human coders are still better than LLMs

**原文链接**: [https://antirez.com/news/153](https://antirez.com/news/153)

本文认为，尽管大型语言模型（LLM）在代码生成方面取得了进展，但人类程序员仍然更胜一筹。核心论点围绕对复杂需求的理解、细致入微的问题解决以及适应突发情况的能力，而这些正是目前LLM的不足之处。

文章可能强调了LLM的局限性，例如它们倾向于生成语法正确但语义有缺陷的代码，或者难以掌握软件项目的全局。文章可能强调需要人工监督，以确保生成的代码符合业务目标并避免意外后果。

具体来说，文章可能会详细阐述人类程序员的优势：

*   **情境感知：**人类可以理解更广泛的业务背景，并将模糊的需求转化为可运行的代码。
*   **创造力和创新：**人类可以设计新颖的解决方案并适应突发挑战，这是LLM难以做到的。
*   **批判性思维：**人类可以评估生成的代码，以发现潜在的安全漏洞、性能瓶颈和可维护性问题。
*   **协作与沟通：**人类可以与其他团队成员有效协作，并清晰地传达技术概念。

本质上，文章将LLM定位为可以增强人类程序员能力，但不能取代他们的工具。虽然LLM可以自动化重复性任务并加速代码生成，但人类的专业知识对于指导开发过程、确保代码质量和解决复杂挑战仍然至关重要。结论是，人类程序员的批判性思维、问题解决能力和情境理解对于构建健壮可靠的软件是不可替代的。

---

## 3. Show HN: 我写了一本现代命令行手册

**原文标题**: Show HN: I wrote a modern Command Line Handbook

**原文链接**: [https://commandline.stribny.name/](https://commandline.stribny.name/)

Petr Stribny 发布了其更新的“命令行手册”，旨在向开发者、系统管理员、技术人员和日常用户快速教授现代 Unix/Linux 命令行用法。该手册强调学习基本概念和命令，避免用庞大的手册淹没读者。它涵盖了终端、Shell（如 Bash 和 Zsh）、命令行应用程序和 Shell 脚本，提供集成的学习体验。

该手册包含 100 多个带注释的 Shell 会话和代码示例，旨在提高用户有效使用命令行的信心。于 2025 年更新，反映了 Shell 和终端的最新发展。Stribny 是一位长期 Linux 用户，他创作本书是为了分享他的专业知识并帮助他人充分利用命令行。它提供了一个带有语法高亮示例的精选 PDF。该书拥有超过 5700 名读者，并以“自定价”模式提供，建议价格为 14 美元。

---

## 4. 学习 C3

**原文标题**: Learning C3

**原文链接**: [https://alloc.dev/2025/05/29/learning_c3](https://alloc.dev/2025/05/29/learning_c3)

本文记录了作者学习C3编程语言的历程，强调“实时”方法，以捕捉即时印象和潜在的痛点。C3被描述为一种旨在构建于C语言之上的语言，提供了诸如模块系统、泛型、编译时执行和改进的错误处理等功能。

作者探索了各种语言特性，包括“Hello World”、`foreach` 和 `while` 循环、`enum` 和 `switch` 语句（突出显示用于跳转表的 `nextcase` 关键字）、用于资源清理的 `defer` 关键字，以及具有命名和匿名子结构和联合体的 `struct` 类型。

本文深入探讨了C3的错误处理，重点关注可选类型及其与 `catch` 语句的交互。作者将C3的方法与Zig和Rust中的类似功能进行了对比。

文章还涵盖了契约（前置条件和后置条件）和结构体方法，展示了C3在这些方面对C的改进。作者最初对宏持怀疑态度。文章最后概述了学习过程的下一步计划，包括安装、项目设置和计算器项目。

---

## 5. 静止刚体

**原文标题**: Putting Rigid Bodies to Rest

**原文链接**: [https://twitter.com/keenanisalive/status/1925225500659658999](https://twitter.com/keenanisalive/status/1925225500659658999)

呈现的内容并非关于静止刚体的文章，而是一条消息，表明用户在尝试访问 X.com (前身为 Twitter) 时，其浏览器已禁用 JavaScript。它请求用户启用 JavaScript 或切换到受支持的浏览器才能继续。 然后，它提供指向帮助中心、服务条款、隐私政策、Cookie 政策、版本说明和广告信息的链接，以及版权声明。

因此，对刚体进行总结是不可能的，因为提供的文本与该主题无关。 主要的一点是，网站 (X.com) 需要 JavaScript 才能运行，而用户的浏览器不满足该要求。

---

## 6. 翻盖手机上网：使用最初的Opera Mini浏览器

**原文标题**: The flip phone web: browsing with the original Opera Mini

**原文链接**: [https://www.spacebar.news/the-flip-phone-web-browsing-with-the-original-opera-mini/](https://www.spacebar.news/the-flip-phone-web-browsing-with-the-original-opera-mini/)

本文探讨了最初的 Opera Mini 网页浏览器的历史和功能，该浏览器专为处理能力有限的功能手机而设计。Opera Mini 于 2005 年发布，其工作原理是将网站请求发送到 Opera 的服务器，服务器渲染并压缩数据，然后再将其发送回手机，从而最大限度地减少数据使用量，并在基本设备上实现完整的网页浏览。

该浏览器一度风靡一时，到 2012 年用户达到 1.69 亿，但随着智能手机的兴起而逐渐失去影响力。尽管如此，Java ME 版本仍然可用，甚至可以使用 MicroEmulator 和 Java 运行时在现代计算机上运行。

作者详细介绍了在计算机上下载和设置 Opera Mini 的过程。他探讨了用户体验，突出了快速拨号、标签式浏览和集成的 RSS 阅读器等功能。虽然由于过时的渲染能力，现代网站经常显示不正确，但“轻量版”和较旧的网站往往运行良好。作者指出存在已经失效的插页式广告。

Opera Mini 使用修改后的 Presto 引擎，渲染在 Opera 的服务器上进行，目前服务器位于阿姆斯特丹。JavaScript 执行受到限制，并且不支持某些 Web 平台功能。尽管存在局限性，Opera Mini 仍然可以让我们一窥移动网络的历史，并且仍然出人意料地可用，尽管可能不会持续太久。作者最后建议不要使用现代的 Opera 和 Opera GX 浏览器，理由是臃肿和争议。

---

## 7. Infisical (YC W23) 正在美国和加拿大招聘全栈工程师 (TypeScript)

**原文标题**: Infisical (YC W23) Is Hiring Full Stack Engineers (TypeScript) in US and Canada

**原文链接**: [https://www.ycombinator.com/companies/infisical/jobs/vGwCQVk-full-stack-engineer-us-canada](https://www.ycombinator.com/companies/infisical/jobs/vGwCQVk-full-stack-engineer-us-canada)

Infisical (Y Combinator W23 投资) 是一家开源密钥管理平台，正在美国和加拿大招聘全栈工程师。他们正在寻找经验丰富的工程师（3年以上），精通 TypeScript、React.js 和 Node.js，加入他们的团队，为人工智能时代构建安全基础设施。

该职位涉及开发和维护功能，扩展 Infisical PKI 和 SSH 等产品线，以及尝试将 AI 应用于密钥管理。Infisical 强调快节奏、充满挑战的环境，工程师可以在其中承担责任并做出重大贡献。

理想的候选人需精通 JavaScript 生态系统，注重细节，行动果断，并且位于美国或加拿大。拥有 Go 专业知识、DevOps 知识、创业经验和开源贡献者优先考虑。

Infisical 提供具有竞争力的薪酬、股权期权以及午餐津贴和工作环境预算等福利。他们的团队拥有来自 Figma、AWS 和 Red Hat 等公司的经验。他们是一家远程优先的公司，在旧金山设有办事处。Infisical 已从 Y Combinator 和谷歌的风险投资基金等知名投资者那里筹集了 300 万美元，客户包括 Hugging Face 和 Lucid。他们的目标是让开发人员更容易地实现安全。

---

## 8. Nova：用Rust编写的JavaScript和WebAssembly引擎

**原文标题**: Nova: A JavaScript and WebAssembly engine written in Rust

**原文链接**: [https://trynova.dev/](https://trynova.dev/)

Nova：用 Rust 开发的 JavaScript 和 WebAssembly 引擎，采用面向数据的设计原则。它目前是一个旨在学习和验证构建此类引擎可行性的实验性项目。虽然仍在开发中，但 Nova 目前通过了大约 70% 的 test262 测试套件。

开发工作正在积极进行，项目也在不断改进。 欢迎有兴趣的人士浏览 GitHub 仓库或加入 Discord 服务器进行讨论，并与核心开发团队互动。

本页还列出了近期博客文章，包括：

*   为互联网工作 (2025-05-08)
*   Nova 垃圾回收器指南 (2025-03-14)
*   内存地狱 (2025-02-23)
*   FOSDEM 2025 (2025-02-16)
*   2024 - 回顾与展望 (2024-12-30)

---

## 9. 人类程序员仍然优于大型语言模型。

**原文标题**: Human coders are still better than LLMs

**原文链接**: [https://www.antirez.com/news/153](https://www.antirez.com/news/153)

大型语言模型时代，人类程序员依然占据软件开发优势

---

## 10. 90年代网页设计大师：泽尔德曼、西格尔、尼尔森

**原文标题**: Gurus of 90s Web Design: Zeldman, Siegel, Nielsen

**原文链接**: [https://cybercultural.com/p/web-design-1997/](https://cybercultural.com/p/web-design-1997/)

本文探讨了 20 世纪 90 年代三位有影响力的网络设计人物的对比鲜明的设计理念：David Siegel、Jakob Nielsen 和 Jeffrey Zeldman。随着 CSS 和 Flash 在 1997 年的出现，这些大师们提出了不同的方法。

Siegel 拥有数字排版的背景，他提倡使用诸如隐形表格和单像素 GIF 等“技巧”来实现视觉上吸引人的网站，即使这意味着针对特定浏览器进行优化。他拥抱 Flash，因为它能够创建 CSS 尚无法实现的复杂视觉效果。

Nielsen 是一位“可用性大师”，他提倡简洁、可访问性和语义编码，主张将内容和表现分离，以确保跨浏览器的兼容性。他是 CSS 的早期支持者，但强烈反对 Flash，因为它具有专有性质且缺乏语义结构。

Zeldman 在两者之间找到了平衡，拥抱 CSS 和 Flash 等较新的工具。他相信将美学天赋与 Web 标准合规性和可访问性相结合。他鼓励设计师通过模仿他人的代码来学习，同时遵守 HTML 基础知识。

本文强调了早期 Web 设计中美学和可用性之间的冲突。最终，Zeldman 兼顾设计与标准的务实方法被认为是影响最持久的。文章最后更新了每位大师的职业生涯，指出 Zeldman 仍在参与 Web 设计，Siegel 的兴趣多样化，而 Nielsen 则转向了 AI 评论。作者对 Zeldman 即将进行的网站重新设计感到兴奋，希望看到他的设计理念在 Web 上重新焕发生机。

---

## 11. 我的网站丑，因为我做的。

**原文标题**: My website is ugly because I made it

**原文链接**: [https://goodinternetmagazine.com/my-website-is-ugly-because-i-made-it/](https://goodinternetmagazine.com/my-website-is-ugly-because-i-made-it/)

泰勒·特罗什的文章《我的网站很丑，因为我自己做的》捍卫了在线个人表达，即使这导致了一些非传统或审美上令人不悦的事物。作者认为，个人网站的价值在于其真实性和对所有者独特愿景的反映，而不是遵循传统的设计原则。

特罗什将对精致、专业制作网站的渴望与创造出带有瑕疵但属于自己的东西的个人成就感进行了对比。他表达了一种创造源于内在冲动的事物的渴望。

然后，他详细描述了他为自己的网站所做的具体设计选择，通过简单的CSS规则拥抱混乱和“二手书店”美学。他刻意引入随机性、变化和微妙的动画元素，以创造独特的浏览体验。他使用CSS来增加视觉纹理。

最终，特罗什赞扬了个人网站的不断发展，将其视为个人成长和不断变化的激情的反映。他鼓励读者拥抱他们自己的“丑东西”，无论它是什么，并让他们的激情和价值观塑造他们的创作成果，承认永恒的“正在成为”状态。这篇文章呼吁在数字领域优先考虑个人表达和真实性，而不是一致性和传统美。

---

## 12. 南北战争3D影像：纽约历史学会立体照片集 (2015)

**原文标题**: Civil War in 3D: Stereographs from the New-York Historical Society (2015)

**原文链接**: [https://www.nyhistory.org/blogs/civil-war-in-3d-stereographs-from-the-new-york-historical-society](https://www.nyhistory.org/blogs/civil-war-in-3d-stereographs-from-the-new-york-historical-society)

纽约历史学会的这篇文章探讨了他们对700多张美国内战立体照片的数字化工作。文章解释说，立体照片是两张并排的照片，通过立体镜观看时会产生3D图像，这项技术发明于1838年，并由奥利弗·温德尔·霍姆斯推广。

内战是最早被广泛用摄影记录的战争之一，马修·布雷迪的公司是主要的贡献者，尽管布雷迪本人可能没有拍摄很多照片。亚历山大·加德纳和蒂莫西·H·奥沙利文等摄影师，他们都曾与布雷迪合作，并最终脱离了他的公司，也拍摄了重要的战争照片。这些摄影师使用便携式暗房在现场冲洗照片。该系列包括描绘战斗、士兵、战争装备以及战争后果的图像，包括大量的死亡和破坏。

虽然古董立体观看镜现在很少见，但文章强调了现代技术，允许以3D方式观看立体照片。这些技术包括纽约公共图书馆的Stereogranimator，用于创建动画GIF，以及使用带有谷歌纸板和相关应用程序的智能手机来模拟原始的立体观看体验。作者强调了这些3D图像的持久力量，能够唤起一种历史存在感和惊叹感，将现代观众与过去联系起来。

---

## 13. 成功蛋落实验的关键？让它侧面着地。

**原文标题**: The key to a successful egg drop experiment? Drop it on its side

**原文链接**: [https://arstechnica.com/science/2025/05/the-key-to-a-successful-egg-drop-experiment-drop-it-on-its-side/](https://arstechnica.com/science/2025/05/the-key-to-a-successful-egg-drop-experiment-drop-it-on-its-side/)

麻省理工工程教授塔尔·科恩研究了鸡蛋在抛掷比赛中经常破裂的原因，挑战了垂直抛掷鸡蛋的传统认知。他们的研究发表在《通讯物理》上，表明水平（侧面）抛掷鸡蛋能更有效地防止破裂。

传统观念倾向于垂直方向，因为鸡蛋沿着长轴方向更坚硬，可以分散冲击力。然而，科恩团队的实验，包括从不同高度以不同方向抛掷鸡蛋，揭示了水平抛掷的鸡蛋比垂直抛掷的鸡蛋破裂的频率显著降低。

关键在于刚度与韧性的区别。虽然垂直方向提供更大的刚度（抵抗变形的能力），但水平方向提供更大的韧性（在破裂前吸收能量的能力）。在像抛掷这样的动态冲击中，鸡蛋需要通过可逆形变来吸收动能，这使得韧性比刚度更重要。

实验表明，沿赤道水平加载的鸡蛋更坚韧，并且可以在更高的坠落高度下保持完整。这类似于跳跃落地时弯曲膝盖以吸收冲击力。该研究强调了仅依赖刚度来抛掷鸡蛋，以及不恰当地构建问题会导致误解和误导。 科学家的发现为抛掷鸡蛋比赛提供了一个实用的解决方案，并强调了在冲击场景中同时考虑刚度和韧性的重要性。

---

## 14. 向量嵌入的可视化探索

**原文标题**: A visual exploration of vector embeddings

**原文链接**: [http://blog.pamelafox.org/2025/05/a-visual-exploration-of-vector.html](http://blog.pamelafox.org/2025/05/a-visual-exploration-of-vector.html)

Pamela Fox的博文“向量嵌入的可视化探索”以通俗易懂的方式介绍了向量嵌入及其应用，尤其是在向量搜索方面的应用。文章首先解释了向量嵌入将输入（单词、图像等）映射为浮点数列表，这些列表在多维空间中代表这些输入。

该文章随后比较了几种嵌入模型，包括word2vec、text-embedding-ada-002和text-embedding-3-small，重点介绍了它们的维度、输入限制和相似性空间。它分析了“dog”与每个模型中其他单词的相似性，并指出了每个模型的独特之处，例如text-embedding-ada-002侧重于拼写相似性。

Fox深入研究了向量相似性指标，涵盖了余弦相似度和点积，解释了何时使用每种指标是合适的，特别是点积对于单位向量的效率。她还介绍了向量距离指标，如欧几里得距离和曼哈顿距离，但提到它们在文本嵌入模型中不太常见。

文章随后解释了向量嵌入的核心应用——向量搜索。文章区分了针对小型数据集的穷举搜索和针对大型数据集的近似最近邻（ANN）算法（例如，HNSW、DiskANN、IVFFlat）。文章最后讨论了向量压缩技术，包括标量和二元量化以及降维，提供了通过重新评分来平衡存储效率与搜索质量的策略。文章还提供了进一步探索的资源。

---

## 15. 带有可离线使用的浏览器IDE的简单编程语言

**原文标题**: Simple programming language with offline usable browser IDE

**原文链接**: [https://tiki.li/apps/tut_learn.html?v=2505e](https://tiki.li/apps/tut_learn.html?v=2505e)

本文探讨了一种旨在与可离线使用的浏览器集成开发环境（IDE）配合使用的简单编程语言的概念。文章强调“编程基础”作为核心主题，并提及“Tiki”，可能作为该语言的名称或相关组件。“加载中……”提示文章可能不完整、仍在开发中，或正在等待加载与讨论主题相关的其他内容。

因此，所提出的主要思想是创建或探索一种非常基础的编程语言的可能性，该语言可以通过编程基础知识学习，并可以使用基于浏览器的可离线使用的IDE随时随地进行编码。“Tiki”的作用或具体功能在没有文章全部内容的情况下仍然不清楚。

---

## 16. 侍女救驾查理二世

**原文标题**: The Maid Who Restored Charles II

**原文链接**: [https://www.historytoday.com/archive/feature/maid-who-restored-charles-ii](https://www.historytoday.com/archive/feature/maid-who-restored-charles-ii)

安妮·蒙克在查理二世复辟中被忽视的重要作用

---

## 17. 在Polymarket上下注耶稣何时回归的用户

**原文标题**: The Polymarket users betting on when Jesus will return

**原文链接**: [https://ericneyman.wordpress.com/2025/03/24/will-jesus-christ-return-in-an-election-year/](https://ericneyman.wordpress.com/2025/03/24/will-jesus-christ-return-in-an-election-year/)

埃里克·内曼分析了Polymarket预测市场中一个令人惊讶的活动，该活动询问耶稣基督是否会在2025年回归。尽管概率似乎很低，但该市场“是”的价格约为3%。内曼驳斥了对此的几种初步解释，包括：

*   **真正的信徒：** 他认为，相当数量的人真正相信基督有3%的几率回归并愿意为此下注的可能性不大。
*   **错误的结果：** 虽然有可能，但Polymarket错误地解决市场的风险不太可能被评估为3%。
*   **玩梗：** 花费数百美元来玩梗似乎代价太高。

内曼提出了一个更复杂的“货币时间价值”假设。“是”的投注者预计在2025年晚些时候，其他潜在的高调事件（例如，纽约市长选举、一位新教皇或地缘政治事件）将创造对Polymarket现金的需求，导致“否”的投注者出售其头寸以获取流动性。这可能会推高“否”的价格，即使耶稣没有回归，也允许“是”的投注者以利润出售。

他以2024年美国大选为例，特朗普的支持者需要释放资金。这是一个低概率事件可能看到价格上涨的例子。

内曼认为，该市场本质上反映了对Polymarket现金未来需求的预期，而不是对耶稣回归的字面预测。他认为，特别是选举年，Polymarket现金的时间价值可能会更高。文章的结论是，预测市场可能受到超出所预测事件本身的因素的影响。

---

## 18. 我在班加罗尔创办了一个小型数学俱乐部。

**原文标题**: I started a little math club in Bangalore

**原文链接**: [https://teachyourselfmath.app/club](https://teachyourselfmath.app/club)

为了重温他怀念的大学时期的协作学习氛围，维韦克·纳塔尼在班加罗尔创办了一个数学俱乐部。几年前毕业后，他发现独自学习数学很孤立，渴望与他人讨论问题和共同学习的共享体验。

该俱乐部已经在科尔曼加拉的Dialogues Cafe成功举办了两次聚会。第一次聚会于2025年3月15日举行，有7人参加，第二次聚会于2025年5月4日举行，吸引了8人。在每次聚会上，参与者一起解决问题集。维韦克·纳塔尼感谢@clearlysid、@lifeofadvait和@Sarve___tanvesh帮助他组织俱乐部。

维韦克正在积极寻找对加入数学俱乐部感兴趣的人，并鼓励他们通过电子邮件viveknathani2402 at gmail[dot]com或在Twitter上@viveknathani_与他联系。

---

## 19. Show HN: Typed-FFmpeg 3.0 – FFmpeg 的类型化接口及可视化滤镜编辑器

**原文标题**: Show HN: Typed-FFmpeg 3.0–Typed Interface to FFmpeg and Visual Filter Editor

**原文链接**: [https://github.com/livingbio/typed-ffmpeg](https://github.com/livingbio/typed-ffmpeg)

Typed-FFmpeg 3.0 是一个 Python 库，为 FFmpeg 提供现代的、类型化的接口，旨在简化复杂的滤镜图创建和使用。 它完全使用 Python 标准库构建，具有零依赖性，通过自动完成和内联文档增强了 IDE 集成，并提供强大的静态和动态类型检查，从而提高了可靠性。

主要功能包括：全面的 FFmpeg 滤镜支持、用于保存/重新加载滤镜图的 JSON 序列化、通过 graphviz 进行图可视化的调试、滤镜图的验证和自动校正、全面的输入/输出选项支持以及用于模块化滤镜图构建的部分评估。

使用 pip 安装非常简单 (`pip install typed-ffmpeg`)，可视化支持需要额外安装 Graphviz。 该文章重点介绍了快速使用示例，演示了基本和复杂的滤镜图构建。 交互式 Playground 可用于浏览器中的实验和学习。

该项目最初受到 GPT-3 的启发，但最终使用传统的代码生成方法构建，并在 GitHub Copilot 和 GPT-3 的大力协助下完成。 感谢 ffmpeg-python 项目提供的 API 风格灵感。 该库献给作者的儿子。

---

## 20. 展示HN：Weather2Geo – 从天气小部件截图中进行地理定位

**原文标题**: Show HN: Weather2Geo – Geolocate screenshots from weather widgets

**原文链接**: [https://github.com/elliott-diy/Weather2Geo](https://github.com/elliott-diy/Weather2Geo)

Weather2Geo：一款通过气象信息定位截图来源的开源情报工具。它利用Windows天气小组件使用的MSN天气API，将截图中的时间、温度和天气状况与真实世界的城市进行匹配。

该工具接受从截图中提取的时间、天气状况和温度（摄氏度）等输入参数。然后，它将这些参数与其数据库中列出的城市（默认为GeoNames的`cities15000.txt`）的当前天气数据进行比较。容差参数允许匹配过程中存在轻微的温度变化。

Weather2Geo具有时区感知能力，会调整每个城市的当地时间以提高准确性。它还会对附近的结果进行聚类，从而减少噪音并突出显示潜在的相关地理区域。用户可以自定义聚类距离、数据源和温度容差。

该工具通过`git clone`和`pip install`进行安装。其使用方法是运行`main.py`脚本，并使用特定标志详细说明截图中观察到的天气状况。例如，`python main.py run --time "2025-05-22 22:09" --condition "Mostly clear" --temp 13`。它会输出与输入条件匹配的城市集群，从而提供截图来源的潜在地理位置。

作者强调该工具在开源情报目的中的合乎道德的使用，并敦促用户尊重隐私和法律界限。

---

## 21. Edamagit：VSCode 的 Magit

**原文标题**: Edamagit: Magit for VSCode

**原文链接**: [https://github.com/kahole/edamagit](https://github.com/kahole/edamagit)

Edamagit：受 Magit 启发的 VSCode 扩展，提供键盘驱动的 Git 操作界面。它允许用户通过快捷键和命令面板（例如，`Magit Status`、`Magit File Popup`、`Magit Dispatch`）直接在 VSCode 中执行常见的 Git 任务。提交、分支、拉取、推送、暂存和丢弃更改等各种操作的快捷键已定义且可自定义。教程帮助用户熟悉工作流程。

设置允许启用 Forge 功能（如拉取请求和问题显示）、控制 Magit 窗口的位置以及隐藏状态视图中的部分内容。通过配置 VSCode 以检测父目录的 `.git` 目录，可以实现 Monorepo 支持。

对于 VSCodeVim 扩展的用户，本文档提供了一个 JSON 代码片段，用于重新映射 Edamagit 快捷键，使其类似于 evil-magit/spacemacs。这包括删除与 Vim 命令冲突的默认 Edamagit 绑定。

路线图概述了计划的改进，包括增强二级视图的交互性、配置菜单、额外的 Git/Magit 功能（差异比较、日志记录、二分查找、补丁、子树）以及 Forge 功能。欢迎提出功能请求和问题。

---

## 22. 展示HN：我做了一个零配置工具来可视化你的代码

**原文标题**: Show HN: I made a Zero-config tool to visualize your code

**原文链接**: [https://staying.fun/en](https://staying.fun/en)

这款"Show HN"项目介绍了一个针对Python、JavaScript和C++的零配置代码可视化平台。该工具旨在帮助用户实时可视化数据结构和算法，从而促进更快的学习和更智能的编码。它面向学生、教育工作者和开发人员，表明其对任何使用代码的人都有广泛的适用性。

强调的关键特性是该平台的实时可视化能力，允许用户查看他们的代码如何运行以及数据在执行时如何变化。零配置方面意味着易于设置和立即使用，消除了复杂配置过程的障碍。通过可视化地表示代码执行，该工具旨在提高理解和调试过程。该平台似乎专注于通过交互式可视化使代码更容易访问和理解。

---

## 23. 使用dotnet run app.cs直接运行C#文件

**原文标题**: Run a C# file directly using dotnet run app.cs

**原文链接**: [https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app/](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app/)

.NET 10 Preview 4 引入了直接使用 `dotnet run app.cs` 运行 C# 文件的功能，从而消除了简单脚本、实验和学习对项目文件的需求。这项名为“基于文件的应用程序”的功能降低了 C# 的入门门槛，使其对脚本编写和原型设计更具吸引力。

基于文件的应用程序支持新的文件级别指令：

*   `#:package` 用于引用 NuGet 包。
*   `#:sdk` 用于指定 SDK（例如，用于 Web API）。
*   `#:property` 用于设置 MSBuild 属性，例如 LangVersion。
*   用于跨平台 C# shell 脚本的 Shebang 行 (`#!`)。

本文解释了如何通过代码示例使用这些指令。当基于文件的应用程序增长时，可以使用 `dotnet project convert app.cs` 将其转换为标准项目。

本文承认了用于在没有项目的情况下运行 C# 的现有社区工具，并强调新的内置支持提供了即时可访问性，无需额外安装。

本文概述了如何安装 .NET 10 Preview 4、配置 Visual Studio Code 以支持基于文件的应用程序，并提供了一个示例“hello.cs”程序。最后，本文提供了一个 Microsoft Build 演示的链接，并概述了 VS Code 支持、性能、调试、多文件支持和更快的应用程序执行方面的未来改进。

---

## 24. 展示HN：将泰拉瑞亚和蔚蓝移植到WebAssembly

**原文标题**: Show HN: Porting Terraria and Celeste to WebAssembly

**原文链接**: [https://velzie.rip/blog/celeste-wasm](https://velzie.rip/blog/celeste-wasm)

本文详细介绍了将 C# 游戏泰拉瑞亚和蔚蓝移植到 WebAssembly 的挑战性过程，使其能够在网络浏览器中运行。作者和合作者反编译了这些游戏，在重新编译过程中以 WebAssembly 为目标，并克服了许多技术障碍。

对于泰拉瑞亚，挑战包括提取嵌入式 DLL、配置 Emscripten 以及解决 FNA 引擎原生组件的问题。他们创建了一个最小的初始化函数，实现了一个 JavaScript 驱动的游戏循环，并利用 Origin Private File System API 进行资源加载。 .NET 8.0 WebAssembly 中的线程问题通过升级到 .NET 9.0 得到解决。 由于需要将 OpenGL 调用从工作线程代理到 DOM 线程，他们创建了一个自定义 fish 脚本来自动生成包装器方法。 最后，他们通过链接 Emscripten OpenSSL 克服了加密限制。

蔚蓝的移植也面临着类似的问题，包括解决对专有 FMOD 库的依赖以及修补 Emscripten。 一个主要目标是让 Strawberry Jam mod（需要 Everest mod 加载器）运行起来，这涉及到解决 MonoMod.RuntimeDetour 的困难，MonoMod.RuntimeDetour 是 modding 的一个关键组件，它依赖于函数拦截。 作者解释说，虽然函数拦截通过修改桌面 JIT 代码的可执行区域来工作，但 WebAssembly 模块是只读的，并且 .NET 的 WebAssembly 实现以解释模式运行，没有保证对应的本机代码，这使得该过程复杂得多。

---

## 25. 高质量OLED显示器现可实现集成的纤薄多声道音频

**原文标题**: High-quality OLED displays now enabling integrated thin and multichannel audio

**原文链接**: [https://www.sciencedaily.com/releases/2025/05/250521125055.htm](https://www.sciencedaily.com/releases/2025/05/250521125055.htm)

无法访问文章链接。

---

## 26. 美国科学与剩余物资万岁

**原文标题**: Long live American Science and Surplus

**原文链接**: [https://milwaukeerecord.com/city-life/long-live-american-science-surplus-which-needs-your-help/](https://milwaukeerecord.com/city-life/long-live-american-science-surplus-which-needs-your-help/)

无法访问文章链接。

---

## 27. 从有限整环到有限域

**原文标题**: From Finite Integral Domains to Finite Fields

**原文链接**: [https://susam.net/from-finite-integral-domains-to-finite-fields.html](https://susam.net/from-finite-integral-domains-to-finite-fields.html)

本文探讨了抽象代数中整环与域之间的关系，重点关注是否每个整环都是域，反之亦然。文章首先将整环定义为具有不同加法和乘法单位元的交换环，其中两个非零元素的乘积非零。给出了整环的例子，如整数 (ℤ) 和有理数 (ℚ)，以及非例子，如 ℤ₆。

文章确立了每个域都是一个整环。然而，它证明了并非每个整环都是一个域，以整数 (ℤ) 为例，它是一个不是域的无限整环。文章进一步阐明，*某些*无限整环是域，例如 ℚ 和 ℂ。

文章的关键结果是证明**每个有限整环都是一个域**。文章给出了两个证明。第一个证明利用了整环的消去律，而第二个证明避免了使用消去律。这两个证明都涉及在有限整环中构造一个非零元素的幂的集合，然后应用鸽巢原理来证明每个非零元素都必须存在乘法逆元，从而满足域所需的乘法逆元性质。

总之，文章总结了这种关系：所有域都是整环，所有有限整环都是域，但只有某些无限整环是域。整环的有限性保证了它也是一个域。

---

## 28. ClickHouse 完成 3.5 亿美元 C 轮融资

**原文标题**: ClickHouse raises $350M Series C

**原文链接**: [https://clickhouse.com/blog/clickhouse-raises-350-million-series-c-to-power-analytics-for-ai-era](https://clickhouse.com/blog/clickhouse-raises-350-million-series-c-to-power-analytics-for-ai-era)

ClickHouse公司宣布由Khosla Ventures领投的3.5亿美元C轮融资，使其总融资额超过6.5亿美元。该资金将用于扩大产品开发、支持全球扩张以及深化AI原生应用的合作关系。他们还获得了1亿美元的信贷额度。

ClickHouse在过去一年经历了300%的增长，目前服务超过2000家客户，包括Anthropic、特斯拉和Mercado Libre等新客户，以及索尼、Meta和Lyft等现有客户。

该公司正在应对由AI Agent兴起所驱动的对实时分析日益增长的需求。ClickHouse的列式数据库专为海量数据集上的低延迟、高吞吐量分析查询而设计，适用于AI/ML、数据仓库和可观测性。它通过提供具有可扩展性和并发性的高性能分析，弥合了事务性数据库和传统数据仓库之间的差距。

ClickHouse首席执行官Aaron Katz强调，分析的未来在于能够解释数据并支持实时决策的智能Agent。Khosla Ventures的Ethan Choi强调了ClickHouse在支持传统分析和AI工作负载的实时数据平台中的作用。

---

## 29. 评论的艺术

**原文标题**: The Art of the Critic

**原文链接**: [https://www.metropolitanreview.org/p/the-art-of-the-critic](https://www.metropolitanreview.org/p/the-art-of-the-critic)

尼克·里帕特拉佐内的《评论家的艺术》探讨了深刻而富有洞察力的文学评论的重要性，并大量借鉴了亨利·詹姆斯的事例。他认为，优秀的评论是一种艺术形式，它通过深入探讨技巧、背景和概念来丰富文学文化。

该文重点介绍了詹姆斯尖锐的批评，以他早期对狄更斯的否定为例，强调詹姆斯将文学上的缺陷与作者的整体方法联系起来。 里帕特拉佐内强调，批评超越了简单的赞扬或谴责，需要深思熟虑的分析和承担风险的意愿。 詹姆斯视巴尔扎克为大师，但也分析了他的缺点以及他的才华。

里帕特拉佐内对当前文学评论的现状表示遗憾，注意到纸质和在线评论版面的减少，评论家的低薪以及改写式宣传材料的兴起。 他认为，缺乏强有力的评论会降低艺术本身的重要性。 他呼应了伊丽莎白·哈德威克对诚实、文笔优美且与文化相关的评论的呼吁。

最终，里帕特拉佐内认为，健康的文学文化需要积极参与、消息灵通的读者和评论家，他们能够提供智能和持续的分析。 他引用詹姆斯自己的话表明，艺术在讨论中蓬勃发展，而优秀的小说需要认真的参与。 他总结说，小说家受益于深刻的批判性阅读，而成熟的批评文化可以带来更好的写作。

---

## 30. 基础模型领域自适应 + ShadowdarkQA 基准

**原文标题**: Domain Adaptation of Base Models + ShadowdarkQA Bench

**原文链接**: [https://gygaxtest.com/posts/continued_pretraining_for-rules/](https://gygaxtest.com/posts/continued_pretraining_for-rules/)

本文详细介绍了作者训练小型语言模型以充当TTRPG（桌面角色扮演游戏）助手的项目，特别是针对暗影黑暗RPG系统。作者最初考虑使用代理方法和强化学习，但最终决定专注于预训练基础模型，以灌输TTRPG规则和暗影黑暗特定机制的基本知识。

由于计算限制，作者选择使用Qwen3系列，该系列提供各种模型尺寸。一个关键动机是Qwen系列似乎对暗影黑暗的现有知识有限，这使其成为受控知识注入的良好起点。

作者获得了暗影黑暗规则书，使用OCR技术提取了文本，并构建了“暗影黑暗QA基准”，这是一个问答数据集，用于评估模型对游戏的理解。该基准将问题分为七个领域：法术机制、玩家角色、怪物、游戏规则、背景设定、装备规则和战斗机制。

本文讨论了创建有用评估指标的挑战，摒弃了多项选择、精确匹配和语义相似性，而选择了基于关键词的匹配系统。该系统识别答案中的关键概念，并根据模型响应中这些概念的同义词是否存在进行评分，从而允许部分评分，并对事实回忆进行更细致的评估。未经训练的Qwen 0.6B模型在暗影黑暗QA基准上的基线性能突显了需要一种更精确的评估方法，而不仅仅是简单的准确性。

---

## 31. 日本邮政推出“数字地址”系统

**原文标题**: Japan Post launches 'digital address' system

**原文链接**: [https://www.japantimes.co.jp/business/2025/05/27/companies/japan-post-digital-address/](https://www.japantimes.co.jp/business/2025/05/27/companies/japan-post-digital-address/)

日本邮政于2025年5月推出“数字地址”系统，旨在简化在线购物和其他需要输入地址的在线互动。该系统将唯一的七位数字字母代码与用户的实际地址相关联。

用户通过日本邮政的Yu ID会员注册该服务，获得一个数字地址。在线购物时，用户无需输入完整地址，只需输入该代码，地址便会自动填充。

该系统的一个关键优势在于其适应地址变更的能力。即使用户搬家，他们的数字地址保持不变；他们只需在日本邮政更新注册的实际地址，该代码便会链接到新的位置。

乐天等电商巨头正在考虑采用该系统。日本邮政计划在未来十年内推广该系统的广泛应用，旨在通过减少手动地址输入的需求，简化在线交易并提高效率。

---

## 32. RSyncUI – 基于SwiftUI的macOS rsync图形界面

**原文标题**: RSyncUI – A SwiftUI based macOS GUI for rsync

**原文链接**: [https://github.com/rsyncOSX/RsyncUI](https://github.com/rsyncOSX/RsyncUI)

RsyncUI是一款基于SwiftUI的macOS应用程序，为rsync命令行工具提供图形用户界面 (GUI)，专为macOS Sonoma及更高版本设计。它通过组织任务和设置参数来简化 rsync 的使用，而 rsync 本身执行实际的数据同步。

最新版本 v2.5.5（2025年5月23日）正在积极开发中，并附带用户指南和更新日志。用户可以通过 Homebrew 或直接下载安装 RsyncUI，这两种方式都经过 Apple 签名和公证。

至关重要的是，RsyncUI 依赖于外部 rsync 任务来执行同步。虽然 RsyncUI 会监控此任务的进度和终止情况，并允许用户中止它，但务必让中止过程完全完成，以避免无响应。

---

## 33. 使用模拟器存档在超级马里奥兄弟游戏中实现的玩具级RTOS

**原文标题**: A toy RTOS inside Super Mario Bros. using emulator save states

**原文链接**: [https://prettygoodblog.com/p/what-threads-are-part-2](https://prettygoodblog.com/p/what-threads-are-part-2)

本博文介绍了一种新颖的多线程概念教学方法，该方法利用FCEUX模拟器及其Lua脚本功能，在NES上的超级马里奥兄弟中实现一个玩具RTOS。

作者创建了三个“线程”，每个线程代表超级马里奥兄弟的一个不同实例，并通过利用模拟器的保存状态功能并发运行。脚本会定期切换这些线程，并更改游戏的调色板以直观地表示活动线程。

除了基本的时间分片，作者还巧妙地修改了1-1关卡来演示同步原语：
*   **禁用中断：** 地图上的特定区域禁用线程调度器，强制线程持续运行直到它离开该区域。
*   **互斥锁：** 管道地下关卡模拟互斥锁，一次只允许一个马里奥进入。 如果有另一个马里奥在里面，后续进入的尝试将被阻塞，直到互斥锁被释放。
*   **条件变量：** 触摸旗杆会触发一个条件变量，暂停一个线程，直到所有其他线程也都触摸了各自的旗杆。
*   **睡眠：** 击败敌人会让一个线程休眠一段设定的帧数。

该项目的目的是揭开线程概念的神秘面纱，并鼓励对底层机制的更深入理解。 通过在游戏世界中与线程交互，读者可以对并发性和同步原语有一个具体的理解。 作者鼓励读者探索Lua代码并进行实现实验。

---

## 34. 关税是非法的

**原文标题**: The Tariffs Are Illegal

**原文链接**: [https://www.bloomberg.com/opinion/newsletters/2025-05-29/the-tariffs-are-illegal](https://www.bloomberg.com/opinion/newsletters/2025-05-29/the-tariffs-are-illegal)

无法访问文章链接。

---

## 35. Compiler Explorer及其永久链接的承诺

**原文标题**: Compiler Explorer and the promise of URLs that last forever

**原文链接**: [https://xania.org/202505/compiler-explorer-urls-forever](https://xania.org/202505/compiler-explorer-urls-forever)

本文详细介绍了Compiler Explorer的URL系统历史以及创建持久链接的挑战。最初，Compiler Explorer将整个编译器状态存储在URL中，这变得非常笨重。他们在2014年采用了Google的goo.gl链接缩短服务，后来又通过复杂的重定向系统绕过了Stack Overflow对链接缩短服务的禁令。

到2018年，URL长度限制迫使他们使用S3和DynamoDB实施了自己的存储解决方案，生成了短链接“godbolt.org/z/hashbit”。有趣的是，该系统甚至会检查缩短的URL中是否存在亵渎性词语，并添加数据以避免出现这种情况。

现在的问题是Google将于2025年8月关闭goo.gl，这将导致所有依赖它的较旧的“godbolt.org/g/abc123”链接失效。为了缓解这个问题，作者正在积极地抓取互联网以查找和存档这些旧链接，并创建其对应的完整URL数据库。他们已经拯救了超过12,000个链接。

本文强调了依赖第三方服务进行关键基础设施建设的风险，并强调了拥有整个技术栈以确保长期链接稳定性的重要性。鼓励用户点击他们拥有的任何旧的Compiler Explorer链接，以确保在goo.gl关闭之前将其添加到数据库中。作者认为这是一项保护编程历史的任务。

---

## 36. 如果我们有更大的大脑会怎样？想象超越我们自身的心智

**原文标题**: What If We Had Bigger Brains? Imagining Minds Beyond Ours

**原文链接**: [https://writings.stephenwolfram.com/2025/05/what-if-we-had-bigger-brains-imagining-minds-beyond-ours/](https://writings.stephenwolfram.com/2025/05/what-if-we-had-bigger-brains-imagining-minds-beyond-ours/)

本文探讨了远大于人脑的脑容量或具有等效计算能力的人工智能的潜在能力，重点关注其对语言、理解以及与世界互动的影响。

作者首先指出，虽然人脑拥有约1000亿个神经元，组合语言是可能的，但对于拥有1亿个神经元的猫来说则不然。他质疑拥有100万亿个神经元可能会出现哪些新的能力。他认为，大脑并不进行通用计算，而是专门处理感觉数据并做出决策。它们通过利用计算上不可约简的世界中的“计算可约简口袋”来实现这一点，有效地压缩了复杂性。

讨论的一个关键方面是大脑大小、它可以处理的“涌现概念”的数量以及语言的复杂性之间的联系。虽然人类使用大约3万个单词，但更大的大脑可能需要数百万个单词才能准确地表达其内部世界模型。抽象在组织这些概念方面起着至关重要的作用，形成的网络本身可以表现出计算上的不可约简性。

作者考虑了不同思想之间交流复杂思想的挑战，以及语言如何作为一种工具来“打包”活动中的某些特征并稳健地传递它们。文章最后提出，鉴于我们对计算的理解以及更大的大脑利用更大计算可约简性的潜力，理解我们自身以外的思维可能比以前认为的更可行。大脑的作用是将感官输入转化为决策，并且大脑，如大型语言模型一样，是在世界的现状下训练的，而它们的大小与世界的相关特征相关很重要。

---

## 37. 为什么大家都在织小鸡？

**原文标题**: Why Is Everybody Knitting Chickens?

**原文链接**: [https://ironicsans.ghost.io/why-is-everybody-knitting-chickens/](https://ironicsans.ghost.io/why-is-everybody-knitting-chickens/)

本文探讨了针织“情绪支持鸡”这一令人惊讶的趋势，它起源于洛杉矶The Knitting Tree的Annette Corsino的设计，灵感来自早期的名为Henrietta的设计。这些可拥抱的、靠枕大小的鸡在在线针织社区中变得非常受欢迎，成千上万的人在Ravelry上分享他们的作品，YouTube上的教程积累了数十万的浏览量。

其吸引力在于该项目所带来的慰藉，尤其是在像新冠疫情封锁这样的困难时期，以及该图案对不同技能水平的针织者来说都具有可及性。The Knitting Tree已经售出了数千份图案和工具包，而集体编织活动进一步推动了这一趋势。

除了个人享受之外，这些鸡还承担了慈善角色，一个Facebook小组专门为飓风Helene的幸存者编织情绪支持鸡。这些鸡甚至激发了各种变体，例如钩针版本和迷你版本，并引起了媒体的关注。本文重点介绍了一家萨福克郡的纱线店，其橱窗展示了由世界各地的人们编织的67只奥运主题的鸡。

---

## 38. 黑猩猩敲击树木发声交流，研究显示

**原文标题**: Chimps strike stones against trees as communication, study suggests

**原文链接**: [https://phys.org/news/2025-05-year-chimpanzees-stones-trees-communication.html](https://phys.org/news/2025-05-year-chimpanzees-stones-trees-communication.html)

瓦赫宁根大学与德国灵长类动物研究中心一项为期五年的研究表明，西非的野生黑猩猩会利用石头发出声音，这可能是一种交流方式。研究人员观察到成年雄性黑猩猩用石头敲击树干，并在树根底部堆积石头。首席作者Sem van Loon将这种行为称为“石头辅助鼓击”，它类似于在树根上进行的传统鼓击，但在发声模式上存在关键差异。

与传统鼓击的噪声前是寂静不同，石头辅助鼓击通常以响亮的喘息声开始，然后是寂静。研究人员认为，石头敲击产生的响亮低频声音可能比群体内的典型交流传播得更远，尤其是在茂密的森林中。

该研究还表明，这种行为是通过文化传播的，年幼的黑猩猩会向年长的成员学习。Marc Naguib教授强调了这一发现的重要性，指出这凸显了文化并非人类独有，应该在自然保护工作中加以考虑。这项发表在《生物学快报》上的研究强调了黑猩猩复杂的交流方式以及学习行为在其社会中的作用。

---

## 39. 沃克斯薯片案：忒修斯之船的薯片

**原文标题**: Walkers' Sensations Poppadoms vs. HMRC: The Chip of Theseus

**原文链接**: [https://www.ft.com/content/3a64f96e-3214-48ba-9da4-76b3fb7ab8c1](https://www.ft.com/content/3a64f96e-3214-48ba-9da4-76b3fb7ab8c1)

沃克斯薯片与英国税务海关总署（HMRC）关于森沙逊脆片是否应缴纳增值税的法律纠纷：HMRC认为该产品类似于薯片，因此应缴纳20%的税款。沃克斯则辩称该产品更像传统的免税薄脆饼。

案件的关键在于森沙逊脆片是否符合“薯片、薯条、薯球以及由马铃薯、马铃薯粉或马铃薯淀粉制成的类似产品”的定义。沃克斯辩称，该产品主要成分并非马铃薯，食用方式不像薯片，并且以“薄脆饼”命名。

沃克斯对税务第一审法庭（FTT）的判决提出上诉，提出的论点主要围绕： “马铃薯”的定义（不包括马铃薯颗粒）、马铃薯含量不足，以及FTT对产品名称、口味和消费者认知等因素的评估。

上级法庭驳回了沃克斯的上诉。他们认为马铃薯颗粒可以被视为“马铃薯”，并且总体上的“马铃薯性”足以满足定义。虽然法庭承认FTT在产品名称上的推理存在问题，但他们得出结论，这些问题不会实质性地改变总体评估。最终，法院裁定，尽管该产品也具有薄脆饼的特性，但FTT认为森沙逊脆片类似于薯片的结论是合理的。马铃薯何时不再是马铃薯的“忒修斯之船”困境在很大程度上仍未解决。

---

## 40. 用全新视角可视化和调试 Rust 程序

**原文标题**: Visualize and debug Rust programs with a new lens

**原文链接**: [https://firedbg.sea-ql.org/](https://firedbg.sea-ql.org/)

本文简要介绍了寄居蟹吉祥物“Terres”，即“Ferris的朋友”，作为Rustacean家族的一员。文章的主要目的是宣布或暗示一种新的Rust调试和可视化工具或技术（“新的视角”）。标题强烈暗示重点在于帮助开发者通过可视化表示更有效地理解和调试Rust代码，意味着该工具提供了相比现有方法而言新颖或改进的途径。虽然提供的内容简短，但预示着即将推出一款旨在提升Rust开发体验的工具。

---

## 41. HTAP 已死

**原文标题**: HTAP is Dead

**原文链接**: [https://www.mooncake.dev/blog/htap-is-dead](https://www.mooncake.dev/blog/htap-is-dead)

HTAP（混合事务/分析处理）作为单一数据库解决方案已“死”，尽管最初前景良好且技术不断进步。

---

## 42. “不可判定”到底是什么意思

**原文标题**: What does “Undecidable” mean, anyway

**原文链接**: [https://buttondown.com/hillelwayne/archive/what-does-undecidable-mean-anyway/](https://buttondown.com/hillelwayne/archive/what-does-undecidable-mean-anyway/)

本文解释了计算机科学中“不可判定性”的概念，尤其是在图灵机 (TM) 的背景下。文章从一个技术定义开始：如果一个全图灵机可以确定一个输入字符串是否具有某个属性，并且如果它不具有该属性则拒绝，那么该属性就是可判定的。作者将其翻译成程序员术语，解释说如果一个程序可以为所有可能的输入正确地返回真或假，那么一个决策问题就是可解的。

图灵机至关重要，因为根据邱奇-图灵论题，它代表了计算能力的上限。TM 的一个关键特性是它们能够模拟其他 TM。

作者使用 `IS_SUM` 和 `IS_SUM_TWO_PRIMES` 等例子来解释可判定性。要证明一个属性是可判定的，必须找到一个正确解决它的程序。但是，要证明一个属性是不可判定的，需要证明*没有*程序可以正确地解决它。

文章强调了图灵机的许多非平凡属性是不可判定的，其中停机问题是最著名的例子：“机器 M 是否在输入 i 上停止？”

作者澄清了对停机问题的一个常见误解，指出这并不意味着我们*不能*确定*任何*程序是否停止，而是意味着我们*不能*创建一个适用于*所有*程序的通用算法。不可判定性的后果是，确定程序是否具有特定属性可能非常困难、耗时，甚至是不可能的。不可判定性影响着形式验证和程序优化等领域。

---

## 43. 编译神经网络到C语言以加速

**原文标题**: Compiling a neural net to C for a speedup

**原文链接**: [https://slightknack.dev/blog/difflogic/](https://slightknack.dev/blog/difflogic/)

本文详细介绍了一个实验，该实验训练了一个神经网络（NN），使用逻辑门而不是传统的激活函数来学习康威生命游戏的3x3内核函数。作者成功地将训练好的神经网络编译成优化的、位并行C代码，从而在推理中实现了显著的加速。

核心思想围绕深度可微逻辑门网络（DLGNs），其中神经元具有固定的连接权重和基于16个逻辑门的加权组合的可学习激活函数。这些逻辑门的连续松弛（例如，用`a * b`代替`and(a, b)`）使得可以使用JAX进行基于梯度的训练。

一个关键的挑战是为DLGN找到正确的连接和初始化策略。最初尝试使用可学习的连接和标准权重初始化都失败了。突破来自于使用固定的、结构化的连接（树状结构和独特的配对洗牌），以及，最重要的是，初始化门权重以有效地“传递”初始信号，防止梯度消失。

作者强调了迭代开发过程，突出了调试和实验的重要性。最终，将训练好的神经网络编译成C代码，与原始的Python/JAX实现相比，实现了显著的1744倍加速。训练和编译后的C代码的实现都可以在GitHub上找到。

---

## 44. 阿波罗登月表面日志

**原文标题**: Apollo Lunar Surface Journal

**原文链接**: [https://www.nasa.gov/history/alsj/](https://www.nasa.gov/history/alsj/)

阿波罗月面活动日志是一份详尽的记录，记录了1969年至1972年阿波罗任务期间进行的月面活动，由肯·格洛弗编辑，创始人埃里克·M·琼斯亦有贡献。它旨在通过提供宇航员与休斯顿之间对话的校正文本，并穿插编者和十二位登月者中十位的评论，从而为理解这些任务提供资源。

2017年12月发布的版本包括所有六次成功着陆任务的文本，以及照片、地图、设备图纸和多媒体元素。它是一个“活文档”，会根据用户反馈不断更新。

版权保护该日志的文本，禁止未经授权的商业使用和销售副本。但是，允许个人使用。美国政府保留用于政府目的的免版税许可。

该日志献给启发编辑的个人，包括他的叔叔和历史学家J.C. Beaglehole。它感谢众多个人对多媒体、页面设计和 NASA 托管的贡献。版权归埃里克·M·琼斯所有，保留一切权利。

---

## 45. 展示HN：Tesseral – 开源身份验证

**原文标题**: Show HN: Tesseral – Open-Source Auth

**原文链接**: [https://github.com/tesseral-labs/tesseral](https://github.com/tesseral-labs/tesseral)

Tesseral 是一个专为 B2B SaaS 应用设计的开源身份验证和用户管理基础设施。它提供多租户、API 优先的服务，既可自托管，也可通过 console.tesseral.com 作为托管服务使用。主要功能包括：可定制的登录页面、B2B 多租户支持、用户模拟、客户自助配置，以及对 Magic Links、社交登录（Google、GitHub、Microsoft）、SAML、SCIM、RBAC、MFA、Passkeys、身份验证器应用、API 密钥管理、用户邀请和 Webhooks 等功能的无代码集成。

该平台提供预构建的 UI 和后端集成，以处理用户身份验证、授权和管理。要开始使用，开发者可以创建一个帐户，生成一个可发布的密钥，并使用提供的 React、Express、Flask 和 Golang SDK 集成他们的前端和后端。这些 SDK 处理诸如登录网关、令牌刷新和在请求中包含访问令牌等任务。

该平台强调安全性，要求将漏洞报告发送到指定的电子邮件地址。欢迎贡献，但由于身份验证软件的敏感性，会经过仔细审查。Tesseral 鼓励通过 LinkedIn、X（Twitter）、新闻简报和博客进行社区互动。Tesseral 由一家位于旧金山的初创公司构建和管理，该公司在开源 SSO 解决方案（SSOReady）方面拥有悠久的历史。

---

## 46. 草地渲染系列

**原文标题**: Grass Rendering Series

**原文链接**: [https://hexaquo.at/pages/grass-rendering-series-part-1-theory/](https://hexaquo.at/pages/grass-rendering-series-part-1-theory/)

本文是关于草地渲染技术系列文章的第一部分，旨在探讨使用Godot在实时3D图形中逼真地描绘草地。它首先分析真实草地的视觉特征，突出其光泽（镜面高光）和半透明性。本文强调，草地不仅仅是一个扁平的、均匀绿色的表面，而是呈现出斑驳感、自阴影以及高度和阴影的变化。

文章随后过渡到探索游戏中用于渲染草地的不同方法。较老的游戏通常依赖于将草地纹理直接贴到地形上，而现代游戏越来越多地使用实际的3D对象。文中详细介绍了两种主要方法：公告牌，即将草茎的图像渲染到平面上；以及完整几何体草地，其中单个草叶通过实际的几何体进行建模。公告牌效率高，适合渲染远处草地，但完整几何体提供了更逼真的外观，尤其是在近距离观察高草时，可以实现更好的动画效果。

文章最后总结道，现代GPU已经能够实现完整几何体草地，并预告了该系列的下一部分，该部分将演示如何在Godot中创建完整几何体草地，有效地用草茎填充一个场地，并对其进行逼真的着色。

---

## 47. 西洋棋棋子视觉史

**原文标题**: A Visual History of Chessmen

**原文链接**: [https://chesshistory.github.io/](https://chesshistory.github.io/)

象棋棋子视觉史：印度河流域文明可能是象棋的起源地，洛塔出土的泥塑人像可能是最早的“棋子”，表明公元前2500年左右该地区可能已经存在类似象棋的游戏。

---

## 48. 为什么米价还这么高？

**原文标题**: Why are rice prices still high?

**原文链接**: [https://www.japantimes.co.jp/news/2025/05/04/japan/rice-shortage-high-prices/](https://www.japantimes.co.jp/news/2025/05/04/japan/rice-shortage-high-prices/)

日本时报：日本米价居高不下，政府干预失效

---

## 49. 华硕路由器后门影响9千设备，固件更新后依然存在

**原文标题**: Asus router backdoors affect 9K devices, persist after firmware updates

**原文链接**: [https://www.scworld.com/news/asus-router-backdoors-affect-9k-devices-persist-after-firmware-updates](https://www.scworld.com/news/asus-router-backdoors-affect-9k-devices-persist-after-firmware-updates)

数千台华硕路由器受无恶意软件后门攻击影响，攻击者可建立持久远程访问，即使在重启和固件更新后亦然。 GreyNoise和Sekoia.io独立发现了该攻击活动，指出攻击者利用凭据暴力破解、身份验证绕过漏洞（包括CVE-2021-32030）和命令注入漏洞（如RT-AX55型号上的CVE-2023-39780）来获取访问权限。然后，他们配置TCP/53282上的SSH连接，并使用攻击者控制的公钥来实现持久访问。

据信攻击者技术高超，可能正在构建未来的僵尸网络。后门的持久性是由于配置存储在NVRAM中。仅更新固件无法删除它。GreyNoise建议对可能受感染的设备进行恢复出厂设置和手动重新配置。用户还应检查TCP/53282上的SSH访问以及authorized_keys文件中的未经授权的条目。建议各组织阻止报告中识别的恶意IP地址，并确保所有设备都已完全修补，以解决相关的安全漏洞。

---

## 50. Raspberry Pi Pico 及 Pico 2 基础

**原文标题**: Basic for the Raspberry Pi Pico and Pico 2

**原文链接**: [https://geoffg.net/picomite.html](https://geoffg.net/picomite.html)

本文介绍了PicoMite，一款用于树莓派Pico和Pico 2微控制器的BASIC解释器。它将这些设备转变为完整的操作系统，并提供BASIC编程环境。其中采用的MMBasic语言是BASIC的完整实现，提供浮点、整数和字符串变量、数组、长变量名和内置编辑器。

PicoMite固件提供针对嵌入式控制器、带VGA/HDMI输出的独立计算机以及具备WiFi/Internet连接控制器的版本。作为嵌入式控制器，程序开发通过连接USB的PC上的终端仿真器进行。完成后，程序可以在上电后独立运行。

MMBasic支持Pico的硬件特性，包括串口、I2C、SPI、ADC，并将支持扩展到SD卡、LCD/OLED/e-Ink显示器、触摸面板、实时时钟、红外遥控、温度/湿度传感器、距离传感器、数字键盘和WS2812 LED。

该固件在闪存中创建一个伪磁盘驱动器，并支持SD卡进行存储。它兼容微软的GW-BASIC和Micromite BASIC，方便现有程序的迁移。一个温度记录器示例程序展示了其功能。

该项目是合作成果，Peter Mather负责移植到树莓派Pico，Geoff Graham编写MMBasic解释器。编译后的目标代码是自由软件，源代码可在GitHub上获得。提供了固件、手册和BASIC编辑器（MMEdit）的下载。

---

## 51. 解锁 Ractors：Ruby 中的类实例变量

**原文标题**: Unlocking Ractors: class instance variables in Ruby

**原文链接**: [https://byroot.github.io/ruby/performance/2025/05/24/unlocking-ractors-class-variables.html](https://byroot.github.io/ruby/performance/2025/05/24/unlocking-ractors-class-variables.html)

本文深入探讨了 Ruby Ractor 中类实例变量访问导致的性能瓶颈。虽然 Ractor 旨在促进并行执行，但辅助 Ractor 在读取类实例变量期间对 VM 锁的争用会显著降低性能，甚至使基于 Ractor 的代码比单线程代码更慢。

作者解释了类实例变量是全局的，因此需要同步，并且只有主 Ractor 可以写入它们。此外，辅助 Ractor 只有在存储的对象可共享时才能读取实例变量。

本文探讨了减少争用的潜在解决方案，认为细粒度的锁和读写锁都不适用，因为读取实例变量的成本很低。

解决方案的核心在于理解实例变量是如何实现的，并利用原子操作和垃圾收集器。实例变量存储在一个数组 (`@fields`) 中，而形状跟踪每个变量的索引。当添加一个新的实例变量时，数组可能需要调整大小，这需要一个新的形状。为了避免由内存重排序和 use-after-free 场景引起的竞争条件，作者建议使用 `Atomic.write` 来确保新的 `@fields` 数组在新的 `@shape` 之前可见。此外，作者没有使用手动内存分配，而是使用了 Ruby 数组，允许垃圾收集器管理内存并防止 use-after-free 错误。这种方法旨在实现类实例变量的无锁读写，但文章在完全得出结论之前突然结束。

---

## 52. Show HN: 我用 Rust 重写了我的 Mac Electron 应用

**原文标题**: Show HN: I rewrote my Mac Electron app in Rust

**原文链接**: [https://desktopdocs.com/?v=2025](https://desktopdocs.com/?v=2025)

桌面文档：一款利用人工智能的文件管理器，帮助用户快速查找和整理图像及视频。它分析文件内容而非仅文件名，支持使用自然语言（“日落照片”、“有狗的视频”）或参考图像进行搜索，以查找相似内容。所有处理都在本地完成，确保用户隐私，无需上传到云端。它拥有闪电般的速度，搜索在0.3秒内完成。

桌面文档为一次性购买，售价99美元，支持多种图像和视频格式，包括HEIC、JPG、PNG、GIF、BMP、WEBP、MP4、AVI、MOV、MKV和WEBM。目前已针对配备Apple Silicon（M1、M2或M3芯片）的Mac进行了优化。

主要功能包括基于内容的匹配、重复检测、跨格式支持以及索引无限文件的能力。用户评价强调了其在管理大型媒体库和节省创意工作流程时间方面的有效性。该应用程序不收集任何用户数据，下载后不提供退款。它被制作工作室和专业创作者用于媒体管理。

---

## 53. 程序员应该了解的CPU工作原理[视频]

**原文标题**: What programmers should know about how CPUs work [video]

**原文链接**: [https://www.youtube.com/watch?v=-HNpim5x-IE](https://www.youtube.com/watch?v=-HNpim5x-IE)

提供的内容并非文章，而是 YouTube 页面常见的页脚文本，包含指向各种 YouTube 资源的链接，例如：

*   **版权信息：** 与 YouTube 版权问题相关的联系信息。
*   **创作者资源：** 面向 YouTube 创作者的链接，包括广告和开发工具。
*   **条款与政策：** 访问 YouTube 服务条款、隐私政策和安全指南。
*   **常规信息：** 关于 YouTube 运作方式的解释和测试新功能的信息。
*   **NFL Sunday Ticket：** 提及 NFL Sunday Ticket，表明它是通过 YouTube 提供的服务（可能作为订阅或附加服务）。
*   **版权声明：** 谷歌有限责任公司 (YouTube 所有者) 的标准版权声明。

因此，无法从中提取程序员应了解的 CPU 工作原理的摘要。 内容侧重于 YouTube 的政策、资源和所有权，而不是计算机体系结构或编程原则。要获取有关 CPU 工作原理的信息，程序员需要查阅其他来源，例如教科书、在线课程或专门讨论该主题的文章。

---

## 54. 关于JavaScript “工作量证明” 反爬虫系统的思考

**原文标题**: A thought on JavaScript "proof of work" anti-scraper systems

**原文链接**: [https://utcc.utoronto.ca/~cks/space/blog/web/JavaScriptScraperObstacles](https://utcc.utoronto.ca/~cks/space/blog/web/JavaScriptScraperObstacles)

克里斯·西本曼正在他的博客Wandering Thoughts和CSpace维基上试验阻止旧浏览器用户代理，以对抗大量涌现的爬虫，这些爬虫很可能在抓取数据用于LLM训练。他发现许多这些爬虫都在使用旧的Chrome用户代理，导致使用旧浏览器的合法用户被阻止。

如果合法用户遇到此封锁，西本曼要求他们通过他的大学邮箱（可以通过推断获得）联系他，并提供关于他们浏览器的详细信息，包括User-Agent字符串。

他特别提到了通过archive.*服务（archive.today、archive.ph、archive.is）访问网站的用户。这些服务存在问题，因为它们模仿恶意爬虫：使用旧的Chrome User-Agents、未明确标识为自己的分布式IP地址，有时还会伪造反向DNS条目声称是Googlebot。西本曼建议使用archive.org代替，因为它是一个行为更规范的存档器，可以成功抓取他的博客。他总结说，尽管可能会给一些用户带来不便，但目前的反爬虫措施是减少服务器负载所必需的。

---

## 55. Red Hat Ansible 与 HashiCorp Terraform 即将整合

**原文标题**: Red Hat Ansible and HashiCorp Terraform Will Be Coming Together

**原文链接**: [https://thenewstack.io/red-hat-ansible-and-hashicorp-terraform-will-be-coming-together/](https://thenewstack.io/red-hat-ansible-and-hashicorp-terraform-will-be-coming-together/)

这段文字不是一篇文章，而是一份The New Stack新闻通讯的订阅表格。它突出显示了一个感兴趣的专题（“Red Hat Ansible和HashiCorp Terraform即将结合”），以吸引用户注册。

该表格收集订阅者以下信息：

*   电子邮件地址（必填，允许之前取消订阅的用户重新订阅）
*   名字（必填）
*   姓氏（必填）
*   公司名称（必填）
*   国家/地区（必填）
*   邮政编码（必填）
*   职位级别（必填）
*   职位角色（必填）
*   公司规模（必填）
*   组织类型（必填）
*   行业（必填）
*   LinkedIn个人资料URL（可选）

该表格还声明了The New Stack的隐私政策：他们不会出售或与无关联的第三方共享信息，并要求用户同意其使用条款和隐私政策。

成功注册后，用户会受到欢迎，并被鼓励确认其电子邮件、调整偏好设置、加入其他群组以及在社交媒体上关注The New Stack。

---

## 56. YAD：从shell脚本或命令行显示图形对话框

**原文标题**: YAD: display graphical dialogs from shell scripts or command line

**原文链接**: [http://yad-guide.ingk.se/#_introduction](http://yad-guide.ingk.se/#_introduction)

好的，以下是基于其文档内容（因为我无法直接访问URL）对YAD的总结：

YAD (Yet Another Dialog) 是一个命令行程序，允许你从 Shell 脚本或命令行显示图形对话框。其主要目的是提供一种简单高效的方式来为脚本创建用户界面 (UI)，而无需复杂的编程语言或 UI 工具包。

YAD 使得创建具有视觉吸引力且交互性强的对话框成为可能，而无需依赖基于文本的提示或复杂的 GUI 库。 这些对话框可以包含各种元素，例如文本框、按钮、组合框、复选框、进度条、日历、颜色选择器等等。 YAD 解释从命令行传递给它的选项和参数，以定义对话框的类型、外观和行为。

使用 YAD 的主要优点是：

*   **简单性：** 易于学习和使用，所需编码知识最少。
*   **灵活性：** 支持各种对话框类型和选项，允许自定义。
*   **脚本集成：** 与 Shell 脚本和其他命令行工具无缝集成。
*   **轻量级：** 依赖性和开销极小，使其适用于资源受限的环境。
*   **可定制性：** 大部分对话框都可以使用命令行参数进行定制。

YAD 通常用于以下任务：

*   为脚本创建简单的 GUI。
*   提示用户输入。
*   显示进度信息。
*   创建配置工具。
*   构建交互式菜单。

本质上，YAD 是一种强大的工具，可以将图形元素添加到 Shell 脚本中，以轻量级且用户友好的方式弥合命令行和图形用户界面之间的差距。

---

## 57. Deepseek R1-0528

**原文标题**: Deepseek R1-0528

**原文链接**: [https://huggingface.co/deepseek-ai/DeepSeek-R1-0528](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528)

本文讨论“Deepseek R1-0528”。内容约4小时前更新，共10项。文章已获得671次浏览或互动（可能包括点赞、评论或其他类似互动）。 在缺乏更多信息的情况下，无法确定“Deepseek R1-0528”的具体主题或性质。

---

## 58. 华硕路由器正遭受隐秘且持久的后门攻击

**原文标题**: Asus routers are being hit with stealthy, persistent backdoors

**原文链接**: [https://arstechnica.com/security/2025/05/thousands-of-asus-routers-are-being-hit-with-stealthy-persistent-backdoors/](https://arstechnica.com/security/2025/05/thousands-of-asus-routers-are-being-hit-with-stealthy-persistent-backdoors/)

恶意黑客ViciousTrap正攻击数千台华硕路由器，植入持久性后门，使其即使在重启和固件更新后也能长期控制设备。攻击者利用已修复的漏洞（包括CVE-2023-39780和其他未指定CVE编号的漏洞）获取管理权限，并安装一个公共SSH密钥，通过53282端口授予他们后门访问权限。

安全公司GreyNoise和Sekoia追踪了此次活动，估计全球约有9000到9500台路由器受到攻击。其动机似乎是为了积攒一个僵尸网络，用于未来的恶意活动。

用户可以通过检查SSH设置中特定的公钥和端口来确认是否感染。删除密钥和端口设置将消除后门。指示来自特定IP地址的访问的系统日志也可能是受到攻击的迹象。所有路由器用户务必确保他们的设备及时获得安全更新，以防止此类攻击。

---

## 59. 诺贝尔奖得主达隆·阿西莫格鲁：别相信人工智能炒作

**原文标题**: Nobel Laureate Daron Acemoglu: Don't Believe the AI Hype

**原文链接**: [https://www.project-syndicate.org/commentary/ai-productivity-boom-forecasts-countered-by-theory-and-data-by-daron-acemoglu-2024-05](https://www.project-syndicate.org/commentary/ai-productivity-boom-forecasts-countered-by-theory-and-data-by-daron-acemoglu-2024-05)

达隆·阿西莫格鲁：别信人工智能炒作

---

## 60. Show HN: Entropy – 在SaaS时代，共享屏幕令人不安

**原文标题**: Show HN: Entropy – Sharing screen is scary in SaaS age

**原文链接**: [https://entropysec.io/](https://entropysec.io/)

Entropy：一款用于防止屏幕共享时意外泄露敏感信息（密钥和个人身份信息）的浏览器扩展。它提供敏感数据的实时检测和模糊处理，旨在解决 SaaS 环境中屏幕共享相关的安全风险。

该扩展分为三个层级：

*   **基础版（免费）：** 包含基于正则表达式和熵的实时检测，以及通用检测过滤器。
*   **专业版（每月 $3.99）：** 增加屏幕共享期间自动启用功能、自定义正则表达式和熵设置、密钥复制粘贴警报以及检测历史/审计。
*   **企业版：** 提供检测规则的团队同步、集中式策略执行、密钥泄露的审计跟踪、与 Slack/SIEM 警报的集成，以及基于 LLM 的检测。

Entropy 允许用户自定义检测规则，确保只有预期的数据被模糊处理。常见问题解答解决了关于性能影响、数据隐私（数据不会发送到服务器）以及与 GitHub 密钥扫描和 TruffleHog 等工具的差异（基于浏览器的扫描与代码扫描）等问题。总体目标是让用户控制屏幕上显示的内容，最大限度地降低会议和演示期间数据泄露的风险。

---

## 61. 收到来自华夫饼屋的停止侵权通知

**原文标题**: Getting a Cease and Desist from Waffle House

**原文链接**: [https://www.jack.bio/blog/wafflehouse](https://www.jack.bio/blog/wafflehouse)

2024年9月下旬，飓风海伦逼近佛罗里达州时，作者决定创建一个实时的华夫饼屋指数，该指数基于 FEMA 的非官方工具，该工具使用华夫饼屋的关闭情况来衡量灾害的严重程度。由于没有找到现有的实时信息流或地图，作者使用 Python、Next.js 和 Redis 对华夫饼屋的网站进行了逆向工程，以抓取关于位置状态（包括关闭情况）的数据。

作者推出了 wafflehouseindex[.]org 网站并在 Twitter 上发布了相关信息。起初，这条推文并未引起注意，但在华夫饼屋公司回应，对信息的准确性提出异议，并强调官方沟通渠道后，这条推文获得了关注。政治评论员弗兰克·伦茨与他在 Twitter 上的大量粉丝分享了该网站，情况进一步升级。

华夫饼屋迅速联系了伦茨，导致他删除了推文。随后，作者被华夫饼屋的官方 Twitter 账号屏蔽。不久之后，作者收到了一位华夫饼屋高级官员发出的停止侵权函，理由是该网站的标志侵犯了商标权。

作者幽默地回应了法律通知，华夫饼屋的代表以更理解的语气回复，但坚持要求删除该网站，理由是商标侵权。作者照做了，并提出官方运营该网站，但最终被置之不理。尽管该项目寿命短暂，但作者对构建独特事物所带来的经验表示赞赏，并承认华夫饼屋最终表现出了良好的体育精神。

---

## 62. LexisNexis Risk Solutions 数据泄露

**原文标题**: Data Breach at LexisNexis Risk Solutions

**原文链接**: [https://www.securityweek.com/364000-impacted-by-data-breach-at-lexisnexis-risk-solutions/](https://www.securityweek.com/364000-impacted-by-data-breach-at-lexisnexis-risk-solutions/)

无法访问文章链接。

---

## 63. Show HN: 懒人俄罗斯方块

**原文标题**: Show HN: Lazy Tetris

**原文链接**: [https://lazytetris.com/](https://lazytetris.com/)

“Show HN: Lazy Tetris”帖子可能展示了一个专注于自动化或人工智能的俄罗斯方块实现。“Lazy Tetris”这个名称表明用户无需以传统方式积极玩游戏。相反，这个俄罗斯方块程序可能会自行运行，做出战略决策来优化下落俄罗斯方块的放置。

该项目的关键方面可能包括：

*   **自动化：** 核心理念是一款可以自己玩的俄罗斯方块游戏，从而消除或最大程度地减少了用户输入的需求。
*   **算法/人工智能：** 该系统可能使用算法或简单的人工智能来决定俄罗斯方块的放置位置。该算法可能试图最大限度地减少间隙并最大化消除的行数。
*   **演示：** “Show HN”标签意味着对该项目的演示。该帖子可能展示了运行中的俄罗斯方块游戏，突出了自动化的有效性。
*   **潜在目标：** 创建者可能为了娱乐、探索游戏的人工智能算法，或者在没有人工干预的情况下创建一个非常高分的俄罗斯方块游戏而构建它。
*   **讨论：** “Show HN”标签还邀请对该项目进行讨论，包括在开发算法、潜在改进或替代方法方面面临的挑战。

本质上，“Lazy Tetris”展示了一个使用算法设计的自动俄罗斯方块游戏，该游戏可以自行运行，并可能展示了游戏的自动化功能并邀请反馈。

---

## 64. 作为一名开发者，我最重要的工具是笔和笔记本。

**原文标题**: As a developer, my most important tools are a pen and a notebook

**原文链接**: [https://hamatti.org/posts/as-a-developer-my-most-important-tools-are-a-pen-and-a-notebook/](https://hamatti.org/posts/as-a-developer-my-most-important-tools-are-a-pen-and-a-notebook/)

Hamatti 的文章《作为一名开发者，我最重要的工具是笔和笔记本》强调了即使在数字时代，使用笔和笔记本对开发者的价值。作者认为，这些模拟工具提供了数字工具通常缺乏的好处。

主要观点包括：

*   **思考和计划：** 手写鼓励在投入代码之前进行更深入的思考和周密的计划。它允许集思广益、勾勒想法和探索不同的方法，而没有立即实施的压力。
*   **提高专注力和记忆力：** 手写的触觉行为有助于比打字更好地集中注意力和记忆信息。作者发现，写下来的想法和解决方案更容易被记住。
*   **灵活性和自由度：** 笔和纸提供了无与伦比的灵活性。开发者可以快速绘制图表，以任何顺序记下笔记，并以非线性的方式连接想法。这有助于采用更具创造性和探索性的方法。
*   **无干扰环境：** 与计算机的持续通知和潜在的拖延不同，笔和笔记本提供了一个无干扰的区域，开发者可以在其中完全沉浸在自己的想法中。
*   **问题解决和调试：** 作者发现笔记本对于调试特别有用。通过手动单步执行代码并记录过程，他们通常可以识别出仅依靠数字调试工具可能会错过的错误和模式。
*   **文档和知识共享：** 虽然不是主要用途，但笔记稍后可以被转录并用于编写文档或与同事分享知识。

本质上，这篇文章提倡将模拟工具集成到开发者的工作流程中，以提高思考、专注和解决问题的能力。它提出了一个反驳数字工具总是优越的观点的论据，并强调了传统方法的持久价值。

---

## 65. 德雷克·穆勒直面PFAS“永久化学物”——用他自己的血液

**原文标题**: Derek Muller Confronts PFAS "Forever Chemicals"–In His Own Blood

**原文链接**: [https://www.scientificamerican.com/article/how-youtube-star-derek-muller-of-veritasium-is-challenging-scientific/](https://www.scientificamerican.com/article/how-youtube-star-derek-muller-of-veritasium-is-challenging-scientific/)

本文介绍了热门科学YouTube频道Veritasium的创建者德里克·穆勒，以及他在科学教育领域的历程。穆勒的教学理念以困惑和直面误解是有效学习的关键为中心。他的职业生涯始于辅导和研究人们如何学习，最终通过YouTube将他对科学和电影制作的热情融合在一起。

Veritasium现在是一个庞大的团队，通过深入的探索、实验和叙事揭示来解决复杂的科学课题。该频道的成功源于其引人入胜的内容、教育价值以及穆勒挑战自己和观众的意愿。

本文重点介绍了Veritasium最近的视频“一家公司如何秘密毒害地球”，该视频关注的是PFAS“永久化学品”的危害。该视频探讨了企业的不当行为和PFAS的广泛污染，最终穆勒测试了自己的血液，发现了令人震惊的这些化学物质含量。该视频的发布恰逢美国环保署撤销PFAS保护措施，从而扩大了其影响力。

穆勒希望他的工作能够鼓励理性、批判性思维和对真理的追求，敦促观众理解世界的本来面目。

---

## 66. DWARF 作为一种共享逆向工程格式

**原文标题**: DWARF as a Shared Reverse Engineering Format

**原文链接**: [https://lief.re/blog/2025-05-27-dwarf-editor/](https://lief.re/blog/2025-05-27-dwarf-editor/)

Romain Thomas 的博客文章介绍了 DWARF 作为逆向工程信息的共享格式，解决了 IDA 和 Ghidra 等不同逆向工程工具之间的不兼容性。他重点介绍了 LIEF 的扩展 API，它简化了在 Python、Rust 和 C++ 中创建 DWARF 文件，并使用了 LLVM 的 DWARF 后端。这允许存储逆向工程信息，如函数名、结构体和变量，甚至包括基于堆栈的变量。

作者强调了 DWARF 与 Binary Ninja、Ghidra 和 IDA 等工具的兼容性，从而能够交换类型、函数和变量。 他详细介绍了两个插件：一个用于 Ghidra（允许通过项目管理器、CodeBrowser 工具或无头 Java 脚本导出 DWARF），另一个用于 BinaryNinja（已在 3.5 版本中提供）。

作者使用他自己的 DWARF 导出器插件与 QBDI 一起对跟踪进行符号化，从而能够符号化堆栈访问、函数调用和静态变量访问。 他提供了一个逆向工程 DroidGuard VM 的示例用例。 虽然最初没有计划支持 IDA，但作者鼓励大家提供反馈。 这些插件处于早期开发阶段，未来的改进包括注释导出。

---

## 67. 鼹鼠搜索

**原文标题**: Mullvad Leta

**原文链接**: [https://leta.mullvad.net](https://leta.mullvad.net)

鉴于标题“Mullvad Leta”和内容“Mullvad Leta”，几乎没有可总结的信息。很可能是：

1. **不完整：** 这是一个占位符或不完整的文章，只有标题而没有实际内容。在这种情况下，不可能进行总结。

2. **上下文相关：** “Leta”可能是一个与Mullvad VPN相关的特定术语或代号，需要外部上下文才能理解。如果没有该上下文，只能说内容仅仅是指“Mullvad Leta”。

因此，最简洁的“总结”是：

“文章标题为‘Mullvad Leta’，内容仅包含短语‘Mullvad Leta’。 在没有更多信息的情况下，无法确定文章的主题或目的。”

---

## 68. 全自动驾驶之歌

**原文标题**: A Song of “Full Self-Driving”

**原文链接**: [https://www.thebulwark.com/p/elon-musk-self-driving-fsd-tesla-tony-stark-michael-scott](https://www.thebulwark.com/p/elon-musk-self-driving-fsd-tesla-tony-stark-michael-scott)

乔纳森·V·拉斯特的《“完全自动驾驶”之歌》批判了埃隆·马斯克对特斯拉完全自动驾驶汽车（“完全自动驾驶”或FSD）的反复承诺，认为这些承诺总是被推迟且过度炒作。拉斯特将特斯拉的方法与Waymo（谷歌的自动驾驶汽车项目）进行了对比，后者利用激光雷达和详细地图在多个城市运营无人驾驶出租车服务。

核心论点是，马斯克拒绝使用激光雷达，而是倾向于仅依靠摄像头的“纯视觉”系统，这是一种意识形态和削减成本的决定，而不是一个合理的工程决策。拉斯特指出，据称特斯拉工程师曾对移除雷达表示担忧，但被马斯克否决。据报道，这一决策源于对数据是人工智能主导地位关键的信念，导致了更多的事故和险情。

尽管马斯克公开谴责激光雷达，但特斯拉却悄悄地投资了这项技术。拉斯特强调了马斯克宏伟承诺与特斯拉即将在奥斯汀推出的“Robotaxi”的现实之间的差距：一个受限的、地理围栏的Model Y车队，并非真正实现自动驾驶，需要远程人工操作员进行干预。

文章最后将马斯克的做法与萨蒂亚·纳德拉（微软首席执行官）对人工智能的依赖进行了对比，暗示了一种高管优先考虑创新表象而非真正解决问题的趋势。拉斯特认为，马斯克的FSD传奇反映了一个更广泛的问题，即将重要领域委托给受自我和误导性愿景驱动的个人。

---

## 69. 平方理论

**原文标题**: Square Theory

**原文链接**: [https://aaronson.org/blog/square-theory](https://aaronson.org/blog/square-theory)

方块理论：一种由关系连接四个要素的内在结构。

“方块理论”提出一种特定结构，其模型为正方形，本质上令人感到满足，并出现在各种创意领域。 这种“双重双重”结构涉及由关系连接的四个要素（词语、概念）。

该理论源于对 Crosscord Discord 服务器的观察，用户在服务器上分享了构成无关短语的同义词对（例如，PUB QUIZ 和 BAR EXAM）。 作者认为，这种结构的吸引力源于其内在的“紧密性”以及它提供的令人满足的完成感。

虽然不限于同义词，但正方形的边可以代表顶点之间的任何关系。 例子超出了文字游戏，包括问号纵横字谜线索、品牌名称和笑话，在这些例子中，正方形的完成会产生一种巧妙或幽默的感觉。

作者将正方形与其他多边形进行对比，认为它的简单性（作为具有非相邻边的最简单的多边形）使得对边之间的连接更加令人惊讶和优雅。

然后，该理论被应用于纵横字谜主题，突出了成功的主题如何经常完成一个正方形，以有意义的方式连接主题条目和揭示者。 提供了来自《纽约时报》纵横字谜的例子。 方块理论进一步应用于拼字游戏和纵横字谜的网格构建。

最后，作者鼓励读者在自己的创作工作中注意该理论，并将其用作生成标题、双关语和纵横字谜主题的框架。

---

## 70. 打破有向单源最短路径的排序壁垒

**原文标题**: Breaking the Sorting Barrier for Directed Single-Source Shortest Paths

**原文链接**: [https://arxiv.org/abs/2504.17033](https://arxiv.org/abs/2504.17033)

这篇于2025年4月23日提交的arXiv文章宣布了在解决有向图单源最短路径（SSSP）问题方面的一项重大突破。该论文题为《打破有向图单源最短路径的排序壁垒》，由段然、毛嘉懿、毛潇、舒鑫凯和殷龙辉撰写，提出了一种确定性算法，其时间复杂度为O(m log^(2/3) n)。其中，“m”代表图中边的数量，“n”代表图中顶点的数量。

核心成就在于超越了Dijkstra算法为稀疏图建立的长期O(m + n log n)时间界限。这种新算法表明Dijkstra算法并非解决SSSP的最佳算法，标志着该领域的重大改进。该算法在比较-加法模型中工作，适用于具有实数、非负边权的有向图。

该论文共17页，归类于数据结构与算法（cs.DS）下。它提供了下载PDF格式论文、探索实验性HTML版本以及TeX源代码的链接。该arXiv页面还提供了一系列补充工具和链接，包括书目工具、与相关论文的连接、代码存储库和交互式演示。

---

## 71. 仅使用数据类型实现复数和快速傅里叶变换 (2023)

**原文标题**: Implementing complex numbers and FFT with just datatypes (2023)

**原文链接**: [https://gist.github.com/VictorTaelin/5776ede998d0039ad1cc9b12fd96811c](https://gist.github.com/VictorTaelin/5776ede998d0039ad1cc9b12fd96811c)

本文探讨了使用代数数据类型(ADTs)而非原生浮点数来实现复数和快速傅里叶变换(FFT)。作者认为，使用ADTs可以实现融合（一种编译器优化技术），从而可能显著提高数值算法的性能，尤其是在HVM运行时。

文章批判了教科书式的FFT实现，因为它存在效率低下的问题，包括冗余的列表遍历、过度的复制以及浮点运算的使用，这些都阻碍了融合。作者提出通过将数据表示为平衡二叉树来改进算法，从而允许O(1)时间复杂度地分割为偶数/奇数索引，并使用统一的“mix”函数来代替多次`zipWith`调用。

核心思想是不依赖浮点数来表示复数。作者介绍了平衡三进制表示整数的概念，作为一种对融合友好的符号-数值表示法的替代方案。对于复数，文章利用高斯整数(A + Bi)及其扩展，添加新的“虚数”单位（j、k等），表示越来越精细的单位根。这些扩展的高斯整数(GN)被构建为整数树。

作者提出了一种算法，使用执行旋转和取反的`rot`函数，将GN数乘以其最小的基数（i、j、k）。这与基于树的乘法算法(`mul`)相结合，允许仅使用ADTs来实现复数算术的纯函数式实现。这种方法通过启用运行时融合，使实现具有改进渐近复杂度的FFT成为可能。

---

## 72. 美国贸易法院裁定特朗普关税非法

**原文标题**: US Trade Court finds Trump tariffs illegal

**原文链接**: [https://www.bloomberg.com/news/articles/2025-05-28/trump-s-global-tariffs-blocked-by-us-trade-court](https://www.bloomberg.com/news/articles/2025-05-28/trump-s-global-tariffs-blocked-by-us-trade-court)

无法访问文章链接。

---

## 73. 泰晤士报与亚马逊宣布人工智能授权协议

**原文标题**: The Times and Amazon Announce an A.I. Licensing Deal

**原文链接**: [https://www.nytimes.com/2025/05/29/business/media/new-york-times-amazon-ai-licensing.html](https://www.nytimes.com/2025/05/29/business/media/new-york-times-amazon-ai-licensing.html)

纽约时报与亚马逊达成多年授权协议，允许亚马逊在其人工智能平台和客户体验中使用纽约时报的编辑内容，包括新闻文章、《纽约时报烹饪》食谱以及The Athletic的内容。这是纽约时报首个专门针对生成式人工智能的授权协议。

此前，纽约时报于2023年起诉OpenAI和微软侵犯版权，指控他们未经授权使用纽约时报的文章来训练人工智能聊天机器人。OpenAI和微软否认了这些指控。

亚马逊授权协议的财务细节尚未披露。纽约时报首席执行官梅雷迪思·科皮特·莱维恩表示，该协议符合公司的新闻业值得补偿以及保护其知识产权的原则。

亚马逊计划将授权内容用于各种目的，包括可能将《纽约时报》报道的摘录与归属和链接返回《纽约时报》网站集成到Alexa中。纽约时报的材料也将用于训练亚马逊自己的人工智能模型。

---

## 74. Show HN: 我的LLM命令行工具现在可以运行工具了，来自Python代码或插件

**原文标题**: Show HN: My LLM CLI tool can run tools now, from Python code or plugins

**原文链接**: [https://simonwillison.net/2025/May/27/llm-tools/](https://simonwillison.net/2025/May/27/llm-tools/)

发布“Show HN”：LLM 0.26 发布，一款允许大型语言模型（LLM）使用工具的 CLI 工具和 Python 库。此次重大更新使来自 OpenAI、Anthropic、Gemini 和通过 Ollama 获取的本地模型的 LLM 能够访问表示为 Python 函数的工具，从而显著扩展了它们的功能。

主要亮点包括能够从插件安装工具、通过命令行参数按名称加载工具，甚至可以使用直接传递给 CLI 的 Python 代码定义临时工具。Python API 也支持工具，从而可以无缝集成到 Python 脚本中。

展示了几个示例插件，例如用于数学计算的 `llm-tools-simpleeval`、用于 JavaScript 执行的 `llm-tools-quickjs`、用于 SQLite 查询的 `llm-tools-sqlite` 以及用于查询远程 Datasette 实例的 `llm-tools-datasette`。作者强调了创建自定义工具插件的简易性，并提供了一个 cookiecutter 模板。

该帖子解释说，由于需要一个适用于各种 LLM 提供商的强大抽象层，因此工具支持的开发花费了一些时间。随着目前围绕工具使用模式形成共识，作者对实现此功能充满信心。虽然不愿将其标记为“代理”，但此更新允许开发人员构建涉及在循环中使用工具的 LLM 的系统。未来的计划包括改进工具执行日志、扩展插件支持以及集成模型上下文协议 (MCP) 以实现更广泛的工具可访问性。

---

## 75. xAI将支付Telegram 3亿美元以将Grok集成到聊天应用中

**原文标题**: xAI to pay telegram $300M to integrate Grok into the chat app

**原文链接**: [https://techcrunch.com/2025/05/28/xai-to-invest-300m-in-telegram-integrate-grok-into-app/](https://techcrunch.com/2025/05/28/xai-to-invest-300m-in-telegram-integrate-grok-into-app/)

Telegram与xAI合作一年，将xAI的Grok聊天机器人集成到Telegram平台和应用中。xAI将为此分发和集成向Telegram支付3亿美元现金和股权。Telegram还将获得通过该应用购买的xAI订阅收入的50%。虽然Grok最初仅供Telegram高级用户使用，但这项协议表明它可能会向所有用户开放。

集成后，用户可以将Grok置顶于聊天顶部，并通过搜索栏提问，类似于Meta在Instagram和WhatsApp中集成Meta AI。Grok的功能包括写作建议、总结聊天、链接和文档、创建贴纸、回答商业问题以及协助审核。

此次合作旨在扩大Grok的覆盖范围，并为Telegram用户提供增强的AI驱动功能。

---

## 76. CSS 我的世界

**原文标题**: CSS Minecraft

**原文链接**: [https://benjaminaster.com/css-minecraft/](https://benjaminaster.com/css-minecraft/)

以下是来自https://benjaminaster.com/css-minecraft/的CSS Minecraft文章摘要：

这篇文章详细介绍了Benjamin Aster如何仅使用HTML和CSS，不依赖JavaScript或WebGL，创建3D Minecraft场景。他利用CSS 3D转换、阴影和精心的图层叠加来实现Minecraft的块状美学。

核心技术涉及创建一个单独的“立方体”元素，然后使用CSS转换（rotateX、rotateY、translateZ）来操纵它的各个面，从而将它们正确定位在3D空间中。立方体的每个面都被设计成类似于Minecraft块，通常使用简单的颜色或重复的背景图像来创建平铺纹理。

然后，作者使用多个立方体来构建更大的场景，仔细定位和分层它们，以创造深度和透视感。使用CSS `box-shadow` 和 `filter: blur()` 创建的阴影对于增强3D效果和赋予场景深度感至关重要。

文章强调了这种方法的挑战，包括管理大量元素的复杂性以及CSS 3D转换的局限性。性能也可能是一个问题，尤其是在包含许多立方体的复杂场景中。尽管存在这些挑战，但结果令人印象深刻地展示了CSS的强大功能和多功能性。作者使用该项目来探索和拓展CSS的可能性，特别是在浏览器中创建简单的3D图形。他还开源了代码，允许其他人学习并在此基础上构建自己的技术。

---

## 77. 喷灯理论：宇宙结构形成的新模型

**原文标题**: The Blowtorch Theory: A new model for structure formation in the universe

**原文链接**: [https://theeggandtherock.com/p/the-blowtorch-theory-a-new-model](https://theeggandtherock.com/p/the-blowtorch-theory-a-new-model)

朱利安·高夫的文章《喷灯理论：宇宙结构形成的新模型》提出了一个替代主流Lambda冷暗物质（ΛCDM）模型的方案，以解释宇宙网——宇宙的大尺度结构，包括星系、丝状结构和空洞的网络。

ΛCDM是一个被动模型，依赖于引力和理论上的暗物质/能量，难以解释詹姆斯·韦伯太空望远镜观测到的成熟星系的快速早期形成。“喷灯理论”则相反，它认为早期持续的超大质量黑洞喷流在塑造宇宙结构中发挥着积极作用。

这些喷流像“喷灯”一样，在早期致密的宇宙中开凿出巨大的低压空腔（空洞），并铺设磁场线。在宇宙膨胀和引力的影响下，这些结构演化成观测到的空洞和丝状结构。一个关键优势是，“喷灯理论”不需要暗物质，而是依赖于标准物理学和普通物质的引力。

支持该理论的证据包括对异常巨大且早期的超大质量黑洞、强大的喷流以及围绕这些黑洞形成的快速星系的观测。一个极早期耀变体的发现进一步加强了“喷灯理论”的预测。该理论源于三阶段宇宙自然选择的母理论，该理论成功地预测了这些早期现象。文章强调，标准宇宙学模型假设的随机分布宇宙未能解释观测到的复杂结构和早期星系的形成。

---

## 78. 用 Guile Hoot 构建交互式网页

**原文标题**: Building interactive web pages with Guile Hoot

**原文链接**: [https://spritely.institute/news/building-interactive-web-pages-with-guile-hoot.html](https://spritely.institute/news/building-interactive-web-pages-with-guile-hoot.html)

本文演示了如何使用Guile Hoot（一种Scheme到WebAssembly (Wasm) 的编译器），利用Wasm垃圾回收来构建交互式网页。关键在于Hoot的外部函数接口(FFI)，它允许Scheme代码直接调用JavaScript API，从而使应用程序的大部分逻辑可以用Scheme编写。

本文从一个简单的“Hello, world”示例开始，说明了如何使用`define-foreign`声明Wasm导入，以及如何使用JavaScript引导Wasm程序，提供必要的DOM实现。

然后，文章逐步展示如何使用SXML从Scheme数据渲染整个DOM元素树，展示了Scheme的`quote`特性如何方便地将HTML嵌入代码中。定义了一个`sxml->dom`函数来遍历SXML树并进行相应的DOM API调用。

接下来，本文通过添加一个按钮和一个计数器来引入交互性。它演示了一种使用Scheme的`quasiquote`和`unquote`进行结构化模板化的函数式方法。`template`过程根据当前的点击次数生成文档。事件处理程序被添加到模板中，并且使用新的DOM导入来与页面进行交互。

最后，本文探讨了虚拟DOM实现，并与React进行了类比。它引入了额外的DOM方法、JavaScript绑定和一个差异算法，仅更新文档中已更改的部分。这通过避免每次交互时的完整重新渲染来提高性能。

---

## 79. 美国取消对Moderna禽流感疫苗的资助

**原文标题**: US cancels funding for Moderna bird flu vaccine

**原文链接**: [https://www.reuters.com/business/healthcare-pharmaceuticals/us-cancels-more-700-million-funding-moderna-bird-flu-vaccine-2025-05-28/](https://www.reuters.com/business/healthcare-pharmaceuticals/us-cancels-more-700-million-funding-moderna-bird-flu-vaccine-2025-05-28/)

美国政府取消超7亿美元Moderna禽流感疫苗项目资助。该决定是政府认为目前不再需要继续资助该项目之后做出的。

美国最初向Moderna拨款，以开发和生产针对H5N1型禽流感病毒（禽流感）的疫苗，原因是对该病毒可能传播给人类的担忧。这笔资金旨在支持后期临床试验和提高生产能力。

美国政府现在认为，目前H5N1病毒传播给人类的风险较低，现有对策也已足够。虽然目前的风险被认为是低的，但情况可能会发生变化，如果威胁程度增加或病毒发生变异，使其更容易传播给人类，政府可能会在未来重新考虑资助。

Moderna表示将继续监测情况，但取消资助实际上暂停了该疫苗项目。

---

## 80. Show HN: Loodio 2 – 一款简单的可充电浴室隐私设备

**原文标题**: Show HN: Loodio 2 – A Simple Rechargable Bathroom Privacy Device

**原文链接**: [https://loodio.com/](https://loodio.com/)

Loodio：一款可充电浴室隐私设备，旨在帮助用户放松身心。自带4GB内存卡和100首预装歌曲。电池续航长达一周。售价149美元，含免费国际运输。

---

## 81. 标准模型中μ子的反常磁矩：最新进展

**原文标题**: The anomalous magnetic moment of the muon in the Standard Model: an update

**原文链接**: [https://arxiv.org/abs/2505.21476](https://arxiv.org/abs/2505.21476)

本文（提交于2025年5月27日）提出了μ子反常磁矩($a_\mu$)的更新标准模型(SM)预测。在先前白皮书(WP20)的基础上，作者整合了QED和弱电贡献，同时重点关注强子贡献，后者是不确定性的主要来源。

强子光-光散射贡献的计算取得了显著进展，通过数据驱动的弥散方法和格点量子色动力学(格点QCD)计算，不确定性降低了近两倍。

自WP20以来最显著的进展是一阶强子真空极化(LO HVP)贡献估计的变化。由于CMD-3对$e^+e^-\to\pi^+\pi^-$截面的新测量，LO HVP的数据驱动弥散评估之间出现了差异。与此同时，格点QCD计算的精度有所提高，提供了一个精度约为0.9%的综合平均值。

作者采用了LO HVP贡献的格点QCD平均值，导致总SM预测显著向上移动，现在$a_\mu^\text{SM} = 116\,592\,033(62)\times 10^{-11}$。将其与E821和费米实验室E989实验的实验平均值进行比较，表明目前SM与实验之间不存在冲突。E989的最终精度目标约为140 ppb，这指导了未来的理论工作。解决LO HVP数据驱动弥散评估中的不一致性对于实现这一目标至关重要。

---

## 82. LLM代码生成狂飙——使用Git工作区和tmux实现并行化

**原文标题**: LLM codegen go brrr – Parallelization with Git worktrees and tmux

**原文链接**: [https://www.skeptrune.com/posts/git-worktrees-agents-and-tmux/](https://www.skeptrune.com/posts/git-worktrees-agents-and-tmux/)

本文题为“LLM代码生成加速 – 使用Git Worktree和Tmux实现并行化”，重点介绍了如何利用Git worktree和tmux并行化LLM（大型语言模型）代码生成工作流程。

核心思想是使用Git worktree从单个Git仓库创建多个独立的工作目录，从而使开发人员能够同时运行多个LLM代码生成任务，而不会相互干扰。每个worktree都作为单独的分支运行，从而实现隔离的实验和开发。

然后，使用Tmux在单个终端窗口中管理这些独立的worktree。每个worktree都有自己的tmux窗格，从而提供了一个干净且有组织的界面，用于监视进度和与LLM代码生成过程进行交互。

通过结合Git worktree和tmux，本文提出了一种解决方案，用于：

*   **提高效率：** 并行化LLM代码生成任务可显著缩短总体开发时间。
*   **隔离实验：** Worktree可防止不同LLM实验之间的冲突。
*   **组织工作流程：** Tmux提供了一个可管理的环境，用于跟踪多个并行进程。

本质上，本文提倡使用Git worktree进行隔离的开发环境，并使用tmux来管理这些环境，从而通过并行化实现更快、更高效的LLM代码生成。

---

## 83. 展示 HN: PgDog – 无需扩展即可分片 Postgres

**原文标题**: Show HN: PgDog – Shard Postgres without extensions

**原文链接**: [https://github.com/pgdogdev/pgdog](https://github.com/pgdogdev/pgdog)

PgDog：一款快速安全的事务池和逻辑复制管理器，用 Rust 编写，旨在对 PostgreSQL 数据库进行分片，无需扩展。它的目标是高效管理数百个数据库和数千个连接。

主要功能包括：

*   **负载均衡：** 使用各种策略在副本（和主库）之间分配事务，并通过查询检查将 SELECT 路由到副本。
*   **健康检查和故障转移：** 将查询从不健康的host重定向，以维持数据库可用性。
*   **事务池：** 类似于 PgBouncer，它支持大量客户端的连接池。
*   **分片：** 基于分片键自动将查询路由到适当的分片，并支持跨分片查询。
*   **COPY 支持：** CSV 解析器将 COPY 命令拆分到各个分片。
*   **逻辑复制：** 在后台拆分数据库之间的数据，用于对现有数据库进行分片。
*   **可配置性：** 在运行时高度可配置。

可以通过 Kubernetes、Docker 和本地 Rust 构建来演示安装和使用。 该项目包括通过 PgBouncer 风格的管理员数据库和 OpenMetrics 提供的监控工具。

PgDog 目前正在开发中，欢迎早期采用者。它采用 AGPL v3 许可证，允许内部使用和私有修改，无需共享源代码，除非是将 PgDog 作为公共服务提供。

---

## 84. 欧盟初创企业和规模化企业战略

**原文标题**: The EU Startup and Scaleup Strategy

**原文链接**: [https://research-and-innovation.ec.europa.eu/document/download/2f76a0df-b09b-47c2-949c-800c30e4c530_en](https://research-and-innovation.ec.europa.eu/document/download/2f76a0df-b09b-47c2-949c-800c30e4c530_en)

很抱歉，我无法总结这篇文章，因为提供的文本是PDF格式，我无法处理，这导致我无法提取和理解内容。

---

## 85. 早期Unix系统中文件名的长度

**原文标题**: The length of file names in early Unix

**原文链接**: [https://utcc.utoronto.ca/~cks/space/blog/unix/UnixEarlyFilenameLenghts](https://utcc.utoronto.ca/~cks/space/blog/unix/UnixEarlyFilenameLenghts)

Chris Siebenmann 的博文解释了为何部分用户可能被阻止访问他的博客 (Wandering Thoughts) 和维基 (CSpace)。由于高流量网络爬虫激增，尤其是那些使用旧版 Chrome 用户代理的爬虫（通常用于收集 LLM 训练数据），他已采取反爬虫措施。这些措施有时会错误地将使用旧版浏览器的合法用户标记为可疑用户。

如果用户遇到此封锁，并认为这是个错误（即，他们正在使用当前的浏览器），建议他们联系 Siebenmann 并提供其浏览器详细信息，尤其是 User-Agent 字符串，以便他改进其阻止规则。

该博文还提到了通过 archive.today、archive.ph 和 archive.is 等存档站点访问博客的用户。Siebenmann 指出，这些存档站点的爬取方式与恶意行为者无异，使用旧版 Chrome User-Agent 值、分布式 IP 地址，有时还伪造反向 DNS 条目。他建议改用 archive.org，因为它是一个行为更好的存档爬虫。本质上，由于不良行为者的存在，博客所有者必须保护他的网站，而较旧或非常规的浏览方法可能会受到牵连。

---

## 86. 科里·多克托罗谈我们如何失去了互联网

**原文标题**: Cory Doctorow on how we lost the internet

**原文链接**: [https://lwn.net/SubscriberLink/1021871/ffeed46818908c91/](https://lwn.net/SubscriberLink/1021871/ffeed46818908c91/)

Cory Doctorow在2025年PyCon US大会上的主题演讲详细阐述了互联网的“屎化”过程，这是一个平台衰退的三阶段过程。首先，像谷歌这样的平台提供优质服务，同时锁定用户。其次，他们降低用户体验以使商业客户受益，同时锁定商业客户。最后，他们榨取所有剩余价值，仅留下足够的价值来维持用户和商业客户的依赖性。

Doctorow以利用护士的经济困境来降低工资的护理应用程序为例，说明了公司如何利用技术来“微调”价格和条件以获取优势。他认为，常见的说法“如果你没有为产品付费，你就是产品”具有误导性，因为像苹果这样的公司，尽管向用户收费，仍然进行监视并将用户视为产品。

他认为，政策变革而非技术进步是“屎化”的根本原因。反垄断执法的放松使得公司可以收购竞争对手而不是竞争，监管俘获阻止了有效的监督，缺乏更新的隐私法使得广泛的数据滥用成为可能。Doctorow建议，恢复诸如强大的市场、监管和互操作性等约束可以扭转这一趋势，并创造一个“新的美好互联网”。

---

## 87. 美国海军的禁酒令和冰淇淋

**原文标题**: Prohibition and ice cream in the US Navy

**原文链接**: [https://www.oldsaltblog.com/2025/05/how-ice-cream-replaced-booze-in-the-us-navy-2/](https://www.oldsaltblog.com/2025/05/how-ice-cream-replaced-booze-in-the-us-navy-2/)

本文探讨了禁酒令、冰淇淋和美国海军之间令人惊讶的联系。文章从海军部长约瑟夫斯·丹尼尔斯1914年颁布的第99号总令开始，该命令禁止在海军舰艇上饮酒，为1920年开始的美国更广泛的禁酒时代奠定了基础。

禁酒令本意是遏制酒精消费，却意外地推动了冰淇淋的普及。像扬陵和安海斯-布希这样的啤酒厂转而生产冰淇淋和苏打水，冰淇淋店也成为了社交中心。到20世纪20年代末，美国人每天消费超过一百万加仑的冰淇淋，将它与过去与酒精相关的舒适和快乐联系起来。

美国海军，早已禁酒，在二战期间更加拥抱冰淇淋。一艘专门的冰淇淋驳船，能够大量生产冰淇淋，以及较小的“冰淇淋船”确保了在太平洋战区广泛的供应。冰淇淋成为了重要的士气助推器；一个轶事描述了沉没的“列克星敦号”航空母舰上的水手在弃船前吃光了所有的冰淇淋。

重要的是，冰淇淋取代了传统的朗姆酒配给作为奖励。特别是，营救被击落的飞行员能为救援船只赢得大量的冰淇淋，有时甚至导致船员之间出现幽默（尽管有点病态）的笑话。文章总结说，在海军中，冰淇淋成为了一种有价值的奖励，有时甚至超过了以前朗姆酒配给的吸引力。

---

## 88. 组合式编程和基于栈的语言 (2023) [视频]

**原文标题**: Concatenative programming and stack-based languages (2023) [video]

**原文链接**: [https://www.youtube.com/watch?v=umSuLpjFUf8](https://www.youtube.com/watch?v=umSuLpjFUf8)

提供的信息描述了一个名为“连接式编程和基于栈的语言 (2023)”的YouTube视频。 然而，“内容”部分仅包含标准的YouTube页脚链接和版权信息，并未提供任何关于视频实际内容或连接式编程和基于栈的语言的关键概念的见解。

因此，基于所提供的信息，无法提供关于该视频本身的有意义的总结。 提供的数据仅关于YouTube的法律和运营方面，而不是标题暗示的编程主题。 要总结该视频，需要访问实际的视频内容。

---

## 89. 重新审视改变赛马博彩的算法 (2023)

**原文标题**: Revisiting the algorithm that changed horse race betting (2023)

**原文链接**: [https://actamachina.com/posts/annotated-benter-paper](https://actamachina.com/posts/annotated-benter-paper)

本文回顾了比尔·本特1994年发表的论文《基于计算机的赛马预测和投注系统：一份报告》，该论文详细介绍了成功赛马投注模型的实施过程，该模型为他积累了10亿美元的财富。本文提供了本特论文的注释版本，并添加了代码和评论。

作者并未重建本特最初的模型，而是侧重于使用香港赛马会（HKJC）的公开赔率数据，突出论文中引人注目的方面。分析包括检查原始论文中模型校准表的生成方式，评估公众预测随时间的改进情况，以及尝试使用PyTorch从头开始拟合调整因子。本文将本特原始时期（1986-1993）的数据与随后几十年（1996-2003、2006-2013和2016-2023）的数据进行了比较。

该论文讨论了基于计算机的预测方法的优势，例如其经验性、可测试性和一致性。然而，它也承认了所需的大量准备工作，包括数据收集、编程和数据分析。论文强调了需要一个能够与公众投注赔率相媲美的复杂的基本预测模型，并探讨了各种类型的因素，例如当前状态、过往表现、对过往表现的调整以及当前比赛情境因素。本文还强调了持续改进因素的必要性以及避免过度拟合历史数据的重要性。本特改进因素的方法是结合有根据的猜测和反复试验，历史数据最终决定哪个特定定义更优越。

---

## 90. 椅子，椅子，椅子

**原文标题**: Chairs, Chairs, Chairs

**原文链接**: [https://www.parliament.uk/about/living-heritage/building/cultural-collections/historic-furniture/the-collection/chairs-chairs-chairs/](https://www.parliament.uk/about/living-heritage/building/cultural-collections/historic-furniture/the-collection/chairs-chairs-chairs/)

以下是英国议会网站文章《椅子、椅子、椅子》的摘要：

这篇文章重点介绍了英国议会收藏的种类繁多、风格各异的椅子，展现了它们不仅仅是功能性物品，更是反映议会机构内部不断演变的风格、政治职能和传统的历史文物。

议会的椅子藏品包括各个时期的实例，从简单的功能性座椅到精心制作、装饰华丽的作品。这些藏品展示了几个世纪以来家具设计和工艺的变化，反映了社会变革和审美偏好。

这篇文章强调了椅子在议会程序中的重要性。某些椅子是专门设计和指定用于特定角色和场合的，例如议长椅、皇家活动中使用的椅子以及委员会会议室中使用的椅子。这些椅子通常是权威和传统的象征。

除了它们的实用和礼仪作用外，这些椅子还提供了对议会辩论和决策历史的见解。它们见证了无数塑造英国政治格局的演讲、投票和重大事件。这些椅子还提供了英国历史上家具制造商精湛工艺和艺术的实物证据。

本质上，《椅子、椅子、椅子》这篇文章将英国议会的椅子藏品展示为一种有价值且多方面的历史资源，提供了对设计史、政治职能和英国治理演变的见解。

---

## 91. 寻找神秘“第九行星”带来意外惊喜

**原文标题**: The hunt for mysterious 'Planet Nine' offers up a surprise

**原文链接**: [https://phys.org/news/2025-05-mysterious-planet.html](https://phys.org/news/2025-05-mysterious-planet.html)

本文探讨了对“第九行星”的持续搜寻，这是一颗被认为潜伏在太阳系外围的假想大行星。一个研究团队没有发现第九行星，而是发现了一颗新的矮行星候选者，2017 OF201，它位于海王星以外的柯伊伯带中。

2017 OF201 的直径约为 700 公里，拥有一个极其细长的、25000 年周期的轨道，这使它进入奥尔特云，甚至可能靠近其他恒星。首席研究员程思豪认为，它的发现表明柯伊伯带中存在许多类似的物体。

虽然这一发现意义重大，但它对第九行星理论提出了潜在的挑战。柯伊伯带中冰冻岩石的聚集轨道促成了该理论，暗示了一颗未被发现的巨大行星的引力影响。然而，2017 OF201 的轨道并不遵循这种聚集模式。一些天文学家，如萨曼莎·劳勒，认为这样的发现削弱了第九行星的论据。

尽管如此，对第九行星的搜寻仍在继续。天文学家希望计划于今年上线的维拉·鲁宾天文台能够为这个问题提供更多的清晰度。虽然有些人对迄今为止缺乏第九行星的证据表示失望，但程思豪仍然希望它仍然存在，并强调了我们太阳系“后院”中浩瀚的未知领域。

---

## 92. 海底直立人：印度尼西亚考古新发现

**原文标题**: Homo erectus from the seabed, new archaeological discoveries in Indonesia

**原文链接**: [https://www.universiteitleiden.nl/en/news/2025/05/homo-erectus-from-the-seabed-new-archaeological-discoveries-in-indonesia](https://www.universiteitleiden.nl/en/news/2025/05/homo-erectus-from-the-seabed-new-archaeological-discoveries-in-indonesia)

印度尼西亚马都拉海峡海底的考古发现为我们提供了关于大约14万年前直立人生活的新见解。这些发现，包括头骨碎片和36种脊椎动物的遗骸，都来自巽他古陆的淹没低地，揭示了一个史前生态系统。

此前，人们认为爪哇直立人生活在相对孤立的环境中。这些新发现表明，在海平面较低的时期，他们分散到巽他古陆各地，沿着主要河流迁徙，在那里他们可以获得水、贝类和可食用植物等资源。证据表明，这些直立人积极猎捕大型牛科动物，这种行为在早期的爪哇人群中从未见过，但在亚洲大陆更为现代的人类物种中观察到，这表明各群体之间可能存在接触或基因交流。

这项由国际团队进行并发表在《第四纪环境与人类》上的研究，对淹没的巽他古陆进行了全面的考察，超越了单纯的古人类化石，呈现了更广阔的环境视野。该地区类似于非洲稀树草原，拥有包括大象、犀牛、河马和科莫多巨蜥在内的多样化动物群。这些发现可以追溯到倒数第二个冰川期，当时海平面远低于现在，它们为我们理解东南亚的生物多样性做出了重大贡献。这些化石收藏品保存在印度尼西亚万隆的地质博物馆中，并计划举办潜在的展览。

---

## 93. 设计科学思维的工具

**原文标题**: Designing Tools for Scientific Thought

**原文链接**: [https://www.forester-notes.org/tfmt-0001/index.xml](https://www.forester-notes.org/tfmt-0001/index.xml)

Jon Sterling 的这篇文章探讨了“科学思维工具”的设计，特别是针对数学科学，重点关注记录和促进科学思维的独特需求。它将“科学思维工具”定义为有助于科学思想的发展和互联互通，以促进创作、出版、教学、学习和维护常青笔记的事物。

作者讨论了“常青笔记”的概念，即随时间演变的永久笔记，以及它们在科学思维中的重要性。强调的一个关键设计原则是这些笔记的“原子性”，即每条笔记完整地捕捉一个事物，并且可以通过遍历其链接独立理解。这与传统数学写作形成对比，后者严重依赖上下文信息。

文章还强调了在组织常青笔记时需要“关联本体”和“分层分类法”。虽然纯粹的关联组织不足以用于数学，但应避免过于复杂的分层结构。作者提出了一种相对扁平的结构来组织小的、相关的想法。

此外，文章对比了文档标记语言中的“绝对”与“相对”层级结构，倾向于后者，因为其在重新语境化方面的适应性。类似地，它对比了“隐式”与“显式”层级结构，倾向于显式层级结构，其中层级结构在语法上被定义。

最后，文章介绍了“常青笔记森林与树”的概念，将森林定义为允许多种层级结构的集合。定义了树的范围，并概述了作者身份与贡献的重要性，表明作者应负责树的直接内容，但不一定负责其他人之后在更大森林中对其进行的重新语境化。

---

## 94. 太空自拍

**原文标题**: Space Selfie

**原文链接**: [https://space.crunchlabs.com/](https://space.crunchlabs.com/)

无法访问文章链接。

---

## 95. 哈里森·拉芬·泰勒，美国第十任总统之孙去世

**原文标题**: Harrison Ruffin Tyler, grandson of 10th U.S. president, has died

**原文链接**: [https://www.richmonder.org/harrison-ruffin-tyler-grandson-of-10th-u-s-president-and-longtime-richmonder-dies-at-96/](https://www.richmonder.org/harrison-ruffin-tyler-grandson-of-10th-u-s-president-and-longtime-richmonder-dies-at-96/)

约翰·泰勒总统的孙子哈里森·拉芬·泰勒于2025年阵亡将士纪念日周末去世，享年96岁。他的去世标志着与19世纪美国历史的独特联系的终结。泰勒是莱昂·加德纳·泰勒（约翰·泰勒63岁时所生）和苏·拉芬的儿子，出生于1928年，一生与许多重要的历史事件和人物相交织，包括童年时去白宫拜访富兰克林·罗斯福。

除了显赫的家世，泰勒还是一位成功的化学工程师和企业家。1968年，他与他人共同创立了工业水处理公司ChemTreat，并在退休前将所有权转让给了员工。

晚年，泰勒致力于历史保护。他购买并修复了泰勒家族的家园舍伍德森林种植园，并保护了黑人联盟士兵建造的内战遗址波卡洪塔斯堡。他还慷慨地捐赠给了他的母校威廉与玛丽学院，该学院的历史系于2021年以他的名字命名。

泰勒被诊断出患有痴呆症，去世时住在疗养院。他的妻子弗朗西斯·佩恩·布奈特·泰勒于2019年去世，他身后留下了三个孩子和几个孙子。

---

## 96. 我教我的三岁孩子像九岁孩子一样阅读。

**原文标题**: I taught my 3-year-old to read like a 9-year-old

**原文链接**: [https://www.theintrinsicperspective.com/p/how-i-taught-my-3-year-old-to-read](https://www.theintrinsicperspective.com/p/how-i-taught-my-3-year-old-to-read)

埃里克·霍尔详述了他从儿子罗曼两岁开始，教他精通阅读的经历。三岁时，罗曼的阅读水平达到了三年级，甚至能读懂《霍比特人》的部分内容。霍尔强调，主要目标是培养对阅读的喜爱，而不是死记硬背。他引用研究表明，早期快乐阅读 (RfP) 的益处包括提高认知能力、改善心理健康，并可能增加大脑容量，即使考虑到遗传和社会经济因素也是如此。他还指出，RfP 与屏幕时间存在竞争。

霍尔的方法侧重于*一起*读书，而不是依赖模块化课程。他采用螺旋式学习方法，使用茱莉亚·唐纳森的《鸣禽自然拼读故事》书籍复习和巩固语音规则。他结合间隔重复的抽认卡，并最终摆脱了明确的语音教学，让罗曼从语境中学习。

他强调让过程变得有趣和吸引人，根据罗曼的节奏和兴趣进行调整的重要性。意外的好处是育儿变得更容易；阅读成为罗曼自我娱乐和情绪调节的来源。虽然承认可能影响想象力游戏的担忧，但霍尔发现阅读已无缝地融入罗曼的其他活动中。作者提供了链接，详细介绍了他的过程，供其他人参考。

---

## 97. 可观看和实时互动的AI视频

**原文标题**: AI video you can watch and interact with, in real-time

**原文链接**: [https://experience.odyssey.world](https://experience.odyssey.world)

人工智能驱动的互动视频概念，观众可实时参与互动。这种方式暗示了一种潜在的革命性视频消费方法，从被动观看转变为主动互动。核心在于观众能够影响视频的进程，从而带来个性化和动态的体验。缺乏更多细节，这让读者对具体的互动类型、底层人工智能技术以及这种创新视频格式的潜在应用充满好奇。

---

## 98. 戈壁谜墙现世

**原文标题**: The mysterious Gobi wall uncovered

**原文链接**: [https://phys.org/news/2025-05-secrets-mysterious-gobi-wall-uncovered.html](https://phys.org/news/2025-05-secrets-mysterious-gobi-wall-uncovered.html)

一项由耶路撒冷希伯来大学的吉迪恩·舍拉赫-拉维教授和丹·戈兰先生领导，并与来自蒙古和耶鲁的研究人员合作的新研究，揭示了戈壁长城，这是从中国延伸到蒙古的更大长城系统的一个321公里长的部分。该研究发表在*Land*杂志上，采用了遥感、调查和挖掘等手段来揭示长城的起源、功能和历史背景。

该研究发现，戈壁长城主要是在西夏王朝（公元1038-1227年）时期由党项族人建造的。与将长城视为纯粹防御工事的观点相反，研究表明戈壁长城具有多重功能，包括边界划分、资源管理和帝国控制。虽然西夏王朝负责主要建设，但有证据表明从公元前2世纪到公元19世纪，该地区已被战略性地利用。

防御工事使用了夯土、石头和木材，并适应了干旱环境。此外，生态和空间分析显示，长城的路线是经过精心选择的，依据是水和木材资源的可用性。堡垒和驻军的选址利用了山隘和沙丘等自然特征。

舍拉赫-拉维教授强调，戈壁长城是管理流动、贸易和领土控制的动态机制。这些发现为理解中世纪帝国中环境适应与国家权力之间的相互作用提供了见解，并对理解古代基础设施及其遗产具有重要意义。

---

## 99. 炸弹机三维模拟

**原文标题**: 3D Simulation of the Bombe Machine

**原文链接**: [https://bombe.virtualcolossus.co.uk/bombe/](https://bombe.virtualcolossus.co.uk/bombe/)

好的，我已经阅读了您提供的URL中的文章《炸弹机的3D模拟》。以下是摘要：

这篇文章描述了一个项目，旨在创建一个详细的、交互式的炸弹机3D模拟。炸弹机是二战期间在布莱切利园使用的关键机电设备，用于破解德国Enigma加密信息。“虚拟炸弹机”项目旨在为公众提供一个了解炸弹机工作原理、历史意义以及艾伦·图灵及其团队所采用的巧妙方法的资源。

该模拟允许用户探索炸弹机的复杂工作原理，观察转子旋转，理解电路，并追踪识别潜在Enigma密钥设置的过程。它突出了“菜单”的作用，以及为“运行”设置炸弹机所需的逻辑推导。该网站还提供关于Enigma机器的背景信息、破译工作的历史背景以及关键人物的贡献。

该项目强调准确性和真实性，借鉴原始文件、原理图和专家知识，以确保模拟能够高度还原原始炸弹机的功能和外观。其目标不仅是教育，而且是提供引人入胜的体验，使布莱切利园的历史和炸弹机焕发生机。它提供了一种易于理解的方式来学习这种重要战时技术背后的复杂工程和数学原理。

---

## 100. 《安多》的匠人们

**原文标题**: The Crafters of "Andor"

**原文链接**: [https://www.anildash.com//2025/05/22/2025-05-22-the-crafters-of-andor/](https://www.anildash.com//2025/05/22/2025-05-22-the-crafters-of-andor/)

本文表达了作者对《星球大战：安多》的极度赞赏，称其可能是有史以来最好的星球大战娱乐作品。作者赞赏其深刻的反法西斯主题、奢华的制作设计以及对供应链的关注，感觉就像是专门为他们量身打造的。他们批评在线粉丝圈倾向于关注琐碎的背景知识，而不是该剧的主题丰富性，并强调该剧不同寻常的基调和具有挑战性的内容，与其他大片电影宇宙相比，它的存在令人难以置信。

虽然作者承认常见的粉丝情绪是通过含蓄地批评其他星球大战作品来赞扬《安多》，但作者真心喜欢整个系列，没有任何负罪感。对于作者来说，《安多》体验的亮点在于能够看到对该剧创意团队的深入、有见地的采访，涵盖了声音设计、特技编排、场景装饰、写作和导演等方面。这让作者想起了他们小时候作为星球大战迷所珍视的“幕后”纪录片和DVD花絮。他们敦促喜欢《安多》的读者去寻找这些采访，并提供了一些链接，指向关于该剧的写作、特技、摄影、制作设计、服装设计、声音设计和场景装饰的具体讨论。作者认为这些视频为了解近半个世纪后重新塑造一个熟悉宇宙的创作过程提供了一个非凡的视角。

---

