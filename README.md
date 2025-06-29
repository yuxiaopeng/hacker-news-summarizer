# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-06-29.md)

*最后自动更新时间: 2025-06-29 17:45:44*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 2 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 3 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 4 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 5 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 6 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 7 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 8 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 9 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 10 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 11 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 12 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 13 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 14 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 15 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 16 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 17 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 18 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 19 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 20 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 21 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 22 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 23 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 24 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 25 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 26 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 27 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 28 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 29 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 30 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 31 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 32 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 33 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 34 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 35 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 36 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 37 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 38 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 39 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 40 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 41 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 42 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 43 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 44 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 45 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 46 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 47 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 48 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 49 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 50 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 51 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 52 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 53 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 54 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 55 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 56 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 57 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 58 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 59 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 60 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 61 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 62 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 63 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 64 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 65 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 66 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 67 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 68 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 69 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 70 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 71 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 72 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 73 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 74 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 75 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 76 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 77 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 78 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 79 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 80 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 81 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 82 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 83 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 84 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 85 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 86 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 87 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 88 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 89 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 90 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 91 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 92 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 93 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 94 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 95 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 96 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 97 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 98 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 99 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 100 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 101 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 102 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
