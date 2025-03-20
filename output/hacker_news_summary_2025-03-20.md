# Hacker News 热门文章摘要 (2025-03-20)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 克劳德现在可以搜索网络了。


**原文标题**: Claude can now search the web

**原文链接**: [https://www.anthropic.com/news/web-search](https://www.anthropic.com/news/web-search)

以下是将原文翻译成中文的版本，保持了原文的意思和风格：

Anthropic 的 Claude 现在配备了网络搜索功能，能提供更及时和相关的回应。这项功能赋予 Claude 获取最新事件和信息的能力，提升了其在需要最新数据的任务中的准确性。

当 Claude 将网络信息纳入回复时，它会提供直接引用，方便用户核实来源。用户无需自行搜索，Claude 会以对话形式处理并提供相关来源。这项增强功能利用实时洞察扩展了 Claude 广泛的知识库，提供了基于最新信息的答案。

文章列举了网络搜索的几个常见应用场景：销售团队可以通过分析行业趋势进行账户规划；金融分析师可以评估市场数据、盈利报告和行业趋势来做出投资决策；研究人员可以构建更强的资助提案和文献综述；购物者可以比较产品特性、价格和评论，从而做出更明智的购买决策。

目前，网络搜索功能以预览版形式向美国所有付费 Claude 用户开放。未来将支持免费用户和更多国家/地区。用户可以在个人资料设置中启用网络搜索，并与 Claude 3.7 Sonnet 开始对话。


---

## 2. ACARS风云 / ACARS剧


**原文标题**: ACARS Drama

**原文链接**: [https://acarsdrama.com/](https://acarsdrama.com/)

## ACARS 戏剧

“ACARS 戏剧”网站介绍了一个名为“ACARS 戏剧”的项目，该项目通过监听飞机上的无线电信号（ACARS 和 VDLM2），提取其中包含的“戏剧性”信息，并将其发布到社交媒体上。ACARS（飞机通信寻址与报告系统）是一种 20 世纪 70 年代的协议，而 VDLM2（甚高频数据链模式 2）是更现代的协议，两者都用于在飞机和地面站之间传输数据。

该项目利用廉价的无线电接收设备和开源软件解码这些信号，并通过软件过滤出包含人类输入内容的有趣信息，例如飞机故障、乘客问题等。由于接收到的信息量巨大，项目只关注包含特定关键词的“自由文本”消息，这些消息通常是由飞行员或机组人员通过飞行管理计算机（FMC）输入的。

文章解释了如何理解这些信息，例如识别飞机注册号、航班号，并提供了通过链接追踪飞机位置的方法。虽然大部分信息是例行公事，但偶尔会出现有趣的内容，这使得该项目充满乐趣。

最后，文章鼓励读者参与该项目，只需花费约 30 美元购买 SDR 设备和开源软件，就可以监听和分享自己捕捉到的 ACARS 和 VDLM2 信息。文章提供了详细的配置说明和 GitHub 示例配置。


---

## 3. 前端跑步机

（或者 前端车轮）

这个标题很简洁，保留原文意思和风格，主要体现了以下几点：

*   **直译：** "Frontend" 直接翻译为"前端"，"Treadmill" 直译为"跑步机"。
*   **简洁有力：** 与原文一样，翻译后的标题也很简洁，容易理解。
*   **暗示：** "跑步机" 隐喻了前端技术更新迭代快，开发者疲于奔命，难以真正进步的困境。
*   **"车轮" 选项：** 如果更强调“原地踏步”、“无意义循环”的感觉，也可以翻译成"前端车轮"，但相对来说，“跑步机”更常见也更容易理解。

所以，我推荐 **前端跑步机** 作为最佳翻译。


**原文标题**: The Frontend Treadmill

**原文链接**: [https://polotek.net/posts/the-frontend-treadmill/](https://polotek.net/posts/the-frontend-treadmill/)

以下是将原文翻译成中文，保持原文意思和风格的译文：

这篇文章“前端跑步机”批判了前端开发领域对框架的过度依赖和频繁重写。作者认为，对于希望长期存在的项目来说，前端框架的选择是最不重要的技术决策，花费时间争论框架更是浪费精力。框架更新换代迅速，5年后很可能已经过时。

作者建议团队深入了解现有框架，让其不再成为阻碍，而不是不断追逐新的框架。对于求职者，作者建议将框架偏好作为求职标准，避免加入团队后试图强行改变技术栈。

文章倡导回归 Web 平台基础，减少复杂抽象，拥抱 Web 的能力。作者认为，掌握核心 Web 技术能提升工程师的长期职业价值。

文章还指出，当前的前端生态系统让新手难以学习和就业，公司也更难招聘。过度抽象使开发者无法学习 Web 基础，导致未来难以适应变化。作者认为，对框架的过度依赖阻碍了 Web 的发展，建议开发者拥抱 Web 平台并利用其强大的底层工具。


---

## 4. CVE-2024-54471: macOS上泄露密码（以及更多！）


**原文标题**: CVE-2024-54471: Leaking Passwords (and More!) on macOS

**原文链接**: [https://wts.dev/posts/password-leak/](https://wts.dev/posts/password-leak/)

以下是将原文翻译成中文，保持原文意思和风格的译文：

本文详尽地分析了 macOS 中一个已修复的安全漏洞 CVE-2024-54471，该漏洞允许未经授权的进程访问存储在 NetAuthAgent 中的服务器凭据（例如密码）。文章首先对 macOS 的内核（XNU）、Mach 内核的历史和架构，以及进程间通信 (IPC) 的基础知识进行了铺垫，重点介绍了 Mach 的四个核心抽象概念：任务、线程、端口和消息。

文章解释了 Mach 消息传递机制的复杂性，以及 Mach 接口生成器 (MIG) 如何简化通信，但同时也指出了 MIG 服务器可能存在的安全漏洞。文章着重展示了如何利用 `ipsw` 工具来查找潜在的 MIG 服务器。

随后，文章深入探讨了漏洞本身，揭示了 NetAuthAgent 的工作原理，以及在漏洞修复之前，攻击者如何能够向 NetAuthAgent 发送消息，从而直接获取任意服务器的凭据。该漏洞已在 macOS Sequoia 15.1、Sonoma 14.7.1 和 Ventura 13.7.1 中得到修复。文章强调了更新 macOS 操作系统以避免此漏洞的重要性。总体而言，本文是一篇关于 macOS 安全漏洞的技术分析，涵盖了漏洞的背景知识、技术细节和利用方式。


---

## 5. 全是偶数数字的2的幂


**原文标题**: Powers of 2 with all even digits

**原文链接**: [https://oeis.org/A068994](https://oeis.org/A068994)

由于文章内容显示“Just a moment...Enable JavaScript and cookies to continue”，这表明实际文章内容无法被访问。因此，我无法提供关于“Powers of 2 with all even digits”这篇文章的摘要。我只能推测文章可能探讨的内容：

**可能的文章主题摘要：**

文章可能探讨了2的幂（例如2, 4, 8, 16, 32, 64, ...）中，哪些数字是由全部偶数数字（0, 2, 4, 6, 8）构成的。

可能的讨论点包括：

* **这类数字是否存在？** 探讨是否存在这样的2的幂，以及其数量是否有限。
* **寻找这类数字：** 如果存在，文章可能提供寻找这些数字的方法，或者列举已知的例子。
* **数学性质：** 分析这些数字的数学性质，例如它们出现的频率、分布规律，或者与其他数论概念的联系。
* **证明或猜想：** 文章可能提出关于这类数字的猜想，或者提供证明，例如证明不存在大于某个值的、由全偶数数字组成的2的幂。

**由于缺乏实际文章内容，以上仅仅是基于标题的猜测。更准确的摘要需要获取文章的实际内容。**


---

## 6. Oxygen discovered in most distant known galaxy

**原文标题**: Oxygen discovered in most distant known galaxy

**原文链接**: [https://www.eso.org/public/news/eso2507/](https://www.eso.org/public/news/eso2507/)

天文学家在已知最遥远的星系 JADES-GS-z14-0 中发现了氧气。距离如此遥远，它的光花了134亿年才到达地球，这意味着我们看到的星系是宇宙诞生后不到3亿年，约占宇宙现在年龄的2%时的样子。两项独立研究都利用阿塔卡马大型毫米/亚毫米阵列 (ALMA) 发现了这一现象，这让天文学家重新思考早期宇宙中星系形成的速度。

这一发现表明，该星系的化学成熟度远超预期，重元素的含量是预计的10倍，这表明该星系形成和成熟的速度比之前认为的要快得多。氧的发现还使天文学家能够更准确地测量 JADES-GS-z14-0 的距离，精度达到0.005%。虽然该星系最初是由詹姆斯韦伯太空望远镜发现的，但 ALMA 证实并精确地确定了它的巨大距离，展示了 ALMA 和 JWST 在揭示第一批星系的形成和演化方面的惊人协同作用。

---

## 7. Pump.co (YC S22) Is Hiring

**原文标题**: Pump.co (YC S22) Is Hiring

**原文链接**: [https://www.ycombinator.com/companies/pump-co/jobs/7kB7DNb-email-outreach-manager](https://www.ycombinator.com/companies/pump-co/jobs/7kB7DNb-email-outreach-manager)

生成摘要时出错

---

## 8. Grease: An Open-Source Tool for Uncovering Hidden Vulnerabilities in Binary Code

**原文标题**: Grease: An Open-Source Tool for Uncovering Hidden Vulnerabilities in Binary Code

**原文链接**: [https://www.galois.com/articles/introducing-grease](https://www.galois.com/articles/introducing-grease)

生成摘要时出错

---

## 9. Understanding Solar Energy

**原文标题**: Understanding Solar Energy

**原文链接**: [https://www.construction-physics.com/p/understanding-solar-energy](https://www.construction-physics.com/p/understanding-solar-energy)

生成摘要时出错

---

## 10. Minding the gaps: A new way to draw separators in CSS

**原文标题**: Minding the gaps: A new way to draw separators in CSS

**原文链接**: [https://blogs.windows.com/msedgedev/2025/03/19/minding-the-gaps-a-new-way-to-draw-separators-in-css/](https://blogs.windows.com/msedgedev/2025/03/19/minding-the-gaps-a-new-way-to-draw-separators-in-css/)

生成摘要时出错

---

