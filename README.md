# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-10-31.md)

*最后自动更新时间: 2025-10-31 17:50:10*
## 1. Ubuntu 推出架构变体

**原文标题**: Ubuntu Introduces Architecture Variants

**原文链接**: [https://lwn.net/Articles/1044383/](https://lwn.net/Articles/1044383/)

Ubuntu 25.10引入“架构变体”，允许针对特定x86-64架构级别（如x86-64-v3）构建和优化软件包。这种由Michael Hudson-Doyle倡导的方法为现代硬件提供性能改进，同时避免像RHEL放弃x86-64-v2支持那样强制淘汰旧系统。

用户可以选择使用优化的x86-64-v3软件包。然而，评论区显示了对该方法相关成本的担忧，包括仓库和镜像的存储需求增加、构建多个变体导致的构建时间延长，以及与支持和二进制混合相关的潜在复杂性。一些评论员指出，RHEL/Fedora由于这些基础设施和支持负担而选择不实施类似的变体，认为彻底的决裂更为可取，尽管会对遗留硬件用户产生影响。总体情绪倾向于赞赏Ubuntu方法的灵活性，但也承认其在资源、维护和支持复杂性方面的潜在挑战。

---

## 2. Nix 衍生品疯狂

**原文标题**: Nix Derivation Madness

**原文链接**: [https://fzakaria.com/2025/10/29/nix-derivation-madness](https://fzakaria.com/2025/10/29/nix-derivation-madness)

本文探讨了Nix包管理系统令人惊讶的方面，重点关注固定输出派生(FOD)及其对依赖关系图的影响。作者最初遇到一种情况：Ruby二进制文件存在，但其对应的派生文件在他们的系统或NixOS缓存中不可用。

调查表明，FOD虽然为给定哈希生成一致的输出，但可能会在派生中引入意外的变动。对FOD属性的更改，例如添加“垃圾”，会改变其派生路径（.drv文件），而不会影响最终输出。这意味着依赖于FOD的派生也会获得新的.drv路径，即使它们的输出保持不变。如果输出之前被缓存，则到更新后的.drv的链接会丢失，从而产生差异。

此外，作者展示了一个场景：两个具有*相同*输出的FOD可以用作另一个派生的输入。值得注意的是，可以从派生的JSON表示中*删除*其中一个输入，并且修改后的派生仍然会产生相同的输出。这突出了派生和输出之间的多对一关系，允许看似不同的派生产生相同的结果，并展示了固定输出派生引入的复杂动态。文章强调，理解FOD对于理解Nix的行为以及与依赖管理和缓存相关的潜在陷阱至关重要。

---

## 3. 因脑部排液导致睡眠不足，注意力涣散。

**原文标题**: Attention lapses due to sleep deprivation due to flushing fluid from brain

**原文链接**: [https://news.mit.edu/2025/your-brain-without-sleep-1029](https://news.mit.edu/2025/your-brain-without-sleep-1029)

麻省理工学院新闻报道：研究揭示睡眠不足后注意力涣散与脑脊液流动有关。研究人员发现，注意力短暂失效（常被描述为“走神”）与脑脊液*流出*大脑的波浪式流动相一致，而这种过程通常只发生在睡眠期间，用于清除废物。

该研究发表于《自然·神经科学》，让睡眠不足和睡眠充足的参与者在接受fMRI和脑电图监测的同时执行注意力任务。睡眠不足的参与者表现更差，并且关键的是，研究人员观察到脑脊液流动与注意力涣散同时发生。具体来说，当注意力失效时，脑脊液就*流出*大脑，而当注意力恢复时，脑脊液又*流回*大脑。

研究人员推测，睡眠不足的大脑试图通过在清醒时启动这些脑脊液脉冲来补偿夜间清洁的不足，但代价是损害了注意力。他们还注意到同步的生理变化，包括心率和呼吸频率降低以及瞳孔收缩，这表明存在一个统一的回路控制着注意力和身体功能。该回路可能涉及去甲肾上腺素系统。 研究结果表明，大脑对睡眠的需求非常关键，以至于它甚至会在清醒时启动类似睡眠的清洁过程，从而暂时损害注意力表现。

---

## 4. AI爬虫请求注释脚本

**原文标题**: AI scrapers request commented scripts

**原文链接**: [https://cryptography.dog/blog/AI-scrapers-request-commented-scripts/](https://cryptography.dog/blog/AI-scrapers-request-commented-scripts/)

Aaron P. MacSween的文章详细描述了人工智能抓取器请求JavaScript文件的发现，这些文件仅在HTML注释中引用（因此不应由合法浏览器请求）。 这些抓取器很可能正在收集用于LLM训练的数据，它们表现出不同程度的复杂性，一些使用真实的浏览器用户代理字符串，而另一些使用默认的HTTP库值。 MacSween将此行为归类为根本性的，这意味着修复它需要抓取器从根本上改变其行为，使其成为有价值的反制目标。

然后，他探讨了潜在的响应，从使用fail2ban进行简单的IP过滤，到更激进的策略，如提供解压炸弹和毒害训练数据。 他认为，公开披露此类抓取器行为可以帮助其他人阻止它们。

MacSween提倡数据投毒，强调最近的研究表明，相对少量的中毒样本可以显著损害LLM训练。 他认为数据投毒是对不道德收集数据以训练人工智能模型的合理回应，并鼓励使用免费的数据投毒工具。 他承认在将机器人拦截与数据投毒结合使用时可能存在复杂性，但最终强调需要创造性和积极地破坏大型科技公司的反社会活动。 他最后指出，基于行为怪癖识别机器人并不新鲜，但这种特定的怪癖尚未被广泛讨论。

---

## 5. 香菇菌丝制备的可持续忆阻器用于高频生物电子学

**原文标题**: Sustainable memristors from shiitake mycelium for high-frequency bioelectronics

**原文链接**: [https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0328965](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0328965)

本文探讨了香菇（Lentinula edodes）作为一种可持续且稳健的材料，用于创建神经形态计算忆阻器的潜力。作者证明，香菇菌丝网络可以与电极连接，从而创建可以生长、训练和保存的功能性忆阻器。这些真菌忆阻器在高达5.85 kHz的频率下表现出功能性，且精度很高（90±1%）。

该研究强调了使用真菌材料相对于传统半导体忆阻器的优势，包括可持续性、生物降解性和低功耗潜力。与需要稀土矿物和昂贵制造工艺的传统忆阻器生产不同，香菇提供了一种可扩展、环保的替代方案。真菌的天然成分和适应性为神经网络提供了更自然的模型。

此外，本文强调了香菇的耐辐射性，使其成为航空航天应用的可行选择，在这些应用中，传统电子设备可能会受到损害。作者认为，这种韧性归因于香菇多糖等化合物以及真菌的普遍适应性。通过展示真菌计算机的潜力，该研究连接了生物电子学和非常规计算，为神经形态硬件开发提供了一种新颖的方法。

---

## 6. AMD或将携台积电3纳米工艺声波APU进军ARM市场

**原文标题**: AMD Could Enter ARM Market with Sound Wave APU Built on TSMC 3nm Process

**原文链接**: [https://www.guru3d.com/story/amd-enters-arm-market-with-sound-wave-apu-built-on-tsmc-3nm-process/](https://www.guru3d.com/story/amd-enters-arm-market-with-sound-wave-apu-built-on-tsmc-3nm-process/)

据报道，AMD正在开发其首款基于ARM的APU，代号“声波”，旨在低功耗计算市场与高通骁龙X Elite竞争。泄露的信息显示，它将采用台积电的3纳米工艺制造，目标TDP范围为5W-10W。

“声波”采用BGA-1074封装，适用于移动设备，并且据传将为2026年未来的微软Surface产品提供动力。它采用2+4混合核心设计（两个性能核心和四个效率核心），4MB的三级缓存，以及受AMD GPU Infinity Cache启发的16MB MALL缓存。

该APU集成了四个RDNA 3.5计算单元，用于轻量级游戏和机器学习加速，以及一个128位LPDDR5X-9600内存控制器和16GB的板载RAM，反映了ARM SoC中统一内存的趋势。它还包括AMD的第四代AI引擎，用于设备上的推理任务。

虽然AMD之前曾尝试过ARM，“声波”代表着一种新的、更具战略意义的方式进入ARM市场，利用其在图形和AI方面的优势。预计将于2025年末开始生产，商业设备预计将于2026年上市。

---

## 7. 穿山甲 (YC S25) 正在招聘全栈软件工程师（开源）

**原文标题**: Pangolin (YC S25) Is Hiring a Full Stack Software Engineer (Open-Source)

**原文链接**: [https://docs.pangolin.net/careers/software-engineer-full-stack](https://docs.pangolin.net/careers/software-engineer-full-stack)

穿山甲 (YC S25) 正在招聘全栈软件工程师，以帮助构建和维护其身份感知远程访问平台。该平台专注于安全反向隧道，并正在向零信任网络演进，强调开源原则和自托管。

该职位涉及核心穿山甲容器的工作，包括 UI、API、模式等。工程师将设计、开发和测试前端 (NextJS、Tailwind、ShadCN) 和后端 (Express API、SQL、Drizzle ORM) 的功能，以及从事 CICD 和内部工具等流程。一项关键职责是在 GitHub 和 Discord 等平台上与开源社区互动。

穿山甲希望招聘具有 3 年以上经验、强大的 TypeScript 技能以及一些 Go 经验的候选人。熟悉 Web 身份 (OAuth2、OIDC、SSO)、云基础设施 (Docker、Kubernetes、AWS) 和基本网络概念者优先。他们必须位于旧金山或愿意搬迁。

该职位提供 12.5 万美元至 16 万美元的薪资，外加 0.5% 至 1.5% 的股权、搬迁补助、无限带薪休假以及混合办公环境。招聘流程包括初步面试、带薪开源项目贡献和入职。有意者请在 LinkedIn 上与 Owen 联系，发送简历/CV，并突出显示相关的 GitHub 项目。

---

## 8. 又一欧洲机构摆脱美国科技，数字主权势头渐起

**原文标题**: Another European agency shifts off US Tech as digital sovereignty gains steam

**原文链接**: [https://www.zdnet.com/article/another-european-agency-ditches-big-tech-as-digital-sovereignty-movement-gains-steam/](https://www.zdnet.com/article/another-european-agency-ditches-big-tech-as-digital-sovereignty-movement-gains-steam/)

欧洲政府机构和组织正逐渐摆脱对微软等美国大型科技供应商的依赖，转而采用欧洲本土的开源解决方案，以实现数字主权。例如，奥地利经济部正将其1200名员工迁移到基于Nextcloud的平台，以保障数据安全和控制。此举旨在保护敏感数据、遵守GDPR，并降低与外国监控相关的风险。

非营利组织EuroStack倡议通过推广欧洲科技解决方案来鼓励这一趋势。尽管美国政府对此转变表示担忧，但一些迁移，例如奥地利经济部和交通部（BMWET）的迁移，已取得成功，将开源解决方案与Teams等现有系统相结合。

然而，文章也警告称，仓促的过渡可能会带来问题。奥地利司法部向LibreOffice的过渡就出现了问题，导致文档格式不兼容和用户不满。关键在于，虽然开源解决方案具有增强安全性和控制等优势，但周密的计划和执行对于从专有软件成功迁移至关重要。文章总结道，精心设计的自主云解决方案在公共部门具有实用性和用户友好性。

---

## 9. 约翰·卡马克谈可变变量

**原文标题**: John Carmack on mutable variables

**原文链接**: [https://twitter.com/id_aa_carmack/status/1983593511703474196](https://twitter.com/id_aa_carmack/status/1983593511703474196)

未提供文章内容。文本仅包含：

*   一个标题暗示主题是关于约翰·卡马克对可变变量的看法。
*   一个错误信息，表明JavaScript已禁用，导致页面无法访问。
*   标准的网站页脚信息，例如服务条款、隐私政策等。

由于没有文章的实际内容，因此无法提供摘要。

---

## 10. psutil 的免线程 Python Wheels 包现已可用

**原文标题**: Wheels for free-threaded Python now available for psutil

**原文链接**: [https://gmpy.dev/blog/2025/wheels-for-free-threaded-python-now-available-in-psutil](https://gmpy.dev/blog/2025/wheels-for-free-threaded-python-now-available-in-psutil)

本文宣布自 7.1.2 版本起，`psutil` 提供支持自由线程 Python 的预编译 “wheel” 包。自由线程 Python 自 Python 3.13 起可用，禁用了全局解释器锁（GIL），从而允许在多核处理器上真正并行执行 Python 代码。

这些 wheel 包的开发需要对 `psutil` 的 C 代码进行大量的内部重构，这主要得益于社区的贡献。作者特别感谢 Lysandros Nikolaou 的工作。

本文强调，虽然自由线程 wheel 包的应用正在增长，但它在带有 C 扩展的流行 Python 包中仍然有限。

提供 wheel 包简化了用户的安装过程，特别是对于像 `psutil` 这样严重依赖 C 代码且具有复杂构建要求的包，避免了用户安装 C 编译器和相关工具的需求。

然而，本文也指出了库作者面临的一个挑战：缺乏通用的自由线程 wheel 包。必须为每个 Python 版本（例如 3.13 和 3.14）和平台构建单独的 wheel 包，这大大增加了要分发的文件数量并减慢了测试过程。文中提到了两个提案 PEP 803 和 PEP 809，它们有望在 Python 3.15 中通过启用通用 wheel 包来支持多个 Python 版本，从而解决此问题。

最后，它提供了使用 `pip install psutil --only-binary=:all:` 安装自由线程版本的 `psutil` 的说明。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 2 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 3 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 4 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 5 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 6 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 7 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 8 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 9 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 10 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 11 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 12 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 13 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 14 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 15 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 16 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 17 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 18 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 19 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 20 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 21 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 22 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 23 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 24 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 25 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 26 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 27 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 28 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 29 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 30 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 31 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 32 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 33 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 34 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 35 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 36 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 37 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 38 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 39 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 40 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 41 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 42 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 43 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 44 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 45 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 46 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 47 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 48 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 49 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 50 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 51 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 52 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 53 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 54 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 55 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 56 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 57 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 58 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 59 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 60 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 61 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 62 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 63 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 64 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 65 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 66 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 67 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 68 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 69 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 70 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 71 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 72 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 73 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 74 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 75 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 76 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 77 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 78 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 79 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 80 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 81 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 82 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 83 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 84 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 85 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 86 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 87 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 88 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 89 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 90 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 91 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 92 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 93 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 94 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 95 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 96 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 97 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 98 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 99 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 100 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 101 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 102 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 103 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 104 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 105 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 106 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 107 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 108 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 109 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 110 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 111 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 112 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 113 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 114 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 115 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 116 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 117 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 118 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 119 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 120 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 121 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 122 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 123 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 124 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 125 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 126 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 127 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 128 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 129 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 130 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 131 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 132 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 133 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 134 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 135 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 136 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 137 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 138 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 139 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 140 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 141 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 142 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 143 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 144 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 145 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 146 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 147 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 148 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 149 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 150 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 151 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 152 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 153 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 154 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 155 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 156 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 157 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 158 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 159 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 160 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 161 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 162 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 163 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 164 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 165 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 166 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 167 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 168 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 169 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 170 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 171 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 172 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 173 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 174 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 175 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 176 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 177 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 178 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 179 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 180 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 181 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 182 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 183 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 184 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 185 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 186 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 187 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 188 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 189 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 190 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 191 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 192 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 193 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 194 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 195 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 196 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 197 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 198 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 199 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 200 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 201 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 202 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 203 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 204 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 205 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 206 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 207 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 208 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 209 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 210 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 211 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 212 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 213 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 214 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 215 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 216 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 217 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 218 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 219 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 220 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 221 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 222 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 223 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 224 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 225 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
