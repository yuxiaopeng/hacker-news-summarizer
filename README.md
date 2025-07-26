# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-07-26.md)

*最后自动更新时间: 2025-07-26 17:50:19*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 2 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 3 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 4 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 5 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 6 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 7 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 8 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 9 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 10 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 11 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 12 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 13 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 14 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 15 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 16 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 17 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 18 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 19 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 20 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 21 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 22 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 23 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 24 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 25 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 26 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 27 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 28 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 29 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 30 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 31 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 32 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 33 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 34 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 35 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 36 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 37 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 38 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 39 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 40 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 41 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 42 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 43 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 44 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 45 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 46 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 47 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 48 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 49 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 50 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 51 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 52 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 53 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 54 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 55 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 56 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 57 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 58 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 59 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 60 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 61 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 62 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 63 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 64 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 65 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 66 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 67 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 68 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 69 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 70 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 71 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 72 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 73 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 74 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 75 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 76 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 77 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 78 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 79 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 80 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 81 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 82 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 83 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 84 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 85 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 86 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 87 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 88 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 89 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 90 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 91 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 92 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 93 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 94 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 95 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 96 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 97 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 98 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 99 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 100 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 101 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 102 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 103 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 104 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 105 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 106 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 107 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 108 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 109 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 110 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 111 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 112 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 113 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 114 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 115 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 116 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 117 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 118 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 119 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 120 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 121 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 122 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 123 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 124 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 125 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 126 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 127 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 128 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 129 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
