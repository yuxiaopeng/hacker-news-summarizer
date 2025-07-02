# Hacker News 热门文章摘要 (2025-07-02)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. 私营部门失业3.3万，远低于预期增长10万。

**原文标题**: Private sector lost 33k jobs, badly missing expectations of 100k increase

**原文链接**: [https://www.cnbc.com/2025/07/02/adp-jobs-report-june-2025.html](https://www.cnbc.com/2025/07/02/adp-jobs-report-june-2025.html)

2025年6月ADP报告显示，私营部门就业意外萎缩，减少3.3万个职位，远低于经济学家预期的新增10万个职位。这是自2023年3月以来的首次下降，可能预示着经济状况不如投资者认为的强劲。

最大的职位损失出现在服务业，尤其是在专业/商业服务和健康/教育领域。相反，商品生产职位有所增加。从地域上看，美国中西部和西部地区的就业岗位降幅最大，而南部是唯一实现净工资增长的地区。小型企业也比大型企业损失了更多的就业岗位。

尽管ADP报告在预测官方政府就业报告方面的准确性值得怀疑，但市场正在关注周四的非农就业报告，预计将增加11万个职位，失业率可能上升至4.3%。每周失业救济申请数据也将在周四公布。在职者和跳槽者的年度收入增长均略有下降。

---

## 12. 美联储称这是一个价值一百万美元的立方体，他们差了五十万美元。

**原文标题**: The Fed says this is a cube of $1M. They're off by half a million

**原文链接**: [https://calvin.sh/blog/fed-lie/](https://calvin.sh/blog/fed-lie/)

本文以幽默的方式调查了芝加哥联邦储备银行货币博物馆的展品，一个据称装有100万美元1美元纸币的大型透明立方体。作者对这一说法持怀疑态度，试图数清纸币堆叠的数量以验证金额。

由于手动计数困难，作者创建了一个名为“Dot Counter”的Web应用程序，以帮助计数图像中的项目。利用这个工具，他们分析了一张立方体的照片，估计其中包含约1,550,400美元，比声称的金额多出惊人的550,400美元。

作者随后探讨了造成差异的几种可能性，包括通货膨胀导致未来超额金额的合理性、内部大部分是空气的空心立方体，或者仅仅是计算错误。他们甚至考虑了考虑到美元纸币的非立方体友好尺寸，美联储如何构建一个更精确的100万美元的立方体。

最终，作者得出结论，该立方体可能包含155万美元，强调了验证信息和质疑假设的重要性，即使这些假设是由官方机构提出的。作者随后分享了他们新的“Dot Counter”工具，邀请读者使用它进行自己的计数工作。

---

## 13. Cloudflare 推出默认屏蔽 A.I. 数据抓取器

**原文标题**: Cloudflare Introduces Default Blocking of A.I. Data Scrapers

**原文链接**: [https://www.nytimes.com/2025/07/01/technology/cloudflare-ai-data.html](https://www.nytimes.com/2025/07/01/technology/cloudflare-ai-data.html)

无法访问文章链接。

---

## 14. 停止扼杀游戏

**原文标题**: Stop Killing Games

**原文链接**: [https://www.stopkillinggames.com/](https://www.stopkillinggames.com/)

文章《停止扼杀游戏》可能论证反对游戏公司关闭旧游戏服务器和在线服务的行为，导致游戏无法游玩或大幅缩水。

其核心抱怨在于，一旦游戏失去在线功能，无论其是否仍提供单人游戏内容，实际上都变得“死亡”。这种做法通常会移除已购买内容的访问权限，消除驱动玩家参与的社交元素，并最终贬低游戏的价值。

文章可能会讨论公司关闭游戏的原因，例如玩家数量少、维护成本或许可问题。它可能认为这些理由通常不足以完全取消人们为之付费和享受过的游戏的访问权限。

文章也可能探讨让玩家继续享受这些游戏的替代方案，例如：

*   **开源服务器代码：** 允许社区独立维护服务器。
*   **创建在线功能的离线版本：** 在不需要活跃服务器的情况下保留游戏元素。
*   **将游戏授权或出售给其他开发者：** 这可以为旧游戏注入新的活力。
*   **提供合理的提前通知：** 允许玩家为关闭做好准备，并可能存档他们的数据。

最终，《停止扼杀游戏》可能主张更加尊重视频游戏的保存和玩家的投入。它认为公司有责任寻找解决方案，让玩家在游戏最初的受欢迎程度下降后，仍然可以继续享受他们喜爱的游戏。文章可能将目前关闭游戏的做法视为反消费者行为，并对游戏历史构成威胁。

---

## 15. ICEBlock：匿名举报移民执法机构（ICE）目击事件的应用

**原文标题**: ICEBlock, an app for anonymously reporting ICE sightings

**原文链接**: [https://techcrunch.com/2025/07/01/iceblock-an-app-for-anonymously-reporting-ice-sightings-goes-viral-overnight-after-bondi-criticism/](https://techcrunch.com/2025/07/01/iceblock-an-app-for-anonymously-reporting-ice-sightings-goes-viral-overnight-after-bondi-criticism/)

以下是该文章的简明摘要：

允许用户匿名举报移民及海关执法局 (ICE) 特工出现的 iPhone 应用程序 ICEBlock 的受欢迎程度激增，成为美国下载量最高的免费 iPhone 应用程序之一。 这一激增归因于美国司法部长帕姆·邦迪的批评， 这无意中引起了人们对该应用程序的更多关注。

ICEBlock 使 用 户能够分享其位置 5 英里范围内 ICE 目击事件的信息，并在附近发现 ICE 特工时发送通知。 该应用程序在洛杉矶获得了庞大的用户群，那里 ICE 的突袭行动很频繁。 重要的是，该应用程序优先考虑用户隐私，不收集或存储任何用户数据，TechCrunch 对其网络流量的分析证实了这一点。

---

## 16. 六边形模糊：高通基带全系统模拟模糊测试

**原文标题**: Hexagon fuzz: Full-system emulated fuzzing of Qualcomm basebands

**原文链接**: [https://www.srlabs.de/blog-post/hexagon-fuzz-full-system-emulated-fuzzing-of-qualcomm-basebands](https://www.srlabs.de/blog-post/hexagon-fuzz-full-system-emulated-fuzzing-of-qualcomm-basebands)

本文讨论了“Hexagon fuzz”，一种为高通Hexagon基带全系统仿真模糊测试而开发的新型开源工具链。高通Hexagon基带广泛应用于智能手机，但由于其专有架构，缺乏强大的安全工具。

作者强调了现有基带安全研究的差距，因为FirmWire等工具不支持Hexagon的定制CPU架构和操作系统。为了解决这个问题，他们从高通创新中心（QuIC）fork了一个带有Hexagon全系统仿真支持的QEMU版本，并将其与LibAFL的QEMU fork集成，创建了一个定制的模糊测试器。

该工具链允许用户仿真Hexagon基带固件，添加断点，通过Rust钩子修改运行时行为，跳过初始化函数，检测函数以进行调试，并执行覆盖引导的模糊测试。他们开发了一个可视化覆盖脚本，该脚本解析QEMU调试日志并在Ghidra中为程序计数器着色，从而有助于逆向工程工作。

当前的实现成功启动了iPhone基带固件，检测了控制流，并提供了基本的模糊测试基础设施。未来的计划包括更好的目标函数识别、解压缩支持、增强的模糊测试框架以及与动态测试接口的集成。该工具链旨在提高基于Hexagon设备的透明度和安全态势，相关资源可在GitHub上找到。

---

## 17. Recurse Center (YC S10) 招聘职业辅导员

**原文标题**: Recurse Center (YC S10) Is Hiring a Career Facilitator

**原文链接**: [https://recurse.notion.site/Career-Facilitator-22300db231b580ba9190df9d5e480080](https://recurse.notion.site/Career-Facilitator-22300db231b580ba9190df9d5e480080)

本文宣布面向程序员的自主学习教育机构Recurse Center (YC S10) 正在招聘一名职业发展协调员。该职位的主要职责似乎是帮助Recursers (参与者) 在Recurse Center期间或之后实现其职业目标。

主要职责可能包括：

*   **职业指导/辅导：** 为Recursers提供个性化的支持和指导，帮助他们进行求职、职业规划和职业发展。
*   **资源开发：** 创建和维护资源，例如指南、模板和社交机会，以帮助Recursers的职业发展。
*   **社群建设：** 营造一个支持性和协作性的环境，让Recursers可以分享经验、互相学习并建立联系。
*   **联系雇主：** 潜在地与对招聘Recurse Center校友感兴趣的公司建立并维持关系。

该文章可能希望招聘具有职业指导、技术招聘或相关领域经验，并且热衷于帮助程序员提升职业发展的候选人。它隐式地强调了Recurse Center不仅致力于提供独特的学习环境，而且支持Recursers实现其职业理想。

---

## 18. 火狐浏览器120到141版本网络基准测试

**原文标题**: Firefox 120 to Firefox 141 Web Browser Benchmarks

**原文链接**: [https://www.phoronix.com/review/firefox-benchmarks-120-141](https://www.phoronix.com/review/firefox-benchmarks-120-141)

本文对Mozilla Firefox网页浏览器从120版（2023年11月）到最新的141 Beta版（2025年7月初）的性能进行了分析。作者Michael Larabel在同一台搭载AMD Ryzen 9 9950X处理器的Ubuntu 25.04 Linux系统上对每个主要的Firefox版本进行了基准测试。

测试的动机源于近期Firefox 141 Beta版内存使用量降低的发现。Larabel扩大了范围，涵盖了所有追溯到Firefox 120的主要版本，选择120版是因为更早的版本在Selenium/Gecko Web驱动程序自动化方面遇到了问题。这使得可以在大约两年内跟踪Firefox在Linux上的性能轨迹。

测试方法包括对每个主要Firefox版本的发布版本进行基准测试，其中使用Firefox 125.0.1代替了有故障的125.0版本。除了各种网页浏览器测试的性能基准外，还监测了内存使用情况。本文分为五页，此介绍页为接下来的基准测试结果奠定了基础。

---

## 19. 我正在减少大型语言模型的使用。

**原文标题**: I'm dialing back my LLM usage

**原文链接**: [https://zed.dev/blog/dialing-back-my-llm-usage-with-alberto-fortin](https://zed.dev/blog/dialing-back-my-llm-usage-with-alberto-fortin)

经验丰富的软件工程师阿尔贝托·福廷分享了他在最初热情拥抱大型语言模型后，如何逐渐减少对它们在软件开发中的依赖。尽管大型语言模型在初始功能和自动补全方面展现出潜力，但阿尔贝托发现它们常常生成低质量代码，在修复旧错误的同时引入新错误，并且在使用Go和ClickHouse重建其基础设施时最终阻碍了生产力。

他意识到最初的兴奋创造了一种“生产力幻觉”，导致了对大型语言模型能力的不切实际的期望。阿尔贝托强调了一个关键的“思维转变”——将大型语言模型视为助手，而不是架构师或高级工程师。他重新掌控了局面，将大型语言模型的使用重点放在较小的任务上，如重构或小范围的功能，同时亲自处理更重要的问题并保持整体架构愿景。

阿尔贝托强调了现实期望的重要性，并鼓励其他高级开发人员信任他们现有的技能。他建议使用人工智能来利用现有知识，但警告不要完全依赖，强调架构抽象和产品决策仍然需要人类专业知识。最终，阿尔贝托提倡一种平衡的方法，承认人工智能的潜力，但也认识到该技术仍在发展中，需要谨慎地融入现有工作流程。

---

## 20. Show HN: 高清玻璃效果CSS生成器

**原文标题**: Show HN: CSS generator for a high-def glass effect

**原文链接**: [https://glass3d.dev/](https://glass3d.dev/)

此“Show HN”帖子介绍了一个名为“Glass3D generator”的 CSS 生成器，该生成器允许用户创建用于高清玻璃效果的 CSS 代码。该帖子本质上是对该工具的展示，表明这是作者创建并与 Hacker News 社区分享的内容（“Show HN”表明作者希望获得反馈并展示他们的作品）。核心价值在于简化了 CSS 中视觉上吸引人的玻璃效果的创建，与手动编写 CSS 代码相比，可能节省了开发人员的时间和精力。在这个有限的摘要中没有提供关于生成器特性或功能的更多细节，因此用户需要探索该生成器以了解其具体功能和自定义选项。

---

## 21. 贵格会的禅 (2016)

**原文标题**: The Zen of Quakerism (2016)

**原文链接**: [https://www.friendsjournal.org/the-zen-of-quakerism/](https://www.friendsjournal.org/the-zen-of-quakerism/)

唐纳德·阿卜杜拉是一位有15年禅修经验的禅宗修行者，他致信Friend YouTube频道，赞扬彼得对禅宗佛教与贵格会之间异同的讨论。受最近发现物理学家亚瑟·斯坦利·爱丁顿爵士和乔治·埃利斯是贵格会教徒的启发，阿卜杜拉（拥有放射肿瘤学科学背景和朋友大学信息系统硕士学位）询问，即使他自己不是贵格会教徒，是否可以向《朋友杂志》投稿。他提议撰写一篇关于贵格会群体中著名科学家的文章，特别是如果这个话题还没有被广泛报道的话。他引用了爱丁顿参与贵格会教师协会以及他在斯沃斯莫尔学院发表的关于“科学与看不见的世界”的演讲，以及埃利斯与斯蒂芬·霍金的合著和参与贵格会服务基金，作为科学界杰出贵格会教徒的例子。本质上，他是在寻求许可，向《朋友杂志》投稿一篇强调科学与贵格会交叉点的文章。

---

## 22. 拟议首次公开募股的Figma文件

**原文标题**: Figma files for proposed IPO

**原文链接**: [https://www.figma.com/blog/s1-public/](https://www.figma.com/blog/s1-public/)

Figma 宣布已向美国证券交易委员会 (SEC) 公开提交 S-1 表格注册声明，拟首次公开募股 (IPO) 其 A 类普通股，并计划在纽约证券交易所上市，股票代码为“FIG”。本次发行股票的数量和价格范围尚未确定，发行取决于市场情况。

文章重点介绍了管理本次发行的金融机构团队，包括摩根士丹利、高盛集团有限责任公司、艾伦公司有限责任公司和摩根大通，它们将担任联席主承销商。文章还提供了从这些公司获取初步招股说明书的联系方式。

文章强调，本次发行仅通过招股说明书进行，且注册声明尚未生效。因此，在声明生效前，不允许进行任何销售或购买要约。

文章随后简要介绍了 Figma，将其描述为一个协作式的、人工智能驱动的平台，该平台已从设计工具发展为促进整个设计和产品开发流程。文章还提供了媒体和投资者关系的联系方式。

文章还提到此前于四月份向美国证券交易委员会秘密提交的 S-1 表格草案，并链接到涵盖人工智能集成、设计相关讨论和产品更新等相关文章。

---

## 23. 概念验证型神经脑植入体，可提供语音

**原文标题**: A proof-of-concept neural brain implant providing speech

**原文链接**: [https://arstechnica.com/science/2025/06/a-neural-brain-implant-provides-near-instantaneous-speech/](https://arstechnica.com/science/2025/06/a-neural-brain-implant-provides-near-instantaneous-speech/)

加州大学戴维斯分校开发出神经脑植入概念验证，旨在将脑信号直接转化为瘫痪人士的语音。与先前专注于文本翻译、存在显著延迟和词汇量有限的脑机接口 (BCI) 不同，这种新型假体旨在通过将脑信号实时翻译成音素和单词，创建一个“完全数字化的声道”。

在 Maitreyee Wairagkar 的带领下，该团队将 256 个微电极植入一位 46 岁的 ALS 患者 (T15) 的腹侧前中央回，使系统能够提取语音特征，如音高和发声。然后将这些特征输入到声码器中，以合成类似于 T15 原始声音的语音。该系统拥有大约 10 毫秒的低延迟，可将脑信号瞬间转换为声音。

虽然该系统在句子匹配测试中实现了 100% 的可懂度，但在开放式转录测试中的词错率达到了 43.75%，表明它尚未可靠到可以用于日常对话。尽管存在局限性，但这项技术代表着向前迈出的重要一步，使患者能够表达诸如语调之类的细微差别，并使用预定义词典之外的单词。研究人员认为，增加电极数量（如 Paradromics 等公司计划的那样）可以显著提高性能。在加州大学戴维斯分校，已经计划使用 1600 电极系统进行临床试验。

---

## 24. Fakespot在检测虚假产品评论9年后于今日关闭。

**原文标题**: Fakespot shuts down today after 9 years of detecting fake product reviews

**原文链接**: [https://blog.truestar.pro/fakespot-shuts-down/](https://blog.truestar.pro/fakespot-shuts-down/)

Fakespot于2025年7月1日关闭，此前已运营九年，是一款用于检测虚假在线评论的流行工具。Fakespot由Saoud Khalifah于2016年创立，利用人工智能分析亚马逊、eBay和沃尔玛等平台上的评论，识别表明反馈不可靠或捏造的模式。研究表明，很大一部分产品评论，尤其是在服装和珠宝等类别中，都不可靠。

该公司筹集了700万美元的资金，并于2023年被Mozilla收购。Mozilla将Fakespot的技术整合到Firefox中，作为“Mozilla Review Checker”，为用户提供了一种验证产品评论的简便方法。然而，在2025年5月，Mozilla宣布由于可持续性挑战，将停止Fakespot和Pocket，并将资源重新导向核心Firefox功能和人工智能驱动的创新。

此次关闭给那些依靠Fakespot做出明智购买决定的用户留下了一个空白。这篇文章强调了对可信赖的评论分析的持续需求，并介绍了TrueStar，这是一种旨在成为Fakespot“精神继承者”的新工具，它使用了现代人工智能和可持续的经济模式。作者告别了Fakespot，承认它在打击欺诈和促进在线购物真实性方面的作用。

---

## 25. 聊天机器人流程编辑器 – 可视化会话流程设计工具

**原文标题**: Chatbot Flow Editor – Visual tool for designing conversation flows

**原文链接**: [https://github.com/enumura1/chatbot-flow-editor](https://github.com/enumura1/chatbot-flow-editor)

聊天机器人流程编辑器是一个基于浏览器的可视化工具，用于设计聊天机器人对话流程。它允许用户创建、测试和导出流程为JSON格式，从而简化聊天机器人开发。该编辑器可以使用 `npm install --save-dev @enumura/chatbot-flow-editor` 作为开发依赖项安装，并使用 `npx @enumura/chatbot-flow-editor` 启动。

用户可以创建对话节点，编辑其内容和选项，并通过聊天预览模拟用户交互。流程导出为JSON文件，定义对话节点和选项。JSON结构由带有ID、标题和选项的节点组成，这些选项通过 `nextId` 链接到其他节点。

集成涉及将导出的JSON加载到您的聊天机器人应用程序中，并使用它来驱动对话逻辑。代码示例演示了使用流程数据的基本导航。

该工具支持创建节点、编辑内容、测试流程和导出/导入JSON。概述了开发工作流程，详细说明了设计、测试、导出和集成阶段。该编辑器需要Node.js 20.0.0或更高版本，并根据MIT许可证授权。提供入门指南、用户手册和理解JSON结构的文档。

---

## 26. 我收集益智药评级的心得

**原文标题**: What I learned gathering nootropic ratings

**原文链接**: [https://troof.blog/posts/nootropics/](https://troof.blog/posts/nootropics/)

本文分析了从推荐系统和SlateStarCodex聪明药调查中收集的聪明药评分，总计来自2802人的36163个评分。文章强调，个人对聪明药的体验差异很大。使用的评分范围从0（无用）到10（改变生活）。

作者承认数据存在偏差，包括缺乏随机分配、自我报告以及缺乏控制/双盲，并在这些问题存在的情况下，侧重于比较各种聪明药。分析包括平均评分、产生积极效果的概率以及各种聪明药产生改变生活效果的概率。

文章还调查了与聪明药相关的风险，特别是成瘾性、耐受性和副作用，同时承认由于非回应偏差，这些估计存在不确定性。

主要发现包括：

*   **生活方式的改变是有效的聪明药：** 睡眠和运动，特别是举重，即使与处方药相比，也获得了很高的评价。
*   **饮食可能是有益的：** 原始饮食似乎很有前景。
*   **常见的聪明药可能不是最好的：** 许多流行的聪明药，如吡拉西坦、南非醉茄和人参，与不太常见的物质和生活方式干预相比，获得的评分相对较低。
*   **强效聪明药可能值得一试：** 作者建议探索更强效的选择，以获得潜在的改变生活的效果。

---

## 27. IntyBASIC：Intellivision平台的Basic编译器

**原文标题**: IntyBASIC: A Basic Compiler for Intellivision

**原文链接**: [https://nanochess.org/intybasic.html](https://nanochess.org/intybasic.html)

IntyBASIC 是一种 BASIC 编译器，旨在让程序员能够为 Intellivision 家庭视频游戏机创建游戏和应用程序。 它由 Oscar Toledo G. 开发，旨在克服为 Intellivision 发布的原始 BASIC 解释器的局限性，后者存在性能缓慢和功能有限的问题。

该编译器的工作原理是将 BASIC 代码翻译成 General Instrument AY-3-8900 CPU 的本地汇编语言，这是 Intellivision 的核心处理器。 这种编译过程显着提高了 BASIC 程序的执行速度，使其适合创建更复杂、响应更快的游戏。

IntyBASIC 提供了一套全面的命令和函数，涵盖图形处理（包括精灵处理）、音效、输入处理（键盘、控制器）和内存管理。 它支持各种 Intellivision 特定的硬件功能，为程序员提供对游戏机功能的低级控制。

该编译器包含一个 IDE（集成开发环境）或可以与命令行工具一起使用，从而相对容易地编写、编译和测试 IntyBASIC 程序。 然后，可以将生成的已编译代码加载到 Intellivision 游戏机上或在模拟器中运行。

本质上，IntyBASIC 为 Intellivision 开发人员提供了一种现代而强大的工具，使他们能够为这款经典游戏机创建比以前使用原始 BASIC 解释器更复杂、性能更高的软件。 它融合了 BASIC 的易用性以及编译代码的性能优势。

---

## 28. 希尔伯特第六问题：通过玻尔兹曼理论推导流体方程

**原文标题**: Hilbert's sixth problem: derivation of fluid equations via Boltzmann's theory

**原文链接**: [https://arxiv.org/abs/2503.01800](https://arxiv.org/abs/2503.01800)

这篇由余登、Zaher Hani和肖马于2025年3月3日提交的arXiv文章，探讨了希尔伯特第六问题，即从基本物理推导流体方程。该论文题为“希尔伯特第六问题：通过玻尔兹曼动理学理论推导流体方程”，声称严格推导了流体力学的基本偏微分方程（PDE），特别是可压缩欧拉方程和不可压缩纳维-斯托克斯-傅里叶方程。推导始于一个经历弹性碰撞的硬球粒子系统。作者首先推导出二维和三维环上的玻尔兹曼方程，这是基于他们之前的研究成果(arXiv:2408.07818)。该论文共48页，包含5个图。它被归类为偏微分方程分析(math.AP)和数学物理(math-ph)，并使用了MSC分类35Q20、76P05和82C40。其中指出该文章与作者早期发表的文章arXiv:2408.07818存在文本重叠。该论文可引用为arXiv:2503.01800 [math.AP]。

---

## 29. 内容独立日：未经补偿，禁止AI抓取

**原文标题**: Content Independence Day: no AI crawl without compensation

**原文链接**: [https://blog.cloudflare.com/content-independence-day-no-ai-crawl-without-compensation/](https://blog.cloudflare.com/content-independence-day-no-ai-crawl-without-compensation/)

马修·普林斯在“内容独立日”中指出，传统的网络商业模式，即内容创作者通过允许搜索引擎复制其内容来换取流量的补偿方式，在人工智能时代已不再可行。随着人工智能系统越来越多地直接回答问题，绕过了用户访问原始来源的需求，内容创作者正面临流量的急剧下降，进而导致广告和订阅收入的减少。

普林斯强调了传统谷歌搜索与像 OpenAI 和 Anthropic 这样的新型人工智能工具在流量生成方面的巨大差异，表明了创作者流量潜力的巨大降低。他认为，人工智能爬虫正在“ stripmining”网络，消耗内容而没有充分补偿创作者。

作为解决方案，Cloudflare 与出版商和人工智能公司一起，宣布 7 月 1 日为“内容独立日”，并将默认阻止人工智能爬虫，除非它们为所使用的内容付费。此外，Cloudflare 旨在创建一个市场，内容创作者和人工智能公司可以在此协商公平的补偿。该市场将根据内容的独特性和对人工智能知识的贡献来评估内容价值，而不是仅仅基于产生的流量。目标是激励高价值内容的创作，并建立一个可持续的生态系统，让创作者因其工作而获得公平的回报，从而为人工智能时代一个更好、更公平的网络铺平道路。

---

## 30. 萨姆·奥特曼抨击Meta挖AI人才：“有使命感的人会胜过雇佣兵”

**原文标题**: Sam Altman Slams Meta’s AI Talent Poaching: 'Missionaries Will Beat Mercenaries'

**原文链接**: [https://www.wired.com/story/sam-altman-meta-ai-talent-poaching-spree-leaked-messages/](https://www.wired.com/story/sam-altman-meta-ai-talent-poaching-spree-leaked-messages/)

OpenAI CEO奥特曼回应Meta高薪挖角AI人才，尤其针对由Alexandr Wang和Nat Friedman领导的Meta新超级智能团队。奥特曼在给OpenAI研究人员的信息中，淡化了人员流失的影响，暗示Meta不得不向下挖掘人才，并称其招聘策略“令人厌恶”。

他强调OpenAI以负责任地构建通用人工智能(AGI)为中心，拥有卓越的、使命驱动的文化，并将其与Meta可能存在的、受短期利益驱动和注意力分散的问题文化形成对比。奥特曼用“传教士”与“雇佣兵”的比喻，暗示OpenAI对AGI的奉献最终将获胜。

奥特曼还强调了OpenAI对员工薪酬的承诺，暗示可能进行改进，并强调OpenAI股票相比Meta的长期上涨潜力更大。他重申了对OpenAI研究路线图、计算资源和独特团队文化的信心，并声称OpenAI对AGI的关注使其与像Meta这样可能转移优先事项的公司区分开来。

在奥特曼发布信息后，几位OpenAI高层员工在Slack上呼应了他的观点，强化了OpenAI独特且具有创新性的文化使其成为比Meta更好的工作场所的理念。他们强调Meta容易改变焦点是一个关键区别，他们更喜欢OpenAI对AGI的坚定承诺。

---

## 31. 他们试过美国制造——但对他们的顾客来说太贵了。

**原文标题**: They tried Made in the USA – it was too expensive for their customers

**原文链接**: [https://www.reuters.com/business/they-tried-made-usa-it-was-too-expensive-their-customers-2025-07-02/](https://www.reuters.com/business/they-tried-made-usa-it-was-too-expensive-their-customers-2025-07-02/)

无法访问文章链接。

---

## 32. 燕子为何飞往韩国非军事区？

**原文标题**: Why Do Swallows Fly to the Korean DMZ?

**原文链接**: [https://www.sapiens.org/culture/korean-dmz-estuary-politics-war-borders-diaspora/](https://www.sapiens.org/culture/korean-dmz-estuary-politics-war-borders-diaspora/)

金艺珠的文章《燕子为何飞往韩国非军事区？》通过个人联系、流离失所和家燕（jebi）的象征意义，探讨了韩国非军事区（DMZ）。 金是第三代失乡民，她讲述了自己为纪念朝鲜战争停战70周年而前往非军事区的旅程。

每年在韩国和南方气候之间迁徙的家燕，对于在非军事区附近重新定居的失乡民，尤其是在江华郡的失乡民来说，是希望和回归的辛酸象征。 这些居民为燕子筑巢，将它们视为提醒人们有可能重返北方家园的希望，而他们自己却被剥夺了这种自由。

文章强调了汉江河口的悖论，它是非军事区内的“中立”地带，平民曾经可以自由地过境和联系。 尽管有此指定，但重度军事化和监视已将其转变为危险的空间，只有鸟类才能进入。

金的个人叙述与分裂和渴望的更广泛主题交织在一起。 与叔叔的一次公路旅行，他的祖籍就位于边境对面，揭示了水泥般的分裂所造成的深刻情感影响。 尽管痛苦，一种类似于家燕的“归巢本能”将他们拉回河口，突显了与分裂土地的持久联系以及持续不断的跨界联系的寻找。 这篇文章强调了非军事区的复杂现实，它既是无法逾越的边界，又是潜在的团聚场所，而燕子的自由飞翔象征着这一点。

---

## 33. 罗马军团士兵营地发现士兵腕包

**原文标题**: Soldier’s wrist purse discovered at Roman legionary camp

**原文链接**: [https://www.heritagedaily.com/2025/06/soldiers-wrist-purse-discovered-at-roman-legionary-camp/155513](https://www.heritagedaily.com/2025/06/soldiers-wrist-purse-discovered-at-roman-legionary-camp/155513)

考古学家在捷克共和国南摩拉维亚一处罗马临时营地遗址中发现了一件罗马士兵腕部钱袋残片。该营地在公元172至180年马科曼尼战争期间曾被第十军团使用。

这一发现意义重大，因为它位于罗马帝国传统疆界之外。这个钱袋，被描述为一个小型“钱箱”，被设计佩戴在左臂上，以便解放右手进行战斗。

虽然钱袋内没有发现硬币，但在附近发现了大量罗马硬币。专家估计，该钱袋可以容纳大约50枚银币德纳里乌斯，接近一名罗马军团士兵的年薪。这个青铜钱袋可能装有士兵的个人资金和用于行动费用的“勤务现金”。它突显了罗马军事行动的后勤复杂性，并提供了对帝国边境士兵生活的见解。

钱袋残片、重建模型和相关硬币正在帕索赫拉夫基的穆绍夫游客中心展出。

---

## 34. 微软将在第二轮大规模裁员中削减9000个职位

**原文标题**: Microsoft to Cut 9k Workers in Second Wave of Major Layoffs

**原文链接**: [https://www.bloomberg.com/news/articles/2025-07-02/microsoft-to-cut-9-000-workers-in-second-wave-of-major-layoffs](https://www.bloomberg.com/news/articles/2025-07-02/microsoft-to-cut-9-000-workers-in-second-wave-of-major-layoffs)

无法访问文章链接。

---

## 35. 通过LSP实现代码-GUI双向编辑

**原文标题**: Code-GUI bidirectional editing via LSP

**原文链接**: [https://jamesbvaughan.com/bidirectional-editing/](https://jamesbvaughan.com/bidirectional-editing/)

本文介绍了 James Vaughan 构建的一个概念验证系统，该系统利用语言服务器协议 (LSP) 实现代码编辑器和 GUI 之间的实时双向编辑。受 Kevin Lynagh 关于基于 GUI 交互动态更新源代码以及代码 CAD 中反之亦然的想法的启发，Vaughan 创建了一个演示，其中文本编辑器和基于 Web 的 GUI 通过小型服务器同步。该服务器使用 LSP 与文本编辑器通信，并使用 WebSockets 与 Web 应用程序通信。

作者的动机是希望将他首选的文本编辑器 (Emacs) 用于基于代码的 CAD 系统，但不满意现有的解决方案，这些解决方案要么缺乏实时双向编辑，要么强制使用特定的、通常功能较弱的编辑器。该演示实现了双向的“准实时”更新，并与用户首选的编辑器无缝集成，这是作者认为其他 CAD 工具所缺乏的。

作者承认构建可用于生产的系统是一项重要的任务，但他希望这个概念验证能够激发对创意 LSP 服务器应用的进一步探索。他建议将 OpenSCAD 及其现有的 LSP 服务器作为更高级演示的潜在平台。Vaughan 暂时不打算继续该项目，但他鼓励在该领域进一步发展，并认识到冲突解决、增量编辑和整体 LSP 服务器内部结构的复杂性。

---

## 36. Show HN: Spegel，一个使用LLM重写网页的终端浏览器

**原文标题**: Show HN: Spegel, a Terminal Browser That Uses LLMs to Rewrite Webpages

**原文链接**: [https://simedw.com/2025/06/23/introducing-spegel/](https://simedw.com/2025/06/23/introducing-spegel/)

Spegel：利用大语言模型重塑网页的终端网页浏览器

Spegel是一款终端网页浏览器，它使用大语言模型来重写网页，从而提供个性化的内容视图。它最初是一个周末项目，随着谷歌 Gemini 2.5 Pro Lite 等速度更快的 LLM 的发布，它变得更实用。 Spegel 允许用户通过使用自定义提示来生成简化的解释、提取关键信息或专注于特定方面（如食谱）来根据他们的需求调整 Web 内容。

该浏览器获取 HTML 内容，通过基于用户在配置文件中定义的提示的 LLM 进行处理，并使用 Textual 将输出呈现为 markdown 格式，用于终端用户界面。 这允许在浏览期间实时调整提示和视图。

虽然已经存在 Lynx 和 Browsh 等终端浏览器，但 Spegel 旨在清除现代网站的混乱和噪音，这些网站通常未针对终端查看进行优化。 它通过 LLM 驱动的转换提供更贴近用户需求的内容来实现这一点。

Spegel 被展示为一个早期阶段的概念验证，可以通过 pip 安装。 源代码在 GitHub 上提供，供希望贡献的人使用。

---

## 37. HN Slop：从 Hacker News 产生的 AI 初创公司创意

**原文标题**: HN Slop: AI startup ideas generated from Hacker News

**原文链接**: [https://www.josh.ing/hn-slop](https://www.josh.ing/hn-slop)

好的，这是一篇基于标题推断文章可能内容的简明摘要：

文章“HN Slop: 从 Hacker News 产生的AI创业想法” 可能讨论的是在人工智能领域的、受到流行在线论坛Hacker News (HN) 上的讨论和趋势启发或产生的创业想法。

根据标题，文章可能抓取、分析或手动整理 Hacker News 上与 AI 相关的评论、帖子和总体情绪，以寻找潜在的商机。“Slop”一词表明这些想法可能很粗糙、未精炼，甚至有些非常规。它也可能暗示这些想法已经被广泛讨论，不一定是新颖或突破性的。

文章可能会列出这些人工智能创业想法，按人工智能子领域（例如，自然语言处理、计算机视觉、机器学习工具）对其进行分类，或评估其可行性和成功潜力。它还可能提供激发这些想法的现有 Hacker News 讨论的例子。

作者的意图可能是：

*   **集思广益：** 提供一系列潜在的 AI 创业概念。
*   **评论：** 分析 Hacker News 上流行的 AI 创业想法的质量和可行性。
*   **启发：** 鼓励创业者从在线社区中寻找灵感。
*   **评论：** 对 AI 创业炒作进行幽默或讽刺的评论。

本质上，这篇文章探讨了 AI 创业愿望与 Hacker News 上的集体智慧（或感知到的炒作）之间的交集。

---

## 38. 探索赛德娜任务可行性研究——核动力推进与太阳帆推进

**原文标题**: Feasibility study of a mission to Sedna – Nuclear propulsion and solar sailing

**原文链接**: [https://arxiv.org/abs/2506.17732](https://arxiv.org/abs/2506.17732)

本文是一篇arXiv预印本文章，于2025年6月提交，提出了一项使用先进推进技术前往太阳系遥远天体赛德娜的任务可行性研究。作者Ancona、Kezerashvili和Longo探索了基于D-$^{3}$He热核聚变的直接聚变驱动（DFD）火箭发动机和采用热脱附推进的先进太阳帆的应用。

该研究比较了两种推进方法在单程地球至赛德娜任务中的性能。DFD设想用于轨道进入，而太阳帆则提议用于飞掠。该分析考虑了关键任务参数，如有效载荷能力、旅行时间和潜在的科学回报。DFD是一种1.6兆瓦的系统，可以在大约10年内到达赛德娜，其中推力时间为1.5年。利用木星引力助推的太阳帆可以在7年内完成旅程。

任务分析包括出发、行星际加速、行星际巡航和交会阶段。作者强调了由于赛德娜在2075-2076年接近近日点所带来的紧迫性。该研究还考虑了科学有效载荷适应性、功率可用性和通信约束等因素。该研究为未来使用这些先进推进概念的深空任务规划提供了比较基础。本文共26页，包含5张图。

---

## 39. 罗马道路研究协会

**原文标题**: The Roman Roads Research Association

**原文链接**: [https://www.romanroads.org/](https://www.romanroads.org/)

罗马道路研究协会（RRRA）是一家慈善机构，致力于促进对不列颠群岛罗马道路网络和遗产的知识研究，其灵感来源于伊万·D·马格瑞的综合地名词典。他们利用激光雷达等现代技术研究罗马道路，揭示隐藏的考古遗迹。

RRRA出版同行评审期刊《伊提内拉》，专注于不列颠尼亚及更广阔的罗马帝国境内的罗马道路和交通基础设施，欢迎提交与新发现、挖掘以及罗马研究中道路背景相关的稿件。他们目前正在接受第六卷的投稿，截止日期为2025年11月15日。

该协会举办在线讲座和研讨会。近期和即将举行的讲座包括贝德福德郡桑迪周围的罗马道路网络、罗马-凯尔特神庙和罗马道路、罗马时期的苏格兰以及罗马别墅等主题。可通过Eventbrite或TicketTailor进行预订。

RRRA正在开发一个具有改进功能的新网站。该组织还在其YouTube频道上发布过去的在线讲座。他们出版《伊提内拉》期刊，并对会员人数的增长感到兴奋。他们还对罗马道路进行了实地挖掘。

---

## 40. 自动重写 Kubernetes 中的容器镜像引用

**原文标题**: Automatically Rewrite Container Image References in Kubernetes

**原文链接**: [https://github.com/flemzord/mutating-registry-webhook](https://github.com/flemzord/mutating-registry-webhook)

本文档描述了一种 Kubernetes 变更准入 Webhook，旨在自动重写容器镜像引用。这对于实现拉取式缓存注册表（如 AWS ECR）、企业镜像代理或将镜像从公共注册表重定向到内部注册表非常有用。

该 Webhook 使用 `RegistryRewriteRule` CRD，基于正则表达式模式定义规则，并根据标签定向特定命名空间或 Pod。它具有高性能（归功于内存中的规则缓存），默认使用 cert-manager 保证安全，并提供 Prometheus 指标。

安装过程包括部署 cert-manager（如果需要）、安装 Webhook 以及创建 `RegistryRewriteRule` 实例。本文档提供了用于构建、部署和卸载 Webhook 的 `make` 命令，以及将解决方案作为 YAML 包或 Helm chart 分发的选项。

示例演示了如何重写 Docker Hub、GCR、Quay.io 和 GitHub Container Registry 的镜像引用，包括基于命名空间和标签的条件。本文档还涵盖了 Webhook 的架构、故障排除步骤、性能指标、贡献指南和许可信息。一个关键特性是能够使用注解为特定 Pod 禁用镜像重写。

---

## 41. Show HN: 我用 Dart 做了一个 2D 游戏引擎

**原文标题**: Show HN: I made a 2D game engine in Dart

**原文链接**: [https://bullseye2d.org/](https://bullseye2d.org/)

此“Show HN”帖子介绍了一个使用 Dart 编程语言构建的全新 2D 游戏引擎。作者重点介绍了该引擎的图形功能，强调了专注于性能和视觉多样性的特性，包括：

*   **快速 2D 渲染：** 表明该引擎针对 2D 图形的渲染速度和效率进行了优化。
*   **自动精灵批处理：** 一种性能优化技术，将多个精灵分组到单个绘制调用中，从而提高渲染效率。
*   **不同混合模式：** 通过控制颜色的混合方式，实现各种视觉效果。
*   **绘制图元和图像：** 提供绘制基本形状和显示图像的能力，这对于游戏开发至关重要。
*   **位图字体（带 TTF 加载器）：** 支持使用位图字体进行文本渲染，包括加载 TrueType 字体 (TTF) 文件的能力。

本质上，该引擎为使用 Dart 创建 2D 游戏奠定了基础，重点在于性能和一套不错的图形功能。

---

## 42. 关于液态玻璃的更多杂记

**原文标题**: More assorted notes on Liquid Glass

**原文链接**: [https://morrick.me/archives/10068](https://morrick.me/archives/10068)

本文批评了苹果公司新的用户界面设计“液态玻璃”，重点关注其不一致性和潜在的缺点。作者认为，苹果公司关于采用“液态玻璃”的指导意见是自相矛盾的，它模糊了内容和导航之间的界限，同时又建议开发者清晰地分离它们。作者批评列表和表格中增加的填充和空白减少了显示的信息量，并认为重新设计的开关是不必要的。

作者还对“人机界面指南”中“层级”、“和谐”和“一致性”的概念提出质疑，认为它们的措辞不佳或逻辑存在缺陷。大部分的批评集中在应用程序图标的简化上，认为这会导致平淡乏味并稀释其含义，并以“词典”和“迁移助理”等图标的演变为例。作者担心这种趋势会将开发者推向通用、企业化的设计。

本文强调了苹果公司对应用程序外观日益增强的控制，迫使开发者遵守苹果公司的审美，即使这与他们的品牌相冲突。这与 C.M. Harrington 和 Louie Mantia 的担忧不谋而合。 Mantia 的批评强调了独立开发者和公司适应苹果设计系统的负担，以及可疑的回报。作者最后引用了 Mantia 的话，并强调了苹果公司指南中赋予苹果公司控制应用程序视觉外观的具体示例。作者认为，与早期更具支持性的指南相比，苹果公司最近提出的优先考虑系统视觉效果而非自定义外观的建议令人窒息且具有限制性。

---

## 43. 泰坦尼克号上最好的救生艇

**原文标题**: The Titanic’s Best Lifeboat

**原文链接**: [https://99percentinvisible.org/episode/632-the-titanics-best-lifeboat/](https://99percentinvisible.org/episode/632-the-titanics-best-lifeboat/)

本文挑战了围绕泰坦尼克号灾难的普遍说法，特别是认为救生艇不足是造成高死亡人数的唯一原因的观点。文章认为，当时将救生艇作为主要安全措施的观念并不流行。

历史上，救生艇并非为大规模疏散而设计。早期的救生艇主要为岸基救援船只，而船上的救生艇通常建造粗糙，难以在风暴天气中发射。20世纪初的主要策略是建造足够安全坚固的船只，使得救生艇仅用于将乘客转移到救援船上，因此没有必要为船上所有人配备足够数量的救生艇。

泰坦尼克号被认为是当时最安全的船只之一，拥有先进的设计和安全功能，但它在一个独特的脆弱点被冰山击中。文章认为，即使有额外的救生艇，时间限制和条件也会限制额外获救的人数。

这场悲剧引发了公众的强烈抗议，幸存者和遇难者的鲜明对比加剧了这种抗议，从而导致了人们观念的转变，强调了为所有乘客提供足够救生艇容量的必要性。这最终促成了1914年的SOLAS公约，该公约规定为船上所有人配备救生艇。虽然现代救生艇更安全、更高效，但文章总结道，船只本身仍然是主要的安全措施，但泰坦尼克号灾难的影响确保了每个人都应该拥有一个救生艇的位置。

---

## 44. 过去如鬼魅，未来似虚幻。

**原文标题**: The Past Is a Ghost and the Future a Fantasy

**原文链接**: [https://nautil.us/the-past-is-a-ghost-and-the-future-a-fantasy-1221672/](https://nautil.us/the-past-is-a-ghost-and-the-future-a-fantasy-1221672/)

过去是幽灵，未来是幻想
约翰·斯蒂尔在《过去是幽灵，未来是幻想》一文中探讨了这样一个观点：我们对过去的记忆和对未来的憧憬并非固定不变的现实，而是大脑的创造。他认为，记忆不仅仅是检索，而是一个重构过程，大脑会推断、润色，有时甚至会改变过去，以服务于生存和预测。斯蒂尔以童年时对狗的记忆为例，说明了生动的回忆也可能是不准确的。

同样，未来不是预言，而是一种由记忆和欲望构建的模拟。大脑使用相同的机制来回忆过去和构建潜在的未来。斯蒂尔强调，人类是“时间束缚者”，可以按照自己的意愿塑造时间。他强调了当下的重要性，当下是唯一真实的时间，尽管我们对它的感知略有延迟。

斯蒂尔将这一概念与古代智慧联系起来，引用了奥义书，并提出专注于活在当下是幸福和希望的关键。他承认，由于大脑倾向于构建一个跨越时间的自我叙事，因此居住在当下具有挑战性。

最终，这篇文章表明，认识到过去和未来的构建性质可以带来自由。重塑个人和集体叙事可以是一种解放的行为，让我们能够在当下培养意义，并充分投入到我们真正拥有的唯一现实中。

---

## 45. 伊朗暂停与联合国核监督机构的合作

**原文标题**: Iran halts cooperation with UN nuclear watchdog

**原文链接**: [https://www.politico.eu/article/iran-halts-cooperation-un-nuclear-watchdog/](https://www.politico.eu/article/iran-halts-cooperation-un-nuclear-watchdog/)

伊朗在美国六月袭击其核浓缩设施后，已暂停与国际原子能机构（IAEA）的合作。总统马苏德·佩泽什基安宣布了这一暂停，此前伊朗立法者通过了一项法案，要求国际原子能机构的核查人员在访问核设施前必须获得伊朗最高国家安全委员会的许可。该许可将基于伊朗核设施和活动的安全保障。

国际原子能机构表示已获悉相关报道，正在等待官方确认。在此之前，伊朗已经禁止国际原子能机构总干事拉斐尔·格罗西进入其核设施，并移除了监控摄像头，这些行为受到了英国、法国和德国的谴责。格罗西估计美国袭击造成的损害并非“完全”，这一声明招致了伊朗官员的强烈批评，他们认为他应该谴责这些袭击。

佩泽什基安告诉法国总统马克龙，“伊朗国内对联合国核查机构的信任已经破裂”。合作暂停代表着对2015年核协议的重大倒退，该协议允许国际原子能机构进入和检查。美国于2018年退出了该协议。格罗西警告说，伊朗可能会在“几个月内”恢复铀浓缩。

---

## 46. 对自主人工智能的信心：为什么评估基础设施必须先行

**原文标题**: Confidence in agentic AI: Why eval infrastructure must come first

**原文链接**: [https://venturebeat.com/ai/confidence-in-agentic-ai-why-eval-infrastructure-must-come-first/](https://venturebeat.com/ai/confidence-in-agentic-ai-why-eval-infrastructure-must-come-first/)

这篇 VentureBeat 文章探讨了人工智能代理在企业中日益增长的应用，强调了它们在节省时间、提高转化率和增强团队成员能力方面的潜力。像 Rocket Companies 这样的公司已经看到了显著的效益，例如节省数百万美元和增加客户容量。

然而，文章也指出了实施和扩展代理式人工智能的复杂性。挑战包括从确定性软件工程转向 LLM 的概率性质、协调多个模型和代理，以及确保响应能力。随着代理和用例数量的增长，组织需要解决延迟和路由问题。

虽然许多公司最初都在内部构建人工智能代理解决方案，但维护、调试和改进这些系统所需的专业知识正在推动公司寻求与供应商建立合作关系。为应对未来复杂性，需要强大的制衡机制、可观察性、监控以及针对监管或关键任务的人工参与流程。

一个关键的结论是，在构建人工智能代理 *之前* 建立强大的评估基础设施至关重要。该基础设施使企业能够定义“良好”的代理行为，针对定义的基准进行测试，并持续改进系统。大规模模拟对话对于发现不可预测的行为并确保可靠的代理性能至关重要。

---

## 47. 展示HN：通过推荐找工作：在你的领英人脉中寻找工作

**原文标题**: Show HN: Jobs by Referral: Find jobs in your LinkedIn network

**原文链接**: [https://jobsbyreferral.com/](https://jobsbyreferral.com/)

通过人脉找工作是一项旨在帮助用户在其领英人脉圈内寻找职位空缺的服务。它会分析您的职业关系，以识别您有人脉的公司的工作机会，从而增加通过推荐获得面试的机会。

该服务的工作方式是让用户上传他们的联系数据，可以通过来自其职业网络提供商的数据存档或 CSV 文件上传。CSV 文件需要包括每个联系人的名字、姓氏、公司和职位等字段。URL、电子邮件地址和连接时间是可选字段。

对于没有现成联系数据的用户，“通过人脉找工作”提供了一个示例 CSV 文件用于测试。一旦用户上传了他们的网络数据（无论是存档、提取的 CSV 或示例 CSV），该服务就会对其进行分析，以在其网络中找到相关的职位空缺。其目标是利用现有关系来增加获得推荐并最终找到工作的机会。

---

## 48. 将一个用 C++ 编写的大型数学软件包转换为 C++20 模块

**原文标题**: Converting a large mathematical software package written in C++ to C++20 modules

**原文链接**: [https://arxiv.org/abs/2506.21654](https://arxiv.org/abs/2506.21654)

Wolfgang Bangerth的arXiv论文《将大型C++数学软件包从C++转换为C++20模块的经验》探讨了将大型C++数学软件从基于头文件的接口迁移到较新的C++20模块系统的实际问题。该论文以deal.II有限元库（80万行代码）为例进行了研究。

作者研究了一种允许该库同时支持基于头文件和基于模块的接口的方法。他讨论了转换过程中遇到的挑战，并深入了解了模块如何在实际场景中发挥作用，评估了它们对编译时间以及转换所需的人力等技术方面的影响。

研究发现，将大型项目转换为模块是可行的，需要付出相当大的努力，但可以控制。虽然转换本身缩短了库的编译时间，但对使用转换后库的下游项目的编译时间影响尚无定论。

论文最后反思了在数学软件生态系统中更广泛地采用模块的长期策略，考虑了这种大规模转变可能涉及的潜在挑战和收益。

---

## 49. 树木在降低气温和减少拉斯维加斯户外高温暴露方面的有效性

**原文标题**: Effectiveness of trees in reducing temperature, outdoor heat exposure in Vegas

**原文链接**: [https://iopscience.iop.org/article/10.1088/2752-5295/ade17d](https://iopscience.iop.org/article/10.1088/2752-5295/ade17d)

提供的文本并非文章，而是Radware Bot Manager验证码消息。它表明用户在访问网站前被要求验证身份，原因可能是系统怀疑存在机器人活动。该消息对造成的不便表示歉意，并提供了有关在用户无法完成验证码时如何报告问题的说明。此外，它还提供了一个事件ID，用于跟踪。

**因此，没有关于树木在降低拉斯维加斯气温和户外热暴露方面的有效性的文章内容可以总结。** 用户很可能在尝试访问有关该主题的文章时遇到了此验证码。

---

## 50. 图论在电子游戏中的应用

**原文标题**: Graph Theory Applications in Video Games

**原文链接**: [https://utk.claranguyen.me/talks.php?id=videogames](https://utk.claranguyen.me/talks.php?id=videogames)

克拉拉·阮的这篇文章探讨了图论在视频游戏中的应用。文章首先概述了图论原理在3D图形中的应用，阐述了顶点、边和三角形如何在计算机图形中表示和操作，这与理论图论中的抽象表示有所不同。

然后，文章深入研究了具体的游戏机制，例如赛车游戏中的圈数计算。它解释了检查点系统如何被解释为哈密顿回路，其中每个检查点都是一个顶点，完成一圈需要遍历所有顶点并返回起点。文章提出了一种计算玩家之间距离的方法，即将检查点图重新解释为一条直线，从而将距离计算简化为简单的减法。它还分析了《马里奥赛车Wii》中的“超级捷径”漏洞，认为这是未能保证哈密顿回路完整性的结果。

最后，文章讨论了使用不相交集和并查集数据结构生成迷宫的方法。它详细介绍了迷宫的特性、它们的图形表示，以及如何使用不相交集有效地生成它们。文章解释了联合操作，展示了它是如何通过移除单元格之间的墙壁来连接单元格，最终形成一个完整的迷宫。文章强调，不相交集数据结构有助于确保迷宫生成算法创建一个从任何单元格到任何其他单元格都具有唯一路径的迷宫。

---

## 51. Chapel编程语言

**原文标题**: The Chapel Programming Language

**原文链接**: [https://chapel-lang.org/](https://chapel-lang.org/)

Chapel编程语言旨在实现从笔记本电脑到超级计算机等各种规模的高效并行计算。它是一种为性能、可读性和可扩展性而构建的开源语言。Chapel支持各种并行编程范式，包括分布式执行和GPU编程，其功能旨在最大限度地减少样板代码并最大限度地提高生产力。

Chapel的主要特点包括高效、并行、快速、可扩展、支持GPU和开源。用户称赞它的可读性以及在需要时才显示复杂性的能力，使其易于被学生和经验丰富的开发人员所接受。

Chapel已被应用于各种生产应用程序，包括CHAMPS（多物理场仿真）、Arkouda（交互式数据科学）、珊瑚礁生物多样性分析、ChOp（组合优化）和ChplUltra（超轻暗物质模拟）。这些应用程序证明了Chapel在简化开发的同时，超越现有解决方案的能力。

最近的更新包括 Chapel 2.5 的发布、ChapelCon '25 的论文征集以及一系列博客文章和演示，重点介绍了该语言的功能并解决了关于可扩展并行编程的常见误解。每周一次的深入/演示会议已经启动，并且 2025 年春季的通讯已发布。Chapel 社区鼓励新用户通过现有资源尝试、获取和学习该语言。

---

## 52. 克劳德的x86汇编曼德勃罗特集

**原文标题**: Mandelbrot in x86 Assembly by Claude

**原文链接**: [https://simonwillison.net/2025/Jul/2/mandelbrot-in-x86-assembly-by-claude/](https://simonwillison.net/2025/Jul/2/mandelbrot-in-x86-assembly-by-claude/)

本文记录了作者使用AI Claude生成x86汇编语言ASCII艺术曼德勃罗分形生成器的实验。最初，Claude Sonnet 4生成的代码看似汇编，但需要大量修改。作者使用Claude基于初始代码生成的Dockerfile，试图在Mac上编译并运行该代码。在多次失败和编译错误后，作者使用Claude Code（使用`--dangerously-skip-permissions`选项）在Docker环境中迭代地调试和修改汇编代码。

Claude Code分析了错误，修改了汇编，并在循环中重新运行了构建过程。最初，输出是一个有缺陷的图像，只包含“@”符号，表明迭代计数存在问题。在作者对结果表示不满后，Claude Code继续改进代码。最终，Claude Code成功生成了曼德勃罗分形的ASCII艺术图像，作者提供了最终的功能性汇编代码、Dockerfile以及Claude Code会话的完整记录。本文突出了AI辅助编程和调试的迭代过程，即使初始输出需要大量的人工指导和反馈。

---

## 53. 构建个人AI工厂

**原文标题**: Building a Personal AI Factory

**原文链接**: [https://www.john-rush.com/posts/ai-20250701.html](https://www.john-rush.com/posts/ai-20250701.html)

本文介绍了一种用于软件开发的“个人AI工厂”，它围绕Claude Code和Goose、o3等本地模型构建。其核心原则是“修正输入，而非输出”，重点在于改进系统，而不是修补单个代码错误。

该工作流程包含三个步骤：**规划**、**执行**和**验证/反馈**。o3从一个高级任务生成一个计划，然后对其进行细化。Sonnet 4验证该计划并创建任务列表。Claude Code使用Sonnet 3.7或4执行该计划，并在过程中提交更改。最后，Sonnet 4和o3分别根据计划和原始请求验证生成的代码，识别问题，然后将其纳入计划模板中，以供将来运行。

作者使用Git worktree来实现并行开发，同时运行多个Claude Code实例。一个关键要素是创建专门的代理来处理特定任务，例如代码样式和集成内部库。作者强调迭代输入（计划、提示、代理组合），而不是调试生成的代码，并并行运行代理以从失败中学习。

未来的改进重点是更好的代理协调、使业务文档与代理需求对齐，以及更复杂的工作流程。作者还旨在最大化不同模型提供商的令牌使用量，以克服Bedrock的令牌限制。目标是创建一个可以可靠地生成代码的系统，同时不断改进其自身的流程和指令。

---

## 54. 以咒骂应对疼痛：评估新型脏话的效果

**原文标题**: Swearing as a Response to Pain: Assessing Effects of Novel Swear Words

**原文链接**: [https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2020.00723/full](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2020.00723/full)

本研究通过测试新造的“脏话”来调查说脏话的止痛效果是源于情绪唤醒还是注意力转移。研究人员比较了重复传统脏话“fuck”、两个新词“fouch”（旨在唤起情绪）和“twizpipe”（旨在转移注意力）以及一个中性词对冷压试验中疼痛阈值和耐受度的影响。九十二名参与者在重复四个词中的一个时将手浸入冰水中，并测量他们的心率、疼痛感知以及情绪、幽默感和分心程度的评分。

结果重现了之前的发现，表明与中性词相比，重复“fuck”增加了疼痛阈值和耐受度，并且与更高的情绪、幽默感和分心程度评分相关。然而，新的“脏话”“fouch”和“twizpipe”虽然被评为比中性词更具情感性和幽默感，但并未提高疼痛阈值或耐受度。在各种条件下均未观察到心率或疼痛感知的显着变化。

中介分析未确定说脏话缓解疼痛的明确途径，表明注意力转移不是关键因素。该研究支持情绪唤醒可能有助于说脏话的镇痛效果的观点，但还需要进一步研究。研究结果还表明，疼痛缓解效果不容易通过新造的词语重现，这可能是由于缺乏已建立的脏话中固有的学习联想。

---

## 55. Show HN: Core – LLM开源内存图 – 可分享，用户所有

**原文标题**: Show HN: Core – open source memory graph for LLMs – shareable, user owned

**原文链接**: [https://github.com/RedPlanetHQ/core](https://github.com/RedPlanetHQ/core)

C.O.R.E. (情境观察与回忆引擎) 是一个开源、用户拥有的 LLM 记忆图，为管理上下文提供私有、可移植和可共享的解决方案。它允许用户在本地或通过托管版本存储和访问他们的信息，并将其连接到 Cursor 和 Claude 等工具，以获得个性化的 AI 响应。

与简单的“便签”记忆系统不同，C.O.R.E. 作为一个动态的时间知识图谱运行，其中每个事实都是一个“陈述”，包含其完整历史记录（说了什么、谁说的、什么时候说的以及为什么重要）。这提供了透明度和可追溯性。

主要功能包括摄取数据、在私有记忆空间中搜索以及将其用于工作区。用户可以审计更改（例如，价格更新）、追踪信息来源，并了解系统为何相信某些事情。

文章详细介绍了云端和本地设置说明。云端设置包括注册、添加文本以生成图谱以及连接 Cursor。本地设置使用 Docker，需要 OpenAI API 密钥，并涉及复制环境变量、启动应用程序以及通过魔法链接登录。该指南还详细介绍了如何将 C.O.R.E. 作为 MCP 服务器连接到 Cursor。

此外，C.O.R.E. 提供用于摄取和搜索的 API，需要 API 密钥进行身份验证。提供了两者的示例请求正文。

该工具正在积极开发中，计划包括具有唯一 URL 的多个空间、用户控制的共享、摄取过滤器、细粒度的 API 密钥权限、改进的会话支持、审计日志记录、基于角色的访问控制、Webhooks 和通知。它建议不要存储敏感数据、凭据或系统日志。

---

## 56. 丝绒日落乐队，看似由人工智能生成，在Spotify上有32.5万听众。

**原文标题**: The Velvet Sundown are a seemingly AI-generated band with 325k Spotify listeners

**原文链接**: [https://musically.com/2025/06/26/velvet-sundown-are-a-seemingly-ai-generated-band-with-325k-spotify-listeners/](https://musically.com/2025/06/26/velvet-sundown-are-a-seemingly-ai-generated-band-with-325k-spotify-listeners/)

本文调查了拥有超过32.5万Spotify月度听众的乐队The Velvet Sundown，该乐队疑似由人工智能生成。该事件起源于Reddit和TikTok，突显了该乐队在线存在感极低且使用人工智能生成的头像，却拥有异常高的听众数量。

Deezer已将The Velvet Sundown的部分音乐标记为可能由人工智能生成，而DistroKid是用于将其音乐上传到流媒体服务的发行商。该乐队的受欢迎程度似乎与战略性歌单有关。他们的歌曲在由拥有大量粉丝的账号（Extra Music、Solitude Collective、KULTPOP!、In-between和Lost Records）策划的“越南战争音乐”和“橘子郡男孩原声”等歌单中占据显著位置，尽管这些歌曲与这些歌单的主题没有明显的联系。

文章强调，虽然创建一个虚拟乐队并使用人工智能生成的音乐并不违法，但人为地增加流量以赚取版税则属违法行为。The Velvet Sundown的案例中没有直接证据表明存在这种情况，而是巧妙的歌单策略可能提高了他们的发现度。文章最后指出，人工智能生成音乐的格局正在演变，音乐行业正在努力确定其地位，并提到了约翰·奥利弗关于人工智能垃圾音乐的片段，他在其中使用了乐队The Devil Inside来展示可疑的人工智能音乐主题。

---

## 57. 天鹅绒日落乐队，看似由人工智能生成，在Spotify上有32.5万听众。

**原文标题**: The Velvet Sundown are a seemingly AI-generated band with 325k Spotify listeners

**原文链接**: [https://musically.com/2025/06/26/velvet-sundown-are-a-seemingly-ai-generated-band-with-325k-spotify-listeners/](https://musically.com/2025/06/26/velvet-sundown-are-a-seemingly-ai-generated-band-with-325k-spotify-listeners/)

文章调查了“丝绒日落”（The Velvet Sundown）乐队，该乐队在Spotify上拥有超过32.5万名月度听众，但似乎是由人工智能生成的。这个故事始于Reddit和TikTok，用户注意到该乐队的在线存在感极低，宣传材料的真实性也令人怀疑，但听众数量却很高。

Deezer已将该乐队的音乐标记为可能由人工智能生成。调查显示，他们的音乐通过DistroKid发行，并大量出现在由Extra Music和Solitude Collective等不知名策划账户管理的播放列表中。这些播放列表拥有成千上万的粉丝，不成比例地包含了“丝绒日落”的曲目，有时甚至占据了很大比例，尽管主题不一致。例如，尽管该乐队的专辑在2025年发行，但在“越南战争音乐”播放列表中有26首歌曲，在“橘子郡男孩原声”播放列表中有22首歌曲。

文章强调，虽然创作人工智能音乐并将其上传到流媒体服务并不违法，但人为地增加播放量以获取版税是欺诈行为。目前没有确凿的证据表明“丝绒日落”存在欺诈行为，但他们的播放列表策略可能影响了推荐算法，使他们获得了更广泛的影响力。文章最后强调了当前音乐行业对于人工智能生成的音乐与人类创作的内容并存以及对听众的吸引力方面的不确定性。

---

## 58. 所有优秀的编辑都是海盗：纪念刘易斯·H·拉帕姆

**原文标题**: All Good Editors Are Pirates: In Memory of Lewis H. Lapham

**原文链接**: [https://www.laphamsquarterly.org/roundtable/all-good-editors-are-pirates](https://www.laphamsquarterly.org/roundtable/all-good-editors-are-pirates)

基拉·布伦纳·唐的《所有优秀的编辑都是海盗：纪念刘易斯·H·拉帕姆》是对已故著名散文家、编辑及《拉帕姆季刊》创始人刘易斯·H·拉帕姆的生平和影响的个人反思。唐曾担任该杂志的创始执行编辑，她深情地回忆了与拉帕姆共事的八年，突出了他独特的杂志创作方法以及他对她职业生涯的深刻影响。

文章详细描述了《拉帕姆季刊》于2007年的简朴开端，并将其与后来蓬勃发展的出版物形成对比。唐强调了拉帕姆的奉献精神、职业道德和包容的领导风格，指出他愿意征求每个人的意见，无论他们的职位如何。她回忆起他对高质量写作、周到讨论以及自由放任的编辑方式的坚持，从而激发了创造力和独立性。

唐还分享了一些轶事，揭示了拉帕姆的个性，从他光鲜亮丽的社交生活到他对香烟烟雾的偏爱以及他的口头禅“前进，亲爱的心”。她强调了拉帕姆的指导如何塑造了她对杂志创作的理解，并灌输了一种重视声音和深入探索思想的信念。

文章最终，唐承认拉帕姆对她自己与艾比·拉波波特共同创立的《陌生人指南》的影响，并表达了对一个文学时代逝去的失落感。最终，这篇文章是对一位教会她如何成为“海盗”编辑的人的衷心致敬，即窃取最好的想法并开辟自己的道路。

---

## 59. 农村医院倒闭的惊人原因

**原文标题**: The Surprising Reason Rural Hospitals Are Closing

**原文链接**: [https://time.com/7298891/rural-hospitals-closing-explained-health-care/](https://time.com/7298891/rural-hospitals-closing-explained-health-care/)

本文调查了美国农村医院倒闭这一令人担忧的趋势，重点关注阿拉巴马州托马斯维尔地区医疗中心的案例。虽然普遍认为医疗保险和医疗补助的低报销率是罪魁祸首，但本文认为，主要原因是来自私人保险公司的不充分补偿。

农村医院严重依赖私人保险的收入，通常覆盖65-80%的患者费用。然而，由于患者数量较少且缺乏议价能力，这些医院在与保险公司谈判公平的报销率方面面临重大挑战。在阿拉巴马州，蓝十字蓝盾在大型团体私人保险市场中占据主导地位，控制了94%的市场份额，这进一步限制了医院的谈判能力，导致服务报酬严重不足。

农村医院的倒闭给社区带来了可怕的后果，迫使居民长途跋涉寻求医疗服务，延误治疗，并增加了住院率和住院时间。它还通过阻碍新企业的发展和影响劳动力的健康，对当地经济产生负面影响。

本文重点介绍了潜在的解决方案，包括农村医院加入更大的城市医院网络以获得更好的议价能力，组建农村医院网络，以及政府通过《农村医院稳定法案》等立法进行干预。作者还提到了预防性保健的重要性以及人工智能技术在农村医院中的潜力。最终，本文强调了农村医院在维护社区健康方面的关键作用，以及解决它们所面临的金融挑战的迫切需要。

---

## 60. 霍伊尔态 (2021)

**原文标题**: The Hoyle State (2021)

**原文链接**: [https://johncarlosbaez.wordpress.com/2021/02/04/the-hoyle-state/](https://johncarlosbaez.wordpress.com/2021/02/04/the-hoyle-state/)

本文深入探讨了核物理学的复杂性，特别关注碳-12的霍伊尔态。文章首先解释了理解原子核所面临的挑战，对比了强核力与电磁力，并介绍了液滴模型和壳模型等模型，以简化对核结构的理解。

文章随后解释说，原子核可以被认为是较小原子核的集合，如氘核、氚核、氦核和α粒子。文章介绍了霍伊尔态，它是碳-12的一种激发态，在此状态下，碳-12表现为三个互相环绕的α粒子，其能量略高于三个分离的α粒子。这使得处于这种激发态的碳可以分解成三个α粒子。

霍伊尔态的能级非常接近铍-8原子核加上一个α粒子的能量。这种接近共振的现象，由弗雷德·霍伊尔预测，对于恒星中碳的形成至关重要，因为它促进了α粒子与铍核的融合。虽然有些人认为这是人择原理的胜利，但作者认为，霍伊尔最初的预测是基于恒星中观察到的元素丰度，而人择解释是不必要的。

文章最后强调了利用超级计算机进一步理解霍伊尔态的持续研究，并指出即使是基态碳也可以近似为紧密三角形中的三个α粒子，而霍伊尔态则类似于弯曲的手臂结构。

---

## 61. 我做了一个东西，改变了我的朋友圈子的社交结构。

**原文标题**: I built something that changed my friend group's social fabric

**原文链接**: [https://blog.danpetrolito.xyz/i-built-something-that-changed-my-friend-gro-social-fabric/](https://blog.danpetrolito.xyz/i-built-something-that-changed-my-friend-gro-social-fabric/)

2022年，作者的朋友们分散在世界各地，由于Signal群聊中大量的通知，难以协调游戏会话和随意聊天。问题在于关于玩游戏的消息被淹没，朋友们错过了即兴聚会。

作者创建了一个Discord机器人，当有人加入语音频道时，该机器人会向服务器发送通知。这个“蝙蝠信号”旨在解决通知过载问题，并鼓励自发互动。该机器人使用discord.py构建，跟踪加入情况，并将数据存储在Supabase托管的Postgres数据库中。

起初，该机器人受到质疑，但很快就流行起来。它显著减少了协调消息，并培养了一种超越计划游戏会话的非正式聚会文化。多年来收集的数据显示，Discord服务器的使用率一直很高，每年有数千人加入。作者将该机器人的成功归功于其促进快速、随意互动的能力，这对忙碌的朋友和新手父母尤其有益。

作者现在每年为朋友们的圣诞派对制作一份“Discord年度回顾”，突出个人和群组的使用统计数据。未来的计划包括增加成就并跟踪在Discord中花费的时间。作者还设想了一种物联网设备，该设备带有RGB灯，指示指定的朋友何时加入Discord语音频道，并考虑在有足够兴趣的情况下将其变成真正的产品。

---

## 62. 自然何时变得色彩斑斓？

**原文标题**: When Did Nature Burst into Vivid Color?

**原文链接**: [https://www.quantamagazine.org/when-did-nature-burst-into-vivid-color-20250627/](https://www.quantamagazine.org/when-did-nature-burst-into-vivid-color-20250627/)

本文探讨了色彩视觉和自然界中鲜艳信号的进化历史，旨在解决哪个先出现的问题。进化生物学家 Zachary Emberts 和 John Wiens 利用化石记录和系统发育树，重构了五亿年的进化史。他们假设色彩视觉和鲜艳信号是协同进化的。

他们的研究表明，色彩视觉的进化时间比之前认为的要早，大约在4亿到5亿年前，比鲜艳信号的出现早1亿到2亿年。鲜艳的水果和种子大约在3亿年前出现，随后是花朵（1.4亿到2.5亿年前）、警戒色（1.3亿年前），最后是动物的性信号颜色（1亿年前）。

节肢动物和脊椎动物中色彩视觉的独立进化，以及物种间多样的色彩感知能力，突显了这一进化过程的复杂性。文章讨论了重构进化史的挑战，承认颜色不易形成化石，并且性状会随着时间的推移而出现和消失。尽管存在这些局限性，该研究为自然界中色彩的发展提供了宝贵的见解，表明色彩视觉最初的进化原因可能并非为了信号传递，而是为了物体识别或在水生环境中导航。文章最后推测，由于警戒信号和性信号的不断进化，自然界可能会变得更加色彩缤纷。

---

## 63. Australians to face age checks from search engines

**原文标题**: Australians to face age checks from search engines

**原文链接**: [https://ia.acs.org.au/article/2025/australians-to-face-age-checks-from-search-engines.html](https://ia.acs.org.au/article/2025/australians-to-face-age-checks-from-search-engines.html)

Here's a concise summary of the article:

In Australia, search engines like Google and Microsoft's Bing will be required to implement age assurance checks for logged-in users by the end of 2025. This is part of a new online safety code developed with technology companies and registered by the eSafety Commissioner. If a user is determined to be under 18, the search engine will automatically activate the highest safety settings, filtering out pornography and high-impact violence.

Age assurance methods could include ID verification, biometrics, or using online activity data to infer age. Non-logged-in users will also see default blurring of explicit content. The code also mandates improvements to search and age assurance tech, prevention of harmful autocomplete suggestions, and providing crisis information for searches related to self-harm.

The aim is to protect Australian children, and the code was co-led by Digital Industry Group Inc. (DIGI), whose members include Google and Microsoft. Failure to comply could result in substantial penalties. The eSafety Commissioner is also seeking further safety commitments from the industry regarding app stores, device manufacturers, social media, and messaging services, particularly concerning the use of generative AI chatbots by children. If the changes proposed by the industry are unsatisfactory, the eSafety Commissioner will move to developing mandatory standards.


---

## 64. Show HN: A continuation of IRS Direct File that can be self-hosted

**原文标题**: Show HN: A continuation of IRS Direct File that can be self-hosted

**原文链接**: [https://github.com/openfiletax/openfile](https://github.com/openfiletax/openfile)

生成摘要时出错

---

## 65. Math.Pow(-1, 2) == -1 in Windows 11 Insider build

**原文标题**: Math.Pow(-1, 2) == -1 in Windows 11 Insider build

**原文链接**: [https://github.com/dotnet/runtime/issues/117233](https://github.com/dotnet/runtime/issues/117233)

生成摘要时出错

---

## 66. The Evasive Evitability of Enshittification

**原文标题**: The Evasive Evitability of Enshittification

**原文链接**: [https://tailscale.com/blog/evitability-of-enshittification](https://tailscale.com/blog/evitability-of-enshittification)

生成摘要时出错

---

## 67. Show HN: HackerNewt – Breadth-first exploring HN client for iOS

**原文标题**: Show HN: HackerNewt – Breadth-first exploring HN client for iOS

**原文链接**: [https://apps.apple.com/us/app/hackernewt-for-hacker-news/id6448201970](https://apps.apple.com/us/app/hackernewt-for-hacker-news/id6448201970)

生成摘要时出错

---

## 68. Give footnotes the boot – alternatives to footnotes on the web

**原文标题**: Give footnotes the boot – alternatives to footnotes on the web

**原文链接**: [https://jakearchibald.com/2025/give-footnotes-the-boot/](https://jakearchibald.com/2025/give-footnotes-the-boot/)

生成摘要时出错

---

## 69. PortablE

**原文标题**: PortablE

**原文链接**: [https://cshandley.co.uk/portable/](https://cshandley.co.uk/portable/)

生成摘要时出错

---

## 70. The wanton destruction of a creative-tech era

**原文标题**: The wanton destruction of a creative-tech era

**原文链接**: [https://blog.greg.technology/2025/06/30/fastly.html](https://blog.greg.technology/2025/06/30/fastly.html)

生成摘要时出错

---

## 71. Genetic code enables zebrafish to mend damaged organs

**原文标题**: Genetic code enables zebrafish to mend damaged organs

**原文链接**: [https://www.caltech.edu/about/news/genetic-code-enables-zebrafish-to-mend-damaged-organs](https://www.caltech.edu/about/news/genetic-code-enables-zebrafish-to-mend-damaged-organs)

生成摘要时出错

---

## 72. OpenFLOW – Quickly make beautiful infrastructure diagrams local to your machine

**原文标题**: OpenFLOW – Quickly make beautiful infrastructure diagrams local to your machine

**原文链接**: [https://github.com/stan-smith/OpenFLOW](https://github.com/stan-smith/OpenFLOW)

生成摘要时出错

---

## 73. Intel's new CEO explores big shift in chip manufacturing business

**原文标题**: Intel's new CEO explores big shift in chip manufacturing business

**原文链接**: [https://www.reuters.com/business/retail-consumer/intels-new-ceo-explores-big-shift-chip-manufacturing-business-2025-07-02/](https://www.reuters.com/business/retail-consumer/intels-new-ceo-explores-big-shift-chip-manufacturing-business-2025-07-02/)

生成摘要时出错

---

## 74. Embabel Agent Framework for the JVM

**原文标题**: Embabel Agent Framework for the JVM

**原文链接**: [https://github.com/embabel/embabel-agent](https://github.com/embabel/embabel-agent)

生成摘要时出错

---

## 75. 90-degree turn brings bridge project to a screeching halt

**原文标题**: 90-degree turn brings bridge project to a screeching halt

**原文链接**: [https://www.thetimes.com/world/asia/article/90-degree-turn-brings-bridge-project-to-a-screeching-halt-gnqqdkrrv](https://www.thetimes.com/world/asia/article/90-degree-turn-brings-bridge-project-to-a-screeching-halt-gnqqdkrrv)

生成摘要时出错

---

## 76. The Hidden Engineering of Liquid Dampers in Skyscrapers

**原文标题**: The Hidden Engineering of Liquid Dampers in Skyscrapers

**原文链接**: [https://practical.engineering/blog/2025/7/1/the-hidden-engineering-of-liquid-dampers-in-skyscrapers](https://practical.engineering/blog/2025/7/1/the-hidden-engineering-of-liquid-dampers-in-skyscrapers)

生成摘要时出错

---

## 77. Claude Code now supports hooks

**原文标题**: Claude Code now supports hooks

**原文链接**: [https://docs.anthropic.com/en/docs/claude-code/hooks](https://docs.anthropic.com/en/docs/claude-code/hooks)

生成摘要时出错

---

## 78. GPEmu: A GPU emulator for rapid, low-cost deep learning prototyping [pdf]

**原文标题**: GPEmu: A GPU emulator for rapid, low-cost deep learning prototyping [pdf]

**原文链接**: [https://vldb.org/pvldb/vol18/p1919-wang.pdf](https://vldb.org/pvldb/vol18/p1919-wang.pdf)

生成摘要时出错

---

## 79. Microsoft to lay off as many as 9k employees in latest round

**原文标题**: Microsoft to lay off as many as 9k employees in latest round

**原文链接**: [https://www.seattletimes.com/business/microsoft/microsoft-to-lay-off-as-many-as-9000-employees-in-latest-round/](https://www.seattletimes.com/business/microsoft/microsoft-to-lay-off-as-many-as-9000-employees-in-latest-round/)

生成摘要时出错

---

## 80. Aesop in Words of One Syllable

**原文标题**: Aesop in Words of One Syllable

**原文链接**: [https://blog.pgdp.net/2025/07/01/aesop-in-words-of-one-syllable/](https://blog.pgdp.net/2025/07/01/aesop-in-words-of-one-syllable/)

生成摘要时出错

---

## 81. Off with Their Heads: Illustrations of Blemmyes (ca. 1175–1724)

**原文标题**: Off with Their Heads: Illustrations of Blemmyes (ca. 1175–1724)

**原文链接**: [https://publicdomainreview.org/collection/blemmyes/](https://publicdomainreview.org/collection/blemmyes/)

生成摘要时出错

---

## 82. Superstar coders are raking it in. Others, not so much

**原文标题**: Superstar coders are raking it in. Others, not so much

**原文链接**: [https://www.economist.com/business/2025/07/01/superstar-coders-are-raking-it-in-others-not-so-much](https://www.economist.com/business/2025/07/01/superstar-coders-are-raking-it-in-others-not-so-much)

生成摘要时出错

---

## 83. Teaching feed readers about YouTube subscriptions

**原文标题**: Teaching feed readers about YouTube subscriptions

**原文链接**: [https://lectio.news/](https://lectio.news/)

生成摘要时出错

---

## 84. Abstraction boundaries are optimization boundaries

**原文标题**: Abstraction boundaries are optimization boundaries

**原文链接**: [https://blog.snork.dev/posts/abstraction-boundaries-are-optimization-boundaries.html](https://blog.snork.dev/posts/abstraction-boundaries-are-optimization-boundaries.html)

生成摘要时出错

---

## 85. Jack Welch, the Man Who Broke Capitalism (2022)

**原文标题**: Jack Welch, the Man Who Broke Capitalism (2022)

**原文链接**: [https://www.forbes.com/sites/kylewestaway/2022/05/31/jack-welch-the-man-who-broke-capitalism/](https://www.forbes.com/sites/kylewestaway/2022/05/31/jack-welch-the-man-who-broke-capitalism/)

生成摘要时出错

---

## 86. People Keep Inventing Prolly Trees

**原文标题**: People Keep Inventing Prolly Trees

**原文链接**: [https://www.dolthub.com/blog/2025-06-03-people-keep-inventing-prolly-trees/](https://www.dolthub.com/blog/2025-06-03-people-keep-inventing-prolly-trees/)

生成摘要时出错

---

## 87. A CarFax for Used PCs; Hewlett Packard wants to give old laptops new life

**原文标题**: A CarFax for Used PCs; Hewlett Packard wants to give old laptops new life

**原文链接**: [https://spectrum.ieee.org/carmax-used-pcs](https://spectrum.ieee.org/carmax-used-pcs)

生成摘要时出错

---

## 88. Muxio: Rust layered stream and RPC toolkit

**原文标题**: Muxio: Rust layered stream and RPC toolkit

**原文链接**: [https://crates.io/crates/muxio](https://crates.io/crates/muxio)

生成摘要时出错

---

## 89. Victory Shoot: Hanemono in Toy Form

**原文标题**: Victory Shoot: Hanemono in Toy Form

**原文链接**: [https://nicole.express/2025/victory-at-what-cost.html](https://nicole.express/2025/victory-at-what-cost.html)

生成摘要时出错

---

## 90. Microsoft laying off about 9k employees in latest round of cuts

**原文标题**: Microsoft laying off about 9k employees in latest round of cuts

**原文链接**: [https://www.cnbc.com/2025/07/02/microsoft-laying-off-about-9000-employees-in-latest-round-of-cuts.html](https://www.cnbc.com/2025/07/02/microsoft-laying-off-about-9000-employees-in-latest-round-of-cuts.html)

生成摘要时出错

---

## 91. I write type-safe generic data structures in C

**原文标题**: I write type-safe generic data structures in C

**原文链接**: [https://danielchasehooper.com/posts/typechecked-generic-c-data-structures/](https://danielchasehooper.com/posts/typechecked-generic-c-data-structures/)

生成摘要时出错

---

## 92. Pluto is a unique dialect of Lua with a focus on general-purpose programming

**原文标题**: Pluto is a unique dialect of Lua with a focus on general-purpose programming

**原文链接**: [https://github.com/PlutoLang/Pluto](https://github.com/PlutoLang/Pluto)

生成摘要时出错

---

## 93. The original LZEXE (A.K.A. Kosinski) compressor source code has been released

**原文标题**: The original LZEXE (A.K.A. Kosinski) compressor source code has been released

**原文链接**: [https://clownacy.wordpress.com/2025/05/24/the-original-lzexe-a-k-a-kosinski-compressor-source-code-has-been-released/](https://clownacy.wordpress.com/2025/05/24/the-original-lzexe-a-k-a-kosinski-compressor-source-code-has-been-released/)

生成摘要时出错

---

## 94. Moderna says mRNA flu vaccine sailed through trial, beating standard shot

**原文标题**: Moderna says mRNA flu vaccine sailed through trial, beating standard shot

**原文链接**: [https://arstechnica.com/health/2025/07/moderna-says-its-mrna-seasonal-flu-shot-is-27-better-than-current-vaccine/](https://arstechnica.com/health/2025/07/moderna-says-its-mrna-seasonal-flu-shot-is-27-better-than-current-vaccine/)

生成摘要时出错

---

## 95. Voyage of Magellan – Epilogue: Sailor of Eternal Fame

**原文标题**: Voyage of Magellan – Epilogue: Sailor of Eternal Fame

**原文链接**: [https://analog-antiquarian.net/2025/06/27/epilogue-sailor-of-eternal-fame/](https://analog-antiquarian.net/2025/06/27/epilogue-sailor-of-eternal-fame/)

生成摘要时出错

---

## 96. Canada's "Strong Borders Act" (Bill C-2) Contains Four Mass Surveillance Trojans

**原文标题**: Canada's "Strong Borders Act" (Bill C-2) Contains Four Mass Surveillance Trojans

**原文链接**: [https://easydns.com/blog/2025/06/05/canadas-strong-borders-act-bill-c-2-contains-four-surveillance-trojans/](https://easydns.com/blog/2025/06/05/canadas-strong-borders-act-bill-c-2-contains-four-surveillance-trojans/)

生成摘要时出错

---

## 97. Exploring Trichromacy through Maxwell's Color Experiment (2023)

**原文标题**: Exploring Trichromacy through Maxwell's Color Experiment (2023)

**原文链接**: [https://maxwell.kohterai.com/](https://maxwell.kohterai.com/)

生成摘要时出错

---

## 98. A Medical-History Museum Contends with Its Collection of Human Remains

**原文标题**: A Medical-History Museum Contends with Its Collection of Human Remains

**原文链接**: [https://www.newyorker.com/magazine/2025/06/30/a-medical-history-museum-contends-with-its-collection-of-human-remains](https://www.newyorker.com/magazine/2025/06/30/a-medical-history-museum-contends-with-its-collection-of-human-remains)

生成摘要时出错

---

## 99. Flightradar24 uses MLAT to counter GPS jamming

**原文标题**: Flightradar24 uses MLAT to counter GPS jamming

**原文链接**: [https://www.flightradar24.com/blog/aviation-explainer-series/how-flightradar24-uses-mlat-to-counter-gps-jamming/](https://www.flightradar24.com/blog/aviation-explainer-series/how-flightradar24-uses-mlat-to-counter-gps-jamming/)

生成摘要时出错

---

## 100. Melbourne man discovers extensive model train network underneath house

**原文标题**: Melbourne man discovers extensive model train network underneath house

**原文链接**: [https://www.sbs.com.au/news/article/i-was-shocked-melbourne-mans-unbelievable-find-after-buying-house/m4sksfer8](https://www.sbs.com.au/news/article/i-was-shocked-melbourne-mans-unbelievable-find-after-buying-house/m4sksfer8)

生成摘要时出错

---

