# Hacker News 热门文章摘要 (2025-04-09)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 使用内容安全策略强化 Firefox 前端

**原文标题**: Hardening the Firefox Front End with Content Security Policies

**原文链接**: [https://attackanddefense.dev/2025/04/09/hardening-the-firefox-frontend-with-content-security-policies.html](https://attackanddefense.dev/2025/04/09/hardening-the-firefox-frontend-with-content-security-policies.html)

<<<<<<< Updated upstream
需求：
1. 仅提供一个准确的中文翻译
2. 直接输出翻译，无需解释或多重选项
3. 保持原文的含义和风格
4. 如果是标题，保持简洁明了

本文详细介绍了针对 Firefox 用户界面进行加固以抵御注入攻击，尤其是跨站脚本攻击 (XSS) 的工作。Firefox 的 UI 使用 HTML、CSS 和 JavaScript 等 Web 技术构建，容易受到 XSS 攻击，恶意代码可以被注入和执行。核心策略涉及实施内容安全策略 (CSP) 以限制脚本执行。

主要关注点是 `browser.xhtml`，这是包含地址栏和标签等元素的主要 UI 文档。团队从 `browser.xhtml` 中移除了超过 600 个内联事件处理程序，将它们替换为在外部 JavaScript 文件中定义的标准事件监听器。这消除了一个常见的攻击途径。

本文重点介绍了替换内联事件处理程序的过程，并提到了重要的考虑因素，例如 `event.preventDefault()` 和 `this` 的行为。

未来的计划包括将 CSP 扩展到其他 UI 组件，例如“关于 Firefox”对话框，并采用更严格的策略。最终目标是阻止 Firefox 内的所有动态代码执行，进一步增强安全性并提高对 XSS 攻击的抵抗力。这项工作显著提高了 Firefox 的安全态势，旨在打破现有的漏洞利用链。这些更改将包含在 Firefox 138 中。
=======
本文讨论了 Firefox 针对注入攻击，特别是跨站脚本攻击 (XSS) 的前端强化工作。 Firefox 用户界面使用 HTML、CSS 和 JavaScript 等 Web 技术构建，与常规 Web 应用程序一样，容易受到这些攻击。 重点是利用内容安全策略 (CSP) 减轻 XSS 攻击。

此安全计划的主要目标是 `browser.xhtml`，这是包含地址栏和标签栏等元素的核心 UI 文件。 团队一直在系统地删除内联事件处理程序，这是一种常见的攻击媒介，并用在单独的 JavaScript 文件中定义的事件监听器替换它们。 已经通过 50 个错误修复了 600 多个内联事件处理程序。

文章重点介绍了替换内联事件处理程序的过程以及开发人员的注意事项。 它还概述了已取得的进展以及未来的强化前景。 除了删除内联处理程序之外，团队还在实施更严格的 CSP，例如 `default-src chrome: resource:;`，这限制了 Firefox 可以加载的资源。 最终目标是在 Firefox 中完全消除动态代码执行，以增强安全性并提高对 XSS 攻击的抵抗力。 这些更改计划在 Firefox 138 中推出。 通过删除这些事件处理程序，该团队认为它已经显着提高了攻击者利用 Firefox 的门槛。
>>>>>>> Stashed changes

---

