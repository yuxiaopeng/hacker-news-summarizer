# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-09-17.md)

*最后自动更新时间: 2026-09-17 20:30:40*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 2 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 3 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 4 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 5 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 6 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 7 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 8 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 9 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 10 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 11 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 12 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 13 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 14 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 15 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 16 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 17 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 18 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 19 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 20 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 21 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 22 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 23 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 24 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 25 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 26 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 27 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 28 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 29 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 30 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 31 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 32 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 33 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 34 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 35 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 36 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 37 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 38 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 39 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 40 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 41 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 42 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 43 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 44 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 45 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 46 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 47 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 48 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 49 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 50 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 51 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 52 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 53 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 54 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 55 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 56 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 57 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 58 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 59 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 60 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 61 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 62 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 63 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 64 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 65 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 66 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 67 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 68 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 69 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 70 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 71 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 72 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 73 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 74 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 75 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 76 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 77 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 78 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 79 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 80 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 81 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 82 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 83 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 84 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 85 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 86 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 87 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 88 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 89 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 90 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 91 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 92 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 93 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 94 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 95 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 96 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 97 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 98 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 99 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 100 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 101 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 102 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 103 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 104 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 105 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 106 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 107 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 108 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 109 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 110 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 111 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 112 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 113 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 114 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 115 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 116 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 117 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 118 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 119 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 120 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 121 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 122 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 123 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 124 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 125 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 126 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 127 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 128 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 129 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 130 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 131 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 132 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 133 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 134 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 135 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 136 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 137 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 138 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 139 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 140 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 141 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 142 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 143 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 144 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 145 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 146 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 147 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 148 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 149 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 150 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 151 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 152 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 153 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 154 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 155 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 156 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 157 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 158 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 159 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 160 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 161 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 162 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 163 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 164 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 165 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 166 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 167 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 168 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 169 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 170 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 171 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 172 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 173 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 174 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 175 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 176 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 177 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 178 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 179 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 180 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 181 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 182 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 183 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 184 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 185 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 186 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 187 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 188 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 189 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 190 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 191 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 192 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 193 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 194 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 195 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 196 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 197 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 198 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 199 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 200 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 201 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 202 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 203 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 204 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 205 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 206 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 207 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 208 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 209 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 210 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 211 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 212 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 213 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 214 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 215 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 216 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 217 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 218 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 219 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 220 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 221 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 222 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 223 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 224 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 225 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 226 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 227 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 228 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 229 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 230 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 231 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 232 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 233 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 234 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 235 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 236 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 237 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 238 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 239 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 240 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 241 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 242 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 243 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 244 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 245 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 246 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 247 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 248 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 249 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 250 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 251 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 252 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 253 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 254 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 255 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 256 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 257 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 258 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 259 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 260 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 261 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 262 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 263 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 264 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 265 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 266 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 267 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 268 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 269 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 270 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 271 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 272 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 273 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 274 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 275 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 276 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 277 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 278 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 279 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 280 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 281 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 282 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 283 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 284 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 285 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 286 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 287 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 288 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 289 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 290 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 291 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 292 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 293 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 294 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 295 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 296 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 297 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 298 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 299 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 300 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 301 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 302 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 303 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 304 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 305 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 306 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 307 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 308 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 309 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 310 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 311 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 312 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 313 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 314 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 315 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 316 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 317 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 318 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 319 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 320 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 321 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 322 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 323 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 324 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 325 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 326 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 327 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 328 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 329 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 330 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 331 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 332 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 333 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 334 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 335 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 336 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 337 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 338 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 339 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 340 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 341 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 342 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 343 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 344 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 345 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 346 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 347 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 348 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 349 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 350 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 351 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 352 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 353 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 354 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 355 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 356 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 357 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 358 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 359 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 360 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 361 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 362 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 363 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 364 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 365 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 366 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 367 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 368 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 369 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 370 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 371 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 372 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 373 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 374 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 375 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 376 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 377 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 378 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 379 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 380 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 381 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 382 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 383 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 384 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 385 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 386 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 387 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 388 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 389 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 390 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 391 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 392 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 393 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 394 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 395 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 396 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 397 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 398 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 399 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 400 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 401 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 402 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 403 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 404 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 405 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 406 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 407 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 408 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 409 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 410 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 411 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 412 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 413 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 414 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 415 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 416 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 417 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 418 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 419 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 420 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 421 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 422 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 423 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 424 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 425 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 426 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 427 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 428 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 429 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 430 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 431 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 432 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 433 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 434 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 435 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 436 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 437 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 438 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 439 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 440 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 441 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 442 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 443 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 444 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 445 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 446 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 447 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 448 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 449 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 450 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 451 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 452 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 453 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 454 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 455 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 456 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 457 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 458 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 459 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 460 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 461 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 462 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 463 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 464 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 465 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 466 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 467 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 468 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 469 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 470 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 471 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 472 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 473 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 474 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 475 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 476 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 477 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 478 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 479 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 480 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 481 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 482 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 483 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 484 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 485 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 486 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 487 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 488 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 489 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 490 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 491 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 492 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 493 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 494 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 495 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 496 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 497 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 498 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 499 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 500 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 501 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 502 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 503 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 504 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 505 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 506 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 507 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 508 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 509 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 510 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 511 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 512 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 513 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 514 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 515 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 516 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 517 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 518 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 519 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 520 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 521 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 522 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 523 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 524 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 525 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 526 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 527 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 528 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 529 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 530 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 531 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 532 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 533 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 534 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 535 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 536 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 537 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 538 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 539 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 540 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 541 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 542 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 543 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 544 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
