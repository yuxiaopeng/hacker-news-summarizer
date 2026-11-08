# Hacker News 热门文章摘要 (2026-11-08)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 高盛正撤回面向其银行家和交易员的 Claude Code

**原文标题**: Goldman Sachs Is Pulling Claude Code from Its Bankers and Traders

**原文链接**: [https://www.thestateofai.com/news/goldman-sachs-claude-code-traders-bankers](https://www.thestateofai.com/news/goldman-sachs-claude-code-traders-bankers)

高盛已将 AI 编程工具（包括 Anthropic 的 Claude Code 和微软旗下的 GitHub）的使用权限缩减至仅限其 1.2 万名工程师。这一政策取消了银行家和交易员的使用权限，此前他们已开始利用这些工具监测客户资金流并构建市场模型。

此举标志着高盛立场较今年早些时候发生了转变，当时首席信息官马尔科·阿根蒂（Marco Argenti）曾称赞“氛围编程”（vibe coding）——即非技术人员构建自用工具的行为。高盛此次立场逆转主要源于以下几点担忧：

*   **风险与监督：** 与工程师编写的代码不同，交易员创建的脚本往往绕过了正式的审查和测试。如果 AI 生成的代码在处理异常市场情况时出错，将带来财务损失风险。
*   **合规性：** AI 代理可能会突破隔离不同银行业务职能的法定信息壁垒（“中国墙”）。
*   **运营安全：** 编程代理可以在含有敏感客户数据的机器上自主编写并执行程序。
*   **成本：** 这些工具按 Token 计费；在大型机构中若不加控制地使用，可能导致巨额且难以预见的支出。

这一变动的时机尤其引人注目，因为高盛正是 Anthropic 即将进行的 IPO 的主承销商。在高盛收紧权限的同时，巴克莱银行等竞争对手则反其道而行之，正在扩大 Claude Code 的使用范围以提升开发效率。

归根结底，这一限制反映了受严格监管的行业中日益增长的诉求：即确保 AI 生成的软件必须接受专业的工程控制。尽管此举令部分员工感到沮丧，但它凸显了 AI 的快速普及与交易大厅严苛安全标准之间的冲突。

---

## 2. 我如何对抗 AI 脑疲劳

**原文标题**: How I Fight AI Brain Fry

**原文链接**: [https://sergeykuhne.com/blog/fighting-ai-brain-fry](https://sergeykuhne.com/blog/fighting-ai-brain-fry)

在《我如何对抗 AI 大脑疲劳》（How I Fight AI Brain Fry）一文中，作者探讨了因同时处理多个并发的 AI 对话线程和终端上下文而导致的认知超负荷——即“大脑疲劳”问题。为了解决高速 AI 开发中固有的精疲力竭和注意力破碎问题，作者从瞬时的对话会话转向了结构化的、集成 Git 的**优先级队列**。

**系统的核心组件：**
*   **基于 Git 的工作流：** 每一项任务都以 Markdown 文件的形式记录在代码库中。这确保了项目状态是已提交的记录，而非仅存在于对话窗口或用户的记忆中。
*   **智能代理处理：** 由 AI 代理负责处理重复性的“循环”，包括研究工单、在分支上构建代码以及运行测试。关键在于，代理被禁止做出最终决策或部署到生产环境。
*   **所有者收件箱：** 通过脚本解析 Git 看板，为用户呈现一份需要人工判断的优先级清单，例如代码审查或架构权衡。
*   **简化的审查界面：** 作者不再翻阅终端历史记录，而是利用 Claude Artifact（一个基于 Git 重建的单页仪表板）来审查变更并给出裁定。

**心理层面的益处：**
该策略的核心在于“上下文闭合”。通过加载一个工单、做出决定并立即将其返回队列，作者卸下了记忆未完成任务的心理负担。这种“一次只做一件事”的方法防止了心理“内存”溢满，从而在没有多任务干扰的情况下实现深度专注。尽管工作依然繁重，但该系统建立了一种可持续的线性工作流，防止开发者在复杂的 AI 驱动开发中迷失方向。

---

## 3. Dux: Free, open-source Wayland desktop shell with file manager and theming

**原文标题**: Dux: Free, open-source Wayland desktop shell with file manager and theming

**原文链接**: [https://duxlabs.dev/](https://duxlabs.dev/)

生成摘要时出错

---

## 4. 英伟达董事会正在调查黄仁勋

**原文标题**: Nvidia Board of Directors Is Investigating Jensen Huang

**原文链接**: [https://nvidianews.nvidia.com/news/statement-from-nvidia-board-of-directors](https://nvidianews.nvidia.com/news/statement-from-nvidia-board-of-directors)

2026年11月8日，英伟达（NVIDIA）董事会宣布对创始人兼首席执行官黄仁勋启动一项独立调查。此次调查源于有报道称，黄仁勋曾是外国情报活动的目标。

该调查由独立董事委员会在外部法律顾问的协助下进行监督。董事会强调，其首要任务是维护美国的国家安全和经济安全。

声明的关键细节包括：
*   **目前调查结果：** 董事会目前没有理由认为英伟达的专有机密或国家安全已遭到损害。
*   **配合情况：** 黄仁勋对此次审查表示全力支持，并正配合委员会的工作。
*   **领导地位：** 在调查进行期间，董事会维持对黄仁勋及其领导团队的信心。

董事会承诺将随着调查的进展提供进一步的更新。

---

## 5. Outlook.com 正悄悄拦截未配置 DMARC 域名的邮件

**原文标题**: Outlook.com Is Quietly Rejecting Email from Domains Without DMARC

**原文链接**: [https://mailroute.net/blog/outlook-rejecting-email-without-dmarc](https://mailroute.net/blog/outlook-rejecting-email-without-dmarc)

Beginning November 5, 2024, Microsoft’s consumer email services—including Outlook.com, Hotmail, Live, and MSN—began quietly rejecting emails from domains that do not have a DMARC record. Unlike previous mandates targeting bulk senders (those sending over 5,000 messages daily), this change affects small, low-volume senders and was implemented without an official announcement.

**Key Issues**
The primary danger of this update is its inconsistency. Microsoft is only rejecting a portion of affected traffic, meaning some emails pass through while others bounce with a "550 5.7.1" error. This intermittent failure makes the problem difficult to detect, as senders may assume a one-time glitch while recipients remain unaware that messages were sent. Even domains with functional SPF and DKIM records are being blocked if they lack the DMARC record that ties those protocols to the "From" address.

**The Solution**
The immediate fix is to add a single TXT record to the domain's DNS:
`v=DMARC1; p=none`

The `p=none` policy is a "safe" entry that satisfies Microsoft’s requirement without altering how other email providers handle the mail. However, for DMARC to work, the sender must also ensure that either SPF or DKIM is correctly configured and aligned with their "From" domain.

**The Broader Context**
This shift reflects a growing industry trend where major mailbox providers are making DMARC the baseline requirement for all email, not just bulk marketing. While currently a hurdle for small businesses, implementing DMARC is a critical step in preventing domain spoofing and improving overall email security. Senders are encouraged to add the record immediately to avoid delivery disruptions.

---

## 6. 声明式拖拽

**原文标题**: Declarative Dragging

**原文链接**: [https://declarative-dragging.github.io/](https://declarative-dragging.github.io/)

由 Joshua Horowitz、Andrew Blinn 和 Jeffrey Heer 撰写的 UIST 2026 最佳论文 **Declarative Dragging**（声明式拖拽）提出了一种创建拖放交互的新颖方法。传统上，构建此类功能是一个“琐碎且繁杂”的过程，需要为几何图形和动画编写复杂的代码。Declarative Dragging (D2) 通过让开发者指定**未来的模型状态**而非手动定义视觉行为，简化了这一过程。

其核心机制涉及一个能够推测性地渲染应用程序潜在未来状态的引擎。通过识别被拖拽元素在这些推测渲染中出现的位置，系统会自动合成流畅且响应迅速的交互。这使开发者的重心从底层的坐标操作转向了高层的语义规则。

作者在 **Dragology** 中实现了这一概念，这是一个针对 SVG Web 界面的库。Dragology 采用模型驱动且具备可组合性，允许用户叠加吸附（snapping）、漂浮（floating）和过渡（transitions）等功能。该系统对于“并行表示”特别有效，即当用户与系统的一个视图（如数学排列）交互时，可以实时流利地更新其他视图。

该项目源于将数字数学和编程变得更加“触感化”的愿景。它已被应用于多个领域，包括：
*   **教育与数学：** 可视化扭曲树、代数和辫子理论（braid theory）。
*   **游戏设计：** 利用 3D 环境和游戏手柄的具身数学游戏。
*   **软件开发：** 集成到学术编程环境“Hazel”中，使代码重构可以通过触控进行探索。

通过降低丰富触觉交互的实现门槛，Declarative Dragging 使教育工作者、研究人员和创意工具开发者能够创建更具表现力、更“生动”（juicy）的界面，而无需承担传统复杂几何编程的额外负担。

---

## 7. RAM Altman：Linux 脚本每天向 Sam Altman 汇报你电脑中的闲置内存量

**原文标题**: RAM Altman: Linux Script Emails Sam Altman Daily How Much Unused RAM in Your PC

**原文链接**: [https://respawnfirst.com/linux-script-emails-sam-altman-unused-ram-ram-altman/](https://respawnfirst.com/linux-script-emails-sam-altman-unused-ram-ram-altman/)

针对 OpenAI 首席执行官萨姆·奥特曼（Sam Altman）关于优先满足 AI 数据中心需求而非消费电子产品的争议性言论，开源开发者伊恩·凯（Iain Kay）发布了一款名为“Ram Altman”的 Linux BASH 脚本。

该脚本旨在监控系统的空闲内存。如果未使用内存超过 10%，该工具会从一系列讽刺性的邮件模板中进行选择并发送给奥特曼，以嘲讽其“超级大反派”般的言论。其中一封示例邮件告知奥特曼，用户正将特定容量的内存“负责任地囤积”在书桌上，而非投入到数据中心。

为防止该工具被用于针对 OpenAI 的自动化邮件伪造或拒绝服务攻击，凯特意将邮件服务器设为默认未配置状态。用户必须具备自行设置外发邮件的技术能力，不过该代码库包含了一个用于本地测试的“空运行”（dry-run）标志，以及一个嘲讽苹果焊接内存和全球 DRAM 短缺的幽默问答（FAQ）板块。

“Ram Altman”项目突显了互联网对 OpenAI 硬件立场的强烈抵制。在该脚本发布并引发广泛批评后，奥特曼在 X（原 Twitter）上改口，声称其原始言论被断章取义，并坚称他希望消费者能够拥有所需的全部硬件。

---

## 8. Llama-modchip: 284B DeepSeek on 64GB RAM, no GPU

**原文标题**: Llama-modchip: 284B DeepSeek on 64GB RAM, no GPU

**原文链接**: [https://github.com/synchopate/llama-modchip](https://github.com/synchopate/llama-modchip)

生成摘要时出错

---

## 9. 爱德华·霍普的标志性画作《夜游者》

**原文标题**: Edward Hopper's Iconic Painting, "Nighthawks

**原文链接**: [https://lithub.com/the-story-behind-edward-hoppers-iconic-painting-nighthawks/](https://lithub.com/the-story-behind-edward-hoppers-iconic-painting-nighthawks/)

In this excerpt from *Edward Hopper: A Life*, Louis Shadwick explores the creation, context, and enduring legacy of Hopper’s most famous painting, *Nighthawks*. 

**Process and Inspiration**
Started in late 1941, the painting was a product of meticulous planning, involving nineteen preparatory sketches. Hopper and his wife, Jo, modeled for the figures in the diner. While art historians have long searched for the exact location of the restaurant on Greenwich Avenue, Shadwick suggests the diner is likely an amalgamation of several New York landmarks—including "Crawford Lunch" and the Flatiron Building—designed to create a stylized, "fishbowl" aesthetic.

**Wartime Context**
The painting’s production coincided with the United States' entry into World War II following the attack on Pearl Harbor. Letters from Jo Hopper reveal a period of intense anxiety, marked by fears of New York being bombed and the enforcement of nightly blackouts. Shadwick argues that Hopper’s obsession with the canvas served as both a distraction and a response to this tension. The diner, glowing with artificial light amidst the darkness, symbolizes a "poignantly American resilience" and a gesture of endurance during the nation’s darkest hours.

**Themes and Legacy**
Though *Nighthawks* is frequently cited as the definitive portrayal of modern loneliness and urban alienation, Hopper himself felt these interpretations were "overdone," preferring the painting’s emotional depth to remain unformulated. Shadwick highlights how the work bridges European influences—such as Van Gogh’s night scenes and Surrealist mystery—with a uniquely American realist tradition. Ultimately, the painting captures a sense of "heroic isolation" and Emersonian self-reliance, turning the "quiet menace" of the city into something iconic, stoic, and alluring.

---

## 10. 作为思考工具的写作

**原文标题**: Writing as a thinking tool

**原文链接**: [http://muratbuffalo.blogspot.com/2026/11/writing-as-thinking-tool.html](http://muratbuffalo.blogspot.com/2026/11/writing-as-thinking-tool.html)

生成摘要时出错

---

## 11. A Little Snitch for Windows

**原文标题**: A Little Snitch for Windows

**原文链接**: [https://packethound.app/](https://packethound.app/)

生成摘要时出错

---

## 12. Show HN: Vegetable Gardening for Engineers

**原文标题**: Show HN: Vegetable Gardening for Engineers

**原文链接**: [https://jrcpl.us/contrib/2020/gardening-for-engineers/](https://jrcpl.us/contrib/2020/gardening-for-engineers/)

生成摘要时出错

---

## 13. The Reconstruction of Torn Documents

**原文标题**: The Reconstruction of Torn Documents

**原文链接**: [https://www.bundesarchiv.de/en/stasi-records-archive/the-reconstruction-of-torn-documents/](https://www.bundesarchiv.de/en/stasi-records-archive/the-reconstruction-of-torn-documents/)

生成摘要时出错

---

## 14. I'm not a fan of Deno's security model (2024)

**原文标题**: I'm not a fan of Deno's security model (2024)

**原文链接**: [https://goldstein.lol/posts/deno-security/](https://goldstein.lol/posts/deno-security/)

生成摘要时出错

---

## 15. Goodbye Claude, hello Pi

**原文标题**: Goodbye Claude, hello Pi

**原文链接**: [https://caleb.software/posts/claude-to-pi.html](https://caleb.software/posts/claude-to-pi.html)

生成摘要时出错

---

## 16. Porting Android 16 to my blind mother's keypad phone

**原文标题**: Porting Android 16 to my blind mother's keypad phone

**原文链接**: [https://z1x.us/blog/four-hundred-bucks-of-e-waste](https://z1x.us/blog/four-hundred-bucks-of-e-waste)

生成摘要时出错

---

## 17. A field guide to CAPTCHA types and how they break

**原文标题**: A field guide to CAPTCHA types and how they break

**原文链接**: [https://github.com/vsmutok/FuckCaptcha](https://github.com/vsmutok/FuckCaptcha)

生成摘要时出错

---

## 18. Everything should be a random number generator

**原文标题**: Everything should be a random number generator

**原文链接**: [https://en.cppreference.com/cpp/numeric/random](https://en.cppreference.com/cpp/numeric/random)

生成摘要时出错

---

## 19. Playing Zork 1 on a CP/M emulator on Linux (2021)

**原文标题**: Playing Zork 1 on a CP/M emulator on Linux (2021)

**原文链接**: [https://kevinboone.me/cpmzork.html](https://kevinboone.me/cpmzork.html)

生成摘要时出错

---

## 20. Starship Flight 15 on 11/13 plans to catch both booster and ship

**原文标题**: Starship Flight 15 on 11/13 plans to catch both booster and ship

**原文链接**: [https://www.spacex.com/launches/starship-flight-15](https://www.spacex.com/launches/starship-flight-15)

生成摘要时出错

---

## 21. How to prove equations using diagrams, part 1

**原文标题**: How to prove equations using diagrams, part 1

**原文链接**: [https://www.epatters.org/post/e-graphs-1/](https://www.epatters.org/post/e-graphs-1/)

生成摘要时出错

---

## 22. What I run on my $10 USD OpenStick homelab

**原文标题**: What I run on my $10 USD OpenStick homelab

**原文链接**: [https://blog.bosscher.ch/posts/openstick/](https://blog.bosscher.ch/posts/openstick/)

生成摘要时出错

---

## 23. JIT bitmap text rendering for microcontrollers

**原文标题**: JIT bitmap text rendering for microcontrollers

**原文链接**: [https://linebender.org/blog/jit-bitmap-text/](https://linebender.org/blog/jit-bitmap-text/)

生成摘要时出错

---

## 24. Claude Code's "Don't Ask Again" exposes passwords in 1,122 public GitHub files

**原文标题**: Claude Code's "Don't Ask Again" exposes passwords in 1,122 public GitHub files

**原文链接**: [https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again](https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again)

生成摘要时出错

---

## 25. Silicon Valley Promises AI Will Cure Disease. Drugmaker CEOs Aren't Buying It

**原文标题**: Silicon Valley Promises AI Will Cure Disease. Drugmaker CEOs Aren't Buying It

**原文链接**: [https://www.wsj.com/tech/ai/silicon-valley-promises-ai-will-cure-disease-drugmaker-ceos-arent-buying-it-5218511c](https://www.wsj.com/tech/ai/silicon-valley-promises-ai-will-cure-disease-drugmaker-ceos-arent-buying-it-5218511c)

生成摘要时出错

---

## 26. Agent memory needs its OpenTelemetry moment

**原文标题**: Agent memory needs its OpenTelemetry moment

**原文链接**: [https://www.lorekit.io/blog/open-agent-memory-format](https://www.lorekit.io/blog/open-agent-memory-format)

生成摘要时出错

---

## 27. Clj.rs – a Clojure dialect implemented in Rust

**原文标题**: Clj.rs – a Clojure dialect implemented in Rust

**原文链接**: [https://clj.rs/](https://clj.rs/)

生成摘要时出错

---

## 28. Ads in Popular Apps Give Police a Powerful Tool to Spy on Users

**原文标题**: Ads in Popular Apps Give Police a Powerful Tool to Spy on Users

**原文链接**: [https://www.bloomberg.com/features/2026-police-phone-tracking-advertising-tech/](https://www.bloomberg.com/features/2026-police-phone-tracking-advertising-tech/)

生成摘要时出错

---

## 29. Petered

**原文标题**: Petered

**原文链接**: [https://aworkinglibrary.com/writing/petered](https://aworkinglibrary.com/writing/petered)

生成摘要时出错

---

## 30. The Gordon Gekko effect: The role of culture in the financial industry (2016) [pdf]

**原文标题**: The Gordon Gekko effect: The role of culture in the financial industry (2016) [pdf]

**原文链接**: [https://www.newyorkfed.org/medialibrary/media/research/epr/2016/epr_2016_gordon-gekko-effect_lo.pdf](https://www.newyorkfed.org/medialibrary/media/research/epr/2016/epr_2016_gordon-gekko-effect_lo.pdf)

生成摘要时出错

---

## 31. Person of Interest

**原文标题**: Person of Interest

**原文链接**: [https://krthr.co/person-of-interest/](https://krthr.co/person-of-interest/)

生成摘要时出错

---

## 32. Tasfer: a text editor drawn on a 2D canvas

**原文标题**: Tasfer: a text editor drawn on a 2D canvas

**原文链接**: [https://www.hamza.se/blog/tasfer](https://www.hamza.se/blog/tasfer)

生成摘要时出错

---

## 33. MaxxBench – "Nice DeepSWE score. But is it true?"

**原文标题**: MaxxBench – "Nice DeepSWE score. But is it true?"

**原文链接**: [https://maxxbench.unlap.ai/research/why-maxxbench/](https://maxxbench.unlap.ai/research/why-maxxbench/)

生成摘要时出错

---

## 34. Uranium cubes reveal why the German nuclear project failed

**原文标题**: Uranium cubes reveal why the German nuclear project failed

**原文链接**: [https://arstechnica.com/science/2026/11/uranium-cubes-reveal-why-the-german-nuclear-project-failed/](https://arstechnica.com/science/2026/11/uranium-cubes-reveal-why-the-german-nuclear-project-failed/)

生成摘要时出错

---

## 35. Finding Xanadu: Inside a JRPG classic translation 15 years in the making

**原文标题**: Finding Xanadu: Inside a JRPG classic translation 15 years in the making

**原文链接**: [https://readonlymemo.com/legend-of-xanadu-pc-engine-fan-translation-interview-making-of/](https://readonlymemo.com/legend-of-xanadu-pc-engine-fan-translation-interview-making-of/)

生成摘要时出错

---

## 36. Making any integer with four 2s (2025)

**原文标题**: Making any integer with four 2s (2025)

**原文链接**: [https://eli.thegreenplace.net/2025/making-any-integer-with-four-2s/](https://eli.thegreenplace.net/2025/making-any-integer-with-four-2s/)

生成摘要时出错

---

## 37. New typeface using intricate designs from Shakespeare's First Folio (2023)

**原文标题**: New typeface using intricate designs from Shakespeare's First Folio (2023)

**原文链接**: [https://www.itsnicethat.com/news/typeland-shakespeares-globe-amifer-folio-graphic-design-090323](https://www.itsnicethat.com/news/typeland-shakespeares-globe-amifer-folio-graphic-design-090323)

生成摘要时出错

---

## 38. Mizu – zero-copy parallel R and Python over shared memory

**原文标题**: Mizu – zero-copy parallel R and Python over shared memory

**原文链接**: [https://github.com/shikokuchuo/pymizu](https://github.com/shikokuchuo/pymizu)

生成摘要时出错

---

## 39. ISponsorBlockTV: SponsorBlock client for all YouTube TV clients

**原文标题**: ISponsorBlockTV: SponsorBlock client for all YouTube TV clients

**原文链接**: [https://github.com/dmunozv04/isponsorblocktv](https://github.com/dmunozv04/isponsorblocktv)

生成摘要时出错

---

## 40. Show HN: Coldframe, a honeypot that poses as a supermarket fridge controller

**原文标题**: Show HN: Coldframe, a honeypot that poses as a supermarket fridge controller

**原文链接**: [https://github.com/hedgerow-dev/coldframe](https://github.com/hedgerow-dev/coldframe)

生成摘要时出错

---

## 41. Nyquist Limit:The frequency of changes in tech is invalidating our understanding

**原文标题**: Nyquist Limit:The frequency of changes in tech is invalidating our understanding

**原文链接**: [https://www.ryanprior.com/posts/nyquist-limit-frequency-of-changes-in-tech-invalidates-understanding/](https://www.ryanprior.com/posts/nyquist-limit-frequency-of-changes-in-tech-invalidates-understanding/)

生成摘要时出错

---

## 42. GitHub New pull request overview page in public preview

**原文标题**: GitHub New pull request overview page in public preview

**原文链接**: [https://github.blog/changelog/2026-11-05-new-pull-request-overview-page-in-public-preview/](https://github.blog/changelog/2026-11-05-new-pull-request-overview-page-in-public-preview/)

生成摘要时出错

---

## 43. PDP-8/E Restoration Log

**原文标题**: PDP-8/E Restoration Log

**原文链接**: [https://www.ricomputermuseum.org/collections-gallery/equipment/dec-pdp-8e/pdp-8e-restoration-log](https://www.ricomputermuseum.org/collections-gallery/equipment/dec-pdp-8e/pdp-8e-restoration-log)

生成摘要时出错

---

## 44. Fishermen find Royal Caribbean cruise ship employee in water 20 miles off coast

**原文标题**: Fishermen find Royal Caribbean cruise ship employee in water 20 miles off coast

**原文链接**: [https://www.cbsnews.com/losangeles/news/newport-beach-fishermen-find-man-treading-water-royal-caribbean-cruise-ship-employee/](https://www.cbsnews.com/losangeles/news/newport-beach-fishermen-find-man-treading-water-royal-caribbean-cruise-ship-employee/)

生成摘要时出错

---

## 45. Nvidia Board to Probe Spying Case After CEO Admits Affair

**原文标题**: Nvidia Board to Probe Spying Case After CEO Admits Affair

**原文链接**: [https://www.bloomberg.com/news/articles/2026-11-08/nvidia-board-to-probe-spying-case-after-ceo-jensen-huang-admits-infidelity](https://www.bloomberg.com/news/articles/2026-11-08/nvidia-board-to-probe-spying-case-after-ceo-jensen-huang-admits-infidelity)

生成摘要时出错

---

## 46. Consumer brain wave headsets threaten privacy

**原文标题**: Consumer brain wave headsets threaten privacy

**原文链接**: [https://www.science.org/content/article/wearable-device-makers-are-harvesting-brain-data-train-ai-without-telling-users?referrer=https%3A%2F%2Fwww.google.com%2F](https://www.science.org/content/article/wearable-device-makers-are-harvesting-brain-data-train-ai-without-telling-users?referrer=https%3A%2F%2Fwww.google.com%2F)

生成摘要时出错

---

## 47. The efficiency trap: why optimising everything can backfire, badly

**原文标题**: The efficiency trap: why optimising everything can backfire, badly

**原文链接**: [https://www.theguardian.com/books/2026/nov/08/the-efficiency-trap-why-optimising-everything-can-backfire-badly](https://www.theguardian.com/books/2026/nov/08/the-efficiency-trap-why-optimising-everything-can-backfire-badly)

生成摘要时出错

---

## 48. Systemd Loves Rust

**原文标题**: Systemd Loves Rust

**原文链接**: [https://amutable.com/blog/systemd-loves-rust](https://amutable.com/blog/systemd-loves-rust)

生成摘要时出错

---

## 49. Kirlian Photography: Building Your Own Equipment

**原文标题**: Kirlian Photography: Building Your Own Equipment

**原文链接**: [https://imagesco.com/articles/kirlian/kirlian-photography.html](https://imagesco.com/articles/kirlian/kirlian-photography.html)

生成摘要时出错

---

## 50. WaveDudeNext 2D Wave Simulator

**原文标题**: WaveDudeNext 2D Wave Simulator

**原文链接**: [https://github.com/graealex/WaveDudeNext](https://github.com/graealex/WaveDudeNext)

生成摘要时出错

---

## 51. The $8 Linux Computer (2022)

**原文标题**: The $8 Linux Computer (2022)

**原文链接**: [http://thelittleengineerthatcould.blogspot.com/2022/12/the-8-linux-computer.html](http://thelittleengineerthatcould.blogspot.com/2022/12/the-8-linux-computer.html)

生成摘要时出错

---

## 52. Drones built to look like birds evaded detection at Air Force tech exercise

**原文标题**: Drones built to look like birds evaded detection at Air Force tech exercise

**原文链接**: [https://taskandpurpose.com/news/drone-mimicking-bird-test/](https://taskandpurpose.com/news/drone-mimicking-bird-test/)

生成摘要时出错

---

## 53. Amsterdam School

**原文标题**: Amsterdam School

**原文链接**: [https://architecture-history.org/schools/AMSTERDAM%20SCHOOL.html](https://architecture-history.org/schools/AMSTERDAM%20SCHOOL.html)

生成摘要时出错

---

## 54. The end of Microsoft Research's AI Frontiers group

**原文标题**: The end of Microsoft Research's AI Frontiers group

**原文链接**: [https://hunch.net/?p=13764006](https://hunch.net/?p=13764006)

生成摘要时出错

---

## 55. Apple’s grey list: Words and phrases your iPhone won’t help you spell

**原文标题**: Apple’s grey list: Words and phrases your iPhone won’t help you spell

**原文链接**: [https://www.theguardian.com/technology/2026/nov/06/struggling-to-spell-male-chauvinist-pig-apple-grey-list-means-your-iphone-wont-help-you](https://www.theguardian.com/technology/2026/nov/06/struggling-to-spell-male-chauvinist-pig-apple-grey-list-means-your-iphone-wont-help-you)

生成摘要时出错

---

## 56. Running a law firm on Free software

**原文标题**: Running a law firm on Free software

**原文链接**: [https://decoded.legal/blog/2026/11/running-a-law-firm-on-free-software-2026-edition/](https://decoded.legal/blog/2026/11/running-a-law-firm-on-free-software-2026-edition/)

生成摘要时出错

---

## 57. Every processor die anyone has photographed and given away

**原文标题**: Every processor die anyone has photographed and given away

**原文链接**: [https://sheets.works/data-viz/cpu-dies](https://sheets.works/data-viz/cpu-dies)

生成摘要时出错

---

## 58. We know 15k websites are infected. how do we tell them?

**原文标题**: We know 15k websites are infected. how do we tell them?

**原文链接**: [https://scotthelme.co.uk/we-know-15-579-websites-are-infected-how-do-we-tell-them/](https://scotthelme.co.uk/we-know-15-579-websites-are-infected-how-do-we-tell-them/)

生成摘要时出错

---

## 59. Commodore PET – The Worlds First Personal Computer

**原文标题**: Commodore PET – The Worlds First Personal Computer

**原文链接**: [https://www.commodore.ca/commodore-products/commodore-pet-the-worlds-first-personal-computer/](https://www.commodore.ca/commodore-products/commodore-pet-the-worlds-first-personal-computer/)

生成摘要时出错

---

## 60. Need for Speed Underground 2 online in the browser

**原文标题**: Need for Speed Underground 2 online in the browser

**原文链接**: [https://nfsu2.xyz/](https://nfsu2.xyz/)

生成摘要时出错

---

## 61. Five memorable books about programming (2008)

**原文标题**: Five memorable books about programming (2008)

**原文链接**: [https://prog21.dadgum.com/19.html](https://prog21.dadgum.com/19.html)

生成摘要时出错

---

## 62. OpenAI raises $11B at a $1.25T valuation

**原文标题**: OpenAI raises $11B at a $1.25T valuation

**原文链接**: [https://247wallst.com/investing/2026/11/07/openai-just-raised-11-billion-at-a-1-25-trillion-valuation-below-the-1-4-trillion-it-first-sought/](https://247wallst.com/investing/2026/11/07/openai-just-raised-11-billion-at-a-1-25-trillion-valuation-below-the-1-4-trillion-it-first-sought/)

生成摘要时出错

---

## 63. Quadrillion-parameter transformers and how to train them

**原文标题**: Quadrillion-parameter transformers and how to train them

**原文链接**: [https://qlabs.sh/research/parameters](https://qlabs.sh/research/parameters)

生成摘要时出错

---

## 64. Text.js: Build full-stack React apps that render inside console.log

**原文标题**: Text.js: Build full-stack React apps that render inside console.log

**原文链接**: [https://textjs.org/](https://textjs.org/)

生成摘要时出错

---

## 65. The Components of Agent Memory

**原文标题**: The Components of Agent Memory

**原文链接**: [https://www.anthropic.com/research/components-of-agent-memory](https://www.anthropic.com/research/components-of-agent-memory)

生成摘要时出错

---

## 66. How Long Can Life Wait?

**原文标题**: How Long Can Life Wait?

**原文链接**: [https://mceglowski.substack.com/p/how-long-can-life-wait](https://mceglowski.substack.com/p/how-long-can-life-wait)

生成摘要时出错

---

## 67. GeoWorks, Microsoft Windows' Upstart '90s Competitor (2016)

**原文标题**: GeoWorks, Microsoft Windows' Upstart '90s Competitor (2016)

**原文链接**: [https://www.atlasobscura.com/articles/the-history-of-geoworks-microsoft-windows-upstart-90s-competitor](https://www.atlasobscura.com/articles/the-history-of-geoworks-microsoft-windows-upstart-90s-competitor)

生成摘要时出错

---

## 68. Libghostty 1.0

**原文标题**: Libghostty 1.0

**原文链接**: [https://mitchellh.com/writing/libghostty-1-0](https://mitchellh.com/writing/libghostty-1-0)

生成摘要时出错

---

## 69. Terry Pratchett's Study

**原文标题**: Terry Pratchett's Study

**原文链接**: [https://www.sussi.dk/terry-pratchetts-study](https://www.sussi.dk/terry-pratchetts-study)

生成摘要时出错

---

## 70. What do the next 4000 emoji look like?

**原文标题**: What do the next 4000 emoji look like?

**原文链接**: [https://jenniferdaniel.substack.com/p/what-do-the-next-4000-emoji-look](https://jenniferdaniel.substack.com/p/what-do-the-next-4000-emoji-look)

生成摘要时出错

---

## 71. Every Windows 11 app should kill Electron, and Discord just showed why

**原文标题**: Every Windows 11 app should kill Electron, and Discord just showed why

**原文链接**: [https://www.windowslatest.com/2026/11/06/every-windows-11-app-should-kill-electron-and-discord-just-showed-why-no-starting-screen-and-70-less-ram-even-with-two-accounts-signed-in/](https://www.windowslatest.com/2026/11/06/every-windows-11-app-should-kill-electron-and-discord-just-showed-why-no-starting-screen-and-70-less-ram-even-with-two-accounts-signed-in/)

生成摘要时出错

---

## 72. Every Mac comes with an (undocumented) family member classifier

**原文标题**: Every Mac comes with an (undocumented) family member classifier

**原文链接**: [https://8rank.ai/game/apple-intelligence-personal-knowledge-graph](https://8rank.ai/game/apple-intelligence-personal-knowledge-graph)

生成摘要时出错

---

## 73. Retro Song Bird: Plug in any Game Boy cartridge to hear the soundtrack

**原文标题**: Retro Song Bird: Plug in any Game Boy cartridge to hear the soundtrack

**原文链接**: [https://www.retrosongbird.com/](https://www.retrosongbird.com/)

生成摘要时出错

---

## 74. Turning every radio into a radar

**原文标题**: Turning every radio into a radar

**原文链接**: [https://tiaminetworks.com/turning-every-radio-into-a-radar/](https://tiaminetworks.com/turning-every-radio-into-a-radar/)

生成摘要时出错

---

## 75. Etsy changes terms to train AI on your creations, while blocking you doing it [video]

**原文标题**: Etsy changes terms to train AI on your creations, while blocking you doing it [video]

**原文链接**: [https://www.youtube.com/watch?v=zrlLUUdqDJI](https://www.youtube.com/watch?v=zrlLUUdqDJI)

生成摘要时出错

---

## 76. Multi-Column Different-Speed Scrolling

**原文标题**: Multi-Column Different-Speed Scrolling

**原文链接**: [https://blog.master.dev/multi-column-different-speed-scrolling/](https://blog.master.dev/multi-column-different-speed-scrolling/)

生成摘要时出错

---

## 77. IRA Velinsky – Commodore's Industrial Designer

**原文标题**: IRA Velinsky – Commodore's Industrial Designer

**原文链接**: [https://www.commodore.ca/commodore-history/ira-velinsky-commodores-amazing-industrial-designer/](https://www.commodore.ca/commodore-history/ira-velinsky-commodores-amazing-industrial-designer/)

生成摘要时出错

---

## 78. Show HN: Where Were We

**原文标题**: Show HN: Where Were We

**原文链接**: [https://wherewerewe.app/](https://wherewerewe.app/)

生成摘要时出错

---

## 79. Earliest evidence of cannabis use found in ancient Siberian tomb

**原文标题**: Earliest evidence of cannabis use found in ancient Siberian tomb

**原文链接**: [https://www.cnn.com/2026/11/05/science/ancient-cannabis-siberia-scli-intl](https://www.cnn.com/2026/11/05/science/ancient-cannabis-siberia-scli-intl)

生成摘要时出错

---

## 80. sshole

**原文标题**: sshole

**原文链接**: [https://sshhole.com](https://sshhole.com)

生成摘要时出错

---

## 81. UK House of Lords to propose mandatory CSAM detection software on smartphones

**原文标题**: UK House of Lords to propose mandatory CSAM detection software on smartphones

**原文链接**: [https://observer.co.uk/news/national/article/fight-to-block-child-sexual-abuse-images-unites-peers-and-mps-in-cross-party-campaign](https://observer.co.uk/news/national/article/fight-to-block-child-sexual-abuse-images-unites-peers-and-mps-in-cross-party-campaign)

生成摘要时出错

---

## 82. Firecracker VM Escape: PwnEscape Part 2

**原文标题**: Firecracker VM Escape: PwnEscape Part 2

**原文链接**: [https://pwn.ai/blog/firecracker-escape](https://pwn.ai/blog/firecracker-escape)

生成摘要时出错

---

## 83. Sunshine Atlas – the climate of 3,833 destinations, month by month

**原文标题**: Sunshine Atlas – the climate of 3,833 destinations, month by month

**原文链接**: [https://sunshineatlas.com/](https://sunshineatlas.com/)

生成摘要时出错

---

## 84. Anthropic strikes $3.4B deal to generate gas-fired power for data centres

**原文标题**: Anthropic strikes $3.4B deal to generate gas-fired power for data centres

**原文链接**: [https://www.ft.com/content/41bf5c6a-9735-4f1a-a8e3-2bcccad58ba0](https://www.ft.com/content/41bf5c6a-9735-4f1a-a8e3-2bcccad58ba0)

生成摘要时出错

---

## 85. ToothPaste

**原文标题**: ToothPaste

**原文链接**: [https://brisk4t.github.io/blog/toothpaste/](https://brisk4t.github.io/blog/toothpaste/)

生成摘要时出错

---

## 86. UpCodes (YC S17) is hiring SDR's to sell AI compliance software

**原文标题**: UpCodes (YC S17) is hiring SDR's to sell AI compliance software

**原文链接**: [https://up.codes/careers?utm_source=HN](https://up.codes/careers?utm_source=HN)

生成摘要时出错

---

## 87. Show HN: We compressed a 31B video+audio diffusion model to 14B, 6 steps, INT8

**原文标题**: Show HN: We compressed a 31B video+audio diffusion model to 14B, 6 steps, INT8

**原文链接**: [https://github.com/Video-Rebirth/hyperflow-h3-flash](https://github.com/Video-Rebirth/hyperflow-h3-flash)

生成摘要时出错

---

## 88. Claude Code sends your email address to websites

**原文标题**: Claude Code sends your email address to websites

**原文链接**: [https://github.com/anthropics/claude-code/issues/107757](https://github.com/anthropics/claude-code/issues/107757)

生成摘要时出错

---

## 89. Show HN: Maple – Sub-2-BPW Moe Pruning to Run Gemma 4 26B at 45 TPS on a 6GB GPU

**原文标题**: Show HN: Maple – Sub-2-BPW Moe Pruning to Run Gemma 4 26B at 45 TPS on a 6GB GPU

**原文链接**: [https://github.com/AmSach/maple](https://github.com/AmSach/maple)

生成摘要时出错

---

## 90. GitHub's new Git storage architecture

**原文标题**: GitHub's new Git storage architecture

**原文链接**: [https://github.blog/engineering/architecture-optimization/inside-githubs-new-git-storage-architecture/](https://github.blog/engineering/architecture-optimization/inside-githubs-new-git-storage-architecture/)

生成摘要时出错

---

## 91. Asahi Linux Progress Linux 7.3

**原文标题**: Asahi Linux Progress Linux 7.3

**原文链接**: [https://asahilinux.org/2026/11/progress-report-7-3/](https://asahilinux.org/2026/11/progress-report-7-3/)

生成摘要时出错

---

## 92. Nvidia Opens Investigation into Jensen Huang's Relationship with Chinese Spy

**原文标题**: Nvidia Opens Investigation into Jensen Huang's Relationship with Chinese Spy

**原文链接**: [https://www.nytimes.com/2026/11/08/technology/nvidia-investigation-jensen-huang-china.html](https://www.nytimes.com/2026/11/08/technology/nvidia-investigation-jensen-huang-china.html)

生成摘要时出错

---

## 93. ZapFast: A fast, native WhatsApp client in Rust and egui

**原文标题**: ZapFast: A fast, native WhatsApp client in Rust and egui

**原文链接**: [https://github.com/crmne/zapfast](https://github.com/crmne/zapfast)

生成摘要时出错

---

## 94. Notes on San Marino

**原文标题**: Notes on San Marino

**原文链接**: [https://mattlakeman.org/2026/11/05/notes-on-san-marino/](https://mattlakeman.org/2026/11/05/notes-on-san-marino/)

生成摘要时出错

---

## 95. Yes, You Can Pass a Nuclear Missile Driving on Interstate 80 Through Wyoming

**原文标题**: Yes, You Can Pass a Nuclear Missile Driving on Interstate 80 Through Wyoming

**原文链接**: [https://cowboystatedaily.com/2026/11/04/yes-you-can-pass-a-nuclear-missile-driving-on-interstate-80-through-wyoming/](https://cowboystatedaily.com/2026/11/04/yes-you-can-pass-a-nuclear-missile-driving-on-interstate-80-through-wyoming/)

生成摘要时出错

---

## 96. A barbarian tribe's mythic origin story is true, ancient DNA reveals

**原文标题**: A barbarian tribe's mythic origin story is true, ancient DNA reveals

**原文链接**: [https://www.science.org/content/article/barbarian-tribe-s-mythic-origin-story-true-ancient-dna-reveals](https://www.science.org/content/article/barbarian-tribe-s-mythic-origin-story-true-ancient-dna-reveals)

生成摘要时出错

---

## 97. Tesla to wind down Cybertruck production

**原文标题**: Tesla to wind down Cybertruck production

**原文链接**: [https://www.nbcnews.com/tech/tech-news/tesla-wind-cybertruck-production-years-poor-sales-markets-rcna607817](https://www.nbcnews.com/tech/tech-news/tesla-wind-cybertruck-production-years-poor-sales-markets-rcna607817)

生成摘要时出错

---

## 98. First steps in bare-metal programming using UEFI

**原文标题**: First steps in bare-metal programming using UEFI

**原文链接**: [https://kevinboone.me/efitest_index.html](https://kevinboone.me/efitest_index.html)

生成摘要时出错

---

## 99. A Jev that can ask Opus for help gives Opus accuracy at 4x lower cost

**原文标题**: A Jev that can ask Opus for help gives Opus accuracy at 4x lower cost

**原文链接**: [https://hightouch.com/blog/llm-judges-identity-resolution](https://hightouch.com/blog/llm-judges-identity-resolution)

生成摘要时出错

---

## 100. 8088 Domination Post-Mortem

**原文标题**: 8088 Domination Post-Mortem

**原文链接**: [https://trixter.oldskool.org/2014/06/19/8088-domination-post-mortem-part-1/](https://trixter.oldskool.org/2014/06/19/8088-domination-post-mortem-part-1/)

生成摘要时出错

---

