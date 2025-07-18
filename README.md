# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-07-18.md)

*最后自动更新时间: 2025-07-18 17:51:09*
## 1. lsr：使用io_uring的ls

**原文标题**: lsr: ls with io_uring

**原文链接**: [https://tangled.sh/@rockorager.dev/lsr](https://tangled.sh/@rockorager.dev/lsr)

`lsr` 是一款新的 `ls` 工具，它利用 io_uring 通过批量处理系统调用来潜在地提升 Linux 系统上的性能。它用 Zig 编写，需要 Zig 0.14.0 才能安装。 安装需要使用带有期望优化级别和前缀的 `zig build` 命令。

`lsr` 提供了常见的 `ls` 功能，包括显示所有文件 (`-a`)、几乎所有文件 (`-A`)、控制输出格式（列、每行一个）、启用颜色、排序、显示图标以及显示扩展文件元数据 (`-l`) 等选项。

基准测试表明，`lsr` 可以胜过其他 `ls` 实现，包括 `ls`、`eza`、`lsd`、`uutils` 和 `busybox ls`，尤其是在处理大量文件时。这些基准测试比较了执行时间（使用 hyperfine）和系统调用次数（使用 strace）。结果表明，`lsr` 通常表现出更低的执行时间和显著更少的系统调用，尤其是在文件数量增加时，突出了 io_uring 带来的效率提升。然而，io_uring 的优势仅在 Linux 上可用。

---

## 2. DuckDuckGo 现在允许你隐藏搜索结果中的 AI 生成图像

**原文标题**: DuckDuckGo now lets you hide AI-generated images in search results

**原文链接**: [https://techcrunch.com/2025/07/18/duckduckgo-now-lets-you-hide-ai-generated-images-in-search-results/](https://techcrunch.com/2025/07/18/duckduckgo-now-lets-you-hide-ai-generated-images-in-search-results/)

DuckDuckGo推出新功能，过滤搜索结果中的AI生成图像。此功能旨在解决用户反馈AI图像妨碍搜索真实内容的问题。用户可以在图片标签页搜索后切换“AI图像”过滤器，选择“显示”或“隐藏”AI生成内容。该过滤器也可以在通用搜索设置中启用。

DuckDuckGo承认低质量AI生成媒体（“AI垃圾”）日益普遍，并采用手动管理的开源黑名单，如uBlockOrigin的“nuclear”列表和uBlacklist Huge AI Blocklist，来识别和过滤AI图像。虽然该过滤器并不完美，但它能显著减少显示的AI图像数量。

DuckDuckGo计划未来添加更多过滤器。文章指出，DuckDuckGo“小孔雀”的示例搜索参考了谷歌过去在搜索结果中优先显示AI生成图像而非真实图像的争议。

---

## 3. 尝试 Guix：一位 Nix 用户的印象

**原文标题**: Trying Guix: A Nixer's Impressions

**原文链接**: [https://tazj.in/blog/trying-guix](https://tazj.in/blog/trying-guix)

本文详细介绍了Nix用户首次尝试Guix的经历，重点关注在较不常见的CPU架构上复制标准桌面环境时遇到的实际挑战和差异。作者承认由于丰富的经验，对Nix有很强的偏见。

主要要点包括：

*   **政治考量：** Guix严格遵守自由软件，因此需要使用"nonguix"来启用常见的硬件，如无线互联网，这直接影响了技术设置。
*   **架构差异：** 与Nix将nixpkgs作为大型数据结构导入的更模块化的方法不同，Guix将CLI与包含来自频道的所有软件包和模块的系统配置文件紧密集成。这使得Guix中的版本切换速度较慢。
*   **文档与入门：** Guix的文档比Nix更出色，但需要熟悉Scheme。"nonguix"的情况由于缺乏资源而进一步使入门复杂化。
*   **性能：** Guix的评估速度明显慢于Nix，在作者的低性能笔记本电脑上尤其明显。
*   **Init系统：** Guix使用Shepherd（一个用Scheme编写的init系统）而不是systemd。
*   **Profile全局安装：** Guix似乎更喜欢软件包的profile全局安装，例如Emacs软件包，而不是Nix创建具有帮助程序的隔离环境的方法。

作者总结说，虽然Guix提出了挑战，但其连贯的生态系统和Lisp的使用令人着迷。他们计划继续尝试Guix，以实现与其现有NixOS设置的功能对等，并找到更快的迭代工作流程。

---

## 4. CP/M 创始人 Gary Kildall 回忆录免费下载发布

**原文标题**: CP/M creator Gary Kildall's memoirs released as free download

**原文链接**: [https://spectrum.ieee.org/cpm-creator-gary-kildalls-memoirs-released-as-free-download](https://spectrum.ieee.org/cpm-creator-gary-kildalls-memoirs-released-as-free-download)

文章宣布免费下载加里·基尔代尔的回忆录。基尔代尔是CP/M操作系统的创造者，文章将其视为创业文化的先驱。文章暗示他的故事突出了他对这种创业精神的贡献。文章还包含一张兰迪·克莱特（推测与基尔代尔有关）的照片，并注明照片来源为Tom Munnecke/Getty Images，显示的期刊来源为The Kildall Family/Computer History Museum。文章由前IEEE Spectrum编辑Tekla S. Perry撰写。

---

## 5. 揭露隐匿：互联网上 MCP 服务器的地图绘制

**原文标题**: Exposing the Unseen: Mapping MCP Servers Across the Internet

**原文链接**: [https://www.knostic.ai/blog/mapping-mcp-servers-study](https://www.knostic.ai/blog/mapping-mcp-servers-study)

诺斯替研究人员发现大量不安全的MCP（元控制协议）服务器暴露在互联网上。他们使用Shodan和自定义Python工具，识别出1862台服务器，并验证了其中119台允许未经身份验证访问内部工具列表。

该研究揭示了几个关键问题：

*   **缺乏安全性：** 所有测试的服务器都不安全，许多服务器表现出不稳定和漏洞，表明技术成熟度较低。 MCP规范本身通常缺乏默认的身份验证要求。
*   **能力暴露：** 这些服务器向任何发送符合协议的握手请求的人公开其内部工具和功能。
*   **早期采用阶段：** 暴露的服务器数量相对较少，表明该技术仍处于早期采用阶段。

研究人员使用Shodan采用了一种指纹识别方法，利用协议标记、传输信号、端点路径和技术指纹。他们根据服务器标语迭代地完善了搜索过滤器并识别了模式。验证过程包括发送只读的`tools/list`请求，以确认服务器功能，而不会触发任何操作。

研究结果突显了一个重要的安全问题，因为组织机构由于不安全的MCP部署而面临暴露敏感功能的风险。该研究表明，安全性可能只有在广泛的利用之后才能得到解决，这与其他新兴技术的发展模式相似。 该研究侧重于识别暴露的服务器，并遵守道德研究规范，避免采取任何可能更改数据或产生费用的行动。

---

## 6. Root权限遇上不可变性：OpenBSD Chflags对抗日志篡改

**原文标题**: When Root Meets Immutable: OpenBSD Chflags vs. Log Tampering

**原文链接**: [https://rsadowski.de/posts/2025/openbsd-immutable-system-logs/](https://rsadowski.de/posts/2025/openbsd-immutable-system-logs/)

本文详细介绍了如何在OpenBSD中实现不可篡改的日志记录，以满足ISO 27001合规性要求，该合规性要求保护日志信息免受篡改，即使是root用户也不例外。文章认为，虽然ISO 27001没有明确要求不可篡改的日志，但该标准对防篡改日志的要求实际上使其成为必要。

作者演示了如何使用OpenBSD的`chflags`命令，特别是`sappnd` (系统追加) 和 `schg` (系统不可变) 标志来保护日志。常规日志文件被设置为`sappnd`，允许它们增长但防止修改或删除。轮换后的日志被移动到一个存档目录并设置为`schg`，使其完全不可变。

挑战在于，即使是root用户也无法删除这些标志，除非系统以较低的安全级别运行。为了自动化日志轮换，文章提出了一个使用`/etc/rc.securelevel`的解决方案，该脚本在安全级别提高之前启动期间运行。此脚本删除标志，使用`newsyslog`轮换日志，将旧日志移动到`/var/log/archive`，然后重置标志，使存档的日志不可变。这种设置在OpenBSD中提供了一个root用户无法篡改的日志记录解决方案，满足了ISO 27001对日志完整性的隐含要求。

---

## 7. 全同态加密与隐私互联网的曙光

**原文标题**: Fully homomorphic encryption and the dawn of a private internet

**原文链接**: [https://bozmen.io/fhe](https://bozmen.io/fhe)

全同态加密 (FHE)：实现隐私保护的互联网

---

## 8. 百兔号 – 低技术航海环游世界

**原文标题**: Hundred Rabbits – Low-tech living while sailing the world

**原文链接**: [https://100r.co/site/home.html](https://100r.co/site/home.html)

百兔，一对过着低技术生活方式并航行世界的夫妇，分享他们2025年1月至6月的月度更新。更新内容涵盖他们的项目、船只维护、社区参与以及读书俱乐部选书。

**项目：** 他们一直忙于软件和创意项目，包括：
*   **Uxn 生态系统：** Uxntal 文档更新、将 Modal 移植到 Uxn、开发 “Turnip Complete”（Uxn 实现指南）以及改进 HTML5 Uxn 模拟器。
*   **游戏：** 在 Playdate 目录上发布 Oquonie，开发 Flickjam（基于 Flickgame 的游戏创作挑战赛），并将 Oquonie 的资源转换为 1-bit。
*   **网站：** 使用新页面和信息更新 100r.co，使用关于急救的新页面改进 Rabbit Waves，以及发布关于摩尔斯电码和信号旗的可打印杂志。
*   **其他工具：** 发布 Nebu（电子表格编辑器和桌面日历）、改进 M291 和 Turye。

**船只维护：** 他们完成了各种任务，包括将 Pino 拖出进行擦洗和重新喷漆、纠正螺旋桨摆动、与舵轮象限作斗争、重做 Teapot 的凝胶涂层、安装更换的太阳能电池板以及通风发霉的储物柜。

**社区：** 他们参与了 Goblin Week，在 Blakely Island 与 Merveillans 会面，为其他船员提供建议和借用工具，并对他们的社区表示感谢。

**读书俱乐部：** 他们列出了每个月阅读的书籍，包括《月光之下》、《阿忒弥斯》、《金翅雀》和《你想活出怎样的人生？》等书名。

---

## 9. HathiTrust数字图书馆 - 在线书籍

**原文标题**: HathiTrust Digital Library – books online

**原文链接**: [https://www.hathitrust.org/](https://www.hathitrust.org/)

无法访问文章链接。

---

## 10. 尊敬的用户，您已进入错误页面的错误页面。

**原文标题**: Dear valued user, You have reached the error page for the error page

**原文链接**: [https://imgur.com/a/2H7HVcU](https://imgur.com/a/2H7HVcU)

此Imgur错误页面表明用户的浏览器配置存在问题，特别是JavaScript被禁用。主要信息是请求用户启用JavaScript，以使Imgur网站能够正常运行。本质上，用户看到此页面是因为Imgur依赖JavaScript来提供其预期功能，如果没有它，网站就无法按预期运行。页面本身突出显示了核心信息：Imgur需要JavaScript。除此之外没有其他内容，暗示该网站的魔力（指其内容和功能）在未启用JavaScript的情况下无法访问。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 2 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 3 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 4 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 5 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 6 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 7 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 8 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 9 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 10 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 11 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 12 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 13 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 14 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 15 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 16 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 17 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 18 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 19 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 20 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 21 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 22 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 23 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 24 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 25 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 26 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 27 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 28 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 29 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 30 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 31 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 32 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 33 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 34 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 35 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 36 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 37 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 38 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 39 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 40 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 41 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 42 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 43 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 44 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 45 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 46 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 47 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 48 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 49 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 50 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 51 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 52 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 53 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 54 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 55 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 56 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 57 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 58 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 59 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 60 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 61 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 62 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 63 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 64 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 65 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 66 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 67 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 68 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 69 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 70 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 71 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 72 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 73 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 74 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 75 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 76 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 77 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 78 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 79 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 80 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 81 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 82 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 83 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 84 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 85 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 86 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 87 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 88 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 89 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 90 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 91 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 92 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 93 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 94 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 95 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 96 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 97 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 98 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 99 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 100 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 101 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 102 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 103 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 104 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 105 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 106 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 107 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 108 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 109 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 110 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 111 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 112 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 113 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 114 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 115 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 116 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 117 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 118 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 119 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 120 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 121 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
