# Hacker News 热门文章摘要 (2026-01-01)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Build a Deep Learning Library

**原文标题**: Build a Deep Learning Library

**原文链接**: [https://zekcrates.quarto.pub/deep-learning-library/](https://zekcrates.quarto.pub/deep-learning-library/)

生成摘要时出错

---

## 12. 2025: The Year in LLMs

**原文标题**: 2025: The Year in LLMs

**原文链接**: [https://simonwillison.net/2025/Dec/31/the-year-in-llms/](https://simonwillison.net/2025/Dec/31/the-year-in-llms/)

生成摘要时出错

---

## 13. BYD Sells 4.6M Vehicles in 2025, Meets Revised Sales Goal

**原文标题**: BYD Sells 4.6M Vehicles in 2025, Meets Revised Sales Goal

**原文链接**: [https://www.bloomberg.com/news/articles/2026-01-01/byd-sells-4-6-million-vehicles-in-2025-meets-revised-sales-goal](https://www.bloomberg.com/news/articles/2026-01-01/byd-sells-4-6-million-vehicles-in-2025-meets-revised-sales-goal)

生成摘要时出错

---

## 14. Ultra-Wide Band: A Transformational Technology for the Internet of Things

**原文标题**: Ultra-Wide Band: A Transformational Technology for the Internet of Things

**原文链接**: [https://www.eetimes.com/ultra-wide-band-a-transformational-technology-for-the-internet-of-things/](https://www.eetimes.com/ultra-wide-band-a-transformational-technology-for-the-internet-of-things/)

生成摘要时出错

---

## 15. Meta made scam ads harder to find instead of removing them

**原文标题**: Meta made scam ads harder to find instead of removing them

**原文链接**: [https://sherwood.news/tech/rather-than-fully-cracking-down-on-scam-ads-meta-worked-to-make-them-harder/](https://sherwood.news/tech/rather-than-fully-cracking-down-on-scam-ads-meta-worked-to-make-them-harder/)

生成摘要时出错

---

## 16. European Space Agency hit again as cybercriminals claim 200 GB data up for sale

**原文标题**: European Space Agency hit again as cybercriminals claim 200 GB data up for sale

**原文链接**: [https://www.theregister.com/2025/12/31/european_space_agency_hacked/](https://www.theregister.com/2025/12/31/european_space_agency_hacked/)

生成摘要时出错

---

## 17. Easel Turns One One year of building my own IDE in Clojure

**原文标题**: Easel Turns One One year of building my own IDE in Clojure

**原文链接**: [https://blog.phronemophobic.com/easel-one-year.html](https://blog.phronemophobic.com/easel-one-year.html)

生成摘要时出错

---

## 18. A font with built-in TeX syntax highlighting

**原文标题**: A font with built-in TeX syntax highlighting

**原文链接**: [https://rajeeshknambiar.wordpress.com/2025/12/27/a-font-with-built-in-tex-syntax-highlighting/](https://rajeeshknambiar.wordpress.com/2025/12/27/a-font-with-built-in-tex-syntax-highlighting/)

生成摘要时出错

---

## 19. I canceled my book deal

**原文标题**: I canceled my book deal

**原文链接**: [https://austinhenley.com/blog/canceledbookdeal.html](https://austinhenley.com/blog/canceledbookdeal.html)

生成摘要时出错

---

## 20. I rebooted my social life

**原文标题**: I rebooted my social life

**原文链接**: [https://takes.jamesomalley.co.uk/p/this-might-be-oversharing](https://takes.jamesomalley.co.uk/p/this-might-be-oversharing)

生成摘要时出错

---

## 21. Pokémon Team Optimization

**原文标题**: Pokémon Team Optimization

**原文链接**: [https://nchagnet.pages.dev/blog/pokemon-team-optimization/](https://nchagnet.pages.dev/blog/pokemon-team-optimization/)

生成摘要时出错

---

## 22. Beyond the Nat: Cgnat, Bandwidth, and Practical Tunneling

**原文标题**: Beyond the Nat: Cgnat, Bandwidth, and Practical Tunneling

**原文链接**: [https://blog.rastrian.dev/post/beyond-the-nat-cgnat-bandwidth-and-practical-tunneling](https://blog.rastrian.dev/post/beyond-the-nat-cgnat-bandwidth-and-practical-tunneling)

生成摘要时出错

---

## 23. Show HN: I created a tool to design and create foamcore inserts for boardgames

**原文标题**: Show HN: I created a tool to design and create foamcore inserts for boardgames

**原文链接**: [https://boxinsertdesigner.com/](https://boxinsertdesigner.com/)

生成摘要时出错

---

## 24. A Christmas Present to Myself – Vector Network Analyzer (2014)

**原文标题**: A Christmas Present to Myself – Vector Network Analyzer (2014)

**原文链接**: [https://axotron.se/blog/vector-network-analyzer-a-christmas-present-to-myself/](https://axotron.se/blog/vector-network-analyzer-a-christmas-present-to-myself/)

生成摘要时出错

---

## 25. Web Browsers have stopped blocking pop-ups

**原文标题**: Web Browsers have stopped blocking pop-ups

**原文链接**: [https://www.smokingonabike.com/2025/12/31/web-browsers-have-stopped-blocking-pop-ups/](https://www.smokingonabike.com/2025/12/31/web-browsers-have-stopped-blocking-pop-ups/)

生成摘要时出错

---

## 26. Resistance training load does not determine hypertrophy

**原文标题**: Resistance training load does not determine hypertrophy

**原文链接**: [https://physoc.onlinelibrary.wiley.com/doi/10.1113/JP289684](https://physoc.onlinelibrary.wiley.com/doi/10.1113/JP289684)

生成摘要时出错

---

## 27. 50% of U.S. vinyl buyers don't own a record player

**原文标题**: 50% of U.S. vinyl buyers don't own a record player

**原文链接**: [https://lightcapai.medium.com/the-great-return-from-digital-abundance-to-analog-meaning-cfda9e428752](https://lightcapai.medium.com/the-great-return-from-digital-abundance-to-analog-meaning-cfda9e428752)

生成摘要时出错

---

## 28. Flow5 released to open source

**原文标题**: Flow5 released to open source

**原文链接**: [https://flow5.tech/docs/releasenotes.html](https://flow5.tech/docs/releasenotes.html)

生成摘要时出错

---

## 29. Show HN: BusterMQ, Thread-per-core NATS server in Zig with io_uring

**原文标题**: Show HN: BusterMQ, Thread-per-core NATS server in Zig with io_uring

**原文链接**: [https://bustermq.sh/](https://bustermq.sh/)

生成摘要时出错

---

## 30. Build Software. Build Users

**原文标题**: Build Software. Build Users

**原文链接**: [https://dima.day/blog/build-software-build-users/](https://dima.day/blog/build-software-build-users/)

生成摘要时出错

---

## 31. GoGoGrandparent (YC S16) Is Hiring Tech Leads

**原文标题**: GoGoGrandparent (YC S16) Is Hiring Tech Leads

**原文链接**: [https://www.ycombinator.com/companies/gogograndparent/jobs/w2jGKM7-gogograndparent-yc-s16-is-hiring-tech-leads](https://www.ycombinator.com/companies/gogograndparent/jobs/w2jGKM7-gogograndparent-yc-s16-is-hiring-tech-leads)

生成摘要时出错

---

## 32. The Mammoth Pirates – In Russia's Arctic north, a new kind of gold rush

**原文标题**: The Mammoth Pirates – In Russia's Arctic north, a new kind of gold rush

**原文链接**: [https://www.rferl.org/a/the-mammoth-pirates/27939865.html](https://www.rferl.org/a/the-mammoth-pirates/27939865.html)

生成摘要时出错

---

## 33. Pixar's True Story

**原文标题**: Pixar's True Story

**原文链接**: [https://computerhistory.org/blog/pixars-true-story/](https://computerhistory.org/blog/pixars-true-story/)

生成摘要时出错

---

## 34. Demystifying DVDs

**原文标题**: Demystifying DVDs

**原文链接**: [https://hiddenpalace.org/News/One_Bad_Ass_Hedgehog_-_Shadow_the_Hedgehog#Demystifying_DVDs](https://hiddenpalace.org/News/One_Bad_Ass_Hedgehog_-_Shadow_the_Hedgehog#Demystifying_DVDs)

生成摘要时出错

---

## 35. Ÿnsect, a French insect farming startup, has been been placed into liquidation

**原文标题**: Ÿnsect, a French insect farming startup, has been been placed into liquidation

**原文链接**: [https://techcrunch.com/2025/12/26/how-reality-crushed-ynsect-the-french-startup-that-had-raised-over-600m-for-insect-farming/](https://techcrunch.com/2025/12/26/how-reality-crushed-ynsect-the-french-startup-that-had-raised-over-600m-for-insect-farming/)

生成摘要时出错

---

## 36. My role as a founder-CTO: year 8

**原文标题**: My role as a founder-CTO: year 8

**原文链接**: [https://miguelcarranza.es/cto-year-8](https://miguelcarranza.es/cto-year-8)

生成摘要时出错

---

## 37. So I started cloning the Wii U gamepad [video]

**原文标题**: So I started cloning the Wii U gamepad [video]

**原文链接**: [https://www.youtube.com/watch?v=jlbcKuDEBw8](https://www.youtube.com/watch?v=jlbcKuDEBw8)

生成摘要时出错

---

## 38. Akin's Laws of Spacecraft Design (2011) [pdf]

**原文标题**: Akin's Laws of Spacecraft Design (2011) [pdf]

**原文链接**: [https://www.ece.uvic.ca/~elec399/201409/Akin%27s%20Laws%20of%20Spacecraft%20Design.pdf](https://www.ece.uvic.ca/~elec399/201409/Akin%27s%20Laws%20of%20Spacecraft%20Design.pdf)

生成摘要时出错

---

## 39. Show HN: Use Claude Code to Query 600 GB Indexes over Hacker News, ArXiv, etc.

**原文标题**: Show HN: Use Claude Code to Query 600 GB Indexes over Hacker News, ArXiv, etc.

**原文链接**: [https://exopriors.com/scry](https://exopriors.com/scry)

生成摘要时出错

---

## 40. The compiler is your best friend

**原文标题**: The compiler is your best friend

**原文链接**: [https://blog.daniel-beskin.com/2025-12-22-the-compiler-is-your-best-friend-stop-lying-to-it](https://blog.daniel-beskin.com/2025-12-22-the-compiler-is-your-best-friend-stop-lying-to-it)

生成摘要时出错

---

## 41. iPhone driving macOS 15.6, with native M4 driver partially patched for A18

**原文标题**: iPhone driving macOS 15.6, with native M4 driver partially patched for A18

**原文链接**: [https://twitter.com/khanhduytran0/status/2006592404045127835](https://twitter.com/khanhduytran0/status/2006592404045127835)

生成摘要时出错

---

## 42. DHS Says DHS-Certified Real IDs Too Unreliable to Confirm U.S. Citizenship

**原文标题**: DHS Says DHS-Certified Real IDs Too Unreliable to Confirm U.S. Citizenship

**原文链接**: [https://reason.com/2025/12/31/dhs-says-real-id-which-dhs-certifies-is-too-unreliable-to-confirm-u-s-citizenship/](https://reason.com/2025/12/31/dhs-says-real-id-which-dhs-certifies-is-too-unreliable-to-confirm-u-s-citizenship/)

生成摘要时出错

---

## 43. Scientists unlock brain's natural clean-up system for new treatments for stroke

**原文标题**: Scientists unlock brain's natural clean-up system for new treatments for stroke

**原文链接**: [https://www.monash.edu/pharm/about/news/news-listing/latest/scientists-unlock-brains-natural-clean-up-system-to-develop-new-treatments-for-stroke-and-other-neurological-diseases](https://www.monash.edu/pharm/about/news/news-listing/latest/scientists-unlock-brains-natural-clean-up-system-to-develop-new-treatments-for-stroke-and-other-neurological-diseases)

生成摘要时出错

---

## 44. Reminiscences of a Stock Operator (1923)

**原文标题**: Reminiscences of a Stock Operator (1923)

**原文链接**: [https://gutenberg.org/cache/epub/60979/pg60979-images.html](https://gutenberg.org/cache/epub/60979/pg60979-images.html)

生成摘要时出错

---

## 45. Warren Buffett steps down as Berkshire Hathaway CEO after six decades

**原文标题**: Warren Buffett steps down as Berkshire Hathaway CEO after six decades

**原文链接**: [https://www.latimes.com/business/story/2025-12-31/warren-buffett-steps-down-as-berkshire-hathaway-ceo-after-six-decades](https://www.latimes.com/business/story/2025-12-31/warren-buffett-steps-down-as-berkshire-hathaway-ceo-after-six-decades)

生成摘要时出错

---

## 46. Bulgaria joins euro area from 1 January

**原文标题**: Bulgaria joins euro area from 1 January

**原文链接**: [https://ec.europa.eu/commission/presscorner/detail/de/ip_25_3123](https://ec.europa.eu/commission/presscorner/detail/de/ip_25_3123)

生成摘要时出错

---

## 47. Only 5 Sears stores remain in the U.S.

**原文标题**: Only 5 Sears stores remain in the U.S.

**原文链接**: [https://www.nytimes.com/2025/12/26/business/sears-seritage-edward-lampert.html](https://www.nytimes.com/2025/12/26/business/sears-seritage-edward-lampert.html)

生成摘要时出错

---

## 48. Worlds largest electric ship launched by Tasmanian boatbuilder

**原文标题**: Worlds largest electric ship launched by Tasmanian boatbuilder

**原文链接**: [https://www.theguardian.com/australia-news/2025/may/02/hull-096-worlds-largest-electric-ship-battery-power-launched](https://www.theguardian.com/australia-news/2025/may/02/hull-096-worlds-largest-electric-ship-battery-power-launched)

生成摘要时出错

---

## 49. All-optical synthesis chip for large-scale intelligent semantic vision

**原文标题**: All-optical synthesis chip for large-scale intelligent semantic vision

**原文链接**: [https://www.science.org/doi/10.1126/science.adv7434](https://www.science.org/doi/10.1126/science.adv7434)

生成摘要时出错

---

## 50. Why Microsoft Store Discontinued Support for Office Apps

**原文标题**: Why Microsoft Store Discontinued Support for Office Apps

**原文链接**: [https://www.bgr.com/2027774/why-microsoft-store-discontinued-office-support/](https://www.bgr.com/2027774/why-microsoft-store-discontinued-office-support/)

生成摘要时出错

---

## 51. When square pixels aren't square

**原文标题**: When square pixels aren't square

**原文链接**: [https://alexwlchan.net/2025/square-pixels/](https://alexwlchan.net/2025/square-pixels/)

生成摘要时出错

---

## 52. Microtonal Spiral Piano

**原文标题**: Microtonal Spiral Piano

**原文链接**: [https://shih1.github.io/spiral/](https://shih1.github.io/spiral/)

生成摘要时出错

---

## 53. Scaffolding to Superhuman: How Curriculum Learning Solved 2048 and Tetris

**原文标题**: Scaffolding to Superhuman: How Curriculum Learning Solved 2048 and Tetris

**原文链接**: [https://kywch.github.io/blog/2025/12/curriculum-learning-2048-tetris/](https://kywch.github.io/blog/2025/12/curriculum-learning-2048-tetris/)

生成摘要时出错

---

## 54. If childhood is half of subjective life, how should that change how we live?

**原文标题**: If childhood is half of subjective life, how should that change how we live?

**原文链接**: [https://moultano.wordpress.com/2025/12/30/children-and-helical-time/](https://moultano.wordpress.com/2025/12/30/children-and-helical-time/)

生成摘要时出错

---

## 55. PyPI in 2025: A Year in Review

**原文标题**: PyPI in 2025: A Year in Review

**原文链接**: [https://blog.pypi.org/posts/2025-12-31-pypi-2025-in-review/](https://blog.pypi.org/posts/2025-12-31-pypi-2025-in-review/)

生成摘要时出错

---

## 56. The most famous transcendental numbers

**原文标题**: The most famous transcendental numbers

**原文链接**: [https://sprott.physics.wisc.edu/pickover/trans.html](https://sprott.physics.wisc.edu/pickover/trans.html)

生成摘要时出错

---

## 57. Doom in Django: testing the limits of LiveView at 600.000 divs/segundo

**原文标题**: Doom in Django: testing the limits of LiveView at 600.000 divs/segundo

**原文链接**: [https://en.andros.dev/blog/7b1b607b/doom-in-django-testing-the-limits-of-liveview-at-600000-divssegundo/](https://en.andros.dev/blog/7b1b607b/doom-in-django-testing-the-limits-of-liveview-at-600000-divssegundo/)

生成摘要时出错

---

## 58. Kitchen optimizations

**原文标题**: Kitchen optimizations

**原文链接**: [https://www.natemeyvis.com/kitchen-optimizations/](https://www.natemeyvis.com/kitchen-optimizations/)

生成摘要时出错

---

## 59. The rise of industrial software

**原文标题**: The rise of industrial software

**原文链接**: [https://chrisloy.dev/post/2025/12/30/the-rise-of-industrial-software](https://chrisloy.dev/post/2025/12/30/the-rise-of-industrial-software)

生成摘要时出错

---

## 60. The rise of industrial software

**原文标题**: The rise of industrial software

**原文链接**: [https://chrisloy.dev/post/2025/12/30/the-rise-of-industrial-software](https://chrisloy.dev/post/2025/12/30/the-rise-of-industrial-software)

生成摘要时出错

---

## 61. On privacy and control

**原文标题**: On privacy and control

**原文链接**: [https://toidiu.com/blog/2025-12-25-privacy-and-control/](https://toidiu.com/blog/2025-12-25-privacy-and-control/)

生成摘要时出错

---

## 62. How AI labs are solving the power problem

**原文标题**: How AI labs are solving the power problem

**原文链接**: [https://newsletter.semianalysis.com/p/how-ai-labs-are-solving-the-power](https://newsletter.semianalysis.com/p/how-ai-labs-are-solving-the-power)

生成摘要时出错

---

## 63. Tixl: Open-source realtime motion graphics

**原文标题**: Tixl: Open-source realtime motion graphics

**原文链接**: [https://github.com/tixl3d/tixl](https://github.com/tixl3d/tixl)

生成摘要时出错

---

## 64. Nvidia GB10's Memory Subsystem, from the CPU Side

**原文标题**: Nvidia GB10's Memory Subsystem, from the CPU Side

**原文链接**: [https://chipsandcheese.com/p/inside-nvidia-gb10s-memory-subsystem](https://chipsandcheese.com/p/inside-nvidia-gb10s-memory-subsystem)

生成摘要时出错

---

## 65. The story of Squeak, a practical Smalltalk written in itself (1997) [pdf]

**原文标题**: The story of Squeak, a practical Smalltalk written in itself (1997) [pdf]

**原文链接**: [http://www.vpri.org/pdf/tr1997001_backto.pdf](http://www.vpri.org/pdf/tr1997001_backto.pdf)

生成摘要时出错

---

## 66. Observed Agent Sandbox Bypasses

**原文标题**: Observed Agent Sandbox Bypasses

**原文链接**: [https://voratiq.com/blog/yolo-in-the-sandbox/](https://voratiq.com/blog/yolo-in-the-sandbox/)

生成摘要时出错

---

## 67. Who invented the transistor?

**原文标题**: Who invented the transistor?

**原文链接**: [https://people.idsia.ch/~juergen/who-invented-the-transistor.html](https://people.idsia.ch/~juergen/who-invented-the-transistor.html)

生成摘要时出错

---

## 68. Love Your Customers

**原文标题**: Love Your Customers

**原文链接**: [https://bcantrill.dtrace.org/2025/12/31/love-your-customers/](https://bcantrill.dtrace.org/2025/12/31/love-your-customers/)

生成摘要时出错

---

## 69. RoboCop – Breaking the Law. H0ffman Cracks RoboCop Arcade from DataEast

**原文标题**: RoboCop – Breaking the Law. H0ffman Cracks RoboCop Arcade from DataEast

**原文链接**: [https://hoffman.home.blog/2025/12/26/robocop-breaking-the-law/](https://hoffman.home.blog/2025/12/26/robocop-breaking-the-law/)

生成摘要时出错

---

## 70. Stewart Cheifet, creator of The Computer Chronicles, has died

**原文标题**: Stewart Cheifet, creator of The Computer Chronicles, has died

**原文链接**: [https://obits.goldsteinsfuneral.com/stewart-cheifet](https://obits.goldsteinsfuneral.com/stewart-cheifet)

生成摘要时出错

---

## 71. MHC: Manifold-Constrained Hyper-Connections

**原文标题**: MHC: Manifold-Constrained Hyper-Connections

**原文链接**: [https://arxiv.org/abs/2512.24880](https://arxiv.org/abs/2512.24880)

生成摘要时出错

---

## 72. Efficient method to capture carbon dioxide from the atmosphere

**原文标题**: Efficient method to capture carbon dioxide from the atmosphere

**原文链接**: [https://www.helsinki.fi/en/news/innovations/efficient-method-capture-carbon-dioxide-atmosphere-developed-university-helsinki](https://www.helsinki.fi/en/news/innovations/efficient-method-capture-carbon-dioxide-atmosphere-developed-university-helsinki)

生成摘要时出错

---

## 73. The Delete Act

**原文标题**: The Delete Act

**原文链接**: [https://privacy.ca.gov/drop/about-drop-and-the-delete-act/](https://privacy.ca.gov/drop/about-drop-and-the-delete-act/)

生成摘要时出错

---

## 74. DeepSeek kicks off 26 with paper signalling push to train bigger models for less

**原文标题**: DeepSeek kicks off 26 with paper signalling push to train bigger models for less

**原文链接**: [https://www.scmp.com/tech/big-tech/article/3338427/deepseek-kicks-2026-paper-signalling-push-train-bigger-models-less](https://www.scmp.com/tech/big-tech/article/3338427/deepseek-kicks-2026-paper-signalling-push-train-bigger-models-less)

生成摘要时出错

---

## 75. The Origin of the Terms Big-Endian and Little-Endian (2003)

**原文标题**: The Origin of the Terms Big-Endian and Little-Endian (2003)

**原文链接**: [https://www.ling.upenn.edu/courses/Spring_2003/ling538/Lecnotes/ADfn1.htm](https://www.ling.upenn.edu/courses/Spring_2003/ling538/Lecnotes/ADfn1.htm)

生成摘要时出错

---

## 76. Odin: Moving Towards a New "core:OS"

**原文标题**: Odin: Moving Towards a New "core:OS"

**原文链接**: [https://odin-lang.org/news/moving-towards-a-new-core-os/](https://odin-lang.org/news/moving-towards-a-new-core-os/)

生成摘要时出错

---

## 77. Claude wrote a functional NES emulator using my engine's API

**原文标题**: Claude wrote a functional NES emulator using my engine's API

**原文链接**: [https://carimbo.games/games/nintendo/](https://carimbo.games/games/nintendo/)

生成摘要时出错

---

## 78. Readings in Database Systems (5th Edition) (2015)

**原文标题**: Readings in Database Systems (5th Edition) (2015)

**原文链接**: [http://www.redbook.io/](http://www.redbook.io/)

生成摘要时出错

---

## 79. A faster heart for F-Droid

**原文标题**: A faster heart for F-Droid

**原文链接**: [https://f-droid.org/2025/12/30/a-faster-heart-for-f-droid.html](https://f-droid.org/2025/12/30/a-faster-heart-for-f-droid.html)

生成摘要时出错

---

## 80. Learning of the Passing of Stewart Cheifet

**原文标题**: Learning of the Passing of Stewart Cheifet

**原文链接**: [https://christopherdrum.github.io/posts/2026/01/stewart-cheifet-passing](https://christopherdrum.github.io/posts/2026/01/stewart-cheifet-passing)

生成摘要时出错

---

## 81. France targets Australia-style social media ban for children next year

**原文标题**: France targets Australia-style social media ban for children next year

**原文链接**: [https://www.theguardian.com/world/2025/dec/31/france-plans-social-media-ban-for-under-15s-from-september-2026](https://www.theguardian.com/world/2025/dec/31/france-plans-social-media-ban-for-under-15s-from-september-2026)

生成摘要时出错

---

## 82. Show HN: A local-first financial auditor using IBM Granite, MCP, and SQLite

**原文标题**: Show HN: A local-first financial auditor using IBM Granite, MCP, and SQLite

**原文链接**: [https://github.com/simplynd/expense-ai](https://github.com/simplynd/expense-ai)

生成摘要时出错

---

## 83. 'Three norths' alignment about to end

**原文标题**: 'Three norths' alignment about to end

**原文链接**: [https://www.spatialsource.com.au/three-norths-alignment-about-to-end/](https://www.spatialsource.com.au/three-norths-alignment-about-to-end/)

生成摘要时出错

---

## 84. Times New American: A Tale of Two Fonts

**原文标题**: Times New American: A Tale of Two Fonts

**原文链接**: [https://hsu.cy/2025/12/times-new-american/](https://hsu.cy/2025/12/times-new-american/)

生成摘要时出错

---

## 85. Sabotaging Bitcoin

**原文标题**: Sabotaging Bitcoin

**原文链接**: [https://blog.dshr.org/2025/12/sabotaging-bitcoin.html](https://blog.dshr.org/2025/12/sabotaging-bitcoin.html)

生成摘要时出错

---

## 86. Iron Beam: Israel's first operational anti drone laser system

**原文标题**: Iron Beam: Israel's first operational anti drone laser system

**原文链接**: [https://mod.gov.il/en/press-releases/press-room/israel-mod-and-rafael-deliver-first-operational-high-power-laser-system-iron-beam-to-the-idf](https://mod.gov.il/en/press-releases/press-room/israel-mod-and-rafael-deliver-first-operational-high-power-laser-system-iron-beam-to-the-idf)

生成摘要时出错

---

## 87. What an unprocessed photo looks like

**原文标题**: What an unprocessed photo looks like

**原文链接**: [https://maurycyz.com/misc/raw_photo/](https://maurycyz.com/misc/raw_photo/)

生成摘要时出错

---

## 88. Toro: Deploy Applications as Unikernels

**原文标题**: Toro: Deploy Applications as Unikernels

**原文链接**: [https://github.com/torokernel/torokernel](https://github.com/torokernel/torokernel)

生成摘要时出错

---

## 89. Escaping containment: A security analysis of FreeBSD jails [video]

**原文标题**: Escaping containment: A security analysis of FreeBSD jails [video]

**原文链接**: [https://media.ccc.de/v/39c3-escaping-containment-a-security-analysis-of-freebsd-jails](https://media.ccc.de/v/39c3-escaping-containment-a-security-analysis-of-freebsd-jails)

生成摘要时出错

---

## 90. Show HN: 22 GB of Hacker News in SQLite

**原文标题**: Show HN: 22 GB of Hacker News in SQLite

**原文链接**: [https://hackerbook.dosaygo.com](https://hackerbook.dosaygo.com)

生成摘要时出错

---

## 91. Zpdf: PDF text extraction in Zig

**原文标题**: Zpdf: PDF text extraction in Zig

**原文链接**: [https://github.com/Lulzx/zpdf](https://github.com/Lulzx/zpdf)

生成摘要时出错

---

## 92. Approachable Swift Concurrency

**原文标题**: Approachable Swift Concurrency

**原文链接**: [https://fuckingapproachableswiftconcurrency.com/en/](https://fuckingapproachableswiftconcurrency.com/en/)

生成摘要时出错

---

## 93. Show HN: LoongArch Userspace Emulator

**原文标题**: Show HN: LoongArch Userspace Emulator

**原文链接**: [https://github.com/libriscv/libloong](https://github.com/libriscv/libloong)

生成摘要时出错

---

## 94. Mitsubishi Diatone D-160 (1985)

**原文标题**: Mitsubishi Diatone D-160 (1985)

**原文链接**: [https://audio-database.com/MITSUBISHI-DIATONE/diatonesp/d-160-e.html](https://audio-database.com/MITSUBISHI-DIATONE/diatonesp/d-160-e.html)

生成摘要时出错

---

## 95. FediMeteo: A €4 FreeBSD VPS Became a Global Weather Service

**原文标题**: FediMeteo: A €4 FreeBSD VPS Became a Global Weather Service

**原文链接**: [https://it-notes.dragas.net/2025/02/26/fedimeteo-how-a-tiny-freebsd-vps-became-a-global-weather-service-for-thousands/](https://it-notes.dragas.net/2025/02/26/fedimeteo-how-a-tiny-freebsd-vps-became-a-global-weather-service-for-thousands/)

生成摘要时出错

---

## 96. Winnie-the-Pooh brings 100 years of fame to forest

**原文标题**: Winnie-the-Pooh brings 100 years of fame to forest

**原文链接**: [https://www.bbc.com/news/articles/c4g9dzj1xj3o](https://www.bbc.com/news/articles/c4g9dzj1xj3o)

生成摘要时出错

---

## 97. A super fast website using Cloudflare workers

**原文标题**: A super fast website using Cloudflare workers

**原文链接**: [https://crazyfast.website](https://crazyfast.website)

生成摘要时出错

---

## 98. Elastic style faceted search from PostgreSQL

**原文标题**: Elastic style faceted search from PostgreSQL

**原文链接**: [https://www.paradedb.com/blog/faceting](https://www.paradedb.com/blog/faceting)

生成摘要时出错

---

## 99. Veritasium: The Ridiculous Engineering of ASML Machine [video]

**原文标题**: Veritasium: The Ridiculous Engineering of ASML Machine [video]

**原文链接**: [https://www.youtube.com/watch?v=MiUHjLxm3V0](https://www.youtube.com/watch?v=MiUHjLxm3V0)

生成摘要时出错

---

## 100. Show HN: One clean, developer-focused page for every Unicode symbol

**原文标题**: Show HN: One clean, developer-focused page for every Unicode symbol

**原文链接**: [https://fontgenerator.design/symbols](https://fontgenerator.design/symbols)

生成摘要时出错

---

