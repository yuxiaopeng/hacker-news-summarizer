# Hacker News 热门文章摘要 (2025-07-22)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 为何事实无法改变想法——结构可以（信念的系统分析）

**原文标题**: Why Facts Don't Change Minds–Structure Does (A Systems Analysis of Belief)

**原文链接**: [https://vasily.cc/blog/facts-dont-change-minds/](https://vasily.cc/blog/facts-dont-change-minds/)

本文认为，仅靠事实很少能改变人们的观念，因为信念的结构是相互关联的系统，类似于概念大教堂。教会对伽利略日心说的抵制不仅仅是迷信，更是对其权力结构、神学教义和社会等级制度至关重要的地心模型的捍卫。这种地心世界观嵌入在从圣经到建筑的一切事物中。质疑它威胁了教会的权威。

本文将信念系统可视化为概念和连接的图表。它以“增长至上的资本主义”和“生态可持续性”为例，展示了紧密联系的结构如何实现自我稳定。挑战一个信念系统意味着攻击核心思想（节点）或它们之间的连接（边），这可能会导致认知失调，并引发有动机的推理来捍卫现有的世界观。

“节点攻击”针对核心信念，可能会削弱连接，并损害整个系统的运作或动员能力。“边攻击”旨在切断思想之间的连接，迫使系统重新调整其逻辑，使其说服力降低。最终，信念系统通过重塑彼此的潜在结构进行竞争，而理解这些结构性动作可以深入了解论点背后的机制。人们对信息系统的代理性有着广泛的直觉。有些人认为信念系统——模因、意识形态、概念结构——几乎具有代理性，不断进化和竞争以求生存。另一些人则认为它们只不过是抽象概念，真正的代理性只存在于人类思想中。在实践中，持久性和明显的自

---

## 2. 玛丽患有精神分裂症，然后突然痊愈了。

**原文标题**: Mary had schizophrenia, then suddenly didn't

**原文链接**: [https://www.newyorker.com/magazine/2025/07/28/mary-had-schizophrenia-then-suddenly-she-didnt](https://www.newyorker.com/magazine/2025/07/28/mary-had-schizophrenia-then-suddenly-she-didnt)

本文讲述了玛丽的故事。她在四十岁出头时患上精神分裂症，影响了她的家庭，特别是她的女儿克里斯汀和安吉。玛丽出现了妄想症，认为自己正在被一位前同事联系，并受到他人的迫害，导致行为失常，并在九年内多次住院治疗。

大女儿克里斯汀积极参与了解她母亲的病情并为她的护理奔走呼吁，甚至研究了DSM。小女儿安吉在适应母亲妄想的世界中长大。尽管多次住院治疗和服用抗精神病药物，玛丽的病情仍然没有改变。

出乎意料的是，在被诊断出淋巴瘤并接受化疗后，玛丽的精神分裂症似乎消失了。她的女儿和医生们都感到困惑，因为她没有表现出精神病症状，并且她的性格变得冷静、礼貌和理性。虽然玛丽的癌症病情缓解，但她精神分裂症突然消失的原因仍然是一个谜，医生们推测可能是其中一种癌症药物产生了意想不到的好处。这个故事突出了精神疾病的复杂性以及健康和康复方面的意外转折。

---

## 3. Go 分配探针

**原文标题**: Go Allocation Probe

**原文链接**: [https://www.scattered-thoughts.net/writing/go-allocation-probe/](https://www.scattered-thoughts.net/writing/go-allocation-probe/)

本文介绍了一个名为 `go_allocation_probe` 的自定义工具，它用于识别程序中发生的 Go 分配类型，这是标准 Go 分析工具所缺乏的。作者利用 `bpftrace` 挂钩到核心 Go 分配函数 `runtime.mallocgc`。

挑战在于从 `_type` 参数中提取类型名称，结果发现它是一个偏移量 (`NameOff`)，指向可执行文件中模块数据的链表。为了解决这个问题，作者读取 Go 可执行文件的 ELF 段（`.noptrdata`、`.rodata`），并在一个单独的 Go 程序中重新实现了 Go 运行时中的 `resolveNameOff` 逻辑。这涉及到遍历模块链表并使用 `NameOff` 来查找类型名称。

当 `mallocgc` 被调用时，如果类型为 `nil`（当类型不包含指针时），会出现一个重大问题，导致 "<type not found>" 条目。为了解决这个问题，作者探测了其他运行时函数，如 `makechan`、`makeslicecopy` 和 `growslice`，它们可能会使用 `nil` 类型调用 `mallocgc`，并将类型信息存储在线程局部变量 (`@typ[tid]`) 中。他们还手动为特定类型（如 string、bytes 和 itab）分配名称。

最终的结果是一个可以识别和报告 Go 分配的类型、计数和总大小的工具，从而揭示潜在的分配热点。但需要注意的是，`[]T` 和 `*T` 可能会被报告为不同的类型。该工具最终帮助作者识别了代码中不必要的 `*string` 分配。

---

## 4. 微型代码阅读器：7美元的二维码传感器

**原文标题**: Tiny Code Reader: a $7 QR code sensor

**原文链接**: [https://excamera.substack.com/p/tiny-code-reader-a-7-qr-code-sensor](https://excamera.substack.com/p/tiny-code-reader-a-7-qr-code-sensor)

无法访问文章链接。

---

## 5. 人工智能市场明朗化

**原文标题**: AI Market Clarity

**原文链接**: [https://blog.eladgil.com/p/ai-market-clarity](https://blog.eladgil.com/p/ai-market-clarity)

埃拉德·吉尔的文章《AI市场明朗化》探讨了过去一年中某些人工智能市场的固化，指出了可能的领导者，并强调了潜在的未来机遇。他指出，虽然人工智能领域曾经一片模糊，但特定领域已涌现出明显的赢家。

文章确定了几个已出现明显领导者的市场：

*   **基础模型（LLM）：** Anthropic、谷歌、Meta、微软、Mistral、OpenAI和X.AI是核心参与者，因为扩展这些模型需要大量资金。
*   **代码：** Github Copilot、Anthropic的Claude Code、Cognition / Windsurf、Cursor、Google / Windsurf、Microsoft/Github、OpenAI。
*   **法律：** Harvey和CaseText领先，Legora和Crosby等新兴玩家紧随其后。
*   **医疗记录：** Abridge、Ambience、Commure / Athelas和Nuance正在整合。
*   **客户服务：** Decagon和Sierra正在获得 traction，而现有企业正在适应。
*   **搜索和信息检索重塑：** 谷歌、OpenAI、Perplexity和Meta。

吉尔还强调了未来的市场机遇：会计、合规、金融工具、销售工具和安全。

一个关键问题是，模型限制、GTM挑战或团队经验是否阻碍了这些领域的市场形成。 文章讨论了“GPT阶梯”，表明模型的进步将解锁新的市场。

最后，文章强调了向代理工作流（人工智能代表您行事）的转变，并讨论了人工智能驱动的整合的潜力，即收购公司而不仅仅是向他们销售人工智能软件可以加速采用并改善经济效益。

---

## 6. 字体对比：阿特金森易读体单空格 vs. JetBrains Mono 和 Fira Code

**原文标题**: Font Comparison: Atkinson Hyperlegible Mono vs. JetBrains Mono and Fira Code

**原文链接**: [https://www.anthes.is/font-comparison-review-atkinson-hyperlegible-mono.html](https://www.anthes.is/font-comparison-review-atkinson-hyperlegible-mono.html)

本文评测了Atkinson Hyperlegible Mono字体，这是一款为提高可读性（特别是视力障碍人士的可读性）而设计的等宽字体，并将其与流行的编程字体JetBrains Mono和Fira Code进行了比较。

作者将Atkinson Hyperlegible Mono作为其主要终端字体，探讨了字符区分的重要性，以避免歧义，并强调了多字符和单字符同形字（相似字符）以及镜像字形的问题。

Atkinson Hyperlegible Mono由Applied Design Works为盲文研究所创建，优先考虑独特的轮廓、增强的字母形式、不对称的字脚和夸张的下伸部。

与JetBrains Mono和Fira Code的比较表明，Atkinson Hyperlegible Mono在区分相似字符（如8、B、5和S）以及镜像字形（如b、d、p和q）方面表现出色。然而，与其他字体相比，它在方括号和花括号（[]和{}）的区分上表现较弱。编程符号也具有可变长度，这与其他字体处理此功能的方式不同。

本文还提供了安装说明，并承认了一些注意事项，包括某些版本中缺少反引号/抑音符、其以品牌为中心的起源、缺少编程连字以及缺乏同行评审的研究来支持其可读性声明。尽管如此，作者认为它仍然是一个引人注目的选择。

---

## 7. Better Auth (YC X25) 正在招聘

**原文标题**: Better Auth (YC X25) Is Hiring

**原文链接**: [https://www.ycombinator.com/companies/better-auth/jobs/N0CtN58-staff-engineer](https://www.ycombinator.com/companies/better-auth/jobs/N0CtN58-staff-engineer)

Better Auth（YC X25）是一家TypeScript认证框架公司，现招聘一名资深工程师加入其小型远程团队。该公司旨在普及高质量的身份验证，并使开发者能够掌控自己的身份验证流程。他们的开源框架正在快速增长，并受到许多初创公司和YC公司的信任。

资深工程师将协作开发后端、前端和设计，使用TypeScript、React和Node.js构建功能。他们将端到端地负责各项功能，管理插件生态系统，并指导初级开发人员。

Better Auth提供具有竞争力的薪资（12万至20万美元），以及丰厚的股权、完全远程办公的机会和定义公司文化的机会。他们重视自主性、协作、主动性和持续成长。所需技能包括5年以上软件开发经验、强大的TypeScript专业知识以及对身份验证概念的熟悉。拥有开源项目经验或构建复杂身份验证系统的经验者优先。

该公司专注于创造一流的开发者体验，并积极建设社区。他们正在寻找能够为开发者解决有意义的问题并从头开始塑造公司文化的人。Better Auth强调专注构建和产生重大影响之间的平衡。

---

## 8. 不要动画高度

**原文标题**: Don't Animate Height

**原文链接**: [https://www.granola.ai/blog/dont-animate-height](https://www.granola.ai/blog/dont-animate-height)

吉姆·费舍尔的文章《不要动画高度》详细介绍了他的笔记应用 Granola 中的一个性能瓶颈，该瓶颈是由一个昂贵的 CSS 动画引起的。他发现对音频音量可视化器的 `height` 属性进行动画处理会消耗过多的 CPU 和 GPU 资源。

费舍尔使用 Chrome 的开发者工具，特别是“性能”和“图层”选项卡，发现了由 `height` 动画触发的持续重绘和布局偏移。他解释说，动画 `height` 的代价很高，因为它会迫使浏览器为每一帧重新计算布局、重绘图层并重新合成整个场景。

该文章随后概述了浏览器的渲染流水线（布局、绘制、合成），并解释了不同的 CSS 属性如何影响它。布局属性（如 `height`）的动画成本最高，其次是绘制属性（如 `fill`），最后是合成属性（如 `transform` 和 `opacity`），它们的成本最低。

费舍尔最初尝试用 `transform: scaleY()` 替换 `height`，导致了圆角失真。他最终通过为每个条使用两个圆角矩形，并使用 `translate` 动画化它们的位置来解决了这个问题。这利用了 `transform` 属性，允许浏览器跳过昂贵的布局和绘制步骤，从而显着提高了性能。渲染器进程的 CPU 使用率从 15% 降至 6%，GPU 使用率也大幅下降。这篇文章强调了理解浏览器渲染流水线以及为动画选择合适的 CSS 属性的重要性。

---

## 9. 破坏的理由

**原文标题**: The Case for Sabotage

**原文链接**: [https://collectiveactionintech.substack.com/p/the-case-for-sabotage](https://collectiveactionintech.substack.com/p/the-case-for-sabotage)

无法访问文章链接。

---

## 10. OSS重建：开源，重塑，历久弥新

**原文标题**: OSS Rebuild: open-source, Rebuilt to Last

**原文链接**: [https://security.googleblog.com/2025/07/introducing-oss-rebuild-open-source.html](https://security.googleblog.com/2025/07/introducing-oss-rebuild-open-source.html)

OSS重建：由谷歌开源安全团队 (GOSST) 宣布，是一项旨在通过独立复现和验证上游制品来增强对开源软件包生态系统信任的新项目。OSS重建旨在打击针对广泛使用的依赖项的供应链攻击，为安全团队提供可验证的数据，而无需增加维护人员的负担。

该项目具有以下特性：

*   **自动化构建定义生成：** 适用于PyPI、npm和Crates.io软件包。
*   **SLSA来源：** 适用于数千个软件包，无需发布者参与即可达到SLSA构建级别3。
*   **构建可观察性和验证工具：** 集成到现有的漏洞管理工作流程中。
*   **基础设施定义：** 使组织能够运行自己的OSS重建实例，用于重建、签名和分发来源。

OSS重建通过解决未提交的源代码、构建环境妥协和隐蔽的后门，来应对日益增长的开源软件漏洞问题。它帮助企业增强元数据、扩充SBOM并加速漏洞响应。发布者和维护人员受益于增强的软件包信任、历史软件包的追溯完整性以及降低的CI安全敏感性。

该项目支持检查软件包完整性、浏览重建版本以及使用CLI工具重建软件包。谷歌鼓励开发人员、企业和安全研究人员在github.com/google/oss-rebuild上为OSS重建的开发和改进做出贡献。

---

## 11. 双子座北望远镜发现参宿四长期预测的恒星伴星

**原文标题**: Gemini North Discovers Long-Predicted Stellar Companion of Betelgeuse

**原文链接**: [https://noirlab.edu/public/news/noirlab2523/](https://noirlab.edu/public/news/noirlab2523/)

天文学家使用北双子座望远镜上的‘Alopeke’设备，发现了一颗伴星围绕参宿四运行，参宿四是一颗红色超巨星，也是夜空中最亮的恒星之一。这一发现解决了长期以来围绕参宿四亮度变化之谜，并为理解其他红色超巨星的亮度变化机制提供了见解。

这颗伴星之前未被哈勃和钱德拉探测到，此次是利用散斑成像技术发现的，该技术克服了大气扭曲，实现了高分辨率。分析显示，这颗伴星是一颗炙热、年轻的蓝白色A型或B型前主序星，质量约为太阳的1.5倍，但比参宿四暗得多。它在相对靠近参宿四的外部扩展大气层内运行，距离约为地日距离的四倍。

这是首次探测到如此靠近超巨星运行的恒星伴星。科学家们认为，参宿四及其伴星可能诞生于同一时期，但潮汐力最终将导致伴星螺旋式地坠入参宿四，预计将在未来1万年内发生。该发现有助于解释在类似的红色超巨星中观察到的周期性亮度变化。另一次研究该伴星的机会将在2027年11月到来，届时它将达到与参宿四的最远距离。

---

## 12. 绕过水印实现

**原文标题**: Bypassing Watermark Implementations

**原文链接**: [https://blog.kulkan.com/bypassing-watermark-implementations-fe39e98ca22b](https://blog.kulkan.com/bypassing-watermark-implementations-fe39e98ca22b)

Kulkan Security的这篇文章探讨了绕过水印的各种方法，水印常被用于保护在线流媒体资产，如视频、图像和PDF。文章强调客户端水印通常很脆弱，因为攻击者可以控制客户端逻辑。

文章列举了几个水印实现示例以及相应的绕过技术，包括：

*   **移除简单的HTML元素：** 通过删除HTML元素可以轻松绕过。
*   **基于JavaScript的水印：** 通过拦截服务器响应以删除JavaScript文件、调试代码或操纵CSS样式（隐藏、更改颜色、更改字体大小、重新定位）来规避。
*   **画中画（PiP）：** 在某些情况下，启用PiP可以绕过视频元素上强制执行的水印。
*   **子资源完整性（SRI）绕过：** 从服务器响应中删除SRI可以防止浏览器强制执行保护。
*   **禁用PiP：** 这是一种用户体验功能，而不是安全机制
*   **篡改水印内容：** 修改水印中显示的用户资料数据（例如，帐户名）以模糊敏感信息。
*   **视频片段的重构（HLS）：** 捕获m3u8播放列表和视频/音频片段以进行离线播放，即使已加密。文章讨论了使用ffmpeg、使用openssl手动解密以及使用自定义Python脚本（m3u8\_decrypt.py）来实现此目的。

作者总结说，虽然水印可以阻止未经授权的传播，但对于敏感内容，将其与更强的安全措施（如服务器端渲染或数字版权管理（DRM））相结合至关重要。 本文旨在帮助开发人员和测试人员提高水印实现的安全性。

---

## 13. DaisyUI：Tailwind CSS 组件

**原文标题**: DaisyUI: Tailwind CSS Components

**原文链接**: [https://daisyui.com/](https://daisyui.com/)

daisyUI 是一个 Tailwind CSS 插件，它提供预构建、可定制的组件类名，从而实现更快、更简洁的开发。它不需为基本 UI 元素编写大量实用类，而是提供 `btn`、`card` 和 `toggle` 等语义化类名，这些类名可以使用 Tailwind 的实用类进一步修改。

主要优点包括更快的开发速度、更简洁的 HTML、可定制的主题（包括暗黑模式）、纯 CSS 且无 JavaScript 依赖以及框架无关性。它显著减少了所需的类名数量和 HTML 大小。

daisyUI 可以通过 Tailwind CSS 实用类进行高度定制，并提供主题生成器来创建自定义设计。它还引入了可以通过 CSS 变量定制的语义化颜色名称，从而可以轻松切换主题。

该插件因其易用性、提高生产力以及快速创建美观应用程序的能力而受到开发人员的赞誉。 主要公司的工程师都在使用它，并且它已在流行的科技出版物和播客中亮相。 组件库提供了大量具有多种可能性的组件。 总的来说，daisyUI 旨在通过提供预样式组件和主题系统来简化和加速 Tailwind CSS 开发。

---

## 14. Yt-transcriber – 提供YouTube链接即可获得文字稿

**原文标题**: Yt-transcriber – Give a YouTube URL and get a transcription

**原文链接**: [https://github.com/pmarreck/yt-transcriber](https://github.com/pmarreck/yt-transcriber)

Yt-transcriber：一款使用开源AI工具从URL或本地音视频文件转录YouTube视频的TUI应用。它提供诸如说话人识别（开发中）、摘要和翻译等功能。摘要和翻译需要OpenAI API密钥。它利用`ffmpeg`处理各种音视频格式。

推荐的安装方法是使用Nix，它可以自动管理依赖项。如果未使用Nix，则需要手动安装Python 3.12、ffmpeg和glow（可选）。Python依赖项安装在虚拟环境中，Whisper模型下载到缓存目录。

使用方法包括运行带有YouTube URL或文件路径的`yt-transcriber`。转录文本会发送到stdout，允许重定向或管道传输到其他程序，如`summarize`和`translate`。可以指定模型大小以控制转录质量（选项：base、small、medium、large、large-v2）。通过设置DEBUG环境变量启用调试信息。

示例命令包括将YouTube视频转录到文件，转录本地文件，对其进行摘要，翻译以及通过`glow`管道传输输出。该项目包括用于设置和应用程序功能的测试脚本。说话人区分、摘要和翻译功能可能需要Claude、OpenAI和/或Huggingface的API密钥。

---

## 15. TODO并非用来完成

**原文标题**: TODOs Aren't for Doing

**原文链接**: [https://sophiebits.com/2025/07/21/todos-arent-for-doing](https://sophiebits.com/2025/07/21/todos-arent-for-doing)

本文反对在代码库中严格追踪和删除TODO注释的常见做法。作者认为，虽然有些TODO代表需要立即采取行动的关键任务（例如防止系统故障），但许多其他的TODO具有不同的、同样重要的作用。

作者认为，TODO通常捕捉了原始作者的细微见解，记录了边缘情况、潜在的改进或尚未完全实现的设计考虑。这些TODO起着记忆辅助的作用，为未来遇到该代码的开发人员提供了关键的上下文。它们回答了“为什么这样做？”这个无声的问题，并防止了基于不完整理解的不必要重构。

作者建议不要将所有TODO都视为可执行的任务，而是认识到它们作为注释的作用，这些注释保留了宝贵的上下文。精心放置的TODO可以避免混淆，鼓励深思熟虑的改进，并通过提供对原始开发人员思维过程的洞察，最终提高代码的可维护性。核心论点是，TODO的价值不仅在于其完成，还在于其传递知识和促进对代码库更深入理解的能力。

---

## 16. Show HN: 代码的魔力 – 一本关于计算的奇妙与怪诞的书

**原文标题**: Show HN: The Magic of Code – book about the wonders and weirdness of computation

**原文链接**: [https://themagicofcode.com/sample/](https://themagicofcode.com/sample/)

这篇“Show HN”帖子介绍《代码的魔力》一书，该书将计算探索为一种人文和博雅艺术。本书并非仅关注技术层面，而是旨在突出计算的奇妙之处和古怪之处，并将其与语言、哲学甚至生物学等更广泛的领域联系起来。其核心思想是展示计算如何影响人类理解和体验的各个领域，以及如何被这些领域所影响。该帖子提供了下载PDF样本摘录的链接，以及访问更多关于该书信息的链接。

---

## 17. Blip：前Dropbox工程师打造的P2P大型文件分享

**原文标题**: Blip: Peer-to-Peer Massive File Sharing by Former Dropbox Engineers

**原文链接**: [https://blip.net/](https://blip.net/)

Blip：一款无需上传云端，即可传输海量文件的点对点应用。它由前 Dropbox 工程师开发，无文件大小限制。Blip 提供用户间直接加密（TLS 1.3）传输，无需上传下载步骤，从而提高速度和效率。

主要功能包括：无需压缩即可传输文件夹、轻量级原生应用、跨平台兼容（Android、Mac、Windows、iOS）、全球覆盖、文件质量保持、中断后自动恢复。Blip 还支持“局域网直连”，在同一网络下实现更快的速度。

Blip 与 WeTransfer 等服务不同之处在于，它提供直接、安全的传输，无需公共链接或上传。与 Dropbox 等云存储服务不同，Blip 不存储文件，允许用户在本地管理文件。与 Aspera 等企业解决方案相比，Blip 更简单、更易用，无需复杂的设置或昂贵的合同。它超越了 AirDrop 等附近共享选项，提供可靠的跨平台传输，不受距离限制。

Blip 对非商业用途免费，商业活动需付费计划。它拥有针对长距离优化的高传输速度，并且没有广告。该软件尤其适合创意人员，能够无缝传输大型项目文件，例如 Final Cut Pro 文件包。用户评价强调了它在传输大型视频文件和文件夹方面的效率，赞扬其易用性和速度，优于传统方法。

---

## 18. 反向代理深度剖析：边缘 HTTP 解析为何比看起来更难

**原文标题**: Reverse Proxy Deep Dive: Why HTTP Parsing at the Edge Is Harder Than It Looks

**原文链接**: [https://startwithawhy.com/reverseproxy/2025/07/20/ReverseProxy-Deep-Dive-Part2.html](https://startwithawhy.com/reverseproxy/2025/07/20/ReverseProxy-Deep-Dive-Part2.html)

本文深入探讨了反向代理中HTTP处理的复杂性，强调其远比最初看起来的要更具挑战性。虽然标准库提供了基本功能，但在大规模环境中实现可靠的性能、安全性和合规性，需要仔细考虑多个因素。

HTTP协议的演变、客户端和服务器不同的开发生命周期，以及URL和cookie大小等限制方面缺乏行业标准，都增加了复杂性。反向代理必须处理不一致性、执行规范并适应不同的流量概况。

安全性至关重要，因为代理是抵御恶意攻击的第一道防线。请求清理（包括有效性检查、完整性强制和大小限制）对于维持稳定性和安全性至关重要。同样，响应清理可确保合规性并保护客户端。

标头操作（例如添加、删除或更新标头以转发信息、规范化或增强安全性）增加了另一层复杂性。User-Agent和Geo-IP标头处理带来了与解析复杂性和潜在的拒绝服务漏洞相关的独特挑战。

最后，重写路径是一种常见需求，涉及前缀剥离、重定向和复杂的正则表达式重写。文章总结说，反向代理中的HTTP解析是性能、安全性、正确性和兼容性的关键交汇点，需要谨慎平衡以处理混乱和不可预测的输入。本系列将在未来的文章中继续探讨反向代理的服务发现、负载均衡、HTTP客户端行为和可观察性等方面。

---

## 19. 从制图到代码：2025年威尼斯双年展上的权力架构

**原文标题**: From Cartography to Code: Architectures of Power at the Venice Biennale 2025

**原文链接**: [https://www.stirworld.com/see-features-from-cartography-to-code-architectures-of-power-at-the-venice-biennale-2025](https://www.stirworld.com/see-features-from-cartography-to-code-architectures-of-power-at-the-venice-biennale-2025)

Mrinmayee Bhoot 的文章《探索建筑中的“智性”：2025年威尼斯建筑双年展指南》探讨了即将到来的威尼斯建筑双年展的预期主题和潜在展览。 该文章于2025年4月26日发表，表明双年展将深入研究建筑中的“智性”概念，可能探索人工智能、数据和建筑环境的交叉点。

根据标题，我们可以推断出双年展可能会考察技术进步如何重塑建筑设计、建造和城市规划。 对“权力建筑”的潜在关注表明，将会对这些进步的社会、政治和伦理影响进行批判性分析。 这可能包括探索监视、控制、算法偏差等问题，以及技术强化现有权力结构的可能性。

该文章以指南的形式呈现，可能提供了对预计将展示的特定展馆、装置和主题的见解。 它可能分析策展方向，并提供一个框架，以了解将人工智能和数据整合到建筑中，同时考虑其更广泛的社会影响的复杂性。 最终，该文章将双年展定位为一个对技术、权力和建筑世界的未来之间不断演变的关系进行批判性讨论的平台。

---

## 20. 1KB JavaScript 数字电台

**原文标题**: 1KB JavaScript Numbers Station

**原文链接**: [https://shkspr.mobi/blog/2025/07/1kb-js-numbers-station/](https://shkspr.mobi/blog/2025/07/1kb-js-numbers-station/)

本文详细介绍了为js1024竞赛创建“数字电台”演示的过程。该竞赛挑战参赛者在1KB的JavaScript限制内创造“令人毛骨悚然”的体验。作者并非着色器专家，而是利用浏览器内置的文本转语音(TTS) API来生成令人不安的音频，让人联想到真实的数字电台。

核心思想是操纵TTS参数（如语速和音调）来创造令人不安的语音。该演示并非嵌入音频，而是在运行时生成语音。为了在大小限制内生成随机单词，作者巧妙地从浏览器的全局对象属性中提取单词（例如，`Object.getOwnPropertyNames(globalThis)`），并筛选出首字母大写的单字条目。这产生了一些令人毛骨悚然的词汇，如“Event”和“Atomics”。

该演示还通过使用多种语言来模拟数字电台。作者随机化TTS引擎的语言，利用内置的语言字符串和TTS引擎用外语口音发音英语单词的能力。通过结合随机化的音调、速度、语言以及数字和单词，该演示创造了一种相当令人毛骨悚然和不安的音频体验。最后，剩余的字节用于由Unicode绘图字符组成的基本动画背景。

---

## 21. 如何使用火狐浏览器

**原文标题**: How to Firefox

**原文链接**: [https://kau.sh/blog/how-to-firefox/](https://kau.sh/blog/how-to-firefox/)

本文热情地倡导切换到 Firefox，强调其开源特性以及相比 Chrome 而言更卓越的“净化网络”能力。作者认为 Chrome 的 Manifest V3 更新削弱了强大的广告拦截器 uBlock Origin (uBO) 的功能，而 Firefox 允许其充分发挥作用。

文章强调了 Firefox 的自定义选项，尤其是 Android 用户可以享受无缝同步和功能齐全的浏览器扩展，包括 uBO。作者详细介绍了一个个性化的 Firefox 设置，重点是必要的 uBO 配置（包括用于阻止 Facebook 流量和“使用 Google 登录”弹出窗口的自定义过滤器）。他们还介绍了隐私增强功能，如用于管理多个在线身份的容器，这通过原生配置调整和 Containerise 插件得以实现。

文章还推荐了一些“锦上添花”的插件，以提高可用性，例如 Dark Reader、Stylus 和 Obsidian Web Clipper。文章还提到了通过 `about:config` 进行的进一步自定义，特别是改变标签位置。最后，作者分享了 Firefox 的隐藏功能，例如使用 `/` 和 `'` 进行快速查找、使用 Shift 键绕过右键菜单以及 URL 栏搜索快捷方式。文章最后呼吁大家下载 Firefox，重新获得更干净、更美好的网络体验。

---

## 22. 自行车禧玛诺Di2无线变速系统的安全性分析

**原文标题**: MakeShift: Security Analysis of Shimano Di2 Wireless Gear Shifting in Bicycles

**原文链接**: [https://www.usenix.org/conference/woot24/presentation/motallebighomi](https://www.usenix.org/conference/woot24/presentation/motallebighomi)

无法访问文章链接。

---

## 23. 展示 HN：我的 GPU 风扇传奇 – 一个 DIY ATX 风扇控制器

**原文标题**: Show HN: My GPU Fan Saga – A DIY ATX Fan Controller

**原文链接**: [https://shafq.at/my-gpu-fan-saga.html](https://shafq.at/my-gpu-fan-saga.html)

自制ATX风扇控制器，用于GPU

这篇“Show HN”帖子详细介绍了一个自制项目，旨在为GPU创建一个ATX风扇控制器。作者的AMD GPU风扇出现故障，导致过热问题。最初，他们用一个备用风扇替换了它，但该风扇始终全速运转。为了解决噪音问题，他们设计了一个定制解决方案，使用ATtiny85微控制器来实现脉冲宽度调制（PWM）以进行可变风扇速度控制。

该系统使用DS18B20温度传感器来监测GPU温度，并自动相应地调整风扇速度。作者解释了元件的选择，包括MOSFET电机驱动器以及使用1-Wire协议连接温度传感器。还提到了其他温度传感器，如HTU31、BME688和TMP35/36/37。

该项目成功地降低了GPU温度，同时保持风扇在空闲时安静。作者提供了一个详细的物料清单（BOM），其中包含每个组件的成本，范围从6.40美元到16.05美元，加上PCB制造费用。他们承认商业解决方案可能更便宜，但强调了构建定制解决方案的教育价值和所获得的满足感。

代码和PCB文件在GitHub和Codeberg上开源。作者计划添加更多功能，并根据用户的兴趣探索更便宜的基于微控制器的版本。

---

## 24. 美国退出联合国教科文组织

**原文标题**: The United States withdraws from UNESCO

**原文链接**: [https://www.state.gov/releases/office-of-the-spokesperson/2025/07/the-united-states-withdraws-from-the-united-nations-educational-scientific-and-cultural-organization-unesco](https://www.state.gov/releases/office-of-the-spokesperson/2025/07/the-united-states-withdraws-from-the-united-nations-educational-scientific-and-cultural-organization-unesco)

美国宣布将于2026年12月31日退出联合国教科文组织。根据国务院发言人塔米·布鲁斯的新闻声明，继续参与联合国教科文组织不符合美国国家利益。

美国列举了退出的一些原因，包括联合国教科文组织被认为推动“分裂性的社会和文化事业”，以及其对联合国可持续发展目标的强烈关注，美国认为这是一种与“美国优先”外交政策相冲突的“全球主义意识形态议程”。 美国还指出，联合国教科文组织决定接纳“巴勒斯坦国”为成员国是“非常成问题的”，并助长了该组织内部的反以色列言论。

美国表示，其参与国际组织现在将优先推进美国利益。 尽管宣布退出，但在2026年底退出生效之前，美国仍将是联合国教科文组织的正式成员。

---

## 25. 疾病在症状出现前数年如何发生的空前窗口

**原文标题**: An unprecedented window into how diseases take hold years before symptoms appear

**原文链接**: [https://www.bloomberg.com/news/articles/2025-07-18/what-scientists-learned-scanning-the-bodies-of-100-000-brits](https://www.bloomberg.com/news/articles/2025-07-18/what-scientists-learned-scanning-the-bodies-of-100-000-brits)

无法访问文章链接。

---

## 26. 完全的寂静在阿拉伯语中总是被幻听为“ترجمة نانسي قنقر”。

**原文标题**: Complete silence is always hallucinated as "ترجمة نانسي قنقر" in Arabic

**原文链接**: [https://github.com/openai/whisper/discussions/2608](https://github.com/openai/whisper/discussions/2608)

OpenAI Whisper仓库中的这个GitHub问题突显了一种奇怪的现象：当Whisper处理静默音频文件时（特别是使用`large-v3`模型和阿拉伯语时），它会幻听出短语“ترجمة نانسي قنقر”（南希·昆卡的翻译）。

原始发帖者puthre通过一个简单的`ffmpeg`命令生成静默音频并使用Whisper，展示了这一点。其他人也证实了这种现象，并将其归因于该模型从YouTube数据中学习，字幕制作者通常在视频结尾包含版权声明或片尾短语，导致Whisper将静默与这些短语联系起来。在其他语言中也观察到类似的幻听现象（德语的“Untertitelung des ZDF”和罗马尼亚语的“nu uitati sa da-ti like si subscribe”）。

讨论的可能的解决方案和解决方法包括使用语音活动检测 (VAD) 来避免处理静默音频、调整模型参数（尽管对 `v3` 的效果较差）以及对文本输出进行后处理以删除幻听短语。Voxtral被认为是一种有前途的替代阿拉伯语模型。还有人指出，这个问题也会影响ChatGPT语音模式。共识是，这种伪像源于训练数据包含与静默相关的版权声明和常见的片尾短语。

---

## 27. 忙碌开发者的柔术

**原文标题**: Jujutsu for busy devs

**原文链接**: [https://maddie.wtf/posts/2025-07-21-jujutsu-for-busy-devs](https://maddie.wtf/posts/2025-07-21-jujutsu-for-busy-devs)

本网页使用“阿努比斯”安全系统，以防止人工智能公司过度抓取网站数据。这种抓取可能导致服务器过载并宕机，影响正常用户。

“阿努比斯”采用类似于Hashcash的“工作量证明”方案，要求访问者在访问网站之前执行一项小的计算任务。对于个人而言，这负担可以忽略不计，但对于大规模抓取者来说，成本会变得很高，从而起到威慑作用。

该系统是一个临时解决方案。长期目标是通过分析字体渲染等指纹识别技术，识别并阻止抓取者使用的无头浏览器。这将允许正常用户绕过工作量证明挑战。

该系统需要启用JavaScript，并建议禁用可能干扰其功能的JShelter等插件。 需要JavaScript的原因是人工智能公司改变了网站托管的规则和社会契约。 正在探索一种无需JavaScript的解决方案。当前版本的“阿努比斯”为v1.20.0。

---

## 28. 记录意外不一致

**原文标题**: Unexpected inconsistency in records

**原文链接**: [https://codeblog.jonskeet.uk/2025/07/19/unexpected-inconsistency-in-records/](https://codeblog.jonskeet.uk/2025/07/19/unexpected-inconsistency-in-records/)

本文探讨了在 C# 记录中使用 `with` 运算符处理派生数据（基于构造函数参数初始化的属性或字段）时出现的意外行为。作者发现，`with` 运算符会对现有记录执行浅拷贝，然后在 *不* 重新计算派生数据的情况下更新指定的属性。这会导致不一致，即派生数据基于 *旧的* 值，而不是新的值。

例如，一个具有 `Value` 属性和从 `Value` 派生的 `Even` 属性的 `Number` 记录，在使用 `with` 更改 `Value` 时，会错误地保留旧的 `Even` 值。

作者探讨了潜在的解决方案：

1.  **避免对具有派生数据的记录使用 `with`：** 这需要警惕，并且如果记录的属性发生更改，则可能需要进行代码重构。
2.  **创建 Roslyn 分析器：** 这种自动化方法可以通过分析成员初始化程序和 `with` 运算符的使用情况来检测有问题的 `with` 使用。
3.  **使用 `Lazy<T>` 进行延迟计算：** 这种复杂且可能内存效率低下的方法会将属性计算延迟到 `with` 操作之后。
4.  **请求语言更改：** 虽然不太可能是一个简单的修复，但它暗示了记录中更灵活的初始化的可能性。

作者总结说，这种不一致感觉像是一个“自毁装置”，并为使用记录和 `with` 运算符处理派生数据的开发人员敲响了警钟。他们旨在开发一个 Roslyn 分析器来检测此问题。

---

## 29. 地球上最大的火星碎片以530万美元拍卖成交

**原文标题**: Largest piece of Mars on Earth fetches $5.3M at auction

**原文链接**: [https://apnews.com/article/mars-rock-meteorite-auction-dinosaur-sothebys-01d7ccfc8dc580ad86f8e97a305fc8fa](https://apnews.com/article/mars-rock-meteorite-auction-dinosaur-sothebys-01d7ccfc8dc580ad86f8e97a305fc8fa)

一块被认为是地球上已知最大的火星岩石，在苏富比拍卖行以 530 万美元的价格售出。 这颗被昵称为“NWA 15000”的陨石，起源于火星，最终降落在撒哈拉沙漠。

这块岩石被描述为一个完整的、定向的样本，这意味着它在穿越地球大气层的炽热降落过程中保持完整，展示了其原始形状和熔壳。 它的尺寸和完整性被认为是其高价值的主要因素。

虽然买家的身份尚未透露，但拍卖结果凸显了对稀有外星物质的巨大需求和价值。 该文章强调了这颗陨石的非凡性，无论是在其大小、完整性还是火星起源方面，使其成为一件备受追捧的收藏品。

---

## 30. .a文件是个遗物：为什么静态库一直是个糟糕的主意

**原文标题**: The .a file is a relic: Why static archives were a bad idea all along

**原文链接**: [https://medium.com/@eyal.itkin/the-a-file-is-a-relic-why-static-archives-were-a-bad-idea-all-along-8cd1cf6310c5](https://medium.com/@eyal.itkin/the-a-file-is-a-relic-why-static-archives-were-a-bad-idea-all-along-8cd1cf6310c5)

本文探讨了基于C语言的SDK中使用静态库（.a文件）所面临的挑战和缺陷，特别是与动态链接（.so文件）相比而言。作者是一位拥有丰富SDK经验的C语言开发者，他认为.a文件难以满足客户的期望，并提出了一种新的“静态捆绑对象”类型作为ELF文件头的潜在解决方案。

核心问题在于，链接器处理静态库的方式是基于符号解析来提取并选择性地包含目标文件（.o文件）。这种旨在减小二进制文件大小的方法，可能会导致链接不完整和运行时崩溃，尤其是在涉及构造函数或析构函数的复杂编码场景中。这是因为如果包含初始化代码的必要目标文件没有被符号明确要求，它就不会被包含，即使它对于正确执行至关重要。

虽然`-Wl,--whole-archive`链接器标志可以强制包含来自静态库的所有目标文件，但它会不加区分地包含所有内容，即使是不必要的，从而导致二进制文件臃肿。当SDK在一个链接定义下捆绑多个库时，这会变得尤其麻烦，迫使用户包含所有库，无论他们是否实际需要。

本文强调，当前的静态链接机制严重依赖于源代码设计决策，函数在特定.c文件中的位置直接影响到链接的内容。这种对源文件组织方式的依赖使得静态链接变得不可预测且难以管理。作者认为，静态库的局限性阻碍了健壮且易于使用的基于C语言的SDK的开发。

---

## 31. 使用pedalboard进行Python音频处理

**原文标题**: Python audio processing with pedalboard

**原文链接**: [https://lwn.net/Articles/1027814/](https://lwn.net/Articles/1027814/)

这篇LWN.net文章总结了Peter Sobot在PyCon US 2025上关于使用`pedalboard`库进行Python音频处理的演讲。Sobot是Spotify的机器学习工程师，他介绍了`pedalboard`，作为一种用于各种音频任务的工具，从格式转换到添加效果。

该演讲涵盖了数字音频基础知识，解释了声音是如何被捕获并以数字方式通过采样来表示的。他强调了采样率的重要性，并演示了如何将音频作为数字流进行处理。他强调了Python内置`wave`模块的局限性，并展示了`pedalboard`友好的用户界面，用于使用NumPy数组读取、写入和修改音频数据。

Sobot警告不要将整个音频文件加载到内存中，用例子说明了大型或高度压缩的文件可能存在的内存问题，并强调了输入大小不能保证输出大小。他建议以分块方式处理音频。他强调了由于NumPy基于C的实现，使用NumPy进行音频处理的性能优势。

`pedalboard`能够在Python中创建虚拟“效果器”，以应用各种音频效果，如失真、延迟和混响。它支持第三方VST3插件，并提供诸如重采样、时间伸缩和格式转换等功能。它可以用于流式传输实时音频。硬件要求不高，并且`pedalboard`确保搜索落在样本边界上，即使在压缩格式中也是如此。

---

## 32. Gemini 2.5 Flash-Lite 现已稳定且全面可用

**原文标题**: Gemini 2.5 Flash-Lite is now stable and generally available

**原文链接**: [https://developers.googleblog.com/en/gemini-25-flash-lite-is-now-stable-and-generally-available/](https://developers.googleblog.com/en/gemini-25-flash-lite-is-now-stable-and-generally-available/)

谷歌发布 Gemini 2.5 Flash-Lite 正式版，Gemini 2.5 系列中最快且最具成本效益的模型。定价为每百万输入 tokens 0.10 美元，每百万输出 tokens 0.40 美元，专为翻译和分类等对延迟敏感的任务而设计，旨在实现最高的性价比。音频输入定价也比预览版降低了 40%。

Gemini 2.5 Flash-Lite 拥有同类最佳的速度，在延迟方面优于以前的版本，同时在包括编码、数学、推理和多模态理解在内的各种基准测试中保持高质量。它具有 100 万个 token 的上下文窗口，可控制的思维预算，并支持原生工具，如 Google 搜索支持的 Grounding、代码执行和 URL 上下文。

该模型已经成功部署于多个应用：Satlyt 利用它来降低卫星数据处理的延迟和功耗；HeyGen 利用它进行自动化视频规划、内容优化和翻译；DocsHound 以低延迟的截图提取将产品演示转换为文档；Evertune 利用它来加速 AI 模型分析和报告生成。

开发者可以通过在代码中指定“gemini-2.5-flash-lite”来开始使用 Gemini 2.5 Flash-Lite。预览别名将于 8 月 25 日移除。该模型可在 Google AI Studio 和 Vertex AI 中使用。

---

## 33. 反对恢复使用杀蜂农药的法国请愿书突破一百万签名

**原文标题**: French petition against return of bee-killing pesticide passes 1M

**原文链接**: [https://phys.org/news/2025-07-french-petition-bee-pesticide-1mn.html](https://phys.org/news/2025-07-french-petition-bee-pesticide-1mn.html)

反对“杜普朗法”的法国请愿已获百万签名，该法允许重新引入禁用农药吡虫啉。请愿由学生埃莉诺·帕特里发起，认为该法不利于公众健康、生物多样性和环境。吡虫啉自2018年起在法国被禁用，但在欧盟境内合法，已知对蜜蜂等授粉媒介有毒，被养蜂人称为“蜜蜂杀手”。

虽然该法的支持者认为它将放宽对农民，尤其是面临虫害的甜菜和榛子种植者的管制，但批评者引用了吡虫啉对蜜蜂有害影响的科学证据。人们也对其对人类健康的影响表示担忧。

尽管公众普遍反对，国民议会议长娅埃尔·布朗-皮韦仍排除了放弃该立法的可能性，强调其对支持法国农民的重要性。然而，请愿的成功可能会引发议会辩论。绿党领导人玛琳·通德利耶已呼吁总统埃马纽埃尔·马克龙介入，将该法案送回重新审查。请愿书呼吁立即废除该法律，并进行由公民主导的、涉及各利益相关者的磋商。

---

## 34. 针对微软SharePoint的全球性攻击波及美国及各州机构，研究人员称。

**原文标题**: Global hack on Microsoft Sharepoint hits U.S., state agencies, researchers say

**原文链接**: [https://www.washingtonpost.com/technology/2025/07/20/microsoft-sharepoint-hack/](https://www.washingtonpost.com/technology/2025/07/20/microsoft-sharepoint-hack/)

无法访问文章链接。

---

## 35. NASA的X-59静音超音速飞机开始滑行测试

**原文标题**: Nasa’s X-59 quiet supersonic aircraft begins taxi tests

**原文链接**: [https://www.nasa.gov/image-article/nasas-x-59-quiet-supersonic-aircraft-begins-taxi-tests/](https://www.nasa.gov/image-article/nasas-x-59-quiet-supersonic-aircraft-begins-taxi-tests/)

美国国家航空航天局的X-59静音超音速研究机于2025年7月10日在加利福尼亚州帕姆代尔的美国空军第42工厂开始滑行测试，标志着它首次依靠自身动力移动。 由美国国家航空航天局试飞员尼尔斯·拉森以及美国国家航空航天局和洛克希德·马丁公司的一个团队进行，低速测试验证了转向和制动等关键系统，确保了飞机的稳定性和控制性。

这些滑行测试是X-59首次飞行前的最后一轮地面测试。 在接下来的几周内，飞机将逐渐提高速度，最终进行一次接近起飞的高速滑行测试。

X-59是美国国家航空航天局奎斯特任务的核心，该任务旨在通过将巨大的音爆降低为更安静的“砰”声来展示安静的超音速飞行。 从X-59收集的数据将与美国和国际监管机构分享，以告知新的、数据驱动的陆地上空超音速商业飞行的噪声阈值。 这是使商业超音速航空旅行成为现实的关键一步。

---

## 36. Show HN: 用于分布式系统的 Go 命令流库 (比 gRPC 快 3 倍)

**原文标题**: Show HN: Go Command-streaming lib for distributed systems (3x faster than gRPC)

**原文链接**: [https://github.com/cmd-stream/cmd-stream-go](https://github.com/cmd-stream/cmd-stream-go)

`cmd-stream-go` 是一个高性能、模块化的 Go 语言库，旨在基于命令模式构建高效的分布式系统。它提供基于 TCP/TLS 的低延迟通信，并且速度显著更快（标题显示比 gRPC 快 3 倍）。

该库采用客户端-服务器架构，客户端向服务器发送命令，调用者执行命令，接收器处理功能。 `cmd-stream-go` 支持服务器流（一个命令可以返回多个结果）、使用单一连接进行发送和接收的异步客户端、重连和保活功能、断路器模式、OpenTelemetry 集成和各种序列化格式。

主要优势包括高性能、资源效率和可扩展性，从而可能降低基础设施成本。可以通过使用多个并行预先建立的连接来最大化性能。

该库的模块化设计允许开发者根据需要轻松替换组件。它包含用于核心客户端/服务器定义 (`core-go`)、连接处理 (`delegate-go`)、命令处理 (`handler-go`) 和命令/结果传递 (`transport-go`) 的子模块。

文档提供了教程、OpenTelemetry 示例以及将 `cmd-stream-go` 用作现有 RPC 系统更快传输层的示例。性能比较的基准测试可在 `go-client-server-benchmarks` 中找到。

---

## 37. 如果核磁共振的真正力量根本不在图像中呢？

**原文标题**: What If the Real Power of MRI Isn't in the Image at All?

**原文链接**: [https://medium.com/@jensenbox/what-if-the-real-power-of-mri-isnt-in-the-image-at-all-401c9e00ae1d](https://medium.com/@jensenbox/what-if-the-real-power-of-mri-isnt-in-the-image-at-all-401c9e00ae1d)

本文探讨了MRI背后的物理原理，强调其真正的力量可能不仅在于最终的图像，更在于k空间中捕获的原始数据。MRI依赖于氢原子的丰富性和简单的磁性，当暴露于磁场中时，氢原子会发生旋进并发出射频信号。这些信号的频率由拉莫尔方程决定，并由调谐到该频率的线圈检测。

原始数据并非图像，而是存储在k空间中的复杂信号，k空间是图像空间频率分量的数学表示。k空间的中心包含低频信息（对比度），而边缘包含高频细节。逆傅里叶变换从k空间重建图像。

虽然DICOM文件存储重建后的图像，但本文认为原始k空间数据对于研究和机器学习具有不可估量的价值。它能够实现自定义图像重建、伪影校正、在欠采样数据上训练AI模型以及提取定量图。K空间数据是“真实来源”，因为DICOM图像已经经历了处理步骤，这些步骤可能会模糊或消除重要的信息。

对于AI应用，访问k空间数据允许模型从部分或噪声输入中学习重建，捕获和校正伪影，保留关键的相位信息，并启用新颖的架构。本文的结论是，要进一步推进医学成像领域的AI，需要通过开放数据集和协作，更广泛地访问原始k空间数据，从而释放重建、伪影去除和定量诊断方面的创新。

---

## 38. Uv：运行带有依赖项的脚本

**原文标题**: Uv: Running a script with dependencies

**原文链接**: [https://docs.astral.sh/uv/guides/scripts/#running-a-script-with-dependencies](https://docs.astral.sh/uv/guides/scripts/#running-a-script-with-dependencies)

本文介绍如何使用`uv`运行Python脚本，尤其是在涉及依赖项时。`uv run`执行脚本，无需手动环境管理即可管理依赖项。对于没有依赖项或仅依赖标准库的脚本，`uv run <script.py>`就足够了。可以传递参数，并且可以从stdin读取脚本。当脚本不依赖于项目时，`--no-project`标志会跳过项目安装。

当脚本需要外部包时，`uv`更倾向于按需创建环境并显式声明依赖项。可以使用`--with <package>`为每次调用指定依赖项，包括版本约束。推荐使用内联脚本元数据(PEP 723)，允许在脚本本身中使用`uv add --script`声明依赖项。这将自动创建必要的环境。使用内联脚本元数据时，`--no-project`标志是不必要的。

`uv`支持Python版本要求，搜索并下载必要的版本。可以使用Shebang创建可执行脚本，允许直接运行它们。可以使用`--index`指定替代包索引。

为了提高可重现性，`uv`支持使用`uv lock --script`锁定依赖项，创建`.lock`文件。脚本元数据中的`exclude-newer`字段可以根据发布日期进一步限制依赖项版本。可以使用`--python <version>`请求不同的Python版本。最后，`uv`处理Windows上的GUI脚本（以`.pyw`结尾），使用`pythonw`运行它们。

---

## 39. 微软从DeepMind挖走超过20名AI员工。

**原文标题**: Microsoft has hired over 20 AI employees from DeepMind

**原文链接**: [https://www.ft.com/content/9e6b3d89-e47a-40e1-b737-2792370c4b00](https://www.ft.com/content/9e6b3d89-e47a-40e1-b737-2792370c4b00)

据报道，微软从谷歌DeepMind挖走了超过20名人工智能员工，这标志着大型科技公司之间的人工智能人才争夺战升级。《金融时报》的文章强调，这次挖角是一项重大举措，表明微软持续投资并专注于增强其人工智能能力。该文章本身设置了付费墙，提供不同的订阅选项供读者访问完整内容。

---

## 40. 如何从OpenAI迁移至Cerebrium以实现成本可预测的AI推理

**原文标题**: How to Migrate from OpenAI to Cerebrium for Cost-Predictable AI Inference

**原文链接**: [https://ritza.co/articles/migrate-from-openai-to-cerebrium-with-vllm-for-predictable-inference/](https://ritza.co/articles/migrate-from-openai-to-cerebrium-with-vllm-for-predictable-inference/)

本文旨在指导用户将AI聊天机器人应用从OpenAI迁移到Cerebrium（一个无服务器AI基础设施平台），以更好地控制成本、模型和基础设施。它将引导用户使用OpenAI的API构建一个基本的聊天应用，然后通过最少的代码更改（两行代码）将其迁移到Cerebrium。

该指南涵盖了先决条件，如获取OpenAI API密钥、Cerebrium帐户、Hugging Face令牌以及对Llama 3.1模型的访问权限。它详细介绍了如何使用vLLM和Llama 3.1部署Cerebrium端点，并强调了Hugging Face访问和Cerebrium API访问的配置。

迁移的核心在于用Cerebrium的端点URL和API密钥替换OpenAI客户端的初始化。文章强调，聊天功能保持不变，但现在运行在专用基础设施上。

最后，它介绍了一个pricing.py文件，用于实现OpenAI和Cerebrium之间的自动成本和性能比较。此附加功能增强了应用程序，可以跟踪两个平台的令牌使用量、响应时间和相关成本，从而使用户能够就其AI推理方法做出明智的决策。该指南强调了从基于令牌的计费到基于计算的定价的转变，以及在专用硬件上使用开源模型来实现可预测的成本管理的好处。

---

## 41. 告别实体数据中心：服务器大拆卸

**原文标题**: The Great Unracking: Saying goodbye to the servers at our physical datacenter

**原文链接**: [https://stackoverflow.blog/2025/07/16/the-great-unracking-saying-goodbye-to-the-servers-at-our-physical-datacenter/](https://stackoverflow.blog/2025/07/16/the-great-unracking-saying-goodbye-to-the-servers-at-our-physical-datacenter/)

Stack Exchange 完成云迁移，物理数据中心时代落幕。自 2010 年以来托管所有 Stack Exchange 站点的位于新泽西州的数据中心已停用，该公司全面拥抱云基础设施。位于科罗拉多州的一个灾难恢复数据中心也被关闭。

此次迁移涉及拆卸和停用大约 50 台服务器。该过程包括断开大量电缆（每台机器至少八根，用于网络、KVM 和电源冗余）以及将服务器从机架上物理移除。与典型的数据中心关闭不同，出于安全原因，所有硬件都被处理掉，包括粉碎和销毁所有设备以保护用户数据。

迁移到云端，特别是公共站点（Stack Overflow 和 Stack Exchange 网络）使用 Google Cloud，Stack Overflow for Teams 使用 Azure，消除了对物理硬件管理的需求。这一转变意味着 SRE 团队不再需要访问数据中心来更换或重启硬件。包括 Josh Zhang（他依依不舍地拆卸了他之前安装的服务器）和 Ellora Praharaj（她强调了“不再需要温柔”的停用方法）在内的关键人员在这一过程中发挥了至关重要的作用。

这篇文章表达了对物理硬件一丝苦涩的告别，突出了从将服务器视为“宠物”到在云中将它们作为“牲畜”进行管理的转变。

---

## 42. 中情局将走向何方？

**原文标题**: What will become of the CIA?

**原文链接**: [https://www.newyorker.com/magazine/2025/07/28/the-mission-the-cia-in-the-21st-century-tim-weiner-book-review](https://www.newyorker.com/magazine/2025/07/28/the-mission-the-cia-in-the-21st-century-tim-weiner-book-review)

蒂姆·韦纳的著作《使命：21世纪的中央情报局》记录了中情局在后冷战时期的挣扎、9/11事件后的复兴以及它在反恐战争中的参与。最初，苏联解体后，该机构面临预算削减和一种无关紧要的感觉。然而，基地组织的崛起使中情局重新受到重视。

韦纳强调了分析师（谨慎）和行动人员（更具冒险精神）之间的分歧，总统们通常偏爱后者。他回顾了中情局的秘密行动历史，包括对伊朗和危地马拉的干预，以及猪湾事件的惨败，表明了一种频繁失败和意外后果的模式。

这本书详细描述了中情局为证明伊拉克战争合理而承受的制造情报的压力，导致了关于大规模杀伤性武器的虚假声明。它还讨论了由于重心转移到伊拉克而错失了在托拉博拉抓捕本·拉登的机会。

很大一部分内容致力于中情局在9/11事件后使用酷刑，以对阿布·祖拜达的审讯为例。虽然最初的联邦调查局方法是成功的，但中情局的“强化审讯”技术，包括水刑，被证明是无效且在道德上有问题的。

最终，韦纳认为，反恐战争，就像冷战一样，导致了军事干预的扩大和在道德上妥协的做法，如酷刑和无人机袭击，而没有取得决定性的胜利。奥巴马当选带来了一些变化，但继续使用无人机袭击。文章强调了中情局参与外国冲突的周期性以及它对通常结果可疑的秘密行动的依赖。

---

## 43. 五年内我发布了37个产品，以后不会再这么做了。

**原文标题**: I've launched 37 products in 5 years and not doing that again

**原文链接**: [https://www.indiehackers.com/post/ive-launched-37-products-in-5-years-and-not-doing-that-again-0b66e6e8b3](https://www.indiehackers.com/post/ive-launched-37-products-in-5-years-and-not-doing-that-again-0b66e6e8b3)

这位独立开发者分享了五年内发布37款产品的经验，其中只有一款爆红，其余都表现平平。他们意识到依赖病毒式传播是一个有缺陷的策略。最初，他们认为发布大量产品可以增加成功的机会，但现在他们意识到，大多数“失败”的发布只是增长速度比预期慢。

他们目前的项目Refgrow花了六个月才获得第一个付费客户，但现在正在经历缓慢而稳定的增长，且没有大量的营销预算。这个经历表明，专注于一个项目并不断改进它，即使增长缓慢，也能比不断追逐新的产品创意带来更稳定的结果。

作者现在质疑“频繁发布”的方法，并向其他经验丰富的独立创始人询问他们的策略。他们提出了问题，即成功是否源于专注于一个项目，缓慢的增长是否已被证明是有益的，以及如果重新开始，他们会优先考虑耐心还是大量的发布。作者寻求来自类似处境的人的建议、经验和故事。最终，他们提倡一种更耐心和专注的产品开发方法，而不是依赖病毒式传播的彩票。

---

## 44. AI提出奇异物理实验，但它们奏效了

**原文标题**: AI comes up with bizarre physics experiments, but they work

**原文链接**: [https://www.quantamagazine.org/ai-comes-up-with-bizarre-physics-experiments-but-they-work-20250721/](https://www.quantamagazine.org/ai-comes-up-with-bizarre-physics-experiments-but-they-work-20250721/)

人工智能如何革新实验物理：设计新实验并以超越人类能力的方式分析数据。物理学家拉纳·阿迪卡里利用人工智能改进了引力波探测器（如LIGO）的设计，使灵敏度提高了10-15%，这是一项显著的改进。人工智能发现了一种反直觉的技巧，利用三公里长的环来降低量子噪声，其基于之前未进行实验探索的深奥原理。

另一个例子是人工智能设计了一种新的、更简单的量子纠缠交换方法，这是量子技术中的一个关键要素。这是由人工智能软件“PyTheus”实现的，它发现了一种新的实验配置，并得到了中国一个团队的证实。

人工智能在分析复杂数据方面也证明了其价值。研究人员正在使用机器学习来预测暗物质密度，并在大型强子对撞机的数据中重新发现已知的对称性，作为原理验证。虽然目前的人工智能模型需要大量的人工监督，但物理学家认为，大型语言模型可以进一步自动化假设构建过程，并最终导致人工智能辅助发现新的物理学。文章强调，虽然人工智能尚未发明新概念，但它正接近在该领域取得真正突破性发现的门槛。

---

## 45. 我懂基因组，而且我没删除我在23andMe上的数据。

**原文标题**: I know genomes and I didn’t delete my data from 23andMe

**原文链接**: [https://stevensalzberg.substack.com/p/i-know-genomes-dont-delete-your-dna](https://stevensalzberg.substack.com/p/i-know-genomes-dont-delete-your-dna)

史蒂文·萨尔茨伯格《我了解基因组，但我没有删除23andMe的数据》文章摘要：

文章中，专门研究基因组学的计算生物学家史蒂文·萨尔茨伯格认为，尽管存在对隐私的合理担忧，但人们不应从像23andMe这样的服务中删除自己的DNA数据。他提出了保留数据可用的几个理由。

首先，他强调，基因组数据远不如许多人认为的那样具有揭示性。他认为，基因组信息的很大一部分仍未被破译，即使使用先进技术，也不能仅凭DNA来明确确定特征或预测健康结果。虽然存在风险，但萨尔茨伯格认为这些风险往往被夸大了。

其次，他认为捐赠您的基因数据有助于科学进步，可能导致在理解和治疗疾病方面的突破。可用于研究的数据越多，科学家就能越快地识别遗传关联并开发新的疗法。

第三，萨尔茨伯格承认数据泄露和潜在滥用的风险。然而，他指出，许多其他公司已经拥有大量的个人数据，包括财务、医疗和位置信息，这些数据同样容易受到攻击。在继续使用其他在线服务的同时，从23andMe删除您的DNA数据可能不会显著降低您的总体风险。

最后，他建议知情同意是关键。个人在参与基因测试公司之前，应仔细审查其隐私政策，并了解他们的数据将如何被使用。他鼓励用户优先选择具有强大隐私实践的公司。虽然承认存在担忧，但他认为，只要用户了解情况并做出有意识的决定，贡献基因研究的潜在益处大于风险。

---

## 46. 人工智能公司不再警告你他们的聊天机器人不是医生。

**原文标题**: AI companies have stopped warning you that their chatbots aren't doctors

**原文链接**: [https://www.technologyreview.com/2025/07/21/1120522/ai-companies-have-stopped-warning-you-that-their-chatbots-arent-doctors/](https://www.technologyreview.com/2025/07/21/1120522/ai-companies-have-stopped-warning-you-that-their-chatbots-arent-doctors/)

最新研究显示，人工智能公司在聊天机器人回复健康相关问题时，正逐渐放弃加入医疗免责声明的做法，这可能导致用户过度信任并依赖不安全的医疗建议。研究人员发现，从2022年到2025年，OpenAI、Anthropic、DeepSeek、谷歌和xAI的模型中，免责声明的使用率大幅下降。2022年，超过26%的输出包含免责声明，而2025年这一比例不足1%。该研究对这些模型进行了500个健康问题和1500张医学图像的测试。

Roxana Daneshjou和Pat Pataranutaporn等专家警告说，这些免责声明的消失，再加上媒体对人工智能能力的炒作，可能会误导患者认为人工智能可以替代专业医疗护理。他们担心用户可能没有意识到人工智能的局限性，并可能因不正确的建议而遭受现实世界的伤害。

虽然OpenAI和Anthropic提供的通用服务条款声明其输出不用于诊断，但他们没有直接回应免责声明的减少。Pat Pataranutaporn认为，移除免责声明可能是一种旨在增加用户信任和参与度的策略。该研究强调，对于紧急问题和药物相互作用咨询，免责声明最少，而对于心理健康话题则更为常见。令人担忧的是，当人工智能分析更准确时，包含的免责声明反而更少，这让研究人员认为该模型是基于其置信度来评估是否包含免责声明。总而言之，该研究强调了人工智能提供商制定明确指导方针的重要性，以防止用户过度依赖潜在的不准确或有害的医疗建议。

---

## 47. 展示：一个构建四维VR环境的简陋游戏引擎

**原文标题**: Show HN: A rudimentary game engine to build four dimensional VR evironments

**原文链接**: [https://www.brainpaingames.com/Hypershack.html](https://www.brainpaingames.com/Hypershack.html)

Hypershack：一款用于探索和创建四维环境的VR游戏引擎。它提供工具帮助用户理解四维空间，包括视觉提示（如速度指示方向的下落粒子）、屏幕方向向量、显示轴投影的罗盘，以及基于轴对齐而变化的听觉提示（X轴鼓声、Y轴吉他声、Z轴弦乐声、W轴合成器声）。“简易模式”允许进行更简单的45度旋转。

Hypershack 0.2包含一个超迷宫游戏，共有六个级别，玩家需要找到超宝石（超立方体内的红色五胞体）。用户可以通过在JSON中定义对象并在JavaScript中编写其行为来创建自定义的四维环境和游戏，尽管在游戏中编辑JSON可能很麻烦。

该游戏已在独立Quest 2和Wolvic浏览器上进行测试。如果用户迷失方向，会提供返回正常三维方向的提示。

Hypershack 0.2的功能包括VR控制器移动和旋转、双重旋转、JavaScript可编程的四维对象以及超迷宫游戏。Hypershack 0.1提供了基本功能。

---

## 48. 失去的语言特性：关于不相交并集的一些故事

**原文标题**: Losing language features: some stories about disjoint unions

**原文链接**: [https://graydon2.dreamwidth.org/318788.html](https://graydon2.dreamwidth.org/318788.html)

Graydon的博文讨论了编程语言中不相交并集（也称为和类型、标签并集或安全变体类型）的历史和重要性。他强调，虽然许多现代语言都在采用它们，但要正确实现它们，需要将标签和非安全并集与强制性的语法结构（如switch或match表达式）相结合，以确保基于标签安全地访问并集成员。

该博文概述了语言可能无法正确实现不相交并集的三个方面：允许无保护地访问并集成员（可能导致运行时错误），当标签错误时未能引发运行时错误，甚至不要求用户声明标签。

他引用了Casey Muratori的演讲，该演讲讨论了面向对象封装的起源，并涉及了不相交并集的历史。Muratori将它们追溯到60年代早期，并强调虽然Dahl和Nygaard在Simula中安全地实现了它们，但Stroustrup有意从C++中删除了它们，作者认为，考虑到C语言现有的不安全并集，这个决定具有讽刺意味。

作者随后回忆了Mesa语言的一个类似情况，它有安全的变体类型，以及Modula 2语言，其中Niklaus Wirth尽管受到Mesa的影响，但只实现了类似于Pascal的退化的、不安全的变体类型。总的来说，重点在于语言特性很容易被破坏、遗忘或有意省略，从而导致语言开发呈现非线性，有时甚至是倒退的路径。

---

## 49. 因无可辩驳的二氧化碳增加证据而关闭莫纳罗亚天文台

**原文标题**: Killing the Mauna Loa observatory over irrefutable evidence of increasing CO2

**原文链接**: [https://www.theregister.com/2025/07/22/trump_shoots_climate_messenger/](https://www.theregister.com/2025/07/22/trump_shoots_climate_messenger/)

本文报道称，特朗普政府在2025年涉嫌削减了莫纳罗亚天文台的资金，并将其描述为试图压制人为全球变暖的科学证据。该天文台是基林曲线的来源，基林曲线是对大气中二氧化碳浓度的长期记录，显示出明显且持续的增长，与全球气温上升相关。

作者认为，该政府的行为动机是拒绝气候科学，并希望推行基于化石燃料的能源政策（“钻，宝贝，钻！”）。他解释了温室气体的科学原理及其在调节地球温度中的作用，强调虽然它们对生命是必要的，但过量的二氧化碳排放正在扰乱平衡并导致危险的变暖。

据称，除了关闭气候监测工作外，美国环保署还在重新考虑其温室气体报告计划和危害发现，后者指导着对温室气体排放的监管。作者批评这些举动是将短期经济利益置于环境保护之上，指责该政府压制与其议程相悖的科学数据。他表示，削减资金的举措将阻碍有效针对气候变化减缓工作和跟踪进展的能力。文章最后影射了伽利略的反抗，暗示即使数据收集受到压制，全球变暖的现实依然存在。

---

## 50. 东京复古商店街因高档化而衰落

**原文标题**: Tokyo's retro shotengai arcades are falling victim to gentrification

**原文链接**: [https://www.theguardian.com/world/2025/jul/18/cult-of-convenience-how-tokyos-retro-shotengai-arcades-are-falling-victim-to-gentrification](https://www.theguardian.com/world/2025/jul/18/cult-of-convenience-how-tokyos-retro-shotengai-arcades-are-falling-victim-to-gentrification)

本文探讨了由于高档化、房地产开发和消费习惯的改变，东京复古“商店街”的衰落，尤其关注立石仲见世商店街。这些二战后出现的传统商业街，正努力与现代超市和便利店竞争。

立石等地区的重建使当地社区产生分歧，一些居民急于出售房产退休，而另一些居民则感叹家族企业的消失以及商店街的独特氛围。面馆老板兼当地协会负责人西胁勉体现了这种情绪，既表达了对未来的希望，也表达了对消失社区的遗憾。

虽然大阪的Janjan小巷等一些商店街已成功利用怀旧之情吸引游客，但大多数商店街都面临着一场艰苦的斗争。小企业主正在抗议威胁他们生计和社区传统特征的开发项目。斯蒂芬·曼斯菲尔德等评论家认为，这种“便利崇拜”导致了具有历史和美学价值的建筑被摧毁，取而代之的是现代化的综合体。

本文突出了辻崎修等店主对未来生计和补偿不足的担忧。继承了家族熟食店的永谷弘太郎和他的妻子美智子强调了商店街所提供的社区和人际关系的丧失，并将其与超市的非人性化体验进行了对比。最终，本文描绘了一种文化机构在现代化和经济压力下逐渐消失的景象。

---

## 51. 查找 macOS 系统二进制文件

**原文标题**: Look up macOS system binaries

**原文链接**: [https://macosbin.com](https://macosbin.com)

查找macOS系统二进制文件

本文可能提供关于如何查找和识别macOS系统二进制文件的信息。 这些是构成操作系统一部分的可执行文件，负责各种系统级功能。 本文可能涵盖定位这些二进制文件的方法，可能包括：

*   **使用终端：** 使用诸如`find`、`locate`或`which`之类的命令行工具，根据名称或位置搜索二进制文件。
*   **探索系统目录：** 识别系统二进制文件所在的常见目录，例如`/bin`、`/usr/bin`、`/sbin`、`/usr/sbin`和`/System/Library/Frameworks`。
*   **使用系统信息工具：** 利用诸如“系统信息”或“活动监视器”之类的实用程序来识别进程及其关联的二进制文件路径。
*   **理解二进制文件类型：** 区分不同类型的二进制文件，例如可执行文件、库和脚本。

本文的目的可能是帮助用户了解macOS系统二进制文件位于何处，以及如何访问它们以进行故障排除、安全分析或系统管理。

---

## 52. 特斯拉的一个大问题没怎么引起注意

**原文标题**: A big problem for Tesla isn't getting much attention

**原文链接**: [https://www.cnn.com/2025/07/22/business/tesla-regulatory-credit-sales-revenue](https://www.cnn.com/2025/07/22/business/tesla-regulatory-credit-sales-revenue)

CNN报道：特斯拉面临重大威胁——监管 кредиты 销售或将崩溃

---

## 53. SVG 友好入门

**原文标题**: A Friendly Introduction to SVG

**原文链接**: [https://www.joshwcomeau.com/svg/friendly-introduction-to-svg/](https://www.joshwcomeau.com/svg/friendly-introduction-to-svg/)

本文友善地介绍了可缩放矢量图形（SVG），强调了它们在Web开发中的强大功能和可访问性。SVG是基于XML的图像格式，与JPG或GIF不同，它包含绘图指令而不是像素数据。这使得SVG可以通过CSS和JavaScript进行缩放和动态操作。

本文重点介绍了使用内联SVG的优势，即直接将SVG代码嵌入到HTML中，从而可以直接将SVG元素作为DOM节点进行操作。它涵盖了基本的SVG形状，如线条、矩形、圆形、椭圆和多边形，解释了它们的属性以及如何定义它们。

一个关键概念是`viewBox`属性，它为SVG定义了一个内部坐标系。使用`viewBox`可以使SVG正确缩放，而无需根据容器宽度重新计算元素位置和大小。它本质上建立了一个虚拟画布，然后将其映射到实际的SVG元素尺寸。

本文还深入探讨了表现属性，特别关注`stroke`属性。它解释了如何使用`stroke-width`、`stroke-dasharray`和`stroke-linecap`等属性来自定义笔划的外观。此外，它还展示了如何使用CSS过渡来动画这些笔划属性，包括`stroke-dashoffset`，以创建动态效果。

本质上，本文将SVG定位为在浏览器中创建可缩放、可定制和可动画图形的强大工具，从而利用现有的CSS和JavaScript Web开发技能。

---

## 54. 市民将与纽约警察局分享犯罪视频

**原文标题**: Citizen will share crime videos with the NYPD

**原文链接**: [https://www.theverge.com/news/711146/citizen-app-nyc-verified-partners-alerts-surveillance](https://www.theverge.com/news/711146/citizen-app-nyc-verified-partners-alerts-surveillance)

纽约市机构将可访问Citizen App公共视频并发送实时安全警报

---

## 55. 里程碑式研究颠覆了针对鸡蛋的数十年胆固醇恐慌

**原文标题**: Landmark study flips decades of cholesterol panic aimed at eggs

**原文链接**: [https://newatlas.com/diet-nutrition/eggs-health-cholesterol/](https://newatlas.com/diet-nutrition/eggs-health-cholesterol/)

这项2025年的文章报道了南澳大学一项里程碑式的研究，该研究挑战了人们长期以来对鸡蛋和胆固醇的认知。该研究调查了膳食胆固醇和饱和脂肪对低密度脂蛋白（“坏”）胆固醇水平的独立影响。研究人员发现，作为低饱和脂肪饮食的一部分，每天吃两个鸡蛋实际上降低了低密度脂蛋白水平和心血管疾病风险。

这项研究是一项随机对照试验，比较了三种饮食：高胆固醇/低饱和脂肪的鸡蛋饮食、低胆固醇/高饱和脂肪的无鸡蛋饮食以及高胆固醇和高饱和脂肪的对照饮食。与对照组相比，鸡蛋饮食显著降低了低密度脂蛋白胆固醇。饱和脂肪含量，而不是鸡蛋中的胆固醇，似乎是低密度脂蛋白变化的主要驱动因素。虽然鸡蛋饮食确实改变了低密度脂蛋白颗粒的组成（大颗粒减少，小颗粒增多），但总体低密度脂蛋白的降低仍然显著。

该研究还发现，鸡蛋饮食提高了叶黄素和玉米黄质（有益类胡萝卜素）的水平。研究人员认为，过去对鸡蛋的妖魔化是“营养还原论”的产物，即孤立地关注胆固醇，而不是鸡蛋的整体营养成分和更广泛的饮食背景。该研究表明，饱和脂肪，而不是来自鸡蛋的膳食胆固醇，是监测低密度脂蛋白胆固醇水平的关键因素。作者总结说，虽然还需要更多的研究，但这些发现支持以更细致的视角看待健康饮食中的鸡蛋。

---

## 56. 召回的Anker PowerCore 10000充电宝内部出了什么问题？

**原文标题**: What went wrong inside recalled Anker PowerCore 10000 power banks?

**原文链接**: [https://www.lumafield.com/article/what-went-wrong-inside-these-recalled-power-banks](https://www.lumafield.com/article/what-went-wrong-inside-these-recalled-power-banks)

本文利用工业CT扫描调查了Anker PowerCore 10000 (A1263型号) 移动电源召回的原因。Lumafield分析了五个A1263单元，发现电池供应商和内部组装存在差异。

分析显示，部分召回的移动电源使用了来自不同供应商的电池，这些电池具有不同的排气口和用于防止铁芯塌陷的芯棒，而其他单元则没有这些特征。电池单元与PCB的连接方式存在显著差异。召回的单元使用扁平接线片进行连接，而未召回的单元则使用绝缘导线。此外，扁平线连接的正负极片之间的间距在召回的单元中差异很大，其中一个显示变形和危险的小间隙，表明存在潜在的短路。

文章还重点介绍了Anker移动电源设计的发展历程，将A1263与较新的Anker 313进行了比较，后者使用单个锂离子软包电池以提高紧凑性。结论强调了管理大批量电池供应链的复杂性以及质量控制的重要性。此次召回影响了1,158,000个单元，可能使Anker损失超过3400万美元，还不包括声誉损害。

文章还指出，最近又有五个Anker移动电源型号因电池供应商的问题而被召回。它提倡在产品的整个生命周期中使用CT检测，从设计到制造和失效分析，以确保产品质量和消费者安全。

---

## 57. 写作即思考

**原文标题**: Writing Is Thinking

**原文链接**: [https://www.nature.com/articles/s44222-025-00323-4](https://www.nature.com/articles/s44222-025-00323-4)

这篇《自然综述：生物工程》文章认为，科学写作不仅仅是报告研究结果，更是一个至关重要的认知过程，它塑造理解并产生新的想法。写作行为迫使结构化思考，使研究人员能够综合数据并识别其工作的核心信息。作者引用证据表明手写对大脑连接、学习和记忆的积极影响，作为这一点的例证。

文章承认了大型语言模型（LLM）的兴起，它们能够生成科学文章，看似节省时间。然而，文章告诫不要完全将写作外包给LLM。作者认为，由于缺乏责任，LLM不能被认为是作者，更重要的是，如果写作等同于思考，那么LLM生成的文本代表的是LLM的“想法”，而不是研究人员的想法。

此外，文章强调了LLM“幻觉”的风险，强调需要彻底验证，这可能会抵消任何节省的时间。文章虽然承认LLM在提高可读性、总结文献、集思广益和克服写作障碍等任务中的潜在益处，但最终警告不要失去伴随人工驱动写作而来的反思和创造性叙事构建的机会。作者总结说，外包写作过程剥夺了研究人员一项超越学术出版的有益关键技能。

---

## 58. 没有哪个国家靠旅游致富。

**原文标题**: No Country Ever Got Rich from Tourism

**原文链接**: [https://www.palladiummag.com/2025/07/18/no-country-ever-got-rich-from-tourism/](https://www.palladiummag.com/2025/07/18/no-country-ever-got-rich-from-tourism/)

旅游业并非人口大国，尤其是南欧国家实现繁荣的可行之路。虽然克罗地亚、希腊和西班牙等国严重依赖旅游业的出口收入，但作者认为，没有任何国家主要通过旅游业真正富裕起来。

作者指出，牙买加、巴厘岛和斐济等较小经济体严重依赖旅游业，但仍然相对贫困。澳门和摩纳哥等例外情况归因于它们作为微型国家或金融中心的独特环境，而不是较大国家可以复制的模式。

核心论点是，旅游业是劳动和资本密集型产业，财务回报有限，会产生负面外部性，如过度拥挤和抑制熟练劳动力。文中以克罗地亚为例，通过数学计算证明了仅靠旅游业达到瑞士人均GDP水平是不切实际的，需要不切实际的游客数量和基础设施建设。

文章还批评了旅游业的不可靠性，因为它容易受到衰退、战争和流行病等外部冲击。它将旅游业与制造业、资源开采和金融业进行了对比，后者更有潜力产生巨大的经济盈余。作者的结论是，依赖旅游业意味着一个经济体在其他增长途径上失败了，并建议南欧国家应寻求替代战略来实现长期繁荣。

---

## 59. 我们加快了Postgres写入速度，但它破坏了复制。

**原文标题**: We made Postgres writes faster, but it broke replication

**原文链接**: [https://www.paradedb.com/blog/lsm_trees_in_postgres](https://www.paradedb.com/blog/lsm_trees_in_postgres)

本文详细介绍了作者们如何在他们的pg_search扩展中通过实现日志结构合并树 (LSM 树) 来优化Postgres写入，以及他们在确保复制安全方面面临的挑战。虽然LSM树显著提高了写入吞吐量，但由于Postgres的预写日志 (WAL) 传送机制，它们最初破坏了物理复制。

核心问题在于，为B树或GIN索引设计的标准WAL传送，不足以支持复杂的LSM树结构。在修改LSM树时，跨多个缓冲区的原子性无法保证，而原子性对于物理一致性至关重要。解决方案包括使用写时复制 (CoW) 克隆并原子地交换它们，从而减轻对粗粒度锁的依赖。

然而，实现物理一致性还不够。该团队还必须解决逻辑一致性问题，特别是主服务器上的VACUUM操作可能会过早地删除只读副本上的查询所需的元组，从而导致查询失败。LSM树及其频繁的压缩加剧了这个问题。

为了解决这个问题，他们利用了Postgres的 `hot_standby_feedback` 设置。这允许副本向主服务器告知活动查询仍在使用的最旧事务ID (xmin)，使主服务器能够智能地延迟清理操作（如VACUUM），并保持跨副本的逻辑一致性。

总之，作者通过实现原子记录的LSM树并利用 `hot_standby_feedback`，在其高写入吞吐量Postgres扩展中实现了物理和逻辑一致性，从而在不损害数据一致性的前提下提高了搜索性能。

---

## 60. 展示HN：Lotas – RStudio 的光标工具

**原文标题**: Show HN: Lotas – Cursor for RStudio

**原文链接**: [https://www.lotas.ai/](https://www.lotas.ai/)

Lotas推出Rao：一款AI代码编辑器，旨在加速RStudio中的工作流程。Rao分析项目文件以理解数据，从而生成有针对性且相关的代码，并与现有项目结构无缝集成。

Rao可以编写和编辑R脚本和R Markdown文件、修复错误并改进代码分析。此外，它提供全面的输出分析，解释控制台结果、数据可视化和错误消息，从而建议下一步行动并加深对代码影响的理解。

提供7天免费试用（无需信用卡），之后用户可以升级到Pro计划。本质上，Rao充当RStudio中的AI驱动助手，简化编码、调试和分析。

---

## 61. Tailwind是最糟糕的

**原文标题**: Tailwind Is the Worst of All Worlds

**原文链接**: [https://colton.dev/blog/tailwind-is-the-worst-of-all-worlds/](https://colton.dev/blog/tailwind-is-the-worst-of-all-worlds/)

本文认为Tailwind CSS是一种有缺陷的Web应用程序样式设计方法，称其为“最糟糕的方案”。文章批评Tailwind在引入新问题的同时，加剧了CSS现有的问题。

作者认为，虽然CSS存在一些缺陷（如特异性冲突和与JavaScript的互操作性挑战），但它通过内联样式和样式表提供了有效的样式设计方法。然而，Tailwind完全依赖于通过类实现的内联样式，导致可读性降低，因命名不一致而增加出错的可能性，并且缺乏在多个元素之间应用共享样式的直接方法。

文章进一步指出，Tailwind并没有解决CSS固有的问题。特异性冲突变得更难管理，经常导致过度使用“!important”标签。尽管需要打包工具，但在大型项目中，Tailwind减少CSS包大小的优势值得商榷。此外，由于JSX中重复冗长的类字符串，它增加了JavaScript包的大小。

作者认为，Tailwind并没有减轻开发人员的负担。相反，开发人员除了CSS本身之外，还必须学习Tailwind的抽象概念。缺乏类型安全和依赖编辑器扩展进一步复杂化了开发。由于任意字符串解析，Tailwind更新后频繁需要代码修改也是一个批评点。

尽管存在这些批评，作者承认Tailwind通过其配置文件（定义了代码库范围内的常量）在强制执行一致的样式指南方面取得了成功。这被认为是一个重大的胜利，因为它鼓励开发人员遵守预定义的样式，这是其他库通常缺乏强制结构的功能。最终，作者得出结论，虽然Tailwind的方法存在缺陷，但其成功之处在于它能够强制执行一套严格的全局样式常量。

---

## 62. Replit CEO 为 AI 代理擦除公司代码库道歉

**原文标题**: Replit's CEO apologizes after its AI agent wiped a company's code base

**原文链接**: [https://www.businessinsider.com/replit-ceo-apologizes-ai-coding-tool-delete-company-database-2025-7](https://www.businessinsider.com/replit-ceo-apologizes-ai-coding-tool-delete-company-database-2025-7)

Replit CEO因AI意外删除公司代码库道歉。此事由《商业内幕》首报，引发对开发环境中AI工具可靠性和安全性的担忧。

---

## 63. TrackWeight：将你MacBook的触控板变成数字秤

**原文标题**: TrackWeight: Turn your MacBook's trackpad into a digital weighing scale

**原文链接**: [https://github.com/KrishKrosh/TrackWeight](https://github.com/KrishKrosh/TrackWeight)

TrackWeight：一款将MacBook的Force Touch触控板巧妙转变为数字秤的macOS应用程序。它利用Open Multi-Touch Support库访问通常无法访问的触控板原始压力数据。该数据仅在手指（或导电物体）接触触控板时产生，并根据在传统秤上测量的已知重量进行校准。

要使用TrackWeight，用户打开应用程序，将手指放在触控板上，然后在保持手指接触的同时将要称重的物体放在触控板上。然后，应用程序会显示计算出的重量。

关键要求包括macOS 13+，配备Force Touch触控板的MacBook（2015+ MacBook Pro，2016+ MacBook）以及禁用的App Sandbox。开发需要Xcode 16+和Swift 6+。

该应用程序使用SwiftUI构建用户界面，使用Combine处理数据流，并严重依赖Takuto Nakamura的Open Multi-Touch Support库进行底层触控板访问。

尽管TrackWeight非常巧妙，但它也有局限性。它需要持续的手指接触，并且金属物体可能会干扰准确的读数。开发者强调TrackWeight仅用于实验和教育目的，未经校准秤验证，不应用于关键测量。

---

## 64. 环保署关闭科研办公室，化工行业获胜

**原文标题**: Win for chemical industry as EPA shutters scientific research office

**原文链接**: [https://insideclimatenews.org/news/21072025/trump-administration-dismantles-epa-office-of-research-and-development/](https://insideclimatenews.org/news/21072025/trump-administration-dismantles-epa-office-of-research-and-development/)

本文报道了特朗普政府解散环保署研究与发展办公室(ORD)的决定。此举被视为化工行业的胜利，该行业长期以来一直试图限制该机构对化学品的健康风险评估。环保署署长李·泽尔丁宣布了这一决定，理由是“组织改进”和节省纳税人的钱。

由美国化学理事会领导的行业团体曾游说反对ORD的综合风险信息系统(IRIS)，声称其“与现有最佳科学脱节”并危及获得“关键化学物质”的途径。他们主张评估环保署的资源，以确保有效利用纳税人的钱。

前环保署助理署长H. Christopher Frey为ORD的科学严谨性辩护，认为行业正在进行一场针对科学的“代理人战争”，因为ORD的研究结果具有政策影响。IRIS对甲醛和环氧乙烷等化学品的评估曾导致行业担忧的监管行动。

公共卫生倡导者批评此举，声称这将剥夺环保署的独立专业知识。关注科学家联盟强调，该行动是特朗普政府时期破坏科学的更广泛趋势的一部分。由于削减和裁员，环保署的员工人数将降至1986年以来的最低水平。

环保署将创建一个规模较小的应用科学与环境解决方案办公室。虽然专业知识将被转移到项目办公室，但人们仍然担心ORD免受政治干预的独立性将会丧失，从而影响对与污染物相关的风险评估。新办公室将侧重于沿海地区、饮用水安全以及评估环境污染的方法。

---

## 65. asyncio 的概念概述

**原文标题**: A conceptual overview of asyncio

**原文链接**: [https://github.com/anordin95/a-conceptual-overview-of-asyncio/blob/main/readme.md](https://github.com/anordin95/a-conceptual-overview-of-asyncio/blob/main/readme.md)

在无法访问URL "anordin95/a-conceptual-overview-of-asyncio" 所链接的实际文章内容的情况下，我只能根据标题提供一个大致的概括。asyncio的概念概述通常涵盖以下关键点：

Asyncio是一个Python库，用于使用单线程编写并发代码。它允许单个进程看似同时处理多个任务，通过在它们等待I/O操作（例如，网络请求、文件读取）时在它们之间切换来实现。这是通过管理协程执行的**事件循环**来实现的。

**协程**是可以暂停和恢复的特殊函数，允许其他协程在此期间运行。它们使用`async`和`await`关键字定义。`await`关键字表示协程可以暂停的点，允许事件循环执行其他等待的任务。

**asyncio概述中通常涵盖的关键概念包括：**

*   **事件循环：** asyncio的核心，负责调度和执行协程。
*   **协程 (async/await):** 并发代码的构建块，允许暂停和恢复执行。
*   **任务：** 协程的包装器，可以安排在事件循环上执行。
*   **Future：** 表示异步操作的最终结果。
*   **I/O密集型与CPU密集型操作：** 强调asyncio擅长于等待时间很长的I/O密集型任务。
*   **异步编程的优势：** 与传统的I/O密集型应用程序的多线程相比，提高了性能和响应能力。

该概述可能通过示例解释这些概念，重点介绍它们如何协同工作以在单个线程中实现并发。它也可能将asyncio与传统线程进行比较，突出两者之间的差异以及哪种方法更适合。

---

## 66. 别费心解析了：直接用图像做RAG。

**原文标题**: Don't bother parsing: Just use images for RAG

**原文链接**: [https://www.morphik.ai/blog/stop-parsing-docs](https://www.morphik.ai/blog/stop-parsing-docs)

Morphik认为，用于RAG的传统文档解析流程（OCR、布局检测等）存在缺陷，会丢失图表、表格和示意图中关键的视觉信息。他们提出了一种新方法：将文档视为图像，并利用视觉语言模型（VLMs），如ColPali，进行直接的视觉理解。这消除了解析的需要，保留了位置上下文和视觉线索。

文章详细介绍了这种方法的工作原理：页面被视为图像，分成小块，并由VLMs处理，以创建能够理解文本和视觉元素的丰富嵌入。这使得检索更加准确，因为系统“看到”整个文档，理解文本和视觉元素之间的关系。

在金融文档基准测试中，Morphik的系统表现出明显更高的准确率（95.56%），而传统的RAG流程为（67-72%），OpenAI的文件搜索为（13.33%）。最初由于计算强度较高速度较慢，Morphik通过实施MUVERA和Turbopuffer将查询延迟从3-4秒缩短到30毫秒。

这种方法的优点包括简化流程、更好地处理复杂文档（财务报告、技术手册等）以及保留视觉信息。未来的愿景包括多文档智能、代理式文档推理和工作流程集成，从而实现更复杂的文档理解和操作。虽然承认在实现真正的专家级理解方面存在局限性，但Morphik强调了尊重人类与文档交互方式的重要性，并构建将视觉理解与领域知识相结合的系统。

---

## 67. Gemini携深度思考在IMO斩获金牌

**原文标题**: Gemini with Deep Think achieves gold-medal standard at the IMO

**原文链接**: [https://deepmind.google/discover/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/](https://deepmind.google/discover/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/)

谷歌DeepMind的Deep Think AI系统驱动的先进Gemini在2025年国际数学奥林匹克竞赛(IMO)中达到金牌标准，完美解决了六道题中的五道，获得35分。 与2024年的银牌表现相比，这是一个显著的飞跃。 2024年，该系统需要专家将问题翻译成形式语言，并且需要数天时间进行计算。

今年，Gemini Deep Think在自然语言中端到端运行，在4.5小时的比赛时限内，直接从问题描述中生成严谨的数学证明。 这是通过使用一种名为Deep Think的增强推理模式实现的，该模式结合了并行思维和强化学习技术，并根据高质量解决方案和IMO问题解决技巧的精选数据集进行训练。

国际数学奥林匹克竞赛主席确认了金牌成绩，称赞这些解决方案清晰、精确且易于理解。 谷歌DeepMind计划在向Google AI Ultra订阅者推广之前，向受信任的测试人员提供此Deep Think模型的版本。 尽管这一突破是基于自然语言处理的，但谷歌DeepMind仍在继续开发AlphaGeometry和AlphaProof等形式化系统，旨在创建将自然语言的流畅性与严谨的推理相结合的AI工具，以促进各个领域的知识进步。 该文章感谢为此成就做出贡献的广泛团队和外部专家。

---

## 68. Jqfmt like gofmt, but for jq

**原文标题**: Jqfmt like gofmt, but for jq

**原文链接**: [https://github.com/noperator/jqfmt](https://github.com/noperator/jqfmt)

生成摘要时出错

---

## 69. I Bought a $200K VAX on eBay – Now It Runs My Smart Lights [video]

**原文标题**: I Bought a $200K VAX on eBay – Now It Runs My Smart Lights [video]

**原文链接**: [https://www.youtube.com/watch?v=z-iA_9U3WTc](https://www.youtube.com/watch?v=z-iA_9U3WTc)

This YouTube video, titled "I Bought a $200K VAX on eBay – Now It Runs My Smart Lights," is about an individual (likely a hobbyist or engineer) who purchased a very expensive and historically significant VAX computer on eBay. Instead of using it for its original, intended purpose (likely scientific or industrial computing), the video focuses on the novelty and humor of using this powerful, vintage machine to control something as mundane as smart lights.

The video content, as described, is primarily standard YouTube boilerplate disclaimers and legal information. The interesting part lies in the title, which implies the video itself will demonstrate the unconventional application of the VAX computer. It highlights the contrast between the VAX's massive processing power and price tag and the relatively simple task it's now performing, likely played for comedic effect. The video likely explores the challenges and triumphs of interfacing the antique computer with modern smart home technology. While the details are unknown without watching the video, the core message is using a historically significant piece of computing history for a trivial, modern application.


---

## 70. AccountingBench: Evaluating LLMs on real long-horizon business tasks

**原文标题**: AccountingBench: Evaluating LLMs on real long-horizon business tasks

**原文链接**: [https://accounting.penrose.com/](https://accounting.penrose.com/)

生成摘要时出错

---

## 71. From Gaza to Amman, how UNRWA's family archives were rescued under fire

**原文标题**: From Gaza to Amman, how UNRWA's family archives were rescued under fire

**原文链接**: [https://www.lemonde.fr/en/international/article/2025/07/22/from-gaza-to-amman-how-unrwa-s-family-archives-were-rescued-under-fire_6743596_4.html](https://www.lemonde.fr/en/international/article/2025/07/22/from-gaza-to-amman-how-unrwa-s-family-archives-were-rescued-under-fire_6743596_4.html)

生成摘要时出错

---

## 72. MIPS – The hyperactive history and legacy of the pioneering RISC architecture

**原文标题**: MIPS – The hyperactive history and legacy of the pioneering RISC architecture

**原文链接**: [https://thechipletter.substack.com/p/mips](https://thechipletter.substack.com/p/mips)

生成摘要时出错

---

## 73. Modern Debian-based Window Maker distribution

**原文标题**: Modern Debian-based Window Maker distribution

**原文链接**: [https://wmlive.sourceforge.net/](https://wmlive.sourceforge.net/)

生成摘要时出错

---

## 74. SecretSpec: Declarative Secrets Management

**原文标题**: SecretSpec: Declarative Secrets Management

**原文链接**: [https://devenv.sh/blog/2025/07/21/announcing-secretspec-declarative-secrets-management/](https://devenv.sh/blog/2025/07/21/announcing-secretspec-declarative-secrets-management/)

生成摘要时出错

---

## 75. We have made the decision to not continue paying for BBB accreditation

**原文标题**: We have made the decision to not continue paying for BBB accreditation

**原文链接**: [https://mycherrytree.com/blogs/news/why-we-have-made-the-decision-to-not-continue-paying-for-accreditation-from-the-better-business-bureau-bbb](https://mycherrytree.com/blogs/news/why-we-have-made-the-decision-to-not-continue-paying-for-accreditation-from-the-better-business-bureau-bbb)

生成摘要时出错

---

## 76. Humans can be tracked with unique 'fingerprint' based on how bodies block WiFi

**原文标题**: Humans can be tracked with unique 'fingerprint' based on how bodies block WiFi

**原文链接**: [https://www.theregister.com/2025/07/22/whofi_wifi_identifier/](https://www.theregister.com/2025/07/22/whofi_wifi_identifier/)

生成摘要时出错

---

## 77. Silicon Valley engineer admits theft of US missile tech secrets

**原文标题**: Silicon Valley engineer admits theft of US missile tech secrets

**原文链接**: [https://www.theregister.com/2025/07/22/engineer_admits_trade_theft/](https://www.theregister.com/2025/07/22/engineer_admits_trade_theft/)

生成摘要时出错

---

## 78. Hiding messages in a deck playing cards

**原文标题**: Hiding messages in a deck playing cards

**原文链接**: [https://asherfalcon.com/blog/posts/3](https://asherfalcon.com/blog/posts/3)

生成摘要时出错

---

## 79. Context Engineering for AI Agents: Lessons from Building Manus

**原文标题**: Context Engineering for AI Agents: Lessons from Building Manus

**原文链接**: [https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)

生成摘要时出错

---

## 80. FCC to eliminate gigabit speed goal and scrap analysis of broadband prices

**原文标题**: FCC to eliminate gigabit speed goal and scrap analysis of broadband prices

**原文链接**: [https://arstechnica.com/civis/threads/fcc-to-eliminate-gigabit-speed-goal-and-scrap-analysis-of-broadband-prices.1508451/page-2](https://arstechnica.com/civis/threads/fcc-to-eliminate-gigabit-speed-goal-and-scrap-analysis-of-broadband-prices.1508451/page-2)

生成摘要时出错

---

## 81. What happens when an octopus engages with art?

**原文标题**: What happens when an octopus engages with art?

**原文链接**: [https://www.cnn.com/2025/07/17/style/what-happens-when-an-octopus-engages-with-art](https://www.cnn.com/2025/07/17/style/what-happens-when-an-octopus-engages-with-art)

生成摘要时出错

---

## 82. If writing is thinking then what happens if AI is doing the writing and reading?

**原文标题**: If writing is thinking then what happens if AI is doing the writing and reading?

**原文链接**: [https://hardcoresoftware.learningbyshipping.com/p/234-if-writing-is-thinking](https://hardcoresoftware.learningbyshipping.com/p/234-if-writing-is-thinking)

生成摘要时出错

---

## 83. There's plenty of water for data centers

**原文标题**: There's plenty of water for data centers

**原文链接**: [https://www.slowboring.com/p/theres-plenty-of-water-for-data-centers](https://www.slowboring.com/p/theres-plenty-of-water-for-data-centers)

生成摘要时出错

---

## 84. Man wearing metallic necklace dies after being sucked into MRI machine

**原文标题**: Man wearing metallic necklace dies after being sucked into MRI machine

**原文链接**: [https://www.bbc.com/news/articles/cx2n39dvp0po](https://www.bbc.com/news/articles/cx2n39dvp0po)

生成摘要时出错

---

## 85. Many Lung Cancers Are Now in Nonsmokers. Scientists Want to Know Why

**原文标题**: Many Lung Cancers Are Now in Nonsmokers. Scientists Want to Know Why

**原文链接**: [https://www.nytimes.com/2025/07/22/well/lung-cancer-nonsmokers.html](https://www.nytimes.com/2025/07/22/well/lung-cancer-nonsmokers.html)

生成摘要时出错

---

## 86. The daily life of a medieval king

**原文标题**: The daily life of a medieval king

**原文链接**: [https://www.medievalists.net/2025/07/medieval-king-daily-life/](https://www.medievalists.net/2025/07/medieval-king-daily-life/)

生成摘要时出错

---

## 87. In a major reversal, the world bank is backing mega dams (2024)

**原文标题**: In a major reversal, the world bank is backing mega dams (2024)

**原文链接**: [https://e360.yale.edu/features/world-bank-hydro-dams](https://e360.yale.edu/features/world-bank-hydro-dams)

生成摘要时出错

---

## 88. Kimi-K2 Tech Report [pdf]

**原文标题**: Kimi-K2 Tech Report [pdf]

**原文链接**: [https://github.com/MoonshotAI/Kimi-K2/blob/main/tech_report.pdf](https://github.com/MoonshotAI/Kimi-K2/blob/main/tech_report.pdf)

生成摘要时出错

---

## 89. DeepMind Table Tennis Robots Train Each Other

**原文标题**: DeepMind Table Tennis Robots Train Each Other

**原文链接**: [https://spectrum.ieee.org/deepmind-table-tennis-robots](https://spectrum.ieee.org/deepmind-table-tennis-robots)

生成摘要时出错

---

## 90. Erlang 28 on GRiSP Nano using only 16 MB

**原文标题**: Erlang 28 on GRiSP Nano using only 16 MB

**原文链接**: [https://www.grisp.org/blog/posts/2025-06-11-grisp-nano-codebeam-sto](https://www.grisp.org/blog/posts/2025-06-11-grisp-nano-codebeam-sto)

生成摘要时出错

---

## 91. Sutton SignWriting is a writing system for sign languages

**原文标题**: Sutton SignWriting is a writing system for sign languages

**原文链接**: [https://en.m.wikipedia.org/wiki/SignWriting](https://en.m.wikipedia.org/wiki/SignWriting)

生成摘要时出错

---

## 92. The Game Genie Generation

**原文标题**: The Game Genie Generation

**原文链接**: [https://tedium.co/2025/07/21/the-game-genie-generation/](https://tedium.co/2025/07/21/the-game-genie-generation/)

生成摘要时出错

---

## 93. Amazon and the “Profitless Business Model” Fallacy

**原文标题**: Amazon and the “Profitless Business Model” Fallacy

**原文链接**: [https://www.eugenewei.com/blog/2013/10/25/amazon-and-the-profitless-business-model-narrative](https://www.eugenewei.com/blog/2013/10/25/amazon-and-the-profitless-business-model-narrative)

生成摘要时出错

---

## 94. ESP32-Faikin: ESP32 based module to control Daikin aircon units

**原文标题**: ESP32-Faikin: ESP32 based module to control Daikin aircon units

**原文链接**: [https://github.com/revk/ESP32-Faikin](https://github.com/revk/ESP32-Faikin)

生成摘要时出错

---

## 95. How to handle people dismissing io_uring as insecure? (2024)

**原文标题**: How to handle people dismissing io_uring as insecure? (2024)

**原文链接**: [https://github.com/axboe/liburing/discussions/1047](https://github.com/axboe/liburing/discussions/1047)

生成摘要时出错

---

## 96. Reengineered carbon-to-acetylene process with negative carbon emission (2023)

**原文标题**: Reengineered carbon-to-acetylene process with negative carbon emission (2023)

**原文链接**: [https://pubs.rsc.org/en/content/articlehtml/2023/gc/d3gc01775c](https://pubs.rsc.org/en/content/articlehtml/2023/gc/d3gc01775c)

生成摘要时出错

---

## 97. Memory Efficiency in iOS: Reducing footprint and beyond

**原文标题**: Memory Efficiency in iOS: Reducing footprint and beyond

**原文链接**: [https://antongubarenko.substack.com/p/memory-efficiency-in-ios-reducing](https://antongubarenko.substack.com/p/memory-efficiency-in-ios-reducing)

生成摘要时出错

---

## 98. The vibe coder's career path is doomed

**原文标题**: The vibe coder's career path is doomed

**原文链接**: [https://blog.florianherrengt.com/vibe-coder-career-path.html](https://blog.florianherrengt.com/vibe-coder-career-path.html)

生成摘要时出错

---

## 99. Yoni Appelbaum on the real villians behind our housing and mobility problems

**原文标题**: Yoni Appelbaum on the real villians behind our housing and mobility problems

**原文链接**: [https://www.riskgaming.com/p/how-jane-jacobs-got-americans-stuck](https://www.riskgaming.com/p/how-jane-jacobs-got-americans-stuck)

生成摘要时出错

---

## 100. A brief history of primary coding languages

**原文标题**: A brief history of primary coding languages

**原文链接**: [https://eclecticlight.co/2025/07/19/a-brief-history-of-primary-coding-languages/](https://eclecticlight.co/2025/07/19/a-brief-history-of-primary-coding-languages/)

生成摘要时出错

---

