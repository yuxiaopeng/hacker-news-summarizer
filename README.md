# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-11-18.md)

*最后自动更新时间: 2026-11-18 23:42:37*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-11-18](output/hacker_news_summary_2026-11-18.md) |
| 2 | [2026-11-17](output/hacker_news_summary_2026-11-17.md) |
| 3 | [2026-11-15](output/hacker_news_summary_2026-11-15.md) |
| 4 | [2026-11-11](output/hacker_news_summary_2026-11-11.md) |
| 5 | [2026-11-14](output/hacker_news_summary_2026-11-14.md) |
| 6 | [2026-11-10](output/hacker_news_summary_2026-11-10.md) |
| 7 | [2026-11-12](output/hacker_news_summary_2026-11-12.md) |
| 8 | [2026-11-13](output/hacker_news_summary_2026-11-13.md) |
| 9 | [2026-11-05](output/hacker_news_summary_2026-11-05.md) |
| 10 | [2026-11-06](output/hacker_news_summary_2026-11-06.md) |
| 11 | [2026-11-04](output/hacker_news_summary_2026-11-04.md) |
| 12 | [2026-11-08](output/hacker_news_summary_2026-11-08.md) |
| 13 | [2026-11-07](output/hacker_news_summary_2026-11-07.md) |
| 14 | [2026-10-30](output/hacker_news_summary_2026-10-30.md) |
| 15 | [2026-11-03](output/hacker_news_summary_2026-11-03.md) |
| 16 | [2026-10-31](output/hacker_news_summary_2026-10-31.md) |
| 17 | [2026-11-01](output/hacker_news_summary_2026-11-01.md) |
| 18 | [2026-10-29](output/hacker_news_summary_2026-10-29.md) |
| 19 | [2026-10-25](output/hacker_news_summary_2026-10-25.md) |
| 20 | [2026-10-28](output/hacker_news_summary_2026-10-28.md) |
| 21 | [2026-10-24](output/hacker_news_summary_2026-10-24.md) |
| 22 | [2026-10-27](output/hacker_news_summary_2026-10-27.md) |
| 23 | [2026-10-26](output/hacker_news_summary_2026-10-26.md) |
| 24 | [2026-10-21](output/hacker_news_summary_2026-10-21.md) |
| 25 | [2026-10-23](output/hacker_news_summary_2026-10-23.md) |
| 26 | [2026-10-20](output/hacker_news_summary_2026-10-20.md) |
| 27 | [2026-10-22](output/hacker_news_summary_2026-10-22.md) |
| 28 | [2026-10-19](output/hacker_news_summary_2026-10-19.md) |
| 29 | [2026-10-16](output/hacker_news_summary_2026-10-16.md) |
| 30 | [2026-10-17](output/hacker_news_summary_2026-10-17.md) |
| 31 | [2026-10-15](output/hacker_news_summary_2026-10-15.md) |
| 32 | [2026-10-18](output/hacker_news_summary_2026-10-18.md) |
| 33 | [2026-10-11](output/hacker_news_summary_2026-10-11.md) |
| 34 | [2026-10-12](output/hacker_news_summary_2026-10-12.md) |
| 35 | [2026-10-10](output/hacker_news_summary_2026-10-10.md) |
| 36 | [2026-10-14](output/hacker_news_summary_2026-10-14.md) |
| 37 | [2026-10-13](output/hacker_news_summary_2026-10-13.md) |
| 38 | [2026-10-09](output/hacker_news_summary_2026-10-09.md) |
| 39 | [2026-10-06](output/hacker_news_summary_2026-10-06.md) |
| 40 | [2026-10-08](output/hacker_news_summary_2026-10-08.md) |
| 41 | [2026-10-04](output/hacker_news_summary_2026-10-04.md) |
| 42 | [2026-10-07](output/hacker_news_summary_2026-10-07.md) |
| 43 | [2026-10-05](output/hacker_news_summary_2026-10-05.md) |
| 44 | [2026-10-02](output/hacker_news_summary_2026-10-02.md) |
| 45 | [2026-09-28](output/hacker_news_summary_2026-09-28.md) |
| 46 | [2026-09-29](output/hacker_news_summary_2026-09-29.md) |
| 47 | [2026-10-03](output/hacker_news_summary_2026-10-03.md) |
| 48 | [2026-10-01](output/hacker_news_summary_2026-10-01.md) |
| 49 | [2026-09-30](output/hacker_news_summary_2026-09-30.md) |
| 50 | [2026-09-26](output/hacker_news_summary_2026-09-26.md) |
| 51 | [2026-09-25](output/hacker_news_summary_2026-09-25.md) |
| 52 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 53 | [2026-09-27](output/hacker_news_summary_2026-09-27.md) |
| 54 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 55 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 56 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 57 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 58 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 59 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 60 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 61 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 62 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 63 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 64 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 65 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 66 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 67 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 68 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 69 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 70 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 71 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 72 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 73 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 74 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 75 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 76 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 77 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 78 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 79 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 80 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 81 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 82 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 83 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 84 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 85 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 86 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 87 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 88 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 89 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 90 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 91 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 92 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 93 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 94 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 95 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 96 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 97 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 98 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 99 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 100 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 101 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 102 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 103 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 104 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 105 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 106 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 107 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 108 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 109 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 110 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 111 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 112 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 113 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 114 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 115 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 116 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 117 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 118 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 119 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 120 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 121 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 122 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 123 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 124 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 125 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 126 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 127 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 128 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 129 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 130 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 131 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 132 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 133 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 134 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 135 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 136 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 137 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 138 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 139 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 140 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 141 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 142 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 143 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 144 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 145 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 146 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 147 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 148 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 149 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 150 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 151 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 152 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 153 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 154 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 155 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 156 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 157 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 158 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 159 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 160 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 161 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 162 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 163 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 164 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 165 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 166 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 167 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 168 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 169 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 170 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 171 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 172 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 173 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 174 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 175 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 176 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 177 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 178 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 179 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 180 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 181 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 182 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 183 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 184 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 185 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 186 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 187 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 188 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 189 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 190 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 191 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 192 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 193 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 194 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 195 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 196 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 197 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 198 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 199 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 200 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 201 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 202 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 203 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 204 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 205 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 206 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 207 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 208 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 209 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 210 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 211 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 212 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 213 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 214 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 215 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 216 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 217 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 218 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 219 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 220 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 221 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 222 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 223 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 224 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 225 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 226 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 227 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 228 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 229 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 230 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 231 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 232 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 233 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 234 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 235 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 236 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 237 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 238 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 239 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 240 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 241 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 242 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 243 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 244 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 245 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 246 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 247 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 248 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 249 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 250 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 251 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 252 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 253 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 254 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 255 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 256 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 257 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 258 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 259 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 260 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 261 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 262 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 263 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 264 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 265 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 266 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 267 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 268 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 269 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 270 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 271 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 272 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 273 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 274 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 275 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 276 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 277 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 278 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 279 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 280 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 281 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 282 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 283 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 284 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 285 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 286 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 287 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 288 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 289 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 290 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 291 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 292 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 293 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 294 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 295 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 296 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 297 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 298 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 299 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 300 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 301 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 302 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 303 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 304 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 305 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 306 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 307 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 308 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 309 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 310 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 311 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 312 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 313 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 314 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 315 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 316 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 317 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 318 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 319 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 320 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 321 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 322 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 323 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 324 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 325 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 326 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 327 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 328 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 329 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 330 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 331 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 332 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 333 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 334 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 335 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 336 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 337 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 338 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 339 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 340 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 341 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 342 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 343 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 344 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 345 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 346 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 347 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 348 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 349 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 350 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 351 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 352 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 353 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 354 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 355 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 356 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 357 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 358 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 359 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 360 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 361 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 362 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 363 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 364 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 365 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 366 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 367 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 368 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 369 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 370 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 371 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 372 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 373 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 374 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 375 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 376 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 377 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 378 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 379 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 380 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 381 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 382 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 383 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 384 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 385 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 386 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 387 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 388 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 389 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 390 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 391 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 392 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 393 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 394 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 395 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 396 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 397 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 398 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 399 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 400 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 401 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 402 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 403 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 404 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 405 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 406 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 407 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 408 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 409 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 410 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 411 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 412 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 413 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 414 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 415 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 416 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 417 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 418 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 419 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 420 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 421 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 422 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 423 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 424 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 425 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 426 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 427 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 428 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 429 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 430 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 431 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 432 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 433 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 434 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 435 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 436 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 437 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 438 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 439 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 440 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 441 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 442 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 443 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 444 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 445 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 446 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 447 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 448 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 449 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 450 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 451 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 452 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 453 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 454 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 455 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 456 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 457 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 458 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 459 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 460 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 461 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 462 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 463 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 464 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 465 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 466 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 467 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 468 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 469 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 470 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 471 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 472 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 473 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 474 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 475 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 476 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 477 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 478 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 479 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 480 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 481 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 482 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 483 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 484 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 485 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 486 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 487 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 488 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 489 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 490 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 491 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 492 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 493 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 494 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 495 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 496 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 497 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 498 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 499 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 500 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 501 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 502 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 503 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 504 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 505 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 506 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 507 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 508 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 509 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 510 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 511 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 512 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 513 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 514 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 515 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 516 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 517 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 518 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 519 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 520 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 521 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 522 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 523 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 524 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 525 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 526 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 527 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 528 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 529 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 530 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 531 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 532 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 533 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 534 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 535 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 536 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 537 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 538 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 539 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 540 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 541 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 542 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 543 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 544 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 545 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 546 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 547 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 548 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 549 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 550 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 551 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 552 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 553 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 554 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 555 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 556 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 557 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 558 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 559 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 560 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 561 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 562 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 563 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 564 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 565 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 566 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 567 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 568 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 569 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 570 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 571 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 572 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 573 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 574 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 575 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 576 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 577 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 578 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 579 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 580 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 581 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 582 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 583 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 584 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 585 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 586 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 587 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 588 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 589 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 590 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 591 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 592 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 593 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 594 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 595 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 596 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 597 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 598 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 599 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 600 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 601 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 602 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 603 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
