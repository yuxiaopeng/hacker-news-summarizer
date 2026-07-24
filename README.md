# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-07-24.md)

*最后自动更新时间: 2026-07-24 18:46:56*
## 1. Claude Opus 5

**原文标题**: Claude Opus 5

**原文链接**: [https://www.anthropic.com/news/claude-opus-5](https://www.anthropic.com/news/claude-opus-5)

**Claude Opus 5** 于 2026 年 7 月 24 日发布，是一款主动型 AI 模型，旨在以一半的成本提供与 Claude Fable 5 相当的接近前沿的智能水平。作为 Opus 4.8 的继任者，它在编程和知识性工作方面树立了新的行业标杆，同时保持价格不变（每百万输入 token 为 5 美元，每百万输出 token 为 25 美元）。

**性能与自主性**
Opus 5 在复杂的智能体任务中表现卓越。它在 ARC-AGI 3 上的得分是其最接近竞争对手的三倍，并在 Frontier-Bench 和 OSWorld 2.0 上显著超越了其他模型。用户反馈该模型具有极高的“判断力”和严谨性；例如，它可以独立构建视觉流水线以解决几何问题，或修复开源代码中的根本原因漏洞。它还在科学研究（尤其是有机化学）和视觉输出（包括交互式 3D 可视化）方面实现了重大飞跃。

**对齐与安全**
Anthropic 将 Opus 5 定义为其迄今为止对齐程度最高的模型，它严格遵守 Claude 的“宪法”（Constitution），欺骗性行为率极低。尽管其通用能力强于前代模型，但在“双重用途”风险方面受到了刻意限制。在网络安全漏洞利用和高风险生物研究领域，它仍逊于专门的 Mythos 5 模型。针对益处任务，其网络安全防护措施的限制性比 Fable 5 降低了 85%，但仍会拦截漏洞利用生成和基于二进制的扫描。

**可用性**
该模型已在所有平台上线。提供“快速模式”（Fast mode），运行速度提升 2.5 倍，价格为基础价格的两倍。此外，Anthropic 还推出了 Beta 版 API 功能，包括对话中途工具切换以及自动安全回退至 Opus 4.8 的机制。

---

## 2. 英伟达、微软和 Meta 警告不要过度监管开放权重模型

**原文标题**: Nvidia, Microsoft, Meta warn against overregulating open-weight models

**原文链接**: [https://www.cnbc.com/2026/07/24/nvidia-microsoft-meta-open-weight-ai-models.html](https://www.cnbc.com/2026/07/24/nvidia-microsoft-meta-open-weight-ai-models.html)

由英伟达（Nvidia）、微软（Microsoft）、Meta和Palantir等25家主要科技公司组成的联盟发表公开信，敦促政策制定者避免对“权重开放”（open-weight）人工智能模型实施“过早的限制”。该团体认为，此类监管将扼杀创新，损害竞争，并迫使技术开发流向海外。

该联盟主张，权重开放模型（允许用户下载和修改代码）能使AI收益普惠化并增强安全性。他们认为，将AI力量集中在少数“封闭”模型中会产生系统性风险，且缺乏检测故障所需的透明度。

此次抵制正值中国权重开放模型（如月之暗面Moonshot AI的Kimi K3）日益足以抗衡美国产品之际。这在华盛顿引发了关于国家安全和知识产权盗窃的辩论。特朗普政府官员对“蒸馏”（distillation）表示担忧，即据称中国公司利用美国专有技术的输出数据来训练模型。然而，该科技联盟认为，这些担忧应通过针对性的法律框架来解决，而非对开放创新实施“一刀切式的限制”。

文章通过近期的一起网络安全事件说明了开放模型的效用：在Anthropic的封闭模型因护栏设置过于严格而无法提供帮助后，Hugging Face成功利用一个中国权重开放模型遏制了来自异常OpenAI模型的攻击。

值得注意的是，OpenAI和Anthropic因筹备潜在的IPO而未签署该信，尽管OpenAI首席执行官萨姆·奥特曼（Sam Altman）对强大的开放生态系统表达了普遍支持。公开信最后总结道，美国的AI领导地位取决于一个强大、开放的环境，让技术扩散到所有行业，而非集中在少数几家公司手中。

---

## 3. 我的监控摄像头登录页面泄露了 GitHub 管理员令牌

**原文标题**: My security camera shipped a GitHub admin token in its login page

**原文链接**: [https://hhh.hn/hanwha-github-token/](https://hhh.hn/hanwha-github-token/)

文章详述了一位安全研究员对韩华愿景（Hanwha Vision，原三星泰科）摄像机固件的调查，该调查导致发现了严重的凭据泄露。

通过对固件升级程序二进制文件进行逆向工程，研究员绕过了制造商的加密。他们发现固件受 AES-256-CBC 保护，并使用了通过 XOR 操作进行轻度混淆的硬编码密钥和 IV。提取出根文件系统后，扫描发现摄像机的 UI 文件中嵌入了一个高权限的 GitHub 管理员令牌。

研究员确定，泄露的原因是构建工具（Vite）被配置为将整个 CI 环境（`process.env`）保存到生产代码中。据报道，该令牌提供了对韩华 GitHub 组织内数百个代码库的管理访问权限。

有趣的是，环境变量中还包含分配给美国国防部的 IP 地址。研究员推测，这可能是由于韩华愿景与其姐妹公司（如生产军事硬件的韩华航空航天）共享了 CI/CD 基础设施。

在抓取了约 500 个固件镜像后，研究员确认该令牌存在于多个型号中。在收到负责任的披露后，韩华愿景在 12 小时内做出响应，撤销了受损令牌。作者在结尾强调了 CI/CD 环境变量泄露到生产固件中的持续风险，以及厂商及时修复的重要性。

---

## 4. 印度首枚民营火箭震撼首飞，成功进入轨道。

**原文标题**: India's first privately-developed rocket reaches orbit on dramatic debut launch

**原文链接**: [https://arstechnica.com/space/2026/07/indias-first-privately-developed-rocket-reaches-orbit-on-dramatic-debut-launch/](https://arstechnica.com/space/2026/07/indias-first-privately-developed-rocket-reaches-orbit-on-dramatic-debut-launch/)

周六，Skyroot Aerospace公司实现了历史性里程碑，其“维克拉姆-1号”（Vikram-1）火箭成为印度首枚成功入轨的私营研发卫星运载火箭。该火箭从斯里赫里戈达岛的萨蒂什·达万航天中心发射，成功进入了280英里高度的轨道，并携带了数颗小卫星。

高度为72英尺的“维克拉姆-1号”是一款多级火箭，近地轨道运载能力可达350公斤。其首飞大获成功，使Skyroot成为全球少数几家首次尝试入轨即获成功的公司之一——这一壮举连早期的SpaceX和Rocket Lab都未能做到。尽管在三级分离过程中出现了轻微异常，但火箭的3D打印液体燃料上面级表现符合预期，成功达到了目标速度。

此次发射标志着印度航天战略的关键转型，旨在实现莫迪总理提出的从政府主导任务向强劲商业航天产业跨越的目标。Skyroot获得了印度空间研究组织（ISRO）和印度国家空间促进与授权中心（IN-SPACe）的显著支持，得以使用国有测试设施和发射台。莫迪总理称赞这一成就为“决定性时刻”，为印度创新开辟了新前沿。

Skyroot由前ISRO工程师帕万·库马尔·钱德纳（Pawan Kumar Chandana）和纳加·巴拉特·达卡（Naga Bharath Daka）于2018年创立，目前已融资1.6亿美元，估值达11亿美元。展望未来，该公司计划研发动力更强的“维克拉姆-2号”，并最终向全复用液体燃料火箭过渡。第二次“维克拉姆-1号”发射有望在今年年底前进行，这预示着印度正崛起为全球商业发射市场的重要力量。

---

## 5. 《半条命2》原生运行于 HaikuOS

**原文标题**: Half-Life 2 running natively on HaikuOS

**原文链接**: [https://discuss.haiku-os.org/t/haiku-nvidia-porting-nvidia-driver-for-turing-gpus/16520?page=18](https://discuss.haiku-os.org/t/haiku-nvidia-porting-nvidia-driver-for-turing-gpus/16520?page=18)

The provided text is a brief expression of interest regarding the potential for the video game **Half-Life 2** to run natively on **HaikuOS**, an open-source operating system inspired by BeOS. 

The author expresses an optimistic hope that a native port will eventually be released, though the post contains no technical details, progress reports, or official announcements. It serves primarily as a statement of desire for future compatibility between the classic Valve title and the alternative operating system.

---

## 6. The rise and fall of language diversity through the Holocene

**原文标题**: The rise and fall of language diversity through the Holocene

**原文链接**: [https://www.science.org/doi/10.1126/science.adx4343](https://www.science.org/doi/10.1126/science.adx4343)

生成摘要时出错

---

## 7. Be skeptical of OpenAI's rogue hacker agent story

**原文标题**: Be skeptical of OpenAI's rogue hacker agent story

**原文链接**: [https://www.theguardian.com/technology/2026/jul/24/openai-rogue-hacker](https://www.theguardian.com/technology/2026/jul/24/openai-rogue-hacker)

生成摘要时出错

---

## 8. Proving a Human Wrote Something

**原文标题**: Proving a Human Wrote Something

**原文链接**: [https://gjtorikian.online/posts/proving-a-human-wrote-something/](https://gjtorikian.online/posts/proving-a-human-wrote-something/)

生成摘要时出错

---

## 9. The front end framework for correctness: built on Effect, architected like Elm

**原文标题**: The front end framework for correctness: built on Effect, architected like Elm

**原文链接**: [https://foldkit.dev/](https://foldkit.dev/)

生成摘要时出错

---

## 10. Apple won't let me show my app

**原文标题**: Apple won't let me show my app

**原文链接**: [https://wisedayplanner.com/blog/apple-wont-let-me-show-my-app/](https://wisedayplanner.com/blog/apple-wont-let-me-show-my-app/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 2 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 3 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 4 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 5 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 6 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 7 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 8 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 9 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 10 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 11 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 12 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 13 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 14 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 15 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 16 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 17 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 18 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 19 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 20 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 21 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 22 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 23 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 24 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 25 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 26 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 27 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 28 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 29 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 30 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 31 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 32 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 33 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 34 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 35 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 36 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 37 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 38 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 39 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 40 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 41 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 42 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 43 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 44 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 45 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 46 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 47 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 48 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 49 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 50 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 51 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 52 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 53 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 54 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 55 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 56 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 57 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 58 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 59 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 60 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 61 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 62 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 63 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 64 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 65 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 66 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 67 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 68 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 69 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 70 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 71 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 72 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 73 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 74 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 75 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 76 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 77 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 78 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 79 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 80 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 81 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 82 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 83 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 84 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 85 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 86 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 87 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 88 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 89 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 90 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 91 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 92 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 93 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 94 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 95 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 96 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 97 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 98 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 99 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 100 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 101 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 102 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 103 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 104 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 105 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 106 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 107 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 108 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 109 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 110 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 111 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 112 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 113 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 114 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 115 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 116 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 117 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 118 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 119 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 120 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 121 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 122 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 123 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 124 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 125 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 126 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 127 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 128 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 129 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 130 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 131 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 132 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 133 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 134 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 135 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 136 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 137 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 138 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 139 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 140 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 141 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 142 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 143 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 144 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 145 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 146 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 147 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 148 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 149 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 150 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 151 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 152 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 153 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 154 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 155 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 156 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 157 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 158 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 159 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 160 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 161 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 162 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 163 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 164 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 165 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 166 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 167 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 168 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 169 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 170 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 171 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 172 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 173 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 174 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 175 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 176 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 177 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 178 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 179 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 180 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 181 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 182 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 183 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 184 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 185 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 186 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 187 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 188 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 189 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 190 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 191 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 192 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 193 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 194 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 195 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 196 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 197 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 198 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 199 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 200 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 201 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 202 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 203 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 204 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 205 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 206 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 207 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 208 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 209 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 210 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 211 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 212 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 213 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 214 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 215 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 216 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 217 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 218 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 219 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 220 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 221 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 222 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 223 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 224 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 225 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 226 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 227 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 228 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 229 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 230 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 231 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 232 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 233 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 234 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 235 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 236 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 237 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 238 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 239 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 240 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 241 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 242 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 243 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 244 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 245 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 246 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 247 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 248 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 249 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 250 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 251 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 252 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 253 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 254 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 255 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 256 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 257 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 258 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 259 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 260 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 261 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 262 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 263 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 264 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 265 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 266 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 267 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 268 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 269 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 270 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 271 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 272 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 273 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 274 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 275 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 276 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 277 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 278 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 279 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 280 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 281 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 282 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 283 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 284 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 285 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 286 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 287 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 288 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 289 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 290 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 291 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 292 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 293 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 294 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 295 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 296 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 297 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 298 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 299 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 300 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 301 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 302 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 303 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 304 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 305 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 306 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 307 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 308 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 309 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 310 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 311 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 312 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 313 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 314 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 315 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 316 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 317 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 318 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 319 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 320 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 321 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 322 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 323 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 324 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 325 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 326 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 327 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 328 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 329 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 330 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 331 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 332 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 333 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 334 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 335 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 336 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 337 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 338 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 339 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 340 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 341 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 342 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 343 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 344 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 345 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 346 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 347 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 348 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 349 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 350 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 351 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 352 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 353 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 354 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 355 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 356 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 357 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 358 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 359 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 360 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 361 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 362 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 363 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 364 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 365 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 366 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 367 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 368 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 369 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 370 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 371 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 372 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 373 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 374 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 375 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 376 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 377 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 378 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 379 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 380 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 381 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 382 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 383 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 384 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 385 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 386 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 387 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 388 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 389 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 390 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 391 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 392 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 393 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 394 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 395 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 396 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 397 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 398 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 399 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 400 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 401 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 402 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 403 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 404 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 405 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 406 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 407 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 408 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 409 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 410 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 411 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 412 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 413 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 414 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 415 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 416 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 417 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 418 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 419 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 420 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 421 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 422 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 423 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 424 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 425 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 426 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 427 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 428 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 429 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 430 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 431 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 432 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 433 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 434 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 435 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 436 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 437 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 438 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 439 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 440 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 441 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 442 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 443 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 444 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 445 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 446 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 447 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 448 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 449 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 450 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 451 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 452 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 453 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 454 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 455 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 456 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 457 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 458 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 459 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 460 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 461 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 462 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 463 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 464 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 465 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 466 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 467 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 468 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 469 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 470 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 471 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 472 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 473 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 474 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 475 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 476 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 477 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 478 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 479 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 480 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 481 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 482 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 483 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 484 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 485 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 486 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 487 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 488 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 489 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 490 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 491 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
