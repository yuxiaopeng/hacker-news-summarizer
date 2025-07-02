# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-07-02.md)

*最后自动更新时间: 2025-07-02 17:50:15*
## 1. 利用 IKKO Activebuds “AI驱动” 耳机

**原文标题**: Exploiting the IKKO Activebuds "AI powered" earbuds

**原文链接**: [https://blog.mgdproductions.com/ikko-activebuds/](https://blog.mgdproductions.com/ikko-activebuds/)

作者在一段“无用科技”视频中看到了IKKO Activebuds，这是一款运行Android系统的“人工智能”耳机，于是对其进行了调查。发现该耳机启用了ADB，作者侧载了应用程序并检查了ChatGPT的集成。他们发现该设备使用存储的API密钥直接与OpenAI通信，这是一个重大的安全漏洞。

进一步分析显示，该耳机与包括中国服务器在内的多个域名通信，并存储了加密的API端点。通过在root设备上侧载配套应用，作者提取了OpenAI密钥。包括“愤怒的丹”和“恋爱中的丹”模式在内的系统提示也被曝光。

作者发现该耳机仅使用设备IMEI进行身份验证，将聊天记录记录到服务器，允许任何人访问他人的聊天记录。通过使用已知的IMEI伪造链接二维码，可以暴露用户的名字和姓氏。作者随后向IKKO报告了这些问题。

虽然IKKO暂时下架了他们的应用程序并发布了更新，为聊天记录访问添加了签名头，但仍然存在重大的漏洞。作者仍然可以将消息注入到其他用户的配套应用程序中，并链接未绑定的设备，从而泄露聊天记录和用户名。OpenAI密钥也仍然留在设备上。

后来的更新轮换了OpenAI密钥并实施了IMEI检查，之后才启用ChatGPT，同时还增加了一个代理API。然而，这个API只需要一个特定的User-Agent。作者最终因IKKO的回应不足而放弃，但邀请其他人继续推动更好的安全性。

---

## 2. 基因疗法恢复了聋哑患者的听力

**原文标题**: Gene therapy restored hearing in deaf patients

**原文链接**: [https://news.ki.se/gene-therapy-restored-hearing-in-deaf-patients](https://news.ki.se/gene-therapy-restored-hearing-in-deaf-patients)

基因疗法成功恢复OTOF基因突变引起的先天性耳聋患者听力

---

## 3. 不要使用“点击这里”作为链接文本 (2001)

**原文标题**: Don’t use “click here” as link text (2001)

**原文链接**: [https://www.w3.org/QA/Tips/noClickHere](https://www.w3.org/QA/Tips/noClickHere)

这篇来自2001年的W3C QA技巧反对使用“点击这里”作为链接文本，提倡使用更具描述性和意义的链接。其核心信息是，即使链接文本脱离上下文阅读，也应具有信息量，解释链接为用户提供的内容，而不是专注于与之交互的机制。

文章建议网站管理员避免在链接文本中使用通用短语和动词短语。它建议使用更直接和信息丰富的“获取Amaya！”来代替“点击这里下载Amaya”， 同样，文章建议使用更丰富的描述，如“告诉我更多关于Amaya的信息：W3C的免费编辑器/浏览器...”来代替“告诉我更多关于Amaya的信息”。

此建议背后的原因是并非所有用户都会点击，并且依赖“点击这里”之类的视觉提示可能无法访问。清晰、描述性的链接文本通过提供上下文和目的，提高了可用性、可访问性和整体用户体验。

文章还引用了其他资源，包括 W3C HTML Web 内容可访问性指南 1.0 技术和 Tim Berners-Lee 和 Jutta Degener 的文章，以进一步支持其关于有效超文本写作的论点。QA 技巧以 W3C 质量保证兴趣小组提供的信息性指导的形式呈现，而不是作为规范性技术规范。

---

## 4. 索尼的Mark Cerny与AMD合作开发了“RDNA 5的多个重要部分”

**原文标题**: Sony's Mark Cerny Has Worked on "Big Chunks of RDNA 5" with AMD

**原文链接**: [https://overclock3d.net/news/gpu-displays/sonys-mark-cerny-has-worked-on-big-chunks-of-rdna-5-with-amd/](https://overclock3d.net/news/gpu-displays/sonys-mark-cerny-has-worked-on-big-chunks-of-rdna-5-with-amd/)

据报道，PlayStation主机首席架构师索尼的Mark Cerny一直在与AMD合作开发其即将推出的RDNA 5 GPU架构的重要部分。这一消息来自AMD员工的LinkedIn个人资料更新，表明Cerny的参与程度远超他之前与AMD在RDNA 2（PS5）和RDNA 3（传闻中的PS5 Pro）上的合作。

文章强调，虽然细节很少，但Cerny参与RDNA 5暗示了索尼主机开发与AMD GPU路线图之间的强大协同作用。这种合作可能会影响AMD GPU技术的未来方向，尤其是在与游戏性能和主机架构相关的领域。据推测，这可能会进一步优化光线追踪、升级技术和功效等功能，这些功能对于PC游戏和主机性能至关重要。

文章还强调了索尼的潜在利益，索尼可以利用RDNA 5架构来开发未来的PlayStation主机，确保在游戏市场中具有竞争优势。虽然Cerny贡献的具体性质仍不清楚，但他的参与标志着索尼和AMD之间在塑造GPU技术未来方面持续且可能扩大的合作关系。

---

## 5. Double 正在逐步关闭

**原文标题**: Double Is Winding Down

**原文链接**: [https://double.finance/blog/wind_down](https://double.finance/blog/wind_down)

自动化投资组合平台Double因客户获取不足以维持运营而停止服务。公司将在未来几周内结束运营，最终运营日期为2025年7月31日。

请客户在2025年7月31日前提取现金或将资产转移至其他券商。Double将继续正常交易运营，包括自动交易、清算、重新平衡和税务亏损收割，直至2025年7月30日。客户可以手动禁用自动交易。

重要日期包括：

*   **2025年7月2日：**停止接受新账户或转入资金。
*   **2025年7月30日：**停止自动交易。
*   **2025年7月31日：**账户清算或资产转移截止日期。

2025年7月31日之后，Double网站的功能将受到限制，剩余账户可能需要通过Apex Clearing手动转移（如果事先联系，Double将承担ACATS费用）。

Double建议清算并提取现金，或发起ACATS转账至其他券商，并提到了Wealthfront、Frec、M1 Finance、Fidelity、Schwab、Robinhood和Public等选项。他们建议在选择新的券商时考虑投资组合构成。他们还鼓励直接在Apex Clearing创建账户以访问账户文件。

Double将其优化引擎Oracle开源，供有兴趣在Alpaca上设置自己的交易机器人的用户使用。

---

## 6. Azure API 漏洞和角色配置错误导致企业网络受损

**原文标题**: Azure API vulnerability and roles misconfiguration compromise corporate networks

**原文链接**: [https://www.token.security/blog/azures-role-roulette-how-over-privileged-roles-and-api-vulnerabilities-expose-enterprise-networks](https://www.token.security/blog/azures-role-roulette-how-over-privileged-roles-and-api-vulnerabilities-expose-enterprise-networks)

Token Security研究人员的这篇博文详细介绍了Azure基于角色的访问控制(RBAC)系统中的一个严重漏洞。该研究发现，几个内置Azure角色配置错误，授予的权限范围比其描述的更大，导致潜在的过度授权。具体而言，“托管应用程序读取者”角色以及其他九个角色包含“*/read”权限，实际上授予了对几乎所有Azure资源的读取权限，尽管其本意是用于更具体的服务相关功能。

这种过度宽泛的读取权限，通常与“读取者”角色相关联，可能被利用来访问敏感信息，包括自动化帐户中的凭据、部署脚本和Web应用程序。它还允许攻击者发现存储帐户和数据库中的敏感数据，通过检查角色分配和网络配置来计划攻击，并通过资源锁和备份存储库来识别关键资源。

此外，该研究还发现了一个与VPN共享密钥相关的Azure API漏洞。 通过“*/read”权限可以访问的“Get VirtualNetworkGatewaySharedKey”API调用允许攻击者泄露VPN密钥。 该博文解释说，这可能是因为它使用HTTP 'GET'方法而不是'POST'方法实现的。

总而言之，这些问题创建了一条危险的攻击链，权限有限的用户可以借此访问云和本地网络。该文章强调了仔细审查Azure角色分配的重要性，并鼓励组织注意这些由身份驱动的攻击载体，以减轻潜在风险。

---

## 7. 大型语言模型有多大？

**原文标题**: How large are large language models?

**原文链接**: [https://gist.github.com/rain-1/cf0419958250d15893d8873682492c3e](https://gist.github.com/rain-1/cf0419958250d15893d8873682492c3e)

本文记录了大型语言模型 (LLM) 尺寸的演变，重点关注 2019 年至 2025 年间为原始文本续写而设计的基座模型。它从 GPT 系列（GPT-2、GPT-3）开始，然后转向 Meta 的 Llama 系列，包括未发布的 Llama-4。Llama-3.1 (405B) 的发布是一个关键转折点，它是一个大型密集模型，随后是混合专家 (MoE) 模型的激增。

作者强调了一个时期，当时与 GPT-3 相当的可下载 LLM 非常稀缺，阻碍了使用较小模型复制其性能的努力。MoE 架构允许构建更大的模型，同时减少了激活参数的数量，彻底改变了这一局面，像 Mistral 的 Mixtral 系列这样的模型开始可用。

文章随后详细介绍了 2024 年末至 2025 年中发布的一些大型 MoE 模型，主要来自中国公司，包括 Deepseek V3 Base (671B)、Databricks (132B)、Minimax (456B)、Dots (143B)、Hunyuan (80B) 和 Ernie (424B)。这些模型通常包含多模态和多语言能力。

作者对“退火”趋势表示担忧，即在特定数据集（代码和数学）上微调模型以提高基准分数，这可能会使它们偏离纯文本续写。他们还质疑当前基准测试在多大程度上捕捉了 LLM 智能的细微差别，并强调了当前 AI 助手聊天机器人的趋势，敦促探索原始文本续写引擎的替代应用。作者还担心预训练中包含的最新数据会导致模型更像“助手”而不是“基座模型”。

---

## 8. 列表是一个Monad

**原文标题**: A List Is a Monad

**原文链接**: [https://alexyorke.github.io//2025/06/29/a-list-is-a-monad/](https://alexyorke.github.io//2025/06/29/a-list-is-a-monad/)

本文介绍了 Monad，将其作为函数式编程中一种强大的模式，并解释为处理控制流的计算上下文。 Monad 有两种类型：“结果”（Results），表示已经计算好的值，并带有额外的上下文（如 `List<T>` 或 `Maybe<T>`）；以及“配方”（Recipes），表示延迟计算（如 `Task<T>`）。

本文重点介绍“结果” Monad，并使用 `List` 和 `Maybe` 作为示例。 Monad 需要 `Unit` （用于包装一个值）和 `flatMap` （用于链接操作，同时避免嵌套容器）操作。 `Map` 将一个函数应用于 Monad 中的每个值，而 `flatMap` 也会展平结果。

作者强调，Monad 不仅仅是花哨的容器；它们的真正力量在于抽象控制流。 通过将“如何做”委托给 Monad，业务逻辑保持声明式和可组合。 使用 `Maybe` 演示了 Monad 如何处理潜在的值缺失，从而避免了显式的空值检查。 文章认为，通过 `flatMap` 链接 Monad 的能力是关键。

最后，本文介绍了 Monad 的三个定律（左单位元律、右单位元律和结合律），以确保操作链中的可预测行为。 这些定律是数学保证，允许 Monad 可靠地组合。

---

## 9. 官员抨击后，ICEBlock 登上 App Store 排行榜榜首

**原文标题**: ICEBlock climbs to the top of the App Store charts after officials slam it

**原文链接**: [https://www.engadget.com/social-media/iceblock-climbs-to-the-top-of-the-app-store-charts-after-officials-slam-it-004319963.html](https://www.engadget.com/social-media/iceblock-climbs-to-the-top-of-the-app-store-charts-after-officials-slam-it-004319963.html)

ICEBlock应用爆红：追踪ICE特工行踪，引发争议

ICEBlock这款应用允许用户报告和追踪ICE（移民及海关执法局）特工的行踪，因美国政府官员的谴责和CNN的报道而人气飙升，登顶App Store排行榜。该应用由Joshua Aaron开发，旨在回应特朗普政府的移民政策，用户可以在地图上标记ICE特工的位置，并分享服装和车辆等细节，从而向五英里范围内的用户发出警报。

在CNN报道突出了该应用的功能和最初2万名用户的用户群（主要在洛杉矶）之后，该应用迅速走红。然而，白宫和ICE官员批评该应用，声称它危害了执法人员并助长了犯罪活动。新闻秘书Karoline Leavitt声称CNN的报道煽动了针对ICE特工的暴力行为，而ICE代理局长Todd M. Lyons指责CNN进行了鲁莽的新闻报道。

美国国土安全部部长Kristi Noem和美国司法部长Pam Bondi表示，政府正在调查Aaron，暗示他的行为可能被视为对执法的威胁，并不受言论自由保护。Aaron则坚称ICEBlock不收集个人数据，并且仅在iOS系统上可用，以保护用户隐私。

---

## 10. 华为发布基于华为昇腾GPU训练的开源权重模型

**原文标题**: Huawei releases an open weight model trained on Huawei Ascend GPUs

**原文链接**: [https://arxiv.org/abs/2505.21411](https://arxiv.org/abs/2505.21411)

本篇arXiv文章（arXiv:2505.21411）介绍了“盘古Pro MoE”，一种由华为及其他贡献者开发的混合分组专家（MoGE）模型。该模型旨在解决传统MoE架构中专家工作负载分布不平衡的问题，从而提高稀疏大型语言模型的效率。

盘古Pro MoE在token选择过程中对专家进行分组，确保模型分布式部署时设备间计算负载更加平衡。这种架构旨在提高吞吐量，尤其是在推理过程中。

该模型基于MoGE，拥有720亿总参数，每个token激活160亿参数，并针对华为昇腾NPU（昇腾300I Duo和800I A2）进行了优化。实验表明，MoGE在这些NPU上进行训练和推理时，实现了更好的专家负载均衡和更高效的执行。

盘古Pro MoE的推理性能达到每卡1148 tokens/s，通过推测加速可以进一步提高到每卡1528 tokens/s。这优于可比的32B和72B稠密模型。该研究还强调了在昇腾300I Duo上进行模型推理的出色性价比。作者声称，昇腾NPU使盘古Pro MoE在参数小于100B的级别内超越了像GLM-Z1-32B和Qwen3-32B等著名的开源模型。因此，华为发布了在华为昇腾GPU上训练的开放权重模型。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 2 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 3 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 4 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 5 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 6 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 7 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 8 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 9 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 10 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 11 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 12 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 13 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 14 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 15 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 16 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 17 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 18 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 19 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 20 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 21 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 22 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 23 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 24 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 25 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 26 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 27 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 28 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 29 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 30 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 31 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 32 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 33 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 34 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 35 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 36 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 37 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 38 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 39 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 40 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 41 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 42 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 43 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 44 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 45 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 46 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 47 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 48 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 49 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 50 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 51 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 52 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 53 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 54 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 55 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 56 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 57 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 58 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 59 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 60 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 61 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 62 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 63 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 64 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 65 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 66 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 67 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 68 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 69 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 70 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 71 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 72 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 73 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 74 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 75 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 76 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 77 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 78 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 79 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 80 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 81 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 82 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 83 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 84 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 85 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 86 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 87 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 88 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 89 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 90 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 91 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 92 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 93 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 94 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 95 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 96 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 97 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 98 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 99 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 100 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 101 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 102 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 103 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 104 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 105 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
