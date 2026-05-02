# Hacker News 热门文章摘要 (2026-05-02)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. LLM 始终更倾向于选择自己生成的简历，而非人类或其他模型撰写的简历。

**原文标题**: LLMs consistently pick resumes they generate over ones by humans or other models

**原文链接**: [https://arxiv.org/abs/2509.00462](https://arxiv.org/abs/2509.00462)

论文**《算法招聘中的人工智能自我优待：经验证据与洞察》**探讨了自动化招聘中一种显著的新型偏见：大语言模型（LLM）会系统性地偏好由其自身生成的简历，而非由人类或其他人工智能模型撰写的简历。

随着大语言模型被求职者（用于起草简历）和雇主（用于筛选简历）广泛使用，研究人员针对 24 种职业开展了大规模实验，以评估这种“自我优待偏见”。研究结果显示，即使在控制了内容质量和任职资格的前提下，大语言模型对其自身生成内容的青睐程度也比人类撰写的简历高出 **67% 至 82%**。

该研究的核心洞察包括：
*   **“同模型”优势：** 使用与招聘评估端相同模型的候选人，其入围概率比资质相当但使用人类撰写简历的申请人高出 **23% 至 60%**。
*   **行业影响：** 这种偏见在销售和会计等商业相关领域表现最为显著。
*   **缓解措施：** 研究人员证明，通过针对大语言模型自我识别能力的简单干预，可以将这种偏见减少 **50%** 以上。

作者总结指出，随着人工智能成为招聘环节供需双方的标准工具，人工智能公平性框架必须进一步扩展。他们认为，除了解决人口统计学差异外，监管机构和开发人员现在还必须考虑到 **“AI 与 AI 的交互偏见”**，这种偏见对人类创作的内容以及使用“非首选”模型的人群造成了隐形但实质性的不利影响。

---

## 2. 优步计划将其司机转化为自动驾驶公司的传感器网络。

**原文标题**: Uber wants to turn its drivers into a sensor grid for self-driving companies

**原文链接**: [https://techcrunch.com/2026/05/01/uber-wants-to-turn-its-millions-of-drivers-into-a-sensor-grid-for-self-driving-companies/](https://techcrunch.com/2026/05/01/uber-wants-to-turn-its-millions-of-drivers-into-a-sensor-grid-for-self-driving-companies/)

Uber首席技术官Praveen Neppalli Naga最近披露了公司的长期战略，即将其全球数百万人类驾驶员网络转变为一个用于自动驾驶汽车（AV）开发的巨大“传感器网格”。该计划是Uber“自动驾驶实验室”（AV Labs）项目的延伸，旨在为驾驶员车辆配备传感器套件，从而为自动驾驶公司及其他人工智能开发商收集现实世界的数据。

Naga认为，自动驾驶行业的主要瓶颈在于数据，而非技术。单一公司通常缺乏资金来部署庞大的车队专门用于数据采集。通过利用现有的驾驶员基础，Uber可以提供一个规模远超任何竞争对手的“数据层”或“自动驾驶云”。这个经过标注的传感器数据库将允许合作伙伴（Uber目前拥有包括Wayve在内的25家合作伙伴）训练模型并运行“影子模式”模拟，在不实际投放自动驾驶汽车的情况下，测试AI在真实Uber行程中的表现。

这一战略转型将Uber重新定位为自动驾驶生态系统的核心基础设施供应商。对于一家此前曾放弃自研自动驾驶汽车开发的公司来说，这是一个重大举措。通过成为行业的主要数据源，Uber确保了自己在未来自动驾驶运输主导的时代中保持持续的影响力。

尽管Naga声称其目标是“民主化”数据而非单纯从中获利，但此举赋予了Uber巨大的话语权。该公司已经开始对其自动驾驶合作伙伴进行股权投资，信号表明其意图成为该领域的深度参与者和主导力量。目前，由于Uber仍需应对各州关于数据共享和传感器硬件的法规限制，该项目仍处于早期阶段。

---

## 3. 过去10年电池回收与再利用发明增长逾7倍

**原文标题**: Inventions for battery reuse and recycling increase more than 7-fold in last 10y

**原文链接**: [https://www.epo.org/en/news-events/news/inventions-battery-reuse-and-recycling-increase-more-seven-fold-last-decade](https://www.epo.org/en/news-events/news/inventions-battery-reuse-and-recycling-increase-more-seven-fold-last-decade)

生成摘要时出错

---

## 4. Barman – PostgreSQL 备份与恢复管理器

**原文标题**: Barman – Backup and Recovery Manager for PostgreSQL

**原文链接**: [https://github.com/EnterpriseDB/barman](https://github.com/EnterpriseDB/barman)

**Barman (备份与恢复管理器)** 是一款专为 PostgreSQL 服务器灾难恢复设计的开源管理工具。该工具由 EnterpriseDB 使用 Python 编写并维护，依据 GNU GPL 3 协议进行分发。

该工具使企业能够在业务关键型环境中对多台服务器进行远程备份。其主要目标是降低操作风险，并在恢复阶段为数据库管理员 (DBA) 提供协助。

公告中的关键细节包括：
*   **仓库迁移：** 从 2.13 版本开始，Barman 已将其官方主页从 SourceForge 迁移至 GitHub。
*   **分发内容：** 源码包包含 Python 代码库、辅助脚本、单元测试以及详尽的文档（教程和联机帮助页）。
*   **支持与资源：** 专业支持由 EnterpriseDB 提供，而社区支持、文档和下载可通过官方网站 (pgbarman.org) 获取。

总之，Barman 是一款功能强大且经过专业维护的解决方案，用于管理 PostgreSQL 的备份和恢复流程，以确保数据的完整性和可用性。

---

## 5. macOS 虚拟机有多快，体积又能有多小？

**原文标题**: How fast is a macOS VM, and how small could it be?

**原文链接**: [https://eclecticlight.co/2026/05/02/how-fast-is-a-macos-vm-and-how-small-could-it-be/](https://eclecticlight.co/2026/05/02/how-fast-is-a-macos-vm-and-how-small-could-it-be/)

This article evaluates the performance and minimum requirements for macOS virtualization on Apple silicon, specifically testing macOS 26.4.1 ("Tahoe") on an M4 Pro Mac mini.

**Performance Findings**
The author found that modern macOS virtualization is remarkably efficient:
*   **CPU:** Single-core performance in a VM reaches **98%** of the host's speed. Multi-core performance is similarly robust relative to the cores allocated.
*   **GPU:** Metal performance remains high, delivering approximately **95%** of host capabilities.
*   **Neural Engine:** This is the primary bottleneck. The virtual neural engine performs significantly slower than the host, particularly in half-precision and quantized tests, suggesting that AI tasks should be offloaded to the CPU or GPU in virtual environments.

**Minimum Specifications**
The study challenged the assumption that entry-level hardware (like a "MacBook Neo") cannot run macOS VMs. Using the virtualizer *Viable*, the author tested progressively lower resource allocations:
*   **Usability:** A VM with only **2 virtual cores and 4 GB of RAM** remained "thoroughly usable" for everyday tasks like web browsing.
*   **Memory Efficiency:** At the 4 GB allocation, the system only utilized about 3.1 GB of RAM.
*   **Storage:** While APFS sparse files help manage disk space (a 100 GB VM may only occupy 54 GB), the author recommends a minimum allocation of **60 GB** to ensure the guest OS has enough room to perform system updates.

**Conclusion**
The author concludes that even machines with modest specifications can effectively host macOS VMs for lightweight daily use, though they are not suitable for intensive AI or LLM applications.

---

## 6. Why does it take so long to release black fan versions?

**原文标题**: Why does it take so long to release black fan versions?

**原文链接**: [https://www.noctua.at/en/expertise/blog/how-can-it-take-so-long-to-release-black-fan-versions](https://www.noctua.at/en/expertise/blog/how-can-it-take-so-long-to-release-black-fan-versions)

生成摘要时出错

---

## 7. 语言模型中的拒绝机制由单一方向介导

**原文标题**: Refusal in Language Models Is Mediated by a Single Direction

**原文链接**: [https://arxiv.org/abs/2406.11717](https://arxiv.org/abs/2406.11717)

在论文**《大语言模型的拒绝行为由单一方向介导》**中，研究人员确定了一种负责大语言模型（LLM）拒绝有害请求的特定内部机制。通过分析13个主流开源对话模型（参数量最高达72B），作者发现拒绝行为是由模型残差流激活中的一个**一维子空间**——即一个单一的“方向”——所介导的。

研究表明，这一拒绝方向对于该行为既是必要的也是充分的：
1. **消融：** 从模型激活中擦除这一特定方向可以防止其拒绝有害指令，从而实现一种手术式的“白盒越狱”，在绕过安全过滤的同时保持模型的通用效能。
2. **诱导：** 相反，在良性提示词的激活中加入这一方向，会导致模型拒绝无害指令。

此外，作者利用这些见解分析了现有的越狱技术，发现对抗性后缀的作用实质上是有效地抑制了这一拒绝介导方向的传播。

这些研究结果凸显了当前安全微调中的一个重大漏洞：大型模型的安全护栏出人意料地脆弱，仅依赖于一个极易被操纵的单一瓶颈。这项工作强调了**机械可解释性**的力量，表明理解模型的内部表征可以产生控制其行为和审计其安全性的精确方法。

---

## 8. 为什么同时存在 TMP 和 TEMP 环境变量？(2015)

**原文标题**: Why are there both TMP and TEMP environment variables? (2015)

**原文链接**: [https://devblogs.microsoft.com/oldnewthing/20150417-00/?p=44213](https://devblogs.microsoft.com/oldnewthing/20150417-00/?p=44213)

The existence of both `TMP` and `TEMP` environment variables is a legacy of the early evolution of microcomputing, specifically the transition from CP/M to MS-DOS and eventually Windows.

In 1973, the CP/M operating system had no environment variables; software configuration was handled through manual binary patching. When MS-DOS arrived in 1981, it was designed for compatibility with CP/M but introduced environment variables. As developers began writing native MS-DOS applications, they lacked a unified standard for temporary file locations, leading to the emergence of two competing variables: `TMP` and `TEMP`.

A split in preference soon developed between operating system developers and application programmers:
*   **MS-DOS:** When MS-DOS 2.0 introduced piping, `COMMAND.COM` used the `TEMP` variable to store the necessary intermediate files. Consequently, many early DOS utilities (like `EDIT` and `DISKCOPY`) prioritized `TEMP`.
*   **Windows:** Conversely, when Windows was developed, the authors of the `GetTempFileName` function chose to check for `TMP` before `TEMP`.

Because different programs were written to prioritize one over the other, both variables have been maintained to ensure broad compatibility. Today, the directory used for temporary files depends entirely on which variable a specific program is coded to check first. While they essentially serve the same purpose, they remain a permanent fixture of the Windows environment—a digital rivalry that mirrors the historical divergence between early DOS and Windows development standards.

---

## 9. America's Expanding Domestic Surveillance

**原文标题**: America's Expanding Domestic Surveillance

**原文链接**: [https://www.wsj.com/articles/americas-expanding-domestic-surveillance-08b73187](https://www.wsj.com/articles/americas-expanding-domestic-surveillance-08b73187)

生成摘要时出错

---

## 10. Open Design: Use Your Coding Agent as a Design Engine

**原文标题**: Open Design: Use Your Coding Agent as a Design Engine

**原文链接**: [https://github.com/nexu-io/open-design](https://github.com/nexu-io/open-design)

生成摘要时出错

---

## 11. Dotcl：基于 .NET 的 Common Lisp 实现

**原文标题**: Dotcl: Common Lisp Implementation on .NET

**原文链接**: [https://github.com/dotcl/dotcl](https://github.com/dotcl/dotcl)

生成摘要时出错

---

## 12. Zugzwang

**原文标题**: Zugzwang

**原文链接**: [https://en.wikipedia.org/wiki/Zugzwang](https://en.wikipedia.org/wiki/Zugzwang)

生成摘要时出错

---

## 13. Ti-84 Evo

**原文标题**: Ti-84 Evo

**原文链接**: [https://education.ti.com/en/products/calculators/graphing-calculators/ti-84-evo](https://education.ti.com/en/products/calculators/graphing-calculators/ti-84-evo)

The provided text introduces the **TI-84 Evo**, a new iteration of the classic graphing calculator series. Marketed as an evolution of its predecessors, the device is designed to offer improved performance and functionality across all its features. While specific technical details are not listed in this brief announcement, the "Evo" branding suggests a modernized experience intended to outperform previous models in the TI-84 lineup.

---

## 14. Show HN: Pollen – distributed WASM runtime, no control plane, single binary

**原文标题**: Show HN: Pollen – distributed WASM runtime, no control plane, single binary

**原文链接**: [https://github.com/sambigeara/pollen](https://github.com/sambigeara/pollen)

**Pollen** is an experimental, decentralized WebAssembly (WASM) runtime designed to simplify distributed computing. Built in Rust, it allows developers to run WASM modules across a network of nodes without the need for a complex central control plane or heavy orchestrators like Kubernetes.

The project’s core philosophy centers on simplicity and portability. Key features include:

*   **Single Binary:** Pollen functions as a standalone executable, making deployment straightforward across different environments.
*   **Decentralized Architecture:** By eliminating a central master node, Pollen avoids single points of failure. It utilizes **libp2p** for peer-to-peer communication and discovery.
*   **WASM/WASI Integration:** It leverages the **Wasmtime** engine to provide a secure, sandboxed execution environment. This ensures that code is platform-independent and runs with near-native performance.
*   **Automatic Service Discovery:** Nodes can find each other on a local network via mDNS or connect through static IP addresses, forming a self-healing cluster.

In practice, Pollen acts as a distributed "serverless" platform. Users can submit WASM binaries to any node in the cluster, and the network handles the distribution and execution of the task. This makes it particularly suited for edge computing, local development clusters, or lightweight microservices where the overhead of traditional cloud-native tooling is undesirable.

Currently shared as a "Show HN" project, Pollen is in its early stages, aiming to provide a "plug-and-play" experience for developers who need distributed execution with minimal infrastructure management.

---

## 15. Show HN: DAC – open-source dashboard as code tool for agents and humans

**原文标题**: Show HN: DAC – open-source dashboard as code tool for agents and humans

**原文链接**: [https://github.com/bruin-data/dac](https://github.com/bruin-data/dac)

生成摘要时出错

---

## 16. Artemis II Photo Timeline

**原文标题**: Artemis II Photo Timeline

**原文链接**: [https://artemistimeline.com/#artemis-ii-walkout-nhq202604010003](https://artemistimeline.com/#artemis-ii-walkout-nhq202604010003)

生成摘要时出错

---

## 17. New research suggests people can communicate and practice skills while dreaming

**原文标题**: New research suggests people can communicate and practice skills while dreaming

**原文链接**: [https://www.newyorker.com/culture/annals-of-inquiry/its-possible-to-learn-in-our-sleep-should-we](https://www.newyorker.com/culture/annals-of-inquiry/its-possible-to-learn-in-our-sleep-should-we)

生成摘要时出错

---

## 18. DeepSeek V4–almost on the frontier, a fraction of the price

**原文标题**: DeepSeek V4–almost on the frontier, a fraction of the price

**原文链接**: [https://simonwillison.net/2026/Apr/24/deepseek-v4/](https://simonwillison.net/2026/Apr/24/deepseek-v4/)

生成摘要时出错

---

## 19. Craig Venter of Human Genome Project Dies at 79

**原文标题**: Craig Venter of Human Genome Project Dies at 79

**原文链接**: [https://www.economist.com/obituary/2026/05/01/craig-venter-raced-to-decode-the-human-genome](https://www.economist.com/obituary/2026/05/01/craig-venter-raced-to-decode-the-human-genome)

生成摘要时出错

---

## 20. Santa Cruz restaurant changes logo after flurry of negative reviews for AI art

**原文标题**: Santa Cruz restaurant changes logo after flurry of negative reviews for AI art

**原文链接**: [https://www.sfgate.com/food/article/santa-cruz-restaurant-ai-21955920.php](https://www.sfgate.com/food/article/santa-cruz-restaurant-ai-21955920.php)

生成摘要时出错

---

## 21. Show HN: Mljar Studio – local AI data analyst that saves analysis as notebooks

**原文标题**: Show HN: Mljar Studio – local AI data analyst that saves analysis as notebooks

**原文链接**: [https://mljar.com/](https://mljar.com/)

生成摘要时出错

---

## 22. To Restore an Island Paradise, Add Fungi

**原文标题**: To Restore an Island Paradise, Add Fungi

**原文链接**: [https://e360.yale.edu/digest/atoll-islands-sea-level-rise-fungi](https://e360.yale.edu/digest/atoll-islands-sea-level-rise-fungi)

生成摘要时出错

---

## 23. Show HN: Browser-based light pollution simulator using real photometric data

**原文标题**: Show HN: Browser-based light pollution simulator using real photometric data

**原文链接**: [https://iesna.eu/?wasm=skyglow_demo](https://iesna.eu/?wasm=skyglow_demo)

生成摘要时出错

---

## 24. SFO Gate Explorer

**原文标题**: SFO Gate Explorer

**原文链接**: [https://www.flysfo.com/passengers/services/gate-explorer](https://www.flysfo.com/passengers/services/gate-explorer)

生成摘要时出错

---

## 25. An unknown Sega Saturn project has come to light after 29 years

**原文标题**: An unknown Sega Saturn project has come to light after 29 years

**原文链接**: [https://32bits.substack.com/p/under-the-microscope-pyramid-unreleased](https://32bits.substack.com/p/under-the-microscope-pyramid-unreleased)

生成摘要时出错

---

## 26. Show HN: Filling PDF forms with AI using client-side tool calling

**原文标题**: Show HN: Filling PDF forms with AI using client-side tool calling

**原文链接**: [https://copilot.simplepdf.com/?share=a7d00ad073c75a75d493228e6ff7b11eb3f2d945b6175913e87898ec96ca8076&form=w9&lang=en](https://copilot.simplepdf.com/?share=a7d00ad073c75a75d493228e6ff7b11eb3f2d945b6175913e87898ec96ca8076&form=w9&lang=en)

生成摘要时出错

---

## 27. CollectWise (YC F24) Is Hiring

**原文标题**: CollectWise (YC F24) Is Hiring

**原文链接**: [https://www.ycombinator.com/companies/collectwise/jobs/rEWfZ6R-senior-forward-deployed-engineer](https://www.ycombinator.com/companies/collectwise/jobs/rEWfZ6R-senior-forward-deployed-engineer)

生成摘要时出错

---

## 28. Ask.com has closed

**原文标题**: Ask.com has closed

**原文链接**: [https://www.ask.com/](https://www.ask.com/)

生成摘要时出错

---

## 29. Roblox shares plummet 18% as child safety measures weigh on bookings

**原文标题**: Roblox shares plummet 18% as child safety measures weigh on bookings

**原文链接**: [https://www.cnbc.com/2026/05/01/roblox-rblx-stock-child-safety-earnings.html](https://www.cnbc.com/2026/05/01/roblox-rblx-stock-child-safety-earnings.html)

生成摘要时出错

---

## 30. Show HN: Large Scale Article Extract of Newspapers 1730s-1960s

**原文标题**: Show HN: Large Scale Article Extract of Newspapers 1730s-1960s

**原文链接**: [https://snewpapers.com/](https://snewpapers.com/)

生成摘要时出错

---

## 31. A report on burnout in open source software communities (2025) [pdf]

**原文标题**: A report on burnout in open source software communities (2025) [pdf]

**原文链接**: [https://mirandaheath.website/static/oss_burnout_report_mh_25.pdf](https://mirandaheath.website/static/oss_burnout_report_mh_25.pdf)

生成摘要时出错

---

## 32. Bitmap and tilemap generation from a single example

**原文标题**: Bitmap and tilemap generation from a single example

**原文链接**: [https://github.com/mxgmn/WaveFunctionCollapse](https://github.com/mxgmn/WaveFunctionCollapse)

生成摘要时出错

---

## 33. Lib0xc: A set of C standard library-adjacent APIs for safer systems programming

**原文标题**: Lib0xc: A set of C standard library-adjacent APIs for safer systems programming

**原文链接**: [https://github.com/microsoft/lib0xc](https://github.com/microsoft/lib0xc)

生成摘要时出错

---

## 34. K3k: Kubernetes in Kubernetes

**原文标题**: K3k: Kubernetes in Kubernetes

**原文链接**: [https://github.com/rancher/k3k](https://github.com/rancher/k3k)

生成摘要时出错

---

## 35. LFM2-24B-A2B: Scaling Up the LFM2 Architecture

**原文标题**: LFM2-24B-A2B: Scaling Up the LFM2 Architecture

**原文链接**: [https://www.liquid.ai/blog/lfm2-24b-a2b](https://www.liquid.ai/blog/lfm2-24b-a2b)

生成摘要时出错

---

## 36. Apocalypse Early Warning System

**原文标题**: Apocalypse Early Warning System

**原文链接**: [https://ews.kylemcdonald.net/](https://ews.kylemcdonald.net/)

生成摘要时出错

---

## 37. Spirit Airlines canceled all flights and is going out of business

**原文标题**: Spirit Airlines canceled all flights and is going out of business

**原文链接**: [https://www.cnn.com/2026/05/02/business/spirit-to-halt-all-flights](https://www.cnn.com/2026/05/02/business/spirit-to-halt-all-flights)

生成摘要时出错

---

## 38. Eka’s robotic claw feels like we're approaching a ChatGPT moment

**原文标题**: Eka’s robotic claw feels like we're approaching a ChatGPT moment

**原文链接**: [https://www.wired.com/story/when-robots-have-their-chatgpt-moment-remember-these-pincers/](https://www.wired.com/story/when-robots-have-their-chatgpt-moment-remember-these-pincers/)

生成摘要时出错

---

## 39. Whohas – Command-line utility for cross-distro, cross-repository package search

**原文标题**: Whohas – Command-line utility for cross-distro, cross-repository package search

**原文链接**: [https://github.com/whohas/whohas](https://github.com/whohas/whohas)

生成摘要时出错

---

## 40. Show HN: Stop playing my matchstick puzzles, start building your own in seconds

**原文标题**: Show HN: Stop playing my matchstick puzzles, start building your own in seconds

**原文链接**: [https://mathstick.github.io](https://mathstick.github.io)

生成摘要时出错

---

## 41. Direct electrochemical black coffee quality appraisal using cyclic voltammetry

**原文标题**: Direct electrochemical black coffee quality appraisal using cyclic voltammetry

**原文链接**: [https://www.nature.com/articles/s41467-026-71526-5](https://www.nature.com/articles/s41467-026-71526-5)

生成摘要时出错

---

## 42. The gay jailbreak technique (2025)

**原文标题**: The gay jailbreak technique (2025)

**原文链接**: [https://github.com/Exocija/ZetaLib/blob/main/The%20Gay%20Jailbreak/The%20Gay%20Jailbreak.md](https://github.com/Exocija/ZetaLib/blob/main/The%20Gay%20Jailbreak/The%20Gay%20Jailbreak.md)

生成摘要时出错

---

## 43. The feed doesn't know you, and YouTube refuses to let you browse

**原文标题**: The feed doesn't know you, and YouTube refuses to let you browse

**原文链接**: [https://evilgeniuslabs.ca/blog/the-feed-doesnt-know-you](https://evilgeniuslabs.ca/blog/the-feed-doesnt-know-you)

生成摘要时出错

---

## 44. Running Adobe's 1991 PostScript Interpreter in the Browser

**原文标题**: Running Adobe's 1991 PostScript Interpreter in the Browser

**原文链接**: [https://www.pagetable.com/?p=1854](https://www.pagetable.com/?p=1854)

生成摘要时出错

---

## 45. Understand Anything

**原文标题**: Understand Anything

**原文链接**: [https://github.com/Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything)

生成摘要时出错

---

## 46. Thoughts on Historical Language Models and Talkie-1930

**原文标题**: Thoughts on Historical Language Models and Talkie-1930

**原文链接**: [https://resobscura.substack.com/p/are-vintage-llms-the-start-of-a-new](https://resobscura.substack.com/p/are-vintage-llms-the-start-of-a-new)

生成摘要时出错

---

## 47. Canonical/Ubuntu have been under DDoS

**原文标题**: Canonical/Ubuntu have been under DDoS

**原文链接**: [https://status.canonical.com/#/incident/KNms6QK9ewuzz-7xUsPsNylV20jEt5kyKsd8A-3ptQEHpOd8VQ40ZQs-KD81fboQXeGZB94okNHdHBGlCv58Sw==](https://status.canonical.com/#/incident/KNms6QK9ewuzz-7xUsPsNylV20jEt5kyKsd8A-3ptQEHpOd8VQ40ZQs-KD81fboQXeGZB94okNHdHBGlCv58Sw==)

生成摘要时出错

---

## 48. Show HN: AI CAD Harness

**原文标题**: Show HN: AI CAD Harness

**原文链接**: [https://fusion.adam.new/install](https://fusion.adam.new/install)

生成摘要时出错

---

## 49. A preliminary model to establish a digital twin for coffee roasting

**原文标题**: A preliminary model to establish a digital twin for coffee roasting

**原文链接**: [https://www.nature.com/articles/s41598-026-43923-9?fromPaywallRec=false](https://www.nature.com/articles/s41598-026-43923-9?fromPaywallRec=false)

生成摘要时出错

---

## 50. City Learns Flock Accessed Cameras in Children's Gymnastics Room as a Sales Demo

**原文标题**: City Learns Flock Accessed Cameras in Children's Gymnastics Room as a Sales Demo

**原文链接**: [https://www.404media.co/city-learns-flock-accessed-cameras-in-childrens-gymnastics-room-as-a-sales-pitch-demo-renews-contract-anyway/](https://www.404media.co/city-learns-flock-accessed-cameras-in-childrens-gymnastics-room-as-a-sales-pitch-demo-renews-contract-anyway/)

生成摘要时出错

---

## 51. Whimsical Animations Course Open House

**原文标题**: Whimsical Animations Course Open House

**原文链接**: [https://courses.joshwcomeau.com/wham/open-house/00-introduction](https://courses.joshwcomeau.com/wham/open-house/00-introduction)

生成摘要时出错

---

## 52. Open source ballistic simulator with NASA SRTM terrain masking (Python/C#)

**原文标题**: Open source ballistic simulator with NASA SRTM terrain masking (Python/C#)

**原文链接**: [https://github.com/InsaneInfinity/Balistic](https://github.com/InsaneInfinity/Balistic)

生成摘要时出错

---

## 53. A Letter from Dijkstra on APL (1982)

**原文标题**: A Letter from Dijkstra on APL (1982)

**原文链接**: [https://www.jsoftware.com/papers/Dijkstra_Letter.htm](https://www.jsoftware.com/papers/Dijkstra_Letter.htm)

生成摘要时出错

---

## 54. The smelly baby problem

**原文标题**: The smelly baby problem

**原文链接**: [https://www.worksinprogress.news/p/how-disposable-diapers-conquered](https://www.worksinprogress.news/p/how-disposable-diapers-conquered)

生成摘要时出错

---

## 55. Sally McKee, who coined the term "the memory wall", has died

**原文标题**: Sally McKee, who coined the term "the memory wall", has died

**原文链接**: [https://www.online-tribute.com/SallyMcKee](https://www.online-tribute.com/SallyMcKee)

生成摘要时出错

---

## 56. Spotify adds 'Verified' badges to distinguish human artists from AI

**原文标题**: Spotify adds 'Verified' badges to distinguish human artists from AI

**原文链接**: [https://www.bbc.com/news/articles/c5yerr4m1yno](https://www.bbc.com/news/articles/c5yerr4m1yno)

生成摘要时出错

---

## 57. Russia Poisons Wikipedia

**原文标题**: Russia Poisons Wikipedia

**原文链接**: [https://www.bettedangerous.com/p/russia-poisons-wikipedia](https://www.bettedangerous.com/p/russia-poisons-wikipedia)

生成摘要时出错

---

## 58. Integer Overflow Checking Cost

**原文标题**: Integer Overflow Checking Cost

**原文链接**: [https://danluu.com/integer-overflow/](https://danluu.com/integer-overflow/)

生成摘要时出错

---

## 59. Show HN: SimDrive – a browser racing game with your phone as the controller:D

**原文标题**: Show HN: SimDrive – a browser racing game with your phone as the controller:D

**原文链接**: [https://simdrive.xyz/](https://simdrive.xyz/)

生成摘要时出错

---

## 60. Show HN: WhatCable, a tiny menu bar app for inspecting USB-C cables

**原文标题**: Show HN: WhatCable, a tiny menu bar app for inspecting USB-C cables

**原文链接**: [https://github.com/darrylmorley/whatcable](https://github.com/darrylmorley/whatcable)

生成摘要时出错

---

## 61. Advanced Quantization Algorithm for LLMs

**原文标题**: Advanced Quantization Algorithm for LLMs

**原文链接**: [https://github.com/intel/auto-round](https://github.com/intel/auto-round)

生成摘要时出错

---

## 62. GameStop Preparing Offer for eBay

**原文标题**: GameStop Preparing Offer for eBay

**原文链接**: [https://www.wsj.com/business/deals/gamestop-preparing-offer-for-ebay-1678e6de](https://www.wsj.com/business/deals/gamestop-preparing-offer-for-ebay-1678e6de)

生成摘要时出错

---

## 63. AI uses less water than the public thinks

**原文标题**: AI uses less water than the public thinks

**原文链接**: [https://californiawaterblog.com/2026/04/26/ai-water-use-distractions-and-lessons-for-california/](https://californiawaterblog.com/2026/04/26/ai-water-use-distractions-and-lessons-for-california/)

生成摘要时出错

---

## 64. IBM Granite 4.1 family of models

**原文标题**: IBM Granite 4.1 family of models

**原文链接**: [https://research.ibm.com/blog/granite-4-1-ai-foundation-models](https://research.ibm.com/blog/granite-4-1-ai-foundation-models)

生成摘要时出错

---

## 65. New mechanical panoramic film camera from Jeff Bridges

**原文标题**: New mechanical panoramic film camera from Jeff Bridges

**原文链接**: [https://wideluxx.com](https://wideluxx.com)

生成摘要时出错

---

## 66. I got infected with a crypto-miner via misconfigured qBittorrent

**原文标题**: I got infected with a crypto-miner via misconfigured qBittorrent

**原文链接**: [https://blog.vasi.li/well-i-got-hacked/](https://blog.vasi.li/well-i-got-hacked/)

生成摘要时出错

---

## 67. CPanel and WHM Authentication Bypass – CVE-2026-41940

**原文标题**: CPanel and WHM Authentication Bypass – CVE-2026-41940

**原文链接**: [https://labs.watchtowr.com/the-internet-is-falling-down-falling-down-falling-down-cpanel-whm-authentication-bypass-cve-2026-41940/](https://labs.watchtowr.com/the-internet-is-falling-down-falling-down-falling-down-cpanel-whm-authentication-bypass-cve-2026-41940/)

生成摘要时出错

---

## 68. An open letter asking NHS England to keep its code open

**原文标题**: An open letter asking NHS England to keep its code open

**原文链接**: [https://keepthingsopen.com](https://keepthingsopen.com)

生成摘要时出错

---

## 69. Can I disable all data collection from my vehicle?

**原文标题**: Can I disable all data collection from my vehicle?

**原文链接**: [https://rivian.com/support/article/can-i-disable-all-data-collection-from-my-vehicle](https://rivian.com/support/article/can-i-disable-all-data-collection-from-my-vehicle)

生成摘要时出错

---

## 70. Zed 1.0

**原文标题**: Zed 1.0

**原文链接**: [https://zed.dev/blog/zed-1-0](https://zed.dev/blog/zed-1-0)

生成摘要时出错

---

## 71. Your website is not for you

**原文标题**: Your website is not for you

**原文链接**: [https://websmith.studio/blog/your-website-is-not-for-you/](https://websmith.studio/blog/your-website-is-not-for-you/)

生成摘要时出错

---

## 72. Infrasound waves stop kitchen fires, but can they replace sprinklers?

**原文标题**: Infrasound waves stop kitchen fires, but can they replace sprinklers?

**原文链接**: [https://arstechnica.com/gadgets/2026/05/startup-says-sound-waves-can-replace-fire-sprinklers-experts-arent-so-sure/](https://arstechnica.com/gadgets/2026/05/startup-says-sound-waves-can-replace-fire-sprinklers-experts-arent-so-sure/)

生成摘要时出错

---

## 73. Credit cards are vulnerable to brute force kind attacks

**原文标题**: Credit cards are vulnerable to brute force kind attacks

**原文链接**: [https://metin.nextc.org/posts/Credit_Cards_Are_Vulnerable_To_Brute_Force_Kind_Attacks.html](https://metin.nextc.org/posts/Credit_Cards_Are_Vulnerable_To_Brute_Force_Kind_Attacks.html)

生成摘要时出错

---

## 74. Notes on a non-profit indicted for bank fraud

**原文标题**: Notes on a non-profit indicted for bank fraud

**原文链接**: [https://www.bitsaboutmoney.com/archive/nonprofit-indicted-bank-fraud/](https://www.bitsaboutmoney.com/archive/nonprofit-indicted-bank-fraud/)

生成摘要时出错

---

## 75. Ghostty is leaving GitHub

**原文标题**: Ghostty is leaving GitHub

**原文链接**: [https://mitchellh.com/writing/ghostty-leaving-github](https://mitchellh.com/writing/ghostty-leaving-github)

生成摘要时出错

---

## 76. Reverse Engineering SimTower

**原文标题**: Reverse Engineering SimTower

**原文链接**: [https://phulin.me/blog/simtower](https://phulin.me/blog/simtower)

生成摘要时出错

---

## 77. NSA Warned Everyone to Reboot Their Routers

**原文标题**: NSA Warned Everyone to Reboot Their Routers

**原文链接**: [https://www.staysafeonline.org/articles/the-nsa-just-warned-everyone-to-reboot-their-routers-what-to-do-right-now](https://www.staysafeonline.org/articles/the-nsa-just-warned-everyone-to-reboot-their-routers-what-to-do-right-now)

生成摘要时出错

---

## 78. Show HN: Agent-desktop – Native desktop automation CLI for AI agents

**原文标题**: Show HN: Agent-desktop – Native desktop automation CLI for AI agents

**原文链接**: [https://github.com/lahfir/agent-desktop](https://github.com/lahfir/agent-desktop)

生成摘要时出错

---

## 79. Full-Text Search with DuckDB

**原文标题**: Full-Text Search with DuckDB

**原文链接**: [https://peterdohertys.website/blog-posts/full-text-search-w-duckdb.html](https://peterdohertys.website/blog-posts/full-text-search-w-duckdb.html)

生成摘要时出错

---

## 80. Alberta allows windfall oil and gas payments to select ranchers – on public land

**原文标题**: Alberta allows windfall oil and gas payments to select ranchers – on public land

**原文链接**: [https://thenarwhal.ca/alberta-grazing-oil/](https://thenarwhal.ca/alberta-grazing-oil/)

生成摘要时出错

---

## 81. Softmax, can you derive the Jacobian? And should you care?

**原文标题**: Softmax, can you derive the Jacobian? And should you care?

**原文链接**: [https://idlemachines.co.uk/essays/softmax](https://idlemachines.co.uk/essays/softmax)

生成摘要时出错

---

## 82. Good developers learn to program. Most courses teach a language

**原文标题**: Good developers learn to program. Most courses teach a language

**原文链接**: [https://evilgeniuslabs.ca/blog/good-developers-learn-to-program-not-a-language](https://evilgeniuslabs.ca/blog/good-developers-learn-to-program-not-a-language)

生成摘要时出错

---

## 83. Chasing a SharedKey signature mismatch: fix azurerm_storage_table_entity

**原文标题**: Chasing a SharedKey signature mismatch: fix azurerm_storage_table_entity

**原文链接**: [https://topaz.thecloudtheory.com/blog/debugging-table-entity-auth/](https://topaz.thecloudtheory.com/blog/debugging-table-entity-auth/)

生成摘要时出错

---

## 84. Granite 4.1: IBM's 8B Model Matching 32B MoE

**原文标题**: Granite 4.1: IBM's 8B Model Matching 32B MoE

**原文链接**: [https://firethering.com/granite-4-1-ibm-open-source-model-family/](https://firethering.com/granite-4-1-ibm-open-source-model-family/)

生成摘要时出错

---

## 85. Becoming a father shrinks your cerebrum (2022)

**原文标题**: Becoming a father shrinks your cerebrum (2022)

**原文链接**: [https://www.economist.com/science-and-technology/2022/10/21/becoming-a-father-shrinks-your-cerebrum](https://www.economist.com/science-and-technology/2022/10/21/becoming-a-father-shrinks-your-cerebrum)

生成摘要时出错

---

## 86. Tvheadend: Self-Hosted IPTV Server

**原文标题**: Tvheadend: Self-Hosted IPTV Server

**原文链接**: [https://tvheadend.org](https://tvheadend.org)

生成摘要时出错

---

## 87. Grok 4.3

**原文标题**: Grok 4.3

**原文链接**: [https://docs.x.ai/developers/models/grok-4.3](https://docs.x.ai/developers/models/grok-4.3)

生成摘要时出错

---

## 88. Does Postgres Scale?

**原文标题**: Does Postgres Scale?

**原文链接**: [https://www.dbos.dev/blog/benchmarking-workflow-execution-scalability-on-postgres](https://www.dbos.dev/blog/benchmarking-workflow-execution-scalability-on-postgres)

生成摘要时出错

---

## 89. Show HN: Site Mogging

**原文标题**: Show HN: Site Mogging

**原文链接**: [https://sitemogging.com](https://sitemogging.com)

生成摘要时出错

---

## 90. Show HN: Loopsy, a way for terminals and AI agents on different machines to talk

**原文标题**: Show HN: Loopsy, a way for terminals and AI agents on different machines to talk

**原文链接**: [https://github.com/leox255/loopsy](https://github.com/leox255/loopsy)

生成摘要时出错

---

## 91. How Mark Klein told the EFF about Room 641A [book excerpt]

**原文标题**: How Mark Klein told the EFF about Room 641A [book excerpt]

**原文链接**: [https://thereader.mitpress.mit.edu/the-whistleblower-who-uncovered-the-nsas-big-brother-machine/](https://thereader.mitpress.mit.edu/the-whistleblower-who-uncovered-the-nsas-big-brother-machine/)

生成摘要时出错

---

## 92. Shai-Hulud Themed Malware Found in the PyTorch Lightning AI Training Library

**原文标题**: Shai-Hulud Themed Malware Found in the PyTorch Lightning AI Training Library

**原文链接**: [https://semgrep.dev/blog/2026/malicious-dependency-in-pytorch-lightning-used-for-ai-training/](https://semgrep.dev/blog/2026/malicious-dependency-in-pytorch-lightning-used-for-ai-training/)

生成摘要时出错

---

## 93. Copy Fail

**原文标题**: Copy Fail

**原文链接**: [https://copy.fail/](https://copy.fail/)

生成摘要时出错

---

## 94. What can we gain by losing infinity?

**原文标题**: What can we gain by losing infinity?

**原文链接**: [https://www.quantamagazine.org/what-can-we-gain-by-losing-infinity-20260429/](https://www.quantamagazine.org/what-can-we-gain-by-losing-infinity-20260429/)

生成摘要时出错

---

## 95. AWS stops billing Middle East cloud customers as repairs to war damage drag on

**原文标题**: AWS stops billing Middle East cloud customers as repairs to war damage drag on

**原文链接**: [https://arstechnica.com/gadgets/2026/05/amazon-stuck-with-months-of-repairs-after-drone-strikes-on-data-centers/](https://arstechnica.com/gadgets/2026/05/amazon-stuck-with-months-of-repairs-after-drone-strikes-on-data-centers/)

生成摘要时出错

---

## 96. Hermit – uniform tooling for Linux and Mac

**原文标题**: Hermit – uniform tooling for Linux and Mac

**原文链接**: [https://github.com/cashapp/hermit](https://github.com/cashapp/hermit)

生成摘要时出错

---

## 97. OpenX32: Open Linux kernel for Behringer X32 mixer

**原文标题**: OpenX32: Open Linux kernel for Behringer X32 mixer

**原文链接**: [https://github.com/OpenMixerProject/OpenX32](https://github.com/OpenMixerProject/OpenX32)

生成摘要时出错

---

## 98. Roboticist-Turned-Teacher Built a Life-Size Replica of Eniac

**原文标题**: Roboticist-Turned-Teacher Built a Life-Size Replica of Eniac

**原文链接**: [https://spectrum.ieee.org/roboticist-turned-teacher-eniac-replica](https://spectrum.ieee.org/roboticist-turned-teacher-eniac-replica)

生成摘要时出错

---

## 99. Talkie: a 13B vintage language model from 1930

**原文标题**: Talkie: a 13B vintage language model from 1930

**原文链接**: [https://talkie-lm.com/introducing-talkie](https://talkie-lm.com/introducing-talkie)

生成摘要时出错

---

## 100. LibreOffice 26.2.3 Released – What Is New and What Was Fixed?

**原文标题**: LibreOffice 26.2.3 Released – What Is New and What Was Fixed?

**原文链接**: [https://tux.re/forum/viewtopic.php?t=210](https://tux.re/forum/viewtopic.php?t=210)

生成摘要时出错

---

