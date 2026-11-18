# Hacker News 热门文章摘要 (2026-11-18)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Nginx 未经身份验证的远程代码执行

**原文标题**: Unauthenticated remote code execution in Nginx

**原文链接**: [https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities](https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities)

2026 年底，研究人员披露了 Nginx 中的两个严重漏洞：**CVE-2026-123633** 和 **CVE-2026-123007**，两者的 CVSS 4.0 评分均为 9.2。这些缺陷允许攻击者在受影响的服务器上实现未经身份验证的远程代码执行（RCE），从而可能导致数据窃取、内容篡改或服务中断。

**核心技术细节：**
*   **CVE-2026-123633（释放后重用 - Use-After-Free）：** 发生在 HTTP/2 代理处理过程中。当请求仍处于活动状态时，连接被过早地标记为可重用并被释放。
*   **CVE-2026-123007（整数下溢 - Integer Underflow）：** 影响 HTTP/2 流量控制。由于对未使用的窗口配额进行了错误的“退还”，导致发生下溢并引发内存损坏。即使是仅提供静态文件的服务器，也可能因此被利用执行恶意代码。

**影响范围与缓解措施：**
这两个漏洞都要求启用 HTTP/2 才会受到影响。CVE-2026-123007 尤为值得关注，因为它自 2015 年起就一直存在于 Nginx 源码中。

建议相关机构：
1.  **立即升级**至 Nginx OSS 1.30.7（稳定版）或 1.31.9（主线版）。
2.  若无法立即打补丁，可将**禁用 HTTP/2** 作为临时缓解措施。

**AI 的作用：**
此次漏洞披露凸显了安全格局的转变：研究人员利用先进的 AI 模型（Gemini 4 Carbon 和 ChatGPT 5.6 Sol）发现并验证了这些长期存在且复杂的内存安全缺陷。这表明 AI 正在有效瓦解过去十多年来保护此类漏洞不被发现的复杂度障碍。

---

## 2. 七款具有可扩展性价比的新模型

**原文标题**: Seven new models at scalable price-performance

