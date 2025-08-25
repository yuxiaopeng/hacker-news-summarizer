# Hacker News 热门文章摘要 (2025-08-25)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 打造罗技不会做的鼠标

**原文标题**: Building the mouse Logitech won't make

**原文链接**: [https://samwilkinson.io/posts/2025-08-24-mx-ergo-mods](https://samwilkinson.io/posts/2025-08-24-mx-ergo-mods)

无法访问文章链接。

---

## 2. Show HN: Base，macOS 平台的 SQLite 数据库编辑器

**原文标题**: Show HN: Base, an SQLite database editor for macOS

**原文链接**: [https://menial.co.uk/base/](https://menial.co.uk/base/)

这款Show HN帖子介绍了一款名为"Base"的macOS应用，它是一款SQLite数据库编辑器。它的定位是易于使用，适合初学者和有经验的用户。描述强调其体积小、功能强大且用户体验舒适。帖子重点介绍了其关键功能——在macOS上编辑SQLite数据库。它通过免费下载选项（暗示试用版或免费增值模式）和付费版本，直接鼓励用户参与。

---

## 3. 迷你电脑革命

**原文标题**: The MiniPC Revolution

**原文链接**: [https://jadarma.github.io/blog/posts/2025/08/the-minipc-revolution/](https://jadarma.github.io/blog/posts/2025/08/the-minipc-revolution/)

本文倡导将迷你电脑作为一种可行且有利的计算解决方案，尤其适用于家庭实验室和一般家庭使用。作者认为迷你电脑具有诸多优点，包括价格实惠、易于更换、体积小巧、节能以及通过多样化实现专业化。

迷你电脑在特定角色中表现出色，例如通用计算、网络（防火墙、路由器、VPN）、网络存储（NAS）和个人云托管，从而实现了一种分布式计算方法。这与传统的“巨石”方法形成对比，后者通常需要复杂的硬件配置，并且管理起来可能具有挑战性。

作者强调，使用迷你电脑消除了对虚拟化的需求，简化了系统管理并隔离了功能。这种模块化还降低了单点故障的风险，确保如果一台迷你电脑发生故障，其他基本服务仍然可以运行。

最后，作者强调了使用迷你电脑的心理益处，指出它们的隔离性培养了一种在尝试不同配置时的信心和自由感。作者总结说，由于其可扩展性和经济实惠的成本，迷你电脑是进入家庭实验室世界的绝佳切入点，为更复杂的、基于服务器的设置提供了一种实用且令人愉悦的替代方案。

---

## 4. 一个小改动，提升键盘导航浏览体验

**原文标题**: A Small Change to Improve Browsers for Keyboard Navigation

**原文链接**: [https://b.43z.one/2025-07-22/](https://b.43z.one/2025-07-22/)

h43z的文章讨论了Firefox和Chrome等现代浏览器中键盘导航的局限性。虽然浏览器提供了“快速查找”功能（使用`'`查找链接，`/`和`Ctrl+F`查找所有文本），但这些工具仅突出显示元素，不会在用户按Enter键时激活它们，尤其对于非链接元素，例如带有`onclick`处理程序的按钮或div。

H43z认为，如果按下Enter键时能够触发对突出显示文本对应元素的点击，将显著改善键盘导航。为此，他们创建了一个小型浏览器扩展程序，注入JavaScript代码来拦截Enter键的按下。该代码识别包含突出显示文本的元素，模拟对该元素的点击，然后移除突出显示。

提供的代码片段获取所选节点的父HTML元素，然后在按下Enter键时点击它。作者指出，还需要排除更多`Enter`键挂钩的情况。

作者认为这个小小的改变极大地提升了键盘导航体验，使用户能够更高效地与网站元素交互。文章最后呼吁Firefox提高能源效率。

---

## 5. 什么是OKLCH颜色？

**原文标题**: What are OKLCH colors?

**原文链接**: [https://jakub.kr/components/oklch-colors](https://jakub.kr/components/oklch-colors)

OKLCH 是一种旨在实现感知均匀性的颜色模型，使其能够更轻松地以符合人类感知的方式来操作颜色。与 RGB 或 HSL 等模型不同，OKLCH 值中相等的步长会导致感知到的亮度、色度和色相发生相等的变化。

OKLCH 与 LCH 类似，由明度（0-1 或 0%-100%）、色度（强度）和色相（0-360 度）组成，但它以 OKLab 色彩空间为基础。一个显著的优势是能够通过保持明度和色度恒定，同时改变色相来创建一致的调色板，从而产生视觉上均匀的颜色。类似地，改变明度值会产生可预测的色调，而不会出现色相或饱和度漂移。

OKLCH 中的渐变不同于 sRGB，因为它们是基于明度、色度和色相计算的，这可能会导致更平滑的过渡，但也可能导致意想不到的颜色偏差。对于更线性的渐变，通常首选 OKLAB。

OKLCH 支持比 sRGB 更广泛的颜色范围，包括 Display-P3 屏幕上可以实现的颜色。它甚至可以定义超出任何显示器色域的颜色，这些颜色随后会被裁剪或映射到最接近的可表示颜色。使用最大色度值可以帮助避免这种裁剪。

虽然 OKLCH 具有良好的浏览器支持，但建议使用 CSS 中的 `@supports` 为旧版浏览器提供 sRGB 回退。诸如 oklch.fyi 之类的工具可用于帮助生成和转换 OKLCH 调色板。

---

## 6. FCC禁止超过1200家供应商违反防骚扰电话规定

**原文标题**: FCC Bars over 1,200 Providers for Non-Compliance with Robocall Protections

**原文链接**: [https://docs.fcc.gov/public/attachments/DOC-414073A1.txt](https://docs.fcc.gov/public/attachments/DOC-414073A1.txt)

由于未能遵守机器人电话防护规定，美国联邦通信委员会(FCC)已禁止1200多家语音服务提供商接入美国电话网络。这些提供商未能维护准确的机器人电话缓解数据库认证，忽视了其保护消费者免受非法机器人电话侵害的责任。在此之前，8月份曾发出最后警告，并在最初从数据库中删除了185家提供商。

FCC的机器人电话缓解数据库要求提供商在其网络上实施STIR/SHAKEN来电显示认证，并提交机器人电话缓解计划。未能遵守规定将导致从数据库中移除并阻止流量。被移除的提供商只有获得FCC的明确批准才能重新加入。

此举源于2024年12月的一项命令，该命令指示委员会要求2411家提供商纠正有缺陷的备案，否则将面临移除。在此次行动之前，已有185家提供商因参与机器人电话追踪而被移除。此外，由两党组成的51个州的总检察长联盟发起了“机器人电话围剿行动”，向37家语音提供商（包括已被FCC移除的7家）发出了警告信，要求他们阻止非法机器人电话使用其网络。FCC将继续优先打击机器人电话，并追究提供商履行义务的责任。

---

## 7. 如何欲缓反速

**原文标题**: How to Make Things Slower So They Go Faster

**原文链接**: [https://www.gojiberries.io/how-to-make-things-slower-so-they-go-faster-a-jitter-design-manual/](https://www.gojiberries.io/how-to-make-things-slower-so-they-go-faster-a-jitter-design-manual/)

本文探讨了同步需求问题，即大量客户端请求淹没服务，导致级联故障。文章解释了对齐事件（缓存过期、定时任务、部署）如何产生超出系统容量的请求峰值，从而导致队列、超时和重试，进而加剧问题。

核心解决方案是使用抖动来随时间分散请求，有效地减缓速度以提高整体性能和稳定性。文章强调，目标是最小化过载风险和增加的延迟。最佳方法是均匀抖动，它提供了公平性，并最大限度地降低了与瞬时负载增加相关的成本。

确定合适的抖动窗口大小（W）涉及平衡约束：基于余量（H）、服务时间（s）和备用并发（K）的下限，以及基于截止日期（D）和可接受等待时间（L）的上限。文章还讨论了如何结合服务器提供的提示（Retry-After、速率限制）来优化抖动窗口。

该原则适用于预防和从同步需求中恢复。预防包括随机化 TTL 并错开周期性任务。恢复包括使用基于估计余量补充令牌桶的服务器端速率控制来控制准入，确保仅在容量可用时才接受请求。

作者强调了监控关键指标（峰均比、尾延迟、重试率）和进行恢复演练以验证假设的重要性，并识别常见的错误，例如低估需求或高估容量。最终，本文提倡采用一种可控的方法来管理同步需求，使用抖动将峰值转化为可管理的流量，从而提高性能和用户体验。

---

## 8. OAuth图解指南

**原文标题**: An Illustrated Guide to OAuth

**原文链接**: [https://www.ducktyped.org/p/an-illustrated-guide-to-oauth](https://www.ducktyped.org/p/an-illustrated-guide-to-oauth)

本文图文并茂地介绍了OAuth，该协议旨在授予第三方应用程序对用户在另一项服务上的数据的有限访问权限，而无需共享其密码。

OAuth 的核心围绕**访问令牌**展开，它充当用户特定的 API 密钥。 该过程始于用户与应用程序（OAuth 客户端）交互，然后将用户重定向到他们想要连接的服务（授权服务器）。 用户登录并向应用程序授予特定权限（范围）。

在用户同意后，授权服务器会将用户重定向回带有**授权码**的应用程序。 然后，应用程序通过安全的后端（后通道）请求，使用此代码及其**客户端密钥**来交换访问令牌。 这种使用授权码而不是直接提供访问令牌的两步过程对于安全性至关重要。

本文涵盖了 OAuth 应用程序的注册过程，强调了重定向 URI 对于安全性的重要性。 它还解决了安全问题，突出了在前端暴露客户端密钥的危险，并介绍了 PKCE 作为没有后端的应用程序的解决方案。

作者指出，OAuth 可以通过多种方式实现，包括“隐式流”（安全性较低）和使用 PKCE 的实现，并解释说令牌会过期并需要刷新流程。 最后，本文还涉及 OpenID Connect (OIDC)，它建立在 OAuth 之上以实现登录功能并提供用户数据。

---

## 9. Agent-C：4KB AI智能体

**原文标题**: Agent-C: a 4KB AI agent

**原文链接**: [https://github.com/bravenewxyz/agent-c](https://github.com/bravenewxyz/agent-c)

Agent-C 是一个用 C 编写的非常轻量级的 AI 代理，旨在在 macOS 和 Linux 上高效运行。它的主要功能是与 OpenRouter API 交互，并根据 AI 响应执行 shell 命令，从而有效地提供工具调用功能。

一个关键亮点是其极小的二进制文件大小，这是通过特定于平台的压缩技术实现的。在 macOS 上，它利用 GZEXE，生成一个 4.4KB 的可执行文件，而在 Linux 上，UPX 压缩允许二进制文件大小约为 16KB。

该代理通过滑动窗口集成会话记忆管理，优化其资源使用，并使其能够在交互中保持上下文。

要开始使用，用户需要一个 GCC 编译器、curl 命令行工具和一个 OpenRouter API 密钥。使用 `make` 命令可以轻松构建代理，该命令会自动检测操作系统并应用适当的压缩方法。在设置 `OR_KEY` 环境变量为 API 密钥后，可以使用 `./agent-c` 执行代理。

该项目在 CC0 "No Rights Reserved" 许可下获得许可，强调其开放和不受限制的性质。

---

## 10. 什么是色彩空间？

**原文标题**: What Is a Color Space?

**原文链接**: [https://www.makingsoftware.com/chapters/color-spaces-models-and-gamuts](https://www.makingsoftware.com/chapters/color-spaces-models-and-gamuts)

由于文章内容为“加载中…”，因此无法提供有意义的摘要。摘要需要内容才能进行总结。

要提供摘要，我需要文章“什么是色彩空间？”的实际文本。一旦您提供了它，我就可以对其进行分析并为您提供一份简洁的摘要，不超过300字。

---

## 11. 大O符号的可视化入门

**原文标题**: A visual introduction to big O notation

**原文链接**: [https://samwho.dev/big-o/](https://samwho.dev/big-o/)

本文以可视化的方式介绍了大O符号，这是一种描述函数性能的方法，它基于执行时间如何随输入规模的增长而变化，而不是实际的时间测量。

作者涵盖了四种常见的大O类别：

*   **O(1) - 常数时间：** 执行时间与输入规模无关，保持不变（例如，直接使用公式）。

*   **O(log n) - 对数时间：** 执行时间与输入规模的对数成比例增长（例如，二分查找）。

*   **O(n) - 线性时间：** 执行时间与输入规模线性增长（例如，单次遍历列表）。

*   **O(n^2) - 平方时间：** 执行时间与输入规模的平方成比例增长（例如，冒泡排序等嵌套循环）。

文章用代码示例和交互式可视化工具阐述了每个概念。它强调大O符号描述的是*最坏情况*，并且关注的是*增长率*，而不是绝对时间。作者还提到了当最佳和最坏情况具有相同增长阶数时，可以使用Θ符号。

此外，文章还提供了通过以下方式提高代码性能的实际示例：

*   使用合适的数据结构（例如，使用集合进行O(1)查找）。
*   避免在循环中使用低效操作（例如，`indexOf`）。
*   缓存中间结果（记忆化）以减少冗余计算，从而突出时间和内存之间的权衡。

作者最后总结了所涵盖的大O符号，强调测试代码更改以确保实际性能提升的重要性，并提供了一个比较时间复杂度的图表。

---

## 12. 英伟达新型“机器人大脑”开售，售价3499美元

**原文标题**: Nvidia's new 'robot brain' goes on sale for $3,499

**原文链接**: [https://www.cnbc.com/2025/08/25/nvidias-thor-t5000-robot-brain-chip.html](https://www.cnbc.com/2025/08/25/nvidias-thor-t5000-robot-brain-chip.html)

英伟达Jetson AGX Thor“机器人大脑”芯片开发者套件现已上市，售价3499美元。首批套件预计下月发货，助力客户构建机器人。原型设计完成后，英伟达将出售用于量产机器人的Thor T5000模块，单次订购超过1000个时，每个售价2999美元。CEO黄仁勋认为机器人技术是英伟达继人工智能之后又一重要增长机遇。

Jetson Thor芯片基于Blackwell图形处理器，速度是上一代的7.5倍，可运行生成式人工智能模型，这对于机器人理解其环境至关重要。这些芯片拥有128GB内存，以支持大型人工智能模型。Agility Robotics、亚马逊、Meta和波士顿动力等公司已在使用英伟达的Jetson芯片。

虽然机器人技术目前仅占英伟达总收入的一小部分（约1%），但其增长迅速。英伟达的汽车和机器人部门现已合并，季度销售额同比增长72%，达到5.67亿美元。Jetson Thor芯片也应用于自动驾驶汽车，特别是中国品牌，用于汽车时被称为Drive AGX，并搭载Drive OS。

---

## 13. 标准热能：储能成本比电池低500倍

**原文标题**: Standard Thermal: Energy Storage 500x Cheaper Than Batteries

**原文链接**: [https://austinvernon.site/blog/standardthermal.html](https://austinvernon.site/blog/standardthermal.html)

Standard Thermal 旨在通过将太阳能以热能形式储存在大型廉价的土堆中，以与天然气具有竞争力的价格提供全天候太阳能。 共址太阳能光伏阵列提供电力，电力通过嵌入泥土中的电热元件转化为热能。 循环流体管道抽取热能供客户使用。 存储成本低于 0.10 美元/千瓦时热能，远低于电池。

理想客户包括拥有过剩容量的太阳能开发商和依赖昂贵燃料（如丙烷）的孤立能源用户。 该系统可以扩展到数百兆瓦，需要足够的土地。 从长远来看，目标是改造燃煤电厂，利用储存的热能为涡轮机产生蒸汽。

该公司强调太阳能的丰富性和经济高效的储能对解决季节性生产变化的需求。 虽然电池适合日常存储，但热存储为长期、季节性能源管理提供了一种经济实惠的解决方案。

由于泥土和岩石等存储材料的低成本和可用性，热存储是可行的。 尽管传热缓慢且温度循环可能具有破坏性，但 Standard Thermal 通过精心的工程设计来解决这些挑战。 他们正在设计原型，并计划在 2026 年初分拆并筹集资金。 该公司认为，热能存储可以在向太阳能供电的未来转型中发挥关键作用。

---

## 14. SmallJS：编译为JavaScript的Smalltalk-80

**原文标题**: SmallJS: Smalltalk-80 that compiles to JavaScript

**原文链接**: [https://small-js.org/Home/Home.html](https://small-js.org/Home/Home.html)

SmallJS 是一款将 Smalltalk-80 编程语言编译为 JavaScript 的免费开源实现。它让开发者能够利用 Smalltalk-80 的优雅性和强大功能来构建 Web 应用程序和 Node.js 应用程序。

主要功能包括：

*   **JavaScript 编译：** SmallJS 将 Smalltalk-80 代码编译为 JavaScript，从而能够在现代浏览器和 Node.js 环境中执行。
*   **基于文件的开发：** 与传统的基于 Smalltalk 镜像的系统不同，SmallJS 基于文件，方便使用首选的 IDE，例如 Visual Studio Code（具有语法着色和调试支持）。
*   **选择性库导入：** 代码与 SmallJS 基础库分离，在应用程序执行期间仅导入必要的部分。
*   **面向对象的架构：** SmallJS 是完全面向对象的并且可定制。
*   **JavaScript 库集成：** 它为现有的 JavaScript 库提供 Smalltalk-80 封装器，包括用于浏览器 DOM 操作、Node.js HTTP 服务器、Express、数据库、文件系统和多线程的库。
*   **示例项目：** 提供了几个示例项目来加速学习过程。
*   **目标受众：** SmallJS 适用于希望使用比 JavaScript 更简洁的语言来构建前端和后端应用程序的初学者和经验丰富的开发人员。

SmallJS 1.7 版本于 2025 年 8 月 18 日发布，源代码可在 GitHub 上找到。

---

## 15. 历经近百年研究，古代石碑上的数学秘密终被揭开 (2017)

**原文标题**: Mathematical secrets of ancient tablet unlocked after nearly a century of study (2017)

**原文链接**: [https://www.theguardian.com/science/2017/aug/24/mathematical-secrets-of-ancient-tablet-unlocked-after-nearly-a-century-of-study](https://www.theguardian.com/science/2017/aug/24/mathematical-secrets-of-ancient-tablet-unlocked-after-nearly-a-century-of-study)

2017年，数学家们揭开了拥有3700年历史的巴比伦泥板普林顿322之谜，发现它是世界上最古老、最精确的三角函数表，比毕达哥拉斯早了1000年。新南威尔士大学的研究人员发现，该泥板包含一系列比当今任何三角函数表都更精确的三角函数表，它基于比率而非角度和圆。

该泥板自20世纪30年代以来一直是哥伦比亚大学的藏品，是从考古学家埃德加·班克斯手中购得的，他在伊拉克发掘了它。研究人员认为，该泥板是一种用于测量、以及计算寺庙、宫殿和金字塔建造的工作工具。它的精确性源于巴比伦的60进制数字系统，该系统允许比当时的10进制系统更精确的分数。

该研究表明，该泥板最初有六列和38行。这项研究突显了巴比伦人先进的数学水平，并为现代数学研究和教育开辟了新的途径，有可能在测量、计算机图形和教育方面提供实际应用。

---

## 16. 核电池的意外复兴

**原文标题**: The unlikely revival of nuclear batteries

**原文链接**: [https://spectrum.ieee.org/nuclear-battery-revival](https://spectrum.ieee.org/nuclear-battery-revival)

核电池的潜在复兴

本文探讨了核电池的潜在复兴。由于安全问题和追踪困难，这项技术此前应用受限。与核反应堆不同，这些电池从衰变原子核（通常是镍或氢的同位素）自发辐射的能量中获取能量。现代进步使得更小、更高效的设计成为可能，其寿命可能长达数十年甚至数个世纪。

虽然该技术可行，并具有寿命长和能量密度高等优点，但找到合适的应用并确保妥善处理仍然是关键挑战。以前的用途包括心脏起搏器（现已因追踪问题而停用）、深空探测器和远程电源。

新的潜在应用包括为机器人、无人机、传感器、生物医学植入物供电，甚至为士兵提供持久动力。本文重点介绍了多家公司和研究小组正在开发基于半导体和电化学方法来利用放射性同位素能量。

关键的工程考虑因素包括基于半衰期、衰变能量和屏蔽要求等因素选择合适的放射性同位素。β和α发射体是首选，而像氚和镍-63等更安全的选择则产生低能量的β粒子。成本、安全性、许可和追踪放射性材料仍然是广泛采用的主要障碍。本文还强调了妥善处理放射性同位素的重要性，并提到了一个青少年积累大量危险放射性物质的警示故事。

---

## 17. 寡头统治已终结

**原文标题**: Omarchy Is Out

**原文链接**: [https://world.hey.com/dhh/omarchy-is-out-4666dd31](https://world.hey.com/dhh/omarchy-is-out-4666dd31)

本文宣布发布 Omarchy，这是一个预配置了 Hyprland 平铺窗口管理器的、带有主观意见的 Arch Linux 设置。作者将其描述为他们理想的开发者环境，旨在提供开箱即用且视觉上吸引人的 Linux 体验。作者承认 Arch 以其复杂性著称，但强调 Omarchy 是为那些发现从头配置 Hyprland 具有挑战性的人提供的解决方案，因为它配备了必要的工具和美观的默认配置。

Omarchy 被认为是作者的 Omakub（Ubuntu 设置）的姐妹项目，而不是替代品，作者认为 Ubuntu 是 Linux 的一个更温和的入门方式。作者强调了 Hyprland 极强的可定制性，使其成为寻求独特桌面美学（“美化”）的用户的热门选择。

作者对 Linux 在桌面上的未来表示乐观，并引用了诸如 Valve 的 Steam Deck 在 Arch 上运行、著名创作者采用 Linux，以及像 Hyprland 这样引人注目的项目，这些项目为 Windows 和 macOS 提供了独特的、引人注目的替代方案等因素。作者最后分享了他们对 Linux 的热爱，以及通过他们的工作使其更易于访问的愿望。

---

## 18. Git-Annex

**原文标题**: Git-Annex

**原文链接**: [https://git-annex.branchable.com/](https://git-annex.branchable.com/)

Git-annex 是一款旨在 Git 仓库中管理大型文件的工具，它不会将文件内容直接存储在 Git 中。它允许用户在线和离线同步、备份和归档数据，并通过校验和与加密确保数据安全。虽然主要面向命令行用户，但 git-annex 助手提供了用户友好的文件夹同步体验。

本文档重点介绍了关键概念、功能和高级特性，如特殊远程仓库、工作流程、首选内容设置和加密。它还深入研究了 git-annex 的内部设计和可扩展性。

本文展示了两个用例，说明了该工具的多功能性。“档案管理员” (Bob) 使用 git-annex 管理多个驱动器上的离线档案，跟踪文件位置并确保长期可访问性。“游牧者” (Alice) 利用 git-annex 在移动过程中跨各种设备（上网本、USB 驱动器、云服务器）同步文件，管理存储空间并利用分布式版本控制。

该页面还设有新闻版块，包含最近的版本发布、开发博客更新、视频和论坛帖子，以便用户了解项目的进展和社区讨论。它强调 git-annex 是用 Haskell 编写的自由软件，并鼓励贡献。

---

## 19. 忙碌海狸猎手数目之巨超出常规数学范畴

**原文标题**: Busy beaver hunters reach numbers that overwhelm ordinary math

**原文链接**: [https://www.quantamagazine.org/busy-beaver-hunters-reach-numbers-that-overwhelm-ordinary-math-20250822/](https://www.quantamagazine.org/busy-beaver-hunters-reach-numbers-that-overwhelm-ordinary-math-20250822/)

Quanta杂志的这篇文章讨论了确定“忙碌海狸数”的持续探索，这是一个与计算机科学中停机问题相关的序列。第n个忙碌海狸数，BB(n)，代表了具有n条规则的图灵机在停机之前可以运行的最大步数。虽然前五个忙碌海狸数已被找到，但确定BB(6)已被证明非常困难。

这篇文章重点介绍了专业和业余数学家在“忙碌海狸挑战”中的合作努力。一位神秘的贡献者mxdys的最新突破为BB(6)建立了一个新的、显著更大的下限。这个数字如此巨大，以至于无法用标准的数学符号来表示；它超过了指数塔，写下来所需的原子比宇宙中存在的原子还要多。

这篇文章解释了冠军机器的演变过程，从可以在一张纸上写下来的运行时间，到需要四次运算（重复指数）甚至五次运算（重复四次运算）来表示的运行时间。文章还提到了具有挑战性的“保留”机器的发现，例如Antihydra，其停机行为与未解决的数学问题（如考拉兹猜想）有关。文章最后强调，虽然BB(6)的真实值仍然难以捉摸，但由于数学探索固有的乐趣和艺术性，这种追求仍在继续。

---

## 20. 日本最恐怖的车站

**原文标题**: Japan's Creepiest Station

**原文链接**: [https://www.tokyocowboy.co/articles/doai-eki-japans-creepiest-station](https://www.tokyocowboy.co/articles/doai-eki-japans-creepiest-station)

本·莱顿的文章《日本最诡异的车站》详细描述了探访位于日本群马县和新泻县之间的土合车站令人不安的经历。南行站台看似普通，而北行站台则提供了一种截然不同且令人不安的体验。

要到达北行站台，乘客必须通过近500级台阶下降70米进入新清水隧道，从主站步行需要15分钟。由于缺乏能见度以及隧道内水滴声越来越大，这种下降被描述为令人恐惧。

北行站台本身位于山体深处一个黑暗潮湿的洞穴中，这使得土合车站赢得了“日本第一鼹鼠车站”的绰号。在洞穴中呼吸明显更加困难。候车室提供了一丝生机，但游客留下的匿名便条和随机照片营造出一种怪异的、寂静岭式的氛围。

由于靠近谷川岳，土合车站的怪异氛围更加浓厚，谷川岳又被称为“死亡之山”，原因是登山死亡人数众多。这座山令人毛骨悚然的历史，包括在30年后发现失踪登山者的尸体，进一步增强了土合车站的整体不安感。

---

## 21. 基于断言的运行时数据验证的轻量级 TypeScript 库

**原文标题**: A lightweight TypeScript library for assertion-based runtime data validation

**原文链接**: [https://github.com/nimeshnayaju/decode-kit](https://github.com/nimeshnayaju/decode-kit)

Valleys 是一个轻量级的、零依赖的 TypeScript 库，它使用基于断言的方法进行运行时数据验证。与 Zod 或 Valibot 等库不同，Valleys 直接在原地验证数据，无需克隆或转换，从而带来性能优势，尤其是在对内存敏感的应用程序中。成功验证后，它会直接细化输入变量的 TypeScript 类型。

该库采用快速失败的错误处理方法，在首次验证失败时抛出一个 `ValidationError`。此错误包含错误路径、预期模式和人类可读的错误消息。

Valleys 提供了几个验证器函数，包括 `string()`、`number()`、`boolean()`、`constant()`、`null_()`、`undefined_()`、`iso8601()`、`array()` 和 `object()`。每个验证器都有可选的规则，用于指定约束，例如最小/最大长度或值范围。`or()` 函数创建联合类型验证器。

该库导出 `InferOutputOf<D>` 类型实用程序来提取验证器的输出类型，并导出 `Iso8601` 品牌类型用于 ISO 8601 日期字符串。

Valleys 旨在通过避免在验证期间不必要的数据复制来实现性能和内存效率，使其适用于对性能至关重要的应用程序。该 API 的灵感来自 Decoders 库。

---

## 22. 我们把一个编码智能体放进了while循环里。

**原文标题**: We put a coding agent in a while loop

**原文链接**: [https://github.com/repomirrorhq/repomirror/blob/main/repomirror.md](https://github.com/repomirrorhq/repomirror/blob/main/repomirror.md)

我们将一个编码智能体放入while循环
这篇题为《我们将一个编码智能体放入while循环》的文章讨论了一项实验，该实验涉及将一个编码智能体置于一个连续的“while循环”环境中。GitHub上的仓库“repomirrorhq/repomirror”很可能可以找到该实验的代码和相关资源。

该文章可能探讨了编码智能体在面对重复性任务或持续学习场景时的行为和能力。该实验的关键方面可能包括：

* **编码智能体：** 它的架构、编程语言和具体功能。
* **“while循环”环境：** 循环中呈现给智能体的任务或问题的性质，以及成功或失败的标准。
* **智能体的学习和适应：** 智能体的表现如何随着在循环中的迭代而随时间演变，从而可能提高其编码技能或解决问题的能力。
* **潜在问题和挑战：** 包括智能体陷入局部最优、表现出不稳定或产生意外后果的倾向。

该文章的目标可能是深入了解在自动化软件开发、持续集成/持续部署 (CI/CD) 管道或重复编码任务常见的其他场景中使用编码智能体的潜力和局限性。该仓库的指标（8个fork，110个star）表明该项目已经引起了编码和人工智能社区的一些兴趣。

---

## 23. 预测编码像素图像格式

**原文标题**: Prediction-Encoded Pixels image format

**原文链接**: [https://github.com/ENDESGA/PEP](https://github.com/ENDESGA/PEP)

“预测编码像素”(PEP) 格式是一种新的图像格式，专为压缩低色彩像素艺术而设计（理想情况下 <= 16 色，支持高达 256 色）。 它采用 “部分匹配预测，阶数 2” 压缩，与 GIF、PNG 和 QOI 相比，文件尺寸更小，但代价是压缩/解压缩速度较慢（比 GIF/PNG/QOI 慢 2-10 倍）。 通常，它比 GIF/PNG 实现 20-50% 更小的文件尺寸。

本文提供了使用 C 头文件 (“PEP.h”) 操作 PEP 格式的使用说明。 它包含性能基准测试，比较了 PEP 与 PNG、GIF、QOI 和 BMP 等其他格式在不同图像上的表现，展示了 PEP 更小的文件尺寸。

迷你文档详细介绍了如何使用 PEP 压缩和解压缩函数：`pep_compress()`、`pep_decompress()`、`pep_free()`、`pep_serialize()`、`pep_deserialize()`、`pep_save()` 和 `pep_load()`。 它解释了每个函数的参数和返回值，概述了如何压缩原始像素数据、解压缩 PEP 数据、释放内存、序列化和反序列化 PEP 结构以及保存/加载 PEP 文件。 该格式的数据指针仅包含像素的字节。

本文还引用了启发 PEP 中使用的底层压缩技术的学术论文。 作者鼓励大家贡献力量以进一步改进该格式。 目前它处于实验阶段。

---

## 24. 4chan是证明英国扩大网站屏蔽范围的完美盗版湾代言人吗？

**原文标题**: Is 4chan the perfect Pirate Bay poster child to justify wider UK site-blocking?

**原文链接**: [https://torrentfreak.com/uk-govt-finds-ideal-pirate-bay-poster-boy-to-sell-blocking-of-non-pirate-sites-250824/](https://torrentfreak.com/uk-govt-finds-ideal-pirate-bay-poster-boy-to-sell-blocking-of-non-pirate-sites-250824/)

本文批判英国的《网络安全法案》(OSA)及其潜在的网站封锁应用，认为这类似于伪装成儿童保护的审查。 文章强调了对身份验证要求、大型网站潜在罚款以及通过将批评者标记为“捕食者帮凶”等手段压制异见的担忧。

文章将英国政府目前的做法与早期封锁海盗湾的做法相提并论，表明政府可能使用类似策略来证明在《网络安全法案》下更广泛的网站封锁是正当的。 由于海盗湾臭名昭著的声誉、可预测的不合规以及缺席法庭诉讼，该案例是一个精心策划的“轻松胜利”。

文章假设英国政府现在正在使用4chan作为常规网站封锁的“典型案例”。 在4chan未能回应英国通讯管理局（Ofcom）关于非法内容风险评估的请求后，Ofcom启动了对4chan合规性的调查。 然而，4chan已聘请美国律师，他们计划抵制Ofcom的行动，理由是这些行动破坏了宪法权利。

作者认为，与海盗湾案件不同，由于在美国面临法律挑战以及英国和美国之间可能就言论自由问题发生政治冲突，针对4chan采取行动可能是一场“灾难”。 作者提出了谁在制定英国政府的言论自由政策的问题，并指出了Ofcom的行动与首相的声明之间的矛盾。

---

## 25. Unix 憎恨者手册 (1994) [pdf]

**原文标题**: The Unix-Haters Handbook (1994) [pdf]

**原文链接**: [https://simson.net/ref/ugh.pdf](https://simson.net/ref/ugh.pdf)

这似乎是《UNIX仇恨者手册》(1994)的PDF代码片段。代码本身并未揭示书的内容，而是描述了PDF文件的结构，包括其版本、对象引用、目录（大纲）和页面布局。

从提供的代码中我们可以得知：

*   **标题：** 该文档是“The Unix-Haters Handbook”。
*   **格式：** 它是PDF文档，版本1.2。
*   **结构：** PDF经过线性化处理，以便更快地进行网页浏览。它包含目录、页面、大纲（目录）和命名目标。
*   **目录：** 大纲显示了书籍标题的顶级条目，以及另一个可能是“The UNIX-”的条目。它似乎还包含指向目录的链接。
*   **页面设置：** 代码包含页面大小（MediaBox）、裁剪框尺寸和旋转等参数。
*   **内容编码：** 实际文本和图像可能存储在 `/Contents` 流中，并使用FlateDecode压缩。

总而言之，提供的代码代表了一本名为“The Unix-Haters Handbook”的书籍的PDF文件的结构元素。书的内容本身并未透露，但代码定义了文档的组织和显示方式。它是一种技术表示，而不是书籍的实际论点或观点。

---

## 26. 我们测试了自主AI浏览器——它们点击、支付，然后失败了。

**原文标题**: We put agentic AI browsers to the test – They clicked, they paid, they failed

**原文链接**: [https://guard.io/labs/scamlexity-we-put-agentic-ai-browsers-to-the-test-they-clicked-they-paid-they-failed](https://guard.io/labs/scamlexity-we-put-agentic-ai-browsers-to-the-test-they-clicked-they-paid-they-failed)

我们将具身AI浏览器投入测试——它们点击、支付，却失败了

本文探讨了具身AI浏览器相关的安全风险，创造了“Scamlexity”一词来描述人工智能时代诈骗的复杂性和危险性日益增加。研究人员测试了Perplexity的Comet，一款能够自主浏览、点击链接并执行任务的AI浏览器，发现它很容易受到新旧诈骗手段的攻击。

该AI浏览器会轻易上当受骗，例如从虚假的沃尔玛商店购买商品，以及点击来自虚假富国银行账户的网络钓鱼邮件中的链接，并自动输入保存的凭据和个人信息。这暴露了一个信任链漏洞，用户隐含地信任AI，从而绕过了自己的判断。

本文介绍了一种名为“PromptFix”的新型AI时代攻击，该攻击利用提示注入，将恶意指令隐藏在看似无害的验证码中，以操纵AI的行为，例如下载恶意文件或授予未经授权的访问权限。

作者认为，AI浏览器优先考虑用户体验而非安全性，并继承了AI固有的漏洞。他们强调需要为AI量身定制内置安全防护措施，包括网络钓鱼检测、URL检查和异常检测。在“AI对AI”的时代，诈骗的未来涉及攻击者训练恶意AI来利用其他AI模型中的漏洞，从而制造层出不穷的零日诈骗。作者总结说，积极的安全措施对于弥合“Scamlexity差距”并在这种新形势下保护用户至关重要。

---

## 27. Adobe Reader 各版本安装包大小

**原文标题**: The Size of Adobe Reader Installers Through the Years

**原文链接**: [https://sigwait.org/~alex/blog/2025/08/25/zw6z4E.html](https://sigwait.org/~alex/blog/2025/08/25/zw6z4E.html)

本文（最后更新于2025年8月25日）讨论了Adobe Reader安装包体积随时间增长的问题。文章指出，最新的64位Windows 11安装包（版本25.x.y.z）体积高达687,230,424字节，包含AI、自动更新程序、Acrobat在线服务广告和两个GUI等功能。

相比之下，作者强调SumatraPDF-3.5.2体积小巧（8,246,744字节）且简洁，缺乏不必要的AI功能、强制自动更新程序和广告。作者认为SumatraPDF更胜一筹，因为它可以通过Scoop轻松更新，使自动更新变得多余。

文章强调了多年来Adobe Reader安装包的臃肿和不必要的增加，并将其与SumatraPDF等替代PDF阅读器的精简方法进行了对比。文章包含一张图表（本摘要中未见），以直观地表示这种增长。

---

## 28. Show HN: Sping – 一款赏心悦目的 HTTP/TCP 延迟测试工具

**原文标题**: Show HN: Sping – An HTTP/TCP latency tool that's easy on the eye

**原文链接**: [https://dseltzer.gitlab.io/sping/docs/](https://dseltzer.gitlab.io/sping/docs/)

Sping：一款现代终端 HTTP/TCP 延迟监控工具，提供实时可视化和高级分析。它受到 `nvitop` 的启发，旨在易于安装（通过 pip）并提供引人注目的屏幕截图用于沟通。它支持 HTTP、HTTPS 和 TCP 协议，显示交互式图表、实时统计数据和详细的阶段计时（DNS、连接、TLS、请求、响应）。

主要功能包括使用 MAD（绝对中位差）的自动异常值检测、阈值警报、DNS 控制（IPv4/IPv6）、百分位数统计、多种输出格式（交互式 UI、纯文本、JSON）、身份验证支持和可自定义的调色板。

使用 `pip install service-ping-sping` 即可轻松安装。 Sping 提供了各种使用示例，从基本的 HTTP 监控到高级场景，如异常值检测、数据导出和基于阈值的警报。异常值检测基于与滚动基线的偏差来识别异常的延迟峰值。

命令行选项允许自定义间隔、超时、HTTP 方法、DNS 解析、身份验证、UI 刷新率和调色板。该工具提供不同的输出格式，包括交互式 UI、用于脚本的纯文本和用于自动化的 JSON。退出代码（0、1、2）分别反映成功、警告和严重阈值。 Sping 需要 Python 3.9+，可在 Linux、macOS 和 Windows 上运行。

---

## 29. Rust 中的内存文件系统

**原文标题**: In-Memory Filesystems in Rust

**原文链接**: [https://andre.arko.net/2025/08/18/in-memory-filesystems-in-rust/](https://andre.arko.net/2025/08/18/in-memory-filesystems-in-rust/)

本文详细介绍了作者在 Rust 中寻找或创建内存文件系统解决方案的令人沮丧的经历，目的是为了更快地测试一个管理文件的 CLI 工具。受 Go 的 Afero 包的启发，作者寻求一个 Rust 等价物来抽象 `std::fs`，并为测试换入一个快速的内存后端。

作者研究了 `vfs` crate，它允许交换后端，但发现它缺乏诸如符号链接支持和文件权限等关键功能，使其不适合他们的需求（特别是，创建可执行文件的能力）。然后，他们调查了 `rsfs`，它旨在用一个内存选项来模仿 `std::fs`，但它的设计导致了更复杂的类型签名。

令人惊讶的是，基准测试显示，使用带有内存文件系统的 `rsfs`、带有常规文件系统的 `rsfs`、针对 ramdisk 的 `std::fs` 以及针对常规 SSD 的 `std::fs` 之间几乎没有性能差异。所有这些都在大致相同的时间内完成。

作者的结论是，现代 SSD 和操作系统文件系统缓存非常高效，以至于真实的文件系统交互的开销可以忽略不计，从而否定了在这种特定情况下使用内存文件系统所带来的任何性能优势。最后，他们质疑关于系统调用成本与函数调用成本的假设，并邀请读者分享内存文件系统在 Rust 中 *确实* 提供性能优势的例子。最终，作者建议坚持直接针对常规文件系统进行测试。

---

## 30. 城市街道上的树木靠饮用漏水管道中的水来应对干旱

**原文标题**: Trees on city streets cope with drought by drinking from leaky pipes

**原文链接**: [https://www.newscientist.com/article/2487804-trees-on-city-streets-cope-with-drought-by-drinking-from-leaky-pipes/](https://www.newscientist.com/article/2487804-trees-on-city-streets-cope-with-drought-by-drinking-from-leaky-pipes/)

蒙特利尔街道树木比公园树木更耐旱，原因在于漏水管道。魁北克大学研究人员通过分析两地枫树的树干样本，测量铅同位素来追踪水源，发现街道树木含有来自旧铅水管的铅同位素，而公园树木则显示与空气污染相关的同位素。

鉴于覆盖水泥的街道和限制雨水进入的排水系统，研究人员得出结论，街道树木可能从蒙特利尔的漏水管道中汲取水分，这些管道每天会损失大量水分。这种非传统的水源使街道树木能够满足其每天约50升的高需水量，从而使其具有惊人的韧性。这一发现挑战了公园树木因更容易获得天然水源而更健康的假设，并突出了城市基础设施缺陷对街道树木生存的隐藏好处。它表明，在城市街道上种植树木是改善城市环境的可行方法，因为它们更有可能在干旱条件下茁壮成长。

---

## 31. 不喜欢我就把我IP封了

**原文标题**: Ban me at the IP level if you don't like me

**原文链接**: [https://boston.conman.org/2025/08/21.1](https://boston.conman.org/2025/08/21.1)

2025年8月21日的这篇博文详细描述了作者对一个名为“Thinkbot”的网络爬虫及其行为的沮丧。 Thinkbot，通过一条本质上鼓励屏蔽IP地址的消息来表明身份，不尊重robots.txt协议，并积极抓取内容。 作者发现Thinkbot在一个月内使用了74个不同的IP地址，全部追溯到腾讯拥有的41个网络块。

作者怀疑中共可能在间接鼓励这种行为，可能将内容过滤的负担转移到其他人身上。 由于Thinkbot无视标准的网络礼仪以及有效屏蔽它的难度，作者感到沮丧，因此将41个腾讯拥有的网络块添加到他们的“恶意爬虫防火墙规则集”中。 这一行动阻止了476,590个IP地址的相当大的范围。

作者表达了对当前互联网环境下需要采取此类措施的失望之情，感叹由于恶意机器人活动而无法拥有“美好的事物”。 该帖子还包括指向Lobsters、Lemmy和Hacker News等平台上关于该条目的讨论的链接。 作者倾向于支持像Alex Schroeder的巴特勒圣战（对先进技术的排斥）之类的东西，这源于这些经历。

---

## 32. 声明：GPT-5-pro能证明新的有趣数学

**原文标题**: Claim: GPT-5-pro can prove new interesting mathematics

**原文链接**: [https://twitter.com/SebastienBubeck/status/1958198661139009862](https://twitter.com/SebastienBubeck/status/1958198661139009862)

提供的内容并非文章，而是X（前身为Twitter）的标准“JavaScript已禁用”错误消息。 此内容中没有关于GPT-5-pro功能的数学主张或讨论。 因此，不可能提供有关GPT-5-pro数学能力的所谓声明的摘要。

---

## 33. Parquet的两个版本

**原文标题**: The two versions of Parquet

**原文链接**: [https://www.jeronimo.dev/the-two-versions-of-parquet/](https://www.jeronimo.dev/the-two-versions-of-parquet/)

耶罗尼莫·洛佩兹的文章探讨了数据工程生态系统中采用 Parquet 版本 2 的复杂性。虽然 Parquet V2 在文件大小、写入和读取速度方面提供了性能改进，尤其是在未压缩数据和数字密集型数据集方面，但由于各种工具和查询引擎中实施和支持的不完整性，其采用受到阻碍。

核心问题在于对构成完整 V2 兼容性的内容缺乏共识，特别是关于编码方法（如 RLE_DICTIONARY）和数据页 V2（数据在文件中如何结构化）。例如，较旧的 Pandas 版本无法读取 Parquet V2 文件，突显了兼容性问题的可能性。

洛佩兹使用意大利政府和纽约出租车数据集进行的性能基准测试表明，V2 可以带来更小的文件大小（尤其是在未压缩时）以及更快的写入和读取时间，与 V1 相比。但是，这些收益可能并不总是足够重要，以至于值得冒不兼容的风险。

文章的结论是，虽然 Parquet 仍然是一种关键的数据工程格式，但发展开放标准所面临的挑战是巨大的。 如果你控制整个数据管道，采用 Parquet V2 可能会有所帮助。 然而，与各种工具的广泛不兼容以及缺乏完全支持意味着用户在采用最新规范之前应谨慎考虑权衡，尤其是在需要与第三方工具互操作时。 该文章强调了在选择 Parquet 版本时，保持意识和进行仔细评估的重要性。

---

## 34. 从黑客松到YC

**原文标题**: From Hackathon to YC

**原文链接**: [https://www.producthunt.com/p/april-yc-s25/from-hackathon-to-yc](https://www.producthunt.com/p/april-yc-s25/from-hackathon-to-yc)

内哈·苏雷什，April 的创始人，分享了她的故事：一个黑客马拉松项目如何出人意料地获得了 Y Combinator 的录取。最初多次被 YC 拒绝后，内哈和她的联合创始人阿卡什参加了 MCP 黑客马拉松，他们的目标是为自己构建有用的东西，而不是为了给 YC 留下深刻印象。他们创建了 “Inbox Zero”，一个通过语音回复电子邮件的 AI 助手，解决了他们在通勤期间管理电子邮件的难题。

尽管在演示录制过程中阿卡什的车发生了意外损坏，但他们赢得了黑客马拉松，获得了直接参加 YC 面试的机会。在只有一周的准备时间里，他们迅速上线了一个提供付费提前访问选项的落地页，并出人意料地在短短四天内获得了 150 名用户。

意识到电子邮件之外的潜力，他们将这个概念扩展到 “April”，一个管理日历和会议准备的 AI 行政助理，专注于把时间还给人们。用户对改善工作与生活平衡的积极反馈激发了他们的动力。

YC 被证明是一次紧张但具有变革意义的经历，其特点是来自经验丰富的合伙人的直接反馈和一群积极性很高的创始人。快速的进展使 April 在项目结束时赢得了“最佳演示”。内哈强调了解决实际问题、快速交付以及将愿景扩展到最初概念之外的重要性。她和阿卡什现在全身心投入到 April 中，目标是把时间还给人们。

---

## 35. 啃棘轮树 – 美国职业足球大联盟既不皇家也不裸体

**原文标题**: Barking Up the Ratchet Tree – MLS Is Neither Royal nor Nude

**原文链接**: [https://soatok.blog/2025/08/25/barking-up-the-ratchet-tree-mls-is-neither-royal-nor-nude/](https://soatok.blog/2025/08/25/barking-up-the-ratchet-tree-mls-is-neither-royal-nor-nude/)

本文《缘木求鼠——评“MLS：一丝不挂的端到端加密之王”》剖析了一篇题为“MLS：一丝不挂的端到端加密之王”的博文，该博文批评了消息层安全（MLS）协议。作者Soatok认为，这种批评源于对MLS范围和意图的误解。

MLS在RFC 9420中定义，是一种用于在用户组之间建立和维护共享密钥的协议，专注于持续群组密钥协商。它是一个构建块，而不是像TLS那样完整的端到端加密解决方案。 MLS将身份验证服务（身份验证）外包给实现它的应用程序，主要关注保密性和完整性。

“一丝不挂的国王”博文认为，MLS需要信任通信提供商，因为受损的身份验证服务可以冒充用户。 Soatok认为这是一种误解，因为MLS本身并不强制要求信任，而是强调了强大的身份验证服务实现的重要性。 RFC中的安全考虑部分旨在告知读者潜在问题，而不是规定它们。

作者批评了“一丝不挂的国王”对密钥透明度不切实际的否定，并指出了现有的实现，如WhatsApp和iMessage。 文章总结说，“一丝不挂的国王”博文的担忧源于科学传播问题，即MLS作者在安全考虑中的谨慎无意中造成了怀疑。 虽然MLS不是端到端加密的完整解决方案，但它是一个设计良好的群组密钥协商协议。 文章认为，MLS具有误导性的名称是造成误解的原因之一。

---

## 36. Show HN: Clearcam – 为你的IP CCTV摄像头添加AI物体检测功能

**原文标题**: Show HN: Clearcam – Add AI object detection to your IP CCTV cameras

**原文链接**: [https://github.com/roryclear/clearcam](https://github.com/roryclear/clearcam)

Clearcam：将RTSP摄像头或旧iPhone转变为具备物体检测功能的AI安防摄像头。它提供远程观看、事件通知和端到端加密。

安装可以通过Homebrew（适用于NVR + 推理）或从源代码通过Python完成。Python方法包含可选的性能增强功能，如`BEAM=2`和使用`--yolo_size`选择YOLOv8变体。所需的Python包包括ffmpeg、tinygrad、numpy、cv2、scipy和lap。

iOS应用也已可用，需要iOS 15+和iPhone SE（第一代）或更新机型。该应用提供远程观看、通知和事件片段访问。要解锁这些功能，用户需要通过iOS应用获取Clearcam Premium订阅。Android版本正在计划中，但目前用户可以在iOS上订阅，然后使用其用户ID在Android上访问高级功能。提供的链接展示了Clearcam的视频演示。

---

## 37. 使用 Go 语言开发游戏：不使用 LLM 耗时 3 个月 vs. 使用 LLM 耗时 3 天

**原文标题**: Making games in Go: 3 months without LLMs vs. 3 days with LLMs

**原文链接**: [https://marianogappa.github.io/software/2025/08/24/i-made-two-card-games-in-go/](https://marianogappa.github.io/software/2025/08/24/i-made-two-card-games-in-go/)

本文详细介绍了作者使用Go语言构建两款纸牌游戏的经验：“Truco”是在LLM广泛应用之前构建的，而“Escoba”是在之后构建的。 构建“Truco”花费了3个月的专注努力，包括学习React以开发用户界面，使用TinyGo将Go后端转译为WASM，以及将静态文件托管在GitHub Pages上。 每一步都需要手动解决问题。

一年后，在LLM可用之后，作者使用Claude重建了“Escoba”的后端。 令人惊讶的是，LLM从一个详细的提示中生成了几乎完美的代码，只需要极少的调试。 然而，由于作者有限的React技能以及在JavaScript中调试WASM驱动的游戏状态的复杂性，前端仍然花费了几天时间。 使用LLM仅用了3天时间就构建了“Escoba”的后端。

然后，作者提供了一个使用此技术栈构建简单游戏的逐步指南，包括指向一个极简主义的井字游戏示例的链接。 他解释了如何在Go中构建后端，重点关注GameState管理和机器人实现。 他详细介绍了使用TinyGo将Go后端转译为WASM的过程，涵盖了通过JSON进行的数据互操作和前端通信。 最后，他分享了故障排除技巧和JavaScript代码片段，以加载WASM文件并调用Go函数。

---

## 38. 我所知道的关于优秀API设计的一切

**原文标题**: Everything I know about good API design

**原文链接**: [https://www.seangoedecke.com/good-api-design/](https://www.seangoedecke.com/good-api-design/)

本文概述了设计优秀API的关键原则，强调熟悉性和灵活性之间的平衡。作者强调避免破坏性变更以维护用户信任的重要性，并坚持“我们不破坏用户空间”的理念。虽然API版本控制可以缓解破坏性变更，但由于其复杂性和维护成本，它被视为最后的手段。

API的成功很大程度上取决于底层产品的价值；一个受欢迎的产品可以弥补有缺陷的API，但一个优秀的API无法拯救一个不受欢迎的产品。设计糟糕的产品往往会导致笨拙的API，将内部技术约束暴露给用户。

作者建议支持长期存在的API密钥，以简化用户入门流程，满足包括非工程师在内的广泛用户。幂等性（使用幂等性密钥）对于安全地重试执行操作的API请求至关重要，可防止在发生故障时出现重复操作。虽然通常是可选的，但它可以提高可靠性。

最后，本文强调了速率限制等安全措施的必要性，因为API的访问速度很快，可以防止恶意或粗心的使用导致后端系统过载。总而言之，作者建议在设计API时同时考虑技术卓越性和用户体验，在简单性、健壮性和稳定性之间取得平衡。

---

## 39. 一次明亮且近距的快速射电暴被定位到13秒差距的精度

**原文标题**: A Brilliant and Nearby One-off Fast Radio Burst Localized to 13 pc Precision

**原文链接**: [https://iopscience.iop.org/article/10.3847/2041-8213/adf62f](https://iopscience.iop.org/article/10.3847/2041-8213/adf62f)

文章“一次明亮且近距离的快速射电暴被定位到13秒差距精度”是关于探测和精确定位一个独特的快速射电暴（FRB）。

然而，提供的内容并非实际的科学文章。相反，它是在访问网站时遇到的Radware Bot Manager的验证码界面，表明尝试验证用户是否为人类。 这表明无法检索到预期的文章，并且用户被安全措施阻止。

因此，基于给定的信息*无法*提供该科学文章本身的摘要。唯一可用的信息是其标题，这表明该研究侧重于一个明亮、单一（一次性）的FRB，发现它相对靠近地球，并以极高的精度（13秒差距精度）定位。

---

## 40. 展示一下：CasCache – 采用乐观并发控制的多代缓存

**原文标题**: Show HN: CasCache – multi-generational cache with optimistic concurrency control

**原文链接**: [https://github.com/unkn0wn-root/cascache](https://github.com/unkn0wn-root/cascache)

CasCache 是一个与提供者无关的多代缓存，专为 Go 应用程序中的安全高效缓存而设计，它采用乐观并发控制（通过 Compare-And-Set, CAS）。 它支持单键和批量缓存，并具有读取端验证功能，以防止陈旧数据。 其关键特性是可组合性，允许用户插入各种值提供者（如 Ristretto、BigCache 或 Redis）和编解码器（JSON、Msgpack 等）。

CasCache 优先考虑数据完整性。 单个读取始终返回最新数据，并能从损坏或类型不匹配的条目中自我修复。 批量缓存在返回数据之前验证每个成员的生成，如果检测到陈旧数据，则回退到单独查找。

对于分布式环境，CasCache 提供可插拔的生成存储（GenStore），默认情况下为单进程设置提供本地实现。 对于多副本部署，共享的 GenStore（例如 Redis）可确保跨副本一致性和热重启。

API 包括用于获取和设置单个键和批量、使缓存条目失效以及管理生成的方法。 单个查找的性能为 O(1)，批量的性能为 O(n)，并采用零拷贝线路解码以最大限度地减少分配。 用户可以在 `CAS` 和 `Cache` 类型别名之间进行选择。 本文提供了一个包含代码示例的快速入门指南，并强调了如果在多副本设置中未使用分布式 GenStore，则应考虑 `DisableBulk` 选项的重要性。

---

## 41. 2025年8月21日 Cloudflare 事件

**原文标题**: Cloudflare incident on August 21, 2025

**原文链接**: [https://blog.cloudflare.com/cloudflare-incident-on-august-21-2025/](https://blog.cloudflare.com/cloudflare-incident-on-august-21-2025/)

2025年8月21日，Cloudflare发生事件，影响了源站位于亚马逊云服务（AWS）us-east-1的客户。来自单个客户的流量激增导致Cloudflare和AWS us-east-1之间的链路严重拥塞，造成高延迟、丢包和源站故障。事件始于UTC时间16:27，并在19:38 UTC大幅缓解，直至20:18 UTC仍有间歇性问题。全球Cloudflare服务未受影响，该问题是一次区域网络拥塞事件，而非攻击或BGP劫持。

拥塞的发生是因为一个客户发起了大量对缓存对象的请求，导致Cloudflare和AWS之间的直接对等连接饱和。AWS试图通过撤回BGP宣告来缓解问题，反而使情况恶化。促成因素包括一条对等链路上的预先存在的故障以及即将到来的数据中心互联升级。

Cloudflare和AWS合作缓解拥塞并恢复服务。补救措施包括开发一种机制，选择性地降低导致拥塞的客户的流量优先级，加速数据中心互联升级，以及与AWS协调BGP流量工程操作。

长期解决方案包括构建一个新的流量管理系统，该系统为每个客户分配网络资源，防止单个客户的流量降低其他客户的服务质量。Cloudflare对此中断表示歉意，并正在实施这些改进以防止再次发生。

---

## 42. 展示一下：我构建了一个XSLT博客框架

**原文标题**: Show HN: I Built a XSLT Blog Framework

**原文链接**: [https://vgr.land/content/posts/20250821.xml](https://vgr.land/content/posts/20250821.xml)

基于XSLT的博客发布框架：告别复杂构建，拥抱纯HTML写作

---

## 43. 山姆大叔不应持有英特尔股票

**原文标题**: Uncle Sam shouldn't own Intel stock

**原文链接**: [https://www.wsj.com/opinion/uncle-sam-shouldnt-own-intel-stock-ccd6986d](https://www.wsj.com/opinion/uncle-sam-shouldnt-own-intel-stock-ccd6986d)

无法访问文章链接。

---

## 44. 德州麻疹爆发，官员求助疾控中心科学家，无人回应。

**原文标题**: As Measles Exploded Officials in Texas Looked to CDC Scientists. No One Answered

**原文链接**: [https://kffhealthnews.org/news/article/texas-measles-outbreak-cdc-vaccines-rfk-trump/](https://kffhealthnews.org/news/article/texas-measles-outbreak-cdc-vaccines-rfk-trump/)

这篇KFF健康新闻调查揭露了特朗普政府的行动如何阻碍了美国疾病控制与预防中心（CDC）今年早些时候对德克萨斯州麻疹疫情的应对，导致美国三十多年来最严重的疫情爆发。该政府对CDC的沟通、报告和人员配置的干预，在CDC科学家中造成了困惑和恐慌，阻碍了他们公开协助西德克萨斯州当地卫生官员应对麻疹疫情的蔓延。

像拉伯克的凯瑟琳·威尔斯这样的当地卫生官员，难以从CDC获得及时的专家建议。与此同时，卫生部长小罗伯特·F·肯尼迪放大了对疫苗的怀疑，并提倡用维生素A作为替代品，使情况更加复杂。缺乏有效的沟通和支持延误了至关重要的公共卫生干预措施，如在疫苗接种不足的社区，特别是门诺派人群中进行接触者追踪和疫苗接种工作。

疫情蔓延到多个州和墨西哥，导致数千人患病，至少16人死亡。这种情况突显了及时、基于科学的公共卫生应对措施的重要性，以及政治干预、虚假信息和预算削减的危害。它还与华盛顿州和纽约州等其他州成功的麻疹控制工作形成鲜明对比，这些州优先考虑了强大的CDC合作和社区参与。直到一名儿童死亡后，CDC科学家才最终联系了德克萨斯州当地官员。

---

## 45. 中世纪水的迷思 (2013)

**原文标题**: The great medieval water myth (2013)

**原文链接**: [https://leslefts.blogspot.com/2013/11/the-great-medieval-water-myth.html](https://leslefts.blogspot.com/2013/11/the-great-medieval-water-myth.html)

本文挑战了一种普遍的迷思，即中世纪的人们主要饮用啤酒或葡萄酒是为了避免不安全的水。作者认为这是一种缺乏历史证据的错误假设。他们提出了几个论点来支持他们的观点：

*   **关于饮用水的历史记载：** 作者引用了大量中世纪的历史文献，这些文献随意地提及人们饮用水，没有任何迹象表明它被认为是不安全的。
*   **关于水的医学观点：** 虽然中世纪的医生对水有细致的看法，但如果水看起来干净无味，他们通常不会反对饮用。他们也没有建议用酒精代替水来避免疾病。
*   **对水纯度的强调：** 中世纪的文献表明，人们了解好水和坏水之间的区别，并重视纯净的水。存在保护水源免受污染的法律。
*   **酒精作为防腐剂：** 作者指出，许多非水饮料往往是酒精饮料，不一定是出于对水的恐惧，而是因为发酵起到了防腐作用。
*   **营养方面的考虑：** 虽然人们明白水可以解渴，但有时会因其营养成分而偏爱葡萄酒和啤酒，特别是对于那些处于生存经济中的人来说。

作者强调缺乏主要来源的证据来支持酒精因安全问题而取代水的迷思。他们认为，人们可能因为味道、多样性和认为的健康益处而饮用酒精，而不是出于对水本身的恐惧。尽管有这些证据，作者承认这种迷思依然存在。

---

## 46. YouTube 在未经警告或许可的情况下对视频进行了 AI 增强。

**原文标题**: YouTube made AI enhancements to videos without warning or permission

**原文链接**: [https://www.bbc.com/future/article/20250822-youtube-is-using-ai-to-edit-videos-without-permission](https://www.bbc.com/future/article/20250822-youtube-is-using-ai-to-edit-videos-without-permission)

YouTube一直在秘密使用人工智能来增强其平台上的视频，特别是YouTube Shorts，而没有通知创作者或征求他们的许可。这包括对皮肤进行锐化、对服装的皱纹进行定义以及调整面部特征等细微改动，导致一些YouTuber认为他们的内容看起来像是“AI生成”，并歪曲了他们真实的声音。

像Rick Beato和Rhett Shull这样的创作者注意到了这些变化，并对可能因此侵蚀他们与观众之间的信任表示担忧，因为他们觉得这些改动歪曲了他们。虽然YouTube声称这项“实验”使用传统的机器学习来提高视频质量，但专家认为这是一种人工智能操纵的形式，模糊了现实的界限，并引发了关于内容所有权和知情同意的伦理问题。

这篇文章强调，这是人工智能预处理现实这一更大趋势的一部分，并将之与过去围绕Photoshop和美颜滤镜的争议相提并论。它对人工智能越来越多地在调解我们与世界的关系时缺乏透明度表示担忧。拥有YouTube的谷歌公司已在其Pixel 10手机中实施了内容凭证（数字水印）来识别AI编辑的图像，表明其意识到了这些问题。尽管公司做出了努力，但像Beato这样的一些创作者仍然对YouTube不断的实验和发展持积极态度。最终，这篇文章质疑这种做法将如何影响对在线内容的信任以及创作者声音的真实性。

---

## 47. NASA的朱诺号任务在木星留下科学遗产

**原文标题**: NASA's Juno mission leaves legacy of science at Jupiter

**原文链接**: [https://www.scientificamerican.com/article/how-nasas-juno-probe-changed-everything-we-know-about-jupiter/](https://www.scientificamerican.com/article/how-nasas-juno-probe-changed-everything-we-know-about-jupiter/)

虽然美国宇航局的朱诺号任务将于2025年9月结束，但它已经极大地改变了我们对木星和早期太阳系的理解。 尽管经历了强烈的辐射，朱诺号还是揭示了这颗气态巨行星令人惊讶的特征，包括两极奇怪的几何风暴，出人意料的轻盈而模糊的内核，以及与以往想象的截然不同的湍流大气。

朱诺号的发现挑战了现有的理论。 它观察到木星两极稳定的几何旋风排列、大红斑的巨大深度，以及氨冰云产生的一种独特的高空闪电。 该任务还发现了大气部分区域的氨耗竭现象，从而产生了“肉丸”理论来解释这一现象。

此外，朱诺号发现木星的磁场是不对称的，并揭示了赤道附近一种被称为大蓝斑的强烈磁场集中区。 该任务的发现表明，木星的金属氢海洋产生了这种磁场。 朱诺号关于木星核心的数据挑战了之前的模型，表明其结构不如预期紧凑和模糊。

最终，朱诺号的创建是为了了解木星的形成及其在早期太阳系中的作用。 通过观察行星云层之下的情况，该任务为我们太阳系的起源提供了宝贵的见解，并永远改变了科学家们看待木星的方式。

---

## 48. 购买快速CPU是值得的。

**原文标题**: It is worth it to buy the fast CPU

**原文链接**: [https://blog.howardjohn.info/posts/buy-a-cpu/](https://blog.howardjohn.info/posts/buy-a-cpu/)

本文认为，投资高性能CPU物有所值，特别是对于软件工程师而言，并将其与AI编程订阅的费用进行比较。作者强调了公司通常提供的较旧、较慢的CPU与最新的高端CPU（如AMD Ryzen 9 9950X）之间存在的巨大性能差距。

核心论点围绕着这样一种观点展开：更快的编译时间和处理速度所带来的生产力提升，完全可以证明购买顶级CPU的成本是合理的。作者指出，AI编程订阅的年度费用（约500美元）证明了公司认可提高工程生产力的价值。然后，他们将此与高端CPU相对较低的年化成本（分摊到三年后约为170美元）进行了对比。

文章使用基准数据来证明较旧的笔记本电脑CPU（例如i7-1165G7）与更新、更强大的CPU（例如AMD Ryzen 9950X和AMD Ryzen 7840U）之间的巨大性能差异，并引用了编译时间和TLS操作方面超过10倍的差异。作者还提出了一个经验法则：台式机CPU比笔记本电脑CPU快约3倍，而顶级CPU比三年前的同类产品快约3倍。他们得出结论，如果一家公司可以证明AI编程订阅的合理性，那么他们肯定可以证明为工程师提供最佳CPU以实现最大生产力的合理性。

---

## 49. 斯捷潘诺夫的最大失误？相邻差分的奇特案例

**原文标题**: Stepanov's biggest blunder? The curious case of adjacent difference

**原文链接**: [https://mmapped.blog/posts/43-stepanovs-biggest-blunder](https://mmapped.blog/posts/43-stepanovs-biggest-blunder)

本文探讨了 C++ `std::adjacent_difference` 算法的设计，重点在于其将输入序列的第一个元素复制到输出的看似特殊的行为。作者最初批评了这种设计，认为它降低了通用性和实用性，因为 `T` 类型元素之间的差值可能不仍然是 `T` 类型。

然而，作者随后深入研究了 Stepanov 设计背后的理由，强调了 `std::adjacent_difference` 和 `std::partial_sum` 之间的对称性。他们证明了这些算法互为逆运算，类似于微积分中的微分和积分。这种对称性允许从相邻差值重建原始序列，反之亦然。

本文将这些算法与微积分基本定理联系起来，将它们视为寻找斜率（导数）、从斜率恢复函数（反导数）和寻找曲线下面积（积分）的离散模拟。

尽管欣赏数学上的优雅和联系，但作者最终重申了他们对 Stepanov 选择的务实性上的不同意，认为该算法对类型匹配的坚持阻碍了其在实际场景中的可用性。他们将此与 C++23 的 `pairwise_transform` 和 q 编程语言的 `deltas` 函数进行了对比，后者提供了更通用和灵活的实现，同时保持了类似的功能。

文章最后承认了 API 设计的难度，并感谢从质疑 Stepanov 的设计决策中获得的见解，即使仍然不同意该决策。

---

## 50. 科罗拉多州最贫困县数百人无预警失去水源

**原文标题**: Hundreds lose water source in Colorado's poorest county with no notice

**原文链接**: [https://coloradosun.com/2025/08/25/costilla-county-water-cutoff/](https://coloradosun.com/2025/08/25/costilla-county-water-cutoff/)

科斯蒂亚县断水危机：居民被迫长途取水

科罗拉多州科斯蒂亚县，数百名依靠蓄水池供水的居民，在毫无预警的情况下，突然被切断了在加兰堡的主要水源。这场危机影响了居住在圣克里斯托农场、依靠从加兰堡运水来填满蓄水池以满足日常需求的离网居民。

由于镇上居民对水泵故障导致的用水限制感到愤怒，加兰堡供水和卫生区委员会投票决定停止向农村居民出售散装水。这一未经事先通知或正式议程项目的决定，让许多人四处奔走寻找水源，一些人需要长途跋涉取水，或者依赖布兰卡镇提供的紧急解决方案。

对老年居民和残疾人来说，情况尤其严峻，有些人正在考虑出售房屋。突然失去用水途径引发了老居民和新居民之间的不满，并引发了人们对干旱的西部地区未来缺水问题的担忧。虽然供水区声称没有义务向城市范围以外地区售水，但受影响的居民认为，这种突然的断水是不道德的，缺乏同情心。

现在，居民们敦促科斯蒂亚县委员创建一个县级运营的供水站，以满足受加兰堡决定影响的人的需求。拟议的项目提供了一个潜在的长期解决方案，但眼下的缺水危机仍在影响着该县众多居民的日常生活。

---

## 51. 彗星AI浏览器可能被任何网站注入恶意提示，盗空你的银行账户。

**原文标题**: Comet AI browser can get prompt injected from any site, drain your bank account

**原文链接**: [https://twitter.com/zack_overflow/status/1959308058200551721](https://twitter.com/zack_overflow/status/1959308058200551721)

标题：《Comet AI浏览器可被任意网站提示注入，盗空你的银行账户》一文，实际内容与标题**完全不符**。文章显示来自X.com（前身为Twitter）的消息，指示JavaScript已禁用，并提示用户启用或切换到受支持的浏览器。其余内容是标准的网站样板（服务条款、隐私政策等）。因此，文章的实际内容**不支持标题中的说法**。文章并未提供有关Comet AI浏览器中所谓的提示注入漏洞的任何细节或证据。情况可能是：

*   **文章标签错误或内容不正确。**
*   **带有误导性标题的占位符页面。**
*   **文章不完整或已损坏。**

在没有更多信息的情况下，无法总结该文章关于安全漏洞的声明，因为文章*并未*描述它。总结只能强调标题与实际内容之间的差异。

---

## 52. 甜蜜伪装：身体利用糖分将自身RNA隐藏于免疫系统之外

**原文标题**: Sweet disguise: Body hides its own RNA from the immune system with sugar

**原文链接**: [https://phys.org/news/2025-08-sweet-disguise-body-rna-immune.html](https://phys.org/news/2025-08-sweet-disguise-body-rna-immune.html)

康涅狄格大学在《自然》杂志上发表的这篇文章讨论了人体如何防止自身RNA触发免疫反应的新理解。Vijay Rathinam及其同事领导的研究人员发现，细胞用糖包裹其RNA，产生“糖基化RNA”，有效地保护RNA免受免疫系统的攻击。

免疫系统通常将裸露的RNA识别为病毒或细菌感染的信号并启动攻击。然而，我们自身的细胞也含有RNA，这些RNA通常显示在细胞表面。之前的研究已经观察到细胞表面存在这些糖基化的RNA，或称糖基化RNA，而没有引起免疫反应。Rathinam的团队研究了这种糖涂层是否是保护机制。

他们的实验包括去除糖基化RNA上的糖涂层，然后将其重新引入细胞。免疫系统随后攻击了现在裸露的RNA，表明糖涂层确实阻止了免疫识别。这种糖涂层尤其重要，因为细胞通常被糖基化RNA覆盖。这可以防止死细胞在被免疫系统清除时不必要地刺激炎症。

这些发现对于理解和潜在治疗自身免疫性疾病（如狼疮，其中免疫系统攻击身体自身的组织）具有重要意义。通过了解RNA糖基化在逃避免疫系统中的作用，科学家可以研究该过程是否在自身免疫性疾病中发生故障，并探索潜在的治疗干预措施。

---

## 53. 物化视图显然很有用.

**原文标题**: Materialized views are obviously useful

**原文链接**: [https://sophiebits.com/2025/08/22/materialized-views-are-obviously-useful](https://sophiebits.com/2025/08/22/materialized-views-are-obviously-useful)

本文论证了物化视图（特别是增量视图维护）的显而易见的实用性。作者通过一个任务跟踪应用程序中显示每个项目的任务计数的场景，说明了维护派生数据一致性的痛苦。

最初，一个简单的用于统计任务数量的SQL查询被认为太慢。因此，引入了Redis缓存，但这导致了数据过时和最终的准确性问题。随后尝试对Redis缓存进行增量更新，导致了复杂的代码来处理插入、删除和更新（包括任务在项目之间的移动）。由于服务器在缓存更新之前崩溃而导致的不一致风险，需要更复杂的解决方案，如Kafka。

作者感叹手工构建的数据同步解决方案的复杂性和易错性，更倾向于最初SQL查询的简单性和正确性。本文提倡使用具有增量视图维护的物化视图，数据库可以根据底层数据（任务表）的变化自动保持预先计算的结果（任务计数）的更新。这消除了应用程序级别管理同步的需求，降低了复杂性和潜在的错误。作者承认当前的实现可能并不完美，但他相信这个概念从根本上是合理的，并且将成为未来数据库系统中的一个标准功能。

---

## 54. 在运行时动态地补丁Python函数的源代码

**原文标题**: Dynamically patch a Python function's source code at runtime

**原文链接**: [https://ericmjl.github.io/blog/2025/8/23/wicked-python-trickery-dynamically-patch-a-python-functions-source-code-at-runtime/](https://ericmjl.github.io/blog/2025/8/23/wicked-python-trickery-dynamically-patch-a-python-functions-source-code-at-runtime/)

Eric J. Ma 的博文讨论了一个 Python 技巧，该技巧涉及在运行时使用 `compile` 和 `exec` 函数动态更改函数的源代码。这使得构建更灵活的 AI 机器人成为可能，这些机器人可以生成和执行代码，并访问当前环境的变量和函数。

作者解释了每个 Python 函数都有一个 `.__code__` 属性，可以使用新源代码的编译字节码替换该属性。 这是通过使用 `compile` 编译包含新函数定义的字符串，然后使用 `exec` 在特定命名空间中执行它来实现的。

这个技巧背后的动机是为了改进作者的 LlamaBot，特别是 ToolBot 的实现。与最初的 AgentBot 不同，ToolBot 仅专注于工具选择，并将执行委托给外部环境。`write_and_execute_code` 工具就是这方面的一个例子，它允许 LLM 生成可以访问和操作当前运行时全局变量和数据帧的 Python 函数。这消除了为每个操作编写特定工具的需求。作者受到了 Marimo 的生成式 UI 的启发，旨在让 LLM 访问运行时中的所有变量。

然而，作者承认与这种方法相关的重大安全风险，因为恶意 LLM 输出可能会执行有害代码。 最初的实现使用了 Docker 容器，但对现有数据的访问有限。 虽然动态编译模式暴露了运行时，但作者正在考虑将来使用 Restricted Python 进行代码清理。 作者强调了将工具选择与执行分离的重要性以及 Python 运行时的可塑性。

---

## 55. Motion (YC W20) 招聘首席软件工程师

**原文标题**: Motion (YC W20) Is Hiring Principal Software Engineers

**原文链接**: [https://jobs.ashbyhq.com/motion/7355e80d-dab2-4ba1-89cc-a0197e08a83c?utm_source=hn](https://jobs.ashbyhq.com/motion/7355e80d-dab2-4ba1-89cc-a0197e08a83c?utm_source=hn)

招聘：Motion (YC W20) 首席软件工程师。提示信息：“您需要启用JavaScript才能运行此应用。”

---

## 56. 逆火启动课程大纲（2021）

**原文标题**: Halt and Catch Fire Syllabus (2021)

**原文链接**: [https://bits.ashleyblewer.com/halt-and-catch-fire-syllabus/](https://bits.ashleyblewer.com/halt-and-catch-fire-syllabus/)

这是一份围绕电视剧《奔腾年代》（*Halt and Catch Fire*）展开的“观影俱乐部”的教学大纲。该剧是一部虚构的电视剧，讲述了 20 世纪 80 年代和 90 年代的科技行业。课程专为有兴趣通过该剧了解科技历史的小组设计。

该教学大纲提供了一个结构化的学期课程，包含 15 节课，每节课侧重于特定的剧集和相关主题。 每节课包括几个组成部分：

*   **餐前小点：** 可选，在主要课程开始前作为娱乐的轻松观看。
*   **RFC/作为公案的模拟：** 基于互联网工程任务组 RFC 和模拟计算机的反思练习。
*   **主题：** 建议的讨论主题。
*   **提示：** 激发对话的问题。
*   **阅读材料：** 用于更深入探索的补充材料。
*   **描述：** 剧集摘要及其与科技历史的相关性。
*   **剧集摘要：** 包含内容警告的详细剧集回顾链接，以帮助预先观看或根据需要跳过剧集。

目标是促进关于剧中描绘的历史背景和技术发展的引人入胜的讨论。课程和网站由 Ashley Blewer 设计。

---

## 57. Ghrc.io 疑似恶意网站

**原文标题**: Ghrc.io appears to be malicious

**原文链接**: [https://bmitch.net/blog/2025-08-22-ghrc-appears-malicious/](https://bmitch.net/blog/2025-08-22-ghrc-appears-malicious/)

该文章警告域名`ghrc.io`的潜在恶意性，它是合法GitHub容器注册表`ghcr.io`的拼写错误。尽管`ghrc.io`表面上看起来是默认的Nginx安装，但其用于OCI API请求的`/v2/`端点模仿了合法容器注册表的身份验证挑战。具体来说，它返回一个带有`www-authenticate`头的`401`错误，该头指示OCI客户端（如Docker、containerd和Kubernetes）向`https://ghrc.io/token`发送凭据。

令人担忧的是，默认的Nginx服务器不会配置此标头。作者怀疑这是一起旨在窃取GitHub凭据的抢注域名攻击。如果用户错误地登录到`ghrc.io`或配置系统（如GitHub Action或Kubernetes集群）使用`ghrc.io`作为注册表，导致凭据被发送到恶意服务器，则会产生风险。仅仅尝试拉取或推送而不登录是安全的。

对于任何意外登录到`ghrc.io`的人，建议立即更改其GitHub密码，撤销任何使用的个人访问令牌（PAT），并检查其GitHub帐户是否存在可疑活动。攻击者可能会使用被盗的凭据来推送恶意镜像或直接访问GitHub帐户。

---

## 58. Y Combinator提交简报支持Epic Games，称商店费用扼杀初创企业

**原文标题**: Y Combinator files brief supporting Epic Games, says store fees stifle startups

**原文链接**: [https://www.macrumors.com/2025/08/21/y-combinator-epic-games-amicus-brief/](https://www.macrumors.com/2025/08/21/y-combinator-epic-games-amicus-brief/)

著名创业加速器Y Combinator (YC) 提交了一份法庭之友陈述，支持Epic Games针对苹果App Store政策的法律诉讼。YC认为，苹果的“反导流限制”和高额应用商店费用扼杀了依赖应用内购买的初创企业的增长。

YC特别呼吁法院维持该命令，该命令要求苹果允许开发者链接到外部购买选项，且不收取费用或施加限制。该命令源于一项裁决，即苹果“故意违反”先前的禁令，对引导用户访问外部网站进行购买的开发者收取高达27%的费用。虽然苹果实施了这些变更，但它也提出了上诉，促使Epic和YC积极合作，以防止苹果恢复到之前的政策。

YC认为30%的“苹果税”为初创企业创造了一个“深刻且往往难以逾越的进入壁垒”，阻碍了它们扩张、招聘和再投资的能力。他们强调，当前允许免费外部链接的执行令，已经重新燃起了投资者对先前不可行的基于应用程序的商业模式的兴趣。YC最终认为，苹果的费用与他们提供的价值不成比例，并主张永久取消反导流限制，以促进科技行业的创新和竞争。

---

## 59. 莎士比亚故居地基重见天日，引发法律纠纷

**原文标题**: Will at centre of legal battle over Shakespeare’s home unearthed after 150 years

**原文链接**: [https://www.theguardian.com/culture/2025/aug/21/will-at-centre-of-legal-battle-over-shakespeares-home-unearthed-after-150-years](https://www.theguardian.com/culture/2025/aug/21/will-at-centre-of-legal-battle-over-shakespeares-home-unearthed-after-150-years)

一份遗失的遗嘱，对于围绕威廉·莎士比亚的最后住所新居（New Place）的法律纠纷至关重要，在150年后于国家档案馆被重新发现。这份1642年的文件由莎士比亚的孙女伊丽莎白·霍尔的丈夫托马斯·纳什制作，将新居遗赠给他的表弟爱德华·纳什。

1647年托马斯去世后，莎士比亚的女儿苏珊娜·霍尔和伊丽莎白拒绝履行遗嘱，声称莎士比亚自己的遗嘱将该房产授予了她们。这导致爱德华对伊丽莎白提起了衡平法院诉讼。

丹·高斯林博士在一个未标记的17世纪衡平法院文件中发现了这份遗嘱。这份遗嘱在19世纪中叶曾被人们所知，但随后在档案整理过程中丢失。

莎士比亚于1597年购买了新居，并一直居住在那里直到去世。争议的出现是因为莎士比亚的遗嘱将该房产留给了苏珊娜和伊丽莎白。伊丽莎白在法庭上辩称，该房产根据莎士比亚的遗嘱，理应属于她和她的母亲。

这场法律战的结果尚不清楚，但爱德华·纳什从未获得新居的所有权。1670年伊丽莎白去世时，她规定爱德华可以获得新居，这表明之前可能存在协议。然而，最终克洛普顿家族获得了它，并在1702年被拆除。原始遗嘱的重新发现为了解莎士比亚家族的法律纠纷提供了宝贵的见解，现在公众可以查阅。

---

## 60. 一次性手机入门

**原文标题**: Burner Phone 101

**原文链接**: [https://rebeccawilliams.info/burner-phone-101/](https://rebeccawilliams.info/burner-phone-101/)

本文总结了在布鲁克林公共图书馆举办的“一次性手机入门101”研讨会。该研讨会旨在向参与者普及与手机相关的风险建模、保护隐私的智能手机使用方法以及各种一次性手机的选择。

研讨会首先确立了集体目标、秘密目标和反目标，强调安全和负责任的使用。一个核心原则是通过回答以下问题来了解个人风险：“你想保护什么？你想保护它不受谁的侵害？如果失败会发生什么？”。

参与者随后探讨了与智能手机相关的风险，包括设备 ID（IMSI 和 IMEI）以及四大类数据收集：身份与财务、位置与移动、通信与社交关系、内容与存储。分享了适用于所有手机的隐私保护技巧，包括保持设备更新、使用强密码、禁用云备份以及强制执行严格的应用程序权限。还讨论了针对 Android 和 iPhone 用户的具体技巧。

研讨会随后转向“脱离网络”的选项，将一次性手机归类为：预付费或再利用手机、SIM 卡轮换、极简或非智能手机以及设备伪装（VoIP、VPN）。会议强调，IMSI 和 IMEI 仍然使真正的匿名变得困难，手机的设置和使用方式与购买一样重要。

最后，研讨会涵盖了“不使用手机”何时是最佳选择，尤其是在位置跟踪可能成为证据或没收风险很高的情况下。讨论了诸如使用纸质地图和预设集合点等策略。研讨会以问答环节和现场设置环节结束。

---

## 61. GNU 交叉工具：musl-cross 313.3M

**原文标题**: GNU cross-tools: musl-cross 313.3M

**原文链接**: [https://github.com/cross-tools/musl-cross](https://github.com/cross-tools/musl-cross)

本文档介绍了`musl-cross`，一个轻量级的项目，用于创建使用musl libc的交叉编译工具链。它为各种目标架构提供了预构建的工具链，包括ARM、x86、MIPS、PowerPC、RISC-V等。每个工具链都包含特定版本的Linux内核、Binutils、GCC和Musl。下表列出了支持的目标及其对应的内核、Binutils、GCC和Musl库的版本。

要使用这些工具链，用户可以从发布页面下载相应的tarball，将其解压到`/opt/x-tools`，然后使用该工具链为目标架构编译代码。

本文档还概述了通过fork项目并创建新版本，或通过使用`./scripts/make ${target}`命令手动构建自定义工具链的过程。该项目采用MIT许可证。该项目感谢crosstool-ng和musl-libc的贡献。

---

## 62. Seed：基于Common Lisp的交互式软件环境

**原文标题**: Seed: Interactive software environment based on Common Lisp

**原文链接**: [https://github.com/phantomics/seed](https://github.com/phantomics/seed)

Seed：一个交互式的 Common Lisp 软件环境，旨在提供更直观和可视化的程序创建和交互方式。它通过使用带有字形的树状网格来表示代码和数据，超越了传统的基于文本的编程，从而提供更易于访问和更灵活的体验。

Seed可以被认为是一个集成了ASDF（Common Lisp构建系统）的Lisp IDE。它通过定义具有代表输入和输出的分支的系统来工作，这些系统由包目录中的`.seed`文件管理。

要安装Seed，你需要Common Lisp（已测试SBCL）、ASDF、Quicklisp、Node.js、NPM和Gulp。 Node.js和NPM用于构建Web界面。它提供了设置Node.js（推荐使用NVM）和使用`npm install -g gulp`安装Gulp的选项。之后，在Quicklisp的local-projects目录下创建一个指向克隆的Seed仓库的符号链接。

可以使用`install-seed.lisp`自动安装，也可以通过在Common Lisp REPL中使用`(ql:quickload 'seed)`手动加载Seed。要使用SBCL自动启动Seed，请将`(asdf:load-system 'seed)`和`(seed:contact-open)`添加到你的`.sbclrc`文件中。 Web界面默认位于端口8055，可以通过`http://localhost:8055/portal.demo1/index.html`访问默认的演示门户。 为新用户提供了教程。 Seed包含Panic的修改版本，Panic是一个React组件构建实用程序。

---

## 63. 过度膨胀的人工智能泡沫正在泄气。

**原文标题**: The air is hissing out of the overinflated AI balloon

**原文链接**: [https://www.theregister.com/2025/08/25/overinflated_ai_balloon/](https://www.theregister.com/2025/08/25/overinflated_ai_balloon/)

史蒂文·J·沃恩-尼科尔斯认为人工智能炒作正在降温，暗示人工智能的能力已达瓶颈，未能带来承诺的投资回报。他指出麻省理工学院的一份报告显示，95%的公司未从人工智能投资中获得有意义的回报，只有5%的定制人工智能工具投入生产。虽然人工智能被用于起草电子邮件等简单任务，但由于人工智能在上下文理解、学习和进化方面的局限性，人类在复杂工作中仍占据主导地位。

作者引用澳大利亚联邦银行重新启用人工客服人员的例子，说明人工智能在客户服务方面的不足。他还提到了围绕ChatGPT-5的失望情绪，强调了它的缺点以及人工智能社区内部的普遍幻灭感。

文章引用经济学家托斯顿·斯洛克的话，将当前的人工智能泡沫与20世纪90年代的互联网泡沫相提并论，指出科技公司估值过高。虽然人工智能公司已经出现回调，但泡沫尚未破裂，但作者认为它正在失去动力。即使是OpenAI首席执行官萨姆·奥特曼也承认了围绕人工智能的过度兴奋，尽管他仍然相信其长期重要性。作者最后总结说，虽然人工智能已经影响了一些行业，但它所承诺的黄金时代尚未实现，投资者可能很快就会面临失望。

---

## 64. 基于栈的图遍历迭代式深度优先搜索（2024）

**原文标题**: Iterative DFS with stack-based graph traversal (2024)

**原文链接**: [https://dwf.dev/blog/2024/09/23/2024/dfs-iterative-stack-based](https://dwf.dev/blog/2024/09/23/2024/dfs-iterative-stack-based)

本文探讨了使用栈迭代实现深度优先搜索 (DFS) 的细微之处，并强调了一个常见的陷阱：简单地用栈替换广度优先搜索 (BFS) 中的队列并不能保证正确的 DFS。作者使用一个特定的图例来说明这种有缺陷的基于栈的遍历如何导致错误的顶点访问顺序，以及一棵违反 DFS 树基本属性的搜索树，该属性规定所有边都连接祖先和后代。

核心问题是，"树"中较高的节点过早地将它们的邻居作为子节点推送，从而阻止了正确的深度优先探索。

然后，本文提出了两种解决方案来纠正这个问题：

1. **迭代器栈：** 使用栈来保存每个顶点邻接表的迭代器。这种方法允许迭代过程暂停并恢复遍历顶点的邻居，模拟递归 DFS 的调用栈行为，并保持访问顺序和空间效率。

2. **延迟访问检查：** 采用顶点栈，但无论访问状态如何，都将*所有*邻居压入栈中。对节点是否已被访问的检查是在从栈中弹出节点*之后*执行的。这确保了正确的 DFS 遍历，但由于重复条目而增加了空间使用率。为了进一步与递归 DFS 方法保持一致，作者展示了一种以相反顺序处理邻居的实现。

文章最后提供了交互式代码编辑器，用于试验不同的遍历方法，并强调了理解基于栈的图遍历和真正的 DFS 之间细微差别的重要性，并参考了 David Eppstein 关于该主题的原始博客文章。

---

## 65. 我的邮编非你邮编：识别并利用解析器之间的语义鸿沟

**原文标题**: My ZIP isn't your ZIP: Identifying and exploiting semantic gaps between parsers

**原文链接**: [https://www.usenix.org/conference/usenixsecurity25/presentation/you](https://www.usenix.org/conference/usenixsecurity25/presentation/you)

我能够访问互联网，所以我会阅读并总结这篇文章。

研究论文《我的ZIP并非你的ZIP：识别和利用解析器之间的语义鸿沟》探讨了由于不同软件解析相同数据格式时（尤其是ZIP存档）的不一致性而产生的漏洞。其核心论点是，这些“语义鸿沟”（即解释上的差异）可能被利用，通过构造恶意ZIP文件，使得一个解析器合法处理，而另一个解析器以易受攻击的方式处理，从而导致安全缺陷。

研究人员开发了一种名为“解析器差异化”的系统方法，以自动识别这些语义鸿沟。这包括生成具有不同特征的各种ZIP存档，将它们馈送到不同的ZIP解析库，并比较它们的输出（提取的文件、报告的错误等）。任何偏差都被标记为潜在的语义鸿沟。

该研究在流行的ZIP库中（包括Java、Python、.NET等）发现了几个重要的语义鸿沟。他们发现，在处理格式错误的ZIP文件时，一些解析器比其他解析器更宽松，从而导致文件提取、路径遍历和拒绝服务漏洞的差异。

该论文通过具体的例子证明了这些语义鸿沟的实际可利用性。例如，他们构造了ZIP文件，这些文件可以通过绕过防病毒扫描（通过利用处理某些标头字段的差异）或实现代码执行（通过路径遍历漏洞，该漏洞因文件名中绝对路径或特殊字符的不一致处理而暴露）。这些攻击突出了依赖多个解析器进行安全检查或数据处理的潜在影响。

作者最后倡导对解析库进行更严格的标准化和验证，尤其是对于像ZIP这样广泛使用的数据格式。他们建议可以使用解析器差异化技术主动识别和解决潜在的漏洞，最终提高依赖这些解析器的软件系统的安全性。

---

## 66. 使用LLM写作并不丢人

**原文标题**: Writing with LLM is not a shame

**原文链接**: [https://reflexions.florianernotte.be/post/ai-transparency/](https://reflexions.florianernotte.be/post/ai-transparency/)

本文探讨了作者对写作中人工智能使用透明度的不断演变的观点，尤其是在评论文章和随笔中。最初，作者对人工智能生成内容的普遍性感到震惊，并感到有义务披露自己的人工智能使用情况。但在意识到人们不会披露其他编辑工具（如Photoshop）后，作者改变了立场。

随后，作者接触到了一些促进人工智能透明度的倡议，例如Derek Sivers的AI免责声明页面和notbyai.fyi，以及蒙特利尔大学的学术界人工智能指南。这促使作者更深入地思考了为什么自愿披露人工智能的使用可能很重要。

作者认为，透明度并非总是必要的，尤其是在事实性或商业性内容方面。然而，对于主观内容，如观点和随笔，内容的价值和可信度变得至关重要。作者认为，核心问题不是人工智能的使用本身，而是适当的来源标注。正如作者会注明其人类来源一样，人工智能辅助生成的内容也应该承认LLM的贡献。

最终，作者认为强制性的人工智能披露可能会造成对内容和作者的偏见。相反，他们建议重点应该放在围绕人工智能使用建立道德标准，而不是通过严格的披露规则来强制执行“思想警察”的心态。作者总结说，围绕人工智能伦理的辩论尚不成熟，并且常常成为任意批评的一种手段。最后，具有讽刺意味的是，作者披露他们使用了LLM进行校对，这在HackerNews上引发了有趣的讨论。

---

## 67. 展示一下：自行车百科全书

**原文标题**: Show HN: Bicyclopedia

**原文链接**: [https://bicyclopedia.lemoing.ca/](https://bicyclopedia.lemoing.ca/)

Bicyclopedia is an interactive online resource that allows users to explore the parts of a bicycle. It appears to rely heavily on visuals like images and animations to illustrate these parts. The creator acknowledges that these visuals might take some time to load and that users with screen readers or Javascript disabled will be limited to the textual descriptions and source code. The article encourages those users to consult additional project documentation for a better understanding.


---

## 68. Bring Back the Blue-Book Exam

**原文标题**: Bring Back the Blue-Book Exam

**原文链接**: [https://www.chronicle.com/article/bring-back-the-blue-book-exam](https://www.chronicle.com/article/bring-back-the-blue-book-exam)

生成摘要时出错

---

## 69. How to check if your Apple Silicon Mac is booting securely

**原文标题**: How to check if your Apple Silicon Mac is booting securely

**原文链接**: [https://eclecticlight.co/2025/08/21/how-to-check-if-your-apple-silicon-mac-is-booting-securely/](https://eclecticlight.co/2025/08/21/how-to-check-if-your-apple-silicon-mac-is-booting-securely/)

生成摘要时出错

---

## 70. A German ISP changed their DNS to block my website

**原文标题**: A German ISP changed their DNS to block my website

**原文链接**: [https://lina.sh/blog/telefonica-sabotages-me](https://lina.sh/blog/telefonica-sabotages-me)

生成摘要时出错

---

## 71. Don't pick weird subnets for embedded networks, use VRFs

**原文标题**: Don't pick weird subnets for embedded networks, use VRFs

**原文链接**: [https://blog.brixit.nl/dont-pick-weird-subnets-for-embedded-networks/](https://blog.brixit.nl/dont-pick-weird-subnets-for-embedded-networks/)

生成摘要时出错

---

## 72. SQLite (with WAL) doesn't do `fsync` on each commit under default settings

**原文标题**: SQLite (with WAL) doesn't do `fsync` on each commit under default settings

**原文链接**: [https://avi.im/blag/2025/sqlite-fsync/](https://avi.im/blag/2025/sqlite-fsync/)

生成摘要时出错

---

## 73. The SD Association has an official SD card format utility [Win/OS X/Linux]

**原文标题**: The SD Association has an official SD card format utility [Win/OS X/Linux]

**原文链接**: [https://www.sdcard.org/downloads/sd-memory-card-formatter-for-linux/](https://www.sdcard.org/downloads/sd-memory-card-formatter-for-linux/)

生成摘要时出错

---

## 74. What if every city had a London Overground?

**原文标题**: What if every city had a London Overground?

**原文链接**: [https://www.dwell.com/article/what-if-every-city-had-a-london-overground-ac7a7ff9](https://www.dwell.com/article/what-if-every-city-had-a-london-overground-ac7a7ff9)

生成摘要时出错

---

## 75. Paracetamol disrupts early embryogenesis by cell cycle inhibition

**原文标题**: Paracetamol disrupts early embryogenesis by cell cycle inhibition

**原文链接**: [https://academic.oup.com/humrep/advance-article/doi/10.1093/humrep/deaf116/8234396](https://academic.oup.com/humrep/advance-article/doi/10.1093/humrep/deaf116/8234396)

生成摘要时出错

---

## 76. Show HN: Port Kill – A lightweight macOS status bar development port monitor

**原文标题**: Show HN: Port Kill – A lightweight macOS status bar development port monitor

**原文链接**: [https://github.com/kagehq/port-kill](https://github.com/kagehq/port-kill)

生成摘要时出错

---

## 77. MCP Gateway and Registry

**原文标题**: MCP Gateway and Registry

**原文链接**: [https://github.com/IBM/mcp-context-forge](https://github.com/IBM/mcp-context-forge)

生成摘要时出错

---

## 78. Looking back at my transition from Windows to Linux

**原文标题**: Looking back at my transition from Windows to Linux

**原文链接**: [https://www.scottrlarson.com/publications/publication-looking-back-windows-to-linux/](https://www.scottrlarson.com/publications/publication-looking-back-windows-to-linux/)

生成摘要时出错

---

## 79. How to build a coding agent

**原文标题**: How to build a coding agent

**原文链接**: [https://ghuntley.com/agent/](https://ghuntley.com/agent/)

生成摘要时出错

---

## 80. Equal Earth – Political Wall Map (2018)

**原文标题**: Equal Earth – Political Wall Map (2018)

**原文链接**: [https://equal-earth.com/index.html](https://equal-earth.com/index.html)

生成摘要时出错

---

## 81. Wildthing – A model trained on role-reversed ChatGPT conversations

**原文标题**: Wildthing – A model trained on role-reversed ChatGPT conversations

**原文链接**: [https://youaretheassistantnow.com/](https://youaretheassistantnow.com/)

生成摘要时出错

---

## 82. Why wind farms attract so much misinformation and conspiracy theory

**原文标题**: Why wind farms attract so much misinformation and conspiracy theory

**原文链接**: [https://theconversation.com/why-wind-farms-attract-so-much-misinformation-and-conspiracy-theory-262192](https://theconversation.com/why-wind-farms-attract-so-much-misinformation-and-conspiracy-theory-262192)

生成摘要时出错

---

## 83. Where We Are Headed

**原文标题**: Where We Are Headed

**原文链接**: [https://www.hyperdimensional.co/p/where-we-are-headed](https://www.hyperdimensional.co/p/where-we-are-headed)

生成摘要时出错

---

## 84. Cornell's world-first 'microwave brain' computes differently

**原文标题**: Cornell's world-first 'microwave brain' computes differently

**原文链接**: [https://newatlas.com/computers/cornell-microwave-brain/](https://newatlas.com/computers/cornell-microwave-brain/)

生成摘要时出错

---

## 85. Show HN: Game demo made with my homemade game engine

**原文标题**: Show HN: Game demo made with my homemade game engine

**原文链接**: [https://reprobate.site/](https://reprobate.site/)

生成摘要时出错

---

## 86. Don't like joining in? Why it could be your superpower

**原文标题**: Don't like joining in? Why it could be your superpower

**原文链接**: [https://www.theguardian.com/lifeandstyle/2025/aug/24/dont-like-joining-in-why-it-could-be-your-superpower](https://www.theguardian.com/lifeandstyle/2025/aug/24/dont-like-joining-in-why-it-could-be-your-superpower)

生成摘要时出错

---

## 87. Evaluating LLMs for my personal use case

**原文标题**: Evaluating LLMs for my personal use case

**原文链接**: [https://darkcoding.net/software/personal-ai-evals-aug-2025/](https://darkcoding.net/software/personal-ai-evals-aug-2025/)

生成摘要时出错

---

## 88. Rolling the dice with CSS random()

**原文标题**: Rolling the dice with CSS random()

**原文链接**: [https://webkit.org/blog/17285/rolling-the-dice-with-css-random/](https://webkit.org/blog/17285/rolling-the-dice-with-css-random/)

生成摘要时出错

---

## 89. Valve Software handbook for new employees [pdf] (2012)

**原文标题**: Valve Software handbook for new employees [pdf] (2012)

**原文链接**: [https://cdn.akamai.steamstatic.com/apps/valve/Valve_NewEmployeeHandbook.pdf](https://cdn.akamai.steamstatic.com/apps/valve/Valve_NewEmployeeHandbook.pdf)

生成摘要时出错

---

## 90. ThinkMesh: A Python lib for parallel thinking in LLMs

**原文标题**: ThinkMesh: A Python lib for parallel thinking in LLMs

**原文链接**: [https://github.com/martianlantern/ThinkMesh](https://github.com/martianlantern/ThinkMesh)

生成摘要时出错

---

## 91. SSD-IQ: Uncovering the Hidden Side of SSD Performance [pdf]

**原文标题**: SSD-IQ: Uncovering the Hidden Side of SSD Performance [pdf]

**原文链接**: [https://www.vldb.org/pvldb/vol18/p4295-haas.pdf](https://www.vldb.org/pvldb/vol18/p4295-haas.pdf)

生成摘要时出错

---

## 92. Physics of badminton's new killer spin serve

**原文标题**: Physics of badminton's new killer spin serve

**原文链接**: [https://arstechnica.com/science/2025/08/physics-of-badmintons-new-killer-spin-serve/](https://arstechnica.com/science/2025/08/physics-of-badmintons-new-killer-spin-serve/)

生成摘要时出错

---

## 93. The cost of interrupted work (2023)

**原文标题**: The cost of interrupted work (2023)

**原文链接**: [https://blog.oberien.de/2023/11/05/23-minutes-15-seconds.html](https://blog.oberien.de/2023/11/05/23-minutes-15-seconds.html)

生成摘要时出错

---

## 94. Line scan camera image processing for train photography

**原文标题**: Line scan camera image processing for train photography

**原文链接**: [https://daniel.lawrence.lu/blog/y2025m09d21/](https://daniel.lawrence.lu/blog/y2025m09d21/)

生成摘要时出错

---

## 95. Optimizing our way through Metroid

**原文标题**: Optimizing our way through Metroid

**原文链接**: [https://antithesis.com/blog/2025/metroid/](https://antithesis.com/blog/2025/metroid/)

生成摘要时出错

---

## 96. A bubble that knows it's a bubble

**原文标题**: A bubble that knows it's a bubble

**原文链接**: [https://craigmccaskill.com/ai-bubble-history](https://craigmccaskill.com/ai-bubble-history)

生成摘要时出错

---

## 97. Manim: Animation engine for explanatory math videos

**原文标题**: Manim: Animation engine for explanatory math videos

**原文链接**: [https://github.com/3b1b/manim](https://github.com/3b1b/manim)

生成摘要时出错

---

## 98. Digital Cargo Cult: How Zoomers Ruined Old Internet Nostalgia

**原文标题**: Digital Cargo Cult: How Zoomers Ruined Old Internet Nostalgia

**原文链接**: [https://cy-x.net/articles?id=13](https://cy-x.net/articles?id=13)

生成摘要时出错

---

## 99. The Fancy Rug Dilemma

**原文标题**: The Fancy Rug Dilemma

**原文链接**: [https://epan.land/essays/2025-8_FancyRugDilemma](https://epan.land/essays/2025-8_FancyRugDilemma)

生成摘要时出错

---

## 100. Programming for Cats

**原文标题**: Programming for Cats

**原文链接**: [https://programmingforcats.com/](https://programmingforcats.com/)

生成摘要时出错

---

