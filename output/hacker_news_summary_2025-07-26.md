# Hacker News 热门文章摘要 (2025-07-26)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 我们如何攻破Copilot

**原文标题**: How We Rooted Copilot

**原文链接**: [https://research.eye.security/how-we-rooted-copilot/](https://research.eye.security/how-we-rooted-copilot/)

我们如何Root掉Copilot：文章详述了Eye Security如何发现并利用SharePoint零日漏洞（CVE-2025-53770）导致大规模漏洞利用的事件。文章回顾了从最初的SOC警报分流到发现根本原因（SharePoint中先前未知的安全漏洞）的全过程。时间线始于2025年7月18日晚。该博客文章可能更详细地介绍了该漏洞的具体技术方面、利用过程以及潜在影响，并深入分析了看似无害的警报如何导致发现和利用像SharePoint这样广泛使用的平台中的关键安全漏洞，最终使他们能够“root” Copilot（据推测是通过利用SharePoint漏洞获得的访问权限）。

---

## 2. 在所有GPU上运行Rust

**原文标题**: Rust running on every GPU

**原文链接**: [https://rust-gpu.github.io/blog/2025/07/25/rust-on-every-gpu/](https://rust-gpu.github.io/blog/2025/07/25/rust-on-every-gpu/)

本文详细介绍了一个 Rust 演示，该演示实现了跨平台 GPU 计算，使得单个共享的 Rust 代码库能够在不同的 GPU 平台（NVIDIA CUDA、Vulkan/SPIR-V、Apple Metal、DirectX 12、WebGPU）和 CPU 后备方案上运行，而无需专门的着色器语言。它重点介绍了三个关键的 Rust 项目，促进了这一实现：Rust GPU（编译为 SPIR-V）、Rust CUDA（编译为 NVVM IR）和 Naga（GPU 语言翻译）。

该演示实现了一个双调排序，展示了 Rust 在 GPU 编程方面的优势，包括 `no_std` 支持、条件编译、newtypes、枚举、traits、内联函数、结构体组合、内存布局控制、模式匹配和泛型。这些特性有助于直接用 Rust 编写清晰、类型安全和高效的 GPU 代码。

本文解释了如何通过特性标志和编译目标选择后端。内核编译过程包括将 Rust 代码编译为设备特定的格式，并在构建时嵌入到二进制文件中。然后，它详细介绍了各种后端（wgpu、CUDA）的构建和运行时过程，包括 Naga 的翻译步骤。通过利用 Rust 的核心特性，该项目证明了 GPU 编程可以更加集成化和类型安全，与传统的 GPU 编程方法相比，可以降低复杂性并提高代码重用率。这是一个里程碑，展示了 Rust 在 GPU 开发中的潜力。

---

## 3. 字体大小调整很有用

**原文标题**: Font-size-adjust Is Useful

**原文链接**: [https://matklad.github.io/2025/07/16/font-size-adjust.html](https://matklad.github.io/2025/07/16/font-size-adjust.html)

本文倡导对CSS属性`font-size-adjust`进行更广泛和不同于通常理解的用法。作者解释说，`font-size`定义的是字形周围的盒子大小，而不是字形本身，导致相同大小的字体显示不一致。`font-size-adjust`允许基于字体的x高度（字母“x”的高度）缩放字体，旨在为不同的字体创建更一致的视觉外观。

作者挑战了`font-size-adjust`主要用于字体回退场景的普遍看法。相反，他们认为它对于确保使用多种字体的网站上字体大小的一致性，以及减轻潜在的未来字体更改引起的视觉变化更有价值。作者建议在CSS重置中包含`font-size-adjust: ex-height 0.53;`，以及像`box-sizing: border-box`这样的属性，以在整个项目中建立更可预测和统一的字体大小标准。他们选择0.53是因为它是Helvetica的比率，但他们认为该范围内的任何数字都应该有效。

---

## 4. 星际天体3I/Atlas是外星科技吗？

**原文标题**: Is the Interstellar Object 3I/Atlas Alien Technology?

**原文链接**: [https://arxiv.org/abs/2507.12213](https://arxiv.org/abs/2507.12213)

这篇2025年7月提交的arXiv文章探讨了星际天体3I/ATLAS可能是外星科技的可能性。该论文由Adam Hibberd、Adam Crowl和Abraham Loeb撰写，分析了该天体的天体动力学，并认为其特性异常到足以考虑其技术起源，特别是在“黑暗森林”理论（费米悖论的一种悲观解释，认为具有敌意的外星生命会避免被发现）的背景下。

作者强调了3I/ATLAS极低概率（小于0.005%）地接近金星、火星和木星。此外，其轨道相对于黄道面的低倾角为地外文明更容易接近地球提供了便利。

该论文还推测了一种假想的“反向太阳奥伯特机动”，即3I/ATLAS可以在近日点期间利用隐蔽的日食来减速并变为太阳束缚。他们提出了在2025年11月下旬/12月初的最佳地球拦截方案，需要在1天文单位处产生约5.9 x 10^-5 天文单位/天^2的非引力加速度。作者还暗示，该天体的轨迹可能表明其有意在近日点后与木星会合，这意味着观察到的非引力加速度将有助于此类机动。

该文章强调，该分析主要具有教学意义，基于观察到的异常现象和理论可能性，提出了一个供考虑的假设。主题分类包括地球和行星天体物理学、星系天体物理学以及天体物理学仪器和方法。

---

## 5. 地球倾斜了31.5英寸，这不应该发生。

**原文标题**: Earth Has Tilted 31.5 Inches. That Shouldn't Happen

**原文链接**: [https://www.popularmechanics.com/science/environment/a65515974/why-earth-has-tilted-science/](https://www.popularmechanics.com/science/environment/a65515974/why-earth-has-tilted-science/)

地下水抽取显著影响地球倾斜并导致海平面上升

---

## 6. 用开源软件复活一台十年旧的自行车导航仪

**原文标题**: Bringing a decade old bicycle navigator back to life with open source software

**原文链接**: [https://raymii.org/s/blog/Bringing_a_Decade_Old_Bicycle_Navigator_Back_to_Life_with_Open_Source_Software_and_DOOM.html](https://raymii.org/s/blog/Bringing_a_Decade_Old_Bicycle_Navigator_Back_to_Life_with_Open_Source_Software_and_DOOM.html)

雷米·范·埃尔斯特通过开源软件和逆向工程，复活了一台十年前的Navman Bike 1000自行车导航仪，这款导航仪原本是重新贴牌的Mio Cyclo 200。由于过时的地图和官方更新下载失败，该设备面临着计划报废，他便探索了设备的内部运作。

他使用mitmproxy和WireShark拦截了桌面软件的网络请求，揭示了固件和地图更新的下载URL，尽管地图URL已失效。他发现该设备运行的是Windows CE 6.0，并找到一个名为“DODGE.exe”的程序，随后用Total Commander替换了它，以便访问和探索设备的文件系统。

这使他能够安装和运行其他Windows CE应用程序，包括DOOM，以及最重要的NAVeGIS。NAVeGIS是一款与OpenStreetMap兼容的开源导航应用程序，与OpenFietsMap地图一起使用。

通过将开源地图加载到Micro SD卡上，范·埃尔斯特成功地更新了导航系统。虽然缺少一些功能，如音频提示和轨迹记录，但更新后的地图和路线规划功能使该设备再次可以用于自行车导航，有效地绕过了制造商的计划报废。他强调，由于该解决方案是开源的，未来地图提供商的变更不会阻止未来的更新。

---

## 7. 打破WASM/JS通信性能壁垒

**原文标题**: Breaking the WASM/JS communication performance barrier

**原文链接**: [https://github.com/ealmloff/sledgehammer_bindgen](https://github.com/ealmloff/sledgehammer_bindgen)

Sledgehammer bindgen 是一款 Rust 工具，旨在加速 WASM/JS 通信，尤其适用于需要快速、底层 DOM 访问的 Web 框架。与更通用的 `wasm-bindgen` 不同，Sledgehammer 专注于优化的批量绑定。

其速度优势源于几个关键优化：

1.  **高效的字符串解码：** Sledgehammer 不像 `wasm-bindgen` 那样为每个字符串调用 `TextDecoder.decode`，而是以更大的批次解码字符串，从而降低了开销。对于小字符串，它甚至完全绕过解码器以实现更快的 JS 处理。字符串缓存进一步避免了冗余解码。如果字符串是静态的，Sledgehammer 将按指针而不是按值进行哈希。

2.  **字节编码操作：** 操作被编码为数组中紧凑的字节序列。 Sledgehammer 将这些操作分批处理成 u32 块，通过策略性地拆分和内联字节，最大限度地减少数组缓冲区访问对性能的影响。

本质上，Sledgehammer 通过最大限度地降低字符串解码成本以及通过字节编码和批量处理优化数据传输过程来优先考虑速度。虽然不如 `wasm-bindgen` 通用，但对于直接 DOM 操作至关重要且对性能要求苛刻的 Web 框架场景来说，它是一个强大的选择。

---

## 8. Open Sauce 是一个令人困惑但又才华横溢的湾区活动。

**原文标题**: Open Sauce is a confoundingly brilliant Bay Area event

**原文链接**: [https://www.jeffgeerling.com/blog/2025/open-sauce-confoundingly-brilliant-bay-area-event](https://www.jeffgeerling.com/blog/2025/open-sauce-confoundingly-brilliant-bay-area-event)

本文记录了作者在Open Sauce的经历，这是一个由William Osman创建的、类似于湾区创客嘉年华的活动。该活动汇集了各种各样的展品，从疯狂的科学装置到老式电子产品，甚至是魔方解算器。作者在他的退休无线电工程师父亲的陪同下，强调了该活动的一个独特之处，即许多YouTube创客和爱好者的出现，包括CuriousMarc、TubeTime和Ken Sheriff。

作者制作了三个视频博客记录该活动，展示了一个带冷却器的步行咖啡桌，以及与来自Meshtastic、ADSBee和Framework的与会者的互动。他还参与了William Osman新平台Sauce+上的逆向工程小组讨论。一个亮点是与NASA宇航员Matthew Dominick的会面，他讨论了他用于处理国际空间站RAW照片的家庭实验室项目，以及他倡导更多地共享这些文件。

作者将旧金山国际机场以南的湾区与旧金山进行了对比，并指出了寻找有价值的古董技术的独特机会。他强调了该活动在促进创新方面的潜力，并对其未来感到兴奋，希望它能保持目前的精神。他认为Open Sauce是技术过去和未来汇聚的地方，由学生、修补匠和湾区独特的生态系统驱动。

---

## 9. 央视捕捉到地震断层首次移动影像

**原文标题**: CCTV footage captures the first-ever video of an earthquake fault in motion

**原文链接**: [https://www.smithsonianmag.com/smart-news/cctv-footage-captures-the-first-ever-video-of-an-earthquake-fault-in-motion-shining-a-rare-light-on-seismic-dynamics-180987034/](https://www.smithsonianmag.com/smart-news/cctv-footage-captures-the-first-ever-video-of-an-earthquake-fault-in-motion-shining-a-rare-light-on-seismic-dynamics-180987034/)

缅甸一监控摄像头首次拍到2025年3月7.7级地震中地震断层运动视频。地球物理学家Jesse Kearse在视频中注意到断层弯曲滑动，促使他与地球物理学家Yoshihiro Kaneko展开调查。

逐帧分析录像后，他们发现断层在约1.3秒内横向滑动约8.2英尺，峰值速度达到约10.5英尺/秒。这表明地震是脉冲式的，沿着断层传播着集中的滑动爆发。

发表在《地震记录》上的研究结果表明，弯曲滑动路径比以前认为的更为常见，这可能是由于断层表面应力较低。这项研究支持了弯曲的擦痕线（断层表面上的划痕）可以指示地震破裂方向的观点。基于曲率的模型与现实相符，从北向南传播。

这段开创性的录像和分析为了解地震物理学提供了宝贵的见解。它可以帮助地震学家和地质学家更好地预测未来的破裂，并提高基础设施的弹性，最终挽救生命。Kearse和他的团队计划使用物理模型进一步研究断层行为。

---

## 10. 优点与缺点

**原文标题**: Upsides and Downsides

**原文链接**: [https://calv.info/upsides-and-downsides](https://calv.info/upsides-and-downsides)

初创企业成熟之路：从重视“收益”到关注“风险”

---

## 11. 是的，《PF手册》第四版即将推出

**原文标题**: Yes, the Book of PF, Fourth Edition Is Coming Soon

**原文链接**: [https://bsdly.blogspot.com/2025/07/yes-book-of-pf-4th-edition-is-coming.html](https://bsdly.blogspot.com/2025/07/yes-book-of-pf-4th-edition-is-coming.html)

Peter N.M. Hansteen宣布《PF之书》第四版即将于2025年下半年发行。此版本已更新，反映了当前互联网的状况，并从使用OpenBSD 7.8或FreeBSD 14-STABLE用户的角度编写。

此次更新的主要原因是使本书与现代网络现实相符，解决了自2014年第三版发布以来PF配置和功能的变更。虽然以前的版本仍然有价值，但第四版包含了重大更新，尤其是在FreeBSD方面，因此获得了“对FreeBSD友好的版本”的昵称。NetBSD转向NPF以及DragonFly BSD的PF版本过时，促使本书专注于OpenBSD和FreeBSD。

该项目的启动源于对新版本的持续询问，特别是针对FreeBSD，此前Hansteen、Max Stucchi和Tom Smyth已经做了多年的OpenBSD数据包过滤器工具集网络管理教程。在EuroBSDCon 2023之后汇编的注释和修订说明最终说服Hansteen继续进行该项目。

Henning Brauer和Kristof Provost担任技术审阅，编辑过程非常广泛。本书将涵盖现代OpenBSD和FreeBSD版本上的PF，仅简要提及其他平台。Hansteen预计将在萨格勒布举行的EuroBSDcon 2025上提供纸质版，届时他还将展示更新后的教程。他欢迎读者的反馈和意见。

---

## 12. 现代 CSS 是时候终结 SPA 了

**原文标题**: It's time for modern CSS to kill the SPA

**原文链接**: [https://www.jonoalderson.com/conjecture/its-time-for-modern-css-to-kill-the-spa/](https://www.jonoalderson.com/conjecture/its-time-for-modern-css-to-kill-the-spa/)

在他的文章《是时候让现代CSS终结SPA了》中，Jono Alderson认为单页应用(SPA)曾经被认为是实现流畅导航的唯一途径，但现在往往是不必要的，并且对网站性能有害。他提出，现代CSS，特别是视图过渡和推测规则，提供了一种更优越的替代方案。

视图过渡是一个浏览器API，允许在整个网页之间进行平滑的动画过渡，而无需JavaScript。推测规则使浏览器能够根据用户行为预加载或预渲染页面，从而实现近乎即时的导航。Alderson认为这些功能可以取代SPA所依赖的复杂的、JavaScript繁重的路由和水合逻辑。

他批评SPA常常未能兑现其润色的承诺，并列举了诸如滚动恢复失败、焦点行为不一致以及性能下降与视觉效果不成比例等问题。他将基于SPA的网站典型的大型JavaScript包和缓慢的交互时间(TTI)与使用视图过渡和推测规则的现代多页架构(MPA)可实现的0KB JavaScript包和更快的TTI进行了对比。

Alderson认为，许多网站，特别是那些以内容为中心的网站，如营销网站和博客，当作为SPA构建时，会被过度设计。他提倡回归更简单的、HTML驱动的架构，使用原生浏览器功能和CSS进行动画，从而实现更快、更易于维护的网站，并具有更好的SEO和可访问性。他总结说，像2025年那样构建网站，利用现代浏览器的强大功能，可以带来更好的用户体验和更少的开发者遗憾。

---

## 13. 汉萨同盟的兴衰

**原文标题**: The rise and fall of the Hanseatic League

**原文链接**: [https://worksinprogress.co/issue/the-rise-and-fall-of-the-hanseatic-league/](https://worksinprogress.co/issue/the-rise-and-fall-of-the-hanseatic-league/)

本文记录了汉萨同盟的崛起，这是一个中世纪德国商人联盟，它改变了北欧贸易。最初是单个商人为安全和集体谈判而组成“汉萨”，该联盟发展成为一股强大的经济力量，横跨伦敦到俄罗斯。他们在没有中央管理机构的情况下，建立供应链，管理贸易中心，并谈判条约。

本文重点介绍了促成该联盟出现的因素。由于气候变化和罗马基础设施的崩溃等因素，黑暗时代欧洲人口和贸易衰退。然而，“中世纪农业革命”带来了作物产量的增加，导致人口激增以及专业手工艺和城镇的兴起。造船技术的创新，特别是克纳尔船（knarr）和后来的科格船（cog），提高了运输能力。

早期贸易充满了危险，包括海盗、通行费和不可靠的法律体系。“汉萨”通过武装团体旅行，集体谈判贸易权利，并提供相互保护来应对这些挑战。该联盟促进了长途贸易，例如来自诺夫哥罗德的松鼠皮和来自波兰的谷物等商品的规模就证明了这一点。这种转变刺激了工业增长，斯堪的纳维亚半岛的渔业和佛兰德的布料贸易就是例证。英国的羊毛产量蓬勃发展，孕育了富有的商人和令人印象深刻的“羊毛教堂”。到13世纪，科格船取代了克纳尔船，成为主要船只，进一步促进了波罗的海的贸易。

---

## 14. 西蒙·塔特姆的便携谜题集

**原文标题**: Simon Tatham's Portable Puzzle Collection

**原文链接**: [https://www.chiark.greenend.org.uk/~sgtatham/puzzles/](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/)

西蒙·塔特姆的便携谜题集锦是一个单人益智游戏合集，旨在轻量化并在各种平台（包括Unix、Windows和网络（通过JavaScript/WebAssembly））上运行。作者创建此合集是为了提供可在不同操作系统上访问的快速、引人入胜的桌面玩具。

该合集包含现有谜题概念的重新实现，并注明了原始发明者的信息。游戏包括流行的谜题，如黑盒、桥、多米诺、十五拼图、扫雷等等。每个游戏都有在线游戏链接和一个Windows可执行文件下载，以及一个手册链接。

该合集以MIT许可证授权，允许用户广泛地使用和修改游戏，但需注明出处。

该网站提供Windows可执行文件、Windows帮助文件、Windows安装程序以及用于在类Unix系统上编译的源代码的下载。它还包括指向Android和iOS等移动设备第三方移植版本的链接。作者不再支持MacOS版本。

开发者可以通过创建新的谜题或前端来贡献，使用提供的开发者文档和git仓库中的源代码。欢迎提交错误报告和补丁，并附上针对谜题相关问题的相关信息的具体说明。

---

## 15. 倒排索引：循序渐进的实现指南

**原文标题**: Inverted Indexes: A Step-by-Step Implementation Guide

**原文链接**: [https://www.chashnikov.dev/post/inverted-indexes-a-step-by-step-implementation-guide](https://www.chashnikov.dev/post/inverted-indexes-a-step-by-step-implementation-guide)

本文提供了一份逐步指南，用于实现倒排索引以进行高效的文档搜索。首先解释了对倒排索引的需求，强调了其相对于简单扫描每个文档以查找关键字的可扩展性优势。核心思想是创建一个“数据库”，其中单词（标记）是键，而值是包含这些单词的文档 ID（文件名）。

本文逐步介绍了如何构建具有`add`和`getDocumentsForToken`方法的`InvertedIndex`类。然后介绍了一个`IndexGenerator`类，该类读取文件，将文本拆分为标记，清理它们（删除停用词、标签和数字），并将它们添加到索引中。

为了提高性能，本文演示了如何使用 Scala 的并行集合来并行化索引过程。将`merge`方法添加到`InvertedIndex`，以合并由不同线程生成的索引。`runIndexer`函数将要索引的文件分成组，使用`IndexGenerator`并行处理每组文件，然后将生成的索引合并到单个最终索引中。

总之，本文演示了倒排索引的基本实现，涵盖了必要的文本处理注意事项，并解释了如何利用多线程来提高索引速度。作者强调这是一个简化的实现，但它是构建更复杂的文档索引和查询系统的坚实基础。

---

## 16. 衰老在50岁左右加速——有些器官比其他器官更快

**原文标题**: Ageing accelerates around age 50 ― some organs faster than others

**原文链接**: [https://www.nature.com/articles/d41586-025-02333-z](https://www.nature.com/articles/d41586-025-02333-z)

本文报道了一项发表在《细胞》杂志上的研究，该研究调查了衰老如何以不同的速度影响不同的器官。研究人员分析了76名年龄在14-68岁个体中的组织样本，以检查蛋白质随时间的变化。该研究表明，衰老在50岁左右加速，这是一个“拐点”，其中一些组织，特别是像主动脉这样的血管，衰老速度比其他组织更快。

该研究确定了48种与疾病相关的蛋白质随年龄增长而增加的情况，并发现肾上腺在30岁左右出现早期变化，这与衰老过程中已知的激素和代谢转变的重要性相符。主动脉在45至55岁之间显示出最显著的蛋白质水平变化，并且发现来自主动脉的一种特定蛋白质可以加速小鼠的衰老。研究人员假设，血管可能充当载体，将促进衰老的分子分布到全身。

虽然该研究表明衰老可能在50岁左右加速，但其他专家警告说，需要进行更大规模的研究才能明确证实这是一个普遍的“危机点”。这些发现有助于人们日益了解衰老是一个非线性过程，具有明显的快速变化时期，并强化了单个器官以不同速度衰老的观点。

---

## 17. Instapaper 乐天 Kobo 集成

**原文标题**: Instapaper Rakuten Kobo Integration

**原文链接**: [https://blog.instapaper.com/post/789685899750424576/instapaper-rakuten-kobo-integration](https://blog.instapaper.com/post/789685899750424576/instapaper-rakuten-kobo-integration)

Instapaper与乐天Kobo电子书阅读器将于2025年夏末推出全新集成。此次集成将允许Kobo用户在其设备上无缝保存和阅读网页文章，取代Kobo之前与已关闭的Pocket的集成。

Instapaper强调其简洁、无干扰的阅读体验和组织工具，是前Pocket用户迁移到该平台的优势。提供了Pocket用户轻松将其文章导入Instapaper的说明，可以通过Instapaper网站上的2次点击流程或通过Instapaper设置导入Pocket导出文件。

该公告表达了与乐天Kobo合作，为其电子书阅读器提供“稍后阅读”功能的兴奋之情。如有任何问题或疑虑，请联系提供的支持信息。公告后的用户评论表达了兴奋之情，并提出了Kindle集成的请求。

---

## 18. 附加审阅说明

**原文标题**: The append-and-review note

**原文链接**: [https://karpathy.bearblog.dev/the-append-and-review-note/](https://karpathy.bearblog.dev/the-append-and-review-note/)

追加回顾笔记
追加回顾笔记是一种简单的笔记系统，依赖于一个单一的、长文本笔记。其核心原则是：

*   **单一笔记：** 所有笔记都追加到一个文件（例如，在Apple Notes中），以避免管理多个文件和文件夹结构带来的认知负担。这有助于使用CTRL+F轻松搜索。
*   **追加：** 任何新的想法、待办事项或灵感都以纯文本形式添加到笔记的顶部。只使用最少的元数据，除了诸如“watch:”、“listen:”或“read:”之类的标签，以便于分类。
*   **回顾：** 用户定期滚动浏览笔记，将有价值的项目复制并粘贴到顶部进行挽救。这使得重要的想法保持可见，同时允许不太相关的笔记自然沉到底部。笔记很少被删除。

这种方法对于捕捉随机想法、记住推荐、创建临时待办事项列表、起草内容、存储有用的命令、记录实验结果以及清理精神杂乱非常有用。将事情写下来的行为提供了一种认知卸载的感觉。回顾积累的笔记可以通过合并相关想法或在新环境中重温旧想法来产生新的见解。该系统有助于优先处理当前重要的事情，并提供过去想法的历史记录。

---

## 19. 用户声称Discord的年龄验证能被游戏角色蒙混过关

**原文标题**: Users claim Discord's age verification can be tricked with video game characters

**原文链接**: [https://www.thepinknews.com/2025/07/25/discord-video-game-characters-age-verification-checks-uk-online-safety-act/](https://www.thepinknews.com/2025/07/25/discord-video-game-characters-age-verification-checks-uk-online-safety-act/)

本文讨论了据报道用户如何欺骗Discord为遵守英国《网络安全法案》而实施的年龄验证工具。该法案要求托管用户生成内容的平台验证用户年龄，并保护未成年人免受不当内容侵害，Ofcom有权对不合规平台处以罚款。

据报道，Discord的年龄验证（要求用户提供面部照片或身份证件以访问NSFW内容）已被用户提交高保真电子游戏角色照片绕过。一位用户声称使用游戏《死亡搁浅》中的山姆·布里吉斯照片成功通过验证，甚至通过使用游戏照片模式模拟嘴部动作绕过了二次验证。

本文还强调了对英国《网络安全法案》的担忧。电子前沿基金会认为该法案是对隐私和言论自由的威胁，可能导致内容扫描和过滤。其他担忧包括该法案可能迫使小型网站关闭。在该法案颁布后，英国的VPN搜索量显着增加，因为用户试图绕过区域限制。Ofcom表示，平台不得鼓励使用VPN来规避年龄验证。

---

## 20. 不要下载应用，使用网站。

**原文标题**: Do not download the app, use the website

**原文链接**: [https://idiallo.com/blog/dont-download-apps](https://idiallo.com/blog/dont-download-apps)

本文反对下载应用程序，提倡在移动设备上使用网站。文章强调了公司如何积极推动用户下载应用程序，并采用“黑暗模式”来鼓励下载。

公司偏好应用程序使用的主要原因是数据收集。应用程序被设计为与设备深度集成，从而获取大量用户信息，例如联系人、位置、麦克风和已安装的应用程序。另一方面，未经用户明确许可，网站的访问权限受到限制。这种数据提取使公司能够建立全面的用户画像，并可能利用用户行为。

作者质疑应用程序的真正好处，认为表面上的便利往往以牺牲隐私和控制为代价。泄露个人信息很容易，但即使有 GDPR 等法规，也很难取回。

作者总结说，使用网站可以在不牺牲隐私的情况下提供足够的功能。他们强调，抵制下载应用程序的压力是对用户控制和数据安全的一次胜利，使个人能够避免成为口袋里的“持续数字间谍”。文章还包含相关链接、新闻通讯注册、作者社交媒体账号以及用户讨论内容的评论区。

---

## 21. 保持 Pydantic 与你的领域层分离

**原文标题**: Keep Pydantic out of your Domain Layer

**原文链接**: [https://coderik.nl/posts/keep-pydantic-out-of-your-domain-layer/](https://coderik.nl/posts/keep-pydantic-out-of-your-domain-layer/)

本文倡导将 Pydantic 排除在应用程序的领域层之外。虽然 Pydantic 在数据验证方面很方便，尤其是在 FastAPI 等框架中，但随着应用程序的增长，其紧密耦合可能会成为一种负担。保持关注点分离可以使代码更易于维护、测试和适应。

作者建议使用 Dacite 等工具将 Pydantic 模型（通常用于表示层和基础设施层）转换为适用于领域层的普通 Python 对象 (POPO)。Dacite 简化了从字典初始化嵌套数据类的过程，减少了手动样板代码。

文章提出了一种使用存储库和映射器的结构化方法。存储库处理数据持久性和检索，利用映射器在数据存储格式（如字典或 JSON）和领域实体之间进行转换。然后，应用服务编排操作，调用存储库来检索或保存数据，并在实体上调用领域逻辑。

关键在于，Pydantic 主要应驻留在应用程序的外部层（基础设施和表示层），处理数据验证和 API 交互，而领域层则保持纯粹和独立，使用由 Dacite 等库支持的简单数据类。这种分离提高了代码质量和长期可维护性。

---

## 22. 它是DE9，不是DB9（但我们知道你的意思）。

**原文标题**: It's a DE9, not a DB9 (but we know what you mean)

**原文链接**: [https://news.sparkfun.com/14298](https://news.sparkfun.com/14298)

这篇SparkFun的文章澄清了一个关于9针串口连接器的常见误解，它常被错误地称为“DB9”。文章解释说，根据D-sub微型连接器标准，正确的术语实际上是“DE9”。

D-sub中的“D”表示D形金属屏蔽罩。后面的字母表示外壳尺寸，而不是特性。因此：

*   DA：15针外壳
*   DB：25针外壳
*   DC：37针外壳
*   DD：50针外壳
*   DE：9针外壳

术语“DB9”是不准确的，因为它将“B”外壳尺寸（25针）与9针数配对。这个错误称谓的出现，是因为最初的IBM PC使用DB25连接器，当引入9针串口时，人们只是出于熟悉而简单地用“9”替换了“25”。尽管不准确，“DB9”已经成为一个广为人知的术语。

SparkFun决定在其新的DE9连接器分线板上使用正确的“DE9”命名。他们相信技术准确性，并将其视为一个教学机会，即使他们知道很多人会搜索“DB9”。这篇文章强调，虽然“DB9”是常见的用法，但“DE9”才是技术上正确的术语。

---

## 23. 可运输微型工厂的兴起

**原文标题**: The Rise of Shippable Microfactories

**原文链接**: [https://www.thesisdriven.com/p/the-rise-of-shippable-microfactories](https://www.thesisdriven.com/p/the-rise-of-shippable-microfactories)

本文探讨了“可运输微工厂”这一新兴概念，将其作为解决传统预制建筑所面临挑战的潜在方案。与前期成本高昂、运输费用昂贵的集中式大型预制工厂不同，微工厂是紧凑型、自动化生产单元（通常为集装箱大小），可以直接部署在建筑工地或附近。

核心理念是颠倒传统模式：不运输笨重的组件，而是运输工厂本身。这种方法旨在获取异地制造的优势（自动化、效率、受控环境），同时最大限度地减少集中式生产的缺点（高资本支出、运输成本、利用率不足）。

本文概述了“工厂效率方程”，以说明与传统工厂相比，微工厂如何通过提高利用率和降低资本成本来实现更高的效率。文中提供了一些可运输微工厂的例子，范围从轻型机器人框架系统（如AUAR）到全套交钥匙微工厂（如Cuby和Reframe Systems）以及混合方法（如Facit Homes的数控制造）。

AUAR在比利时的部署案例研究表明了微工厂在显著减少劳动力和项目时间表方面的潜力。文章最后承认仍然存在技术障碍，但对可运输微工厂的未来及其对建筑行业的变革潜力表示乐观。

---

## 24. 永远不要编写你自己的日期解析库

**原文标题**: Never write your own date parsing library

**原文链接**: [https://www.zachleat.com/web/adventures-in-date-parsing/](https://www.zachleat.com/web/adventures-in-date-parsing/)

本文详细介绍了作者决定为静态站点生成器Eleventy编写自定义日期解析库的历程，尽管通常不建议这样做。最初，Eleventy使用Luxon进行日期解析，这是一个可靠的选择，但随着Eleventy扩展到更多的JavaScript环境，它在大小方面成为一个重要的依赖项。

作者探索了诸如Moment、Day.js和date-fns等替代方案，但发现它们要么太大，要么在解析中不准确。Luxon缺乏tree-shaking进一步复杂化了大小优化。

核心问题在于ISO 8601的模糊性和灵活性，Luxon完全支持它。为了降低复杂性并为未来的Temporal API做准备，Eleventy采用了一种更严格的、符合RFC 9557的解析方法。这涉及到破坏性更改，放弃了对某些ISO 8601子格式的支持。

最终成果是`@11ty/parse-date-strings`，一个小型、基于ESM的库，专门专注于RFC 9557解析。它显著减小了Eleventy的捆绑包大小，并为其原生Temporal支持做好了准备。本文承认自定义日期解析的风险，但根据Eleventy的特定需求以及对更小、更准确的库的渴望，证明了其合理性。作者还列出了其他可供考虑的替代日期库和Temporal polyfill。

---

## 25. 为什么麻省理工学院从Scheme切换到Python (2009)

**原文标题**: Why MIT switched from Scheme to Python (2009)

**原文链接**: [https://www.wisdomandwonder.com/link/2110/why-mit-switched-from-scheme-to-python](https://www.wisdomandwonder.com/link/2110/why-mit-switched-from-scheme-to-python)

2009年，Hal Abelson和Gerald Jay Sussman（SICP的作者）讨论了麻省理工学院为何将其入门编程课程6.001从Scheme切换到Python。这一转变并非因为Scheme的缺陷，而是由于编程本质的转变。

Sussman解释说，在1980年，编程涉及编写精简、易懂、接近硬件的代码。工程师们精心设计他们完全理解的组件，并以可预测的方式组合它们。6.001旨在教授这种有条不紊的、基于组件的方法。

然而，现代编程通常涉及浏览来自未知来源的复杂、文档不完善的库。程序员必须试验和逆向工程这些库，才能理解它们的行为。这种新的现实需要一种不同的入门编程方法。

改版后的6.001以机器人为中心，要求学生编写机器人程序。与过去理想化的组件不同，机器人本质上是不可预测的，存在车轮打滑和环境变化等问题。学生现在专注于构建鲁棒性并适应现实世界的不确定性。

选择Python更多的是出于实用性，而不是语言的优越性。Python很可能有一个与机器人硬件连接的现有库，这使其成为以机器人为中心的课程的便捷选择。

---

## 26. Tailwind Plus 的原生 JavaScript 支持

**原文标题**: Vanilla JavaScript support for Tailwind Plus

**原文链接**: [https://tailwindcss.com/blog/vanilla-js-support-for-tailwind-plus](https://tailwindcss.com/blog/vanilla-js-support-for-tailwind-plus)

Tailwind Plus 现通过 `@tailwindplus/elements` 为其 UI 模块提供完整的 Vanilla JavaScript 支持，这是一个无头自定义元素库。这消除了使用 React 或 Vue 等 JavaScript 框架来使对话框、下拉菜单和命令面板等交互式 UI 元素具有功能性和可访问性的需求。

`@tailwindplus/elements` 使用标准 HTML 和 CSS，允许开发者在任何带有 `<script>` 标签的项目中使用这些 UI 模块。该库利用现代 Web 平台特性，如自定义元素、popover 属性、原生 `<dialog>` 元素、调用器命令和 ElementInternals，以提供强大的功能，同时保持轻量级。其中包含 Polyfill，以确保与 Tailwind CSS v4.0 支持的浏览器兼容。

最初的版本包括 Autocomplete、Command palette、Dialog、Disclosure、Dropdown menu、Popover、Select 和 Tabs 的基本组件。这些组件可在 Svelte、Rails 甚至 React 等框架中使用，使开发者能够在不同的环境中使用 Tailwind Plus UI 模块，而不受特定框架的限制。这允许在不同项目中实现更大的灵活性和代码重用。

---

## 27. 未来并非自托管

**原文标题**: The future is not self-hosted

**原文链接**: [https://www.drewlyton.com/story/the-future-is-not-self-hosted/](https://www.drewlyton.com/story/the-future-is-not-self-hosted/)

德鲁认为，自托管虽然看似赋权，但并非互联网自由的未来。他讲述了在亚马逊的 DRM 更改后，如何构建自己的家庭服务器来替代 Google Photos 和 Kindle 等云服务。虽然他享受这个过程并获得了更多对其数据的控制权，但他意识到自托管在技术上对大多数人来说是不可及的、不可持续的，并且提倡一种孤立的、个人主义的互联网。

他认为，核心问题在于自托管需要重复的基础设施，并使资源共享变得困难，从而创建了数字“郊区”。德鲁提倡社区托管的、公共资助的云服务，而不是个人的数字封地。他设想了一种系统，通过图书馆或非营利组织，以成本价提供基本的存储、共享和流媒体服务，并提供端到端加密和标准化协议，以便轻松进行数据迁移。这将迫使市场提供的选项更具竞争力和用户友好性。

德鲁承认对政府监督的担忧，但他认为端到端加密可以解决这些问题。他总结说，真正的自由需要通过团结和共享的、社区拥有的互联网基础设施来瓦解当前的科技封建体系，从而超越自力更生和个人主义的局限性。

---

## 28. 高效计算机Electron E1 CPU – 效率是Arm的100倍？

**原文标题**: Efficient Computer's Electron E1 CPU – 100x more efficient than Arm?

**原文链接**: [https://morethanmoore.substack.com/p/efficient-computers-electron-e1-cpu](https://morethanmoore.substack.com/p/efficient-computers-electron-e1-cpu)

无法访问文章链接。

---

## 29. C 语言中的泛型容器：Vec

**原文标题**: Generic Containers in C: Vec

**原文链接**: [https://uecker.codeberg.page/2025-07-20.html](https://uecker.codeberg.page/2025-07-20.html)

本文讨论了C语言中类型和边界安全的泛型向量（可变大小数组）的实现。作者Martin Uecker在前面对 span 类型和边界检查的讨论基础上进行了构建。向量实现的核心依赖于宏 `vec(T)`，该宏定义了一个包含大小字段 (`N`) 和柔性数组成员 (`data`) 的结构体。

文章重点介绍了 `vec_push` 宏，它使用 `realloc` 在添加元素时动态调整向量的大小。通过在内存分配失败时使用 `abort()` 简化了错误处理，但作者承认在某些情况下需要更健壮的错误处理。提到了使用 `ssize_t` 以检测潜在的溢出。

为了简单起见，作者特意省略了容量字段，依赖于 `realloc` 的内部优化。但是，对于性能关键的场景，探索了替代接口（`vec_push_cap`、`vec_pop_cap`、`vec_fit`、`vec_push_auto`、`vec_pop_auto`）。这些接口涉及外部容量整数或自动容量管理（向上舍入到下一个 2 的幂）。

通过 `vec2array` 宏实现边界安全，该宏允许将向量的数据视为固定大小的数组，从而可以使用传统的 C 数组进行互操作，并使用诸如 `array_slice` 之类的宏进行边界安全操作。该示例演示了将 `vec2array` 与 `array_sum` 结合使用来计算向量中元素的总和，展示了边界安全处理。还提到了未定义行为清理器未完全检查 `array_sum` 调用中参数匹配的剩余问题。最后，提供了一个包含这些想法的实验性库的链接。

---

## 30. 动画光标

**原文标题**: Animated Cursors

**原文链接**: [https://tattoy.sh/news/animated-cursors/](https://tattoy.sh/news/animated-cursors/)

Tattoy 增加动画光标支持

本文宣布终端应用 Tattoy 增加了动画光标支持。它利用 Ghostty 光标格式并使用自定义着色器进行渲染。与使用实际像素的 Ghostty 不同，Tattoy 使用基于 UTF8 文本的“像素”（“▀”和“▄”）渲染光标，从而产生像素化效果。

由于 Tattoy 现有的基于着色器的框架，实现此功能最初相对较快，但解决细节问题，特别是抗锯齿边缘的透明度，花费了更长时间。一个主要的挑战是复制 Ghostty 采样底层终端像素以实现平滑混合的能力，因为 Tattoy 纯粹基于文本。

解决方案是创建终端的“像素化”版本，通过使用文本的真彩色值并将其用作背景。这引入了一个新问题：像素化终端被包含在光标图像中。通过添加一个后处理步骤来解决这个问题，该步骤将像素化终端与渲染的光标进行比较，并且仅向用户渲染差异。

虽然当前的实现效果良好，但在较大的终端上可能会出现延迟。作者建议了潜在的性能改进，包括 Tattoy 处理所有光标渲染（而不是与主机终端联合渲染），从而可能减少延迟。作者欢迎对新功能的反馈。

---

## 31. 我为什么编程

**原文标题**: Why I do programming

**原文链接**: [https://esafev.com/notes/why-i-do-programming/](https://esafev.com/notes/why-i-do-programming/)

本文是作者对与编程的毕生关系的个人反思，灵感来自 Aaron Boodman 的一篇文章。 从小拆解机器就激发了好奇心和了解事物运作方式的渴望。 这逐渐演变为用 BASIC 编写简单的程序，用早期的 HTML 构建网站，并用 PAWN 修改 GTA。 然后，作者探索了 Second Life，创建虚拟物品，甚至赚取了真钱。

出于在现实世界中创造有意义事物的愿望，作者开始了一项小型在线业务，展示了创业的动力和足智多谋。 接触 HTML5 和 Bret Victor 的“Inventing on Principle”进一步塑造了他们对编程作为一种创造性努力的看法。

大学经历，包括对大学 SMTP 服务器的“黑客”行为，强化了实践技能和哲学思考。 毕业后，在一家初创公司的工作经历教会了他们关于商业、营销和团队合作重要性的宝贵经验。

作者承认经历过倦怠，并认识到休息以重新发现编程乐趣的重要性。 文章总结说，编程不仅仅是一份工作； 它是一种探索、修补和满足跨各种领域（从前端到人工智能）的好奇心的方式。 该领域的不断发展使其保持吸引力，尽管保持专注可能具有挑战性。 最终，编程被认为是作者与世界互动和理解世界的自然方式。

---

## 32. 什么是X-Forwarded-For？何时可以信任它？(2024)

**原文标题**: What is X-Forwarded-For and when can you trust it? (2024)

**原文链接**: [https://httptoolkit.com/blog/what-is-x-forwarded-for/](https://httptoolkit.com/blog/what-is-x-forwarded-for/)

X-Forwarded-For (XFF) HTTP 头部提供了一个客户端 IP 地址列表，该列表随着请求遍历代理和负载均衡器而生成。它帮助服务器识别原始客户端 IP，这对于用户身份验证、负载均衡、地理内容分发、安全和分析至关重要。

然而，XFF 头部很容易被伪造。因此，永远不应盲目信任 XFF 头部。您可以通过使用可信的反向代理（如 CDN 或 API 网关）并限制对后端服务器的直接访问来提高信任度。使用可信代理，您可以替换或附加到 XFF 头部。

确定真实客户端 IP 涉及从右到左分析列表，识别第一个*不是*您内部服务器的 IP 地址，并确保您的服务器无法直接访问。您可以通过维护受信任的 IP 范围列表，或依靠可信代理的数量来实现这一点。

解析 XFF 头部时，必须验证 IP 地址，以防止崩溃和潜在的 DDoS 攻击。本文还强调，即使您拥有可信的代理，也必须进行仔细验证，盲目信任该头部可能会导致安全漏洞。

---

## 33. 人工智能驱动手术机器人实施的实验性手术

**原文标题**: Experimental surgery performed by AI-driven surgical robot

**原文链接**: [https://arstechnica.com/science/2025/07/experimental-surgery-performed-by-ai-driven-surgical-robot/](https://arstechnica.com/science/2025/07/experimental-surgery-performed-by-ai-driven-surgical-robot/)

本文探讨了SRT-H（手术机器人Transformer）的开发，这是一种由约翰·霍普金斯大学研究人员创建、现位于斯坦福大学的人工智能驱动手术机器人。与以往依赖预编程动作的手术机器人不同，SRT-H 使用 Transformer 模型（类似于驱动 ChatGPT 的模型），从演示中学习并自主执行复杂的手术。

该机器人接受了超过 17 小时的视频、运动学数据以及经验丰富的外科医生在猪尸体上进行胆囊切除术的自然语言注释的训练。SRT-H 在新样本上实现了 100% 的成功率，甚至可以响应自然语言反馈。

虽然 SRT-H 展示了手术机器人技术的重大进步，包括灵活性和适应性，但其进展受到无法访问达芬奇机器人（行业标准）运动学数据的限制。达芬奇机器人的制造商直觉外科公司出于对竞争对手逆向工程其技术的担忧，限制对此数据的访问。为了规避这一点，研究人员正在探索收集运动学数据的替代方法，例如在手动手术工具上安装运动追踪传感器。未来的愿景是将人工智能与人形机器人相结合，以实现更加通用的手术应用。

---

## 34. Steam和Itch.io下架“色情”游戏，评论家称此为危险的开端。

**原文标题**: Steam, Itch.io are pulling ‘porn’ games. Critics say it's a slippery slope

**原文链接**: [https://www.wired.com/story/steam-itchio-are-pulling-porn-games-censorship/](https://www.wired.com/story/steam-itchio-are-pulling-porn-games-censorship/)

由于团体 Collective Shout 的倡议，Itch.io 和 Steam 正面临移除成人内容的压力，该团体认为某些游戏宣扬针对女性的暴力。Itch.io 已经从搜索结果中取消了所有成人 NSFW 游戏的索引，而 Steam 已经移除了数百款据称包含虐待、强奸或乱伦内容的游戏。

这些行动是 Collective Shout 游说万事达卡和维萨卡等支付处理商停止与这些平台合作的直接结果，这种策略被称为金融审查。这些平台担心失去支付处理能力，这将严重削弱它们的运营能力。

批评人士认为，这是一种由反色情和反 LGBTQ 群体驱动的审查形式，影响到弱势创作者，尤其是酷儿、女性和有色人种。处理心理健康、家庭虐待和 LGBTQ+ 主题的获奖游戏也受到了影响，即使它们不包含明确的性内容。

开发者担心将内容审核权交给响应道德压力的支付处理商所带来的先例。人们越来越担心保守派会将任何他们不喜欢的內容贴上色情标签，以控制社会，最终扼杀不同的声音并限制表达自由。

---

## 35. 发展我们对人工智能的立场

**原文标题**: Developing our position on AI

**原文链接**: [https://www.recurse.com/blog/191-developing-our-position-on-ai](https://www.recurse.com/blog/191-developing-our-position-on-ai)

本文探讨了Recurse Center (RC) 理解和整合人工智能（特别是大型语言模型LLM）的方法，并将此应用于其编程训练营和招聘业务。RC关注LLM对其“Recursers”个人和职业的影响，避免更广泛的社会辩论。

他们组建了一个非正式的AI顾问小组，成员是RC校友，他们在AI领域拥有不同的背景和观点，以获取见解。一个关键发现是，对于LLM目前在编程中的实用性，存在广泛的观点差异，这归因于LLM的使用经验、编程工作类型和项目规模。

关于学习，校友们看到了机遇和陷阱。许多人建议将“交付模式”（使用LLM）与“学习模式”（避免使用LLM以获得更深入的理解）分开。LLM被认为可能作为导师或用于在新领域进行引导，但它们在学习第一门编程语言中的作用仍然存在疑问。

本文还强调了LLM的社会影响，例如促进结对编程，但也可能阻碍RC社区内的互动。

重要的是，许多校友已经改变了他们对AI的看法，并预计还会再次改变，这强调了保持开放心态的重要性。无论是否使用AI，校友们始终强调需要理解正在构建的底层系统，并批判性地参与代码。做出独立判断和“说不”的能力被视为一项关键技能。自主意志至关重要。

---

## 36. 二氧化碳电池

**原文标题**: CO2 Battery

**原文链接**: [https://energydome.com/co2-battery/](https://energydome.com/co2-battery/)

Energy Dome的CO2电池为长时储能提供了一种经济高效的解决方案。它采用封闭式热机械循环，通过在气态和液态之间转换二氧化碳来运行。该过程包括加热、蒸发和膨胀二氧化碳以驱动涡轮机并产生电力，且二氧化碳零排放。

主要优势包括：往返效率高（75%以上），30年以上无衰减；全球部署能力；成本效益；以及使用易于获取的环保材料（水、钢和二氧化碳），避免依赖锂等稀有金属。该系统储能时长为8-24小时。

CO2电池被认为是锂离子电池的更好替代品，因为它具有更长的使用寿命、更低的资本支出、100%的放电深度以及全球化的组件供应。它集成了标准的工业组件，采用模块化和可扩展的设计，使其成为一种即插即用的解决方案，可在全球范围内部署。

该电池提供多种服务，包括时间转移、物理惯性、频率抑制储备（FCR）、自动和手动频率恢复储备（aFRR/mFRR）以及电压调节，从而支持电网稳定性。Energy Dome最近与谷歌合作，并在墨尔本设立了新的亚太总部，扩大了业务。

---

## 37. 游戏中的车辆编程

**原文标题**: Programming vehicles in games

**原文链接**: [https://wassimulator.com/blog/programming/programming_vehicles_in_games.html](https://wassimulator.com/blog/programming/programming_vehicles_in_games.html)

本文旨在提供游戏载具编程的基础理解，强调逼真物理效果与理想玩家体验之间的关键平衡。文章详述了作者从最初级的“凑合”载具模拟到更深入了解实际车辆动力学的过程。

文章的核心是将载具模拟分解为三个相互关联的部分：引擎（和变速箱）、车轮和轮胎，以及底盘。引擎被视为扭矩计算器，利用定制的方程式来模拟逼真且可调的扭矩曲线。变速箱是一个简单的查找表，根据档位选择修改扭矩和转速。车轮和轮胎侧重于通过摩擦力产生力的物理原理，以及基于扭矩、制动、转向和重量等输入的轮胎模型。底盘响应来自轮胎和外部因素的力，影响重量分配。

作者强调，对于大多数游戏来说，完美的模拟是不切实际且不必要的。开发者应专注于通过策略性地模拟、伪造和欺骗载具物理的各个方面来创造可信且愉悦的体验。文章提供了一个包含每个车辆组件的物理循环的基本算法伪代码。

---

## 38. 女性约会安全应用“Tea”遭泄露，用户ID被发布至4chan

**原文标题**: Women dating safety app 'Tea' breached, users' IDs posted to 4chan

**原文链接**: [https://www.404media.co/women-dating-safety-app-tea-breached-users-ids-posted-to-4chan/](https://www.404media.co/women-dating-safety-app-tea-breached-users-ids-posted-to-4chan/)

Tea，一款拥有超过160万用户的女性约会安全应用，遭遇数据泄露。4chan用户声称在谷歌的Firebase平台上发现了一个暴露的数据库，其中包含用户上传到该应用的个人数据和自拍。根据4chan帖子、截图以及404 Media审查的代码，用户正在访问并将这些数据发布到网上。据称泄露的信息包括驾驶执照和面部识别数据。Tea向404 Media证实了此次泄露事件，称其影响了一些私信，并且数据是两年前的。该应用旨在帮助女性分享关于男性的信息以确保安全，通过要求上传自拍来验证用户，而这些自拍现在可能已经暴露。4chan帖子强调了缺乏身份验证，称其为“公共数据桶”。

---

## 39. 展示 HN: 苹果健康 MCP 服务器

**原文标题**: Show HN: Apple Health MCP Server

**原文链接**: [https://github.com/neiltron/apple-health-mcp](https://github.com/neiltron/apple-health-mcp)

这个“Show HN”帖子介绍了一个由 neiltron 构建的 Apple Health MCP (模型上下文协议) 服务器，该服务器允许用户使用 SQL 查询和分析他们的 Apple Health 数据。该服务器利用 DuckDB 实现高效的数据处理。

**主要特性：**

*   **SQL 查询：** 用户可以直接对他们的 Apple Health 数据执行 SQL 查询。
*   **自然语言查询：** 通过 MCP 客户端（例如，Claude Desktop）支持自然语言查询。
*   **自动报告：** 生成每周/每月健康摘要。
*   **高效数据加载：** 利用惰性加载和可配置的时间窗口。
*   **智能缓存：** 使用 TTL 缓存查询结果，以便更快地进行后续查询。

**安装和使用：**

该服务器无需安装。它通过 `npx` 和 MCP 客户端（如 Claude Desktop）使用，只需使用健康数据目录的路径（`HEALTH_DATA_DIR`）配置 `claude_desktop_config.json` 文件。

**数据来源：**

该服务器依赖于 "Simple Health Export CSV" iOS 应用程序将 Apple Health 数据导出为 CSV 文件。 用户需要将导出的数据传输到他们的计算机，解压缩，并将 `HEALTH_DATA_DIR` 环境变量指向该目录。

**数据结构：**

该服务器期望 CSV 文件根据 Apple Health 指标类型命名（例如，`HKQuantityTypeIdentifier*.csv`）。每个 CSV 文件应具有 `type`、`sourceName`、`startDate`、`endDate`、`value` 和 `unit` 列。

**可用工具：**

*   `health_schema`: 提供有关可用表及其结构的信息。
*   `health_query`: 执行 SQL 查询。
*   `health_report`: 生成健康报告。

**开发：**

该帖子提供了本地开发的说明，包括克隆存储库、安装依赖项、构建项目和类型检查。

**贡献：**

该项目欢迎贡献，强调代码风格、TypeScript 类型、错误处理和性能。

---

## 40. 英国新的年龄验证规则很容易被绕过

**原文标题**: The UK’s new age-gating rules are easy to bypass

**原文链接**: [https://www.theverge.com/analysis/713773/uk-online-safety-act-age-verification-bypass-vpn](https://www.theverge.com/analysis/713773/uk-online-safety-act-age-verification-bypass-vpn)

本文讨论了英国针对在线平台的新年龄验证规则的无效性。这些规则旨在遵守在线安全法规，要求平台阻止儿童访问有害内容，但通过使用VPN可以轻松绕过。

许多平台，如Reddit和Bluesky，都基于IP地址验证年龄。通过使用VPN伪装成位于英国境外，用户可以完全避免年龄验证。尽管英国通信管理局（Ofcom）要求“强大”且“高效”的年龄验证方法，但他们并未明确具体方式。目前的方法包括上传银行卡信息、政府颁发的身份证件或用于年龄估算的自拍照。

本文认为自拍验证可能被欺骗，并证实VPN完全可以规避这些检查。作者指出自己年轻时使用VPN绕过防火墙的经历，表明青少年有能力找到这种变通方法。其他绕过方法包括使用带有自定义过滤器的广告拦截器以及尚未实施年龄验证的第三方应用程序。

文章最后指出，英国对“VPN”的Google搜索量激增，表明人们对这一漏洞的认识正在提高。

---

## 41. 联合太平洋-诺福克南方合并将重塑铁路版图

**原文标题**: A Union Pacific-Norfolk Southern combination would redraw the railroad map

**原文链接**: [https://www.trains.com/trn/news-reviews/news-wire/a-union-pacific-norfolk-southern-combination-would-redraw-the-railroad-map/](https://www.trains.com/trn/news-reviews/news-wire/a-union-pacific-norfolk-southern-combination-would-redraw-the-railroad-map/)

文章探讨了联合太平洋铁路公司（UP）和诺福克南方铁路公司（NS）之间潜在的合并谈判，旨在创建美国第一条横贯大陆的铁路，一个长达52215英里的系统。此次合并有望简化从东海岸到西海岸的运输服务，绕过拥堵的转运点。

联合太平洋铁路公司首席执行官吉姆·维纳认为，在技术快速变革的时代，这样的合并对于保持竞争力至关重要，并将通过将货物从公路转移到铁路，从而惠及经济。合并后的系统将产生可观的收入，处理大量的货物运输，并雇用大量的劳动力。

合并后的公司将利用联合太平洋铁路公司强大的整车运输网络，特别是其通往墨西哥湾沿岸石化工厂的通道，以及诺福克南方铁路公司在东部强大的多式联运网络，从而提供更优质的配送中心通道。该交易可能会对西方BNSF和东方NS的主要多式联运合作伙伴J.B.亨特产生重大影响，可能迫使他们在这两者之间做出选择。汽车运输网络也将受益。

潜在的运营变更包括将交通流量从芝加哥和新奥尔良转移，可能有利于堪萨斯城、孟菲斯和什里夫波特。虽然大宗货物运输网络可能基本保持不变，但在密苏里州和伊利诺伊州的部分路线上存在一些重叠。

此次合并面临美国地面运输委员会（STB）2001年合并审查规则的监管障碍，该规则要求证明“增强竞争”并服务于“公共利益”。美国地面运输委员会的规则还可能导致需要做出让步或附加条件，例如互惠铁路调车。

文章还探讨了此次合并可能引发业内进一步整合的可能性，可能涉及BNSF和CSX。虽然CSX专注于自身增长，但BNSF目前认为没有对横贯大陆合并的需求。

---

## 42. Claude Code 推出专用子代理

**原文标题**: Claude Code introduces specialized sub-agents

**原文链接**: [https://docs.anthropic.com/en/docs/claude-code/sub-agents](https://docs.anthropic.com/en/docs/claude-code/sub-agents)

本文介绍了Claude Code中的“子代理”，它们是专门设计的AI助手，旨在更高效地处理特定任务。子代理拥有自己的上下文窗口、系统提示，并且可以配置特定的工具，从而实现更专注的问题解决。

主要优势包括上下文保持、专业知识、跨项目可重用性以及灵活的权限，允许为特定的子代理类型限制工具访问。

用户可以通过`/agents`命令或直接在`.claude/agents/`(项目级)或`~/.claude/agents/`(用户级)中创建带有YAML frontmatter的Markdown文件来创建子代理。配置文件定义了子代理的名称、描述和可访问的工具。如果省略工具，子代理将继承主线程中的所有工具。

子代理可以被显式调用（例如，“使用代码审查员子代理……”）或根据请求和子代理的描述自动委派任务。示例子代理包括代码审查员、调试器和数据科学家，每个都预先配置了各自的角色。

最佳实践包括从Claude生成的代理开始，设计具有单一职责的专注代理，编写详细的提示，限制工具访问以及使用版本控制。本文还讨论了高级用法，例如链接子代理以及性能考虑因素，例如上下文效率和延迟。

---

## 43. 风帆公司员工#2：我的股票分红只有价值的1%。

**原文标题**: Windsurf employee #2: I was given a payout of only 1% what my shares where worth

**原文链接**: [https://twitter.com/premqnair/status/1948420769945682413](https://twitter.com/premqnair/status/1948420769945682413)

页面显示Twitter/X消息，提示用户浏览器禁用了JavaScript，导致无法访问题为“Windsurf公司员工#2：我的股份清算金仅为应有价值的1%”的推文内容。

因此，在无法访问文章主体的情况下，无法提供文章摘要。现有信息表明，一家名为“Windsurf”公司的前员工（被标识为员工#2）声称其股份获得的清算金远低于其认为应有的价值（仅为1%）。

总结来说，提供的信息指向：

*   一位前“Windsurf”公司员工的声明。
*   该员工声称其公司股份在清算时被严重低估。
*   该员工表示清算金仅为股份预期价值的1%。

关于该员工情况的更多细节、清算金低的原因以及公司的回应均未知，且在没有原文全文内容的情况下无法获得。

---

## 44. 研究人员重视零结果，但难以发表。

**原文标题**: Researchers value null results, but struggle to publish them

**原文链接**: [https://www.nature.com/articles/d41586-025-02312-4](https://www.nature.com/articles/d41586-025-02312-4)

一项调查报告显示，研究人员对零结果价值的看法与其发表意愿之间存在脱节。在来自166个国家的11069名受访研究人员中，98%的人承认分享零结果（未证实假设的结果）的重要性，但只有30%的产生零结果的研究人员试图在期刊上发表。

Springer Nature进行的这项调查发现，研究人员通常避免发表零结果，原因是担心它们不会被接受、缺乏对合适期刊的了解、资金问题以及害怕负面的同行评价。Springer Nature的Ritu Dhand解释说，研究人员接受的培训是撰写积极进展，而零结果很少被引用。

英国可重复性网络（UK Reproducibility Network）的Marcus Munafò强调，大多数科学研究和实验都会产生零结果，而发表这些结果对于更准确地呈现研究图景至关重要。成功发表零结果的受访者报告了诸如激发新方法（39%）和防止不必要的研究重复（28%）等好处。一位匿名研究人员感叹缺乏对零结果的广泛传播，这本可以节省他们多年的研究。该文章倡导提高意识并改变研究评估方式，以鼓励发表零结果。

---

## 45. 史蒂夫·乔布斯的内阁

**原文标题**: Steve Jobs' cabinet

**原文链接**: [https://perfectdays23.substack.com/p/steve-jobs-cabinet](https://perfectdays23.substack.com/p/steve-jobs-cabinet)

无法访问文章链接。

---

## 46. 谁拥有最快的F1网站(2021)

**原文标题**: Who has the fastest F1 website (2021)

**原文链接**: [https://jakearchibald.com/2021/f1-perf-part-3/](https://jakearchibald.com/2021/f1-perf-part-3/)

本文是系列文章的第三部分，分析了红牛车队本田F1网站的加载性能。作者赞扬了该网站引人入胜的设计，以及相比2019年版本的速度提升，但同时也指出了几个需要优化的地方。

主要问题包括：

*   **不必要的内联：** 网站内联了大量CSS（超过600kB），其中大部分在初始页面加载时未使用，导致3秒延迟。作者建议定制内联代码，仅包含初始渲染所需的内容。
*   **过大的主图像：** 主图像虽然使用了高效的WebP格式，但质量设置过高，没有必要。
*   **过大的叠加图像：** 一个增强设计的叠加图像也是一个很大的WebP文件。作者建议使用AVIF，这种格式对于此类图像的无损透明通道编码效果更好。
*   **叠加图像通过JavaScript加载：** 叠加图像通过JavaScript加载，导致加载延迟超过50秒。作者建议使用标准的`<img>`标签，以利用响应式图像并提前加载。
*   **过大的内联模糊图像：** 网站在主图像加载时使用模糊、低质量的图像作为占位符，但其大小超过了必要。作者探讨了使用更小的尺寸和替代格式来优化此预览图像。

通过解决这些问题，作者估计红牛网站的加载时间可以进一步缩短，从而改善用户体验。文章最后给出了一个记分牌，显示与之前分析过的Alpha Tauri和Alfa Romeo网站相比，红牛处于领先地位。

---

## 47. 如果人工智能让世界经济增长爆发会怎样？

**原文标题**: What if AI made the world’s economic growth explode?

**原文链接**: [https://www.economist.com/briefing/2025/07/24/what-if-ai-made-the-worlds-economic-growth-explode](https://www.economist.com/briefing/2025/07/24/what-if-ai-made-the-worlds-economic-growth-explode)

如果人工智能引爆世界经济增长会怎样？

本文探讨了人工智能对全球经济增长的潜在影响。文章首先指出工业革命前世界经济的停滞，增长几乎可以忽略不计。工业革命引发了增长率的显著加速，最终在20世纪达到平均2.8%。

文章随后暗示，人工智能可能是一种类似的变革力量，可能导致经济增长的“爆炸”。文章假设，如果人工智能显著提高生产力和创新，商品、服务、金融资产和劳动力市场将发生根本性变化，颠覆当前的经济规范。

文章还链接到相关内容，包括人工智能实验室之间竞争激烈背景下的人工智能安全问题，以及癌症预防进展的潜在经济影响。文章还涉及全球庇护制度、美国政治动态以及乌克兰战争对西方工业能力的影响等议题。 本质上，文章利用历史上的经济转变来构建人工智能对未来的潜在影响，以及可能造成的颠覆。

---

## 48. 量化人工智能进展需要准确透明的评估

**原文标题**: Quantitative AI progress needs accurate and transparent evaluation

**原文链接**: [https://mathstodon.xyz/@tao/114910028356641733](https://mathstodon.xyz/@tao/114910028356641733)

量化AI进展需要准确且透明的评估

这篇题为《量化AI进展需要准确且透明的评估》的短文，引用了陶哲轩在Mathstodon上的引言（“随着一项技术成熟，焦点往往会转移……”）来强调在人工智能发展中稳健且清晰的评估的重要性。尽管内容极其简短，但核心信息暗示，随着人工智能的进步，重点应该转向：

*   **量化测量：**人工智能的进展应使用可量化的指标进行评估，从而可以对改进进行客观的比较和跟踪。
*   **准确性：**这些测量必须准确可靠，能够真实地反映人工智能的能力。
*   **透明度：**评估过程和结果应该是透明的，从而能够对人工智能的优势和劣势进行审查、重现和理解。

这段引言表明，重点应该从单纯追求新颖或展示潜力，转向一种更严格和可衡量的方法，这种方法侧重于可靠性、可验证性以及理解人工智能系统的实际性能。访问Mathstodon上完整上下文需要JavaScript，表明上下文可能涉及对人工智能研究中不断变化的优先事项的更广泛讨论。

---

## 49. 互联网档案馆现为联邦政府资料库图书馆。

**原文标题**: Internet Archive is now a federal depository library

**原文链接**: [https://www.kqed.org/news/12049420/sf-based-internet-archive-is-now-a-federal-depository-library-what-does-that-mean](https://www.kqed.org/news/12049420/sf-based-internet-archive-is-now-a-federal-depository-library-what-does-that-mean)

互联网档案馆被加州参议员亚历克斯·帕迪利亚指定为联邦文献存储图书馆，加入了一个由1100多家图书馆组成的网络，这些图书馆负责存档并向公众提供政府文件。帕迪利亚赞扬了互联网档案馆的“数字化重点”及其在数字时代扩大政府出版物获取途径方面的作用。

创始人布鲁斯特·卡勒表示，这一指定将促进与其他联邦文献存储图书馆的合作，通过将政府材料整合到维基百科等平台中，从而加强互联网生态系统。 联邦文献存储图书馆计划成立于1813年，旨在确保公众可以获取政府记录。

互联网档案馆的参与是对其现有工作的自然延伸，包括“民主图书馆”，这是一个政府研究和出版物的在线汇编。

然而，互联网档案馆正面临持续的法律挑战。来自主要出版商和音乐公司的诉讼挑战了其存档实践，并可能导致巨额经济处罚。这些诉讼质疑互联网档案馆作为图书馆的地位及其数字借阅行为，反对者认为它是一个“未经许可的数字版权和发行业务”。包括图书馆员和作家在内的支持者则辩护称，它是一个至关重要的现代文化机构。

卡勒澄清说，这一指定不会改变该组织的运作方式，并强调政府出版物不受版权保护，可以自由数字化和分发。互联网档案馆将继续其保存和提供知识的使命，包括通过时光机器存档网页。

---

## 50. 航 空 里 程 经 济 学

**原文标题**: The Economics of Airline Miles

**原文链接**: [https://reason.com/2025/07/26/qatar-airways-al-safwa-first-class-lounge-doha-qatar/](https://reason.com/2025/07/26/qatar-airways-al-safwa-first-class-lounge-doha-qatar/)

本文探讨了航空里程的历史和经济学，认为它们是1978年航空业解除管制政策的直接结果。在解除管制前，政府控制机票价格，竞争有限。航空公司随后利用常旅客计划来建立品牌忠诚度。作者经常使用航空里程来获得优质旅行体验，他强调这些计划如何作为一种私人货币运作，受供需影响，并且容易贬值。

关键一点是，航空公司通过向第三方（特别是提供联名信用卡的银行）出售里程来产生大量收入。这种收入模式甚至被用来获得贷款，突显了忠诚度计划的价值。然而，这些计划很脆弱，因为航空公司可以更改规则并使里程贬值，而消费者几乎没有追索权。

本文还讨论了参议员迪克·德宾试图监管信用卡“刷卡费”的举措，这可能会间接影响航空里程的价值。他认为，降低这些费用会将资金从银行和消费者重新分配给零售商。作者认为，虽然航空公司掌握了大部分牌，但消费者仍然从该系统中受益，特别是那些在赚取和兑换里程以获得优质旅行体验方面具有战略眼光的人。尽管存在贬值和监管审查的潜在风险，但航空里程已使旅行大众化，并使许多人能够以他们从未想过的方式体验世界。

---

## 51. Asciinema：录制并分享你的终端会话

**原文标题**: Asciinema: Record and share your terminal sessions

**原文链接**: [https://asciinema.org](https://asciinema.org)

Asciinema 是一款免费开源工具，用于录制和分享终端会话。与屏幕录像应用不同，Asciinema 采用基于文本的方式，创建轻量级录像，非常适合在网络上分享。

用户可以使用简单命令 "asciinema rec demo.cast" 开始录制，并使用 "ctrl+d" 或 "exit" 结束录制。Asciinema 具有诸多优势：用户可以轻松地从录像中复制粘贴文本，并且播放器可以嵌入到博客文章和文档等各种平台中。

该网站展示了各种示例录像，展示了 Asciinema 在不同环境中的实用性，从与命令行工具交互到可视化复杂的版本控制操作。这让用户能够探索 Asciinema 的功能和潜在应用。

---

## 52. Show HN: 令牌单价 – LLM API 定价数据

**原文标题**: Show HN: Price Per Token – LLM API Pricing Data

**原文链接**: [https://pricepertoken.com/](https://pricepertoken.com/)

此“Show HN”帖子介绍“单Token价格”，这是一个提供来自OpenAI、Anthropic和Google等主要LLM API提供商的最新定价信息的资源。该资源允许用户比较不同AI模型的每百万token的输入和输出成本，从而找到满足其特定需求的最具成本效益的选项。数据最后更新于2025年7月25日下午3:48。它指出，某些模型采用基于提示长度的分层定价，显示的定价适用于20万token或更少的提示。该帖子还强调了使用图表比较输入成本和输出成本的功能。该服务由@aellman构建，提供每周更新LLM定价变化和新模型发布的时事通讯。该资源总共涵盖了30多种不同的模型。

---

## 53. 通过 DKIM 重放攻击仿冒 Google：技术分析

**原文标题**: Google spoofed via DKIM replay attack: A technical breakdown

**原文链接**: [https://easydmarc.com/blog/google-spoofed-via-dkim-replay-attack-a-technical-breakdown/](https://easydmarc.com/blog/google-spoofed-via-dkim-replay-attack-a-technical-breakdown/)

文章《通过DKIM重放攻击欺骗谷歌：技术分析》讲述的是一份DMARC采纳报告《财富500强和Inc. 5000强企业DMARC采纳情况：日益扩大的差距》（发布于2025年7月25日）。正如标题所示，内容主要关注如何利用DKIM重放攻击欺骗谷歌邮件。这种攻击利用了与域名密钥识别邮件(DKIM)相关的漏洞，DKIM是一种旨在验证电子邮件发件人的安全标准。文章可能提供对此特定漏洞的技术分析，解释攻击者如何重放来自合法谷歌邮件的有效DKIM签名，以欺骗新的邮件，使其看起来来自谷歌。文章似乎还涉及DMARC（基于域的消息认证、报告和一致性）的采纳率，特别是财富500强和Inc. 5000强公司，并指出了在实施这一关键电子邮件身份验证协议方面的日益扩大的差距。本质上，文章可能认为，未能正确采用DMARC会为攻击者利用DKIM重放攻击创造机会，最终影响电子邮件通信的安全性和可信度，特别是对于大型组织而言。

---

## 54. 英国《网络安全法案》生效后，VPN注册量激增1400%

**原文标题**: VPN signups from UK surge 1400% after Online Safety Act goes into effect

**原文链接**: [https://twitter.com/ProtonVPN/status/1948773319148245334](https://twitter.com/ProtonVPN/status/1948773319148245334)

英国VPN注册量在《网络安全法案》实施后激增1400%，主要原因可能是担心该法案对在线隐私和言论自由的潜在影响。文章来源是X（前身为Twitter），内容展示非常基础，需要JavaScript才能查看完整文章。可见信息未提供更多细节，例如VPN注册数据的来源、推动VPN使用的具体原因，或对《网络安全法案》本身的评论。文章仅建立了法案实施与VPN使用量显著上升之间的关联。

---

## 55. 游戏画面糟糕：HDR与色调映射 (2017)

**原文标题**: Games Look Bad: HDR and Tone Mapping (2017)

**原文链接**: [https://ventspace.wordpress.com/2017/10/20/games-look-bad-part-1-hdr-and-tone-mapping/](https://ventspace.wordpress.com/2017/10/20/games-look-bad-part-1-hdr-and-tone-mapping/)

Promit的文章《游戏画面糟糕：HDR和色调映射》批判了视频游戏中高动态范围（HDR）和色调映射的使用，认为它们经常导致视觉上缺乏吸引力、充满“游戏感”的画面，而非电影般的真实感。

文章解释说，HDR和色调映射用于管理现实世界光照的巨大对比度，并将其压缩以便在屏幕上显示。然而，游戏开发者经常滥用这些工具，导致图像对比度过高、黑位溢出和高光溢出。作者指出，许多游戏使用相同的色调映射函数，导致不同游戏之间呈现出同质化的外观。

作者强调了专注于技术能力和专注于“高质量电影的感受和视觉吸引力”之间的区别，并以RED One相机和Arri Alexa为例。

作者还指出，将LUT（查找表）应用于糟糕的色调映射是无效的，并且当前游戏行业中的LUT创作方法不足。

文章赞扬了《塞尔达传说：旷野之息》的风格化、非HDR方法，并认为《生化危机7》、《杀出重围：人类分裂》（在特定场景中）和《极限竞速：地平线3》由于风格选择以及对中间色调和较低对比度的重视，相对较好地处理了HDR。

作者总结说，行业需要改进色调映射技术，并为艺术家提供更好的LUT创作工具。他们强调，色调映射应该是一个基本的美学选择，而不是事后的想法。最后指出，《侠盗猎车手5》是色调映射做得很好的一个例子。

---

## 56. Show HN: 我做了一个生物网络可视化工具

**原文标题**: Show HN: I built a biological network visualization tool

**原文链接**: [https://nodes.bio](https://nodes.bio)

Nodes.bio：加速科学发现的生物网络可视化工具。它使用户能够以交互方式映射、分析和共享复杂系统。主要功能包括可视化各种类型的网络（从生物途径到项目依赖关系），实时协作编辑，以及将网络导出和共享为 PNG 和 JSON 等各种格式的选项。

该工具旨在将手动绘制的网络转换为适合发布的交互式图表。临床遗传学家 Patrick Sewell 博士表示，Nodes.bio 使他能够快速创建使用其他工具不可能实现的高质量图表。

该工具鼓励用户尝试在线演示和/或预约通话。文章还表明，Nodes.bio 受到研究人员和创新者的信任，尽管提供的文本中未具体说明具体的机构或组织。

---

## 57. Dwl: Wayland 上的 Dwm

**原文标题**: Dwl: Dwm for Wayland

**原文链接**: [https://codeberg.org/dwl/dwl](https://codeberg.org/dwl/dwl)

无法访问文章链接。

---

## 58. 巴西央行将于九月推出 Pix 分期付款功能

**原文标题**: Brazil central bank to launch Pix installment feature in September

**原文链接**: [https://www.reuters.com/technology/brazil-central-bank-launch-pix-installment-feature-september-2025-04-03/](https://www.reuters.com/technology/brazil-central-bank-launch-pix-installment-feature-september-2025-04-03/)

**概要：**

据路透社报道，巴西中央银行计划于2024年9月为其即时支付系统Pix推出分期付款功能。这项名为“Pix Garantido”的新功能将允许用户通过Pix直接分期支付购物款项。Pix是巴西一种流行且被广泛使用的支付方式。

其主要目标是进一步增强Pix在巴西支付领域的效用和竞争力，尤其是在与传统信用卡竞争方面。通过提供分期付款选项，Pix旨在占领更大的零售市场份额，让消费者可以在一段时间内分摊购物成本，而无需完全依赖信用卡。

巴西央行认为，Pix Garantido将使消费者和商家受益。消费者将获得更大的财务管理灵活性，而商家可能会因支付方式的增强而看到销售额的增长。预计该新系统将于2024年9月全面投入运营。

---

## 59. Arm 桌面：x86 模拟

**原文标题**: Arm Desktop: x86 Emulation

**原文链接**: [https://marcin.juszkiewicz.com.pl/2025/07/22/arm-desktop-emulation/](https://marcin.juszkiewicz.com.pl/2025/07/22/arm-desktop-emulation/)

本文详细介绍了作者在基于Ampere Altra的Fedora AArch64 (Arm) 桌面系统上使用x86-64模拟的经验。主要使用的模拟方案是FEX-Emu，作者建议移除QEMU软件包以确保FEX-Emu是唯一的模拟器。

最初的Geekbench 6结果令人失望，性能仅达到旧款英特尔Atom CPU的水平。然而，作者强调了Arm CPU可能提高模拟速度的功能，如加密、TSO模拟、原子操作等，尽管Altra较旧的架构限制了这些功能的可用性。

通过降低FPU精度和禁用TSO来调整FEX-Emu配置提高了性能，尤其是在Factorio中。作者使用RPM和FEXBash成功安装了Steam。Factorio最初无法运行，但在配置调整后变得更具可玩性。

一个幽默的轶事说明了避免意外模拟的重要性：使用Ninja构建固件的速度明显降低，直到将x86-64 Ninja二进制文件替换为指向原生AArch64版本的符号链接。

作者总结说，虽然x86-64模拟是可行的，但其性能限制使其不适合日常使用。他们可能会尝试运行像火炬之光II这样的老游戏，但不期望大量依赖模拟。

---

## 60. 石墨烯操作系统：一个安全增强的安卓版本

**原文标题**: Graphene OS: a security-enhanced Android build

**原文链接**: [https://lwn.net/SubscriberLink/1030004/898017c7953c0946/](https://lwn.net/SubscriberLink/1030004/898017c7953c0946/)

这篇LWN.net文章评测了GrapheneOS，这是一款注重用户隐私和设备控制的增强安全型安卓系统。GrapheneOS脱胎于CopperheadOS，旨在通过移除代码和增加安全特性（如强化的malloc()库和控制流完整性）来加固安卓系统，抵御威胁。

文章强调GrapheneOS仅支持最新的谷歌Pixel设备（6-9），并通过硬件内存标记和更长的支持保障来优先考虑安全性。安装可以通过网页或命令行进行，网页方法更可靠。

GrapheneOS提供了一种纯净的体验，缺乏原生安卓的预装应用。它提供了自己的浏览器（Vanadium）、相机应用、PDF阅读器和应用商店。为了更广泛的应用可用性，它支持Accrescent、F-Droid，甚至还有一个沙盒化的Google Play商店。文章提到了安卓完整性API及其可能导致某些应用出现问题。

评测强调了安全特性，包括细粒度的应用权限控制（网络、传感器、存储、联系人）、带锁定的指纹解锁以及用于数据擦除的胁迫密码。系统频繁更新，并积极更新到最新的安卓版本。

文章指出，人们可能担心GrapheneOS开发社区的透明度以及对单个个人Daniel Micay的依赖。然而，作者总结认为，尽管可能需要集成像Google Play服务这样的专有软件，GrapheneOS仍然提供了更安全和私密的安卓体验。作者承诺将GrapheneOS作为他们的日常使用系统。

---

## 61. 无需定制ROM，在Android Termux proot上运行PostmarketOS (2024)

**原文标题**: Running PostmarketOS on Android Termux proot without a custom ROM (2024)

**原文链接**: [https://ivonblog.com/en-us/posts/postmarketos-in-termux-proot/](https://ivonblog.com/en-us/posts/postmarketos-in-termux-proot/)

本文详细介绍了一种使用Termux proot在Android手机上运行带有Phosh桌面环境的postmarketOS的方法，无需root或刷入自定义ROM。作者旨在探索Android上的移动Linux可能性，并利用Phosh的触摸屏优化界面。

该过程涉及通过Termux的proot-distro安装Alpine Linux，然后通过添加其存储库和更新软件包将其转换为postmarketOS。这样做是因为postmarketOS并非适用于所有Android手机，并且移植它很复杂。Termux提供了一种无需root访问权限即可运行Linux容器的便捷方式。

随后安装了轻量级且触摸屏友好的桌面环境Phosh。该指南概述了如何在Termux X11中使用Openbox和Cage启动Phosh，以在X11中启用嵌套的Wayland会话。

本文提供了设置先决条件（如Termux X11、virglrenderer（可选）和 Hacker's Keyboard）的说明。它还涵盖了配置Alpine Linux proot环境，包括切换到适当的Alpine版本（v3.20，对应于postmarketOS v24.06），添加用户，启用SSH，然后过渡到postmarketOS。

最后，作者简要探讨了其他桌面环境，如Plasma Mobile和SXMO，并指出了它们在此环境中的缺点。文章以参考文献和相关教程结尾。Phosh体验允许使用触摸手势，但指出它不是一个完整的Linux环境。

---

## 62. 让网络再次伟大

**原文标题**: Make the Web Great Again

**原文链接**: [https://koshka.love/mwwwga.html](https://koshka.love/mwwwga.html)

让网络再次伟大：文章认为现代网络已经从其最初的状态恶化，失去了曾经的魔力和奇迹。作者指出了“旧网络”中如今缺失的五个关键原则：

*   **匿名性：** 通过隐藏个人信息来鼓励思想精英制度，防止偏见。
*   **去中心化：** 反对垄断，倡导一个没有单一实体拥有过度控制权的网络。
*   **技术素养：** 认为一定的技术技能水平作为准入门槛是有益的，可以防止网络被最低共同标准所支配。
*   **非商业化：** 反对为利润而进行的激进商业化和算法操纵，以及空洞的“个人品牌”。
*   **言论自由：** 哀叹对多元化和可能冒犯性观点的容忍度下降，倡导一个真正自由和开放的全球媒介。

作者认为，这种衰落是由于日益增长的平庸化、智能手机的使用以及大型科技公司的统治造成的。 解决方案在于抵制这些公司，并支持 Neocities、Gab、Kolyma 和独立 Web 1.0 站点等替代平台。 作者重点介绍了 Wiby，这是一个专注于 Web 1.0 站点的搜索引擎。 通过拥抱这些替代方案，作者认为有可能恢复旧网络的价值和奇迹。

---

## 63. 铁杆丹词典：2025年6月30日 – 25周年纪念

**原文标题**: The Steely Dan Dictionary: 30th June 2025 – 25th anniversary

**原文链接**: [https://steelydandictionary.com](https://steelydandictionary.com)

这是为“铁娘子丹词典”发布的公告，这是一部A-Z词汇表，致力于解释铁娘子丹歌词中引用的晦涩词汇、人物和地点。该网站由Dan O'Malley创建，于2000年6月启动，旨在阐明Walter Becker和Donald Fagen在铁娘子丹歌曲中穿插的往往晦涩的文学和文化典故。

该词典主要关注真实人物和地点，刻意排除Becker和Fagen创造的虚构名称、物品和场所（如Hoops McCann或Steamer Heaven），因为无法对其进行定义。仅当创作者本人对诸如“Custerdome”之类的新词提供了明确定义时，才会做出例外。

该网站主要面向非美国受众，为美国境外的人可能不熟悉的地点和机构提供解释，例如“TJ”或“IHOP”。然而，即使是美国人也可能会发现了解更多全球认可的地点和鸡尾酒的价值。

为了纪念该网站于2025年6月30日迎来25周年，现已添加了八个新条目，这些条目取自非专辑和未发行的铁娘子丹歌曲。作者Dan O'Malley鼓励用户提供反馈、建议和更正，以进一步改进该词典。

---

## 64. 如何简单配置X11

**原文标题**: How to configure X11 in a simple way

**原文链接**: [https://eugene-andrienko.com/en/it/2025/07/24/x11-configuration-simple.html](https://eugene-andrienko.com/en/it/2025/07/24/x11-configuration-simple.html)

本文详细介绍了如何在 FreeBSD 中配置 X11 窗口系统，以获得现代桌面体验，而无需依赖像 Gnome 或 KDE 这样重量级的桌面环境。它侧重于使用简单、久经考验的程序和配置方法。

涵盖的关键主题包括：

*   **高 DPI：** 通过调整 X 服务器配置中活动区域的毫米尺寸，配置 X11 以在高清显示器上正确缩放 GUI 元素。
*   **键盘配置：** 使用 `setxkbmap` 和 `xmodmap` 设置键盘布局、切换方法（使用 Menu 键）、Compose 键功能和重映射键（CapsLock 到 Ctrl），并将这些设置转换为 `xorg.conf` 以进行系统范围的应用。
*   **多媒体键：** 利用内核模块来识别多媒体键的按下并将其绑定到窗口管理器中的操作。
*   **指点设备：** 配置触摸板（禁用它们）、指点杆（最小设置）和轨迹球（重新映射按钮并启用滚动模拟以供左手使用）。
*   **其他：** 提及的主题包括屏幕保护程序、合成器、窗口大小调整、主题（GTK2/3/4、Qt、Librewolf）、字体、图标、显示管理器（XDM）、`xdg-utils`，以及使用 Emacs 作为默认文件管理器、邮件代理、编辑器和 PDF 查看器。

作者优先考虑轻量级解决方案，通过禁用不需要的编译时选项、重新编译必要的程序和选择成熟的实用程序来避免臃肿。这些配置旨在实现系统范围内的外观和感觉一致，影响从登录屏幕到单个应用程序的所有内容。

---

## 65. SRAM 毫无防备：利用电源域隔离窃取片上机密

**原文标题**: SRAM Has No Chill: Exploiting Power Domain Separation to Steal On-Chip Secrets

**原文链接**: [https://cacm.acm.org/research-highlights/sram-has-no-chill-exploiting-power-domain-separation-to-steal-on-chip-secrets/](https://cacm.acm.org/research-highlights/sram-has-no-chill-exploiting-power-domain-separation-to-steal-on-chip-secrets/)

本文介绍了一种名为“Volt Boot”的新型攻击，该攻击利用现代SoC中的电源域分离机制，从片上SRAM恢复敏感数据，绕过传统的冷启动防御。标准的冷启动攻击依赖于低温来延长断电后内存中的数据保留时间，而Volt Boot则利用SoC内不同电源域之间的非对称电源状态，强制SRAM在电源周期内保持状态。这消除了对极端低温或固有保留时间的需求。

作者证明了由于片上SRAM的集成特性、短保留时间和极端温度要求，传统的冷启动攻击对其无效。相比之下，Volt Boot利用电源域架构，其中不同的SoC组件（核心、内存、I/O）在由PMU控制的独立电压级别上运行。

该攻击已在三个现代ARM Cortex-A SoC上进行了演示，当应用程序从内部存储器不受干扰地运行时，成功地从缓存、CPU寄存器和iRAM中检索到数据，准确率达到100%。这是在没有任何复杂的后处理的情况下实现的。

本文强调了片上计算方案的脆弱性，这些方案旨在通过将敏感数据保存在芯片边界内来保护敏感数据。Volt Boot证明，即使是这些架构也容易受到物理内存泄露攻击，因为它们利用了电源域分离。作者还讨论了潜在的对策及其权衡。主要结论是，片上SRAM并非固有地可以抵御所有物理攻击，而像电源域分离这样的架构设计可能会无意中引入新的漏洞。

---

## 66. 据报道，杰夫·贝佐斯有意收购CNBC，科技亿万富翁纷纷抢购媒体。

**原文标题**: Jeff Bezos Reportedly Eyes Purchase of CNBC as Tech Billionaires Gobble Up Media

**原文链接**: [https://gizmodo.com/jeff-bezos-reportedly-eyes-purchase-of-cnbc-as-tech-billionaires-gobble-up-media-2000633437](https://gizmodo.com/jeff-bezos-reportedly-eyes-purchase-of-cnbc-as-tech-billionaires-gobble-up-media-2000633437)

This July 2025 article reports that Jeff Bezos is considering purchasing CNBC, which is being spun off by Comcast into a new company called Versant. The author expresses concern, citing Bezos's alleged influence on the Washington Post since his 2013 acquisition. The article claims that Bezos suppressed a planned endorsement of Kamala Harris in the 2024 election and purged liberal voices from the Post's opinion pages, leading to subscriber losses and accusations of ideological meddling. The author highlights Bezos's apparent shift toward supporting Donald Trump, noting his attendance at the 2025 inauguration and subsequent meetings.

The article positions Bezos's potential acquisition of CNBC within a broader trend of tech billionaires acquiring media properties, referencing Elon Musk's purchase and transformation of Twitter into X, and David Ellison's impending leadership of Paramount after its merger with Skydance. The author also mentions rumors of Bezos's interest in Condé Nast, suggesting the possibility of carving out Vogue for his wife, Lauren Sanchez.

Ultimately, the piece argues that if Bezos were to acquire CNBC, it could become a tool for furthering his political and economic agenda. The author implies that this aligns with a broader trend of billionaires using media ownership to influence public opinion and political discourse.


---

## 67. 荷兰工业在能源转型和全球压力下举步维艰

**原文标题**: Dutch Industry Buckles Under Energy Transition and Global Pressure

**原文链接**: [https://oilprice.com/Energy/Energy-General/Dutch-Industry-Buckles-Under-Energy-Transition-and-Global-Pressure.html](https://oilprice.com/Energy/Energy-General/Dutch-Industry-Buckles-Under-Energy-Transition-and-Global-Pressure.html)

生成摘要时出错

---

## 68. 3-JSON

**原文标题**: 3-JSON

**原文链接**: [https://rgbcu.be/blog/3-json/](https://rgbcu.be/blog/3-json/)

生成摘要时出错

---

## 69. Implementing a functional language with graph reduction (2021)

**原文标题**: Implementing a functional language with graph reduction (2021)

**原文链接**: [https://thma.github.io/posts/2021-12-27-Implementing-a-functional-language-with-Graph-Reduction.html](https://thma.github.io/posts/2021-12-27-Implementing-a-functional-language-with-Graph-Reduction.html)

生成摘要时出错

---

## 70. Fig trees convert atmospheric CO₂ to stone, research reveals

**原文标题**: Fig trees convert atmospheric CO₂ to stone, research reveals

**原文链接**: [https://phys.org/news/2025-07-fig-trees-atmospheric-stone-reveals.html](https://phys.org/news/2025-07-fig-trees-atmospheric-stone-reveals.html)

This 2025 article reveals that certain fig trees in Kenya possess a unique ability to sequester atmospheric CO₂ and convert it into calcium carbonate, essentially turning themselves and the surrounding soil into stone. This process, known as the oxalate-carbonate pathway, involves the trees using CO₂ to create calcium oxalate crystals, which are then converted into calcium carbonate by specialized microorganisms when the tree decays. This inorganic carbon storage is more long-lasting than typical organic carbon sequestration, making it a potentially more effective method of mitigating CO₂ emissions.

Researchers from multiple institutions studied three fig tree species in Samburu County, Kenya, finding that *Ficus wakefieldii* was the most effective at this process. Synchrotron analysis revealed calcium carbonate formation both on the tree's surface and deeper within its wood, increasing soil alkalinity. This finding suggests the oxalate-carbonate pathway's potential for sequestering carbon has been previously underestimated.

The research team plans further studies to assess the suitability of *Ficus wakefieldii* for agroforestry, focusing on water requirements, fruit yields, and the amount of CO₂ sequestered under varying conditions. While the oxalate-carbonate pathway has been primarily studied in tropical, non-food-producing trees, the prevalence of calcium oxalate production and converting microorganisms suggests many more tree species may possess this capability. This highlights the oxalate-carbonate pathway as a significant, underexplored opportunity for CO₂ mitigation in forestry and fruit production.


---

## 71. 可空但非空

**原文标题**: Nullable but not null

**原文链接**: [https://efe.me/posts/nullable-but-not-null/](https://efe.me/posts/nullable-but-not-null/)

生成摘要时出错

---

## 72. Celebrating 20 Years of MDN

**原文标题**: Celebrating 20 Years of MDN

**原文链接**: [https://developer.mozilla.org/en-US/blog/mdn-turns-20/](https://developer.mozilla.org/en-US/blog/mdn-turns-20/)

生成摘要时出错

---

## 73. WhoFi: 基于Wi-Fi信道信号编码的深度行人重识别

**原文标题**: WhoFi: Deep Person Re-Identification via Wi-Fi Channel Signal Encoding

**原文链接**: [https://arxiv.org/abs/2507.12869](https://arxiv.org/abs/2507.12869)

生成摘要时出错

---

## 74. Show HN: The Montana MiniComputer

**原文标题**: Show HN: The Montana MiniComputer

**原文链接**: [https://mtmc.cs.montana.edu/](https://mtmc.cs.montana.edu/)

生成摘要时出错

---

## 75. High-speed organic light-emitting diodes achieving 4-Gbps communication

**原文标题**: High-speed organic light-emitting diodes achieving 4-Gbps communication

**原文链接**: [https://www.spiedigitallibrary.org/journals/advanced-photonics/volume-7/issue-03/036005/High-speed-organic-light-emitting-diodes-based-on-dinaphthylperylene-achieving/10.1117/1.AP.7.3.036005.full](https://www.spiedigitallibrary.org/journals/advanced-photonics/volume-7/issue-03/036005/High-speed-organic-light-emitting-diodes-based-on-dinaphthylperylene-achieving/10.1117/1.AP.7.3.036005.full)

生成摘要时出错

---

## 76. Why is there a date of 1968 in the Intel Chipset Device Software Utility?

**原文标题**: Why is there a date of 1968 in the Intel Chipset Device Software Utility?

**原文链接**: [https://www.intel.com/content/www/us/en/support/articles/000095169/processors.html](https://www.intel.com/content/www/us/en/support/articles/000095169/processors.html)

生成摘要时出错

---

## 77. How to draw lambda diagrams (2020)

**原文标题**: How to draw lambda diagrams (2020)

**原文链接**: [https://risingentropy.com/how-to-draw-lambda-diagrams/](https://risingentropy.com/how-to-draw-lambda-diagrams/)

生成摘要时出错

---

## 78. Lisp project of the day

**原文标题**: Lisp project of the day

**原文链接**: [https://40ants.com/lisp-project-of-the-day/index.html](https://40ants.com/lisp-project-of-the-day/index.html)

生成摘要时出错

---

## 79. Inter-Planetary Network Special Interest Group

**原文标题**: Inter-Planetary Network Special Interest Group

**原文链接**: [https://www.ipnsig.org](https://www.ipnsig.org)

生成摘要时出错

---

## 80. Stackless Traversal (2018)

**原文标题**: Stackless Traversal (2018)

**原文链接**: [https://www.dyalog.com/blog/2018/01/stackless-traversal/](https://www.dyalog.com/blog/2018/01/stackless-traversal/)

生成摘要时出错

---

## 81. Scientists may have found a way to eliminate chromosome linked to Down syndrome

**原文标题**: Scientists may have found a way to eliminate chromosome linked to Down syndrome

**原文链接**: [https://academic.oup.com/pnasnexus/article/4/2/pgaf022/8016019](https://academic.oup.com/pnasnexus/article/4/2/pgaf022/8016019)

生成摘要时出错

---

## 82. Trucking's uneasy relationship with new tech

**原文标题**: Trucking's uneasy relationship with new tech

**原文链接**: [https://www.bbc.com/news/articles/c5yeyn4gl80o](https://www.bbc.com/news/articles/c5yeyn4gl80o)

生成摘要时出错

---

## 83. Mwm – The smallest usable X11 window manager

**原文标题**: Mwm – The smallest usable X11 window manager

**原文链接**: [https://github.com/lslvr/mwm](https://github.com/lslvr/mwm)

生成摘要时出错

---

## 84. How to Catch a Wily Poacher in a Sting: A Thermal Robotic Deer

**原文标题**: How to Catch a Wily Poacher in a Sting: A Thermal Robotic Deer

**原文链接**: [https://www.wsj.com/us-news/how-to-catch-a-wily-poacher-in-a-sting-a-thermal-robotic-deer-ffef0fa8](https://www.wsj.com/us-news/how-to-catch-a-wily-poacher-in-a-sting-a-thermal-robotic-deer-ffef0fa8)

生成摘要时出错

---

## 85. Developing with Kiro: Amazon's New Agentic IDE

**原文标题**: Developing with Kiro: Amazon's New Agentic IDE

**原文链接**: [https://yehudacohen.substack.com/p/developing-with-kiro-amazons-new](https://yehudacohen.substack.com/p/developing-with-kiro-amazons-new)

生成摘要时出错

---

## 86. Air Force unit suspends use of Sig Sauer pistol after shooting death of airman

**原文标题**: Air Force unit suspends use of Sig Sauer pistol after shooting death of airman

**原文链接**: [https://www.nhpr.org/nh-news/2025-07-23/sig-sauer-pistol-air-force-shooting-death](https://www.nhpr.org/nh-news/2025-07-23/sig-sauer-pistol-air-force-shooting-death)

生成摘要时出错

---

## 87. Thunder Compute (YC S24) Is Hiring a C++ Systems Engineer

**原文标题**: Thunder Compute (YC S24) Is Hiring a C++ Systems Engineer

**原文链接**: [https://www.ycombinator.com/companies/thunder-compute/jobs/DhML6Uf-c-systems-engineer](https://www.ycombinator.com/companies/thunder-compute/jobs/DhML6Uf-c-systems-engineer)

生成摘要时出错

---

## 88. Against the censorship of adult content by payment processors

**原文标题**: Against the censorship of adult content by payment processors

**原文链接**: [https://soatok.blog/2025/07/24/against-the-censorship-of-adult-content-by-payment-processors/](https://soatok.blog/2025/07/24/against-the-censorship-of-adult-content-by-payment-processors/)

生成摘要时出错

---

## 89. Nuclear Reactor SIM by PeteTimesSix

**原文标题**: Nuclear Reactor SIM by PeteTimesSix

**原文链接**: [https://petetimessix.itch.io/nuclear-reactors](https://petetimessix.itch.io/nuclear-reactors)

生成摘要时出错

---

## 90. Chinese real-world self-driving test: 36 cars, 216 crashes, with Tesla on top

**原文标题**: Chinese real-world self-driving test: 36 cars, 216 crashes, with Tesla on top

**原文链接**: [https://electrek.co/2025/07/26/a-chinese-real-world-self-driving-test-36-cars-216-crashes-with-tesla-on-top/](https://electrek.co/2025/07/26/a-chinese-real-world-self-driving-test-36-cars-216-crashes-with-tesla-on-top/)

生成摘要时出错

---

## 91. Quantum Scientists Have Built a New Math of Cryptography

**原文标题**: Quantum Scientists Have Built a New Math of Cryptography

**原文链接**: [https://www.quantamagazine.org/quantum-scientists-have-built-a-new-math-of-cryptography-20250725/](https://www.quantamagazine.org/quantum-scientists-have-built-a-new-math-of-cryptography-20250725/)

生成摘要时出错

---

## 92. Building Brain Box, a meta text adventure film adaptation

**原文标题**: Building Brain Box, a meta text adventure film adaptation

**原文链接**: [https://kubicki.org/workbench/brain-box/](https://kubicki.org/workbench/brain-box/)

生成摘要时出错

---

## 93. Nvidia Launches Family of Open Reasoning AI Models: OpenReasoning Nemotron

**原文标题**: Nvidia Launches Family of Open Reasoning AI Models: OpenReasoning Nemotron

**原文链接**: [https://nvidianews.nvidia.com/news/nvidia-launches-family-of-open-reasoning-ai-models-for-developers-and-enterprises-to-build-agentic-ai-platforms](https://nvidianews.nvidia.com/news/nvidia-launches-family-of-open-reasoning-ai-models-for-developers-and-enterprises-to-build-agentic-ai-platforms)

生成摘要时出错

---

## 94. Modernish – A library for writing programs for POSIX-based shells and utilities

**原文标题**: Modernish – A library for writing programs for POSIX-based shells and utilities

**原文链接**: [https://github.com/modernish/modernish](https://github.com/modernish/modernish)

生成摘要时出错

---

## 95. Google's shortened goo.gl links will stop working next month

**原文标题**: Google's shortened goo.gl links will stop working next month

**原文链接**: [https://www.theverge.com/news/713125/google-url-shortener-links-shutdown-deadline](https://www.theverge.com/news/713125/google-url-shortener-links-shutdown-deadline)

生成摘要时出错

---

## 96. Google Opal

**原文标题**: Google Opal

**原文链接**: [https://developers.googleblog.com/en/introducing-opal/](https://developers.googleblog.com/en/introducing-opal/)

生成摘要时出错

---

## 97. My website is one binary (2022)

**原文标题**: My website is one binary (2022)

**原文链接**: [https://j3s.sh/thought/my-website-is-one-binary.html](https://j3s.sh/thought/my-website-is-one-binary.html)

生成摘要时出错

---

## 98. Ambigrammia: Between Creation and Discovery

**原文标题**: Ambigrammia: Between Creation and Discovery

**原文链接**: [https://yalebooks.yale.edu/book/9780300275438/ambigrammia/](https://yalebooks.yale.edu/book/9780300275438/ambigrammia/)

生成摘要时出错

---

## 99. Key Variables That Determine UBI's Inflationary Impact

**原文标题**: Key Variables That Determine UBI's Inflationary Impact

**原文链接**: [https://www.scottsantens.com/17-key-variables-that-determine-ubis-inflationary-impact/](https://www.scottsantens.com/17-key-variables-that-determine-ubis-inflationary-impact/)

生成摘要时出错

---

## 100. SQLx – The Rust SQL Toolkit

**原文标题**: SQLx – The Rust SQL Toolkit

**原文链接**: [https://github.com/launchbadge/sqlx](https://github.com/launchbadge/sqlx)

生成摘要时出错

---