**原文链接**: [https://microsoft.ai/news/microsoft-ignite-2026/](https://microsoft.ai/news/microsoft-ignite-2026/)

2026年11月17日，MAI宣布发布七款新模型，旨在为各种应用场景提供可扩展的性价比。

此次发布的核心亮点是引入了“许可权重”（Licensed Weights），此举赋予了用户对模型的直接控制权。这种方式使企业机构在利用前沿性能的同时，能够保有在其自有基础设施中管理和部署该技术的自主权。

通过平衡顶尖能力与灵活的定价及性能规模，MAI旨在提供强大的AI工具，以满足企业和开发者的需求，并保持其易用性与可定制性。

---

## 3. 走进德意志银行

**原文标题**: Inside Deutsche Bank

**原文链接**: [https://www.inside-db.com/](https://www.inside-db.com/)

基于对超过1500万份泄露文件的全球调查，《德意志银行内幕》（Inside Deutsche Bank）揭露了其将利润置于合规之上的系统性文化，揭示了该银行在反金融犯罪和审计职能方面的深层缺陷。

此次调查突显了几项重大的丑闻和伦理违规行为：

*   **金融犯罪与可疑人物：** 该银行为一马发展公司（1MDB）在逃人员刘特佐（Jho Low）促成了超过1.72亿欧元的交易，并处理了与杰弗里·爱泼斯坦（Jeffrey Epstein）相关的6亿美元可疑付款——这一数额是此前已知金额的两倍。
*   **政治与寡头关联：** 泄露文件显示该银行与涉及唐纳德·特朗普公司的“洗钱”计划有关，并揭露了其在制裁压力下仍努力保护俄罗斯寡头利润的行为。此外，该行还为沙特王子穆罕默德·本·纳伊夫管理复杂的离岸结构，并与卡塔尔王室保持着模糊的利益界限。
*   **冲突与军备融资：** 尽管有内部政策限制，该银行仍为全球战争工业提供资金，包括通过莱昂纳多（Leonardo）等公司为加沙使用的武器提供供应，并向高风险冲突地区输送军备。
*   **全球腐败：** 文件显示，该银行是俄罗斯通过匈牙利进行洗钱的门户，并资助了因涉嫌腐败而受调查的西班牙黑名单企业。内部通信甚至显示，高管们在私下诋毁某些知名客户的同时，仍与之维持着丰厚的业务往来。

最终，这次泄密事件将德意志银行描绘成一个全球性的“纵容者”，为了维持与“高风险”客户、独裁政权及争议性权势人物的关系，它频繁视预警信号及内部安全保障机制于不顾。

---

## 4. DaisyRose-27B：1200任务强化学习将Qwen3.8在Terminal-Bench 4.1上的表现从5.6%提升至12%

**原文标题**: DaisyRose-27B: 1,200-task RL took Qwen3.8 from 5.6% to 12% on Terminal-Bench 4.1

**原文链接**: [https://www.radixark.com/blog/daisyrose-27b](https://www.radixark.com/blog/daisyrose-27b)

RadixArk 发布了其首个基于 Qwen3.8-27B 构建的模型 **DaisyRose-27B**。该模型通过开源的 **Miles** 框架利用强化学习 (RL) 技术，显著提升了在 Terminal-Bench 4.1 上的表现，其 pass@1 通过率从 5.6% 翻倍至 12.0%，同时在编程、推理和指令遵循基准测试中均有进步。

该模型的成功归功于三大核心支柱：

*   **高质量训练数据：** RadixArk 与 Eigent AI 合作开发了 1,200 个经过精选的长时程任务。这些任务专门针对模型弱点设计，旨在防止奖励作弊，并支持包含多达 100 万个 Token 和 100 多次工具调用的复杂会话。
*   **高效基础设施 (Miles)：** 训练采用了全异步强化学习框架，模型在智能体同步工作的同时进行学习。该方案实现了 37% 的模型算力利用率 (MFU)——显著高于标准的基于 Megatron 的训练器——从而使训练成本降低了 57%，并将端到端速度提升了一倍。
*   **鲁棒的沙箱环境：** 团队采用了基于 AgentENV 项目的专用沙箱服务。它在近百万个任务环境中保持了 99.95% 的成功率。通过使用动态内存分配，他们将云基础设施成本相较于标准供应商降低了 80%。

**DaisyRose-27B** 现已在 Hugging Face 上线，提供 BF16、FP8 和 NVFP4 格式。RadixArk 同时也开源了 **Miles** 强化学习框架，鼓励社区利用这些高效方法构建和训练自己的专用智能体。

---

## 5. AI 智能体在审计测试中的提问表现优于毕马威会计师

**原文标题**: AI agents ask better questions than KPMG accountants in audit trial

**原文链接**: [https://europeanbusinessmagazine.com/ai-agents-better-questions-kpmg/](https://europeanbusinessmagazine.com/ai-agents-better-questions-kpmg/)

毕马威英国分所（KPMG UK）最近完成了一项名为“指数项目”（Project Exponential）的里程碑式试验，证明了人工智能代理在分析深度上有时能超越人类审计师。通过使用100多个AI代理审查一家富时250指数公司的账目，该公司发现该技术识别出了人类团队所忽略的问题，并提出了深入的调查性提问。

该实验标志着AI正从单纯的辅助工具转向能够管理整个工作流程（包括数据收集、协调和起草结论）的自主代理系统。尽管AI在某些领域展示了卓越的调查能力，但人类的监督依然至关重要。例如，当一个代理未能正确将监管要求与公司文件匹配时，审计师必须介入干预。

此次试验的成功挑战了传统的“四大”会计师事务所业务模式，即依靠庞大的初级会计师团队处理重复性的数据任务。通过自动化这些流程，事务所可以实现更快速、更全面的审计，使资深专业人员能够专注于复杂的专业判断。然而，毕马威指出，由于数据质量不佳以及需要人类承担问责责任等障碍，该技术尚未准备好在全公司范围内推广。

包括英国财务报告委员会（FRC）在内的监管机构警告称，AI绝不能损害审计师的独立性或职业怀疑精神。虽然该试验并不意味着AI会立即取代会计师，但它证明了机器正在侵入曾经由人类专业知识主导的领域。审计行业正面临着人类审计师角色被重新定义的未来：人类将专注于高层监督，而机器则处理大部分的分析性调查工作。

---

## 6. DNS解析器并非打击盗版的正确场所

**原文标题**: DNS resolvers are the wrong place to fight piracy

**原文链接**: [https://techstackups.com/articles/quad9-leaves-france-dns-blocking/](https://techstackups.com/articles/quad9-leaves-france-dns-blocking/)

以隐私保护和恶意软件防护著称的瑞士非营利性 DNS 解析服务商 Quad9 宣布，将于 2026 年 11 月 24 日停止在法国的业务。此次退出源于巴黎法院的一项裁决：由于 Quad9 拒绝根据 beIN Sports 的要求屏蔽盗版体育直播域名，法院对其处以每日 1,000 欧元的罚款。鉴于还有 20 起类似案件待审，该非营利组织坚称其无法承担巨额诉讼费用或潜在罚款。

文章认为，出于以下原因，DNS 解析器并非打击盗版的合适环节：

*   **低效性：** DNS 屏蔽并不能删除内容，而只是隐藏了指向内容的路径。用户可以通过使用 VPN 或替代解析器轻松绕过此类屏蔽。
*   **技术局限：** 作为一家注重隐私且不保留用户记录的机构，Quad9 无法可靠地仅针对法国用户实施“地理屏蔽”。若实施全球屏蔽，则会将法国法律不公平地强加于世界其他地区。
*   **附带损害：** DNS 过滤是一种粗放的工具，存在误封合法网站的风险。此外，排挤专注于安全的解析器会使包括医院和政府机构在内的法国关键基础设施更容易受到恶意软件和网络钓鱼的攻击。
*   **市场集中化：** 高昂的合规成本将非营利组织和小型实体逐出市场，使互联网被少数几家负担得起法律开支的大型企业所掌控。

尽管法国法律（第 L.333-10 条）已扩大范围，允许实施“动态”和自动屏蔽，但文章指出，盗版率并未随着屏蔽数量的增加而相应下降。作者总结称，这种司法压力不仅未能有效解决版权侵权的根本问题，反而损害了数字主权和用户安全，并开创了一个正向全欧洲蔓延的危险先例。

---

## 7. Gemini 4 霓虹

**原文标题**: Gemini 4 Neon

**原文链接**: [https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)

2026年11月18日，Google DeepMind 宣布推出 **Gemini 4 Neon**。这是一款前沿级 AI 模型，专为在复杂的工程、科学及知识型工作流中实现高速、端到端的任务处理而设计。在 Gemini 4 系列中，Neon 的定位介于高容量的“Carbon”与轻量级的“Hydrogen”之间，在深度推理与运行效率之间实现了战略平衡。

**核心性能与能力**
Neon 在 Artificial Analysis 智能指数中排名全球第 3，在 Agent Arena 指数中排名第 2。它拥有 **100 万 token 的上下文窗口**，在多步指令遵循方面表现卓越，并具有 Google 迄今为止最低的幻觉编造率。其显著特色是设有四个“思维级别”，允许用户根据具体工作负载需求灵活扩展模型的智能水平与成本。

**专项应用**
*   **编程与工程：** Neon 在 Artificial Analysis 编程代理指数中位居榜首，能够执行精准的多文件调试和仓库级代码重构。
*   **Google Antigravity：** 通过集成“Antigravity”套件，Neon 利用 `/swarm` 能力执行大规模任务，例如生成包含 10 万个单元格的交互式电子表格，或从零开始构建复杂的 3D 环境。
*   **网络安全：** 专门的“Neon for cyber”变体在漏洞发现、补丁修复和安全代码生成方面提供顶尖性能。

**效率与安全**
该模型具有极高的成本效益，价格为每百万输入 token 3 美元（缓存 token 可享受 95% 的折扣）。它包含了先进的实时防护机制，以防止网络和生物安全滥用，并在抵御间接提示注入攻击方面展现出行业领先的韧性。

**可用性**
Gemini 4 Neon 即日起通过 Gemini API、Google AI Studio 以及 Gemini for Business 陆续推出。此外，Google AI Pro 和 Ultra 订阅用户也可在 Gemini 应用及 Antigravity 平台中使用。

---

## 8. Cuttlefish on Mac: Android's Virtual Device Framework on Apple Silicon

**原文标题**: Cuttlefish on Mac: Android's Virtual Device Framework on Apple Silicon

**原文链接**: [https://engineering.fb.com/2026/11/13/android/cuttlefish-on-mac/](https://engineering.fb.com/2026/11/13/android/cuttlefish-on-mac/)

生成摘要时出错

---

## 9. 利用 OpenAI 模型助力芯片设计

**原文标题**: Advancing chip design with OpenAI models

**原文链接**: [https://openai.com/index/advancing-chip-design-with-our-models/](https://openai.com/index/advancing-chip-design-with-our-models/)

OpenAI 正在与博通（Broadcom）等半导体行业领军企业合作，将其先进的推理模型——特别是 **o1 系列**——应用于复杂的芯片设计领域。该举措旨在缩短开发周期，降低半导体工程中高昂的成本并突破技术瓶颈。

此次合作重点关注 AI 提升生产力的几个关键领域：

*   **Verilog 生成与调试：** OpenAI 模型协助工程师编写和修复硬件描述语言（HDL）代码，从而减少人为错误并加速初步设计阶段。
*   **逻辑验证：** 利用 o1 的思维链推理能力，模型可以识别芯片架构中人类工程师通常难以发现的复杂漏洞和边缘情况。
*   **工作流自动化：** AI 有助于简化电子设计自动化（EDA）工具的使用，并协助物理设计过程，而这些环节通常需要多年的专业经验。
*   **知识管理：** 模型充当智能助手，能够解析数千页的技术规范，为工程师的设计咨询提供即时、准确的解答。

博通已将这些模型整合到其内部工程工作流中，并报告称生产力和“工程速率”得到了显著提升。OpenAI 强调，o1 模型非常适合该领域，因为芯片设计需要严密的逻辑推理和精确度，而这正是标准大语言模型通常所欠缺的。

这一合作标志着技术领域一个重要的“良性循环”：OpenAI 模型正被用于设计驱动未来 AI 所需的硬件，这可能会带来更快、更高效的芯片，从而支撑全球 AI 创新的快速步伐。

---

## 10. The Cambridge Dictionary has named ‘human’ as the Word of the Year 2026

**原文标题**: The Cambridge Dictionary has named ‘human’ as the Word of the Year 2026

**原文链接**: [https://www.cam.ac.uk/news/cambridge-dictionary-reveals-word-of-the-year-2026](https://www.cam.ac.uk/news/cambridge-dictionary-reveals-word-of-the-year-2026)

The Cambridge Dictionary has named **"human"** as its Word of the Year for 2026, reflecting a global preoccupation with defining humanity as artificial intelligence increasingly blurs the line between people and machines. 

The selection highlights a year defined by debates over what distinguishes "human" qualities—such as feelings, faults, and compassion—from those of "artificial beings." Prominent figures have led the charge in defending human-centric values:
*   **Labor and Ethics:** Bill Gates advocated for "human reserved jobs," such as caregiving, while "AI godfather" Geoffrey Hinton and Pope Leo XIV warned against the potential for dehumanization and the rise of "alien beings."
*   **Creative Integrity:** Artists including Scarlett Johansson, Taylor Swift, and Billie Eilish challenged the "assault on human creativity" posed by AI replicas. This led to high-profile actions, such as Matthew McConaughey and Taylor Swift trademarking their likenesses, and the Authors Guild launching a "Human Authored" kitemark to protect writers.
*   **Philosophical Inquiry:** Academic experts at the University of Cambridge noted that AI is forcing society to revisit ancient questions regarding identity and consciousness. They emphasize that the future of AI is not inevitable but depends on deliberate human choices.

According to lexicographer Colin McIntosh, "human" was chosen because it captured the 2026 zeitgeist. The word represents a collective effort to place people at the center of technological progress and to safeguard the unique creativity and empathy that define the human experience.

---

## 11. Show HN: ExitPath – Open-source ways out of Slack, Notion and Microsoft 365

**原文标题**: Show HN: ExitPath – Open-source ways out of Slack, Notion and Microsoft 365

**原文链接**: [https://exitpath-ruddy.vercel.app/](https://exitpath-ruddy.vercel.app/)

生成摘要时出错

---

## 12. Show HN: Take Voyager 1 apart, down to a single memory chip

**原文标题**: Show HN: Take Voyager 1 apart, down to a single memory chip

**原文链接**: [https://rshekhar.com/voyager/](https://rshekhar.com/voyager/)

生成摘要时出错

---

## 13. A Collage Showing 49 Drill Holes Made by NASA's Curiosity Mars Rover

**原文标题**: A Collage Showing 49 Drill Holes Made by NASA's Curiosity Mars Rover

**原文链接**: [https://science.nasa.gov/photojournal/a-collage-showing-49-drill-holes-made-by-nasas-curiosity-mars-rover/](https://science.nasa.gov/photojournal/a-collage-showing-49-drill-holes-made-by-nasas-curiosity-mars-rover/)

生成摘要时出错

---

## 14. Genie 4 is now available

**原文标题**: Genie 4 is now available

**原文链接**: [https://blog.google/innovation-and-ai/models-and-research/google-deepmind/genie-4-now-available-project-genie/](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/genie-4-now-available-project-genie/)

生成摘要时出错

---

## 15. CrossPoint Reader

**原文标题**: CrossPoint Reader

**原文链接**: [https://crosspointreader.com](https://crosspointreader.com)

生成摘要时出错

---

## 16. The First Revolver: How We Got from Blackbeard's Six Pistols to the Six-Shooter

**原文标题**: The First Revolver: How We Got from Blackbeard's Six Pistols to the Six-Shooter

**原文链接**: [https://americanhandgunner.com/handguns/revolvers/the-first-revolver/](https://americanhandgunner.com/handguns/revolvers/the-first-revolver/)

生成摘要时出错

---

## 17. KVM: x86: Unconditionally reset MMU context when emulating INIT (CVE-2026-99312)

**原文标题**: KVM: x86: Unconditionally reset MMU context when emulating INIT (CVE-2026-99312)

**原文链接**: [https://www.cve.org/CVERecord?id=CVE-2026-99312](https://www.cve.org/CVERecord?id=CVE-2026-99312)

生成摘要时出错

---

## 18. Search Browser – Minimalist WebKit browser with Chrome extension support

**原文标题**: Search Browser – Minimalist WebKit browser with Chrome extension support

**原文链接**: [https://searchbrowser.app/](https://searchbrowser.app/)

生成摘要时出错

---

## 19. The Magic of Partial Evaluation

**原文标题**: The Magic of Partial Evaluation

**原文链接**: [https://jimmyhmiller.com/magic-of-partial-evaluation](https://jimmyhmiller.com/magic-of-partial-evaluation)

生成摘要时出错

---

## 20. The x86 CPU: From 4004 to 486

**原文标题**: The x86 CPU: From 4004 to 486

**原文链接**: [https://pikuma.com/blog/history-of-x86-4004-to-486](https://pikuma.com/blog/history-of-x86-4004-to-486)

生成摘要时出错

---

## 21. GTA6-like as a 942Kb UEFI bootable image

**原文标题**: GTA6-like as a 942Kb UEFI bootable image

**原文链接**: [https://github.com/eklavya-raj/gta6-uefi](https://github.com/eklavya-raj/gta6-uefi)

生成摘要时出错

---

## 22. Sexp Matrix

**原文标题**: Sexp Matrix

**原文链接**: [https://lisper.cc/ideas/entangle.html](https://lisper.cc/ideas/entangle.html)

生成摘要时出错

---

## 23. Energy-Based Reasoners: 385x more efficient inference

**原文标题**: Energy-Based Reasoners: 385x more efficient inference

**原文链接**: [https://energy-based-reasoners.github.io/](https://energy-based-reasoners.github.io/)

生成摘要时出错

---

## 24. A Primer on Fourier Series (2025)

**原文标题**: A Primer on Fourier Series (2025)

**原文链接**: [https://arxiv.org/abs/2510.18203](https://arxiv.org/abs/2510.18203)

生成摘要时出错

---

## 25. Why educational system is broken

**原文标题**: Why educational system is broken

**原文链接**: [https://keycybermonk.com/edu](https://keycybermonk.com/edu)

生成摘要时出错

---

## 26. F-22 Next-Generation micro–Data Transfer Cartridge (mDTC)

**原文标题**: F-22 Next-Generation micro–Data Transfer Cartridge (mDTC)

**原文链接**: [https://sam.gov/workspace/contract/opp/8948e8601e964c6aba9c801eee16b1be/view](https://sam.gov/workspace/contract/opp/8948e8601e964c6aba9c801eee16b1be/view)

生成摘要时出错

---

## 27. Horizon Labs Report

**原文标题**: Horizon Labs Report

**原文链接**: [https://horizon-labs.ai/](https://horizon-labs.ai/)

生成摘要时出错

---

## 28. Evidence (YC S21) Is Hiring

**原文标题**: Evidence (YC S21) Is Hiring

**原文链接**: [https://www.ycombinator.com/companies/evidence/jobs/1xb9PpP-founding-gtm-lead](https://www.ycombinator.com/companies/evidence/jobs/1xb9PpP-founding-gtm-lead)

生成摘要时出错

---

## 29. A live service duress prototype

**原文标题**: A live service duress prototype

**原文链接**: [https://github.com/Ymsniper/vault-share](https://github.com/Ymsniper/vault-share)

生成摘要时出错

---

## 30. Octopus, Gecko and Tortoise: the 3 scanners hunting your AI keys

**原文标题**: Octopus, Gecko and Tortoise: the 3 scanners hunting your AI keys

**原文链接**: [https://tin.computer/blog/fake-ai-crawler-secrets-scanners](https://tin.computer/blog/fake-ai-crawler-secrets-scanners)

生成摘要时出错

---

## 31. US charges Irishman with destroying a $60M Air Force C-130

**原文标题**: US charges Irishman with destroying a $60M Air Force C-130

**原文链接**: [https://taskandpurpose.com/news/c-130-damage-ireland-daithi-ocorrain/](https://taskandpurpose.com/news/c-130-damage-ireland-daithi-ocorrain/)

生成摘要时出错

---

## 32. Show HN: Type Fighter 2

**原文标题**: Show HN: Type Fighter 2

**原文链接**: [https://typefighter2.com/](https://typefighter2.com/)

生成摘要时出错

---

## 33. Show HN: Robotics needs better CAD, so I wrote a B-rep kernel and 3,487 tests

**原文标题**: Show HN: Robotics needs better CAD, so I wrote a B-rep kernel and 3,487 tests

**原文链接**: [https://springcraft-ai.github.io/springrep/](https://springcraft-ai.github.io/springrep/)

生成摘要时出错

---

## 34. SuperEMeans: Making e-means 3× faster

**原文标题**: SuperEMeans: Making e-means 3× faster

**原文链接**: [https://www.lkuffo.com/superemeans/](https://www.lkuffo.com/superemeans/)

生成摘要时出错

---

## 35. Lakegres: Vector search on existing Open/Hudi/Iceberg tables

**原文标题**: Lakegres: Vector search on existing Open/Hudi/Iceberg tables

**原文链接**: [https://www.onehouse.ai/blog/lakegres-vector-search-on-open-table-formats](https://www.onehouse.ai/blog/lakegres-vector-search-on-open-table-formats)

生成摘要时出错

---

## 36. Why is Gemini 4 Carbon taking so long?

**原文标题**: Why is Gemini 4 Carbon taking so long?

**原文链接**: [https://kernel.dev/blog/why-is-gemini-4-carbon-taking-so-long/](https://kernel.dev/blog/why-is-gemini-4-carbon-taking-so-long/)

生成摘要时出错

---

## 37. VB Harness – Make local coding agents verify their own work

**原文标题**: VB Harness – Make local coding agents verify their own work

**原文链接**: [https://github.com/Viktotovich/vb-harness-for-agentic-building](https://github.com/Viktotovich/vb-harness-for-agentic-building)

生成摘要时出错

---

## 38. Java4Shell: RCE in OpenJDK when processing Base64

**原文标题**: Java4Shell: RCE in OpenJDK when processing Base64

**原文链接**: [https://calif.io/java4shell/](https://calif.io/java4shell/)

生成摘要时出错

---

## 39. Just Because You Can, Doesn't Mean You Should: Re-Evaluating Galera Node Weights

**原文标题**: Just Because You Can, Doesn't Mean You Should: Re-Evaluating Galera Node Weights

**原文链接**: [https://www.percona.com/blog/just-because-you-can-doesnt-mean-you-should-re-evaluating-galera-node-weights/](https://www.percona.com/blog/just-because-you-can-doesnt-mean-you-should-re-evaluating-galera-node-weights/)

生成摘要时出错

---

## 40. When Everything Has Changed, What Do We Do Next?

**原文标题**: When Everything Has Changed, What Do We Do Next?

**原文链接**: [https://css-tricks.com/when-everything-has-changed/](https://css-tricks.com/when-everything-has-changed/)

生成摘要时出错

---

## 41. Show HN: Beat – a to-do list that completes its own tasks

**原文标题**: Show HN: Beat – a to-do list that completes its own tasks

**原文链接**: [https://gobeat.ai/auth/login](https://gobeat.ai/auth/login)

生成摘要时出错

---

## 42. New FreeBSD Pkgbase(8) Tool

**原文标题**: New FreeBSD Pkgbase(8) Tool

**原文链接**: [https://vermaden.wordpress.com/2026/11/10/freebsd-pkgbase-update-tool/](https://vermaden.wordpress.com/2026/11/10/freebsd-pkgbase-update-tool/)

生成摘要时出错

---

## 43. Scottish HTTP Codes

**原文标题**: Scottish HTTP Codes

**原文链接**: [https://underwood.network/http/scots.html](https://underwood.network/http/scots.html)

生成摘要时出错

---

## 44. What is the randomart image for? (2023)

**原文标题**: What is the randomart image for? (2023)

**原文链接**: [https://bytes.zone/posts/what-is-the-randomart-image-for/](https://bytes.zone/posts/what-is-the-randomart-image-for/)

生成摘要时出错

---

## 45. Quad9's withdrawal from France: A canary in the coal mine

**原文标题**: Quad9's withdrawal from France: A canary in the coal mine

**原文链接**: [https://blog.cloudflare.com/quad9-withdrawal-from-france/](https://blog.cloudflare.com/quad9-withdrawal-from-france/)

生成摘要时出错

---

## 46. My Emacs 31 contributions

**原文标题**: My Emacs 31 contributions

**原文链接**: [https://xenodium.com/my-emacs-31-contributions](https://xenodium.com/my-emacs-31-contributions)

生成摘要时出错

---

## 47. Claude was trained on protein sequences at scale

**原文标题**: Claude was trained on protein sequences at scale

**原文链接**: [http://xinmingtu.cn/blog/2026/claude-opus-5-5-protein-sequences/](http://xinmingtu.cn/blog/2026/claude-opus-5-5-protein-sequences/)

生成摘要时出错

---

## 48. How to Bypass Rust's Orphan Rule

**原文标题**: How to Bypass Rust's Orphan Rule

**原文链接**: [https://edvong.com/bypass-orphan-rule/](https://edvong.com/bypass-orphan-rule/)

生成摘要时出错

---

## 49. Show HN: PocketOps for SigNoz: The Open Source Datadog Alternative

**原文标题**: Show HN: PocketOps for SigNoz: The Open Source Datadog Alternative

**原文链接**: [https://github.com/avens19/pocketops](https://github.com/avens19/pocketops)

生成摘要时出错

---

## 50. U.S. School Districts Weigh Breaking Up with Google Search over A.I

**原文标题**: U.S. School Districts Weigh Breaking Up with Google Search over A.I

**原文链接**: [https://www.nytimes.com/2026/11/18/technology/google-gemini-ai-search-schools-nyc-la-chicago.html](https://www.nytimes.com/2026/11/18/technology/google-gemini-ai-search-schools-nyc-la-chicago.html)

生成摘要时出错

---

## 51. Can Universities Survive? AI vs. Higher Education [audio]

**原文标题**: Can Universities Survive? AI vs. Higher Education [audio]

**原文链接**: [https://www.ppfideas.com/episodes/can-universities-survive-ai-vs-higher-education](https://www.ppfideas.com/episodes/can-universities-survive-ai-vs-higher-education)

生成摘要时出错

---

## 52. Anthropic reportedly prices its IPO at $83 per share, valuing at $1.5T

**原文标题**: Anthropic reportedly prices its IPO at $83 per share, valuing at $1.5T

**原文链接**: [https://apnews.com/article/anthropic-ipo-pricing-70b660ddf900d90bbf484ecdf1fb441c](https://apnews.com/article/anthropic-ipo-pricing-70b660ddf900d90bbf484ecdf1fb441c)

生成摘要时出错

---

## 53. Show HN: Poptato – App launcher, command runner, and fuzzy menu for Linux

**原文标题**: Show HN: Poptato – App launcher, command runner, and fuzzy menu for Linux

**原文链接**: [https://github.com/skorotkiewicz/poptato](https://github.com/skorotkiewicz/poptato)

生成摘要时出错

---

## 54. Show HN: Nobody blocks a keyboard – Rooted Android as a physical USB Deck

**原文标题**: Show HN: Nobody blocks a keyboard – Rooted Android as a physical USB Deck

**原文链接**: [https://github.com/mr-anjaneyam/Emittr](https://github.com/mr-anjaneyam/Emittr)

生成摘要时出错

---

## 55. Google's AI answers reducing search traffic by 40%

**原文标题**: Google's AI answers reducing search traffic by 40%

**原文链接**: [https://revscope.co/blog/search-seo-geo-2026/](https://revscope.co/blog/search-seo-geo-2026/)

生成摘要时出错

---

## 56. A Perfect SimCity

**原文标题**: A Perfect SimCity

**原文链接**: [https://www.jeffquast.com/post/a-perfect-simcity/](https://www.jeffquast.com/post/a-perfect-simcity/)

生成摘要时出错

---

## 57. Demazure Operators for Beginners

**原文标题**: Demazure Operators for Beginners

**原文链接**: [https://webspace.science.uu.nl/~kalle101/Demazure.html](https://webspace.science.uu.nl/~kalle101/Demazure.html)

生成摘要时出错

---

## 58. M.C. Escher's Art Creates Mathematical Worlds

**原文标题**: M.C. Escher's Art Creates Mathematical Worlds

**原文链接**: [https://www.quantamagazine.org/how-m-c-eschers-art-creates-bizarre-mathematical-worlds-20261118/](https://www.quantamagazine.org/how-m-c-eschers-art-creates-bizarre-mathematical-worlds-20261118/)

生成摘要时出错

---

## 59. M.C. Escher's Art Creates Mathematical Worlds

**原文标题**: M.C. Escher's Art Creates Mathematical Worlds

**原文链接**: [https://www.quantamagazine.org/how-m-c-eschers-art-creates-bizarre-mathematical-worlds-20261118/](https://www.quantamagazine.org/how-m-c-eschers-art-creates-bizarre-mathematical-worlds-20261118/)

生成摘要时出错

---

## 60. Show HN: BPM – Baby Plus Music Visualizer

**原文标题**: Show HN: BPM – Baby Plus Music Visualizer

**原文链接**: [https://hberg.com/bpm/](https://hberg.com/bpm/)

生成摘要时出错

---

## 61. ID.me terms required for IRS sign-in

**原文标题**: ID.me terms required for IRS sign-in

**原文链接**: [https://consumerrights.wiki/w/ID.me_terms_required_for_IRS_sign-in](https://consumerrights.wiki/w/ID.me_terms_required_for_IRS_sign-in)

生成摘要时出错

---

## 62. Nvidia stopped disclosing Singapore sales as revenues hit $104B

**原文标题**: Nvidia stopped disclosing Singapore sales as revenues hit $104B

**原文链接**: [https://www.ft.com/content/dbde7a30-548c-4f9d-a4be-7898a0c24dcf](https://www.ft.com/content/dbde7a30-548c-4f9d-a4be-7898a0c24dcf)

生成摘要时出错

---

## 63. AI is killing All About Berlin

**原文标题**: AI is killing All About Berlin

**原文链接**: [https://nicolasbouliane.com/blog/death-by-ai](https://nicolasbouliane.com/blog/death-by-ai)

生成摘要时出错

---

## 64. Tencent Hy4 Flash

**原文标题**: Tencent Hy4 Flash

**原文链接**: [https://hy.tencent.ai/research/hy4-flash](https://hy.tencent.ai/research/hy4-flash)

生成摘要时出错

---

## 65. Steve Jobs Core Animation Demo from WWDC 2007

**原文标题**: Steve Jobs Core Animation Demo from WWDC 2007

**原文链接**: [https://lucas.love/100/058](https://lucas.love/100/058)

生成摘要时出错

---

## 66. The Codex Sandbox

**原文标题**: The Codex Sandbox

**原文链接**: [https://openai.com/index/inside-the-codex-sandbox/](https://openai.com/index/inside-the-codex-sandbox/)

生成摘要时出错

---

## 67. Carnegie Mellon is putting computer science courses on YouTube for free

**原文标题**: Carnegie Mellon is putting computer science courses on YouTube for free

**原文链接**: [https://www.cs.cmu.edu/learn/](https://www.cs.cmu.edu/learn/)

生成摘要时出错

---

## 68. When AI Knows More Than It Can Offer

**原文标题**: When AI Knows More Than It Can Offer

**原文链接**: [https://medium.com/@smoking2man/when-ai-knows-more-than-it-can-offer-how-training-turns-an-intelligent-assistant-into-a-generator-7e700f05163e](https://medium.com/@smoking2man/when-ai-knows-more-than-it-can-offer-how-training-turns-an-intelligent-assistant-into-a-generator-7e700f05163e)

生成摘要时出错

---

## 69. IPv6 delegation, an unusually subtle failure mode

**原文标题**: IPv6 delegation, an unusually subtle failure mode

**原文链接**: [https://savyasacheejha.com/posts/why-odhcpd/](https://savyasacheejha.com/posts/why-odhcpd/)

生成摘要时出错

---

## 70. Gemini 4 Neon

**原文标题**: Gemini 4 Neon

**原文链接**: [https://aistudio.google.com/docs/models/gemini-4-neon](https://aistudio.google.com/docs/models/gemini-4-neon)

生成摘要时出错

---

## 71. Pikuma: Fundamentals of Computer Science and Mathematics

**原文标题**: Pikuma: Fundamentals of Computer Science and Mathematics

**原文链接**: [https://pikuma.com/](https://pikuma.com/)

生成摘要时出错

---

## 72. Show HN: Fun with bicycle trainers and web APIs

**原文标题**: Show HN: Fun with bicycle trainers and web APIs

**原文链接**: [https://joelriley.com/fun-with-trainers](https://joelriley.com/fun-with-trainers)

生成摘要时出错

---

## 73. Amazon and Google will together own nearly 30% of Anthropic after its IPO

**原文标题**: Amazon and Google will together own nearly 30% of Anthropic after its IPO

**原文链接**: [https://techcrunch.com/2026/11/17/amazon-and-google-will-together-own-nearly-30-of-anthropic-after-its-ipo/](https://techcrunch.com/2026/11/17/amazon-and-google-will-together-own-nearly-30-of-anthropic-after-its-ipo/)

生成摘要时出错

---

## 74. Forking TuxGuitar into a 17-EDO tab editor

**原文标题**: Forking TuxGuitar into a 17-EDO tab editor

**原文链接**: [https://frogwizard.bearblog.dev/tuxguitar-17edo/](https://frogwizard.bearblog.dev/tuxguitar-17edo/)

生成摘要时出错

---

## 75. Highly classified US national security communications network goes down

**原文标题**: Highly classified US national security communications network goes down

**原文链接**: [https://www.cnn.com/2026/11/17/politics/highly-classified-national-security-communications-network-goes-down](https://www.cnn.com/2026/11/17/politics/highly-classified-national-security-communications-network-goes-down)

生成摘要时出错

---

## 76. Waymo pulls driverless taxis from all US freeways

**原文标题**: Waymo pulls driverless taxis from all US freeways

**原文链接**: [https://www.bbc.com/news/articles/cmy86pp336qlo](https://www.bbc.com/news/articles/cmy86pp336qlo)

生成摘要时出错

---

## 77. New Evidence Shows School Phone Bans Are Gradually Improving Test Scores

**原文标题**: New Evidence Shows School Phone Bans Are Gradually Improving Test Scores

**原文链接**: [https://www.nytimes.com/2026/11/17/upshot/school-phone-bans-study-scores.html](https://www.nytimes.com/2026/11/17/upshot/school-phone-bans-study-scores.html)

生成摘要时出错

---

## 78. Anthropic Prices IPO at $83 a Share

**原文标题**: Anthropic Prices IPO at $83 a Share

**原文链接**: [https://www.wsj.com/finance/stocks/anthropic-prices-ipo-at-83-a-share-0290494c](https://www.wsj.com/finance/stocks/anthropic-prices-ipo-at-83-a-share-0290494c)

生成摘要时出错

---

## 79. Google Buys Worker Data from Spirit Airlines in a New Market to Feed AI

**原文标题**: Google Buys Worker Data from Spirit Airlines in a New Market to Feed AI

**原文链接**: [https://www.nytimes.com/2026/11/18/business/economy/google-spirit-employee-data-ai.html](https://www.nytimes.com/2026/11/18/business/economy/google-spirit-employee-data-ai.html)

生成摘要时出错

---

## 80. Microsoft's ONNX Runtime has disappeared from GitHub

**原文标题**: Microsoft's ONNX Runtime has disappeared from GitHub

**原文链接**: [https://github.com/microsoft/onnxruntime](https://github.com/microsoft/onnxruntime)

生成摘要时出错

---

## 81. Cerebras Disaggregated Inference

**原文标题**: Cerebras Disaggregated Inference

**原文链接**: [https://www.cerebras.ai/blog/cerebras-launches-disaggregated-inference](https://www.cerebras.ai/blog/cerebras-launches-disaggregated-inference)

生成摘要时出错

---

## 82. Web Browser Engineering (2021)

**原文标题**: Web Browser Engineering (2021)

**原文链接**: [https://browser.engineering/](https://browser.engineering/)

生成摘要时出错

---

## 83. Linux/4004

**原文标题**: Linux/4004

**原文链接**: [https://dmitry.gr/?r=05.Projects&proj=35.%20Linux4004](https://dmitry.gr/?r=05.Projects&proj=35.%20Linux4004)

生成摘要时出错

---

## 84. Harvard researchers find AI coding agents shifted the bottleneck to code review

**原文标题**: Harvard researchers find AI coding agents shifted the bottleneck to code review

**原文链接**: [https://complexdiscovery.com/harvard-researchers-find-ai-coding-agents-shifted-the-bottleneck-to-code-review/](https://complexdiscovery.com/harvard-researchers-find-ai-coding-agents-shifted-the-bottleneck-to-code-review/)

生成摘要时出错

---

## 85. Apple Services Down

**原文标题**: Apple Services Down

**原文链接**: [https://developer.apple.com/system-status/](https://developer.apple.com/system-status/)

生成摘要时出错

---

## 86. Not Everything Needs an LLM

**原文标题**: Not Everything Needs an LLM

**原文链接**: [https://newsletter.posthog.com/p/decision-models](https://newsletter.posthog.com/p/decision-models)

生成摘要时出错

---

## 87. Archive Team is archiving the Apple Support Community

**原文标题**: Archive Team is archiving the Apple Support Community

**原文链接**: [https://wiki.archiveteam.org/index.php/Apple_Discussions](https://wiki.archiveteam.org/index.php/Apple_Discussions)

生成摘要时出错

---

## 88. Gateway-Free Kafka Streaming from FPGA-Based Detectors on Zynq-7000

**原文标题**: Gateway-Free Kafka Streaming from FPGA-Based Detectors on Zynq-7000

**原文链接**: [https://arxiv.org/abs/2611.22674](https://arxiv.org/abs/2611.22674)

生成摘要时出错

---

## 89. The Quad9 Alternatives

**原文标题**: The Quad9 Alternatives

**原文链接**: [https://eualternative.eu/guides/quad9-alternatives/](https://eualternative.eu/guides/quad9-alternatives/)

生成摘要时出错

---

## 90. Gemini 4 Neon

**原文标题**: Gemini 4 Neon

**原文链接**: [https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/guides/gemini-4-neon](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/guides/gemini-4-neon)

生成摘要时出错

---

## 91. Phrack 73

**原文标题**: Phrack 73

**原文链接**: [https://phrack.org/issues/73/introduction_md](https://phrack.org/issues/73/introduction_md)

生成摘要时出错

---

## 92. Fun with Constrained Programming (2012)

**原文标题**: Fun with Constrained Programming (2012)

**原文链接**: [https://blog.cmpxchg8b.com/2012/09/fun-with-constrained-programming.html](https://blog.cmpxchg8b.com/2012/09/fun-with-constrained-programming.html)

生成摘要时出错

---

## 93. MAI Code 2 and Code 2 Flash

**原文标题**: MAI Code 2 and Code 2 Flash

**原文链接**: [https://microsoft.ai/news/introducing-mai-code-2-and-mai-code-2-flash/](https://microsoft.ai/news/introducing-mai-code-2-and-mai-code-2-flash/)

生成摘要时出错

---

## 94. 350 years ago, Ole Rømer discovered that light has a finite speed

**原文标题**: 350 years ago, Ole Rømer discovered that light has a finite speed

**原文链接**: [https://www.sciencenorway.no/culture-history-history-of-science/350-years-ago-this-man-discovered-that-light-has-a-finite-speed/2737969](https://www.sciencenorway.no/culture-history-history-of-science/350-years-ago-this-man-discovered-that-light-has-a-finite-speed/2737969)

生成摘要时出错

---

## 95. Jensen Huang's fall hits 'open' models in boost to Anthropic and OpenAI

**原文标题**: Jensen Huang's fall hits 'open' models in boost to Anthropic and OpenAI

**原文链接**: [https://www.ft.com/content/418ca885-fbcf-4b9f-a8b9-2bd60b543fc5](https://www.ft.com/content/418ca885-fbcf-4b9f-a8b9-2bd60b543fc5)

生成摘要时出错

---

## 96. When Free Software Isn't Free Enough

**原文标题**: When Free Software Isn't Free Enough

**原文链接**: [https://foss.life/notes/2026/free-software-isnt-free-enough/](https://foss.life/notes/2026/free-software-isnt-free-enough/)

生成摘要时出错

---

## 97. Energy drinks linked to 11 times more reports of cardiac arrest

**原文标题**: Energy drinks linked to 11 times more reports of cardiac arrest

**原文链接**: [https://www.sciencedaily.com/releases/2026/11/261110042543.htm](https://www.sciencedaily.com/releases/2026/11/261110042543.htm)

生成摘要时出错

---

## 98. Who Builds the Machines That Build the Machines?

**原文标题**: Who Builds the Machines That Build the Machines?

**原文链接**: [https://read.corematter.com/p/section-232-us-machine-tools](https://read.corematter.com/p/section-232-us-machine-tools)

生成摘要时出错

---

## 99. Show HN: Unref – A Python dead code finder built on Ruff's parser

**原文标题**: Show HN: Unref – A Python dead code finder built on Ruff's parser

**原文链接**: [https://github.com/Apakottur/unref](https://github.com/Apakottur/unref)

生成摘要时出错

---

## 100. Show HN: Alloy CSS, dialogs, menus and tabs that work with JavaScript off

**原文标题**: Show HN: Alloy CSS, dialogs, menus and tabs that work with JavaScript off

**原文链接**: [https://alloyhtml.com/example.html](https://alloyhtml.com/example.html)

生成摘要时出错

---

