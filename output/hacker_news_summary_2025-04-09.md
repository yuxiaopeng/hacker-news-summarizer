# Hacker News 热门文章摘要 (2025-04-09)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 使用内容安全策略强化 Firefox 前端

**原文标题**: Hardening the Firefox Front End with Content Security Policies

**原文链接**: [https://attackanddefense.dev/2025/04/09/hardening-the-firefox-frontend-with-content-security-policies.html](https://attackanddefense.dev/2025/04/09/hardening-the-firefox-frontend-with-content-security-policies.html)

需求：
1. 仅提供一个准确的中文翻译
2. 直接输出翻译，无需解释或多重选项
3. 保持原文的含义和风格
4. 如果是标题，保持简洁明了

本文详细介绍了针对 Firefox 用户界面进行加固以抵御注入攻击，尤其是跨站脚本攻击 (XSS) 的工作。Firefox 的 UI 使用 HTML、CSS 和 JavaScript 等 Web 技术构建，容易受到 XSS 攻击，恶意代码可以被注入和执行。核心策略涉及实施内容安全策略 (CSP) 以限制脚本执行。

主要关注点是 `browser.xhtml`，这是包含地址栏和标签等元素的主要 UI 文档。团队从 `browser.xhtml` 中移除了超过 600 个内联事件处理程序，将它们替换为在外部 JavaScript 文件中定义的标准事件监听器。这消除了一个常见的攻击途径。

本文重点介绍了替换内联事件处理程序的过程，并提到了重要的考虑因素，例如 `event.preventDefault()` 和 `this` 的行为。

未来的计划包括将 CSP 扩展到其他 UI 组件，例如“关于 Firefox”对话框，并采用更严格的策略。最终目标是阻止 Firefox 内的所有动态代码执行，进一步增强安全性并提高对 XSS 攻击的抵抗力。这项工作显著提高了 Firefox 的安全态势，旨在打破现有的漏洞利用链。这些更改将包含在 Firefox 138 中。

---

