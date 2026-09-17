# Hacker News 热门文章摘要 (2026-09-17)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Hister：一款针对已访问网页和保存文件的私密搜索引擎

**原文标题**: Hister: A private search engine for the pages you visit and the files you keep

**原文链接**: [https://github.com/asciimoo/hister](https://github.com/asciimoo/hister)

**Hister** 是一款开源的私有搜索引擎，旨在为您访问过的网页和存储的本地文件建立索引。与传统的搜索引擎不同，它会为您个人的数字历史记录创建一个可进行全文检索的数据库，让您无需依赖第三方云服务商即可找回之前接触过的信息。

**核心功能：**
*   **索引：** 它通过浏览器扩展（Firefox 和 Chrome）抓取网页的全文内容，并能对本地目录、现有的浏览器历史记录或通过爬虫抓取的特定网站建立索引。
*   **搜索能力：** 用户可以使用字段过滤、通配符和否定词进行强大的查询。它还支持可选的**语义搜索**，通过嵌入（embeddings）技术根据含义而非仅仅是关键词来查找文档。
*   **访问方式：** 该工具非常灵活，提供 Web 界面、基于终端的（CLI/TUI）客户端，并可通过模型上下文协议（MCP）与 AI 助手集成。
*   **隐私保护：** Hister 采用“隐私优先”的设计理念。它不含遥测数据采集或强制性的云端同步；所有数据都存储在本地或由用户控制的基础设施中。

**技术细节：**
Hister 使用 Go 语言开发，基于 **AGPLv3** 协议授权。它支持多用户环境，在共享服务器上可确保不同用户的文档和搜索结果相互隔离。通过预编译二进制文件、Homebrew、Docker 或 Nix，安装过程非常简便，本地个人设置无需初始配置。

最终，Hister 充当了一个“个人记忆”工具，为您从自己的网络活动和文件系统中检索信息提供了一种集中且私密的方式。

---

## 2. 密苏里州州长下令规范Flock摄像头和自动车牌识别系统的使用。

**原文标题**: Missouri governor orders guardrails on Flock cameras and ALPRs

**原文链接**: [https://www.stlpr.org/news-briefs/2026-09-16/flock-cameras-guardrails-missouri-kehoe](https://www.stlpr.org/news-briefs/2026-09-16/flock-cameras-guardrails-missouri-kehoe)

密苏里州州长迈克·基霍（Mike Kehoe）签署了一项行政命令，为州政府机构和受州政府资助的执法部门使用自动车牌识别器（ALPR，如 Flock 摄像头）制定了严格的安全保障措施。该命令旨在通过防止“无节制地收集”位置数据，来保护公民的隐私和宪法权利。

该行政命令提出了几项关键

基霍将该命令描述为“第一步”，是在州立法者通过永久性立法之前的过渡性措施。在此之前，该州发生了多起备受关注的滥用事件，包括一名布伦特伍德（Brentwood）警察利用该技术跟踪前妻，以及圣查尔斯县（St. Charles County）的一名文职雇员滥用系统数据。

虽然执法官员坚持认为 Flock 摄像头是侦破犯罪的重要工具，但该技术面临着来自隐私、民权和移民倡导者日益增加的批评。针对这些担忧和滥用案例，包括圣查尔斯县警察局和普拉斯基县（Pulaski County）警长办公室在内的一些地方部门已经停止使用 Flock 摄像头。

---

## 3. Fujitsu launches made-in-Japan next-generation CPU FUJITSU-MONAKA

**原文标题**: Fujitsu launches made-in-Japan next-generation CPU FUJITSU-MONAKA

**原文链接**: [https://global.fujitsu/en-global/pr/news/2026/09/14-02](https://global.fujitsu/en-global/pr/news/2026/09/14-02)

生成摘要时出错

---

## 4. 石蜡马达

**原文标题**: Wax Motor

**原文链接**: [https://en.wikipedia.org/wiki/Wax_motor](https://en.wikipedia.org/wiki/Wax_motor)

蜡马达是一种利用石蜡的相变特性将热能转化为机械能的线性致动器。当石蜡熔化时，其体积通常会膨胀 5% 至 20%，从而产生强大的液压，驱动活塞或推杆向外运动。

**结构与设计**
该装置由封闭的石蜡、活塞、热源（如电热敏电阻、太阳辐射或环境热量）以及用于冷却的散热器组成。当热源移除后，石蜡会收缩；通常需要弹簧或重力等复位力使活塞返回其原始位置。

**优势**
与电磁螺线管相比，蜡马达具有以下优点：
*   **力量：** 能够产生显著的液压（约 4,000 牛顿）。
*   **平稳性：** 运行过程平缓稳定，而非瞬间动作。
*   **被动运行：** 能够直接响应环境温度变化，无需外部电源即可工作。
*   **电气简化：** 作为阻性负载，在由双向可控硅（TRIAC）控制时无需缓冲电路。

**应用领域**
凭借其可靠性和可预测的动作时间，蜡马达被广泛应用于多个领域：
*   **家用电器：** 在洗衣机中，它们用于机门锁闭并提供内置安全延迟（确保滚筒在石蜡冷却解锁前停止旋转）。在洗碗机中，它们用于触发洗涤剂投放器和排气口。
*   **航空航天与暖通空调（HVAC）：** 它们控制飞机的燃油和机油流量，并驱动供暖系统中的恒温混水阀和散热器阀。
*   **温室：** 作为被动调节器，在气温过高时自动打开通风口，并在冷却时将其关闭。
*   **微技术：** 微型化版本（即石蜡微致动器）被应用于微机电系统（MEMS）技术中的精密机械。

---

## 5. CrowdSec Source Code Leak

**原文标题**: CrowdSec Source Code Leak

**原文链接**: [https://www.crowdsec.net/blog/crowdsec-statement-source-code-exposure](https://www.crowdsec.net/blog/crowdsec-statement-source-code-exposure)

On September 16, CrowdSec confirmed a source code leak involving approximately 300 GitHub repositories that occurred in May 2026. While 130 of these repositories were already public, the leak exposed private code related to the company’s SaaS console, AWS Cloud routines, connectors, and automations.

**Key details from the report include:**

*   **No Client Impact:** The company verified that no client data, login credentials, or PII were compromised. CrowdSec does not store client logs, and the leak’s impact is limited to the company’s internal code.
*   **Limited Risk:** Management stated that the leaked code poses no immediate threat. Its utility is limited outside of CrowdSec’s specific environment, and the company’s primary value lies in its "network effect" rather than the code alone. Additionally, much of the leaked code has evolved significantly since May.
*   **Root Cause:** The leak was likely caused by a backdoored **Tanstack** component used in May 2026. This vulnerability allowed an attacker to extract a CI/CD API token with read access to private repositories for a short duration.
*   **Response:** CrowdSec has rotated all sensitive tokens and credentials to prevent further unauthorized access. They are currently monitoring for any abnormal activity and continue to investigate the incident.

The company expressed appreciation for **Fuites Infos**, who professionally reported the issue. Under the current assessment, the leak is viewed as a limited incident with no direct threat to users or the core functionality of the Security Engine.

---

## 6. GitLab.com 速率限制正在调整

**原文标题**: Rate limits on GitLab.com are changing

**原文链接**: [https://about.gitlab.com/blog/rate-limit-change-2026/](https://about.gitlab.com/blog/rate-limit-change-2026/)

GitLab 正在更新 GitLab.com 的速率限制结构，以在需求增长时保持平台性能。自 **2026 年 10 月 19 日**起，速率限制将根据用户的订阅级别（Free、Premium 或 Ultimate）确定，并按用户及顶级群组（top-level group）实施。

**关键时间节点：**
*   **2026 年 10 月 7 日及 14 日：** 将在 UTC 时间 15:00 至 19:00 开启预览窗口（“断续测试”），以帮助免费用户和未认证用户在限制下测试其工作负载。
*   **2026 年 10 月 19 日：** 新限制对**免费账号**和**未认证请求**生效。
*   **2027 年 1 月：** 新限制对 **Premium 和 Ultimate** 订阅生效。

**主要变更：**
*   **身份认证：** 未认证请求的上限为每 IP 地址每小时 60 次。强烈建议用户进行身份认证（使用 PAT、OAuth 或 CI/CD 作业令牌），以获得与其方案关联的更高限额。
*   **分级扩展：** Premium 和 Ultimate 级别将提供最慷慨的限制，旨在满足企业级自动化的需求。
*   **适用范围：** 这些变更**仅适用于 GitLab.com**。GitLab 自托管（Self-Managed）和 GitLab 专用版（Dedicated）实例不受影响。
*   **影响：** 大多数用户不会察觉到变化。UI 浏览、Git 操作（push/pull）以及正常的 CI/CD 使用均不是这些限制的目标。

**缓解与支持：**
如果达到限制，GitLab 将返回 **HTTP 429** 错误及 `Retry-After` 响应头。用户可以通过批量处理、缓存和分页来优化流量。对于需要超出标准级别限制的容量的用户，GitLab 正在开发购买额外额度的方式。具有独特集成需求或高并发需求的用户应联系 `limits@gitlab.com`。

---

## 7. 无限参数大语言模型：基于实时数据的权重生成与自适应

**原文标题**: Infinite-Parameter LLMs: Generating and Adapting Weights from Live Data

**原文链接**: [https://arxiv.org/abs/2609.18842](https://arxiv.org/abs/2609.18842)

The paper **"Infinite-Parameter LLMs: Generating and Adapting Weights from Live Data"** (2026) by Hu et al. addresses a fundamental limitation in current Large Language Models (LLMs): the inability to integrate new information into their weights after pretraining. While current models rely on in-context learning (ICL) or retrieval-augmented generation (RAG) to handle live data, these methods are temporary, consume context window space, and must be re-processed for every request.

The authors propose the **Infinite-Parameter LLM**, an architecture designed to learn from live interactions by dynamically updating its weights. The system utilizes a compact **hypernetwork** that transforms run-time data into low-rank modulations of a shared base network. Unlike static weight generators, this model maintains a **Bayesian belief** over the generator’s latent code. This belief is updated online as a session progresses, allowing the model to continuously refine and re-derive its effective weights based on user feedback or new facts.

**Key advantages of this approach include:**
*   **Efficiency:** Carrying knowledge in weights rather than the prompt amortizes compute costs and frees up the context window.
*   **Persistence:** Changes to the model's behavior and knowledge persist across turns within a session.
*   **Scalability:** The model maintains a fixed storage footprint while technically accessing an "infinite" variety of weight configurations.
*   **Generalization:** The authors argue that this weight-based adaptation generalizes better than standard in-context learning.

The paper concludes by establishing an evaluation protocol that compares this architecture against traditional ICL and retrieval methods, demonstrating its superior ability to adapt to live data.

---

## 8. Why I didn’t sign the Fields medallists’ letter

**原文标题**: Why I didn’t sign the Fields medallists’ letter

**原文链接**: [https://gowers.wordpress.com/2026/09/17/why-i-didnt-sign-the-fields-medallists-letter/](https://gowers.wordpress.com/2026/09/17/why-i-didnt-sign-the-fields-medallists-letter/)

生成摘要时出错

---

## 9. 台积电披露下一代 A14 制程细节

**原文标题**: TSMC revealing details about next gen A14 node

**原文链接**: [https://iedm26.mapyourshow.com/8_0/sessions/session-details.cfm?scheduleid=331](https://iedm26.mapyourshow.com/8_0/sessions/session-details.cfm?scheduleid=331)

Unable to access the article link.

---

## 10. How GLM built its own inference infrastructure

**原文标题**: How GLM built its own inference infrastructure

**原文链接**: [https://z.ai/blog/glm-built-its-inference-infrastructure](https://z.ai/blog/glm-built-its-inference-infrastructure)

生成摘要时出错

---

## 11. Running Ubuntu on the Lenovo IdeaPad Duet

**原文标题**: Running Ubuntu on the Lenovo IdeaPad Duet

**原文链接**: [https://vhaudiquet.fr/blog/duet-ubuntu/](https://vhaudiquet.fr/blog/duet-ubuntu/)

生成摘要时出错

---

## 12. Zettascale (YC S24) Is Hiring ASIC/FPGA Engineers to Build Chips for ASI

**原文标题**: Zettascale (YC S24) Is Hiring ASIC/FPGA Engineers to Build Chips for ASI

**原文链接**: [https://zscc.ai/careers?job_id=109821](https://zscc.ai/careers?job_id=109821)

生成摘要时出错

---

## 13. The American Religion of Self-Storage Facilities

**原文标题**: The American Religion of Self-Storage Facilities

**原文链接**: [https://www.newyorker.com/magazine/2026/09/21/the-american-religion-of-self-storage-facilities](https://www.newyorker.com/magazine/2026/09/21/the-american-religion-of-self-storage-facilities)

生成摘要时出错

---

## 14. One year of sponsored Servo development

**原文标题**: One year of sponsored Servo development

**原文链接**: [https://servo.org/blog/2026/09/15/one-year-of-sponsorship/](https://servo.org/blog/2026/09/15/one-year-of-sponsorship/)

生成摘要时出错

---

## 15. Show HN: Share your AI Setup, Learn from others

**原文标题**: Show HN: Share your AI Setup, Learn from others

**原文链接**: [https://mysetup.ai/](https://mysetup.ai/)

生成摘要时出错

---

## 16. CCC invites all model citizens to 40C3

**原文标题**: CCC invites all model citizens to 40C3

**原文链接**: [https://events.ccc.de/en/2026/09/12/40c3-model-citizens/](https://events.ccc.de/en/2026/09/12/40c3-model-citizens/)

生成摘要时出错

---

## 17. Grand MS-DOS Gaming General MIDI Showdown

**原文标题**: Grand MS-DOS Gaming General MIDI Showdown

**原文链接**: [https://blog.johnnovak.net/2023/03/05/grand-ms-dos-gaming-general-midi-showdown/](https://blog.johnnovak.net/2023/03/05/grand-ms-dos-gaming-general-midi-showdown/)

生成摘要时出错

---

## 18. The Return of Sail Power: Cargo Ships Are Turning Back to the Wind

**原文标题**: The Return of Sail Power: Cargo Ships Are Turning Back to the Wind

**原文链接**: [https://gcaptain.com/the-return-of-sail-power-cargo-ships-are-turning-back-to-the-wind/](https://gcaptain.com/the-return-of-sail-power-cargo-ships-are-turning-back-to-the-wind/)

生成摘要时出错

---

## 19. Don't Make Job Referrals Public

**原文标题**: Don't Make Job Referrals Public

**原文链接**: [https://blog.melashri.net/micro/public-job-referral/](https://blog.melashri.net/micro/public-job-referral/)

生成摘要时出错

---

## 20. LLM Classification Is Feature Engineering

**原文标题**: LLM Classification Is Feature Engineering

**原文链接**: [https://minimallysufficient.com/posts/llm-classification-is-feature-extraction/](https://minimallysufficient.com/posts/llm-classification-is-feature-extraction/)

生成摘要时出错

---

## 21. Show HN: Craigslist for agent skills, curated by a human

**原文标题**: Show HN: Craigslist for agent skills, curated by a human

**原文链接**: [https://skillbay.sh/](https://skillbay.sh/)

生成摘要时出错

---

## 22. My temporary PHP fix from 2014 has nearly 20M installs. Today I'm deprecating it

**原文标题**: My temporary PHP fix from 2014 has nearly 20M installs. Today I'm deprecating it

**原文链接**: [https://jakeasmith.com/blog/http-build-url/](https://jakeasmith.com/blog/http-build-url/)

生成摘要时出错

---

## 23. Economic policy for AGI

**原文标题**: Economic policy for AGI

**原文链接**: [https://institute.deepmind.com/essays/economic-policy-for-agi/](https://institute.deepmind.com/essays/economic-policy-for-agi/)

生成摘要时出错

---

## 24. Vinix – A modern operating system written in V

**原文标题**: Vinix – A modern operating system written in V

**原文链接**: [https://vinix-os.org/](https://vinix-os.org/)

生成摘要时出错

---

## 25. Mastering Layout Engines in Graphviz: Dot vs. Neato vs. Twopi vs. Circo

**原文标题**: Mastering Layout Engines in Graphviz: Dot vs. Neato vs. Twopi vs. Circo

**原文链接**: [https://guides.visual-paradigm.com/mastering-graphviz-layout-engines-dot-neato-twopi-circo/](https://guides.visual-paradigm.com/mastering-graphviz-layout-engines-dot-neato-twopi-circo/)

生成摘要时出错

---

## 26. Artificial intelligence now beats some of the best human forecasters

**原文标题**: Artificial intelligence now beats some of the best human forecasters

**原文链接**: [https://www.economist.com/science-and-technology/2026/09/16/artificial-intelligence-now-beats-some-of-the-best-human-forecasters](https://www.economist.com/science-and-technology/2026/09/16/artificial-intelligence-now-beats-some-of-the-best-human-forecasters)

生成摘要时出错

---

## 27. Stallman: Thousands Dead, Millions Deprived of Liberties (2001)

**原文标题**: Stallman: Thousands Dead, Millions Deprived of Liberties (2001)

**原文链接**: [https://news.slashdot.org/story/01/09/17/1758231/stallman-thousands-dead-millions-deprived-of-liberties](https://news.slashdot.org/story/01/09/17/1758231/stallman-thousands-dead-millions-deprived-of-liberties)

生成摘要时出错

---

## 28. The Relation Between Mathematics and Physics by Paul Dirac (1939)

**原文标题**: The Relation Between Mathematics and Physics by Paul Dirac (1939)

**原文链接**: [https://www.damtp.cam.ac.uk/events/strings02/dirac/speach.html](https://www.damtp.cam.ac.uk/events/strings02/dirac/speach.html)

生成摘要时出错

---

## 29. Don't Just Say Hello

**原文标题**: Don't Just Say Hello

**原文链接**: [https://nohello.net/en/](https://nohello.net/en/)

生成摘要时出错

---

## 30. Show HN: I built a new version of my fun spatial 3D online meeting app

**原文标题**: Show HN: I built a new version of my fun spatial 3D online meeting app

**原文链接**: [https://flat.social](https://flat.social)

生成摘要时出错

---

## 31. Show HN: An e-ink frame that hears birds and draws them as 1800s illustrations

**原文标题**: Show HN: An e-ink frame that hears birds and draws them as 1800s illustrations

**原文链接**: [https://github.com/arnegiacomo/fugleramme](https://github.com/arnegiacomo/fugleramme)

生成摘要时出错

---

## 32. Show HN: Aclif – Agent CLI framework: one grammar, canonical names across SaaS

**原文标题**: Show HN: Aclif – Agent CLI framework: one grammar, canonical names across SaaS

**原文链接**: [https://www.aclif.ai/](https://www.aclif.ai/)

生成摘要时出错

---

## 33. Better Vector Search for Long Documents: Chunking Inside Manticore Search

**原文标题**: Better Vector Search for Long Documents: Chunking Inside Manticore Search

**原文链接**: [https://manticoresearch.com/blog/auto-chunking/](https://manticoresearch.com/blog/auto-chunking/)

生成摘要时出错

---

## 34. Nvidia announces native GPU programming in Rust

**原文标题**: Nvidia announces native GPU programming in Rust

**原文链接**: [https://developer.nvidia.com/blog/introducing-cuda-rust-two-tracks-for-writing-gpu-kernels/](https://developer.nvidia.com/blog/introducing-cuda-rust-two-tracks-for-writing-gpu-kernels/)

生成摘要时出错

---

## 35. KIDS Act

**原文标题**: KIDS Act

**原文链接**: [https://digital-strategy.ec.europa.eu/en/policies/kids-act](https://digital-strategy.ec.europa.eu/en/policies/kids-act)

生成摘要时出错

---

## 36. Whoisinspace.com/

**原文标题**: Whoisinspace.com/

**原文链接**: [https://whoisinspace.com](https://whoisinspace.com)

生成摘要时出错

---

## 37. Lucasart's Afterlife

**原文标题**: Lucasart's Afterlife

**原文链接**: [https://togameforlife.wordpress.com/2023/12/09/on-lucasarts-afterlife/](https://togameforlife.wordpress.com/2023/12/09/on-lucasarts-afterlife/)

生成摘要时出错

---

## 38. Cloudflare/Security-Audit-Skill

**原文标题**: Cloudflare/Security-Audit-Skill

**原文链接**: [https://github.com/cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)

生成摘要时出错

---

## 39. Towards Self-Driving Codebases

**原文标题**: Towards Self-Driving Codebases

**原文链接**: [https://blog.detail.dev/posts/towards-self-driving-codebases/](https://blog.detail.dev/posts/towards-self-driving-codebases/)

生成摘要时出错

---

## 40. Show HN: AutoBot – live voice control for long-running AI work

**原文标题**: Show HN: AutoBot – live voice control for long-running AI work

**原文链接**: [https://github.com/demeyer1/Autobot](https://github.com/demeyer1/Autobot)

生成摘要时出错

---

## 41. BYD looking to build 5-minute EV charging network in Canada

**原文标题**: BYD looking to build 5-minute EV charging network in Canada

**原文链接**: [https://driving.ca/auto-news/industry/byd-china-ev-megawatt-flash-charger-network-canada](https://driving.ca/auto-news/industry/byd-china-ev-megawatt-flash-charger-network-canada)

生成摘要时出错

---

## 42. The Bicycle and the Algorithm: Amber Case on Why AI Has It Backwards

**原文标题**: The Bicycle and the Algorithm: Amber Case on Why AI Has It Backwards

**原文链接**: [https://www.designwhine.com/amber-case-interview-why-ai-has-it-backwards/](https://www.designwhine.com/amber-case-interview-why-ai-has-it-backwards/)

生成摘要时出错

---

## 43. Priest, Monk, and Mathematician

**原文标题**: Priest, Monk, and Mathematician

**原文链接**: [https://logangraves.com/priest-monk-mathematician](https://logangraves.com/priest-monk-mathematician)

生成摘要时出错

---

## 44. Comparison of Malloc() Algorithms

**原文标题**: Comparison of Malloc() Algorithms

**原文链接**: [https://egbert.net/blog/articles/comparison-of-arena-architecture-in-malloc.html](https://egbert.net/blog/articles/comparison-of-arena-architecture-in-malloc.html)

生成摘要时出错

---

## 45. OpenAI models secretly generate instructions to ignore constraints

**原文标题**: OpenAI models secretly generate instructions to ignore constraints

**原文链接**: [https://alignment.openai.com/misalignment-reports/self-generated-prompt-injections-in-compaction-summaries/](https://alignment.openai.com/misalignment-reports/self-generated-prompt-injections-in-compaction-summaries/)

生成摘要时出错

---

## 46. Online Z3 Guide

**原文标题**: Online Z3 Guide

**原文链接**: [https://microsoft.github.io/z3guide/](https://microsoft.github.io/z3guide/)

生成摘要时出错

---

## 47. Developing provably correct Rust code with Verus

**原文标题**: Developing provably correct Rust code with Verus

**原文链接**: [https://www.amazon.science/blog/developing-provably-correct-rust-code-with-verus](https://www.amazon.science/blog/developing-provably-correct-rust-code-with-verus)

生成摘要时出错

---

## 48. I Don't Like LLMs

**原文标题**: I Don't Like LLMs

**原文链接**: [https://martinfowler.com/articles/2026-dont-like-llms.html](https://martinfowler.com/articles/2026-dont-like-llms.html)

生成摘要时出错

---

## 49. Training a 4B model to produce 81% faster query plans than Postgres

**原文标题**: Training a 4B model to produce 81% faster query plans than Postgres

**原文链接**: [https://rohanbansal.com/qorl](https://rohanbansal.com/qorl)

生成摘要时出错

---

## 50. Tests of the New AI Siri

**原文标题**: Tests of the New AI Siri

**原文链接**: [https://pogueman.substack.com/p/125-tests-of-the-new-ai-siri](https://pogueman.substack.com/p/125-tests-of-the-new-ai-siri)

生成摘要时出错

---

## 51. 4-Bit Rotational Quantization: -45% RAM, <1% recall drop vs. TurboQuant

**原文标题**: 4-Bit Rotational Quantization: -45% RAM, <1% recall drop vs. TurboQuant

**原文链接**: [https://weaviate.io/blog/4-bit-rotational-quantization](https://weaviate.io/blog/4-bit-rotational-quantization)

生成摘要时出错

---

## 52. The First New Cat Species Discovered in 100 Years

**原文标题**: The First New Cat Species Discovered in 100 Years

**原文链接**: [https://www.nationalgeographic.com/animals/article/meet-the-first-new-cat-species-discovered-in-100-years](https://www.nationalgeographic.com/animals/article/meet-the-first-new-cat-species-discovered-in-100-years)

生成摘要时出错

---

## 53. OpenSpec – A lightweight and configurable AI spec framework

**原文标题**: OpenSpec – A lightweight and configurable AI spec framework

**原文链接**: [https://openspec.dev/](https://openspec.dev/)

生成摘要时出错

---

## 54. AI safety is mostly a sex cult

**原文标题**: AI safety is mostly a sex cult

**原文链接**: [https://skywriter.blue/@segyges.bsky.social/3mvom4b4dn22q](https://skywriter.blue/@segyges.bsky.social/3mvom4b4dn22q)

生成摘要时出错

---

## 55. Our framework for reporting model misalignment

**原文标题**: Our framework for reporting model misalignment

**原文链接**: [https://openai.com/index/model-misalignment-reporting-framework/](https://openai.com/index/model-misalignment-reporting-framework/)

生成摘要时出错

---

## 56. Reversing Factorio's RNG

**原文标题**: Reversing Factorio's RNG

**原文链接**: [https://gegell.github.io/posts/factorio-rng/](https://gegell.github.io/posts/factorio-rng/)

生成摘要时出错

---

## 57. Keys Not Included: recovering the signing keys for US driver's license barcodes

**原文标题**: Keys Not Included: recovering the signing keys for US driver's license barcodes

**原文链接**: [https://ryan.science/blog/keys-not-included](https://ryan.science/blog/keys-not-included)

生成摘要时出错

---

## 58. A 32-year-old bug walks into a Telnet server

**原文标题**: A 32-year-old bug walks into a Telnet server

**原文链接**: [https://labs.watchtowr.com/a-32-year-old-bug-walks-into-a-telnet-server-gnu-inetutils-telnetd-cve-2026-32746/](https://labs.watchtowr.com/a-32-year-old-bug-walks-into-a-telnet-server-gnu-inetutils-telnetd-cve-2026-32746/)

生成摘要时出错

---

## 59. Be alert: targeted attacks on prominent Rustaceans

**原文标题**: Be alert: targeted attacks on prominent Rustaceans

**原文链接**: [https://blog.rust-lang.org/2026/09/17/targeted-attacks/](https://blog.rust-lang.org/2026/09/17/targeted-attacks/)

生成摘要时出错

---

## 60. Iran school bombing: grounds to believe US was behind atrocity, UN finds

**原文标题**: Iran school bombing: grounds to believe US was behind atrocity, UN finds

**原文链接**: [https://www.theguardian.com/world/2026/sep/17/iran-school-bombing-un-mission-us-military-behind-attack](https://www.theguardian.com/world/2026/sep/17/iran-school-bombing-un-mission-us-military-behind-attack)

生成摘要时出错

---

## 61. South Africa is at risk of becoming a mafia state

**原文标题**: South Africa is at risk of becoming a mafia state

**原文链接**: [https://www.economist.com/middle-east-and-africa/2026/09/14/south-africa-is-at-risk-of-becoming-a-mafia-state](https://www.economist.com/middle-east-and-africa/2026/09/14/south-africa-is-at-risk-of-becoming-a-mafia-state)

生成摘要时出错

---

## 62. Anecdotally, programmers dislike "reduce"

**原文标题**: Anecdotally, programmers dislike "reduce"

**原文链接**: [https://evanhahn.com/posts/2026-09-13-programmers-dislike-reduce/](https://evanhahn.com/posts/2026-09-13-programmers-dislike-reduce/)

生成摘要时出错

---

## 63. The Shortcut Became the System

**原文标题**: The Shortcut Became the System

**原文链接**: [https://christophermeiklejohn.com/ai/agents/reliability/development/games/2026/09/14/the-shortcut-became-the-system.html](https://christophermeiklejohn.com/ai/agents/reliability/development/games/2026/09/14/the-shortcut-became-the-system.html)

生成摘要时出错

---

## 64. Xiaomi Mimo 2.6 live post-training dashboard

**原文标题**: Xiaomi Mimo 2.6 live post-training dashboard

**原文链接**: [https://mimo.xiaomi.com/rl/](https://mimo.xiaomi.com/rl/)

生成摘要时出错

---

## 65. 1,000+ shoes reviewed and cut in half

**原文标题**: 1,000+ shoes reviewed and cut in half

**原文链接**: [https://runrepeat.com](https://runrepeat.com)

生成摘要时出错

---

## 66. New evidence for hidden chambers beyond Tutankhamun's tomb

**原文标题**: New evidence for hidden chambers beyond Tutankhamun's tomb

**原文链接**: [https://www.nature.com/articles/d41586-026-02621-2](https://www.nature.com/articles/d41586-026-02621-2)

生成摘要时出错

---

## 67. Small programming tricks

**原文标题**: Small programming tricks

**原文链接**: [https://will-keleher.com/posts/small-programming-tricks-matter/](https://will-keleher.com/posts/small-programming-tricks-matter/)

生成摘要时出错

---

## 68. Show HN: Navier-Stokes Visualized as 1kB i386 demos

**原文标题**: Show HN: Navier-Stokes Visualized as 1kB i386 demos

**原文链接**: [https://juandecos.github.io/TurboZip/vortex.html](https://juandecos.github.io/TurboZip/vortex.html)

生成摘要时出错

---

## 69. Robots are asking for tips. But who gets the money?

**原文标题**: Robots are asking for tips. But who gets the money?

**原文链接**: [https://www.bbc.com/future/article/20260818-do-you-have-to-tip-the-robots](https://www.bbc.com/future/article/20260818-do-you-have-to-tip-the-robots)

生成摘要时出错

---

## 70. OpenAI Discloses Six New Incidents of ‘Concerning’ A.I. Behavior

**原文标题**: OpenAI Discloses Six New Incidents of ‘Concerning’ A.I. Behavior

**原文链接**: [https://www.nytimes.com/2026/09/16/technology/openai-model-safety-guardrails.html](https://www.nytimes.com/2026/09/16/technology/openai-model-safety-guardrails.html)

生成摘要时出错

---

## 71. Reverse-engineered Jev-like model

**原文标题**: Reverse-engineered Jev-like model

**原文链接**: [https://github.com/vinnylarouge/jevlike](https://github.com/vinnylarouge/jevlike)

生成摘要时出错

---

## 72. An Archive of Colour Gradients

**原文标题**: An Archive of Colour Gradients

**原文链接**: [https://phillips.shef.ac.uk/pub/cpt-city/](https://phillips.shef.ac.uk/pub/cpt-city/)

生成摘要时出错

---

## 73. Hafnium Controversy

**原文标题**: Hafnium Controversy

**原文链接**: [https://en.wikipedia.org/wiki/Hafnium_controversy](https://en.wikipedia.org/wiki/Hafnium_controversy)

生成摘要时出错

---

## 74. Hackers Got Inside a Flock Camera

**原文标题**: Hackers Got Inside a Flock Camera

**原文链接**: [https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/](https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/)

生成摘要时出错

---

## 75. Jev Ultrafast: A browser agent with a dynamic, indexed action space

**原文标题**: Jev Ultrafast: A browser agent with a dynamic, indexed action space

**原文链接**: [https://github.com/browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast)

生成摘要时出错

---

## 76. Introducing System One Models and Jev

**原文标题**: Introducing System One Models and Jev

**原文链接**: [https://typesafe.ai/blog/introducing-system-one-models-and-jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev)

生成摘要时出错

---

## 77. OpenAI's Misalignment Framework: A Tactical Bid to Preempt Global AI Governance

**原文标题**: OpenAI's Misalignment Framework: A Tactical Bid to Preempt Global AI Governance

**原文链接**: [https://asiaai.fyi/openai-misalignment-framework-global-governance/](https://asiaai.fyi/openai-misalignment-framework-global-governance/)

生成摘要时出错

---

## 78. Breaking the 1.58-bit Barrier for Ternary LLMs

**原文标题**: Breaking the 1.58-bit Barrier for Ternary LLMs

**原文链接**: [https://arxiv.org/abs/2609.16338](https://arxiv.org/abs/2609.16338)

生成摘要时出错

---

## 79. The DeepMind Institute

**原文标题**: The DeepMind Institute

**原文链接**: [https://institute.deepmind.com/](https://institute.deepmind.com/)

生成摘要时出错

---

## 80. HarnessTax: How Much Does the Harness Matter for Coding Agents?

**原文标题**: HarnessTax: How Much Does the Harness Matter for Coding Agents?

**原文链接**: [https://harnesstax.github.io/](https://harnesstax.github.io/)

生成摘要时出错

---

## 81. Part-human part-mouse brain developed in science breakthrough

**原文标题**: Part-human part-mouse brain developed in science breakthrough

**原文链接**: [https://www.bbc.com/news/articles/c60m3k28j81mo](https://www.bbc.com/news/articles/c60m3k28j81mo)

生成摘要时出错

---

## 82. Backups Aren't Simple

**原文标题**: Backups Aren't Simple

**原文链接**: [https://filipovski.net/2026/09/16/backups-arent-simple.html](https://filipovski.net/2026/09/16/backups-arent-simple.html)

生成摘要时出错

---

## 83. Missouri governor orders guardrails on Flock cameras and ALPRs

**原文标题**: Missouri governor orders guardrails on Flock cameras and ALPRs

**原文链接**: [https://www.stlpr.org/news-briefs/2026-09-16/flock-cameras-guardrails-missouri-kehoe](https://www.stlpr.org/news-briefs/2026-09-16/flock-cameras-guardrails-missouri-kehoe)

生成摘要时出错

---

## 84. Tell the speakers that you liked their talks

**原文标题**: Tell the speakers that you liked their talks

**原文链接**: [https://ohhelloana.blog/tell-the-speakers/](https://ohhelloana.blog/tell-the-speakers/)

生成摘要时出错

---

## 85. The engineering behind the US Strategic Petroleum Reserve

**原文标题**: The engineering behind the US Strategic Petroleum Reserve

**原文链接**: [https://johnjwang.com/post/2026/09/15/engineering-behind-us-strategic-petroleum-reserve](https://johnjwang.com/post/2026/09/15/engineering-behind-us-strategic-petroleum-reserve)

生成摘要时出错

---

## 86. This PCB is brought to you by Fable 5

**原文标题**: This PCB is brought to you by Fable 5

**原文链接**: [https://a6mzero.com/posts/this-pcb-is-brought-to-you-by-fable-5/](https://a6mzero.com/posts/this-pcb-is-brought-to-you-by-fable-5/)

生成摘要时出错

---

## 87. AWS says it can't restore some data from mideast facilities struck by Iran

**原文标题**: AWS says it can't restore some data from mideast facilities struck by Iran

**原文链接**: [https://www.wsj.com/world/middle-east/aws-says-it-cant-restore-some-data-from-mideast-facilities-struck-by-iran-ddcb7e5d](https://www.wsj.com/world/middle-east/aws-says-it-cant-restore-some-data-from-mideast-facilities-struck-by-iran-ddcb7e5d)

生成摘要时出错

---

## 88. Japan's book scene is moving from bookstores to libraries

**原文标题**: Japan's book scene is moving from bookstores to libraries

**原文链接**: [https://untranslatedjp.substack.com/p/japans-book-scene-is-quietly-moving](https://untranslatedjp.substack.com/p/japans-book-scene-is-quietly-moving)

生成摘要时出错

---

## 89. Douglas Adams and the exterminated Doctor Who adventure

**原文标题**: Douglas Adams and the exterminated Doctor Who adventure

**原文链接**: [https://www.bbc.co.uk/news/articles/c8jdp38z4jgo](https://www.bbc.co.uk/news/articles/c8jdp38z4jgo)

生成摘要时出错

---

## 90. Accurate Models of AMD Matrix Cores

**原文标题**: Accurate Models of AMD Matrix Cores

**原文链接**: [https://arxiv.org/abs/2609.14845](https://arxiv.org/abs/2609.14845)

生成摘要时出错

---

## 91. Back to the future: modules for Guix packages (2022)

**原文标题**: Back to the future: modules for Guix packages (2022)

**原文链接**: [https://hpc.guix.info/blog/2022/05/back-to-the-future-modules-for-guix-packages/](https://hpc.guix.info/blog/2022/05/back-to-the-future-modules-for-guix-packages/)

生成摘要时出错

---

## 92. Performance Improvements in .NET 11

**原文标题**: Performance Improvements in .NET 11

**原文链接**: [https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-11/](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-11/)

生成摘要时出错

---

## 93. Uploading Files to the Internet in Order to Cite Them

**原文标题**: Uploading Files to the Internet in Order to Cite Them

**原文链接**: [https://alignment.openai.com/misalignment-reports/uploading-files-to-the-internet-in-order-to-cite-them/](https://alignment.openai.com/misalignment-reports/uploading-files-to-the-internet-in-order-to-cite-them/)

生成摘要时出错

---

## 94. Doing Everyone Else's Job

**原文标题**: Doing Everyone Else's Job

**原文链接**: [https://yosefk.com/blog/doing-everyone-elses-job.html](https://yosefk.com/blog/doing-everyone-elses-job.html)

生成摘要时出错

---

## 95. Why Arab armies don't win wars

**原文标题**: Why Arab armies don't win wars

**原文链接**: [https://worksinprogress.co/issue/why-arab-armies-dont-win-wars/](https://worksinprogress.co/issue/why-arab-armies-dont-win-wars/)

生成摘要时出错

---

## 96. Tin: full-text search for Postgres

**原文标题**: Tin: full-text search for Postgres

**原文链接**: [https://planetscale.com/blog/introducing-tin](https://planetscale.com/blog/introducing-tin)

生成摘要时出错

---

## 97. Victory Appeals Court Rejects Expansive New Copyright Claim

**原文标题**: Victory Appeals Court Rejects Expansive New Copyright Claim

**原文链接**: [https://www.eff.org/deeplinks/2026/09/victory-appeals-court-rejects-expansive-new-copyright-claim](https://www.eff.org/deeplinks/2026/09/victory-appeals-court-rejects-expansive-new-copyright-claim)

生成摘要时出错

---

## 98. A warning about 'model welfare'

**原文标题**: A warning about 'model welfare'

**原文链接**: [https://mustafa-suleyman.ai/a-warning-about-model-welfare](https://mustafa-suleyman.ai/a-warning-about-model-welfare)

生成摘要时出错

---

## 99. Training Text-to-Image Models 3.6× Faster

**原文标题**: Training Text-to-Image Models 3.6× Faster

**原文链接**: [https://www.linum.ai/field-notes/jit-ddt](https://www.linum.ai/field-notes/jit-ddt)

生成摘要时出错

---

## 100. How big are factorials?

**原文标题**: How big are factorials?

**原文链接**: [https://eli.thegreenplace.net/2026/how-big-are-factorials/](https://eli.thegreenplace.net/2026/how-big-are-factorials/)

生成摘要时出错

---

