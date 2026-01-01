# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-01-01.md)

*最后自动更新时间: 2026-01-01 17:47:36*
## 1. ACM 现已实现开放获取

**原文标题**: ACM Is Now Open Access

**原文链接**: [https://www.acm.org/articles/bulletins/2026/january/acm-open-access](https://www.acm.org/articles/bulletins/2026/january/acm-open-access)

无法访问文章链接。

---

## 2. OpenWorkers：Rust 实现的自托管 Cloudflare Workers

**原文标题**: OpenWorkers: Self-Hosted Cloudflare Workers in Rust

**原文链接**: [https://openworkers.com/introducing-openworkers](https://openworkers.com/introducing-openworkers)

**OpenWorkers** 是一款开源的、基于 Rust 的运行时，旨在私有基础设施上自托管兼容 Cloudflare Workers 的服务。它利用 V8 隔离槽（通过 `rusty_v8`）构建，为执行 JavaScript 和 TypeScript 提供了一个沙箱环境，并设有严格的资源限制（每个 Worker 100ms CPU 和 128MB RAM）。

该平台旨在复刻 Cloudflare 的开发体验，同时避免厂商锁定。其核心特性包括：

*   **API 兼容性：** 支持 `fetch`、`ReadableStream`、`crypto.subtle` 和 `setTimeout` 等标准 Web API。
*   **集成绑定：** 内置支持 KV 存储、PostgreSQL 数据库、兼容 S3/R2 的存储以及服务绑定。
*   **基础设施：** 包含仪表板、API、运行节点和调度器，全部通过 NATS 和 PostgreSQL 进行管理。
*   **部署简便：** 设计追求极致简洁，整个技术栈可通过单个 Docker Compose 文件完成部署。
*   **Cron 定时任务：** 内置支持标准的 Cron 语法。

该项目是七年演进的结晶，经历了从 `vm2` 到 `deno-core`，再到直接使用 Rust 实现的转变。通过自托管，用户可确保数据不离开私有基础设施，并免去按请求计费的模型。未来的更新预计将引入执行录制与重放功能，以实现确定性调试。

---

## 3. 2025 Letter

**原文标题**: 2025 Letter

**原文链接**: [https://danwang.co/2025-letter/](https://danwang.co/2025-letter/)

生成摘要时出错

---

## 4. 在 PHP 中实现 HNSW (Hierarchical Navigable Small World) 向量搜索

**原文标题**: Implementing HNSW (Hierarchical Navigable Small World) Vector Search in PHP

**原文链接**: [https://centamori.com/index.php?slug=hierarchical-navigable-small-world-hnsw-php&lang=en](https://centamori.com/index.php?slug=hierarchical-navigable-small-world-hnsw-php&lang=en)

本文介绍了如何在 PHP 中实现**分级导航小世界 (HNSW)** 算法，以解决线性向量检索效率低下的问题。标准的线性检索 ($O(N)$) 在处理大规模数据集时速度过慢，而 HNSW 通过将数据组织成多层图，将搜索复杂度降低至 $O(\log N)$。

**核心概念：**
*   **层级结构：** HNSW 采用了城市道路的类比。上层充当“高速公路”，节点稀疏且连接跨度大，用于快速跨越；下层则充当“局部街道”，节点密度高，用于精确查找。
*   **搜索过程：** 搜索从最高层开始，以找到与查询点最接近的点。随后，算法通过逐层下降进行“缩放”。到达底层（Level 0）后，它利用优先队列执行贪心搜索。
*   **关键参数：** 性能由两个核心参数决定：**$ef$**（搜索规模），决定了为提升精度而评估的候选者数量；以及 **$M$**，限制每个节点的最大连接数，以平衡内存占用和连通性。
*   **索引构建：** 图是动态构建的。新数据点通过指数概率分布被分配到各层，确保绝大多数点位于 Level 0，而极少数点能进入“高速公路”。每个新节点随后与其最近邻连接，从而维持一张高效的可导航地图。

**重要意义：**
通过从逐一遍历文档转变为利用概率捷径在多维空间中导航，HNSW 使搜索响应时间从数小时缩短至毫秒级。这种架构是现代 AI 应用（包括**检索增强生成 (RAG)** 和推荐系统）的基石。作者通过 **Vektor**（一个用于原生向量搜索的开源 PHP 服务）展示了这些原理。

---

## 5. 蓝牙耳机劫持：开启你手机的钥匙 [视频]

**原文标题**: Bluetooth Headphone Jacking: A Key to Your Phone [video]

**原文链接**: [https://media.ccc.de/v/39c3-bluetooth-headphone-jacking-a-key-to-your-phone](https://media.ccc.de/v/39c3-bluetooth-headphone-jacking-a-key-to-your-phone)

在 39c3 安全会议上，研究人员 Dennis Heinze 和 Frieder Steinmetz 披露了影响达发科技（Airoha）生产的蓝牙音频芯片的关键漏洞（CVE-2025-20700、CVE-2025-20701 和 CVE-2025-20702）。这些芯片被广泛应用于索尼（如 WH-1000XM5 和 XM6）、捷波朗（Jabra）、马歇尔（Marshall）以及拜雅（Beyerdynamic）等知名品牌的高端耳机和耳塞中。

该研究的核心是在 Airoha SDK 中发现的一种名为 RACE 的强大自定义蓝牙协议。该协议允许攻击者通过读写设备的 RAM 和闪存，实现对外设的完全控制。

其影响不仅限于耳机本身。由于智能手机与已配对的外设之间存在高度信任，受损的耳机可被用作攻击手机的门户。通过窃取“蓝牙链路密钥”（Bluetooth Link Key），攻击者可以冒充耳机来绕过安全措施，并获得对配对智能手机功能的未经授权访问。

演讲者旨在实现两个主要目标：
1. **提高用户意识：** 他们强调，许多制造商在向消费者传达此类风险以及提供安全更新方面进度缓慢或成效不彰。
2. **研究与自定义：** 通过发布技术细节和工具，研究人员使他人能够检测自己的设备是否存在漏洞，并可能对固件进行修复或自定义。

最后，这场演讲发出了警示：随着智能手机的安全性能不断提升，攻击者正将重点转向防御较弱的外设，以利用用户个人设备生态系统中的信任关系。

---

## 6. 程序员必知的 Python 数字

**原文标题**: Python Numbers Every Programmer Should Know

**原文链接**: [https://mkennedy.codes/posts/python-numbers-every-programmer-should-know/](https://mkennedy.codes/posts/python-numbers-every-programmer-should-know/)

本文为 Python 开发者提供了全面的性能参考，在 Mac Mini M4 Pro 上对 CPython 3.14.2 进行了基准测试。它详细说明了基础操作的时间和内存开销，旨在帮助程序员做出明智的架构决策。

**主要发现：**

*   **内存效率：** Python 对象具有显著的开销；空字符串占用 41 字节，小整数需要 28 字节。在类中使用 `__slots__` 对扩展极其有效，与普通类相比，在管理大量实例列表时可减少 50% 以上的内存占用。
*   **数据结构：** 选择正确的数据结构至关重要。对于包含 1,000 个元素的容器，集合（set）或字典（dict）的成员检查速度比列表（list）快约 200 倍。此外，列表推导式的执行速度比传统的 `for` 循环配合 `.append()` 快约 20%。
*   **序列化：** 标准 `json` 库的性能已被现代替代方案超越。对于复杂对象的序列化，`orjson` 和 `msgspec` 的速度最高可提升 11 倍。
*   **Web 框架：** 对于简单的 JSON 响应，FastAPI 和 Starlette 等现代异步框架的吞吐量几乎是 Flask 和 Django 的两倍，且延迟显著降低。
*   **持久化：** 进程内存储解决方案（如使用 JSON blob 的 SQLite 和 DiskCache）提供了极快的主键查询速度（3.5–4.2 μs），在简单操作中通常优于 MongoDB 等依赖网络的数据库。
*   **计算开销：** 基本算术和函数调用非常快（纳秒级），但 `asyncio` 的运行机制和异常处理会引入显著开销，使性能耗时进入微秒级。

文章总结指出，尽管 Python 比底层语言慢，但开发者可以通过利用优化库（如 `orjson`）、合适的数据结构（如集合 vs 列表）以及节省内存的特性（如 `__slots__`）来获得高性能。

---

## 7. FFmpeg EXIF 堆溢出

**原文标题**: Heap Overflow in FFmpeg EXIF

**原文链接**: [https://bugs.pwno.io/0014](https://bugs.pwno.io/0014)

FFmpeg 的 EXIF 写入器（`avcodec/exif`）中发现了一个堆缓冲区溢出漏洞，受影响的主要图像格式包括 PNG、JPG、WebP、AVIF 和 JXL。该缺陷存在于图像文件目录（IFD）的处理过程中，特别是涉及分配给内部合成标签（范围从 0xFFFC 到 0xFFED）的“额外 IFD”。

该漏洞源于缓冲区大小计算与写入过程之间的逻辑不匹配。当 FFmpeg 准备写入 EXIF 数据时，函数 `exif_get_ifd_size` 会计算所需的内存。它假设所有合成标签都将被“剥离”（从主 IFD 中移除并重定位），因此为其 12 字节的目录条目分配零字节。

然而，`av_ex_write` 中的“剥离”逻辑从 0xFFFC 开始线性向下扫描这些标签，并在遇到第一个缺失标签时终止。通过在源文件中伪造一个非连续的合成标签（如 0xFFFB），攻击者可以绕过移除过程。这会导致意外的标签残留在主 IFD 列表中。

在写入阶段，写入器尝试将这个未剥离标签的 12 字节条目记录到分配不足的缓冲区中。当代码执行 `AV_WN32` 以清零内联填充时，会导致四字节的越界写入，直接溢出到下一个堆块的元数据中。

该漏洞由 Ruikai Peng 发现，在引入代码库仅三天后就被识别。目前已向 FFmpeg 安全团队报告，并于 2025 年 12 月完成修复。用户应确保更新其 FFmpeg 构建版本以包含该修复补丁。

---

## 8. 索尼 PS5 ROM 密钥遭泄露：利用 BootROM 代码越狱或将更加容易

**原文标题**: Sony PS5 ROM keys leaked – jailbreaking could be made easier with BootROM codes

**原文链接**: [https://www.tomshardware.com/video-games/playstation/playstation-5-rom-keys-leaked-jailbreaking-could-be-made-easier-with-bootrom-codes](https://www.tomshardware.com/video-games/playstation/playstation-5-rom-keys-leaked-jailbreaking-could-be-made-easier-with-bootrom-codes)

**索尼 PS5 ROM 密钥泄露事件综述**

索尼正面临重大的安全挑战，据称 PlayStation 5 的 ROM 密钥已遭到泄露。这些十六进制字符串直接固化在主机的 APU（加速处理器）硬件中，这意味着对于市面上已售出的主机，该漏洞无法通过软件更新进行修复。

**技术影响**
泄露的密钥允许研究人员和黑客解密并分析 PS5 的 BootROM 和引导加载程序（bootloader）。这是 CPU 在启动时为验证系统完整性而运行的初始代码。通过了解这一过程，黑客在识别 PS5 底层安全机制运作原理方面获得了基础性优势。

**未来影响**
虽然由于索尼采用了多层安全机制，此次泄露并不能立即实现“一键越狱”，但它显著降低了开发自定义固件或替代操作系统的门槛。由于该缺陷存在于硬件层面，索尼无法使现有设备的密钥失效；他们只能在未来的生产批次中使用修正后的芯片来解决此问题。

**背景与先例**
历史上，类似的硬件级漏洞也曾影响过其他游戏机，例如 PlayStation 3 的加密错误和 Nintendo Switch 的 Tegra X1 漏洞。

**索尼的回应**
索尼尚未发布官方声明。虽然该公司可能会推出修正后的硬件以确保未来设备的安全，但考虑到高昂的成本和物流复杂性，召回现有主机被认为极不可能。就目前而言，由于这次泄露，现有的 PS5 用户最终可能会看到一条通往自制软件和深度系统修改的道路。

---

## 9. Common Lisp SDK for the Datastar Hypermedia Framework

**原文标题**: Common Lisp SDK for the Datastar Hypermedia Framework

**原文链接**: [https://github.com/fsmunoz/datastar-cl](https://github.com/fsmunoz/datastar-cl)

生成摘要时出错

---

## 10. iOS allows alternative browser engines in Japan

**原文标题**: iOS allows alternative browser engines in Japan

**原文链接**: [https://developer.apple.com/support/alternative-browser-engines-jp/](https://developer.apple.com/support/alternative-browser-engines-jp/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 2 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 3 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 4 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 5 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 6 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 7 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 8 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 9 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 10 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 11 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 12 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 13 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 14 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 15 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 16 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 17 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 18 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 19 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 20 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 21 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 22 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 23 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 24 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 25 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 26 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 27 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 28 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 29 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 30 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 31 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 32 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 33 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 34 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 35 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 36 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 37 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 38 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 39 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 40 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 41 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 42 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 43 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 44 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 45 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 46 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 47 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 48 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 49 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 50 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 51 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 52 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 53 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 54 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 55 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 56 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 57 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 58 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 59 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 60 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 61 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 62 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 63 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 64 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 65 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 66 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 67 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 68 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 69 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 70 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 71 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 72 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 73 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 74 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 75 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 76 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 77 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 78 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 79 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 80 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 81 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 82 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 83 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 84 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 85 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 86 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 87 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 88 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 89 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 90 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 91 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 92 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 93 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 94 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 95 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 96 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 97 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 98 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 99 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 100 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 101 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 102 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 103 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 104 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 105 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 106 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 107 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 108 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 109 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 110 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 111 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 112 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 113 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 114 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 115 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 116 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 117 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 118 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 119 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 120 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 121 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 122 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 123 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 124 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 125 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 126 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 127 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 128 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 129 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 130 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 131 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 132 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 133 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 134 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 135 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 136 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 137 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 138 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 139 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 140 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 141 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 142 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 143 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 144 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 145 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 146 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 147 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 148 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 149 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 150 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 151 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 152 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 153 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 154 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 155 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 156 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 157 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 158 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 159 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 160 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 161 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 162 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 163 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 164 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 165 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 166 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 167 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 168 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 169 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 170 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 171 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 172 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 173 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 174 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 175 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 176 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 177 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 178 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 179 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 180 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 181 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 182 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 183 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 184 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 185 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 186 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 187 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 188 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 189 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 190 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 191 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 192 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 193 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 194 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 195 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 196 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 197 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 198 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 199 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 200 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 201 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 202 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 203 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 204 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 205 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 206 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 207 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 208 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 209 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 210 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 211 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 212 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 213 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 214 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 215 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 216 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 217 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 218 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 219 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 220 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 221 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 222 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 223 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 224 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 225 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 226 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 227 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 228 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 229 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 230 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 231 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 232 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 233 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 234 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 235 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 236 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 237 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 238 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 239 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 240 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 241 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 242 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 243 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 244 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 245 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 246 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 247 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 248 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 249 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 250 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 251 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 252 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 253 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 254 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 255 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 256 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 257 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 258 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 259 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 260 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 261 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 262 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 263 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 264 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 265 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 266 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 267 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 268 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 269 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 270 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 271 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 272 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 273 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 274 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 275 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 276 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 277 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 278 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 279 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 280 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 281 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 282 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 283 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 284 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 285 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 286 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 287 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
