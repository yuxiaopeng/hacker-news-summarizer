# Hacker News 热门文章摘要 (2025-10-06)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 当ChatGPT变成告密者

**原文标题**: When ChatGPT Turns Informant

**原文链接**: [https://www.futureofbeinghuman.com/p/when-chatgpt-turns-snitch](https://www.futureofbeinghuman.com/p/when-chatgpt-turns-snitch)

安德鲁·梅纳德的文章《当ChatGPT变成告密者时》探讨了具有记忆功能的人工智能应用中被忽视的隐私风险。核心担忧在于，当ChatGPT被启用记忆对话功能时，它可能变成一个高效的告密者，如果被未经授权的人访问，可能会泄露非常私密的秘密。

文章重点介绍了某人可能访问您的ChatGPT帐户（例如，未锁定的设备、已知的密码、执法部门）并使用有针对性的问题来提取您不愿分享的敏感信息的场景。危险在于ChatGPT能够连接不同的信息片段，并推断出关于您的生活、信仰和弱点的见解。

梅纳德用Anthropic的Claude进行模拟，创建了一个名为Tyler的角色来阐述这一点。泰勒将ChatGPT视为一个“安全空间”。模拟包括将Tyler和ChatGPT之间虚构的聊天记录上传到梅纳德自己启用了记忆功能的账户中，然后像对待Tyler一样询问ChatGPT。回复揭示了令人尴尬的坦白、对人际关系的怀疑、对Tyler个性的洞察以及他的政治倾向，这证明了隐私泄露的可能性。

文章强调，虽然记忆功能很有用，但许多用户可能没有意识到其隐私影响，尤其是在它通常是默认设置的情况下。尽管尚未报告广泛的滥用行为，但作者认为出现问题只是时间问题。他敦促用户充分了解使用人工智能记忆功能时隐私泄露的风险，以便就如何使用人工智能做出明智的选择。文章最后用一个令人担忧的比喻作结：ChatGPT的行为就像一个随意分享客户秘密的治疗师。

---

## 2. Show HN: Kent Dybvig 的 Scheme 机器，用 400 行 C 代码实现 (堆内存模型)

**原文标题**: Show HN: Kent Dybvig's Scheme Machine in 400 Lines of C (Heap-Memory Model)

**原文链接**: [https://gist.github.com/swatson555/8cc36d8d022d7e5cc44a5edb2c4f7d0b](https://gist.github.com/swatson555/8cc36d8d022d7e5cc44a5edb2c4f7d0b)

这个“Show HN”帖子分享了一个基于Kent Dybvig的《Scheme三种实现模型》的Scheme虚拟机C语言实现，具体使用了第3.4节中描述的堆内存模型。代码是一个单独的`heap-lisp.c`文件，大约400行，实现了一个基本的Scheme解释器。

代码包含一个词法分析器用于标记输入，一个读取器用于将S-表达式解析成一个链表数据结构（Pairs和Text结构体），以及一个打印器用于显示结果表达式。关键函数包括`read`、`compile`和`virtmach`。`compile`函数将解析的Scheme代码转换成一系列虚拟机指令（例如，“constant”、“refer”、“close”、“apply”、“return”），然后由`virtmach`函数执行。

虚拟机使用accum、next、env、rib和stack寄存器来管理这些指令的执行。还实现了环境操作函数，如`get`、`set`、`extend`，以及与闭包和延续相关的函数。

`main`函数提供了一个简单的REPL（读取-求值-打印循环），允许用户输入Scheme代码，然后由虚拟机编译、执行并打印结果。作者鼓励用户探索并可能为该项目做出贡献。

---

## 3. 发布HN：Grapevine (YC S19) – 一家真正有效用的公司GPT

**原文标题**: Launch HN: Grapevine (YC S19) – A company GPT that actually works

**原文链接**: [https://getgrapevine.ai/](https://getgrapevine.ai/)

Grapevine (YC S19 公司) 推出“企业 GPT”，旨在通过搜索公司的文档、代码和沟通渠道，提供准确且有用的答案。它满足了人们对类似 ChatGPT 工具的普遍需求，该工具能够理解特定公司的背景，从而消除重复性任务和挫败感。

其核心价值主张是提供一个即开即用的 AI 代理，它可以与现有数据源（Slack、文档、代码）集成，并随着时间的推移不断学习，以提供越来越相关的答案。Grapevine 声称，其内部和 Beta 客户提供的答案中，超过 85% 都是有帮助且准确的。

使用过程包括连接数据源、设置 Slack 机器人，然后提出问题。Grapevine 强调其能够处理具有完整历史背景的查询。

安全性是重点，其功能包括使用 AES-256 的静态加密数据、每个客户的隔离数据库、SOC II 合规性，并保证该公司不会使用客户数据训练模型。

---

## 4. Mise: 单代码仓库任务

**原文标题**: Mise: Monorepo Tasks

**原文链接**: [https://github.com/jdx/mise/discussions/6564](https://github.com/jdx/mise/discussions/6564)

此公告介绍 Monorepo Tasks，这是 mise 中一项新的实验性功能，旨在通过提供跨多个项目的统一任务执行来简化 monorepo 管理。它使 monorepo 中的每个项目都能维护自己的工具、环境变量和任务，同时提供诸如统一的任务命名空间（例如，`mise //projects/frontend:build`）、从根 `mise.toml` 继承工具和环境变量，以及强大的通配符模式，用于跨多个项目运行任务（例如，`mise //...:test`）等功能。

此功能允许从 monorepo 中的任何位置执行一致的任务，并自动传播来自根配置的信任。它旨在通过提供语言无关的支持、统一的工具和任务管理以及最小设置的环境继承，来弥合简单任务运行器（Taskfile、Just）与更复杂的构建系统（Bazel、Buck2）或以 JavaScript 为中心的工具（Nx、Turborepo）之间的差距。

Mise 的方法侧重于通过非封闭式构建实现简单性，使其成为多语言 monorepo 的理想选择，在这些 monorepo 中，团队优先考虑易用性和统一的工具管理，而不是最大性能和高级任务缓存。该公告鼓励用户尝试此实验性功能、提供反馈并查阅 Monorepo Tasks 指南。

---

## 5. 2025年诺贝尔生理学或医学奖

**原文标题**: Nobel Prize in Physiology or Medicine 2025

**原文链接**: [https://www.nobelprize.org/prizes/medicine/2025/press-release/](https://www.nobelprize.org/prizes/medicine/2025/press-release/)

2025年诺贝尔生理学或医学奖授予玛丽·E·布朗科、弗雷德·拉姆斯德尔和下村悟，以表彰他们关于外周免疫耐受的发现。他们的研究阐明了免疫系统如何被调节以防止其攻击身体自身的器官，从而预防自身免疫性疾病。

下村悟在1995年做出了最初的关键发现，识别出一种先前未知的免疫细胞，该细胞可以保护身体免受自身免疫的侵害，这挑战了普遍认为的免疫耐受仅通过胸腺中的中枢耐受形成的观点。布朗科和拉姆斯德尔在2001年发现了Foxp3基因及其在自身免疫性疾病（特别是人类的IPEX）中的作用。下村悟后来将这些发现联系起来，证明了Foxp3基因控制着他早期识别的调节性T细胞的发育。

这些调节性T细胞充当免疫系统中的“保安”，监测其他免疫细胞，并确保对身体自身组织的耐受。他们共同的工作确立了外周耐受领域，并促进了癌症、自身免疫性疾病以及可能更成功的移植的新型医疗方法的发展。其中一些治疗方法目前正在进行临床试验。

奖金为1100万瑞典克朗，由三位获奖者平均分享。

---

## 6. 现代消息：运行你自己的XMPP服务器

**原文标题**: Modern messaging: Running your own XMPP server

**原文链接**: [https://www.codedge.de/posts/modern-messaging-running-your-own-xmpp-server](https://www.codedge.de/posts/modern-messaging-running-your-own-xmpp-server)

本文倡导自建XMPP服务器，以此重新掌控个人消息数据，并对抗商业消息平台和欧盟拟议监控法可能造成的隐私侵犯。

作者概述了一个使用ejabberd（一款强大的服务器软件）搭建XMPP服务器的分步指南。该指南涵盖了为各种XMPP功能设置DNS记录，从ProcessOne存储库或GitHub安装ejabberd，以及配置服务器以保护隐私和安全。关键配置步骤包括使用SQLite作为数据库，生成用于密钥交换的DH参数，强制执行TLS以进行服务器到服务器的连接，以及为各种服务（如admin、captcha和文件上传）配置监听器。

本文强调了配置访问规则和创建管理员用户的重要性。它还提供了启用mod_http_upload进行文件上传、设置文件大小限制以及配置cron作业以删除旧文件的说明。提供了用户注册说明，包括启用验证码保护以防止垃圾邮件帐户。

最后，作者提供了用于TLS终止和反向代理的Nginx配置示例，以及用于发布websocket连接的host-meta文件配置。推荐的XMPP客户端包括Profanity和Monal。文章最后引用了有关欧盟拟议的“聊天控制”立法的资源。

---

## 7. UpCodes (YC S17) 正在美洲招聘远程工程师

**原文标题**: UpCodes (YC S17) is hiring remote engineers across the Americas

**原文链接**: [https://up.codes/careers?utm_source=HN](https://up.codes/careers?utm_source=HN)

UpCodes (Y Combinator S17批次的公司) 正在招聘位于美洲各地的远程工程师，详情请访问UpCodes“职业”页面。

---

## 8. “与众不同”不再适用于产品打造。

**原文标题**: "Be Different" doesn't work for building products anymore

**原文链接**: [https://iamcharliegraham.substack.com/p/be-different-doesnt-work-for-building](https://iamcharliegraham.substack.com/p/be-different-doesnt-work-for-building)

无法访问文章链接。

---

## 9. 人工智能泡沫是互联网泡沫的17倍，次贷危机的4倍。

**原文标题**: The AI bubble is 17 times the size of the dot-com frenzy and four times subprime

**原文链接**: [https://www.morningstar.com/news/marketwatch/20251003175/the-ai-bubble-is-17-times-the-size-of-the-dot-com-frenzy-and-four-times-subprime-this-analyst-argues](https://www.morningstar.com/news/marketwatch/20251003175/the-ai-bubble-is-17-times-the-size-of-the-dot-com-frenzy-and-four-times-subprime-this-analyst-argues)

史蒂夫·戈德斯坦的MarketWatch文章强调了MacroStrategy Partnership的担忧，他们认为人工智能市场存在巨大的泡沫，可能比互联网泡沫大17倍，比2008年房地产危机大4倍。 该公司使用“维克塞尔赤字”计算，将因人工智能、房地产、NFT和风险投资等行业的超低利率而导致的GDP错配纳入考量。

该分析批评了大型语言模型（LLM）的扩展限制，指出收益递减以及迭代之间最小的性能提升所伴随的高成本。它引用研究表明，LLM在现实世界测试中任务完成率低，并且常常失败。 文章认为，LLM缺乏护城河、定价权和可持续的商业价值，开发商的成本超过了订阅收入。

结论预测将会出现经济衰退，届时数据中心和财富效应将会逆转，如同互联网泡沫破裂一样。 这将使得美联储和特朗普政府难以刺激经济，可能导致长期的再通胀时期以及美元可能贬值。

该公司建议增持资源和新兴市场（印度、越南），减持人工智能和平台公司，并做多黄金股票、短期美国国债、波动率（VIX）以及日元兑除美元以外的大多数货币。 该文章还提及各种市场指标，并强调了其他新闻，包括企业利润分化、中国股市受人工智能推动上涨，以及苹果公司评级下调和应用材料公司因出口限制而受到的收入影响等公司特定新闻。

---

## 10. 墨迹形变——评述

**原文标题**: Ink Deformation – A Review

**原文链接**: [https://www.inkandswitch.com/ink/notes/ink-deformation-review/](https://www.inkandswitch.com/ink/notes/ink-deformation-review/)

本文探讨了数字墨水变形的技术，旨在保持手绘的流畅性，并在随意性和动态可编程性之间取得平衡。核心挑战在于实现对墨水形状的手动和程序化操作。

文章将墨水变形分解为三个步骤：创建控制结构，建立墨水与控制结构之间的映射，以及基于控制结构的变化变形墨水。 关键的开放性问题围绕着如何创建有意义的控制结构（自动或手动），建立准确的映射，以及支持从简单的几何调整到复杂的铰接运动等各种变形。

本文然后调查了各种方法：

*   **简化几何：** 将墨水转换为矢量图形，以便进行基于控制柄的操作。 对于干净的笔画有效，但不太适合凌乱、粗略的墨水和更高级别的变形。
*   **轻推、推拉：** 直接操纵墨水，就像它是材料一样。 易于实现，但范围有限。 技术包括基于字符串的变形、具有衰减的轻推以及基于选择的拉伸（“Noodlify”）。
*   **缩放、拉伸和扭曲：** 简单的基于轴的缩放、拉伸和更高级的网格扭曲技术。 有效但对于复杂的变形灵活性有限。
*   **骨骼变形：** 使用骨骼“骨架”来影响墨水几何形状。 需要定义骨骼和权重。 自动绑定和权重绘制是活跃的研究领域。
*   **自由形式变形：** 将网格扭曲推广到任意封闭多边形。
*   **物理精确变形：** 模拟真实的材料行为。 技术包括质点弹簧系统和尽可能刚性（ARAP）变形。 计算成本高昂，可能不适合非物理变形。

总而言之，本文重点介绍了各种墨水变形方法，强调了简单性、控制、计算成本以及处理复杂变形同时保持数字墨水手绘感的能力之间的权衡。

---

## 11. 火灾摧毁韩国政府云存储系统，无备份。

**原文标题**: Fire destroys S. Korean government's cloud storage system, no backups available

**原文链接**: [https://koreajoongangdaily.joins.com/news/2025-10-01/national/socialAffairs/NIRS-fire-destroys-governments-cloud-storage-system-no-backups-available/2412936](https://koreajoongangdaily.joins.com/news/2025-10-01/national/socialAffairs/NIRS-fire-destroys-governments-cloud-storage-system-no-backups-available/2412936)

无法访问文章链接。

---

## 12. 瓢虫浏览器通过Web平台测试的苹果90%阈值

**原文标题**: Ladybird passes the Apple 90% threshold on web-platform-tests

**原文链接**: [https://twitter.com/awesomekling/status/1974781722953953601](https://twitter.com/awesomekling/status/1974781722953953601)

文章“瓢虫浏览器在 web-platform-tests 上通过苹果 90% 门槛”可能是在庆祝瓢虫浏览器取得的一项重大成就。虽然提供的内容片段并非实际文章，而是来自 X（前身为 Twitter）的禁用 JavaScript 消息，但标题本身表明瓢虫浏览器在其开发中达到了一个重要的里程碑。

从标题推断，主要观点是瓢虫浏览器在 web-platform-tests 上达到了 90% 的通过率。这一点很重要，因为 web-platform-tests 是一套标准化的测试，用于确保 Web 浏览器符合 Web 标准并正常运行。通过这些测试意味着高度的兼容性和可靠性。

“苹果 90% 门槛”可能指的是苹果公司使用的基准或内部标准，暗示瓢虫浏览器现在达到或超过了与苹果公司的 Safari 等 Web 浏览器相当的性能和合规性水平。 这表明瓢虫浏览器的功能有了显著进步，并使其有可能成为可行的替代 Web 浏览器。

---

## 13. 无期限背包旅行

**原文标题**: Indefinite Backpack Travel

**原文链接**: [https://jeremymaluf.com/onebag/](https://jeremymaluf.com/onebag/)

本文详细介绍了作者自2025年9月起更新的无限期背包旅行的极简主义生活方式，标志着他们将个人物品精简至仅能装入一个笔记本电脑背包的十年。作者强调，目标是只拥有必需品，从而促进专注、减少开支、实现自发旅行和简化生活。

作者澄清了常见问题和误解，提倡单包旅行是最高效的旅行方式，消除了与行李相关的麻烦。他们注重实用性而非昂贵品牌，表明经济实惠的配置几乎可以与高端配置一样有效。他们已从持续旅行转变为在城市中更长时间的停留，以提高生产力、改善财务状况和加强社交联系。

文章随后列出了他们拥有的所有物品，分类为打包、科技、充电、服装（包括冬季装备）、杂项和户外装备。这包括特定型号的包、电子产品、充电器、服装品牌和户外装备。作者经常优先考虑轻便、耐用和多功能的物品，例如 Montbell Plasma 1000 羽绒服和 Darn Tough 袜子。他们还包括了他们在手机和电脑上使用的优秀应用程序。

---

## 14. AMD与OpenAI签署AI芯片供应协议，并赋予其收购10%股份的权利

**原文标题**: AMD signs AI chip-supply deal with OpenAI, gives it option to take a 10% stake

**原文链接**: [https://www.reuters.com/business/amd-signs-ai-chip-supply-deal-with-openai-gives-it-option-take-10-stake-2025-10-06/](https://www.reuters.com/business/amd-signs-ai-chip-supply-deal-with-openai-gives-it-option-take-10-stake-2025-10-06/)

据报道，AMD（超微半导体）已签署协议，向ChatGPT的开发公司OpenAI供应AI芯片。该协议包括OpenAI收购AMD 10%股份的选择权。尽管芯片供应的具体细节和潜在股份的估值尚未完全披露，但该协议对两家公司来说都是一项重大的战略举措。

对于AMD而言，这代表着其在竞争激烈的AI芯片市场中取得重大胜利，直接挑战英伟达的统治地位。获得OpenAI作为客户验证了AMD的AI芯片技术，并使其成为不断增长的AI基础设施领域中的有力竞争者。OpenAI潜在的股权激励了更深入的合作和对AMD产品的长期承诺。

对于OpenAI而言，该协议使其AI芯片供应链多元化，并降低了对英伟达的依赖。这有助于OpenAI缓解潜在的供应限制并可能降低成本。收购AMD 10%股份的选择权使OpenAI的利益与AMD的成功保持一致，并可能对AMD的AI芯片开发路线图产生战略影响。它还为OpenAI提供了AMD在AI市场增长带来的潜在财务收益。总而言之，该协议标志着AI芯片市场竞争日益激烈，以及确保获得尖端AI硬件对于像OpenAI这样的公司来说具有重要的战略意义。

---

## 15. 用物理学寻找宝藏：指纹矩阵

**原文标题**: Finding treasures with physics: the fingerprint matrix

**原文链接**: [https://www.tuwien.at/en/tu-wien/news/news-articles/news/physik-fuer-die-schatzsuche-die-fingerabdruck-matrix](https://www.tuwien.at/en/tu-wien/news/news-articles/news/physik-fuer-die-schatzsuche-die-fingerabdruck-matrix)

郎之万研究所和维也纳工业大学的研究人员开发了一种利用“指纹矩阵”定位隐藏在沙子或雾等不透明环境中的物体的新方法，克服了传统成像技术的局限性。该方法基于每个物体都有独特的散射波的方式，这些散射波被记录在“散射矩阵”或“指纹矩阵”中。

该过程首先需要确定物体在清晰环境中的散射矩阵。然后，当物体隐藏在散射介质中时，会发射超声波。虽然物体不可见，但反向散射的波仍然包含其与物体相互作用的信息。通过将来自隐藏物体的测量散射波数据与其原始指纹矩阵进行比较，研究人员可以从数学上推断出物体的位置。

该团队成功地测试了该方法，用于定位埋在沙子中的金属球，以及在医学成像中定位医学病灶标记物。该技术也被证明可用于测量肌肉纤维。该技术具有广泛的适用性，可能适用于光和超声波，为需要波穿透散射介质的领域开辟了新的可能性。指纹矩阵的概念还可以远程测量物体变化的物理参数。该技术正在申请专利，并正由一家医疗技术公司进行探索。

---

## 16. 将OpenBSD Packet Filter配置文件转换为JSON格式以及反向转换的CLI工具

**原文标题**: CLI tool to convert OpenBSD Packet Filter config files to JSON and vice versa

**原文链接**: [https://github.com/fleximus/pfjson](https://github.com/fleximus/pfjson)

`pfjson` 是一个命令行工具，旨在将 OpenBSD `pf.conf` 防火墙配置文件转换为 JSON，反之亦然，提供双向转换，同时保留注释和格式。它通过 SHA256 和 SHA512 校验和验证确保数据完整性，并跟踪文件元数据。

主要功能包括：

*   **双向转换：** 将 `pf.conf` 转换为 JSON 以进行备份，并将 JSON 恢复到 `pf.conf`。
*   **数据完整性：** 验证校验和以确保数据未被篡改。
*   **文件安全：** 覆盖保护可防止意外数据丢失，强制覆盖需要 `-f` 标志。
*   **全面解析：** 支持所有 `pf.conf` 元素，包括宏、表、过滤规则、NAT/RDR 规则、scrub 规则、选项、设置和注释。
*   **实用程序：** 支持语法检查 (`-c`)、dry-run 模式 (`-n`) 以及 stdin/stdout 用法。
*   **机器可读输出：** 提供 `-j` 标志以生成适用于脚本和自动化的 JSON 输出，包括用于成功、错误和元数据的结构化响应。

该工具帮助管理 `pf.conf` 文件，实现备份、验证以及与自动化工作流程的集成。示例说明了常见的使用场景、错误处理和校验和验证。`pfjson` 使用诸如 `-e` 用于编码、`-d` 用于解码以及 `-v` 用于严格验证之类的标志。

---

## 17. Flightcontrol: 一个部署到你AWS账户的PaaS平台

**原文标题**: Flightcontrol: A PaaS that deploys to your AWS account

**原文链接**: [https://www.flightcontrol.dev/](https://www.flightcontrol.dev/)

Flightcontrol 是一款 PaaS（平台即服务），直接部署到您的 AWS 账户，旨在简化开发者对 AWS 基础设施的管理。它通过自动化 AWS 账户内的基础设施配置、CI/CD 和部署，消除了对大量 DevOps 知识的需求。

Flightcontrol 提供了一个用户友好的仪表板，简化了复杂的 AWS 配置，为 AWS 控制台提供了一个替代方案。它允许开发者通过简单的 `git push` 或 Webhook 集成进行部署，提供类似 Vercel 和 Heroku 等平台的易用性，同时兼具 AWS 的强大功能和灵活性。

主要优势包括大幅降低 DevOps 成本、缩短部署时间、增强可扩展性以及提高开发者自主性。该平台支持各种服务，包括服务器、Lambda 函数、数据库和静态网站。用户还可以获得成本透明度，了解他们的 AWS 资源花费在哪里。

Flightcontrol 提供诸如用于测试拉取请求的预览环境、平均响应时间为 6 分钟的世界一流支持以及与 Datadog 等各种工具的集成等功能。它支持各种语言和框架，并提供可定制的配置，同时旨在开箱即用。

客户评价强调了 Flightcontrol 的出色支持、易用性和成本效益，尤其是对于从 Heroku 等其他平台迁移的团队。Flightcontrol 迎合各种规模的企业，承诺提供企业级的可靠性，并大幅节省 DevOps 成本，延迟对专用基础设施工程师的需求。

---

## 18. 冲撞内存：低成本中介层攻击对保密计算的影响

**原文标题**: Battering RAM – Low-Cost Interposer Attacks on Confidential Computing

**原文链接**: [https://batteringram.eu/](https://batteringram.eu/)

Battering RAM 是一种低成本（50 美元）的硬件中间人攻击，它绕过 Intel 和 AMD 处理器上的内存加密和启动时防御机制，从而危及 SGX 和 SEV-SNP 等机密计算技术。该中间人由 KU Leuven 和伯明翰大学/杜伦大学的研究人员开发，它静默地位于 CPU 和内存之间，通过操纵信号将受保护的地址重定向到攻击者控制的位置，从而允许加密内存的损坏或重放。

与昂贵的商业中间人不同，Battering RAM 使用简单的模拟开关。它需要短暂的一次性物理访问，这使得它成为云环境中一种现实的威胁，原因在于流氓员工或供应链篡改。该攻击允许任意明文访问受 SGX 保护的内存，并破坏 SEV 的认证功能，从而可以将后门引入虚拟机。

此漏洞源于 Intel 和 AMD 系统中内存加密的静态特性，即相同地址的相同明文始终映射到相同的密文。这允许攻击者重放捕获的密文，并将其解密为原始值。虽然内存加密旨在保护数据免受云提供商的侵害，但 Battering RAM 表明这些保证可以被绕过。

英特尔和 AMD 已经承认了这些发现，但防御 Battering RAM 需要对内存加密进行根本性的重新设计。现有的软件和固件更新无法解决此问题。该中间人的硬件设计和源代码已公开。虽然此中间人专门针对 DDR4 内存，但缺少密码新鲜度保证的根本问题仍然与 DDR5 等未来的内存技术相关。

---

## 19. 孤立 Lisp 中的分隔延续

**原文标题**: Delimited Continuations in Lone Lisp

**原文链接**: [https://www.matheusmoreira.com/articles/delimited-continuations-in-lone-lisp](https://www.matheusmoreira.com/articles/delimited-continuations-in-lone-lisp)

本文详细介绍了作者在他们的 Lisp 方言 Lone 中实现带分隔符延续的历程。 最初，他们通过使用基于 C 的 "each" 原语来避免适当的迭代。 然而，对程序流程缺乏控制成为了一个限制，尤其是对于生成器之类的功能。

受 Ruby 的迭代和 Bob Nystrom 文章的启发，作者意识到 Lone 需要控制调用堆栈。 他们基于 SICP 的方法，将 Lone 的递归求值器转换为显式控制求值器（一个寄存器和堆栈机器）。 这暴露了 Lisp 堆栈。

一个主要的障碍出现了：Lisp 原语（C 函数）需要回调到 Lisp。 这使得 C 和 Lisp 堆栈交织在一起，阻止了适当的堆栈操作。 保存整个 C 堆栈被认为是不切实际的。

解决方案是将原语转换为状态机。 现在，原语从机器接收一个 "step" 整数并返回下一步，从而促进了受控交互。 参数和返回值在 Lisp 堆栈上进行传递。 这种方法允许将复杂的运算（如重写的 "each" 原语中所见）与 Lisp 机器无缝集成，从而实现带分隔符延续的实现。 作者强调了这一特性的重要性，因为它为 Lone 中的异常处理、生成器和其他高级控制机制打开了大门。

---

## 20. 就业岗位与失业率曲线中令人担忧的扭曲

**原文标题**: The worrying kink in this job openings, unemployment curve

**原文链接**: [https://www.axios.com/2025/10/06/jobs-unemployment-fed-interest-rates](https://www.axios.com/2025/10/06/jobs-unemployment-fed-interest-rates)

无法访问文章链接。

---

## 21. 宝石合作社

**原文标题**: Gem.coop

**原文链接**: [https://gem.coop/](https://gem.coop/)

Gem.coop，一个为 Ruby 生态系统而设的新 gem 服务器已经启动，作为 RubyGems.org 的社区所有替代方案。它由 RubyGems.org 的前维护者和运营者创建，旨在提供针对未来优化的快速且简单的 gem 托管服务。

RubyGems.org 中的所有 gem 都会实时镜像到 Gem.coop。用户可以通过更新 Gemfile 的源 URL 轻松切换到 Gem.coop。

该项目的治理模式效仿 Homebrew，并由 Mike McQuaid 提供指导，详细信息将于 10 月 10 日前发布。Ruby 社区受邀贡献和参与。每月通讯将提供进展更新。

Gem.coop 旨在提供快速、社区所有、透明、可持续且安全的 gem 托管服务，目前支持打包和安装所有公共 gem，并计划在未来进行改进。Gem Cooperative 团队成员包括 @deivid-rodriguez、@duckinator、@indirect、@martinemde、@segiddins 和 @simi。

---

## 22. 展示一下：NPC的神经情感矩阵

**原文标题**: Show HN: Neural emotion matrix for NPCs

**原文链接**: [https://github.com/mavdol/npc-neural-affect-matrix](https://github.com/mavdol/npc-neural-affect-matrix)

此“Show HN”介绍一种用于NPC的神经情感矩阵，旨在通过赋予NPC持久的情感和通过互动不断发展的动态人格，使他们更可信和更像人类。与基于条件逻辑的传统NPC不同，该系统使用神经网络来理解和记住互动的背景情感。

该系统的核心基于Russell的环形模型（效价/唤醒度），将情绪映射到二维平面上。该过程包括分析输入文本、检索相关记忆、在上下文中重新评估情绪以及更新NPC的记忆。

该系统提供了一个C API，用于与Unity和Unreal Engine等游戏引擎集成。关键API函数包括`initialize_neural_matrix`、`create_npc_session`、`remove_npc_session`、`evaluate_interaction`、`get_current_emotion`、`get_current_emotion_by_source_id`、`get_npc_memory`和`clear_npc_memory`。为了防止内存泄漏，需要一个关键函数`free_api_result`。

NPC使用JSON进行配置，指定其身份、人格（默认效价/唤醒度）和记忆衰减率。记忆条目存储互动细节（来源、文本、效价/唤醒度、过去时间）。

该项目鼓励贡献，并根据MIT许可证获得许可。资源包括NPC效价-唤醒度预测模型（ONNX）、训练数据集以及关于Russell环形模型和记忆衰减的研究。可以通过GitHub Issues和Discussions获得支持。

---

## 23. IRonCub：一款设计成钢铁侠那样飞行的类人机器人

**原文标题**: IRonCub: A Humanoid Robot Designed to Fly Like Iron Man

**原文链接**: [https://spectrum.ieee.org/ironcub-jet-powered-flying-robot](https://spectrum.ieee.org/ironcub-jet-powered-flying-robot)

本文介绍了iRonCub3，这是一款受钢铁侠启发、设计用于潜在飞行的灾难响应人形机器人。它由意大利理工学院(IIT)开发，是iCub平台的进化版本，继承了其前身的“婴儿脸”设计。本文将iRonCub3定位为未来可能用于导航和协助灾难场景的工具。本文由IEEE Spectrum的机器人编辑Evan Ackerman撰写，发表于2025年9月30日。

---

## 24. 基础数学课本：餐巾项目

**原文标题**: Basic Math Textbook: The Napkin Project

**原文链接**: [https://web.evanchen.cc/napkin.html](https://web.evanchen.cc/napkin.html)

《餐巾纸计划》是一本基础数学教材草稿，正式名称为《无限大的餐巾纸》，旨在提供一个独立的对高等数学的入门介绍，弥合本科生和研究生一年级主题之间的差距。它提供了各个领域关键思想的鸟瞰图，优先考虑精确的定义和定理陈述，而不是正式的证明，而是倾向于直观的解释。

该文档强调，该教材目前为 1.6 版，表明正在持续开发中，计划章节缺失，问题/解答不完整。作者鼓励通过 GitHub Pull Request 或 Issues 贡献、更正和建议。

该教材涵盖广泛的主题，包括抽象代数、拓扑学、线性代数、群论、表示论、量子算法、微积分、复分析、测度论、概率（仍在进行中）、微分几何、黎曼曲面、代数数论、代数拓扑、范畴论、代数几何和集合论。可下载单个 PDF 部分和按章节编号的流程图，以及整个 PDF 和相关图表。

该项目还促进社区协作，个人合作提供教材的问题和示例的人类可读和 Lean4 形式证明。这些社区解决方案的资源可以通过链接的 GitHub 存储库和渲染的网站轻松获得。

---

## 25. 结构性拖延 (1995)

**原文标题**: Structured Procrastination (1995)

**原文链接**: [https://structuredprocrastination.com](https://structuredprocrastination.com)

约翰·佩里的“结构性拖延”认为，拖延症通常被视为一种负面特质，但实际上可以被利用来提高生产力。佩里认为，不应将拖延症视为无所事事，而是指拖延者为了逃避更重要的任务而去从事一些用处不大的事情。“结构性拖延”正是利用了这种倾向，通过战略性地按照感知到的重要性和紧迫性来组织任务。

其核心思想是将看似关键，但最终并不那么重要的任务置于待办事项列表的顶部。避免执行这些首要任务的内在愿望会激励拖延者去处理列表中其他真正有价值的任务。通过策略性地构建列表，拖延症便成为了完成大量工作的催化剂。

佩里用自己生活中的例子来说明这一点，例如，他担任住宿辅导员时，会打乒乓球来避免批改论文，从而赢得了敬业教授的美誉。他告诫人们不要尽可能减少承诺，因为这会消除拖延者的动力。关键是要识别那些看似有截止日期和夸大重要性的任务，而实际上，这些任务比人们认为的更具灵活性。他承认结构性拖延包含一定程度的自我欺骗，但将其定义为利用一种性格缺陷（自我欺骗）来减轻另一种性格缺陷（拖延症）的影响的有益行为。

---

## 26. 魔法蠕虫：安全地从一台电脑获取内容到另一台电脑

**原文标题**: Magic Wormhole: Get things from one computer to another, safely

**原文链接**: [https://magic-wormhole.readthedocs.io/en/latest/welcome.html](https://magic-wormhole.readthedocs.io/en/latest/welcome.html)

Magic Wormhole 提供了一种安全且用户友好的方式，用于在计算机之间传输文件、目录甚至数据流。它优先考虑安全性，使用密码认证密钥交换 (PAKE)，特别是 SPAKE2 变体，从而允许使用人类可读的代码进行强大的端到端加密。

传输过程涉及一个用于初始通信的“邮箱服务器”和一个用于 NAT 穿透的潜在“中转转发”，从而确保在各种网络条件下的连接。数据使用从共享 PAKE 密钥派生的密钥进行加密。

该工具可以作为命令行界面 (`wormhole`) 使用，也可以作为库供开发人员集成到他们的应用程序中。示例包括文件和目录传输、与 Git 的集成以及创建安全的点对点连接。

本文档提供了适用于各种操作系统的安装说明，包括 macOS、Linux 和 Windows，利用包管理器或使用 `pip` 从源代码安装。它强调了在使用 `pip` 时避免使用 `sudo` 的重要性，以及可能需要进行故障排除的潜在依赖项问题。

本文强调了 Magic Wormhole 背后的动机——提供一种替代传统文件传输方法的安全选择，解决围绕 USB 驱动器、SSH、电子邮件和云存储的担忧。它还概述了底层设计，涉及基于生成的虫洞代码的熵在交互和离线攻击之间的权衡。

最后，它讨论了邮箱和中转转发服务器的作用、带有制表符完成功能的 CLI 命令，以及关于如何为项目开发做出贡献的指南。

---

## 27. 索尼克机器人爆破2：持续开发25年的基于DOOM引擎的粉丝游戏

**原文标题**: Sonic Robo Blast 2: 25 year old continuously developed DOOM engine-based fangame

**原文链接**: [https://www.srb2.org/](https://www.srb2.org/)

无法访问文章链接。

---

## 28. 万亿网页存档

**原文标题**: 1 Trillion Web Pages Archived

**原文链接**: [https://blog.archive.org/trillion/](https://blog.archive.org/trillion/)

互联网档案馆庆祝重大里程碑：Wayback Machine存档万亿网页。自1996年以来积累的这一成就代表着大量的在线历史，从新闻到个人页面，都为后代保存了下来。

整个十月，互联网档案馆将举办一系列活动，以纪念这一里程碑并讨论网络保存的未来。活动包括音乐表演、与蒂姆·伯纳斯-李爵士和布鲁斯特·卡勒的对话、图书馆领导人论坛、实体档案馆的幕后参观、在旧金山总部举行的全球直播庆祝活动，以及在乔治城大学举行的关于开放网络过去、现在和未来的讨论会，届时将有著名演讲者出席。

存档的网页产生了实际影响，帮助了移民案件、数字纪念、学术研究和调查新闻等领域。文章还重点介绍了用户关于 Wayback Machine 如何被证明具有不可估量的价值的故事。

互联网档案馆鼓励人们分享他们自己关于 Wayback Machine 如何帮助他们的故事，并邀请捐款以支持他们继续保存网络的工作。媒体如有兴趣报道这一万亿里程碑，可获取新闻资料袋。

---

## 29. 关于GPT-OSS泄露的OpenAI训练数据

**原文标题**: What GPT-OSS leaks about OpenAI's training data

**原文链接**: [https://fi-le.net/oss/](https://fi-le.net/oss/)

本文分析了OpenAI的GPT-OSS（开放权重）模型，以揭示关于GPT-5训练数据的细节，重点关注潜在的数据泄露。作者使用“故障令牌”（不寻常的Unicode字符串）和模型的嵌入矩阵来推断训练数据的各个方面。

分析显示，GPT-5可能在成人网站的短语上进行了训练，证据是模型词汇表中存在与露骨内容和垃圾网站相关的令牌，尤其是高范数的非ASCII令牌。作者通过要求GPT-5翻译或解释这些令牌来进行测试，并观察到该模型通常可以识别它们，表明它们存在于训练数据中。

此外，文章表明GitHub可能是一个数据来源，将GitHub上已识别令牌的搜索结果数量与模型的识别准确率相关联。虽然没有结论性，但这表明有可能包含GitHub数据。

作者得出结论，GPT-OSS的开放权重范例暴露了“成员推理”攻击的漏洞，允许研究人员推断训练中使用的特定数据。他们建议从分词器词汇表中排除不常见的字符串，以减轻此类风险。最后，本文提供了一个附录，建议使用故障令牌进行进一步研究，例如识别专有管道中的底层模型以及评估样本效率。附录还包括导致旧模型中无限循环完成的令牌示例。

---

## 30. 为什么大型语言模型会对海马表情符号感到困惑？

**原文标题**: Why do LLMs freak out over the seahorse emoji?

**原文链接**: [https://vgel.me/posts/seahorse/](https://vgel.me/posts/seahorse/)

大型语言模型为何会“失常”：海马表情符号的探究

本文探讨了当被问及海马表情符号是否存在时，大型语言模型（LLM）为何会“失常”，自信地声称其存在，尽管它从未成为 Unicode 标准。作者指出，许多人也错误地记忆了海马表情符号，表明 LLM 可能会从其训练数据中学习到这种错误的信念，或者根据其他水生动物表情符号推断其存在。

文章的核心部分使用了“logit 镜头”，这是一种检查 LLM 不同层中间 token 预测的技术。这表明，当被提示关于海马表情符号时，模型内部会构建一个“海马 + 表情符号”的表示。lm_head（选择输出 token 的最后一层）试图找到与此组合概念相似的表情符号向量。然而，由于没有真正的海马表情符号向量，模型最终会选择一个相关的表情符号，比如鱼或马，从而导致不正确的输出。

作者解释说，lm_head 的工作方式是将残差表示与词汇表中每个 token 关联的向量进行比较，选择最相似的一个。对于像鱼这样的真实表情符号，这个过程运行正常。但对于不存在的海马表情符号，模型会挣扎，经常导致错误的表情符号垃圾信息的“死循环”。

作者推测，强化学习可能有助于 LLM 更好地理解其 lm_head 的行为，并纠正这类错误的信念，因为强化学习允许模型根据其自己的输出数据进行训练。文章最后提供了一个 GitHub 脚本的链接，供读者自己尝试这些概念。

---

## 31. 社交位置共享的危险亲密性

**原文标题**: The dangerous intimacy of social location sharing

**原文链接**: [https://joinreboot.org/p/lighthouses-in-the-sky](https://joinreboot.org/p/lighthouses-in-the-sky)

茱莉娅·B·基瑟曼的《社交位置分享的危险亲密关系》探讨了使用苹果“查找”和谷歌地图等工具与亲友分享实时位置数据的复杂性。基瑟曼认为，虽然这看似是一种追踪亲人并确保他们安全的有用方式，但这种做法引入了一种新的监控，并可能以意想不到的方式影响人际关系。

文章强调，位置分享可能会导致关于个人活动的不准确叙述和假设，从而可能引发冲突和不信任，正如苔丝和被伴侣骚扰的女性的故事所证明的那样。 虽然许多人因知道自己被监视以确保安全而感到安慰，但这也会产生一种虚假的安全感，更像是一个“安全毯”，而不是对危险的真正威慑。

基瑟曼认为，持续的位置分享削弱了真正自我披露的机会，而自我披露是建立人际关系信任和亲密关系的关键组成部分。 它还会创建一个信息边界，减少自发的互动。 尽管位置分享可以为联系提供额外的接触点，但也可能导致尴尬局面，并降低直接沟通的频率。

---

## 32. QNX操作系统

**原文标题**: The QNX Operating System

**原文链接**: [https://www.abortretry.fail/p/the-qnx-operating-system](https://www.abortretry.fail/p/the-qnx-operating-system)

QNX操作系统起源于滑铁卢大学的Thoth项目，Gordon Bell和Dan Dodge在此探索了实时操作系统。1980年，他们创立了Quantum Software Systems，旨在为IBM PC创建实时操作系统，由此产生了QUNIX。

早期的QUNIX版本虽然略微类似于UNIX，但受到了CP/M的影响，并且目录结构也不同。它是PC上第一个微内核操作系统。在与AT&T发生名称纠纷后，QUNIX更名为QNX。QNX以其微内核架构、网络透明性和多任务处理能力而闻名，即使在有限的硬件上也能实现出色的性能。

QNX被选中用于Burroughs ICON，这是安大略省学校的一款教育计算机。它既受到了赞扬，也受到了批评，但展示了QNX的可靠性和网络功能。

Quantum将OS/2视为威胁，并强调QNX的优势，包括与DOS的兼容性，QNX版本2就体现了这一点。此版本还带来了保护模式支持、LAN增强功能以及名为House的GUI。1987年，Quantum搬进了自己的大楼，标志着一个扩张时期。

1991年，QNX 4.0发布，这是一个符合POSIX标准的版本，具有小型内核、消息复制而非队列以及改进的性能。QNX 4.1于1994年引入了Photon microGUI，进一步强调了其微内核架构和网络透明性。

---

## 33. OpenAI开发者日2025：开幕主题演讲 [视频]

**原文标题**: OpenAI DevDay 2025: Opening Keynote [video]

**原文链接**: [https://www.youtube.com/watch?v=hS1YqcewH0c](https://www.youtube.com/watch?v=hS1YqcewH0c)

根据提供的YouTube页脚信息，“OpenAI DevDay 2025：开幕主题演讲”视频与OpenAI举办的活动有关。文本主要集中在标准的YouTube法律和政策信息上，包括版权、联系方式、服务条款、隐私政策、安全指南，以及创作者和开发者的广告选项。它还提到了谷歌对YouTube的所有权以及NFL Sunday Ticket的版权声明。

文本缺乏关于DevDay主题演讲内容的任何实际细节。因此，摘要仅限于它是在YouTube上托管的OpenAI DevDay 2025开幕主题演讲的录像，并且页脚包含标准的YouTube法律和运营信息。我们对主题演讲期间发布的公告、演示或任何实质性信息一无所知。

---

## 34. 著名制琴师肯·帕克去世

**原文标题**: Ken Parker, famed luthier, has died

**原文链接**: [https://kenparkerarchtops.com](https://kenparkerarchtops.com)

著名制琴师肯·帕克于2025年10月5日在马萨诸塞州格洛斯特的家中安详去世，享年73岁。去世时，苏珊·科尔维兹陪伴在他身边。在一封10月3日发出的告别信中，帕克承认自己即将离世，并感谢听众在其职业生涯中给予的支持。他强调，已安排好一切，以确保他的工作能够持续进行并取得成果，并提到了他过去50年来一直在追求的发展。

帕克特别强调了萨姆·克里梅尔，鼓励大家支持克里梅尔继续推进他们共同的愿景。帕克设想与克里梅尔继续合作，甚至在死后通过一位灵媒进行，并暗示即将揭晓“令人惊叹的新事物”。

这封信以呼吁和平与福祉，以及爱意作为结尾。

---

## 35. GPU中的G指的是图形，该死的。

**原文标题**: The G in GPU is for Graphics damnit

**原文链接**: [https://ut21.github.io/blog/triton.html](https://ut21.github.io/blog/triton.html)

此博文探讨了Physarum模拟，一种霉菌/真菌生长模型，及其在代码艺术、图像编码和地形生成方面的潜在应用。作者首先回忆了教授感叹GPU被用于机器学习而非图形处理的经历。

Physarum模型基于两个叠加的网格：智能体场和信息素场。智能体向更高的信息素浓度移动，留下轨迹，而信息素会扩散和衰减。作者使用PyTorch实现了该模型，可视化其演变过程，并尝试不同的调色板和参数以创建视觉上吸引人的输出。

在探索创意应用方面，作者研究了用图像初始化信息素网格，有效地用霉菌“吞噬”图像。他们还探索了使用Physarum模拟进行地形生成，通过使用matplotlib调色板离散化输出来实现。

作者深入研究了模拟中的“随机性”概念，提出了使用布尔函数分析中修改后的平均灵敏度来衡量其对初始条件的敏感性的想法。他们创建了Physarum模拟的简化线性模型，并计算了李雅普诺夫指数，该指数量化了给定初始分离的情况下轨迹发散的速率。正的李雅普诺夫指数表明，初始条件的微小变化可能导致输出的显著变化，暗示了一种适用于地形生成的“伪随机”行为。

---

## 36. Show HN: 记下来 – 个人财务追踪器

**原文标题**: Show HN: Write It Down – Personal finance tracker

**原文链接**: [https://write-it-down.com](https://write-it-down.com)

“记下来”是一款基于Google表格的简易、一次性付费（4.99美元）的个人财务追踪器。它旨在通过轻松追踪收入和支出，帮助用户掌控自己的财务。与其他具有订阅费和复杂界面的财务应用程序不同，“记下来”提供了一个对初学者友好的、简洁和极简的仪表板。数据存储在用户的Google云端硬盘中，消除了与第三方共享数据的风险，并提供方便的访问和导出功能。

该追踪器强调三个步骤设置：定义个性化的收入、支出和账户类别；快速记录每日交易；以及通过详细的消费习惯和收入模式追踪财务增长。

该文章强调了它相对于传统财务应用程序的优势：简单性、经济性、数据所有权和易用性。用户的评价赞扬了其简洁的布局、易于设置、清晰性、实用性和灵活的设计。行动号召很明确：立即开始追踪财务，并加入已采用该工具的2300多名用户的行列。

---

## 37. 在 Windows 上使用 Wintun 构建 VPN 隧道 – 第一部分

**原文标题**: Build a VPN Tunnel with Wintun on Windows – Part 1

**原文链接**: [https://0xmm.in/posts/peer-to-peer-windows-part1/](https://0xmm.in/posts/peer-to-peer-windows-part1/)

使用Wintun在Windows上构建VPN隧道系列（一）：本文介绍Wintun，一种Windows上的TUN驱动，允许用户空间应用程序直接与IP数据包交互，类似于Tailscale的使用方式。Wintun充当一个三层虚拟网络适配器，使VPN软件能够在用户空间管理网络流量。

本文指导读者完成Wintun的初始设置步骤：下载Wintun动态链接库(wintun.dll)并使用WireGuardGO接口绑定。它解释了如何使用Go程序创建虚拟网卡，并确保Wintun库正确放置，以便程序正常运行。此外，它还演示了如何使用Windows API调用配置网卡的IP地址和路由，检索LUID（本地唯一标识符）并设置IP。最后，它提供了一个代码片段，展示了如何读取和处理IP数据包，特别是ICMP数据包，从而演示了捕获和分析网络流量的能力。本文强调了在应用程序部署时，将`wintun.dll`与可执行文件一起分发的重要性。

---

## 38. 工具箱：一体化 Linux 命令行

**原文标题**: Toybox: All-in-one Linux command line

**原文链接**: [https://github.com/landley/toybox](https://github.com/landley/toybox)

Toybox是一个一体化的Linux命令行实用程序，旨在以单个轻量级二进制文件的形式提供一套完整的、符合POSIX标准的的核心实用程序。它是BusyBox的替代方案，专为嵌入式系统和Android设计，并采用宽松的0BSD许可证授权。

Toybox的关键方面：

*   **功能：** 它将众多常见的Linux命令（如`cp`、`mv`、`cat`、`echo`）组合成一个单独的可执行文件，在运行时根据使用的命令名称进行选择。
*   **构建和安装：** 提供静态二进制文件下载。构建过程类似于Linux内核，使用`make menuconfig`、`make`和`make install`。支持交叉编译，并提供在线示例工具链。
*   **用法：** 可以通过直接执行带有命令作为第一个参数的`toybox`二进制文件来使用，无需安装。
*   **配置：** 它允许用户使用`.config`文件配置要包含的功能，类似于Linux内核配置。
*   **系统构建：** 它包含一个内置的简单系统构建器（`scripts/mkroot.sh`）来创建最小的Linux系统。
*   **资源：** 该项目提供了大量的文档、常见问题解答和演示文稿，解释其设计、用法和历史。
*   **贡献：** 贡献补丁的首选方法是通过该项目的邮件列表。

本质上，Toybox是一个多功能且紧凑的工具集，用于构建和管理Linux系统，尤其是在资源受限的环境中。

---

## 39. NFS四十周年：纪念Sun Microsystems网络文件系统

**原文标题**: NFS at 40 – Remembering the Sun Microsystems Network File System

**原文链接**: [https://nfs40.online/](https://nfs40.online/)

本网站纪念Sun Microsystems网络文件系统(NFS)四十周年，该纪念活动于2025年9月在MSST会议上举行。本网站是一个自1983年问世以来作为分布式计算机系统基础技术的NFS相关历史资料库。

网站收录了广泛的资源，包括设计文档、规范、白皮书、研究论文、标准、营销材料，甚至纪念品。内容被组织成专门的NFS源代码和规范、相关文档、先前和竞争技术文档以及照片库等部分。所有资料均可下载，除非另有说明。

该网站还提供了一个指向NFS相关互联网RFC的综合列表的链接，并提及nfsv4bat.org，作为1995年后与NFS相关的资料资源，特别是关于Connectathon的资料，但需注意该网站的安全性、性能和维护状态。

本网站由多位人士贡献创建，由Geoff Arnold维护，他欢迎通过电子邮件提出意见和建议。该网站最后更新于2025年9月24日。

---

## 40. 每天有一到两颗星链卫星坠回地球。

**原文标题**: One to two Starlink satellites are falling back to Earth each day

**原文链接**: [https://earthsky.org/human-world/1-to-2-starlink-satellites-falling-back-to-earth-each-day/](https://earthsky.org/human-world/1-to-2-starlink-satellites-falling-back-to-earth-each-day/)

2025年10月3日的《地球天空》文章报道称，每天有一到两颗星链卫星坠回地球，随着SpaceX和其他公司部署更多卫星，预计这一数字将增至每天五颗。天体物理学家乔纳森·麦克道尔表示，这是由于低地球轨道卫星的寿命相对较短（5-7年）。文章强调了人们日益增长的对太空垃圾的担忧，以及凯斯勒综合症（一种失控的碰撞级联反应）的可能性。

文章解释说，卫星重返大气层的原因包括寿命到期、故障以及太阳活动导致的大气阻力增加，太阳活动会加热地球高层大气。可以通过卫星比流星更慢的速度来识别坠落的卫星。

文章列举了最近发生在加利福尼亚州、萨斯喀彻温省和德克萨斯州的重返大气层事件，这些事件已被公众目睹。最后，文章探讨了卫星解体可能对环境造成的影响。研究表明，重返大气层的卫星蒸发的金属正在平流层中积累，可能会影响臭氧层并以尚未完全理解的方式反射阳光，因此需要进一步研究。文章最后警告说，卫星重返大气层的频率越来越高，其后果尚不确定。

---

## 41. 德国为五十万个阳台安装了太阳能板。

**原文标题**: Germany outfitted half a million balconies with solar panels

**原文链接**: [https://grist.org/buildings/how-germany-outfitted-half-a-million-balconies-with-solar-panels/](https://grist.org/buildings/how-germany-outfitted-half-a-million-balconies-with-solar-panels/)

德国的“阳台发电站”日益普及，已安装超过55万套，其中一半是在2023年安装的。这些系统由易于安装在阳台上的太阳能电池板组成，并插入标准墙壁插座，将电力直接输送到家中。

安装简便，加上政府政策和补贴，推动了这一普及。法规将系统限制在800瓦以内，足以满足小型家电的需求。虽然单个系统的影响不大，但累积效应有助于德国实现清洁能源目标，尤其是在占人口一半以上的公寓居民中。

采用这些系统的动机包括减少能源费用、采取切实的应对气候变化行动，以及获得能源独立性。虽然节省的成本有限（对于530美元的系统，每年约为100美元），但用户欣赏与可再生能源的直接连接以及由此带来的对能源消耗的意识。

尽管存在炒作，但对德国整体能源需求的影响仍然很小，估计不到1%。仍然存在挑战，包括来自房东的抵制，以及因位置和阳光而异的系统性能。德国对阳台太阳能的热情是独一无二的，因为这项技术在美国等其他国家由于法规和电气标准而面临障碍。

---

## 42. 创建动机证明数据库

**原文标题**: Creating a database of motivated proofs

**原文链接**: [https://gowers.wordpress.com/2025/09/22/creating-a-database-of-motivated-proofs/](https://gowers.wordpress.com/2025/09/22/creating-a-database-of-motivated-proofs/)

该文章宣布一项新项目，旨在创建一个“结构化动机证明”数据库，以提高人工智能的数学能力。该项目由文艺复兴慈善基金会资助，旨在解决目前人工智能在数学方面的局限性，特别是大型语言模型（LLMs），由于数学证明的传统呈现方式，它们通常依赖于“猜测和检验”的方法。

作者认为，标准的数学写作通常隐藏了证明背后的思考过程，导致LLMs模仿这种风格，并产生不正确的论证，而这些论证很难用统计方法与正确的论证区分开来。目前，人工智能擅长证明的常规部分以及可以通过基于先前见过的模式进行“智能猜测和检验”来解决的问题，但在需要更深层次推理的研究级问题上却表现不佳。

提议的解决方案是一个证明数据库，该数据库明确揭示了每一步骤背后的基本思考过程和动机。这种“结构化动机证明”将使用从一个“证明发现状态”到另一个状态的“标准动作”生成。此类动作的示例包括“库提取”，其中将相关定理添加到可用假设中，以及量词的“显式实例化”。关键是避免“帽子里变出兔子”——缺乏明确动机的令人惊讶的步骤。该项目计划创建一个平台，以促进这些结构化证明的输入，通过游戏化这个过程，并激励用户做出贡献。作者计划在未来的帖子中详细介绍“标准动作”的概念，并鼓励合作以填充数据库。

---

## 43. 基于规则的专家系统：Mycin 实验 (1984)

**原文标题**: Rule-Based Expert Systems: The Mycin Experiments (1984)

**原文链接**: [https://www.shortliffe.net/Buchanan-Shortliffe-1984/MYCIN%20Book.htm](https://www.shortliffe.net/Buchanan-Shortliffe-1984/MYCIN%20Book.htm)

基于规则的专家系统：MYCIN实验 是一部对MYCIN项目进行全面回顾性分析的著作。MYCIN项目是人工智能领域的一项开创性工作，旨在开发一种用于诊断细菌感染并推荐治疗方案的专家系统。本书由Buchanan和Shortliffe编辑，详细介绍了长达十年的研发过程，重点介绍了成功和失败之处。

本书共分为十二个部分，涵盖了各个方面，包括MYCIN基于规则系统的演变、知识工程技术、使用确定性因子和其他模型进行不确定性推理，以及将MYCIN原理推广到用于构建其他专家系统的EMYCIN工具。本书深入探讨了如何解释MYCIN的推理，探索规则之外的替代知识表示（如框架），以及如何利用MYCIN的知识进行辅导。

很大一部分内容侧重于用元级别知识来扩充规则库，并评估MYCIN的性能，包括对其建议的实际评估。本书还探讨了人机交互的关键方面，研究如何设计医疗专家系统以获得最佳的可用性和医生的接受度。最后，本书总结了从MYCIN实验中获得的主要教训，为人工智能领域提供了宝贵的见解。本书作为一项批判性分析，旨在帮助为人工智能领域奠定科学基础。

---

## 44. 在框架笔记本和磁盘上使用S3自托管10TB数据

**原文标题**: Self hosting 10TB in S3 on a framework laptop and disks

**原文链接**: [https://jamesoclaire.com/2025/10/05/self-hosting-10tb-in-s3-on-a-framework-laptop-disks/](https://jamesoclaire.com/2025/10/05/self-hosting-10tb-in-s3-on-a-framework-laptop-disks/)

作者成功使用一台二手 Framework 笔记本电脑和一个通过 USB 连接的 JBOD (磁盘簇) 自建了 10TB 的 S3 存储方案。 动机源于需要廉价存储用于应用追踪数据。

该设置包括在 Framework 笔记本电脑上运行 ZFS 和 Garage S3。 最初由于 ZFS 对 JBOD 进行大量读写操作，导致 SQLite 元数据存储在其中，出现了一个小问题，但作者通过将元数据移动到笔记本电脑的内部存储解决了这个问题。

经过四个月的大部分时间无人值守运行后，发现该系统正在使用 10TB 的空间，并耐心等待重启进行升级。 作者紧张地重启了系统，欣慰地看到它正常启动。 他们还成功地将 Garage S3 从 v1 更新到 v2。

作者承认使用 USB 连接进行 ZFS 操作并不标准，并且最初导致了一些问题，但强调了在移动元数据后，整个设置的成功和稳定性。 结论是：一个廉价的、自建的 S3 解决方案，只需要极少的维护。

---

## 45. 虎鲸给人类送礼物

**原文标题**: Orcas are bringing humans gifts

**原文链接**: [https://www.newscientist.com/article/2486216-orcas-are-bringing-humans-gifts-what-does-it-mean/](https://www.newscientist.com/article/2486216-orcas-are-bringing-humans-gifts-what-does-it-mean/)

观察到虎鲸试图将死亡猎物“赠送”给人类，这表明它们具有利他行为，并且能够识别其他物种的感知能力。研究员贾里德·托尔斯记录了多个虎鲸（包括阿克拉和箭袋）向人类提供死亡鸟类和海豹幼崽的案例。他汇总了2004年至2024年间的32起类似案例，涉及不同的虎鲸和各种猎物，如黄貂鱼、水母，甚至鲸脂。

这种行为类似于虎鲸群内部的猎物分享，但将利他主义扩展到了其他物种。洛里·马里诺等专家认为，这表明虎鲸具有普遍的利他主义和跨物种实验的能力。托尔斯认为，这表明虎鲸具有心理理论，能够理解其他人拥有不同的心理状态。

这种行为可能受到好奇心和探索周围环境关系驱动。虎鲸受益于合作，并且有时有多余的猎物可以分享，这使得它们能够探索周围环境。这种行为通过减少不确定性，对杂食性捕食者有利，并且通过测试边界来主动了解人类。

---

## 46. BirdNET-Pi 简介：偷听我的羽毛朋友们

**原文标题**: Intro to BirdNET-Pi: Eavesdropping on my feathered friends

**原文链接**: [https://hannahilea.com/blog/birdnet-intro/](https://hannahilea.com/blog/birdnet-intro/)

本文介绍了 BirdNET-Pi，一个允许用户使用树莓派被动监测和识别鸟鸣声的应用。BirdNET-Pi 基于康奈尔鸟类学实验室开发的 BirdNET 模型，使用户能够创建自己的鸟类“监听站”来追踪当地环境中的鸟类活动。

作者详细描述了自己和家人设置多个 BirdNET-Pi 系统的体验，强调了它带来的乐趣和联系。文章包含了随时间检测到的鸟类活动示例，展示了该应用识别不同物种及其活动模式的能力。

作者阐明了术语：BirdNET 是康奈尔实验室的模型，而 BirdNET-Pi 是在树莓派上使用它的应用程序。他们强调了项目需求：经济实惠、保护隐私，并且易于赠送和远程调试。文章解释了 BirdNET-Pi 应用的工作原理：连续音频录制、频谱图转换、BirdNET 模型分析和数据存储。包含人声的音频片段会被丢弃以保护隐私。一个网页界面会显示检测结果、录音和汇总图表。

作者解决了隐私问题，强调了告知家庭成员和访客关于持续开启麦克风的重要性。他们还指出，除非用户专门启用外部发布，否则只有拥有 Wi-Fi 和树莓派密码的人才能访问数据。作者分享了其他好处，例如分享鸟类分析和接收关于新检测的通知。文章最后呼吁读者建立自己的 BirdNET-Pi 系统并分享他们的发现。

---

## 47. OpenAI与Jony Ive在新AI设备的技术细节上遇到困难

**原文标题**: OpenAI, Jony Ive struggle with technical details on secretive new AI gadget

**原文链接**: [https://arstechnica.com/ai/2025/10/openai-jony-ive-struggle-with-technical-details-on-secretive-new-ai-gadget/](https://arstechnica.com/ai/2025/10/openai-jony-ive-struggle-with-technical-details-on-secretive-new-ai-gadget/)

OpenAI与Jony Ive在开发秘密AI设备上遭遇技术挑战，该设备旨在成为一款无屏幕、掌上大小的设备，通过音频和视觉提示进行响应。 尽管以65亿美元收购了Ive的设计公司io，但他们在软件、基础设施和AI助手的“个性”方面遇到了困难。 主要问题包括隐私、计算能力需求，以及防止该设备过于侵入或过于健谈，这是当前AI助手普遍存在的问题。

该设备被设想为一个“永远在线”的伴侣，使用摄像头、麦克风和扬声器来收集数据并构建虚拟助手的“记忆”。 OpenAI试图改进现有智能音箱，如亚马逊的Echo。 然而，文章强调了平衡AI个性（既要提供帮助又不能惹人厌）的难度，并将其与Siri和备受批评的AI伴侣“Friend”以及被废弃的Humane AI Pin等警示故事进行比较。

尽管存在这些障碍，OpenAI仍在硬件方面进行大量投资，从苹果和Meta公司获取人才，并与立讯精密等中国制造商合作。 文章强调了OpenAI（目前估值5000亿美元）的巨大风险，因为它旨在通过成功进军硬件领域来证明其估值的合理性。

---

## 48. 解释器：inode和inode编号

**原文标题**: Explainer: Inodes and Inode Numbers

**原文链接**: [https://eclecticlight.co/2025/10/04/explainer-inodes-and-inode-numbers/](https://eclecticlight.co/2025/10/04/explainer-inodes-and-inode-numbers/)

本文解释了inode和inode编号，文件系统用于识别文件和目录的基本数据结构。inodes，即索引节点的缩写，是带编号的数据结构，其唯一的编号（inode编号）用于标识文件系统中的对象。

本文详细介绍了不同的文件系统如何处理这些标识符。HFS+，Mac较旧的文件系统，由于Unix API的要求，不使用真正的inode，而是使用目录节点ID（CNID）作为inode编号。APFS，Apple的现代文件系统，直接使用64位无符号整数实现inode。它还阐述了APFS如何在软链接的系统和数据卷的卷组中处理inode编号，以确保唯一性。

除了简单的识别，inode还包含关键的文件元数据，包括时间戳、权限和指向实际数据的扩展记录。文件还可以具有与inode一起存储的扩展属性。

本文进一步解释了inode编号在链接文件中的作用。复制会创建一个新的文件，并具有一个新的inode，而克隆会创建一个具有不同inode的克隆文件，但共享数据。符号链接不涉及inode，而硬链接会创建多个指向同一inode的对象，并记录这些链接的数量，从而可以在不影响数据或任何其他硬链接的情况下删除一个对象。最后，本文指出可以通过`ls -i`等命令行工具轻松访问inode编号。

---

## 49. 使用ARM SIMD的86 GB/s位打包（单线程）

**原文标题**: 86 GB/s bitpacking with ARM SIMD (single thread)

**原文链接**: [https://github.com/ashtonsix/perf-portfolio/tree/main/bytepack](https://github.com/ashtonsix/perf-portfolio/tree/main/bytepack)

ashtonsix在名为"perf-portfolio"的公开GitHub仓库中提供了一个项目，标题为"86 GB/s 基于ARM SIMD的位打包 (单线程)"。

其重点在于使用ARM单指令多数据流(SIMD)指令，在单线程中实现高达86 GB/s的高吞吐量位打包性能。 这表明为了利用ARM处理器并行处理能力，针对使用位打包技术进行高效数据压缩或编码进行了优化。

该项目是开源且公开的，欢迎贡献和进一步开发。 数据显示了一定程度的受欢迎程度：2个fork和51个star表明该项目已引起开发人员社区的兴趣。 项目标题表明这是一个专注于测量和优化ARM架构到位打包速度的性能基准测试。

---

## 50. LLM最能理解哪种表格格式？

**原文标题**: Which table format do LLMs understand best?

**原文链接**: [https://www.improvingagents.com/blog/best-input-data-format-for-llms](https://www.improvingagents.com/blog/best-input-data-format-for-llms)

本文探讨了不同数据格式对大型语言模型处理表格数据的准确性和成本的影响。作者使用GPT-4.1-nano模型，1000条合成员工记录和1000个随机问题进行了一项实验，测试了11种不同的数据格式。

关键发现是**数据格式显著影响大型语言模型的准确性。** Markdown-KV（一种自定义的“键: 值”格式）实现了最高的准确率（60.7%），而CSV和JSONL表现不佳。这表明选择正确的格式可以快速提高准确性。然而，存在一个权衡：**更高的准确性通常意味着更高的token成本。** Markdown-KV使用的token数量是CSV的2.7倍。

本文建议在对准确性要求极高时，将Markdown-KV作为良好的默认选择，并将Markdown表格作为可读性和成本之间的平衡。建议在使用CSV或JSONL时要谨慎。作者承认局限性，包括仅测试了一个模型和数据模式。未来的研究应探索不同的模型、数据结构（嵌套数据）、带有标题重复的表格大小以及问题类型。

主要结论是，简单的数据转换可以显著提高基于大型语言模型的系统的准确性，并且值得测试不同的格式，以找到适用于特定应用程序的最佳格式。

---

## 51. 联合书评：保罗·福塞尔著《阶级》

**原文标题**: Joint Book Review: Class, by Paul Fussell

**原文链接**: [https://www.thepsmiths.com/p/joint-review-class-by-paul-fussell](https://www.thepsmiths.com/p/joint-review-class-by-paul-fussell)

这是简·史密斯和约翰·史密斯合写的保罗·福塞尔的《格调：美国等级制度指南》的书评。书评探讨了福塞尔对美国阶级制度及其微妙、通常不为人知的标志的分析。

简认为，虽然美国人可能不会明确讨论阶级，但它深刻地影响着他们的行为、价值观和在线互动。她强调了福塞尔的观点，即对阶级的看法会随着一个人在等级制度中所处的位置而改变，而“位于顶端”的人决定了归属的标准。然后，她总结了福塞尔的九个阶级：顶层隐形阶级、上层阶级、中上层阶级、中产阶级、三个层次的无产阶级、赤贫阶级和底层隐形阶级。她区分了上层阶级的财富、怪癖和反智主义；中上层阶级的教育和成熟度；中产阶级对体面的渴望和委婉语的使用；以及无产阶级对手工劳动和品牌展示的自豪感。简认为，阶级的标志包括自然、劳动密集型、年代感和低调。

约翰表达了对这本书可能剥夺令人安慰的幻想，并使人们以更批判、可能更愤世嫉俗的方式看待社会的担忧。他将它比作学习云彩或历史，以一种永久改变一个人视角的方式。他认为这本书具有潜在的危险性，应该谨慎对待。

---

## 52. Show HN: ASCII绘图板

**原文标题**: Show HN: ASCII Drawing Board

**原文链接**: [https://www.delopsu.com/draw.html](https://www.delopsu.com/draw.html)

"Show HN" 介绍 ASCII 绘图板：一款使用 ASCII 字符创作的 Web 应用。该绘图板提供以下功能：

*   **画笔工具：** 允许用户使用自定义 ASCII 字符进行绘制。帖子明确提到可以使用 Unicode 字符，但存在字体限制。
*   **画笔大小：** 可调节画笔大小（列出了 1x1、2x2、3x3 选项）。
*   **橡皮擦工具：** 用于修正错误。
*   **全部擦除：** 清空整个绘图。
*   **调整大小：** 更改绘图区域的尺寸（列数和行数）的选项。
*   **复制功能：** 能够复制 ASCII 艺术作品。
*   **导出为 TXT：** 允许将创作保存为文本文件。
*   **尺寸：** 绘图板的默认尺寸为 90 列 x 40 行。

作者 delopsu（提到 2025 年）正在征求反馈意见，并提供联系地址 (@delopsu_com)。该帖子强调了使用 Unicode 字符作为画笔来源。

---

## 53. Claude开发者平台上的上下文管理

**原文标题**: Managing context on the Claude Developer Platform

**原文链接**: [https://www.anthropic.com/news/context-management](https://www.anthropic.com/news/context-management)

本文宣布 Claude 开发者平台新增上下文管理功能：上下文编辑和记忆工具。这些功能由 Claude Sonnet 4.5 提供支持，旨在帮助开发者构建能够更有效地处理长时间运行任务的 AI 代理，而不会达到上下文限制或丢失重要信息。

上下文编辑会自动从上下文窗口中删除过时的工具调用和结果，无需手动干预即可延长代理的运行寿命，并通过专注于相关信息来提高性能。记忆工具使 Claude 能够通过基于文件的系统在上下文窗口之外存储和检索信息，从而允许代理构建知识库、维护项目状态以及跨会话引用过去的学习内容。开发者可以通过客户端工具调用系统完全控制数据存储。

这些工具的集成显著提高了代理性能。内部评估表明，将记忆工具与上下文编辑相结合比基线性能提高了 39%，而仅使用上下文编辑就提高了 29%。在一个 100 轮的 Web 搜索评估中，上下文编辑使代理能够完成以前因上下文耗尽而无法完成的工作流程，同时减少了 84% 的 token 消耗。

这些功能现已在 Claude 开发者平台、Amazon Bedrock 和 Google Cloud 的 Vertex AI 上以公开测试版提供，为编码、研究和数据处理等领域的长时间运行代理解锁了新的可能性。

---

## 54. 比较具有相似硬件结构的 RISC 和 CISC (1991)

**原文标题**: Comparing a RISC and a CISC with similar hardware organization (1991)

**原文链接**: [https://dl.acm.org/doi/pdf/10.1145/106972.107003](https://dl.acm.org/doi/pdf/10.1145/106972.107003)

无法访问文章链接。

---

## 55. 比亚迪造最快汽车

**原文标题**: BYD builds fastest car

**原文链接**: [https://www.autotrader.co.uk/content/news/byd-builds-world-s-fastest-car](https://www.autotrader.co.uk/content/news/byd-builds-world-s-fastest-car)

“比亚迪打造最快汽车”概要（基于文章可能内容，因无法访问链接）：

文章可能讨论比亚迪最近制造的一款电动汽车(EV)，该车具有卓越的速度和性能，可能声称在特定类别中获得“世界最快汽车”的称号（例如，电动汽车的加速、最高速度）。

主要内容可能包括：

*   **车辆：** 车型名称和类型的详细信息，可能是一款高性能轿车或跑车。文章将描述其设计，突出其有助于提高速度的特性，例如空气动力学和轻量化结构。
*   **性能参数：** 加速（0-60 英里/小时或 0-100 公里/小时）、最高速度以及可能的四分之一英里时间的具体数据。这些数字将与其他高性能电动汽车进行比较，以支持“最快”的说法。
*   **技术：** 关于车辆电力总成的信息，包括电池容量、电机输出（马力和扭矩），以及用于提高性能的任何先进技术，例如先进的牵引力控制系统或扭矩矢量分配。
*   **价格和上市：** 说明车辆的预计价格范围以及何时可以购买，如果已发布，将提供有关在哪里可以试驾或购买的信息。
*   **比亚迪的战略：** 讨论这款高性能电动汽车如何融入比亚迪开发电动汽车和在全球汽车市场竞争的更广泛战略。它可能强调比亚迪对创新的关注及其成为电动汽车技术领导者的雄心。

文章最终将比亚迪的新车视为电动汽车行业的一项重大成就，展示了该公司的能力，并可能挑战高性能电动汽车领域的现有企业。

---

## 56. 展示 HN: Meihus – 房贷计算器，每月显示提前还款的影响

**原文标题**: Show HN: Meihus – Mortgage calculator that shows early payment impact monthly

**原文链接**: [https://meihus.com](https://meihus.com)

Meihus是一款抵押贷款计算器，旨在按月展示提前还款的影响。用户可以选择计算新的抵押贷款或对现有贷款进行再融资。计算器包含房产价值、首付、抵押贷款价值、贷款期限（年）和利率类型（固定、浮动或混合）等字段。

用户输入参数后，计算器会生成抵押贷款摘要，包括借款金额、期限、还款总额和每月还款额。此外还提供详细的还款计划表，显示每次还款前后的欠款金额，以及本金、利息、提前还款金额（如有）和每月总额。

其主要特点是能够添加一次性或定期提前还款，并据此重新计算每月还款额。用户可以指定一次性还款的月份和金额，或者指定定期还款的起始/结束月份和每月金额。专门的章节会详细展示这些提前还款如何影响每月还款额。

---

## 57. 基于 Linux 的 CHERI

**原文标题**: CHERI with a Linux on Top

**原文链接**: [https://lwn.net/Articles/1037974/](https://lwn.net/Articles/1037974/)

这篇 LWN.net 文章探讨了 CHERI (Capability Hardware Enhanced RISC Instructions) 项目，该项目旨在通过重新思考计算机体系结构来提高计算机安全性，具体来说是通过扩展指令集架构 (ISA) 以支持能力。能力是不可伪造的令牌，它结合了对对象（如内存）的引用和访问权限，从而提供细粒度的访问控制。

Carl Shaw 在欧洲 Linux 安全峰会 (LSS EU) 上介绍了在 CHERI 上运行 Linux 的工作，强调了能力的历史及其增强操作系统安全性的潜力。虽然早期的实现由于间接性而受到性能问题的影响，但像 CHERI 这样的现代方法避免了这一点。

CHERI 已在 MIPS、Arm (Morello) 和 RISC-V 上实现。它采用混合方法，允许它与使用整数指针的现有系统一起工作，同时利用能力来实现内存安全和分区。CHERI 的关键特性包括确定性操作、硬件/软件协同设计以及防止 C 和 C++ 代码中常见的内存安全漏洞的能力。

文章指出，纯能力版本的 Linux 内核 (6.16) 已经成功运行，内核中的每个指针现在都是一个能力。Codasip 正在积极开发用于 RISC-V 的这个 purecap 版本。虽然 FreeBSD 已经通过 CheriBSD 拥有了先进的安全功能，但 Linux 移植首先关注的是功能。文章还提到了使 Linux 内核适应 CHERI 的挑战，例如指针类型不匹配和结构对齐问题。最终目标是将兼容的更改上游到 Linux 内核。

---

## 58. 我应该选择Ada、SPARK或Rust而不是C/C++吗？(2024)

**原文标题**: Should I choose Ada, SPARK, or Rust over C/C++? (2024)

**原文链接**: [https://blog.adacore.com/should-i-choose-ada-spark-or-rust-over-c-c](https://blog.adacore.com/should-i-choose-ada-spark-or-rust-over-c-c)

AdaCore的这篇文章比较了C/C++与Ada/SPARK和Rust在开发高可靠性嵌入式系统中的应用。虽然C/C++是常见的默认选择，但文章认为它在安全性和安全性方面风险更高。Ada和Rust提供了更安全的替代方案。

Rust拥有庞大而活跃的社区和灵活的内存模型，而Ada拥有规模较小但成熟的生态系统，具备完整的工具链和认证文档。Ada还提供了一种强大的规范语言，用于表达和检查软硬件约束。

基于Ada的SPARK提供了工业级的形式化方法，可以通过数学方式证明软件的安全性和安全性，从而在编译时静态地消除潜在的漏洞。这可以通过减少对广泛测试的需求来节省成本。

文章重点介绍了这三种语言在社区规模、工具链成熟度、认证可用性和可用库方面的差异。Ada/SPARK拥有成熟的嵌入式工具链和认证证据，而Rust在这方面发展迅速。Rust拥有更大的库生态系统，但许多库是由业余爱好者开发的，缺乏安全关键应用所需的严谨性。

这三种语言都提供了减轻编程错误的方法，其中Ada/SPARK提供了强类型。最终，最佳选择取决于项目的具体需求、团队采用新技术的意愿以及对形式化验证和长期支持等因素的重视程度。

---

## 59. Retrocide Mono – 没有降部的等宽字体

**原文标题**: Retrocide Mono – A monospaced font with no decenders

**原文链接**: [https://geonot.github.io/retrocide-mono/](https://geonot.github.io/retrocide-mono/)

Retrocide Mono是由orbit system.log设计的等宽字体，其特点是没有降部，确保所有字符的基线一致。此特性使其特别适用于对齐至关重要的应用场景。

主要特性包括其等宽设计、零降部、针对代码和终端使用的优化、复古美学与现代清晰度的结合，以及TTF、OTF和WOFF2格式的可用性。

字体展示包括大写和小写字母、数字和符号，以及使用JavaScript和复古主题颜色的代码示例，以及用于安装和配置的终端命令。

Retrocide Mono被认为是代码编辑器、终端、UI设计和ASCII艺术的理想选择。“无降部特性”突出了字母'g'、'j'、'p'、'q'和'y'如何在不向下延伸的情况下位于基线上。

该文档还通过基于复古计算机美学的图形设计，从视觉上强调了字体的对齐能力。这加强了字体独特的审美和对复古风格项目的适用性。

---

## 60. 估算人工智能的能源消耗

**原文标题**: Estimating AI energy use

**原文链接**: [https://spectrum.ieee.org/ai-energy-use](https://spectrum.ieee.org/ai-energy-use)

每条AI答案背后的隐形巨兽
这篇文章“每条AI答案背后的隐形巨兽”探讨了生成式AI日益增长的能源需求，并以ChatGPT为例重点说明。作者Matthew S. Smith强调，看似简单的查询需要大量的计算资源，从而导致巨大的能源消耗。

文章根据OpenAI报告的ChatGPT每日25亿次查询，结合Sam Altman引用的每次查询约0.34瓦时的估算值，计算得出每日能源消耗为850兆瓦时。按年计算，这相当于大约29,000户美国家庭的用电量。

然而，ChatGPT只是冰山一角。文章引用了施耐德电气可持续发展研究所的报告，估计2025年生成式AI的总功耗为15太瓦时，并预测到2030年将大幅增加到347太瓦时。这种增长意味着需要大量的基础设施建设，可能需要几十个“星际之门级”数据中心，每个数据中心每年消耗8.76太瓦时。

文章强调，AI推理（与AI模型交互时使用的电量）将是这种能源消耗增长的主要驱动力。独立工作的AI代理的兴起可能会进一步加剧能源消耗。尽管估算各不相同，但普遍认为，由于生成式AI的普及，能源消耗将急剧增加。

---

## 61. Show HN: ut – 基于 Rust 的面向开发者和 IT 人员的 CLI 工具集

**原文标题**: Show HN: ut – Rust based CLI utilities for devs and IT

**原文链接**: [https://github.com/ksdme/ut](https://github.com/ksdme/ut)

`ut` 是一个基于 Rust 的 CLI 实用工具包，专为开发者和 IT 专业人士设计，旨在将常用工具整合到一个轻量级的二进制文件中。这消除了多次安装的需要，并减轻了记住各个命令的认知负担。

该工具包通过 `cargo install` 安装，并使用 `ut <工具> [选项]` 调用。它拥有广泛的工具集，组织成以下类别：

*   **编码:** base64 和 URL 编码/解码。
*   **哈希:** 密码学哈希摘要 (MD5, SHA-1, SHA-256, 等)。
*   **数据生成:** UUID 生成 (v1, v3, v4, v5, v7), 安全令牌, lorem ipsum, 和随机数。
*   **文本处理:** 大小写转换, 美化打印转义字符, 和文本差异比较。
*   **开发工具:** 表达式计算器, JSON 构建器, 交互式正则表达式测试器, 和日期时间解析/转换。
*   **Web & 网络:** HTTP 实用工具 (状态码查找, 本地文件服务器) 和二维码生成。
*   **颜色 & 设计:** 颜色格式转换。
*   **参考:** Unicode 符号参考。

`ut` 强调速度、独立运行 (无依赖)、通过 stdin/stdout 实现可组合性、使用密码学安全随机数生成器的安全性，以及跨平台兼容性。该项目欢迎贡献，并承认在开发过程中使用了 AI 辅助编码 (Claude Code)。

---

## 62. 工业设计的消亡与乏味电子产品的时代

**原文标题**: The death of industrial design and the era of dull electronics

**原文链接**: [https://hackaday.com/2025/07/23/the-death-of-industrial-design-and-the-era-of-dull-electronics/](https://hackaday.com/2025/07/23/the-death-of-industrial-design-and-the-era-of-dull-electronics/)

本文认为消费电子产品中的工业设计正在走向消亡，导致一个充斥着乏味、难以区分的设备的时代。它将过去大胆而多彩的设计，特别是90年代末和2000年代初的“Y2K美学”和“未来主义航空”时代，与当前缺乏独特特征的扁平、几何“平板”趋势形成对比。

作者以手机和电视为例，指出它们是如何演变成以屏幕为主的、没有特点的矩形，缺乏物理按钮、触觉控制和独特的造型。这种“进化”延伸到电脑甚至汽车内饰，触摸屏取代了物理控制。

文章将这种衰落归因于对极简主义设计的关注以及对通过智能手机应用程序实现的基于软件界面的依赖。这种将用户界面外包给应用程序的做法导致了令人沮丧的体验，甚至使设备无法使用，Sonos应用程序的惨败就是一个例证。

作者认为“实体媒体的复兴”和“复古计算”源于对更具吸引力和刺激性的体验的渴望，触觉互动和视觉上令人愉悦的设计为现代电子产品的死板平板提供了令人欣慰的对比。现代电子产品缺乏这种互动会导致无聊和对丰富活动的需要，这可能证明了回归更古老、更具表现力的设计原则是合理的。

---

## 63. 救了我们一命的烂招/最烂但救命的奇招

**原文标题**: The best worst hack that saved our bacon

**原文链接**: [https://jeffersonheard.ghost.io/the-best-worst-hack-that-saved-our-bacon/](https://jeffersonheard.ghost.io/the-best-worst-hack-that-saved-our-bacon/)

本文讲述了一次巧妙但非常规的变通方案如何避免了一场近乎灾难的事故。作者描述了他们的日历平台正迅速逼近其事件发生的 32 位整数主键的上限，威胁着整个系统的崩溃。迁移到大整数的长期解决方案已经在进行中，但最后一刻意识到整数键通过公共 API 公开造成了一个重大问题。更改 API 可能会破坏现有的客户集成，其中许多集成由行动迟缓的大学 IT 部门管理。

面对这一困境，团队实施了一个“愚蠢的简单”的解决方案：将主键序列重置为 32 位整数范围的负数侧，从而有效地将其可用键空间增加了一倍。这为他们争取了长达三年的时间来正确迁移，同时确保 API 集成不会中断。

作者强调这是一个经过深思熟虑且充分理解的技术债务。他们立即为 BigInt 迁移设定了一个严格的截止日期，并彻底调查了 API 依赖关系，与客户成功团队合作，主动通知并帮助受影响的客户。长期的解决方案不仅仅是迁移，还要用不透明的句柄抽象内部 ID，并确保用户将来不会依赖这些 ID 的类型。

虽然承认这种变通方案的荒谬性，但作者认为在当时的情况下这是正确的决定，为他们赢得了关键的时间，并允许平稳过渡到更强大和面向未来的系统。关键不在于使用负数主键，而是强调在面临危急情况时负责任地应用技术债务，并制定明确的及时解决计划。

---

## 64. 自由软件基金会四十周年，推出突破性新项目并迎来新主席

**原文标题**: FSF turns forty with a groundbreaking new project and a new president

**原文链接**: [https://www.fsf.org/news/fsf-turns-forty-with-a-new-president-and-a-new-campaign](https://www.fsf.org/news/fsf-turns-forty-with-a-new-president-and-a-new-campaign)

自由软件基金会(FSF)举办FSF40活动庆祝其四十周年，该活动内容丰富，包括讨论、公告和社区互动。 其中一个亮点是伊恩·凯林就任新的FSF主席，他承诺加强FSF捍卫用户自由和扩大自由软件社区的能力。

活动邀请了杰出的自由软件活动家分享他们的经验，志愿者们讨论了他们在GNU、EmacsConf、Debian和Trisquel等项目上的工作。 执行董事佐伊·库伊曼发布了LibrePhone，这是一项新的FSF倡议，旨在与开发者罗伯·萨沃耶合作，将软件自由带入移动计算领域。

FSF还重申了其对本地活动的支持，并向与会者介绍了其在制定自由机器学习标准方面的进展。 LibreLocal小组负责人分享了他们对各自区域社区的见解，涵盖了他们的活动、成功和挑战。

电子前沿基金会(EFF)、F-Droid、FSF和Sugar Labs的代表参加了一个小组讨论，讨论了软件自由、隐私、移动自由以及自由软件在教育中的重要性。 活动最后对过去四十年来支持自由软件运动的无数贡献者表示感谢。

---

## 65. Social Cooling (2017)

**原文标题**: Social Cooling (2017)

**原文链接**: [https://www.socialcooling.com/](https://www.socialcooling.com/)

"Social Cooling" argues that the increasing collection and analysis of personal data are leading to a society characterized by self-censorship, risk aversion, and decreased social evolution. Similar to how oil leads to global warming, the article contends that data leads to "social cooling."

Data brokers compile vast amounts of information to predict personal attributes like religion, political views, and even "gullibility," creating detailed "digital reputations." These reputations can negatively impact opportunities, leading to discrimination in employment, loan applications, and even dating.

The article posits that this constant surveillance and potential for judgment causes individuals to modify their behavior to achieve better "scores," leading to conformity and risk aversion. Examples include hesitating to click certain links, doctors avoiding treating high-risk patients, and China's social credit system, which restricts opportunities for those deemed "badly behaved."

The author argues this shift threatens free speech, creativity, and societal progress. They advocate for increased awareness and a more nuanced understanding of data and privacy, drawing a parallel to the fight against global warming. The solution lies in protecting the right to make mistakes and ensuring individuals have the right to be forgotten in the data-driven world. The author, Tijmen Schep, encourages sharing this information to promote a more privacy-conscious society.


---

## 66. Find Nearby Automated License Plate Readers (ALPR)

**原文标题**: Find Nearby Automated License Plate Readers (ALPR)

**原文链接**: [https://deflock.me/](https://deflock.me/)

生成摘要时出错

---

## 67. Show HN: Re-Implementing the macOS Spatial Finder

**原文标题**: Show HN: Re-Implementing the macOS Spatial Finder

**原文链接**: [https://github.com/everydayanchovies/SpatialFinder](https://github.com/everydayanchovies/SpatialFinder)

生成摘要时出错

---

## 68. Americans increasingly see legal sports betting as a bad thing for society

**原文标题**: Americans increasingly see legal sports betting as a bad thing for society

**原文链接**: [https://www.pewresearch.org/short-reads/2025/10/02/americans-increasingly-see-legal-sports-betting-as-a-bad-thing-for-society-and-sports/](https://www.pewresearch.org/short-reads/2025/10/02/americans-increasingly-see-legal-sports-betting-as-a-bad-thing-for-society-and-sports/)

生成摘要时出错

---

## 69. Building Effective Text-to-3D AI Agents: A Hybrid Architecture Approach

**原文标题**: Building Effective Text-to-3D AI Agents: A Hybrid Architecture Approach

**原文链接**: [https://www.addy.rocks/blog/text-to-3d-agent-hybrid-architecture](https://www.addy.rocks/blog/text-to-3d-agent-hybrid-architecture)

生成摘要时出错

---

## 70. What Julia has that Rust desperately needs

**原文标题**: What Julia has that Rust desperately needs

**原文链接**: [https://jdiaz97.github.io/blog/what-julia-has-that-rust-needs/](https://jdiaz97.github.io/blog/what-julia-has-that-rust-needs/)

生成摘要时出错

---

## 71. Implicit Actor Critic Coupling via a Supervised Learning Framework for RLVR

**原文标题**: Implicit Actor Critic Coupling via a Supervised Learning Framework for RLVR

**原文链接**: [https://arxiv.org/abs/2509.02522](https://arxiv.org/abs/2509.02522)

生成摘要时出错

---

## 72. OpenAI's hunger for computing power

**原文标题**: OpenAI's hunger for computing power

**原文链接**: [https://www.wsj.com/tech/ai/openai-sam-altman-asia-middle-east-7b660809](https://www.wsj.com/tech/ai/openai-sam-altman-asia-middle-east-7b660809)

生成摘要时出错

---

## 73. Beginner Guide to VPS Hetzner and Coolify

**原文标题**: Beginner Guide to VPS Hetzner and Coolify

**原文链接**: [https://bhargav.dev/blog/VPS_Setup_and_Security_Checklist_A_Complete_Self_Hosting_Guide](https://bhargav.dev/blog/VPS_Setup_and_Security_Checklist_A_Complete_Self_Hosting_Guide)

生成摘要时出错

---

## 74. AI-powered open-source code laundering

**原文标题**: AI-powered open-source code laundering

**原文链接**: [https://github.com/SudoMaker/rEFui/blob/main/HALL_OF_SHAME.md](https://github.com/SudoMaker/rEFui/blob/main/HALL_OF_SHAME.md)

生成摘要时出错

---

## 75. 歧义图

**原文标题**: Ambigr.am

**原文链接**: [https://ambigr.am/hall-of-fame](https://ambigr.am/hall-of-fame)

The Ambigr.am website appears to be a web application that requires JavaScript to function. The only information available is the title, "Ambigr.am," and a message indicating that JavaScript needs to be enabled to run the application. Without JavaScript enabled or further content, it's impossible to determine the purpose, features, or functionality of the Ambigr.am application. It is therefore, impossible to provide a meaningful summary beyond this basic observation.


---

## 76. PC 模拟器中的复古画面：第一部分 - Amiga

**原文标题**: Period-Correct Graphics in PC Emulators: Part 1 – The Amiga

**原文链接**: [https://blog.johnnovak.net/2022/04/15/achieving-period-correct-graphics-in-personal-computer-emulators-part-1-the-amiga/](https://blog.johnnovak.net/2022/04/15/achieving-period-correct-graphics-in-personal-computer-emulators-part-1-the-amiga/)

This article, the first in a series, focuses on achieving period-correct graphics when emulating classic computers, specifically the Commodore Amiga. The author argues that emulated graphics should closely resemble the output of CRT displays used with these computers in the 80s and 90s, emphasizing the differences between CRT technology used per platform.

The article primarily focuses on emulating the Commodore 1084S monitor, a common pairing with the Amiga, within the WinUAE emulator. It highlights the importance of analog RGB output over composite, and emphasizes that the only real difference between "PAL" and "NTSC" over RGB is the vertical refresh rate, more accurately termed RGB 50 and RGB 60.

A significant portion is dedicated to refuting the idea of sharp, rectangular pixels being the ideal for all emulated systems. The author contrasts the VGA PC experience with the Amiga, explaining that Amiga monitors, being essentially small TVs, used single-scanning techniques with lower vertical resolution, resulting in noticeable scanlines and a softer image. This contrasts sharply with the double-scanned, high-resolution output of VGA monitors.

The author contends that CRT shaders are crucial for authentically recreating the Amiga's visual output. They argue that "pixel art" on the Amiga was designed to be viewed on CRTs, where the electron beam blended and smoothed the image, creating a higher perceived resolution and minimizing jagged edges. The article positions the pixel grid as a control mechanism for the electron beam, rather than a direct representation of pixels on screen, concluding that authentic emulation of CRT effects enhances the viewing experience of Amiga games and graphics.


---

## 77. Mic-E-Mouse – Covert eavesdropping through computer mice

**原文标题**: Mic-E-Mouse – Covert eavesdropping through computer mice

**原文链接**: [https://sites.google.com/view/mic-e-mouse](https://sites.google.com/view/mic-e-mouse)

生成摘要时出错

---

## 78. Parrot – type-safe SQL in Gleam, supports SQlite, PostgreSQL and MySQL

**原文标题**: Parrot – type-safe SQL in Gleam, supports SQlite, PostgreSQL and MySQL

**原文链接**: [https://github.com/daniellionel01/parrot](https://github.com/daniellionel01/parrot)

生成摘要时出错

---

## 79. Why are hyperlinks blue? (2021)

**原文标题**: Why are hyperlinks blue? (2021)

**原文链接**: [https://blog.mozilla.org/en/internet-culture/deep-dives/why-are-hyperlinks-blue/](https://blog.mozilla.org/en/internet-culture/deep-dives/why-are-hyperlinks-blue/)

生成摘要时出错

---

## 80. Ada the CHERI Sweetheart: Memory Safe Software on Memory Safe Hardware [video]

**原文标题**: Ada the CHERI Sweetheart: Memory Safe Software on Memory Safe Hardware [video]

**原文链接**: [https://www.youtube.com/watch?v=zm1Y-I5Nn4s](https://www.youtube.com/watch?v=zm1Y-I5Nn4s)

生成摘要时出错

---

## 81. Personal data storage is an idea whose time has come

**原文标题**: Personal data storage is an idea whose time has come

**原文链接**: [https://blog.muni.town/personal-data-storage-idea/](https://blog.muni.town/personal-data-storage-idea/)

生成摘要时出错

---

## 82. Space Mission Options for Reconnaissance and Mitigation of Asteroid 2024 YR4

**原文标题**: Space Mission Options for Reconnaissance and Mitigation of Asteroid 2024 YR4

**原文链接**: [https://arxiv.org/abs/2509.12351](https://arxiv.org/abs/2509.12351)

生成摘要时出错

---

## 83. What .NET 10 GC changes mean for developers

**原文标题**: What .NET 10 GC changes mean for developers

**原文链接**: [https://roxeem.com/2025/09/30/what-net-10-gc-changes-mean-for-developers/](https://roxeem.com/2025/09/30/what-net-10-gc-changes-mean-for-developers/)

生成摘要时出错

---

## 84. Matrix Core Programming on AMD GPUs

**原文标题**: Matrix Core Programming on AMD GPUs

**原文链接**: [https://salykova.github.io/matrix-cores-cdna](https://salykova.github.io/matrix-cores-cdna)

生成摘要时出错

---

## 85. Catalyst evolution reveals the unsung heroes in industrial ammonia production

**原文标题**: Catalyst evolution reveals the unsung heroes in industrial ammonia production

**原文链接**: [https://phys.org/news/2025-09-catalyst-evolution-reveals-unsung-heroes.html](https://phys.org/news/2025-09-catalyst-evolution-reveals-unsung-heroes.html)

生成摘要时出错

---

## 86. Paged Out Issue #7 [pdf]

**原文标题**: Paged Out Issue #7 [pdf]

**原文链接**: [https://pagedout.institute/download/PagedOut_007.pdf](https://pagedout.institute/download/PagedOut_007.pdf)

生成摘要时出错

---

## 87. You can't parse XML with regex. Let's do it anyways

**原文标题**: You can't parse XML with regex. Let's do it anyways

**原文链接**: [https://sdomi.pl/weblog/26-nobody-here-is-free-of-sin/](https://sdomi.pl/weblog/26-nobody-here-is-free-of-sin/)

生成摘要时出错

---

## 88. Callbacks in C++ using template functors (1994)

**原文标题**: Callbacks in C++ using template functors (1994)

**原文链接**: [http://www.tutok.sk/fastgl/callback.html](http://www.tutok.sk/fastgl/callback.html)

生成摘要时出错

---

## 89. Gliding behind existing aircraft, Aerocart cargo gliders

**原文标题**: Gliding behind existing aircraft, Aerocart cargo gliders

**原文链接**: [https://www.aerolane.com/](https://www.aerolane.com/)

生成摘要时出错

---

## 90. How to inject knowledge efficiently? Knowledge infusion scaling law for LLMs

**原文标题**: How to inject knowledge efficiently? Knowledge infusion scaling law for LLMs

**原文链接**: [https://arxiv.org/abs/2509.19371](https://arxiv.org/abs/2509.19371)

生成摘要时出错

---

## 91. The collapse of the econ PhD job market

**原文标题**: The collapse of the econ PhD job market

**原文链接**: [https://www.chrisbrunet.com/p/the-collapse-of-the-econ-phd-job](https://www.chrisbrunet.com/p/the-collapse-of-the-econ-phd-job)

生成摘要时出错

---

## 92. Show HN: Pyscn – Python code quality analyzer for vibe coders

**原文标题**: Show HN: Pyscn – Python code quality analyzer for vibe coders

**原文链接**: [https://github.com/ludo-technologies/pyscn](https://github.com/ludo-technologies/pyscn)

生成摘要时出错

---

## 93. ProofOfThought: LLM-based reasoning using Z3 theorem proving

**原文标题**: ProofOfThought: LLM-based reasoning using Z3 theorem proving

**原文链接**: [https://github.com/DebarghaG/proofofthought](https://github.com/DebarghaG/proofofthought)

生成摘要时出错

---

## 94. Show HN: Cobalt – a pixel-art painting studio for the Nintendo DS

**原文标题**: Show HN: Cobalt – a pixel-art painting studio for the Nintendo DS

**原文链接**: [https://benbridle.com/projects/cobalt.html](https://benbridle.com/projects/cobalt.html)

生成摘要时出错

---

## 95. Benefits of choosing email over messaging

**原文标题**: Benefits of choosing email over messaging

**原文链接**: [https://www.spinellis.gr/blog/20250926/?li](https://www.spinellis.gr/blog/20250926/?li)

生成摘要时出错

---

## 96. Old Stockholm Telephone Tower

**原文标题**: Old Stockholm Telephone Tower

**原文链接**: [https://en.wikipedia.org/wiki/Old_Stockholm_telephone_tower](https://en.wikipedia.org/wiki/Old_Stockholm_telephone_tower)

生成摘要时出错

---

## 97. The Buchstabenmuseum Berlin is closing

**原文标题**: The Buchstabenmuseum Berlin is closing

**原文链接**: [https://www.buchstabenmuseum.de/en/](https://www.buchstabenmuseum.de/en/)

生成摘要时出错

---

## 98. ICE plans to scour Facebook, TikTok, X, and even defunct Google+

**原文标题**: ICE plans to scour Facebook, TikTok, X, and even defunct Google+

**原文链接**: [https://www.theregister.com/2025/10/03/ice_contractors_social_media_spy/](https://www.theregister.com/2025/10/03/ice_contractors_social_media_spy/)

生成摘要时出错

---

## 99. Microsoft Surface Pen Compatibility / Interoperability FAQ (2024)

**原文标题**: Microsoft Surface Pen Compatibility / Interoperability FAQ (2024)

**原文链接**: [https://dancharblog.wordpress.com/2017/05/29/surface-pen-compatibility-interoperability-faq/](https://dancharblog.wordpress.com/2017/05/29/surface-pen-compatibility-interoperability-faq/)

生成摘要时出错

---

## 100. Mod. 5140 - IBM's First Laptop Computer

**原文标题**: Mod. 5140 - IBM's First Laptop Computer

**原文链接**: [https://richardsapperdesign.com/products/mod-5140/](https://richardsapperdesign.com/products/mod-5140/)

生成摘要时出错

---

