# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-08-25.md)

*最后自动更新时间: 2025-08-25 17:46:53*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 2 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 3 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 4 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 5 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 6 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 7 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 8 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 9 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 10 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 11 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 12 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 13 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 14 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 15 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 16 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 17 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 18 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 19 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 20 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 21 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 22 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 23 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 24 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 25 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 26 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 27 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 28 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 29 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 30 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 31 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 32 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 33 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 34 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 35 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 36 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 37 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 38 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 39 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 40 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 41 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 42 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 43 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 44 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 45 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 46 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 47 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 48 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 49 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 50 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 51 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 52 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 53 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 54 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 55 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 56 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 57 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 58 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 59 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 60 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 61 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 62 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 63 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 64 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 65 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 66 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 67 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 68 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 69 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 70 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 71 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 72 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 73 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 74 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 75 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 76 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 77 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 78 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 79 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 80 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 81 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 82 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 83 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 84 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 85 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 86 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 87 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 88 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 89 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 90 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 91 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 92 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 93 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 94 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 95 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 96 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 97 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 98 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 99 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 100 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 101 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 102 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 103 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 104 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 105 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 106 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 107 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 108 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 109 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 110 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 111 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 112 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 113 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 114 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 115 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 116 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 117 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 118 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 119 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 120 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 121 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 122 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 123 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 124 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 125 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 126 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 127 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 128 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 129 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 130 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 131 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 132 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 133 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 134 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 135 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 136 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 137 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 138 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 139 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 140 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 141 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 142 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 143 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 144 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 145 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 146 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 147 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 148 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 149 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 150 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 151 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 152 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 153 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 154 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 155 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 156 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 157 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 158 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 159 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
