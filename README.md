# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-10-21.md)

*最后自动更新时间: 2026-10-21 20:55:03*
## 1. Mistral Large 4

**原文标题**: Mistral Large 4

**原文链接**: [https://docs.mistral.ai/models/mistral-large-4-0](https://docs.mistral.ai/models/mistral-large-4-0)

**Mistral Large 4** (v26.10) 于 2026 年 10 月 6 日发布，是一款最先进的开放权重多模态模型，现已提供公开预览。它采用了细粒度的混合专家 (MoE) 架构，专为高性能、通用人工智能任务而设计。

**技术规格**
该模型规模庞大，拥有 **1.05 万亿总参数**，推理期间的**激活参数为 520 亿**。它包含一个专门的 **16 亿参数视觉编码器**，使其能够无缝处理文本和视觉数据。值得注意的是，它支持高达 **100 万 token** 的超大上下文窗口。

**能力与特性**
Mistral Large 4 专为复杂的开发者工作流构建，为以下功能提供强大支持：
*   **结构化输出**与**函数调用**。
*   **文档问答**与**前缀填充 (Prefixing)**。
*   具备内置工具的**智能体与对话**。
*   通过 `/v1/batch` 端点进行**批处理**。

**定价 (美元)**
该模型采用基于每百万 token 的分层定价结构：
*   **输入：** $1.36
*   **缓存输入：** $0.14
*   **输出：** $4.18

此次发布将 Mistral Large 4 定位为专有模型极具竞争力的开放权重替代方案，为高级智能体和文档密集型应用提供庞大的规模和多模态能力。

---

## 2. 今日 PHP 安全版本发布，以及我们如何加强安全性

**原文标题**: Today's PHP security release, and how we're strengthening security

**原文链接**: [https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/)

2026年10月21日，PHP基金会发布了关键安全版本（版本号 8.5.12、8.4.27、8.3.36 和 8.2.35），以修复两个重大的远程代码执行（RCE）漏洞：**CVE-2026-109618**（内存溢出损坏）和 **CVE-2026-109619**（内部状态陈旧）。这些存在于 PHP 核心内存管理和错误处理机制中的缺陷，可能允许未经身份验证的攻击者在服务器上执行恶意代码。

基金会承认，尽管在2024年的一次审计中就已发现内存溢出（OOM）问题的迹象，但由于安全团队决策过程中的“结构性失败”以及资源的匮乏，导致修复工作停滞了数月。为解决这些系统性问题，基金会此后通过以下措施扩展了其安全基础设施：
*   成立**生态系统安全团队 (Ecosystem Security Team)**。
*   聘请专职的安全工程师和人工智能（AI）工程师。
*   整合 AI 辅助工具（如 Claude Mythos 和 OpenAI Daybreak Red）用于漏洞扫描和报告分级。
*   与 Calif、Wiz 和 Trail of Bits 等外部公司合作进行深度审计。

10月20日，由于网络信息泄露以及 Chainguard 违反披露禁令，这些漏洞的协调披露过程受到干扰。这迫使 PHP 项目组将发布时间提前了24小时，以便在平衡下游分销商需求的同时保护用户安全。

文章最后呼吁各方提供可持续的资金支持。尽管 PHP 驱动着全球互联网的绝大部分，但其安全性却依赖于极少数专家。基金会敦促企业、托管服务商和政府提供资金赞助，以帮助壮大核心工程师团队，并确保结构性漏洞在演变成紧急状况之前得到妥善处理。

---

## 3. Google Rust 风格指南

**原文标题**: Google's Rust Style Guide

**原文链接**: [https://google.github.io/styleguide/rustguide.html](https://google.github.io/styleguide/rustguide.html)

Google 的 Rust 风格指南为 Android、Chromium 和 Fuchsia 等重大项目确立了一致性、可读性和可维护性的标准。除了格式规范，该指南还强调 API 与实现设计，旨在促进大规模变更 (LSCs) 和工具辅助的重构。

**核心原则与组织：**
指南要求遵循官方 Rust 风格规则，除非其与内部目标冲突。在代码组织方面，尤其是在 Chromium 中，鼓励使用小型、单一用途的 crate 和扁平的文件布局。为了保持清晰，开发者应避免通配符导入 (glob imports) 和 use 语句嵌套。顶层函数应带上模块名限定（例如 `mem::transmute`），而类型则应在导入后直接使用，无需限定。

**API 与实现设计：**
指南区分了库代码（严格规则）和应用代码（强力推荐）。关键设计偏好包括：
*   **数据处理：** 倾向于借用而非深拷贝，并尽可能避免使用 `Rc`/`Arc`。
*   **清晰度：** 使用枚举而非布尔值，以构建更具描述性的 API。
*   **Trait：** 优先实现标准库 trait（如 `Default` 或 `From`），而非创建自定义方法。
*   **错误处理：** 相比 `.unwrap()`，更倾向于模式匹配和 `.expect()`，并在断言中使用上下文字符串。

**特定约束：**
在 Chromium 等特定环境中存在更严格的限制，包括禁用 `async/await` 和标准库线程。此外，指南不建议使用不稳定特性、命名缩写以及会掩盖逻辑的复杂迭代器链。

最终，该指南将代码的可读性和可重构性置于编写速度之上，以确保 Google 庞大的多语言代码库的长期健康。

---

## 4. GitLab CVSS 10.0 整数溢出漏洞

**原文标题**: GitLab CVSS 10.0 Integer Overflow issue

**原文链接**: [https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-5-1-released/](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-5-1-released/)

2026年10月21日，GitLab 发布了针对社区版 (CE) 和企业版 (EE) 的关键安全补丁，以修复多个漏洞。此次更新涵盖了 19.5.1、19.4.3、19.3.6、19.2.9、19.1.9、19.0.10 和 18.11.13 版本。

**修复的主要漏洞：**
*   **CVE-2026-110264 (CVSS 10.0)：** 最严重的问题是正则表达式编译器中的整数溢出。这一关键缺陷允许未经身份验证的攻击者通过精心构造的正则表达式，在 GitLab 服务器上执行任意代码。GitLab 已提供具体的威胁检测指导（如监控 Onigmo 工作进程崩溃），以帮助管理员识别潜在的攻击行为。
*   **CVE-2026-15723 (CVSS 8.2)：** 一个高危身份验证不当问题。在启用 OmniAuth 和 LDAP 自动链接的情况下，经过身份验证的用户可能会接管现有的 LDAP 关联账户。
*   **CVE-2026-112212 (CVSS 7.5)：** OAuth/OIDC 发现端点中的高危缓存中毒漏洞，可能导致用户被重定向到外部控制的恶意服务器。
*   **其他问题：** 补丁还解决了多个中低风险漏洞，包括 GraphQL 访问控制绕过、内部凭据泄露、通过绕过 SAML/LDAP 锁定进行的未经授权成员添加，以及对 AI Gateway 功能的未经授权访问。

**建议采取的措施：**
GitLab 强烈建议所有自托管实例管理员立即升级到最新的补丁版本。虽然 GitLab.com 和 GitLab Dedicated 已受保护，但自托管安装在更新前仍面临风险。除安全修复外，这些版本还包含了针对 CI 变量、仓库备份和工作项管理的多项功能性缺陷修复。

---

## 5. Why Windows 11 still ships with Windows 95's memory manager hidden inside it

**原文标题**: Why Windows 11 still ships with Windows 95's memory manager hidden inside it

**原文链接**: [https://www.windowslatest.com/2026/10/19/why-windows-11-still-ships-with-windows-95s-memory-manager-hidden-inside-it/](https://www.windowslatest.com/2026/10/19/why-windows-11-still-ships-with-windows-95s-memory-manager-hidden-inside-it/)

生成摘要时出错

---

## 6. Compromised LiteLLM 1.107.0 on PyPI Installs a Credential Stealer and Backdoor

**原文标题**: Compromised LiteLLM 1.107.0 on PyPI Installs a Credential Stealer and Backdoor

**原文链接**: [https://safedep.io/litellm-pypi-compromise-credential-stealer-backdoor/](https://safedep.io/litellm-pypi-compromise-credential-stealer-backdoor/)

生成摘要时出错

---

## 7. 八位信任：eMudhra 的 CA 密钥在毫秒内被破解

**原文标题**: Eight Bits of Trust: eMudhra's CA keys cracked in milliseconds

**原文链接**: [https://scotthelme.co.uk/eight-bits-of-trust-emudhras-ca-keys-cracked-in-milliseconds/](https://scotthelme.co.uk/eight-bits-of-trust-emudhras-ca-keys-cracked-in-milliseconds/)

2026年10月，一家名为 eMudhra 的证书颁发机构（CA）被曝出重大安全漏洞。研究人员发现，eMudhra 用于 TLS 和代码签名的八个中间证书私钥存在严重的安全性缺陷。这些私钥本应是 P-384 椭圆曲线所要求的 384 位随机数，结果却只是单字节数值（例如 4、56 和 115）。这使得安全性从 $2^{384}$ 种可能性骤降至仅 256 种，导致私钥在毫秒内即可被破解。

这些受损证书创建于 2025 年 4 月，并由 Sectigo 进行了交叉签名，对全球公钥基础设施（PKI）构成了巨大风险。虽然 Chrome、Firefox 和 Safari 等主流浏览器迅速吊销了这些证书，并利用证书透明度（CT）机制防止其被滥用，但文章强调了显著的“长尾”风险。许多非浏览器客户端——包括 `curl`、Python、Node.js、CI/CD 流水线和物联网（IoT）设备——默认并不会检查吊销状态或 CT 日志。

因此，这些系统仍然面临中间人（MitM）攻击和恶意代码签名的威胁。攻击者可以利用还原出的密钥，为高价值域名（如 `api.stripe.com`）伪造证书，而存在漏洞的客户端会盲目信任这些证书。

该事件被追溯至 eMudhra 在密钥生成典礼中的脚本错误和人为失误。作者强调，尽管现代浏览器是安全的，但更广泛的生态系统必须立即更新 CA 证书包。然而，物联网和老旧设备中“冻结”的固件可能在 2039 年证书自然到期前，始终处于易受攻击的状态。

---

## 8. DuckDB 2.0.0 LTS “肉桂色青翅鸭”

**原文标题**: DuckDB 2.0.0 LTS “Cinnamon Teal”

**原文链接**: [https://duckdb.org/2026/10/21/announcing-duckdb-200](https://duckdb.org/2026/10/21/announcing-duckdb-200)

DuckDB has announced the release of version **2.0.0 LTS**, codenamed **“Cinnamon Teal.”** While version 1.0 focused on stability, this major update is a feature-heavy release providing long-term support until at least October 2027.

**Key Features and Performance**
*   **Asynchronous I/O:** Introduces background I/O processing for Parquet and CSV files, significantly increasing parallelism and speed when querying object storage like Amazon S3.
*   **VARIANT Type:** Now a first-class citizen, the `VARIANT` type supports semi-structured, schema-less data (like JSON) while maintaining columnar execution performance through "shredding."
*   **DuckDB as a Server:** The "Quack" protocol is now polished for stable client-server setups. A new `CONNECT` statement allows seamless switching between remote databases, including PostgreSQL and MySQL, with remote query pushdown.
*   **Agent Mode:** The CLI now detects AI coding agents (like Claude or Cursor), switching to a mode that provides Markdown tables, truncated results, and JSON error reporting to optimize LLM performance.

**Extensibility and SQL Improvements**
*   **New SQL Parser:** A modern, PEG-based parser replaces the legacy PostgreSQL-derived version, allowing extensions to modify the SQL grammar itself. 
*   **Custom Extension Repositories:** Users can now host, sign, and distribute their own trusted extension repositories.
*   **Triggers:** Comprehensive support for `BEFORE` and `AFTER` triggers enables advanced auditing and the manual creation of incremental materialized views.
*   **Dialect Additions:** New features include data-modifying CTEs (`INSERT/UPDATE` in pipelines), similarity-based `NEAREST` joins for vector workloads, and nested schemas.

**Migration**
DuckDB 2.0 remains backward compatible with older database files. However, files created or modified in version 2.0 cannot be read by versions 1.x. Users are advised to test the update on shadow systems before migrating critical production workloads.

---

## 9. EA 正在关闭 BioWare

**原文标题**: EA is shutting down BioWare

**原文链接**: [https://www.theverge.com/games/1015647/ea-is-shutting-down-bioware](https://www.theverge.com/games/1015647/ea-is-shutting-down-bioware)

生成摘要时出错

---

## 10. After automation: Solo founding will be the default

**原文标题**: After automation: Solo founding will be the default

**原文链接**: [https://every.to/thesis-statements/julian-weisser](https://every.to/thesis-statements/julian-weisser)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-10-21](output/hacker_news_summary_2026-10-21.md) |
| 2 | [2026-10-20](output/hacker_news_summary_2026-10-20.md) |
| 3 | [2026-10-19](output/hacker_news_summary_2026-10-19.md) |
| 4 | [2026-10-16](output/hacker_news_summary_2026-10-16.md) |
| 5 | [2026-10-18](output/hacker_news_summary_2026-10-18.md) |
| 6 | [2026-10-17](output/hacker_news_summary_2026-10-17.md) |
| 7 | [2026-10-15](output/hacker_news_summary_2026-10-15.md) |
| 8 | [2026-10-14](output/hacker_news_summary_2026-10-14.md) |
| 9 | [2026-10-11](output/hacker_news_summary_2026-10-11.md) |
| 10 | [2026-10-09](output/hacker_news_summary_2026-10-09.md) |
| 11 | [2026-10-12](output/hacker_news_summary_2026-10-12.md) |
| 12 | [2026-10-08](output/hacker_news_summary_2026-10-08.md) |
| 13 | [2026-10-07](output/hacker_news_summary_2026-10-07.md) |
| 14 | [2026-10-13](output/hacker_news_summary_2026-10-13.md) |
| 15 | [2026-10-10](output/hacker_news_summary_2026-10-10.md) |
| 16 | [2026-09-30](output/hacker_news_summary_2026-09-30.md) |
| 17 | [2026-10-05](output/hacker_news_summary_2026-10-05.md) |
| 18 | [2026-09-29](output/hacker_news_summary_2026-09-29.md) |
| 19 | [2026-10-06](output/hacker_news_summary_2026-10-06.md) |
| 20 | [2026-10-01](output/hacker_news_summary_2026-10-01.md) |
| 21 | [2026-10-04](output/hacker_news_summary_2026-10-04.md) |
| 22 | [2026-10-02](output/hacker_news_summary_2026-10-02.md) |
| 23 | [2026-10-03](output/hacker_news_summary_2026-10-03.md) |
| 24 | [2026-09-28](output/hacker_news_summary_2026-09-28.md) |
| 25 | [2026-09-27](output/hacker_news_summary_2026-09-27.md) |
| 26 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 27 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 28 | [2026-09-26](output/hacker_news_summary_2026-09-26.md) |
| 29 | [2026-09-25](output/hacker_news_summary_2026-09-25.md) |
| 30 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 31 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 32 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 33 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 34 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 35 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 36 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 37 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 38 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 39 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 40 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 41 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 42 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 43 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 44 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 45 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 46 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 47 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 48 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 49 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 50 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 51 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 52 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 53 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 54 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 55 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 56 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 57 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 58 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 59 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 60 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 61 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 62 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 63 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 64 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 65 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 66 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 67 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 68 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 69 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 70 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 71 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 72 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 73 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 74 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 75 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 76 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 77 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 78 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 79 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 80 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 81 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 82 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 83 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 84 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 85 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 86 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 87 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 88 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 89 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 90 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 91 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 92 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 93 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 94 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 95 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 96 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 97 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 98 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 99 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 100 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 101 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 102 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 103 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 104 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 105 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 106 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 107 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 108 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 109 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 110 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 111 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 112 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 113 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 114 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 115 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 116 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 117 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 118 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 119 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 120 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 121 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 122 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 123 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 124 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 125 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 126 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 127 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 128 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 129 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 130 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 131 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 132 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 133 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 134 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 135 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 136 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 137 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 138 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 139 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 140 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 141 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 142 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 143 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 144 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 145 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 146 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 147 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 148 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 149 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 150 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 151 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 152 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 153 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 154 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 155 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 156 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 157 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 158 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 159 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 160 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 161 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 162 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 163 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 164 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 165 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 166 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 167 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 168 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 169 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 170 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 171 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 172 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 173 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 174 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 175 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 176 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 177 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 178 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 179 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 180 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 181 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 182 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 183 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 184 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 185 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 186 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 187 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 188 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 189 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 190 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 191 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 192 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 193 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 194 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 195 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 196 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 197 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 198 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 199 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 200 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 201 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 202 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 203 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 204 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 205 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 206 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 207 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 208 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 209 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 210 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 211 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 212 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 213 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 214 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 215 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 216 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 217 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 218 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 219 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 220 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 221 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 222 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 223 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 224 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 225 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 226 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 227 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 228 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 229 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 230 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 231 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 232 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 233 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 234 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 235 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 236 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 237 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 238 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 239 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 240 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 241 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 242 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 243 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 244 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 245 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 246 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 247 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 248 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 249 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 250 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 251 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 252 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 253 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 254 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 255 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 256 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 257 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 258 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 259 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 260 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 261 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 262 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 263 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 264 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 265 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 266 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 267 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 268 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 269 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 270 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 271 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 272 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 273 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 274 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 275 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 276 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 277 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 278 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 279 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 280 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 281 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 282 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 283 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 284 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 285 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 286 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 287 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 288 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 289 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 290 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 291 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 292 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 293 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 294 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 295 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 296 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 297 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 298 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 299 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 300 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 301 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 302 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 303 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 304 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 305 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 306 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 307 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 308 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 309 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 310 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 311 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 312 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 313 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 314 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 315 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 316 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 317 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 318 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 319 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 320 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 321 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 322 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 323 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 324 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 325 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 326 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 327 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 328 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 329 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 330 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 331 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 332 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 333 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 334 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 335 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 336 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 337 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 338 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 339 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 340 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 341 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 342 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 343 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 344 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 345 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 346 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 347 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 348 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 349 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 350 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 351 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 352 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 353 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 354 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 355 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 356 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 357 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 358 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 359 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 360 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 361 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 362 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 363 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 364 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 365 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 366 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 367 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 368 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 369 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 370 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 371 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 372 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 373 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 374 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 375 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 376 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 377 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 378 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 379 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 380 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 381 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 382 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 383 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 384 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 385 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 386 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 387 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 388 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 389 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 390 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 391 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 392 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 393 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 394 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 395 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 396 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 397 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 398 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 399 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 400 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 401 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 402 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 403 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 404 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 405 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 406 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 407 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 408 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 409 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 410 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 411 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 412 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 413 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 414 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 415 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 416 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 417 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 418 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 419 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 420 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 421 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 422 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 423 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 424 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 425 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 426 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 427 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 428 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 429 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 430 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 431 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 432 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 433 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 434 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 435 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 436 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 437 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 438 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 439 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 440 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 441 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 442 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 443 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 444 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 445 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 446 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 447 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 448 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 449 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 450 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 451 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 452 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 453 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 454 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 455 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 456 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 457 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 458 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 459 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 460 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 461 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 462 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 463 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 464 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 465 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 466 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 467 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 468 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 469 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 470 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 471 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 472 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 473 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 474 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 475 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 476 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 477 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 478 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 479 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 480 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 481 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 482 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 483 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 484 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 485 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 486 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 487 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 488 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 489 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 490 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 491 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 492 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 493 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 494 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 495 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 496 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 497 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 498 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 499 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 500 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 501 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 502 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 503 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 504 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 505 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 506 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 507 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 508 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 509 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 510 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 511 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 512 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 513 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 514 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 515 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 516 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 517 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 518 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 519 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 520 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 521 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 522 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 523 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 524 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 525 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 526 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 527 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 528 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 529 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 530 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 531 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 532 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 533 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 534 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 535 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 536 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 537 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 538 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 539 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 540 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 541 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 542 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 543 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 544 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 545 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 546 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 547 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 548 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 549 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 550 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 551 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 552 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 553 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 554 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 555 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 556 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 557 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 558 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 559 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 560 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 561 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 562 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 563 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 564 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 565 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 566 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 567 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 568 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 569 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 570 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 571 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 572 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 573 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 574 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 575 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 576 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 577 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 578 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
