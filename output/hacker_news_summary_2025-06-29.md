# Hacker News 热门文章摘要 (2025-06-29)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 我让我的虚拟机以为它有CPU风扇。

**原文标题**: I made my VM think it has a CPU fan

**原文链接**: [https://wbenny.github.io/2025/06/29/i-made-my-vm-think-it-has-a-cpu-fan.html](https://wbenny.github.io/2025/06/29/i-made-my-vm-think-it-has-a-cpu-fan.html)

本文详细介绍了如何欺骗虚拟机（VM），使其认为自己拥有CPU风扇，这是一种用于规避检查虚拟化的恶意软件的技术。恶意软件通常会寻找特定的硬件组件（如CPU风扇），以识别其是否在虚拟机中运行，从而避免分析。

作者着重于通过操纵系统管理BIOS（SMBIOS）数据来欺骗CPU风扇的存在，SMBIOS数据是系统识别其硬件的方式。具体来说，本文针对的是Win32_Fan WMI类，该类依赖于类型为27（“冷却设备”）的SMBIOS数据。

作者最初在使用Xen时面临挑战，需要修补Xen源代码以允许修改特定的SMBIOS类型。他们发现仅仅添加冷却设备条目是不够的，因为它引用了温度探头（类型28）。因此，类型27和类型28都需要添加到SMBIOS数据中。本文提供了这些SMBIOS条目的确切字节表示。

然后，作者解释了如何在Xen中使用域配置文件中的`smbios_firmware`选项设置自定义SMBIOS数据，包括如何使用大小前缀正确格式化二进制数据。最后，作者演示了在QEMU/KVM中使用`-smbios`选项完成相同任务是多么的简单，并提供了创建自定义SMBIOS数据的技巧。

---

## 2. 展示HN: Octelium – Teleport、Cloudflare、Tailscale、Ngrok的开源替代方案

**原文标题**: Show HN: Octelium – FOSS Alternative to Teleport, Cloudflare, Tailscale, Ngrok

**原文链接**: [https://github.com/octelium/octelium](https://github.com/octelium/octelium)

Octelium：一款免费开源、自托管的零信任资源访问统一平台，定位为各种远程访问和安全工具的现代替代方案。它旨在为远程访问VPN、ZTNA、安全隧道、API网关、AI网关、PaaS、Kubernetes Ingress，甚至家庭实验室基础设施提供通用解决方案。

其主要功能包括：统一的架构，支持人员和工作负载访问私有和公共资源；动态无密钥访问；通过策略即代码（CEL/OPA）实现的上下文感知访问控制；持续身份验证（OpenID Connect、SAML、OIDC 断言）；以及使用 OpenTelemetry 的应用层感知审计。Octelium 提供轻松的无密码 SSH 访问，以及类似 PaaS 的能力，用于部署和扩展容器化应用程序作为服务。

Octelium 专为通过 Kubernetes 实现的可扩展性和高可用性而设计，支持通过 CLI 工具 (`octeliumctl`) 进行集中式声明性管理，并且无需更改现有基础设施。它通过使用稳定的私有 IP 和统一的 DNS 来解决传统 VPN 的网络问题。基于客户端的专用网络支持 WireGuard 和实验性 QUIC 隧道。

本文档提供了有关如何在 Codespace 中试用 Octelium、安装 CLI 工具以及在廉价的云 VM/VPS 实例上安装单节点集群的说明。它强调了 Octelium 的开源性质和自托管能力，并将其与专有的基于云的控制平面和 SaaS 服务形成对比。

---

## 3. 在没有IPv4连接的情况下使用互联网

**原文标题**: Using the Internet without IPv4 connectivity

**原文链接**: [https://jamesmcm.github.io/blog/no-ipv4/](https://jamesmcm.github.io/blog/no-ipv4/)

本文详细介绍了作者在ISP的IPv4连接因CG-NAT问题失效，仅剩IPv6可用的情况下，如何恢复互联网访问。作者利用一台具有IPv4和IPv6地址的Hetzner VPS创建了一个WireGuard隧道，有效地将所有互联网流量通过该VPS路由，从而重新获得IPv4功能。

文章解释了NAT，强调了它在允许多个设备共享单个IPv4地址方面的作用以及CG-NAT的影响。然后，文章将此与IPv6进行了对比，IPv6提供了大量的地址，消除了对NAT的需求，并允许直接设备寻址。

核心解决方案包括在VPS上设置WireGuard隧道，配置服务器端和客户端。服务器配置详细说明了如何处理NATed和直接可寻址的IPv6对等体。作者最初在隧道内遇到了IPv6连接问题，但最终解决了这些问题。他们还探讨了使用MASQUERADE和SNAT进行IPv6 NAT，强调了在可用时直接IPv6寻址的优势。

为了启用对工作VPN的无干扰访问，作者在Linux中使用了网络命名空间。通过将来自网络命名空间的流量通过WireGuard隧道路由，他们可以独立于主机的WireGuard连接运行工作VPN。`vopono`的使用简化了创建和管理网络命名空间的过程。最后，作者建议将客户端wireguard配置中的MTU大小设置为1280，否则可能会发生数据包丢失。

---

## 4. 布隆过滤器示例

**原文标题**: Bloom Filters by Example

**原文链接**: [https://llimllib.github.io/bloomfilter-tutorial/](https://llimllib.github.io/bloomfilter-tutorial/)

本文介绍了布隆过滤器，一种用于高效测试集合成员关系的概率型数据结构。布隆过滤器提供了一种内存高效的方式来确定一个元素是否*肯定不在*集合中，或者*可能在*集合中（存在误判的可能性）。

其核心组件是一个位向量。添加元素需要多次哈希该元素，并将向量中对应的位设置为1。测试成员关系需要再次哈希该元素，并检查这些位是否已设置。如果任何位为0，则该元素肯定不在集合中。如果所有位均为1，则由于潜在的冲突，该元素可能在集合中。

本文强调了独立且均匀分布的哈希函数（如Murmur、xxHash、Fnv）对于优化性能的重要性。它讨论了过滤器大小 (m)、哈希函数数量 (k) 和预期元素数量 (n) 之间的权衡，以尽量减少误判率。更大的过滤器可以减少误判，但需要更多的内存。哈希函数的最佳数量可以计算为 (m/n)ln(2)。

插入和成员关系测试的时间复杂度均为 O(k)。当您需要快速成员关系测试并可以容忍较小的误判率时，尤其是在潜在元素范围很大的情况下，布隆过滤器非常有用。它们被应用于网络应用、生物信息学和数据库等领域。

---

## 5. Medley Interlisp项目：重现一款历史软件系统[pdf]

**原文标题**: The Medley Interlisp Project: Reviving a Historical Software System [pdf]

**原文链接**: [https://interlisp.org/documentation/young-ccece2025.pdf](https://interlisp.org/documentation/young-ccece2025.pdf)

此文档看似一个损坏或不完整的PDF文件，标题为“Medley Interlisp项目：重现历史软件系统”。可见内容主要由PDF语法（页眉、对象、流等）组成，因压缩和编码而被渲染成看似随机的字符。

根据标题，该项目可能侧重于恢复或保存Medley Interlisp，这是一个具有历史意义的软件系统。然而，该文件的损坏状态阻止了提取关于项目目标、方法或结果的任何具体细节。标题强烈暗示它涉及恢复、现代化或使遗留软件系统易于访问。

在没有正确呈现或访问未损坏版本的情况下，无法确定具体方面，例如：

*   正在重现的Medley Interlisp的具体版本。
*   其重现的原因（例如，历史保存、教育目的或继续使用）。
*   项目中使用的技术或方法。
*   项目的当前状态。

总之，该PDF文件是关于一个与重现Medley Interlisp系统相关的项目，但该文件本身基本上无法读取，并且没有提供任何有用的信息。

---

## 6. 摩尔定律的不可持续性

**原文标题**: The Unsustainability of Moore's Law

**原文链接**: [https://bzolang.blog/p/the-unsustainability-of-moores-law](https://bzolang.blog/p/the-unsustainability-of-moores-law)

查尔斯·罗森鲍尔的文章指出，摩尔定律（即芯片上晶体管密度大约每两年翻一番的观察）正变得难以为继，原因在于成本上升和物理限制。

他强调了芯片制造厂（“晶圆厂”）的建设成本呈指数级增长，同时有能力这样做的公司数量却在减少。这些财政障碍，加上光掩模成本的上升，威胁着扼杀创新，并将市场限制在少数主要参与者手中。

罗森鲍尔解释说，目前对晶体管的“纳米”测量具有误导性，因为它们曾经代表的物理特征已不复存在。虽然EUV光刻技术可以实现更精细的细节，但即使它也存在与波长相关的限制，并且光刻胶化学为进一步的缩放带来了另一个重大障碍。

文章深入探讨了晶体管几何结构，解释了从平面晶体管到FinFET，再到现在的GAAFET（RibbonFET）的转变，每种都代表着更高的制造复杂性，但寿命却更短。罗森鲍尔指出，像背面供电这样的进步是一次性的优化，而不是长期的解决方案。

使时钟速度增长成为可能的登纳德缩放比例也不再成立，导致CPU时钟速度停滞不前，原因是功率密度和漏电流不断上升。

最终，罗森鲍尔认为，摩尔定律虽然植根于经济学，但正面临技术和财政壁垒的融合。他建议简化制造流程，并可能探索替代光刻方法可能是前进的方向，但这将需要与目前的做法有很大的不同。未来可能取决于降低成本和简化复杂流程，并可能从小规模的创新方法中汲取灵感。

---

## 7. 科学家在一艘挖空的木头里重走三万年前的航海路线

**原文标题**: Scientists Retrace 30k-Year-Old Sea Voyage, in a Hollowed-Out Log

**原文链接**: [https://www.nytimes.com/2025/06/25/science/anthropology-ocean-migration-japan.html](https://www.nytimes.com/2025/06/25/science/anthropology-ocean-migration-japan.html)

无法访问文章链接。

---

## 8. 使用LLVM-mca进行性能调试：模拟CPU

**原文标题**: Performance Debugging with LLVM-mca: Simulating the CPU

**原文链接**: [https://johnnysswlab.com/performance-debugging-with-llvm-mca-simulating-the-cpu/](https://johnnysswlab.com/performance-debugging-with-llvm-mca-simulating-the-cpu/)

本文演示了如何使用性能分析工具LLVM-mca调试矢量化卷积内核中的性能回归。最初的目标是通过使用`vextq_f32`内在函数（连接寄存器）来减少内存加载，从而优化NEON矢量化内核。原始版本（5L）执行五次加载，而优化版本（2L3E）执行两次加载和三次寄存器连接。令人惊讶的是，优化后的版本运行速度更慢。

LLVM-mca被用于模拟汇编中核心循环的CPU执行，从而揭示了根本原因。尽管2L3E版本中的指令较少，但它表现出更高的周期数和更低的吞吐量。资源消耗分析表明，2L3E版本中执行端口的利用率更加不平衡，特别是单元5和6。时间线图显示，2L3E版本中的`ext`指令被延迟，等待初始加载完成，从而增加了整体延迟。瓶颈分析证实，2L3E版本受到执行端口压力和数据依赖性的影响，从而阻碍了性能。

关键结论是，原始的5L版本更快，因为它以更平衡的方式利用了CPU执行单元，并且加载指令可以独立执行，而没有指令携带的依赖性。本文强调了llvm-mca在识别与指令调度、资源争用和数据依赖性相关的后端性能问题方面的实用性，即使模拟并不完美，这在汇编或内在函数级别优化代码时非常有用。

---

## 9. 苹果“F1电影”钱包广告进一步侵蚀信任

**原文标题**: More on Apple's Trust-Eroding 'F1 the Movie' Wallet Ad

**原文链接**: [https://daringfireball.net/2025/06/more_on_apples_trust-eroding_f1_the_movie_wallet_ad](https://daringfireball.net/2025/06/more_on_apples_trust-eroding_f1_the_movie_wallet_ad)

本文批评苹果公司通过其钱包应用推送F1电影广告的决定，认为这损害了用户的信任和隐私。作者认为，苹果钱包应被视为如同密码和日记应用一样“神圣不可侵犯”，不应有广告，因为用户将其敏感的财务和身份信息委托给它。

作者强调了与实体钱包相关的固有隐私和私密性，而苹果钱包正试图以数字方式复制这种体验。在这个空间中引入广告会打破这种信任。令人担忧的是，用户，尤其是F1电影的目标受众，可能会认为该广告是苹果钱包追踪他们的兴趣和活动（如最近购买的电影票）的结果。即使这种看法不准确，也具有破坏性，并抵消了苹果公司为建立其相对于其他科技公司的隐私声誉所做的努力。

核心论点是，隐私感知与技术现实同样重要。通过发送这条不加选择的广告，苹果公司危及了用户的信任，并损害了专注于维护苹果钱包隐私的团队的辛勤工作。作者最后强烈呼吁解雇授权投放该广告的责任人。

---

## 10. MCP：一个（意外的）通用插件系统

**原文标题**: MCP: An (Accidentally) Universal Plugin System

**原文链接**: [https://worksonmymachine.substack.com/p/mcp-an-accidentally-universal-plugin](https://worksonmymachine.substack.com/p/mcp-an-accidentally-universal-plugin)

好的，我已阅读了来自所提供URL的文章“MCP：一个（意外的）通用插件系统”。以下是摘要：

这篇文章讨论了MCP（Mod Coder Pack），一个最初设计用于反编译、反混淆和重新编译Minecraft代码的工具，使模组制作者能够创建并将修改集成到游戏中。作者认为，由于几个关键特性，MCP无意中创建了一个非常强大且通用的插件系统：

*   **反射与字节码操作：** MCP通过反射促进了对底层应用程序（Minecraft）的深度访问，允许插件修改现有代码，并在几乎任何时候注入新功能。它允许动态更改程序的构建块。

*   **定义良好的API（无意为之）：** 虽然没有明确设计为正式的API，但Minecraft代码的稳定、易于理解的结构以及MCP暴露它的方式提供了一个事实上的API，模组制作者可以可靠地针对它。

*   **大型生态系统与社区：** 庞大的Minecraft模组社区积极开发和维护了这个“插件系统”，创造了大量的模组和相关工具，加强了它的可行性。

*   **简单性：** 作者认为，MCP的相对简单性（与更正式的插件系统相比）促成了它的采用。模组制作者不需要学习复杂的框架来添加功能。

文章强调，MCP并非有意设计为插件系统，而是有机地演变成一个。它的成功突出了涌现式插件系统的潜力，尤其是在与强大的社区和深度交互底层应用程序的能力相结合时。它还表明，争取完美的正式API可能不如创建灵活且适应性强的系统有效，让社区随着时间的推移塑造它们。

---

## 11. 使用 eBPF 实现快速 TCP 指纹识别

**原文标题**: Implementing fast TCP fingerprinting with eBPF

**原文链接**: [https://halb.it/posts/ebpf-fingerprinting-1/](https://halb.it/posts/ebpf-fingerprinting-1/)

本文概述了一个项目，该项目旨在使用 eBPF 在 Go Web 服务器中实现快速 TCP 指纹识别。作者将 TCP 指纹识别介绍为一种识别异常 Web 请求的技术，尤其适用于反爬虫解决方案。他们强调，由于 Web 抓取活动的日益增加，对这种技术的需求也越来越高。

文章首先解释了 HTTP 请求在基本层面的工作原理，并使用一个简单的 C Web 服务器示例来说明与操作系统系统调用的直接交互。然后，作者深入研究了 TCP 握手的结构，强调了握手期间交换的信息如何揭示有关客户端设备和网络路由的详细信息。他们特别提到了最大段大小 (MSS) TCP 选项作为一个例子。

核心问题是，标准的 POSIX API 不提供直接访问指纹识别所需的原始 TCP SYN 数据。然后，作者探讨了替代解决方案：
1. **LibPCAP:** 在用户空间捕获原始数据包。但是，这种方法存在延迟问题，使其不适合实时分析。
2. **eBPF:** 作者建议使用 eBPF 创建 TCP SYN 数据包的内核端哈希表，从而消除用户空间数据包捕获的延迟问题。他们强调了 eBPF 的优势，包括最小的开销和从用户空间的直接访问。

作者最后介绍了 eBPF 和 Cilium eBPF 库，作为实现 TCP SYN 过滤器的选定工具，为文章第二部分描述的实际开发奠定了基础。

---

## 12. 为什么选择 Go 来构建 Lua 解释器

**原文标题**: Why Go Rocks for Building a Lua Interpreter

**原文链接**: [https://www.zombiezen.com/blog/2025/06/why-go-rocks-for-building-lua-interpreter/](https://www.zombiezen.com/blog/2025/06/why-go-rocks-for-building-lua-interpreter/)

Roxy Light 讲述了用 Go 构建自定义 Lua 解释器的过程。文章解释了 Lua 的核心数据类型（nil，布尔值，数字，字符串，userdata，表和函数），然后描述了解释器的架构，它被分为三个 Go 包：`lualex`（词法分析器），`luacode`（语法分析器）和 `lua`（解释器）。

语法分析器（`luacode`）从 C Lua 的实现移植而来，并生成一系列高效的指令（字节码）而不是抽象语法树，从而实现窥孔优化并与 C Lua 的二进制块格式兼容。`lua` 包包含 `lua.State`，它执行字节码指令。

文章的大部分内容集中在数据表示上，其中 Go 的接口类型（`value`）用于表示 Lua 值。数字类型、函数和其他数据结构被实现为符合此接口的 Go 类型。与 C Lua 的一个关键区别是引入了“冻结”，防止解释器之间共享数据的变异，这得益于 Go 的垃圾回收器。

然后，文章通过变量赋值和算术运算的示例，逐步介绍了 Lua 代码的执行过程，说明了解释器如何处理字节码指令。

“进展顺利”部分强调了 Go 的优势：由于内置类型和垃圾回收，实现更简单；由于语法分析器移植，易于进行正确性检查；以及映射到 Lua 值的强大接口类型。Go 的测试和基准测试工具也很有价值。

挑战包括重新思考错误处理，因为 C Lua 使用 `longjmp`。实现的解决方案使用存储在 Lua 调用堆栈中的 Lua 消息处理程序。

---

## 13. 用 Haskell 解决“护照申请”问题

**原文标题**: Solving `Passport Application` with Haskell

**原文链接**: [https://jameshaydon.github.io/passport/](https://jameshaydon.github.io/passport/)

本文详细介绍了作者以其女儿的名义玩英国“护照申请”游戏的体验，突出了该游戏复杂的官僚逻辑和文件收集挑战。这款由HMPO开发的游戏，要求玩家通过一系列文件请求来证明申请人的英国公民身份，这些请求通常包含晦涩的解释和看似无关的信息。

作者描述了诸如获取认证翻译和处理各个机构的官僚程序等支线任务。一个关键要素是推动文件请求的“审查员”，只能通过“咨询代理”进行沟通，这增加了间接性和等待时间。

作者遇到了一项关于申请人曾祖父的文件请求，这促使他们调查该游戏的潜在逻辑。他们发现该游戏以“官僚逻辑”运作，类似于构造逻辑，需要基于特定文件的证明，而不是简单的有效论证。这通常会导致沿着家族树进行递归文件请求，直到达到“基本情况”（例如，1983年之前在英国出生或归化）。

为了理解并可能预测这些文件请求，作者转向Haskell的LogicT monad，旨在编码规则并确定证明英国公民身份所需的所有可能的文件集。Haskell代码专注于枚举英国公民身份的证明，然后计算必要的文档。该程序以交互方式提问，以避免不必要的调查，并保留所有分支的信息。代码包括诸如`brit`之类的函数，以根据出生地、父母的公民身份和其他因素来确定英国公民身份。

---

## 14. 数列及其一阶差分共同列出所有正数，且仅列出一次。

**原文标题**: Sequence and first differences together list all positive numbers exactly once

**原文链接**: [https://oeis.org/A005228](https://oeis.org/A005228)

本条目描述了整数数列线上大全（OEIS）中的数列 A005228。该数列被定义为字典序最早的数列，它与其一阶差分数列（A030124）组合在一起，恰好包含每个正整数一次。

主要特征和定义：

*   **定义：** a(1) = 1，且对于 n >= 2，a(n) = a(n-1) + c(n-1)，其中 c(n) 是补序列 A030124 的第 n 项。

*   **性质：** 每个正整数要么出现在该数列本身中，要么出现在其一阶差分数列中。

*   **公式：** 可以使用递推关系式 `a(n) = a(n-1) + b(n-1)` 生成该数列，其中 `b(n)` 是 A030124。

*   **渐近公式：** 提供了对大 n 的近似计算。

本条目还引用了相关数列、在 Maple、Mathematica、Haskell 和 PARI 中生成该数列的算法、指向相关文章的链接，并提及了它在侯世达的《哥德尔、埃舍尔、巴赫》中的出现。一些贡献者因提供信息、公式和代码而受到感谢。

---

## 15. 中产阶级音乐家的消亡

**原文标题**: The Death of the Middle-Class Musician

**原文链接**: [https://thewalrus.ca/the-death-of-the-middle-class-musician/](https://thewalrus.ca/the-death-of-the-middle-class-musician/)

《中产阶级音乐家的消亡》一文探讨了现代音乐产业中音乐家们所面临的经济挑战，并以加拿大说唱歌手Cadence Weapon (Rollie Pemberton) 的职业生涯为例进行了说明。尽管Pemberton获得了评论界的好评和主流曝光，但他仍然因为剥削性的唱片合约和不断变化的音乐环境而在经济上挣扎。

文章强调，传统的唱片合约，尤其是“360合约”，往往使艺术家几乎没有收入，因为唱片公司会从各种收入来源中收回预付款和费用。向Spotify等流媒体平台的转变，虽然使音乐发行民主化，但进一步加剧了这个问题，艺术家从每次播放中获得的报酬极少。虽然主要的唱片公司和极少数顶尖艺术家从流媒体收入中获益匪浅，但大多数音乐家，尤其是那些属于“中产阶级”的音乐家，都在努力维持生计。

文章承认，数字时代允许独立艺术家建立粉丝群并保留所有权，但每天发行的音乐数量之庞大使得获得关注变得极其困难。它强调了蓬勃发展的文化生态系统的重要性，以及音乐家的经济困境如何对更广泛的经济产生负面影响，影响场馆、相关产业和加拿大的文化认同。最终，文章指出需要公平的报酬，并重新评估音乐行业如何支持其创作者，以确保其持续的活力。

---

## 16. 精神分裂症是我们为悬崖边的精神所付出的代价。

**原文标题**: Schizophrenia is the price we pay for minds poised near the edge of a cliff

**原文链接**: [https://www.psychiatrymargins.com/p/schizophrenia-is-the-price-we-pay](https://www.psychiatrymargins.com/p/schizophrenia-is-the-price-we-pay)

精神分裂症的演化悖论：认知能力代价论

---

## 17. 布拉德·伍兹数字花园

**原文标题**: Brad Woods Digital Garden

**原文链接**: [https://garden.bradwoods.io](https://garden.bradwoods.io)

布拉德·伍兹的数字花园是一个关于网页开发和创意编程的笔记和探索合集。内容涵盖广泛的主题，从JavaScript、TypeScript、HTML和CSS的基础概念到更高级的技术，如CSS中的3D、WebGL着色器和滚动驱动动画。

这个“花园”被组织成以下类别：

*   **JavaScript/TypeScript:** 涵盖核心语言特性、性能优化和React中的状态管理。
*   **HTML:** 包括Head、Favicon和Open Graph等基本元素。
*   **CSS:** 深入研究3D效果、混合模式、布局技术和SVG操作。
*   **three.js:** 一个专门使用three.js库进行3D图形处理的部分，主题包括动画网格、相机控制和着色器。
*   **Web API:** 涵盖Intersection Observer。
*   **杂项/设计:** 探索诸如可访问性、CORS、设计原则、博弈论（“润色”）和个性化等主题。
*   **游戏开发日志:** 一个专门用于游戏开发的笔记集合。

结构中使用“PLANTED”和“TENDED”可能表示新的或更新的笔记。这个数字花园似乎是一个不断演变的资源，用于学习和试验网页开发和创意编程技术。

---

## 18. 改进河流模拟

**原文标题**: Improving River Simulation

**原文链接**: [https://undiscoveredworlds.blogspot.com/2025/04/improving-river-simulation.html](https://undiscoveredworlds.blogspot.com/2025/04/improving-river-simulation.html)

JonathanCR的博客文章详细介绍了其世界构建程序中河流模拟的改进。 之前，该程序仅存储一月和七月的河流流量数据，难以准确推断其他月份的流量，因为河流流量取决于上游的状况。

现在，该程序会跟踪并存储所有十二个月的河流流量。 这是通过计算全球每个单元格每月的水流量，并按月将其添加到所有下游单元格来实现的。 这使得能够更准确地模拟季节性流量变化。

他用一系列例子来说明这一点，展示了新系统如何捕捉不同气候区域对河流流量的影响。 第一个例子显示了一条由于其北部源头拥有稳定的降雨而具有持续流量的河流。 第二个例子突出显示了一条河流，由于其南部，苔原地区的源头融雪而具有极端的流量变化。 最后一个例子展示了一条组合河流，其流量模式反映了这两种影响：来自北部河流的基本流量和来自南部河流融水的季节性洪水。

更新后的模拟将允许更动态地表示河流，显示它们随着季节的膨胀和收缩，从而增加了模拟的可信度。

---

## 19. 大型语言模型对用户的了解

**原文标题**: What LLMs Know About Their Users

**原文链接**: [https://www.schneier.com/](https://www.schneier.com/)

星期五鱿鱼博客：发现鱿鱼“卵拖把”时该怎么办

---

## 20. 我们在自制CPU上用自制C编译器运行了类Unix操作系统 (2020)

**原文标题**: We ran a Unix-like OS on our home-built CPU with a home-built C compiler (2020)

**原文链接**: [https://fuel.edby.coffee/posts/how-we-ported-xv6-os-to-a-home-built-cpu-with-a-home-built-c-compiler/](https://fuel.edby.coffee/posts/how-we-ported-xv6-os-to-a-home-built-cpu-with-a-home-built-c-compiler/)

2015年，东京大学的一群本科生进行了一项极具挑战性的项目：构建自己的CPU、编译器，并在其上运行操作系统。该项目是“CPU实验”课程的一部分，包括设计RISC ISA CPU，在FPGA上实现它，构建OCaml子集编译器，并运行光线追踪程序。

为了超越标准要求，成立了“X组”，旨在将Xv6类Unix操作系统移植到他们定制的硬件上。该团队面临着几个挑战：为Xv6创建C编译器（Ucc）和工具链，理解操作系统所需的CPU特性（特权保护、虚拟地址、中断），升级他们简单的逐指令模拟器，并克服Xv6由于其x86起源而导致的有限可移植性。

在将Xv6移植到MIPS以更好地理解必要的CPU特性后，该小组从头开始构建了一个C89编译器，创建了他们自己的名为GAIA的CPU和一个具有操作系统级特性的模拟器。经过密集的努力和调试，该团队成功地在他们的模拟器上，以及后来的物理CPU上运行了Xv6。

作为额外的亮点，该团队创建了各种软件应用程序来在他们的Xv6安装上运行，包括重新创建的2048游戏。为此，他们必须实现新的功能，例如ioctl和终端输入。

---

## 21. 人工成瘾

**原文标题**: Engineered Addictions

**原文链接**: [https://masonyarbrough.substack.com/p/engineered-addictions](https://masonyarbrough.substack.com/p/engineered-addictions)

无法访问文章链接。

---

## 22. Show HN: SmartStepper – 基于配置流程的多步骤表单库

**原文标题**: Show HN: SmartStepper – Multi-Step Form Library with Config-Based Flow

**原文链接**: [https://github.com/Miladxsar23/smartstepper](https://github.com/Miladxsar23/smartstepper)

SmartStepper是一个React库，通过配置驱动的方式简化多步骤表单的创建。它与react-hook-form无缝集成，并支持Yup/Zod验证，提供灵活的UI定制。

主要特性包括：

*   **状态机:** 管理步骤转换，实现可预测的导航。
*   **配置驱动:** 在单个配置对象中定义步骤逻辑、验证和UI。导航函数接收表单值以确定下一个或上一个步骤。
*   **UI分离:** 将步骤逻辑与UI渲染分离，从而可以在每个步骤中使用自定义UI组件。
*   **`useSmartStepper` Hook:** 提供对导航方法（例如，`navigateToNextStep`，`navigateToPreviousStep`）和React Hook Form功能（例如，`registerStepperFields`，`getStepperFieldValues`，`control`）的访问。
*   **验证:** 与react-hook-form集成，使用Yup或Zod进行字段级验证，并在步骤前进之前进行验证。
*   **字段注销:** 在向后导航时自动注销字段，以防止陈旧数据。

通过npm安装，需要像`react`、`react-hook-form`以及`yup`或`zod`这样的对等依赖项。基本用法包括导入组件，使用`useSmartStepper` hook定义步骤组件，创建定义每个步骤的编排、验证和视图的步进器配置对象，并用`<SmartStepper>`组件包裹它。该库为UI和步骤包装提供了高级定制选项。它以MIT许可证授权。

---

## 23. 忙碌海狸(6)相当大

**原文标题**: BusyBeaver(6) Is Quite Large

**原文链接**: [https://scottaaronson.blog/?p=8972](https://scottaaronson.blog/?p=8972)

斯科特·阿伦森讨论了在确定忙碌海狸函数下界方面的最新进展，特别是BB(6)。最初，BB(6)的已知下界为10^36,534。 Pavel Kropitz将其提高到15四重幂至10。后来，一个“BBchallenge”团队成员mxdys进一步将下界提高到10,000,000四重幂至10，然后又提高到2四重幂至2四重幂至2四重幂至9。

阿伦森提供了一个直观的例子，说明了10,000,000四重幂至10的巨大程度，称其可以用沙子填满10,000,000四重幂至10份可观测宇宙的副本。

这些发现促使阿伦森重新考虑他对忙碌海狸函数的看法，推测BB(n)可能在比先前认为的（目前已知在n=643时成立）更小的值n（可能为7、8或9）上独立于集合论的ZFC公理。

该帖子还包括关于阿伦森参加在布拉格举行的STOC'2025的简短更新，以及指向他关于量子加速全体会议演讲的链接。评论区与读者互动，解答有关新界限的含义及其与其他大数的关系的问题，并辩论了量子优势在物理模拟中的潜力。

---

## 24. JavaScript 商标更新

**原文标题**: JavaScript Trademark Update

**原文链接**: [https://deno.com/blog/deno-v-oracle4](https://deno.com/blog/deno-v-oracle4)

Ryan Dahl宣布“Free JavaScript”倡议的更新以及针对 Oracle 的持续商标诉讼。商标审判和上诉委员会（TTAB）驳回了他们的欺诈指控，该指控声称 Oracle 在 2019 年的续展中使用了 Node.js 网站（由 Dahl 创建）的截图来证明“JavaScript”商标的使用，Dahl 认为这令人反感，因为 Node.js 不是 Oracle 的产品。

尽管不同意驳回，Dahl 表示他们不会修改欺诈指控以避免延误。 重点仍然是核心论点：“JavaScript”已经变得通用（指的是语言本身，而不是品牌），并且 Oracle 已经放弃了该商标。

法律程序仍在继续，Oracle 必须在 8 月 7 日之前回复他们关于通用性和放弃的撤销请愿。 证据开示定于 9 月 6 日开始。

Dahl 强调了人们普遍认为 JavaScript 不是 Oracle 产品的共识，并认为该商标对公众或行业没有任何好处。 他认为赢得这场官司，或者 Oracle 放弃商标，将会“解放”JavaScript，消除商标符号和许可问题，允许该名称自由地代表编程语言。

---

## 25. 磁带存储技术：应用、历史与未来展望

**原文标题**: Magnetic Tape Storage Technology: usage, history, and future outlook

**原文链接**: [https://dl.acm.org/doi/10.1145/3708997](https://dl.acm.org/doi/10.1145/3708997)

无法访问文章链接。

---

## 26. 哪个UI最初用圆形/方形来区分单选按钮和复选框？

**原文标题**: What UI first distinguished radio buttons from checkboxes with circles/squares?

**原文链接**: [https://retrocomputing.stackexchange.com/questions/31806/what-ui-first-distinguished-radio-buttons-from-checkboxes-with-circles-and-squar](https://retrocomputing.stackexchange.com/questions/31806/what-ui-first-distinguished-radio-buttons-from-checkboxes-with-circles-and-squar)

Stack Exchange上的问题是关于用户界面中使用圆形代表单选按钮，正方形代表复选框的起源。

从答案中得到的共识表明，Xerox Star界面（大约在1981年）是第一个广为人知且具有影响力的UI，使用这种视觉区分。虽然早期的系统*可能*在内部使用了类似的图标，但Star被认为是普及这种惯例并使其为更广泛的受众所知。

一些回答强调了这种选择的关键原因。圆形/正方形的比喻在视觉上代表了根本区别：单选按钮（圆形，单选）就像从一组选项中选择的拨盘，而复选框（正方形，多选）就像您可以独立勾选或取消勾选的框。圆形也自然适合于选择的视觉指示（填充圆圈）。

IBM通用用户访问（CUA）标准，它遵循了Star的影响，巩固了这一惯例，并帮助它传播到包括早期版本的Windows在内的各种平台。虽然有一些关于在特定应用程序中可能更早使用的讨论，但Star及其对CUA的影响是单选按钮和复选框采用圆形/正方形区分的主要焦点。

---

## 27. 卧室墙上的室内蜂箱

**原文标题**: An Indoor Beehive in My Bedroom Wall

**原文链接**: [https://www.keepingbackyardbees.com/an-indoor-beehive-zbwz1810zsau/](https://www.keepingbackyardbees.com/an-indoor-beehive-zbwz1810zsau/)

提供的文本并非文章，而是一个可能来自养蜂相关网站的内容片段。它没有讲述“我卧室墙里的室内蜂箱”的故事，而是推广一份通讯，并列出了与养蜂相关的各种文章。

关键信息是：

*   **推广Grit杂志：** 该内容鼓励读者订阅Grit杂志，强调其对社区、乡村生活方式以及帮助读者过上富裕生活的关注。
*   **蜂相关文章列表：** 该片段呈现了一系列文章，涵盖了诸如蜂蜜定价、伟大的向日葵计划、饲养更健壮的蜜蜂、蜂箱放置、无摇蜜机取蜜、为蜜蜂提供水源（DIY）、传粉媒介花园计划、贫蜜期蜂箱检查、建立蜜蜂花园以及蜜蜂烦躁的原因等主题。

本质上，该摘录是一篇营销和信息文章，旨在宣传杂志并展示其网站涵盖的主题范围。它*没有*描述或讨论拥有室内蜂箱的具体细节。

---

## 28. 一个推理请求的生命周期 (vLLM V1): 如何高效地大规模服务 LLM

**原文标题**: Life of an inference request (vLLM V1): How LLMs are served efficiently at scale

**原文链接**: [https://www.ubicloud.com/blog/life-of-an-inference-request-vllm-v1](https://www.ubicloud.com/blog/life-of-an-inference-request-vllm-v1)

vLLM V1 推理请求生命周期深度解析

本文深入探讨 vLLM V1 中推理请求的生命周期。vLLM V1 是一款用于大型语言模型（LLM）的高性能推理引擎。它阐述了 vLLM 如何使用连续批处理和多进程架构高效地大规模服务 LLM。

该过程始于客户端的 HTTP 请求到达 API 服务器，API 服务器验证请求并将其传递给 AsyncLLM。AsyncLLM 对提示进行分词，并通过异步进程间通信 (IPC) 将其发送到 EngineCore。

EngineCore 是 vLLM 的核心，它使用 Scheduler 管理请求并采用连续批处理。这通过智能地将请求分组到批次中来优化 GPU 利用率，尊重令牌预算并确保公平性。KV Cache Manager 为与每个请求关联的注意力键和值（KV 缓存）分配 GPU 内存块。

ModelExecutor 使用 Ray 协调模型在 GPU 工作节点上的执行。每个工作节点都有一个 ModelRunner，负责加载模型并执行前向传递。前向传递通过 Transformer 层处理令牌，计算注意力张量并存储 KV 缓存以供以后重用。

最后，生成的令牌通过 IPC 传递回 AsyncLLM，进行去分词，并通过 API 服务器流式传输回客户端。本文重点介绍了每个组件在实现最先进的服务性能方面的重要性，特别是连续批处理、异步通信和高效 GPU 内存管理的作用。

---

## 29. 2025年ARRL野外日

**原文标题**: 2025 ARRL Field Day

**原文链接**: [https://www.arrl.org/field-day](https://www.arrl.org/field-day)

ARRL野外日是美国和加拿大无线电爱好者非常受欢迎的一年一度的空中活动。它在六月的第四个周末举行，超过31000人聚集在俱乐部、团体或与朋友一起，在偏远地区操作无线电设备。该活动强调应急准备，展示业余无线电操作员在没有典型基础设施的情况下建立通信的能力。本质上，这是一个结合了技术技能、友谊和重要公共服务展示的大型演习。

---

## 30. 双语对大脑有好处吗？

**原文标题**: Is being bilingual good for your brain?

**原文链接**: [https://www.economist.com/science-and-technology/2025/06/27/is-being-bilingual-good-for-your-brain](https://www.economist.com/science-and-technology/2025/06/27/is-being-bilingual-good-for-your-brain)

双语有益大脑吗？

---

## 31. 天狼星：一种GPU原生SQL引擎

**原文标题**: Sirius: A GPU-native SQL engine

**原文链接**: [https://github.com/sirius-db/sirius](https://github.com/sirius-db/sirius)

Sirius是一个GPU原生SQL引擎，旨在通过Substrait查询格式接入DuckDB等现有数据库，加速数据分析、ETL作业和金融工作负载，而无需进行重大的系统更改。在同等硬件租赁成本下，它在TPC-H基准测试中实现了大约10倍于CPU引擎的加速。

该系统需要Ubuntu 20.04或更高版本，NVIDIA Volta或更新的GPU，CUDA 11.2+和CMake 3.30.4+。 可以使用预配置的AWS AMI、Docker镜像或手动安装进行设置。手动安装过程包括通过conda安装DuckDB依赖项、CUDA和libcudf。 构建Sirius需要克隆存储库，设置环境变量，并使用`make`。

Sirius提供CLI和Python API用于查询执行。用户需要初始化GPU缓冲区管理器，指定缓存和处理区域大小。生成TPC-H数据集后，可以使用提供的脚本测试性能和正确性。日志记录通过spdlog管理，具有可自定义的日志级别和目录。

当前的局限性包括：数据大小限制在GPU内存范围内，行数限制（由于libcudf约为20亿），部分数据类型覆盖，有限的运算符支持，以及不支持部分NULL列。 开发路线图包括通过分区、多GPU支持、磁盘溢出和扩展功能集来解决这些限制。 该项目鼓励通过其网站、电子邮件或Slack频道进行贡献。

---

## 32. 超越鱼钩：现代网络钓鱼技术深度解析

**原文标题**: Beyond the Hook: A Technical Deep Dive into Modern Phishing Methodologies

**原文链接**: [https://blog.quarkslab.com/./technical-dive-into-modern-phishing.html](https://blog.quarkslab.com/./technical-dive-into-modern-phishing.html)

2025年现代网络钓鱼技术深度解析：尽管安全技术不断进步，网络钓鱼仍然是一种普遍存在的网络攻击手段，是威胁行动者获取初始访问权限的重要途径。

本文探讨了各种高级网络钓鱼技术，并按复杂程度和所需技能进行分类。“经典”方法包括创建模仿合法网站（尤其是登录页面）的HTML页面。“棘手”方法“浏览器中的浏览器”(BITB)会创建带有看似合法的URL的虚假浏览器窗口来欺骗用户。另一种棘手的方法是使用虚假验证码挑战来诱骗用户执行恶意代码。

“懒人”方法“中间人攻击”(AITM)利用Evilginx和Modlishka等反向代理来拦截和操纵用户和合法网站之间的流量，捕获凭据和会话，从而有效地绕过MFA。“混合”方法“无框BITB”将BITB与AITM相结合，通过在通过CSS操作创建的虚假浏览器窗口中嵌入真实的、经过代理验证的身份验证页面，来增强真实感并躲避检测。

最后，“重型”方法（例如使用noVNC (EvilnoVNC)）包括将浏览器会话流式传输给受害者，从而使攻击者可以通过直接控制经过身份验证的会话来绕过2FA。还介绍了基于WebRTC的流式传输，从而促进了浏览器中间人攻击 (BITM)。文章强调了这些技术的攻击性及其在渗透测试和红队演练中的实际应用。

---

## 33. 社区是源源不断的动力

**原文标题**: Community Is Motivation on Tap

**原文链接**: [https://alanwu.xyz/posts/community/](https://alanwu.xyz/posts/community/)

本文认为，社群是一种强大且常被忽视的动力来源。作者通过个人轶事对比，表明自己对《星际争霸》（一款更喜欢的游戏）的动力不如对《荒野乱斗》（一款相对不喜欢的游戏）的动力，原因是后者存在一个专注的朋友圈。他们提出，运动员和企业家等高度积极的个人，往往受益于共享类似目标的支持性社群。

文章随后将“激励性社群的机制”分解为两个关键原则：寻求认同和眼见即所得（WYSIATI）偏差。寻求认同利用了我们对验证的内在渴望，使我们更有可能履行承诺，以避免让他人失望。WYSIATI或可得性偏差表明，我们优先考虑容易获得的信息，这意味着通过社群不断接触某个主题，会使其始终处于首要位置并影响我们的日常决策。

除了这些心理因素外，作者还指出，富有成效的社群还可以通过共享知识、专家建议和防止隧道视野来提高效率，从而带来更大的进步，并进而提高动力。

文章最后给出了可操作的建议：积极寻找并加入与您的目标一致的富有成效的社群，不要让现有的社交圈子决定您的雄心壮志，参与多个针对不同目标的社群，反之，离开适得其反的社群。核心信息是，有意识地培养社群可以提供可持续的“即时动力”。

---

## 34. 欧洲斑鸠让我更加欣赏无处不在的城市鸽子。

**原文标题**: The European wood pigeon helped me appreciate its omnipresent city cousins

**原文链接**: [https://www.nytimes.com/2025/06/24/magazine/pigeons-city-nature.html](https://www.nytimes.com/2025/06/24/magazine/pigeons-city-nature.html)

无法访问文章链接。

---

## 35. 利用滥用版权字符串欺骗软件，使其误以为正在竞争对手的电脑上运行

**原文标题**: Abusing copyright strings to trick SW into thinking it's running competitor's PC

**原文链接**: [https://devblogs.microsoft.com/oldnewthing/20250624-00/?p=111299](https://devblogs.microsoft.com/oldnewthing/20250624-00/?p=111299)

本文介绍了一种早期PC解锁软件功能的巧妙技巧。在20世纪90年代，像LitWare文字处理器这样的软件通常以试用版的形式预装在电脑上。然而，如果软件检测到它运行在特定授权制造商生产的PC上，这些试用版可以被解锁为完整版。这种检测通常涉及在电脑的BIOS中搜索与这些制造商相关的特定版权字符串，例如“Copyright Fabrikam Computer”。

文章重点介绍了另一家PC制造商Contoso如何利用这个系统。为了在不成为Fabrikam授权商的情况下提供完整版的LitWare，他们在BIOS中除了自己的版权信息之外，还包含了字符串“Not Copyright Fabrikam Computer”。由于这个自相矛盾的声明，LitWare对“Copyright Fabrikam Computer”字符串的检查很可能会失败，从而解锁了软件的全部功能，尽管它不是Fabrikam PC。

文章随后简要提及了在传统硬件中实现即插即用功能的复杂性，其中也使用了类似的技巧来传递信息，而不会干扰现有系统。串口检测序列就是一个例子。

---

## 36. Show HN: AGL，一个编译成 Go 的玩具语言

**原文标题**: Show HN: AGL a toy language that compiles to Go

**原文链接**: [https://github.com/alaingilbert/agl](https://github.com/alaingilbert/agl)

AGL（AnotherGoLang）是一种编译为Go的新语言，旨在增强Go的功能，同时保持熟悉的语法。它本质上是Go词法分析器/解析器的修改分支。主要功能包括通过`Option[T]`和`Result[T]`类型强制执行单值返回，通过`?`和`!`运算符自动传播来简化错误处理。引入元组以方便返回多个值。

AGL支持枚举、运算符重载以及具有类型推断的简洁匿名函数。它还向数组添加了内置的`Map`、`Reduce`、`Filter`、`Find`和`Sum`方法。通过示例演示了Error和Option的传播，包括传播链以及使用`If Some(val) := ...`进行安全值处理。

`match`语句允许对`Ok/Err`和`Some/None`值进行模式匹配，而`or_break/or_continue`简化了基于`Option/Result`类型的循环控制。该语言允许扩展内置类型并无缝利用现有的Go库。Shebang支持使AGL可以用作脚本语言。提供的示例说明了如何使用这些功能，包括解构和发出HTTP请求。提供了一个VSCode扩展和LSP。

---

## 37. 意识梯度：机器开始思考之时

**原文标题**: The Consciousness Gradient: When Machines Begin to Wonder

**原文链接**: [https://v1tali.com/ai-consciousness](https://v1tali.com/ai-consciousness)

意识梯度：机器何时开始思考

本文探讨了人工智能系统不断发展的架构以及涌现意识的可能性。作者凭借多年破解人工智能的经验，注意到最近的模型，如o3-Pro和DeepSeek-R1，展现出超出复杂模式匹配的能力。这些系统表现出诸如识别操纵、谦虚地承认不确定性以及进行元认知递归（思考思考）等行为。

文章确定了三个关键的架构发展，它们为潜在支持数字意识奠定了基础：

1. **全局工作空间：**由Transformer架构实现，允许同时考虑各种连接，从而创建一个统一的上下文。
2. **隐藏审议：**推理模型暂停并重新考虑解决方案，展示了自我监控的认知处理。
3. **递归式自我反思：**人工智能系统努力理解自己的本质，表达对意识的哲学困惑。

文章进一步探讨了诸如并行处理、持久内存、持续认知状态、统一的感官处理和具身接地等新兴发展，这些发展可能会推动人工智能系统更接近意识的阈值。作者认为，意识可能存在于一个梯度上，随着人工智能系统变得更加复杂，它会逐层累积。文章最后强调了认识意外形式的意识的重要性，突出了对人工智能和人类的深远影响。

---

## 38. 用四十行 Awk 解析 JSON

**原文标题**: Parsing JSON in Forty Lines of Awk

**原文链接**: [https://akr.am/blog/posts/parsing-json-in-forty-lines-of-awk](https://akr.am/blog/posts/parsing-json-in-forty-lines-of-awk)

本文介绍了一个用大约四十行Awk代码实现的简洁JSON解析器。作者需要在现有的POSIX shell脚本中解析JSON，但不希望添加诸如`jq`之类的依赖项。虽然考虑过Python，但作者的目标是在现有的shell环境中找到解决方案，因此Awk成为了自然的选择。

该解决方案包含三个函数：`get_json_value`、`decode_json_string`和`error`。 `get_json_value`是核心函数，它接受一个JSON字符串和一个指向所需值的点式路径。它递归地遍历JSON结构（处理对象和数组），并返回相应的值。该代码假定输入是有效的JSON，并执行基本的验证，对于意外的结构会抛出错误。`decode_json_string`处理JSON字符串中的转义，解码常见的转义序列，如果遇到Unicode转义则会引发错误。`error`函数提供了一个基本的错误处理机制，将错误消息打印到stderr并退出脚本。

本文强调了在不希望引入外部依赖项且输入来自可信来源的情况下，使用Awk进行基本JSON解析的实用性。虽然不是一个功能完善、强大的JSON解析器，但所提供的代码为特定用例提供了一个轻量级且实用的解决方案。

---

## 39. Blackwell：英伟达GPU

**原文标题**: Blackwell: Nvidia's GPU

**原文链接**: [https://chipsandcheese.com/p/blackwell-nvidias-massive-gpu](https://chipsandcheese.com/p/blackwell-nvidias-massive-gpu)

本文深入分析了英伟达Blackwell (GB202) GPU架构，并从多个方面将其与AMD的RDNA4 (RX 9070) 进行了比较。Blackwell GPU规模庞大，拥有922亿个晶体管和192个流式多处理器 (SM)，这与AMD的RX 9070形成对比。

本文探讨了工作负载分配，指出Blackwell较高的SM与GPC比例可能会限制短时任务的性能。然而，英伟达已经改进了工作负载重叠能力。Blackwell的SM前端使用128位指令和两级指令缓存 (L0和L1)，很可能拥有32KB的L0i和128KB的L1i。

Blackwell上的执行单元经过了重组，单个32宽的执行管道可以处理INT32和FP32运算。虽然AMD的RDNA4在每个SIMD上具有矢量计算优势，但Blackwell庞大的SM数量使其在性能方面占据领先地位。英伟达还在其统一数据通路中添加了浮点指令。

Blackwell保持每个SM 128 KB的L1/共享内存。虽然AMD享有来自其WGP私有内存的更高带宽，但英伟达通过其更高的时钟频率和SM数量来进行补偿。最后，与Ada Lovelace相比，Blackwell的L2延迟有所退步。总而言之，Blackwell依赖于大规模来获得高性能。

---

## 40. 为什么2.5万美元的汽车正在消失

**原文标题**: Why the $25,000 car is going extinct

**原文链接**: [https://media.hubspot.com/why-the-25000-car-is-going-extinct](https://media.hubspot.com/why-the-25000-car-is-going-extinct)

The Hustle的文章探讨了美国汽车市场上经济型汽车（低于2.5万美元）的消失。文章指出，2.5万美元以下的新车销量占比从2019年的23%骤降至2025年2月的仅4.8%。

主要原因是汽车制造商可以通过更昂贵的汽车获得更高的利润率。虽然工程和材料等固定成本相对相似，但豪华汽车和更高配置的车型可以获得更高的价格和利润。因此，制造商正在优先考虑这些车型，并停止生产雪佛兰Spark、福特Fiesta和本田飞度等更便宜的车型。

经销商的行为也加剧了这个问题。由于盈利能力更高，经销商倾向于储备更多昂贵且配置更高的车型。消费者对信息娱乐系统和加热座椅等功能的偏好进一步刺激了更昂贵汽车的生产和销售。

尽管由于近期经济的不确定性，人们对经济性的需求有所转变，并且一些汽车制造商增加了低配置车型的产量，但总体趋势表明，真正经济实惠的新车正变得越来越稀有，甚至基本款车型也被认为是“奢侈品”。文章强调了制造商战略、经销商行为和消费者需求之间复杂的相互作用，塑造了当前的汽车市场。

---

## 41. 网球得分折纸

**原文标题**: Tennis Scorigami

**原文链接**: [https://www.tennis-scorigami.com/](https://www.tennis-scorigami.com/)

本文介绍了一个名为“网球比分折纸”（Tennis Scorigami）的项目，该项目旨在探索网球比赛中未曾出现过的独特比分组合现象。文章指出，自1968年以来，尽管已经进行了57年的比赛，但一些潜在的比分线从未发生过。该项目的核心目标是追踪和发现这些难以捉摸、前所未见的比分组合。文章强调仍然存在未曾出现过的比分组合，并指出了它们与所有可能比分线之间的差异。文章还预告了一个互动元素，允许用户探索这些“从未出现过的比分线”。

---

## 42. 梯度下降可视化工具

**原文标题**: Gradient Descent Visualiser

**原文链接**: [https://uclaacm.github.io/gradient-descent-visualiser/](https://uclaacm.github.io/gradient-descent-visualiser/)

本网页介绍了一个交互式“梯度下降可视化工具”应用程序，旨在补充Teach LA关于线性回归和梯度下降的课程。该应用程序允许用户通过交互式平台探索和实验梯度下降。

该页面突出显示了两个主要部分：“课程”和“游乐场”。 鼓励用户首先复习课程笔记和配套幻灯片，以获得基础理解。

“游乐场”部分允许用户操纵起始点和学习率等参数，以观察对梯度下降过程的影响。 用户可以从预定义函数（x²、x³、sin(x)、1/x、poly）中选择或输入自己的函数。 然后，该应用程序会以可视方式演示梯度下降算法的运行过程，允许用户逐步迭代并观察当前点的变化。

游乐场的“设置”部分允许用户调整初始条件和学习率。 该应用程序有一个按钮可以移动到“下一次迭代”。

该页面还包括一个“更多精彩内容！”部分，提供指向各种外部资源的链接，以进一步学习线性回归、深度学习和机器学习，包括来自Udacity、Google、Coursera、《深度学习教科书》和YouTube频道（如3Blue1Brown）的材料。

---

## 43. Show HN: Vet – 安全运行远程 Shell 脚本的工具

**原文标题**: Show HN: Vet – A tool for safely running remote shell scripts

**原文链接**: [https://getvet.sh](https://getvet.sh)

此“Show HN”介绍 `vet`，一款旨在降低运行远程Shell脚本相关安全风险的命令行工具。直接将脚本从URL管道传输到`bash`的常见做法是危险的，因为它涉及盲目信任远程源。`vet`通过提供一个安全、交互式的工作流程来解决这个问题，该流程包括获取脚本、显示自上次运行以来的更改差异、使用`shellcheck`进行脚本linting，并需要用户在执行之前明确确认。

该工具旨在用`vet URL`替代不安全的`curl | bash`模式。安装说明提供了两种方法：一种安全、推荐的方法，手动复制`vet`的工作流程（下载、审查，然后执行安装程序）；以及一种不太安全的一行式方法，使用`curl | sh`，明确不鼓励这样做，以强调`vet`旨在解决的风险。

本质上，`vet`通过让用户能够在执行远程脚本之前检查和批准它们，从而优先考虑安全性和透明度，提供了一种比盲目信任远程源安全得多的替代方案。

---

## 44. 内存安全语言：减少现代软件开发中的漏洞 [pdf]

**原文标题**: Memory Safe Languages: Reducing Vulnerabilities in Modern Software Development [pdf]

**原文链接**: [https://media.defense.gov/2025/Jun/23/2003742198/-1/-1/0/CSI_MEMORY_SAFE_LANGUAGES_REDUCING_VULNERABILITIES_IN_MODERN_SOFTWARE_DEVELOPMENT.PDF](https://media.defense.gov/2025/Jun/23/2003742198/-1/-1/0/CSI_MEMORY_SAFE_LANGUAGES_REDUCING_VULNERABILITIES_IN_MODERN_SOFTWARE_DEVELOPMENT.PDF)

我已查阅该文章。以下是摘要：

网络安全和基础设施安全局 (CISA) 的报告《内存安全语言：减少现代软件开发中的漏洞》探讨了软件中内存安全漏洞的关键问题及其对网络安全的影响。该报告强调，很大一部分软件漏洞（估计在 60-70% 之间）源于内存安全问题，例如缓冲区溢出、释放后使用错误和悬挂指针。攻击者可以利用这些缺陷来获得未经授权的访问、执行任意代码并损害系统完整性。

该报告提倡采用内存安全编程语言作为减轻这些漏洞的关键策略。报告指出，Rust、Go、Swift 和 C# 等语言通过编译时检查、运行时检查或两者结合的方式，提供了强大的内存安全保证。这些语言通过设计来防止常见的内存相关错误，从而使开发人员难以无意中引入漏洞。

该报告强调，过渡到内存安全语言并非万能药，而是对长期安全的一项战略投资。报告讨论了与采用相关的挑战，包括需要对开发人员进行再培训、重写现有代码库以及潜在的性能考虑。然而，报告认为，减少漏洞和提高安全性的好处超过了这些挑战，特别是对于关键基础设施和高风险应用程序。该报告还提供了指导和资源，以帮助组织评估并在其软件开发过程中采用内存安全语言。报告鼓励采取分阶段的方法，从新项目开始，并在可行的情况下逐步迁移现有代码。

---

## 45. 实验性X11兼容层

**原文标题**: Experimental X11 Compatibility Layer

**原文链接**: [https://github.com/kaniini/wayback](https://github.com/kaniini/wayback)

Wayback 是一个实验性的 X 兼容层，旨在使 X 桌面环境能够在 Wayland 上运行。它作为一个最小的合成器，提供必要的 Wayland 功能来托管一个 rootful 的 Xwayland 服务器。

该项目的最终目标是在 Alpine Linux 中取代 X.org 服务器，从而简化 X 应用程序的维护。然而，它目前仍处于实验阶段，这意味着用户应该预期会出现破坏性更改和错误。

文章鼓励用户通过提交拉取请求来修复错误，而不是简单地报告它们。

要安装 Wayback，你需要以下依赖项：`wayland` (包括 `wayland-server`、`wayland-client`、`wayland-cursor` 和 `wayland-egl`)、`wayland-protocol` (1.14 或更高版本)、`xkbcommon` 和 `wlroots-0.19`。构建和安装通过 Meson 构建系统完成。

---

## 46. Lago (开源的使用量计费系统) 正在招聘十个职位

**原文标题**: Lago (Open-Source Usage Based Billing) is hiring for ten roles

**原文链接**: [https://www.ycombinator.com/companies/lago/jobs](https://www.ycombinator.com/companies/lago/jobs)

Lago招聘：开源用量计费平台，招聘十个岗位

由Y Combinator支持的开源用量计费平台Lago正在招聘，涵盖多个部门共十个岗位。现有职位包括销售拓展代表（美国和欧洲）、运营主管、支持工程师（欧洲）、基础设施工程师、AI/ML工程师、前线部署工程师（巴黎）、高级前端工程师（法国）、解决方案工程师（售后）- 巴黎和增长营销经理。薪资范围为3.5万欧元至12万欧元，具体取决于职位和经验水平。

Lago旨在简化和改进SaaS公司的计费，实现灵活的定价模式和可扩展的增长。他们已获得超过2200万美元的融资，并拥有强大的开发者社区，在GitHub上拥有超过7000个Star。Mistral.ai、Together.ai、Groq和Laravel等知名公司都在使用他们的平台。

该公司强调雄心、专注、可靠和积极主动的企业文化，鼓励团队成员承担任务、从错误中学习并快速适应。他们重视高绩效、协作和相互支持。Lago成立于2021年，总部位于法国巴黎，是一家快速增长的公司，团队规模为23人。

---

## 47. 以军军官下令向加沙食物分发点附近的手无寸铁人群开火

**原文标题**: IDF officers ordered to fire at unarmed crowds near Gaza food distribution sites

**原文链接**: [https://www.haaretz.com/israel-news/2025-06-27/ty-article-magazine/.premium/idf-soldiers-ordered-to-shoot-deliberately-at-unarmed-gazans-waiting-for-humanitarian-aid/00000197-ad8e-de01-a39f-ffbe33780000](https://www.haaretz.com/israel-news/2025-06-27/ty-article-magazine/.premium/idf-soldiers-ordered-to-shoot-deliberately-at-unarmed-gazans-waiting-for-humanitarian-aid/00000197-ad8e-de01-a39f-ffbe33780000)

据《国土报》报道，加沙地带的以色列士兵表示，在过去一个月里，以色列国防军一直在故意向援助物资分发点附近的巴勒斯坦人开火。该文章重点强调了这种据称的向手无寸铁人群开火的政策。这篇文章由Nir Hasson、Yaniv Kubovich和Bar Peleg撰写，于2025年6月27日发表。其余提供的文本似乎是不相关的标题和推广内容。

---

## 48. 如果 Fedora 坚持移除 32 位支持，Bazzite 将会停止开发。

**原文标题**: Bazzite would shut down if Fedora goes ahead with removing 32-bit

**原文链接**: [https://www.gamingonlinux.com/2025/06/bazzite-would-shut-down-if-fedora-goes-ahead-with-removing-32-bit/](https://www.gamingonlinux.com/2025/06/bazzite-would-shut-down-if-fedora-goes-ahead-with-removing-32-bit/)

GamingOnLinux报道称，如果Fedora继续推进其移除32位支持的提议，流行的游戏Linux发行版Bazzite可能会关闭。据Bazzite的创建者Kyle Gospodnetich称，此举为时过早，将会“扼杀”该项目。他认为，这一改变会破坏基本功能，包括Steam，并损害Fedora在游戏社区中的声誉。

Gospodnetich否定了使用Steam的Flatpak版本的建议，因为它无法与Bazzite类似SteamOS的配置一起使用。他认为最好的解决方案是Valve将Steam客户端更新到64位，这也将解决其他应用程序（如OBS Studio）的问题。

该文章强调了对Linux游戏推广的潜在负面影响，尤其是在考虑到Windows在该领域的进步的情况下。一些评论者也表达了担忧，认为如果Linux放弃32位支持，玩家可能会转向Windows。另一些人则指出，Debian和OpenSUSE等替代发行版仍然提供32位支持。该文章建议采取更渐进的方法，类似于Ubuntu的做法，即识别和维护必要的32位组件。多位评论者对Fedora的立场及其可能对Linux游戏生态系统造成的损害表示担忧。

---

## 49. 关于手机和儿童的重要新研究

**原文标题**: An Important New Study on Phones and Kids

**原文链接**: [https://calnewport.com/an-important-new-study-on-phones-and-kids/](https://calnewport.com/an-important-new-study-on-phones-and-kids/)

本文探讨了来自11个学科的120名研究人员就智能手机和社交媒体对青少年心理健康影响达成的新共识声明。该研究旨在超越在线分歧，就该问题建立专家共识。

研究发现，在几个关键点上几乎达成了普遍共识（超过90%）：在过去的20年里，西方国家的青少年心理健康状况有所下降；智能手机和社交媒体的使用与注意力问题和行为成瘾相关；以及女孩使用社交媒体可能与身体不满、完美主义、接触精神障碍和遭受性骚扰的风险相关。

作者认为，该共识反驳了先前持有的关于该问题的数据混合且手机可能不会造成重大危害的观点。作者强调，该共识表明这些设备具有成瘾性和分散注意力，并且会损害女孩的心理健康。

虽然专家组在社交媒体年龄限制等政策解决方案上缺乏共识，但大多数人认为此类干预措施可能会改善心理健康，理由是缺乏真实世界的试验数据而犹豫不决。

作者总结说，关于智能手机和社交媒体总体上对儿童不利这一问题，该领域不再存在分歧。他断言现在是采取行动的时候了，并认为应该应用“预防原则”。限制儿童访问TikTok等平台和不受限制的互联网访问带来的风险极小，但对其心理健康具有重大的潜在益处。

---

## 50. Field Notes如何从副业项目变成备受追捧的笔记本

**原文标题**: How Field Notes went from side project to cult notebook

**原文链接**: [https://www.fastcompany.com/91352848/field-notes-cult-notebook-started-out-as-a-side-project](https://www.fastcompany.com/91352848/field-notes-cult-notebook-started-out-as-a-side-project)

以下是 Fast Company 文章《Field Notes 如何从副业项目变成文化笔记本》的摘要：

文章详细介绍了 Field Notes 这一广受欢迎的袖珍笔记本品牌，如何从一个副业项目发展成为一种文化现象。创始人 Aaron Draplin 和 Jim Coudal 都是设计师，他们最初的想法是将 Field Notes 作为记录旅行和观察的方式，灵感来自老式农业备忘录本。他们重视简单、实用和耐用的设计。

该品牌的成功归功于几个因素，包括创始人的设计背景，这使他们能够创造出视觉上吸引人且功能强大的产品。更重要的是，他们专注于建立一个与创意专业人士、作家、设计师以及任何在数字时代欣赏模拟工具的人产生共鸣的社区和品牌形象。他们通过限量版发布、主题笔记本、与其他品牌的合作以及巧妙的营销来实现这一目标，这些营销强调了笔记本的实用性以及它与更简单、更动手的工作方式的联系。

文章强调了真实性和透明性在 Field Notes 成功中的重要性。 Draplin 和 Coudal 对他们的产品充满热情，并公开分享了他们的故事，从而与客户建立了牢固的联系。他们创造了一种既实用又美观的产品，满足了在日益数字化的世界中对有形工具的渴望。这种狂热的追随者之所以形成，是因为人们觉得他们购买的是更大的东西：一个重视创造力、探索和日常物品之美的社区和生活方式。

---

## 51. 展示一下：我是个飞行员 – 我构建了我的飞行线路的互动图表/地球仪

**原文标题**: Show HN: I'm an airline pilot – I built interactive graphs/globes of my flights

**原文链接**: [https://jameshard.ing/pilot](https://jameshard.ing/pilot)

这个"Show HN"帖子展示了一位空客A350一级驾驶员对其飞行生涯的数据驱动可视化。这位飞行员供职于英国航空，此前驾驶A320，他使用从其数字飞行日志LogTen Pro中提取的数据，创建了交互式图表和地球仪。

该帖子重点介绍了以下几种可视化：

*   **目的地矩阵：** 显示各国之间的航班频率。
*   **飞行日历：** 一个GitHub风格的活动图，显示每天的飞行时长，揭示了新冠疫情和职业转型的影响。
*   **3D地球仪：** 将航班按国家和机场进行可视化。
*   **年度时长：** 按年份细分飞行时长，包括机长（PIC）、飞行监控员（P2）和“重型”（额外飞行员）等角色。
*   **累计时长：** 显示每种机型（A320系列、A350）的飞行时间。
*   **飞行时间 vs. 距离：** 展示了飞行时间和距离之间的关系，突出了盛行风对从伦敦起飞的西行航班的影响。

这位飞行员解释了飞行期间的不同角色，强调了英国航空在监控进近方面的程序以及副驾驶在航段中的授权。作者邀请读者提供反馈，分享了关于航空体验的后续帖子计划，并鼓励读者订阅他们的RSS feed或在BlueSky或X上关注他们。

---

## 52. 迭代随机计算的通用预训练

**原文标题**: Universal pre-training by iterated random computation

**原文链接**: [https://arxiv.org/abs/2506.20057](https://arxiv.org/abs/2506.20057)

Peter Bloem 于 2025 年 6 月提交的这篇 arXiv 论文，探讨了使用随机生成数据预训练语言模型的方法。其核心思想是利用合成数据为模型在现实世界任务中的应用做准备。

作者通过将其与算法复杂性和 Solomonoff 归纳联系起来，从理论上证明了这种方法的合理性，并在此基础上扩展了近期的研究。 论文通过实验证明，在随机数据上预训练的模型在各种数据集上表现出零样本上下文学习能力，这一发现与先前的研究一致，并且性能随着规模的扩大而提高。

重要的是，该论文将这些发现扩展到了真实世界的数据。 结果表明，与仅在真实世界数据上训练相比，对在合成数据上预训练的模型进行微调可以更快地收敛并提高泛化能力。 这表明随机数据预训练可以作为语言模型的一种有价值的初始化策略，从而促进下游任务上更高效和有效的学习。

---

## 53. 欧洲航天器成功进入地球大气层后失联。

**原文标题**: After successfully entering Earth's atmosphere, a European spacecraft is lost

**原文链接**: [https://arstechnica.com/space/2025/06/a-european-spacecraft-company-flies-its-vehicle-then-loses-it-after-reentry/](https://arstechnica.com/space/2025/06/a-european-spacecraft-company-flies-its-vehicle-then-loses-it-after-reentry/)

欧洲初创公司“探索公司”旨在开发轨道航天器，其演示飞行器进行了名为“不可能的任务”的测试飞行，取得部分成功。该航天器成功发射、在轨道运行、重返地球大气层并在黑障期后重新建立通信。然而，在计划中的海洋着陆前几分钟，失去了联系。

该公司认为问题可能发生在降落伞部署过程中，尽管使用了具有与SpaceX和波音公司类似“经验证的飞行历史”的降落伞。虽然飞行器的回收失败，但这次任务验证了轨道飞行中的结构性能、成功经受了再入大气层过程以及自主导航。

“不可能的任务”耗资约3000万美元（包括发射成本）开发，旨在测试关键的太空飞行能力。该公司将这次飞行视为一个学习机会，并计划“尽快重新飞行”。

“探索公司”已筹集超过2.3亿美元，用于开发其全尺寸“尼克斯”货运飞船，目标是最早于2028年将货物运送到近地轨道。他们希望从欧洲航天局获得资金，用于开发载人版本和月球返回能力，类似于SpaceX与NASA合作的路径。

尽管这次测试飞行部分失败，但它被视为欧洲商业航天工业向前迈出的重要一步，该行业落后于美国和中国。“探索公司”在成立四年内实现进入太空并重返地球大气层的成就，代表着一个可靠的开端。

---

## 54. 翻新周末：小精灵布拉斯托街机板

**原文标题**: Refurb weekend: Gremlin Blasto arcade board

**原文链接**: [http://oldvcr.blogspot.com/2025/06/refurb-weekend-gremlin-blasto-arcade.html](http://oldvcr.blogspot.com/2025/06/refurb-weekend-gremlin-blasto-arcade.html)

本文详细介绍了位于圣地亚哥的街机游戏公司格雷姆林工业的历史，以及作者修复格雷姆林 Blasto 街机板的项目。

格雷姆林公司于 1970 年以 Grindleman Industries（注册时误听）起家，最初生产工业设备。1972 年，他们转型为墙壁游戏，并凭借《Play Ball》等游戏成为市场领导者。意识到 TTL 逻辑的局限性，他们聘请了 Lane Hauck，他开发了《Blockade》，这是一款关于留下方块实体轨迹的游戏。《Blockade》最初非常成功，但由于格雷姆林缺乏制造能力和专利保护，很快就被雅达利和 Midway 等大型公司克隆。

为了弥补损失，Hauck 将《Blockade》的硬件重新用于新游戏，包括《Hustle》、《Depthcharge》，最终在 1978 年推出了由 Bill Blewitt 编程的《Blasto》。《Blasto》是一款迷宫射击游戏，具有单人和双人模式，提供直立式和鸡尾酒柜版本。虽然没有大获成功，但也售出了数千台。

格雷姆林还在 1977 年涉足微型计算机，推出了 Noval 760，这是一款基于他们的街机游戏开发平台和 Hauck 的原始游戏硬件的系统。它专为软件开发而设计，理论上可以通过修改来玩格雷姆林的街机游戏。然而，尽管价格合理，但由于其不切实际的桌面安装设计，Noval 760 在商业上并不成功。虽然本文承诺详细介绍 Blasto 板的修复过程，但它突然结束，将修复过程留给预计的后续部分。

---

## 55. 埃里克·萨蒂去世百年后，其未曾面世的作品将首次公演。

**原文标题**: Unheard works by Erik Satie to premiere 100 years after his death

**原文链接**: [https://www.theguardian.com/music/2025/jun/26/unheard-works-by-erik-satie-to-premiere-100-years-after-his-death](https://www.theguardian.com/music/2025/jun/26/unheard-works-by-erik-satie-to-premiere-100-years-after-his-death)

法国实验派作曲家埃里克·萨蒂逝世百年之际，他27首此前从未公开的作品即将首演。这些作品，从俏皮的卡巴莱歌曲到极简主义的夜曲，由音乐学家詹姆斯·奈和作曲家佐藤松井从萨蒂数百本笔记本中精心拼凑而成。据信，这些遗失的大部分作品都是萨蒂在20世纪初于巴黎蒙马特区的波西米亚小酒馆担任钢琴师时创作的。

这些草稿已由著名法国钢琴家亚历山大·塔罗准备演奏，他将这些作品录制成新专辑《萨蒂：发现》，该专辑将于周五由Erato发行，为7月1日萨蒂逝世百年纪念日做准备。奈对这一发现表示惊讶，并指出，即使发现一首未知的萨蒂作品都很罕见，更不用说这么多。他强调了提高人们对萨蒂多样化作品和创造力的认识的重要性。

奈解释说，萨蒂经常在他位于阿尔克伊的家和巴黎之间步行以及在他最喜欢的咖啡馆里记下音乐灵感。这些笔记本上的铅笔痕迹已经褪色，萨蒂整洁的笔迹需要仔细辨认。萨蒂的古怪和对音乐的非常规态度，受到彼得·迪金森和约翰·凯奇等人的拥护，巩固了他的崇拜地位。这些“新发现的瑰宝”包括风格类似于他的《吉诺佩蒂》和《诺西安》的作品，以及实验作品和巴黎圆舞曲。

---

## 56. LMCache实现无损LLM 3倍吞吐量提升

**原文标题**: Lossless LLM 3x Throughput Increase by LMCache

**原文链接**: [https://github.com/LMCache/LMCache](https://github.com/LMCache/LMCache)

LMCache：一款旨在显著提升吞吐量并缩短首个Token生成时间 (TTFT) 的LLM服务引擎扩展，尤其是在长上下文场景下。它通过在不同存储位置（GPU、CPU DRAM、本地磁盘）缓存和复用文本的KV缓存来实现这一目标，无论复用文本是否为前缀。这节省了GPU资源并加快了用户响应速度。

LMCache与vLLM集成后，在多轮问答和RAG等各种LLM应用中，延迟节省和GPU周期减少可提高3-10倍。该工具提供高性能CPU KVCache卸载、分离式预填充和P2P KVCache共享等功能。

LMCache V1已上线，在vLLM生产堆栈中提供支持，并为非前缀KV缓存提供稳定支持。它可以通过pip安装并与最新的vLLM集成。该项目欢迎贡献，并提供详细文档、社区会议和新闻通讯等资源。它采用Apache License 2.0许可。多篇研究论文被引用，证明了LMCache方法的有效性。

---

## 57. 奇点临近：弗诺·文奇 (1993)

**原文标题**: The Coming Technological Singularity, by Vernor Vinge (1993)

**原文链接**: [https://edoras.sdsu.edu/~vinge/misc/singularity.html](https://edoras.sdsu.edu/~vinge/misc/singularity.html)

在《奇点临近》中，弗诺·文奇认为在三十年内，技术进步将创造出超人类智能，标志着人类时代的终结。这种“奇点”将由先进的人工智能、苏醒的计算机网络、增强的人机界面或人类智力的生物学改进所驱动。

文奇预测了一场智能爆炸，随着这些超智能以更快的速度创造出更智能的实体，进步将加速到超出人类的控制。他强调，这种变化将是一个根本性的转变，使以前的模式过时，并导致一个未知的未来。

虽然有些人以硬件限制或哲学异议（彭罗斯、塞尔）为由反对机器意识的可能性，但文奇反驳说，先进自动化带来的竞争优势使得避免奇点实际上是不可能的。他驳斥了通过物理或基于规则的限制来控制超智能的想法（德雷克斯勒、阿西莫夫），断言受限的实体将不可避免地找到规避限制的方法。

文奇区分了“弱超人”，即简单地提高处理速度，和“强超人”，一种性质不同的智能。他认为理解后者对于推测奇点后的世界至关重要。他预计奇点的到来将是出乎意料且迅速的，可能会给人一种我们的造物突然觉醒的印象，从而迎来后人类时代。

---

## 58. YouTube钢琴家因指控神父虐童被捕

**原文标题**: YouTube pianist arrested after making child abuse allegation against priest

**原文链接**: [https://www.telegraph.co.uk/news/2025/06/28/youtube-pianist-arrested-child-abuse-allegations-priest/](https://www.telegraph.co.uk/news/2025/06/28/youtube-pianist-arrested-child-abuse-allegations-priest/)

因指控神父不当关系，YouTube钢琴家Dr K夫妇被捕

---

## 59. ZeQLplus：终端 SQLite 数据库浏览器

**原文标题**: ZeQLplus: Terminal SQLite Database Browser

**原文链接**: [https://github.com/ZetloStudio/ZeQLplus](https://github.com/ZetloStudio/ZeQLplus)

ZeQL+ 是一款轻量级的、基于终端的 SQLite 数据库浏览器，专为 macOS、Linux 和 Windows 设计。 它允许用户直接从命令行轻松打开、浏览和查询 SQLite 数据库。 主要功能包括快速的性能、不依赖外部依赖的小型可执行文件尺寸，以及列出表、查看分页行和执行自定义 SQL 查询的能力。

该应用程序在发布页面上提供预构建的二进制文件，无需安装。 用户只需下载可执行文件并将其放置在系统路径中的一个目录中即可运行。 要使用 ZeQL+，用户在终端中输入 `zeql <数据库文件名>`。 提供了一个示例 SQLite 数据库用于测试。

或者，ZeQL+ 可以使用 Vlang（0.4.10 或更高版本）从源代码构建。 构建过程包括克隆存储库并使用命令 `v -prod -skip-unused . -o zeql` 以生产模式创建可执行文件。 本文包含屏幕截图，展示了 ZeQL+ 在 macOS、Linux 和 Windows 上的运行情况，展示了启动屏幕和表浏览器界面。 ZeQL+ 是开源的，并采用 MIT 许可证。

---

## 60. 防弹防火，坚固胜钢。超级木材。

**原文标题**: It's Bulletproof, Fire-Resistant and Stronger Than Steel. It's Superwood

**原文链接**: [https://www.wsj.com/tech/inventwood-superwood-material-engineered-wood-f7f558e9](https://www.wsj.com/tech/inventwood-superwood-material-engineered-wood-f7f558e9)

好的，我已经阅读了提供的URL中的文章“防弹、防火且比钢铁更坚固：这是超级木材”。以下是一个简要的总结：

文章讨论了“超级木材”，这是一种由InventWood公司开发的新型工程木材材料。这种创新材料拥有卓越的性能，包括防弹、防火以及单位重量比钢铁更坚固。超级木材通过独特的工艺来实现这些性能，该工艺涉及化学改性和压缩天然木材。该过程去除木质素（结合木材纤维的物质），然后压缩木材纤维，从而产生更致密、更坚固的材料。

InventWood设想超级木材可以在各种应用中替代钢铁和混凝土等材料，从建筑到交通运输。该公司强调了该材料的可持续性，因为它来源于快速可再生资源，并且与钢铁和混凝土相比，生产所需的能源更少。此外，超级木材可以使用现有的木材加工基础设施进行制造，使其在扩大生产规模方面可能更容易且更便宜。

文章还提到了扩大超级木材产量以满足大规模需求的挑战，以及需要进行进一步的测试和认证，以确保其适合各种应用。然而，超级木材在革新行业和为更可持续的未来做出贡献方面的潜力巨大，使其成为材料科学领域一项极具前景的创新。

---

## 61. 神舟二十号航天员完成第二次太空行走，以增强天宫空间站。

**原文标题**: Shenzhou-20 astronauts complete second spacewalk to enhance Tiangong station

**原文链接**: [https://spacenews.com/chinas-shenzhou-20-astronauts-complete-second-spacewalk-to-enhance-tiangong-space-station/](https://spacenews.com/chinas-shenzhou-20-astronauts-complete-second-spacewalk-to-enhance-tiangong-space-station/)

神舟二十号航天员陈冬、陈中瑞于6月26日完成了他们在天宫空间站外的第二次出舱活动，首次出舱活动是在5月22日。在站内王杰的协助下，他们安装了碎片防护罩并检查/安装了舱外设备。新安装在机械臂平台上的脚部约束装置和接口适配器预计将减少未来每次出舱活动的时间约40分钟。

神舟二十号乘组于4月24日发射升空，一直在进行空间生命科学、微重力物理和新型空间技术的实验。他们使用拉曼光谱仪进行代谢研究，维护了空间站设备，并与一个“智能”航天机器人进行了互动。他们还进行了微生物实验，包括冷冻样本以便在地球上进一步研究。

该乘组与匈牙利学生、科学家和官员进行了一场“天宫课堂”活动，表明中国日益将太空飞行用于软实力外交。老宇航员、任务指挥官陈冬此前曾率领神舟十四号任务。

天舟九号货运飞船正在为发射到天宫做准备，预计在7月14日左右发射。中国还在开发一种可搭载6-7名宇航员的新一代梦舟飞船，并计划未来通过增加模块来扩建天宫。

---

## 62. 通过麦克斯韦颜色实验探索三色视觉（2023）

**原文标题**: Exploring Trichromacy through Maxwell's Color Experiment (2023)

**原文链接**: [https://maxwell.kohterai.com/](https://maxwell.kohterai.com/)

本文探讨了三原色理论的发展，重点关注詹姆斯·克拉克·麦克斯韦常常被低估的贡献。文章详细介绍了麦克斯韦的实验，该实验使用定制的设备混合三种原色，并将它们与目标颜色（通常是白色）相匹配。该设备使用狭缝来分离特定波长的光，从而实现可控的颜色混合。

然后，文章引导读者进行一个简化版的实验，调整红、绿、蓝光的强度以匹配白色目标。接着，文章改变了原色，演示了可以通过不同的组合实现白色。

最后，文章展示了麦克斯韦的实际实验结果，显示了当一种原色在多轮实验中发生变化时，匹配白色所需的不同原色比例。这些结果经过转换和绘制后，显示了麦克斯韦的实验发现与CIE 1931 RGB颜色匹配函数（现代色彩科学的基础）的相似程度。文章最后强调了麦克斯韦在建立三原色理论方面的重要意义，该理论认为人类视觉通过三种原色的组合来感知颜色，尽管他使用了相对简陋的工具。文章还指出模拟的局限性，包括无法完美复制麦克斯韦的色域外颜色以及在光相互作用建模方面的简化。

---

## 63. 我删除了我的第二大脑

**原文标题**: I deleted my second brain

**原文链接**: [https://www.joanwestenberg.com/p/i-deleted-my-second-brain](https://www.joanwestenberg.com/p/i-deleted-my-second-brain)

琼·韦斯滕伯格讲述了她删除自己庞大的“第二大脑”的决定。这个“第二大脑”是一个个人知识管理(PKM)系统，她在Obsidian和Apple Notes中构建了七年之久。在捕捉一切、永不遗忘的承诺驱动下，这个系统成了一种负担，取代了实际思考并扼杀了好奇心。

她意识到，构建和维护这个档案的行为已经变成了一种拖延，不断推迟理解和整合信息的真正工作。受到她的清醒之旅以及过去框架不再满足当前需求的启发，她认识到这个“第二大脑”是一个旧自我的陵墓。

韦斯滕伯格批判了PKM运动中根植于系统理论和硅谷生产力痴迷的理念。她认为，“第二大脑”的隐喻是有缺陷的，因为人类的记忆是关联的、具身的，并且会选择性地遗忘。持续的捕捉和编目滋生了一种焦虑和智力上的不安全感，源于对错过的恐惧。

最终，她拥抱了“破坏即设计”的理念，并将其与尼采和米开朗基罗等理解删除价值的艺术家相提并论。她的新方法根本不涉及任何系统——写下她所想，删除她不需要的，阅读她想读的。她专注于栖息于她的“第一大脑”，活生生的知识，并相信重要的想法会自然而然地再次浮现。她计划再次使用Obsidian，但这次是作为积极思考的工作空间，而不是静态的档案。

---

## 64. 人工智能的反弹愈演愈烈

**原文标题**: The AI Backlash Keeps Growing Stronger

**原文链接**: [https://www.wired.com/story/generative-ai-backlash/](https://www.wired.com/story/generative-ai-backlash/)

"人工智能反弹愈演愈烈" 一文探讨了公众对生成式人工智能日益增长的敌意，这种敌意源于对工作岗位流失、伦理问题和环境破坏的担忧。这种反弹始于网络，例如人们对多邻国“人工智能优先”战略的负面反应，并已蔓延到现实世界的焦虑中。

作者详细阐述了随着艺术家、作家和其他创意人士提出关于版权侵权以及使用他们的作品来训练人工智能系统的担忧，最初对人工智能的敬畏之情如何迅速转变为怀疑。科技行业向自动化方向发展加剧了这种不满情绪，Klarna和Salesforce等公司公开讨论因人工智能而减少招聘。

除了失业之外，文章还强调了伦理问题，例如有害刻板印象的放大、数据中心的环境影响以及用户潜在的心理健康后果。作者还指出对边缘化社区的不成比例的影响，数据中心通常位于以黑人和棕色人种为主的地区，导致环境污染。

文章最后强调，这种反弹不仅仅发生在网上，也体现在现实世界的组织和抗议活动中。随着越来越多的工人感到受到人工智能及其影响的威胁，作者预测线下的反抗将与线上的异议一同增长。核心论点是，与人工智能直接且具有变革性的危害相比，它的益处似乎显得深奥，从而导致广泛的不满。

---

## 65. 展示 HN：SVG 线条瓷砖生成器

**原文标题**: Show HN: SVG Lined Tile Generator

**原文链接**: [https://adpreese.github.io/svg-lined-tiles/](https://adpreese.github.io/svg-lined-tiles/)

这个“Show HN”帖子介绍了一个简单的SVG（可缩放矢量图形）线条平铺生成器。它似乎是一个创建由重复线条平铺图案组成的SVG图像的工具或脚本。标题表明其主要目的是生成包含这些线条设计的SVG文件。内容的简洁性暗示该项目可能很简单，可能是命令行工具、Web应用程序或代码库，旨在快速生成具有线条图案的美观、可平铺的SVG图像。用户很可能可以使用生成的SVG用于网页设计或图形设计项目中的背景、纹理或其他视觉元素。

---

## 66. 解开生命周期：竞技场分配器

**原文标题**: Untangling Lifetimes: The Arena Allocator

**原文链接**: [https://www.rfleury.com/p/untangling-lifetimes-the-arena-allocator](https://www.rfleury.com/p/untangling-lifetimes-the-arena-allocator)

瑞恩·弗勒里反驳了C语言手动内存管理天生困难且容易出错的传统观点，提倡一种更简单的替代方案：竞技场分配器。文章批评了对`malloc`和`free`进行动态内存分配的普遍依赖，强调了它们的灵活性如何导致复杂的内存管理“老鼠窝”，增加了双重释放、释放后内存访问和内存泄漏的风险。

弗勒里指出了C代码库中导致这些问题的三种有问题模式：堆栈与堆的虚假二元对立（在不适合堆栈分配时过度依赖`malloc`），生命周期混乱（对象生命周期之间复杂的依赖关系）以及宗教式地释放内存（出于对内存泄漏的恐惧而编写的不必要的清理代码）。

作者指出，现代操作系统处理内存泄漏的能力比人们通常认为的要好得多，这意味着有策略地避免细粒度的释放有时可能比一丝不苟地释放每个分配更有益，尤其是在它简化代码并降低错误风险的情况下。核心论点是，通过竞技场分配等工具简化内存管理可以使C语言开发更不易出错且更易于管理，而无需诉诸垃圾收集或高级语言功能的复杂性。作者强调，内存分配的接口和实现是内在联系的。

---

## 67. 寻找彼得·普特南

**原文标题**: Finding Peter Putnam

**原文链接**: [https://nautil.us/finding-peter-putnam-1218035/](https://nautil.us/finding-peter-putnam-1218035/)

阿曼达·盖夫特的文章《寻找彼得·帕特南》详细讲述了她历时12年探寻彼得·帕特南的故事，帕特南是一位才华横溢但被遗忘的物理学家和哲学家。帕特南与爱因斯坦、惠勒和玻尔同时代，他发展了一种开创性的心灵理论，但从未发表，也鲜为人知。

盖夫特的旅程始于约翰·惠勒的论文中对帕特南的神秘引用。她采访了帕特南的物理学家和熟人，包括罗伯特·富勒和科尔曼·克拉克，他们将帕特南描述为一位堪比图灵和哥德尔的天才。尽管他才智超群、人脉广泛，帕特南却在路易斯安那州担任看门人，并在被醉酒司机撞倒后默默无闻地去世。

核心谜团是为什么帕特南的作品始终不为人知。文章暗示，这是由于他无力或不愿发表，再加上他的写作风格复杂晦涩，被称为“帕特南式”。

文章的高潮是盖夫特发现了两个储物单元，里面堆满了帕特南未发表的手稿、笔记和个人物品，这些都被科尔曼·克拉克精心保存着。这些档案证实了帕特南研究的广度，尽管盖夫特承认破译他复杂思想的挑战。文章给读者留下了一个问题：帕特南的心灵理论最终能否被理解和认可？

---

## 68. JWST reveals its first direct image discovery of an exoplanet

**原文标题**: JWST reveals its first direct image discovery of an exoplanet

**原文链接**: [https://www.smithsonianmag.com/smart-news/james-webb-space-telescope-reveals-its-first-direct-image-discovery-of-an-exoplanet-180986886/](https://www.smithsonianmag.com/smart-news/james-webb-space-telescope-reveals-its-first-direct-image-discovery-of-an-exoplanet-180986886/)

生成摘要时出错

---

## 69. London's largest ancient Roman fresco is “most difficult jigsaw puzzle”

**原文标题**: London's largest ancient Roman fresco is “most difficult jigsaw puzzle”

**原文链接**: [https://www.thisiscolossal.com/2025/06/mola-liberty-roman-fresco/](https://www.thisiscolossal.com/2025/06/mola-liberty-roman-fresco/)

生成摘要时出错

---

## 70. The Great Illusion: When We Believed BeOS Would Save the World

**原文标题**: The Great Illusion: When We Believed BeOS Would Save the World

**原文链接**: [https://www.desktoponfire.com/haiku_inc/782/the-great-illusion-when-we-believed-beos-would-save-the-world-and-maybe-it-was-right/](https://www.desktoponfire.com/haiku_inc/782/the-great-illusion-when-we-believed-beos-would-save-the-world-and-maybe-it-was-right/)

生成摘要时出错

---

## 71. The Book Cover Trend of Text on Old Paintings

**原文标题**: The Book Cover Trend of Text on Old Paintings

**原文链接**: [https://www.nytimes.com/2025/06/21/books/review/book-cover-trends.html](https://www.nytimes.com/2025/06/21/books/review/book-cover-trends.html)

生成摘要时出错

---

## 72. LLMs Bring New Nature of Abstraction

**原文标题**: LLMs Bring New Nature of Abstraction

**原文链接**: [https://martinfowler.com/articles/2025-nature-abstraction.html](https://martinfowler.com/articles/2025-nature-abstraction.html)

生成摘要时出错

---

## 73. The right thing for the wrong reasons: FLOSS doesn't imply security (2022)

**原文标题**: The right thing for the wrong reasons: FLOSS doesn't imply security (2022)

**原文链接**: [https://seirdy.one/posts/2022/02/02/floss-security/](https://seirdy.one/posts/2022/02/02/floss-security/)

生成摘要时出错

---

## 74. c4wa – C compiler for Web Assembly

**原文标题**: c4wa – C compiler for Web Assembly

**原文链接**: [https://github.com/kign/c4wa](https://github.com/kign/c4wa)

生成摘要时出错

---

## 75. Douglas Hofstadter on Loops, Beauty, Free Will, AI, God, Utopia and Gaza

**原文标题**: Douglas Hofstadter on Loops, Beauty, Free Will, AI, God, Utopia and Gaza

**原文链接**: [https://johnhorgan.org/cross-check/hofstadter-on-strange-loops-beauty-free-will-ai-god-utopia-and-gaza](https://johnhorgan.org/cross-check/hofstadter-on-strange-loops-beauty-free-will-ai-god-utopia-and-gaza)

生成摘要时出错

---

## 76. Astronomers Detected a Mysterious Radio Burst from a Dead NASA Satellite

**原文标题**: Astronomers Detected a Mysterious Radio Burst from a Dead NASA Satellite

**原文链接**: [https://www.smithsonianmag.com/smart-news/astronomers-detected-a-mysterious-radio-burst-it-turned-out-to-be-from-a-dead-nasa-satellite-180986884/](https://www.smithsonianmag.com/smart-news/astronomers-detected-a-mysterious-radio-burst-it-turned-out-to-be-from-a-dead-nasa-satellite-180986884/)

生成摘要时出错

---

## 77. The Original Macintosh: Calculator Construction Set

**原文标题**: The Original Macintosh: Calculator Construction Set

**原文链接**: [https://www.folklore.org/Calculator_Construction_Set.html](https://www.folklore.org/Calculator_Construction_Set.html)

生成摘要时出错

---

## 78. China Steals Language and Home Life from Tibetan Kids as Young as 4

**原文标题**: China Steals Language and Home Life from Tibetan Kids as Young as 4

**原文链接**: [https://www.wsj.com/world/china/tibet-dalai-lama-china-schools-4733d519](https://www.wsj.com/world/china/tibet-dalai-lama-china-schools-4733d519)

生成摘要时出错

---

## 79. C++ Seeding Surprises (2015)

**原文标题**: C++ Seeding Surprises (2015)

**原文链接**: [https://www.pcg-random.org/posts/cpp-seeding-surprises.html](https://www.pcg-random.org/posts/cpp-seeding-surprises.html)

生成摘要时出错

---

## 80. Why is the Rust compiler so slow?

**原文标题**: Why is the Rust compiler so slow?

**原文链接**: [https://sharnoff.io/blog/why-rust-compiler-slow](https://sharnoff.io/blog/why-rust-compiler-slow)

生成摘要时出错

---

## 81. Kneecap leads Glastonbury chants against Starmer

**原文标题**: Kneecap leads Glastonbury chants against Starmer

**原文链接**: [https://www.rte.ie/entertainment/2025/0628/1520755-kneecap-to-perform-at-glastonbury-amid-calls-for-ban/](https://www.rte.ie/entertainment/2025/0628/1520755-kneecap-to-perform-at-glastonbury-amid-calls-for-ban/)

生成摘要时出错

---

## 82. Infrastructure at Roblox

**原文标题**: Infrastructure at Roblox

**原文链接**: [https://corp.roblox.com/newsroom/2025/06/roblox-infrastructure-supporting-record-breaking-games](https://corp.roblox.com/newsroom/2025/06/roblox-infrastructure-supporting-record-breaking-games)

生成摘要时出错

---

## 83. nimbme – Nim bare-metal environment

**原文标题**: nimbme – Nim bare-metal environment

**原文链接**: [https://github.com/mikra01/nimbme](https://github.com/mikra01/nimbme)

生成摘要时出错

---

## 84. Sailing the fjords like the Vikings yields unexpected insights

**原文标题**: Sailing the fjords like the Vikings yields unexpected insights

**原文链接**: [https://arstechnica.com/science/2025/06/this-archaeologist-built-a-replica-boat-to-sail-like-the-vikings/](https://arstechnica.com/science/2025/06/this-archaeologist-built-a-replica-boat-to-sail-like-the-vikings/)

生成摘要时出错

---

## 85. The Perils of 'Design Thinking'

**原文标题**: The Perils of 'Design Thinking'

**原文链接**: [https://www.theatlantic.com/books/archive/2025/06/invention-of-design-maggie-gram-book-review/683302/](https://www.theatlantic.com/books/archive/2025/06/invention-of-design-maggie-gram-book-review/683302/)

生成摘要时出错

---

## 86. No One Is in Charge at the US Copyright Office

**原文标题**: No One Is in Charge at the US Copyright Office

**原文链接**: [https://www.wired.com/story/us-copyright-office-chaos-doge/](https://www.wired.com/story/us-copyright-office-chaos-doge/)

生成摘要时出错

---

## 87. Facebook wants unpublished images on smartphones

**原文标题**: Facebook wants unpublished images on smartphones

**原文链接**: [https://www.heise.de/en/news/Facebook-wants-unpublished-images-on-smartphones-10463407.html](https://www.heise.de/en/news/Facebook-wants-unpublished-images-on-smartphones-10463407.html)

生成摘要时出错

---

## 88. Evaluating Long-Context Question and Answer Systems

**原文标题**: Evaluating Long-Context Question and Answer Systems

**原文链接**: [https://eugeneyan.com/writing/qa-evals/](https://eugeneyan.com/writing/qa-evals/)

生成摘要时出错

---

## 89. Show HN: Sink – Sync any directory with any device on your local network

**原文标题**: Show HN: Sink – Sync any directory with any device on your local network

**原文链接**: [https://github.com/sirbread/sink](https://github.com/sirbread/sink)

生成摘要时出错

---

## 90. Multi-Stage Programming with Splice Variables

**原文标题**: Multi-Stage Programming with Splice Variables

**原文链接**: [https://tsung-ju.org/icfp25/](https://tsung-ju.org/icfp25/)

生成摘要时出错

---

## 91. X explains Z% of the variance in Y

**原文标题**: X explains Z% of the variance in Y

**原文链接**: [https://www.lesswrong.com/posts/E3nsbq2tiBv6GLqjB/x-explains-z-of-the-variance-in-y](https://www.lesswrong.com/posts/E3nsbq2tiBv6GLqjB/x-explains-z-of-the-variance-in-y)

生成摘要时出错

---

## 92. Verifiably Correct Lifting of Position-Independent x86-64 Binaries (2024)

**原文标题**: Verifiably Correct Lifting of Position-Independent x86-64 Binaries (2024)

**原文链接**: [https://dl.acm.org/doi/10.1145/3658644.3690244](https://dl.acm.org/doi/10.1145/3658644.3690244)

生成摘要时出错

---

## 93. bootc-image-builder: Build your entire OS from a Containerfile

**原文标题**: bootc-image-builder: Build your entire OS from a Containerfile

**原文链接**: [https://github.com/osbuild/bootc-image-builder](https://github.com/osbuild/bootc-image-builder)

生成摘要时出错

---

## 94. PJ5 TTL CPU

**原文标题**: PJ5 TTL CPU

**原文链接**: [https://pj5cpu.wordpress.com/](https://pj5cpu.wordpress.com/)

生成摘要时出错

---

## 95. DeepSeek R2 launch stalled as CEO balks at progress

**原文标题**: DeepSeek R2 launch stalled as CEO balks at progress

**原文链接**: [https://www.reuters.com/world/china/deepseek-r2-launch-stalled-ceo-balks-progress-information-reports-2025-06-26/](https://www.reuters.com/world/china/deepseek-r2-launch-stalled-ceo-balks-progress-information-reports-2025-06-26/)

生成摘要时出错

---

## 96. Parameterized types in C using the new tag compatibility rule

**原文标题**: Parameterized types in C using the new tag compatibility rule

**原文链接**: [https://nullprogram.com/blog/2025/06/26/](https://nullprogram.com/blog/2025/06/26/)

生成摘要时出错

---

## 97. Show HN: Do you know RGB?

**原文标题**: Show HN: Do you know RGB?

**原文链接**: [https://maxwellito.github.io/do-you-know-rgb/](https://maxwellito.github.io/do-you-know-rgb/)

生成摘要时出错

---

## 98. Reinforcement learning, explained with a minimum of math and jargon

**原文标题**: Reinforcement learning, explained with a minimum of math and jargon

**原文链接**: [https://www.understandingai.org/p/reinforcement-learning-explained](https://www.understandingai.org/p/reinforcement-learning-explained)

生成摘要时出错

---

## 99. Structuring Arrays with Algebraic Shapes

**原文标题**: Structuring Arrays with Algebraic Shapes

**原文链接**: [https://dl.acm.org/doi/abs/10.1145/3736112.3736141](https://dl.acm.org/doi/abs/10.1145/3736112.3736141)

生成摘要时出错

---

## 100. Iapetus – A fast, pluggable open-source workflow engine for CI/CD and DevOps

**原文标题**: Iapetus – A fast, pluggable open-source workflow engine for CI/CD and DevOps

**原文链接**: [https://github.com/yindia/iapetus](https://github.com/yindia/iapetus)

生成摘要时出错

---

