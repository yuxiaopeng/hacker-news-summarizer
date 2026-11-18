# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-11-18.md)

*最后自动更新时间: 2026-11-18 00:09:44*
## 1. Java4Shell：OpenJDK 处理 Base64 时存在的远程代码执行漏洞

**原文标题**: Java4Shell: RCE in OpenJDK when processing Base64

**原文链接**: [https://calif.io/java4shell/](https://calif.io/java4shell/)

本文披露了 **Java4Shell** (CVE-2026-114938)，这是 OpenJDK Base64 解码器中一个严重的内存损坏漏洞，其 CVSS 评分高达 9.2。

**技术细节**
该缺陷存在于为了通过 x86-64 AVX-512 VBMI 指令优化 Base64 解码而使用的手写汇编代码中。在处理特定的恶意输入时（例如 64 个“A”字符后跟一个等号），解码器会计算出负的输出长度。这会导致越界写入并覆盖邻近内存，进而可能导致敏感数据泄露或远程代码执行 (RCE)。

**影响与范围**
由于 Base64 是身份验证和数据传输的基础，该漏洞影响了极其广泛的 Java 基础设施。研究人员已在 Jenkins、Atlassian Jira/Confluence、Keycloak 和 Elasticsearch 等广泛使用的应用程序中成功演示了 RCE。服务端和客户端（通过恶意的 TLS 连接）攻击均可行。

**核心主题**
*   **“半人马黑客”：** 该漏洞在短短三小时内通过 AI 代理与人类研究员的协作（即“半人马式黑客攻击”）被发现并武器化，凸显了 AI 如何加速漏洞利用程序的开发。
*   **优化的风险：** 尽管 Java 通常是内存安全的，但其底层性能优化（由 C++ 或汇编编写）绕过了这些保护机制，从而将“传统”内存损坏风险引入了现代技术栈。
*   **Vibe-Uncoding：** 作者主张利用 AI 识别并删除不必要的、臃肿的或“死”代码，以减少攻击面，并称这一过程为 “Vibe-Uncoding”。他们认为，许多系统从其并不真正需要的复杂优化或过时协议（如 FTP）中继承了安全风险。

---

## 2. GPT-6.2 阿斯特拉与索尔

**原文标题**: GPT‑6.2 Astra and Sol

**原文链接**: [https://openai.com/index/introducing-gpt-6-2-astra-sol/](https://openai.com/index/introducing-gpt-6-2-astra-sol/)

无法访问文章链接。

---

## 3. Quad9 撤出法国：煤矿里的金丝雀

**原文标题**: Quad9's withdrawal from France: A canary in the coal mine

**原文链接**: [https://blog.cloudflare.com/quad9-withdrawal-from-france/](https://blog.cloudflare.com/quad9-withdrawal-from-france/)

**摘要：Quad9 撤出法国**

瑞士非营利组织 Quad9 正将其公共 DNS 解析服务撤出法国。此前，法院因该组织拒绝屏蔽涉及侵权的域名而对其处以罚款。Quad9 认为，该裁决使其陷入了两难境地：要么面临毁灭性的诉讼，要么从根本上牺牲其服务的隐私和安全性。

文章强调了此次撤出的几项关键后果：

*   **基础设施立即中断：** 由于 Quad9 不追踪用户，因此无法通知他们服务关停。结果，包括医院、大学和政府机构在内的许多个人和组织可能会在不明原因的情况下突然遭遇断网。
*   **DNS 屏蔽的无效性：** Cloudflare 认为 DNS 屏蔽是一种容易被绕过的“笨拙工具”。它屏蔽的是整个域名而非特定的侵权文件，且无法从互联网上移除实际内容。
*   **日益增长的趋势：** Quad9 并非孤例。此前，思科（Cisco）在类似压力下已将其 OpenDNS 服务撤出多个欧洲国家；目前，Cloudflare、谷歌和思科还面临比利时法院的裁决，要求在 2027 年前开始屏蔽相关网站。
*   **附带损害：** 针对声誉良好且透明的解析服务，会将用户推向信誉较低的匿名服务，而这些服务可能会利用数据牟利，或缺乏恶意软件防护等安全功能。

Cloudflare 及其他行业领导者主张，版权持有者应将反盗版工作的重点放在托管服务商（即内容实际存放地）上，而非基础架构层。他们警告称，对 DNS 解析器持续施加法律压力会威胁开放互联网的稳定性，并开创一个危险的先例，即个别国家可以主宰全球内容的访问权限。目前，Cloudflare 及其同行正就类似裁决提起上诉，以防止互联网服务的进一步碎片化。

---

## 4. jQuery 4.1.0

**原文标题**: jQuery 4.1.0

**原文链接**: [https://github.com/jquery/jquery/releases/tag/4.1.0](https://github.com/jquery/jquery/releases/tag/4.1.0)

2026年11月17日，jQuery 4.1.0 版本与 3.8.0 版本同步发布。此次更新重点在于代码库的现代化、安全性提升，以及对现代 Web 标准兼容性的扩展。

**核心技术更新：**
*   **核心现代化：** 库架构发生了重大转变，放弃了传统的 `getElementsByTagName` 和 `getElementsByClassName` 方法，转而采用更现代的 `querySelectorAll`。同时重构了核心循环以防止数组越界错误。
*   **安全与选择器：** 该版本修复了标识符匹配中的 ReDoS（正则表达式拒绝服务）漏洞。此外，它还包含针对 Safari 27 中正则表达式解释器错误的临时解决方案，并优化了 `jQuery.uniqueSort` 以提升性能。
*   **Ajax 与序列化：** `jqXHR` 对象现在包含 `responseURL` 字段。此外，序列化模块现已支持表单关联的自定义元素，并为传输层（transports）添加了新的回调 API。
*   **XML 与 CSS：** 通过 `createElementNS` 增强了对 XML 文档的支持，并修复了表格样式探测的相关问题。

**文档与社区：**
发布说明中引入了多项组织更新，包括：
*   管理**机器生成（AI）贡献**的指南。
*   新增 **TuxCare** 为商业支持供应商。
*   更新了通过 HeroDevs 获取 jQuery NES（永无止境支持）的链接。

**测试：**
该版本包含了全面的测试套件更新，特别加强了对 SVG 数据、动画和 AJAX 二进制数据的覆盖，并针对 Chrome 和 Internet Explorer 中的特定浏览器行为调整了测试预期。

总体而言，jQuery 4.1.0 展现了在保持其跨浏览器可靠性传统的同时，致力于让该库在现代环境中保持高效与安全的持续努力。

---

## 5. Nvidia stopped disclosing Singapore sales as revenues hit $104B

**原文标题**: Nvidia stopped disclosing Singapore sales as revenues hit $104B

**原文链接**: [https://www.ft.com/content/dbde7a30-548c-4f9d-a4be-7898a0c24dcf](https://www.ft.com/content/dbde7a30-548c-4f9d-a4be-7898a0c24dcf)

在其最新的年度监管文件中，英伟达（Nvidia）已停止单独披露来自新加坡的收入，该市场此前在该公司销售额中占据了极高的份额。这一变化发生在该公司年度总营收飙升126%至609亿美元之际，而近期的季度数据表明其年化营收规模已突破1000亿美元。

历史上，新加坡一直被列为英伟达的主要市场，在2023年底约占其总营收的15%。该国之所以地位显著，主要是因其作为全球数据中心和云服务提供商枢纽的地位。然而，对新加坡的高额销售引发了外界对美国出口管制执行情况的审视。分析师质疑该地区是否被用作向中国运送先进制程AI芯片的“中转站”，而中国目前正面临严厉的美国贸易限制。

英伟达将地理营收归因于客户的“账单地址”而非产品的最终目的地。通过将新加坡重新分类至“其他国家”类别，在半导体技术地缘政治紧张局势加剧的背景下，该公司降低了特定地区销售数据的透明度。

尽管报告方式有所改变，但在AI硬件巨大需求的推动下，英伟达的整体增长势头依然是前所未有的。在应对复杂的贸易法规和不断变化的披露标准的同时，该公司继续主导着全球AI基础设施市场。

---

## 6. MAI Code 2 和 Code 2 Flash

**原文标题**: MAI Code 2 and Code 2 Flash

**原文链接**: [https://microsoft.ai/news/introducing-mai-code-2-and-mai-code-2-flash/](https://microsoft.ai/news/introducing-mai-code-2-and-mai-code-2-flash/)

根据提供的文本，以下是简明摘要：

2026年11月17日，MAI Code 2 系列的衍生版本 MAI Cyber 2 Flash 的相关信息正式发布。公告强调了该新品的两大核心价值主张：领先的安全性和更低的成本。该产品被定位为一种高性能安全解决方案，旨在比以往版本更具价格优势且更易普及。

---

## 7. 

**原文标题**: 350 years ago, Ole Rømer discovered that light has a finite speed

**原文链接**: [https://www.sciencenorway.no/culture-history-history-of-science/350-years-ago-this-man-discovered-that-light-has-a-finite-speed/2737969](https://www.sciencenorway.no/culture-history-history-of-science/350-years-ago-this-man-discovered-that-light-has-a-finite-speed/2737969)

1676年，丹麦天文学家奥勒·罗默（Ole Rømer）证明了光以有限的速度传播，推翻了长期以来认为光是瞬时传播的观念，从而彻底改变了科学界。在巴黎天文台工作期间，罗默花了数年时间观测木星的卫星之一——木卫一。他发现了一个规律：当地球远离木星时，木卫一从木星阴影中出现的时间比预期的要晚；而当地球靠近木星时，出现的时间则比预期的要早。

罗默正确地推断出，这种差异的出现是因为光到达地球时所经过的距离不同。1676年9月，他成功做出公开预言，称11月9日木卫一的出现将比预期晚10分钟。根据他的观测，他估计光穿越地球轨道直径大约需要22分钟。这得出光速约为22.5万公里/秒——虽然比30万公里/秒的实际速度低了约25%，但在17世纪这已是一项了不起的成就。

尽管最初受到了一些质疑，但罗默的发现最终得到了克里斯蒂安·惠更斯和艾萨克·牛顿等著名科学家的支持。50年后，詹姆斯·布拉德利对恒星光行差的观测充分证实了他的结论。

罗默的研究成果至今仍是现代天文学的基石。通过证明光的传播需要时间，他开启了这样一种认知：观测深空等同于回望过去。这一概念对于我们今天研究宇宙的历史和演化至关重要。

---

## 8. Phrack 73 发布

**原文标题**: Phrack 73 Released

**原文链接**: [https://phrack.org/issues/73/introduction_md](https://phrack.org/issues/73/introduction_md)

生成摘要时出错

---

## 9. Highly classified US national security communications network goes down

**原文标题**: Highly classified US national security communications network goes down

**原文链接**: [https://www.cnn.com/2026/11/17/politics/highly-classified-national-security-communications-network-goes-down](https://www.cnn.com/2026/11/17/politics/highly-classified-national-security-communications-network-goes-down)

生成摘要时出错

---

## 10. Java4Shell：Java 17 中的预身份验证 RCE 漏洞使服务器面临风险 (CVE-2026-114938)

**原文标题**: Java4Shell: pre-auth RCE flaw in Java 17 puts servers at risk (CVE-2026-114938)

**原文链接**: [https://www.aikido.dev/blog/java-17-rce-vulnerability-cve-2026-114938](https://www.aikido.dev/blog/java-17-rce-vulnerability-cve-2026-114938)

**Java4Shell (CVE-2026-114938)** is a critical unauthenticated remote code execution (RCE) vulnerability affecting Java 17, 21, 25, and 27. Rated with a high severity score of **9.2 (CVSS 4.0)**, the flaw allows attackers to execute code remotely without authentication. While the vulnerability specifically targets the Java 17 line and newer releases, Oracle Java SE 8 and 11 are confirmed to be unaffected by this specific CVE.

Oracle released emergency patches on November 17, 2026. Organizations are urged to update their Java environments to the following fixed versions (or newer):
*   **Java 17:** 17.0.21.1
*   **Java 21:** 21.0.13.1
*   **Java 25:** 25.0.5.1
*   **Java 27:** 27.0.1.1

The scope of the vulnerability includes various distributions such as Amazon Corretto, Eclipse Temurin, Azul Zulu, and Microsoft Build of OpenJDK, as well as JDKs bundled inside containers and applications. While Amazon Corretto has released fixed builds, other vendors may be on different release schedules.

As of the report date, there have been no confirmed instances of exploitation in the wild. however, technical details are expected to be made public soon, which often leads to a surge in attack attempts. Security experts recommend prioritizing updates for internet-facing services. Currently, no workarounds exist; the only effective mitigation is upgrading to a patched runtime.

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-11-18](output/hacker_news_summary_2026-11-18.md) |
| 2 | [2026-11-17](output/hacker_news_summary_2026-11-17.md) |
| 3 | [2026-11-11](output/hacker_news_summary_2026-11-11.md) |
| 4 | [2026-11-14](output/hacker_news_summary_2026-11-14.md) |
| 5 | [2026-11-10](output/hacker_news_summary_2026-11-10.md) |
| 6 | [2026-11-12](output/hacker_news_summary_2026-11-12.md) |
| 7 | [2026-11-13](output/hacker_news_summary_2026-11-13.md) |
| 8 | [2026-11-15](output/hacker_news_summary_2026-11-15.md) |
| 9 | [2026-11-03](output/hacker_news_summary_2026-11-03.md) |
| 10 | [2026-11-05](output/hacker_news_summary_2026-11-05.md) |
| 11 | [2026-11-06](output/hacker_news_summary_2026-11-06.md) |
| 12 | [2026-11-04](output/hacker_news_summary_2026-11-04.md) |
| 13 | [2026-11-08](output/hacker_news_summary_2026-11-08.md) |
| 14 | [2026-11-07](output/hacker_news_summary_2026-11-07.md) |
| 15 | [2026-10-30](output/hacker_news_summary_2026-10-30.md) |
| 16 | [2026-10-28](output/hacker_news_summary_2026-10-28.md) |
| 17 | [2026-10-31](output/hacker_news_summary_2026-10-31.md) |
| 18 | [2026-11-01](output/hacker_news_summary_2026-11-01.md) |
| 19 | [2026-10-27](output/hacker_news_summary_2026-10-27.md) |
| 20 | [2026-10-29](output/hacker_news_summary_2026-10-29.md) |
| 21 | [2026-10-25](output/hacker_news_summary_2026-10-25.md) |
| 22 | [2026-10-21](output/hacker_news_summary_2026-10-21.md) |
| 23 | [2026-10-23](output/hacker_news_summary_2026-10-23.md) |
| 24 | [2026-10-22](output/hacker_news_summary_2026-10-22.md) |
| 25 | [2026-10-24](output/hacker_news_summary_2026-10-24.md) |
| 26 | [2026-10-26](output/hacker_news_summary_2026-10-26.md) |
| 27 | [2026-10-16](output/hacker_news_summary_2026-10-16.md) |
| 28 | [2026-10-20](output/hacker_news_summary_2026-10-20.md) |
| 29 | [2026-10-17](output/hacker_news_summary_2026-10-17.md) |
| 30 | [2026-10-15](output/hacker_news_summary_2026-10-15.md) |
| 31 | [2026-10-19](output/hacker_news_summary_2026-10-19.md) |
| 32 | [2026-10-18](output/hacker_news_summary_2026-10-18.md) |
| 33 | [2026-10-11](output/hacker_news_summary_2026-10-11.md) |
| 34 | [2026-10-12](output/hacker_news_summary_2026-10-12.md) |
| 35 | [2026-10-10](output/hacker_news_summary_2026-10-10.md) |
| 36 | [2026-10-14](output/hacker_news_summary_2026-10-14.md) |
| 37 | [2026-10-13](output/hacker_news_summary_2026-10-13.md) |
| 38 | [2026-10-09](output/hacker_news_summary_2026-10-09.md) |
| 39 | [2026-10-08](output/hacker_news_summary_2026-10-08.md) |
| 40 | [2026-10-02](output/hacker_news_summary_2026-10-02.md) |
| 41 | [2026-10-03](output/hacker_news_summary_2026-10-03.md) |
| 42 | [2026-10-01](output/hacker_news_summary_2026-10-01.md) |
| 43 | [2026-10-06](output/hacker_news_summary_2026-10-06.md) |
| 44 | [2026-10-04](output/hacker_news_summary_2026-10-04.md) |
| 45 | [2026-10-07](output/hacker_news_summary_2026-10-07.md) |
| 46 | [2026-10-05](output/hacker_news_summary_2026-10-05.md) |
| 47 | [2026-09-26](output/hacker_news_summary_2026-09-26.md) |
| 48 | [2026-09-28](output/hacker_news_summary_2026-09-28.md) |
| 49 | [2026-09-29](output/hacker_news_summary_2026-09-29.md) |
| 50 | [2026-09-25](output/hacker_news_summary_2026-09-25.md) |
| 51 | [2026-09-27](output/hacker_news_summary_2026-09-27.md) |
| 52 | [2026-09-30](output/hacker_news_summary_2026-09-30.md) |
| 53 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 54 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 55 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 56 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 57 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
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
| 71 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 72 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 73 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 74 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 75 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 76 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 77 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 78 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 79 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 80 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 81 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 82 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 83 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 84 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 85 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 86 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 87 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 88 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 89 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 90 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 91 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 92 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 93 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 94 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 95 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 96 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 97 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 98 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 99 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 100 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 101 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 102 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 103 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 104 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 105 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 106 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 107 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 108 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 109 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 110 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 111 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 112 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 113 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 114 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 115 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 116 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 117 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 118 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 119 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 120 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 121 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 122 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 123 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 124 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 125 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 126 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 127 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 128 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 129 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 130 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 131 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 132 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 133 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 134 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 135 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 136 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 137 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 138 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 139 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 140 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 141 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 142 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 143 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 144 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 145 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 146 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 147 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 148 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 149 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 150 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 151 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 152 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 153 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 154 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 155 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 156 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 157 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 158 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 159 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 160 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 161 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 162 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 163 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 164 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 165 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 166 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 167 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 168 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 169 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 170 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 171 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 172 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 173 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 174 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 175 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 176 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 177 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 178 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 179 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 180 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 181 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 182 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 183 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 184 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 185 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 186 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 187 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 188 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 189 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 190 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 191 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 192 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 193 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 194 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 195 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 196 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 197 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 198 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 199 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 200 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 201 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 202 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 203 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 204 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 205 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 206 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 207 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 208 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 209 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 210 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 211 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 212 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 213 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 214 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 215 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 216 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 217 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 218 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 219 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 220 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 221 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 222 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 223 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 224 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 225 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 226 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 227 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 228 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 229 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 230 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 231 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 232 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 233 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 234 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 235 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 236 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 237 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 238 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 239 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 240 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 241 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 242 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 243 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 244 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 245 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 246 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 247 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 248 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 249 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 250 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 251 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 252 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 253 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 254 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 255 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 256 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 257 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 258 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 259 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 260 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 261 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 262 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 263 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 264 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 265 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 266 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 267 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 268 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 269 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 270 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 271 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 272 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 273 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 274 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 275 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 276 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 277 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 278 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 279 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 280 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 281 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 282 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 283 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 284 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 285 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 286 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 287 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 288 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 289 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 290 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 291 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 292 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 293 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 294 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 295 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 296 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 297 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 298 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 299 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 300 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 301 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 302 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 303 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 304 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 305 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 306 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 307 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 308 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 309 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 310 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 311 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 312 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 313 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 314 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 315 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 316 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 317 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 318 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 319 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 320 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 321 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 322 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 323 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 324 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 325 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 326 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 327 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 328 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 329 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 330 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 331 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 332 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 333 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 334 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 335 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 336 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 337 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 338 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 339 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 340 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 341 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 342 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 343 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 344 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 345 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 346 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 347 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 348 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 349 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 350 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 351 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 352 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 353 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 354 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 355 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 356 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 357 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 358 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 359 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 360 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 361 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 362 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 363 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 364 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 365 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 366 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 367 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 368 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 369 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 370 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 371 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 372 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 373 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 374 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 375 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 376 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 377 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 378 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 379 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 380 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 381 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 382 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 383 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 384 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 385 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 386 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 387 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 388 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 389 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 390 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 391 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 392 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 393 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 394 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 395 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 396 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 397 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 398 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 399 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 400 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 401 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 402 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 403 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 404 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 405 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 406 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 407 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 408 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 409 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 410 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 411 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 412 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 413 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 414 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 415 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 416 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 417 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 418 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 419 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 420 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 421 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 422 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 423 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 424 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 425 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 426 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 427 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 428 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 429 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 430 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 431 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 432 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 433 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 434 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 435 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 436 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 437 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 438 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 439 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 440 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 441 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 442 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 443 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 444 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 445 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 446 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 447 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 448 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 449 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 450 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 451 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 452 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 453 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 454 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 455 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 456 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 457 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 458 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 459 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 460 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 461 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 462 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 463 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 464 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 465 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 466 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 467 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 468 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 469 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 470 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 471 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 472 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 473 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 474 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
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
| 485 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 486 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 487 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 488 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 489 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 490 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 491 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 492 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 493 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 494 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 495 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 496 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 497 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 498 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 499 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 500 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 501 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 502 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 503 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 504 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 505 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 506 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 507 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 508 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 509 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 510 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 511 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 512 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 513 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 514 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 515 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 516 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 517 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 518 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 519 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 520 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 521 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 522 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 523 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 524 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 525 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 526 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 527 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 528 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 529 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 530 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 531 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 532 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 533 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 534 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 535 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 536 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 537 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 538 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 539 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 540 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 541 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 542 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 543 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 544 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 545 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 546 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 547 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 548 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 549 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 550 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 551 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 552 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 553 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 554 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 555 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 556 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 557 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 558 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 559 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 560 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 561 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 562 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 563 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 564 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 565 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 566 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 567 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 568 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 569 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 570 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 571 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 572 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 573 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 574 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 575 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 576 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 577 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 578 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 579 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 580 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 581 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 582 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 583 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 584 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 585 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 586 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 587 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 588 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 589 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 590 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 591 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 592 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 593 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 594 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 595 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 596 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 597 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 598 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 599 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 600 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 601 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 602 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 603 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
