# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-04-25.md)

*最后自动更新时间: 2026-04-25 18:10:07*
## 1. Niri 26.04 刚刚发布（可滚动平铺式 Wayland 合成器）

**原文标题**: Niri 26.04 was just released (scrollable-tiling Wayland compositor)

**原文链接**: [https://github.com/niri-wm/niri/releases/tag/v26.04](https://github.com/niri-wm/niri/releases/tag/v26.04)

Niri 26.04 版本正式发布，标志着这款可滚动平铺 Wayland 合成器迎来了重要里程碑。伴随着项目迁移至专门的 GitHub 组织以及 Star 数突破 20,000 大关，本次更新引入了多项备受期待的功能和技术改进。

**核心功能：**
*   **背景模糊：** 此版本引入了原生模糊支持，这是该项目呼声最高的功能。它同时支持标准模糊和高性能的“xray 模糊”，后者通过重用预计算的模糊壁纸来最大限度地减少资源占用。应用程序可以通过 `ext-background-effect` 协议请求模糊效果，或通过 Niri 配置规则对特定窗口和图层强制开启。
*   **录屏增强：** Niri 现支持 PipeWire 的元数据光标流，允许在显示器和窗口流中捕获光标。更新后的“动态投屏目标”提升了对 Microsoft Teams 等应用的兼容性，新的 IPC 机制则允许桌面状态栏显示活动录屏指示器。

**体验与配置：**
*   **指针跳转：** 借助指针跳转（Pointer Warping）功能，在无限窗口条中导航变得更加顺畅，它允许鼠标在滚动操作期间在屏幕边缘循环移动。
*   **配置改进：** 用户现在可以设置“可选”配置包含项，即使文件缺失也不会导致加载失败。合成器现已支持主目录路径的波浪号（~）路径扩展。
*   **窗口规则：** 新规则允许用户对弹出菜单和特定图层应用透明度与模糊效果。

**技术更新：**
最低支持的 Rust 版本现已提升至 1.85。此外，本次更新重构了服务文件，并利用 Smithay 库实现了显著的渲染改进，以支持复杂的新背景效果。

---

## 2. 1-Bit 葛饰北斋《巨浪》(2023)

**原文标题**: 1-Bit Hokusai's "The Great Wave" (2023)

**原文链接**: [https://www.hypertalking.com/2023/05/08/1-bit-pixel-art-of-hokusais-the-great-wave-off-kanagawa/](https://www.hypertalking.com/2023/05/08/1-bit-pixel-art-of-hokusais-the-great-wave-off-kanagawa/)

在本文中，作者介绍了一个将葛饰北斋标志性的《富岳三十六景》重塑为 1-bit 像素画的创意项目。出于对“心流”状态的热爱以及对早期计算技术的怀旧，作者从初代麦金塔（Macintosh）图标设计师苏珊·卡雷（Susan Kare）的作品中汲取了美学灵感。

为确保作品的纯正性，该项目遵循严格的技术限制：所有图像均以 512 x 342 像素的原始麦金塔分辨率创作。作者使用了符合时代特征的硬件和软件，具体为运行 System 7 和 Aldus SuperPaint 3.0 的 Macintosh Quadra 700 或 PowerBook 100。

尽管该项目始于五年前且目前处于停滞状态，但作者还是分享了《神奈川冲浪里》——这是首张发布的图像，尽管它并非按原定顺序创作。该作品以“知识共享 署名-非商业性使用-禁止演绎”（CC BY-NC-ND）许可协议发布。针对复古技术爱好者，作者还提供了一个 640 x 480 版本的作品，供旧版麦金塔系统用作桌面底纹。作者表示，他的目标是最终重启该项目并完成系列中的其余画作。

---

## 3. 新款 10 GbE USB 适配器更冷、更小、更便宜

**原文标题**: New 10 GbE USB adapters are cooler, smaller, cheaper

**原文链接**: [https://www.jeffgeerling.com/blog/2026/new-10-gbe-usb-adapters-cooler-smaller-cheaper/](https://www.jeffgeerling.com/blog/2026/new-10-gbe-usb-adapters-cooler-smaller-cheaper/)

本文评测了新一代 10 GbE USB 网卡，重点介绍了一款售价 80 美元、采用 RTL8159 芯片的 WisdPi 型号。相比传统、笨重的雷电 (Thunderbolt) 接口 10 GbE 网卡，这些适配器体积更小、价格更低且运行温度更低。

**核心发现：**
*   **性能瓶颈：** 虽然标称为 10 Gbps，但这些网卡需要 **USB 3.2 Gen 2x2 (20 Gbps)** 接口才能达到全速。在标准 10 Gbps 接口（常见于大多数 Mac 和笔记本电脑）上，协议开销导致性能被限制在约 6–7 Gbps。
*   **散热与功耗：** 与发热严重的旧款 Aquantia 芯片网卡不同，新型 RTL8159 芯片的效率显著提高。在负载下，WisdPi 网卡的温度仅为 42.5°C，安全性与便携性更高。
*   **兼容性：** 该设备在 macOS 上支持即插即用（尽管设置中可能会误报连接速度）。在 Windows 上，用户必须手动安装最新的 Realtek 驱动程序才能建立连接。
*   **性价比：** 该网卡售价 80 美元，价格仅为雷电替代方案的一半，但比 5 Gbps 网卡贵了一倍多。

**结论：**
作者认为，如果你拥有 20 Gbps USB 接口和现有的 10G RJ45 网络，这些网卡是绝佳的紧凑型选择。然而，对于使用标准 10 Gbps USB 接口的用户，相比仅需 30 美元的 5 Gbps 网卡，其带来的速度提升可能并不足以支撑其价格。对于需要在标准接口上确保 10 Gbps 全速吞吐量的用户，雷电网卡虽然价格更高，但依然是更优的选择。

---

## 4. 免费通用搭建套件

**原文标题**: The Free Universal Construction Kit

**原文链接**: [https://fffff.at/free-universal-construction-kit/](https://fffff.at/free-universal-construction-kit/)

**自由通用搭建套件**（The Free Universal Construction Kit）由 F.A.T. 实验室（F.A.T. Lab）和 Sy 实验室（Sy-Lab）发布，包含近 80 个可 3D 打印的适配积木，旨在实现乐高（Lego）、康乐思（K’Nex）、慧鱼（Fischertechnik）、Tinkertoys 和林肯原木（Lincoln Logs）等十种流行建筑玩具系统之间的全面互操作。通过连接这些传统上封闭且受专利保护的系统，该套件鼓励“激进混搭”的玩法，并确保玩具在孩子成长过程中依然有用，而不至于被淘汰。

这些适配器是通过高精度光学比较仪对玩具连接件进行逆向工程开发的，以确保连接稳固可靠。该项目包含一个“通用适配积木”，可同时实现所有受支持系统之间的连接。创作者在 Thingiverse 等平台上提供免费的 STL 文件，供用户通过个人 3D 打印机自行制作。

该项目既是一个实用工具，也是一份社会政治宣言。创作者将其描述为“儿童玩具界的 VLC”，为玩具制造商造成的“技术锁定”提供了一种草根补救方案，因为制造商往往没有动力让自己的产品与竞争对手兼容。通过提供一个“元混搭系统”，该套件赋能用户去克服大规模生产的商业产品的局限性。

在法律层面，创作者断言该套件构成了出于非商业、私人目的的受保护“合理使用”。为了尊重知识产权法，他们刻意推迟了仍处于有效专利保护期内的系统（如 Zoob 和 Zome）适配器的发布。最终，该套件成为了“逆向工程作为公民活动”的典范，引发了人们对于个人制造如何使大众文化适应人类想象力的深思。

---

## 5. 马丁·加尔维 20 世纪 80 年代 Commodore 64 游戏音乐源文件

**原文标题**: Martin Galway's music source files from 1980's Commodore 64 games

**原文链接**: [https://github.com/MartinGalway/C64_music](https://github.com/MartinGalway/C64_music)

在此公告中，传奇的 Commodore 64 作曲家 Martin Galway 发布了他 20 世纪 80 年代游戏项目的原始音乐源文件和编程代码。此次发布旨在用于教育目的，让爱好者能够分析他的音乐播放程序、修改代码并创作新作品。

关键详情包括：

*   **使用权：** Galway 目前拥有这些作品的版权（购自 Infogrames），并允许重新汇编和修改，前提是必须注明其原作者身份。
*   **技术演进：** 这些文件记录了两代不同音乐播放程序之间的更迭。“第一代”播放器使用于 1984 年至 1987 年中期（代表作为《Wizball》），而“第二代”播放器随《Athena》首次亮相，并用于随后的《Times of Lore》和《Insects in Space》等作品。
*   **发布目的：** 此次发布旨在帮助他人理解这些经典 C64 游戏音频背后的技术实现方法。

---

## 6. Google plans to invest up to $40B in Anthropic

**原文标题**: Google plans to invest up to $40B in Anthropic

**原文链接**: [https://www.bloomberg.com/news/articles/2026-04-24/google-plans-to-invest-up-to-40-billion-in-anthropic](https://www.bloomberg.com/news/articles/2026-04-24/google-plans-to-invest-up-to-40-billion-in-anthropic)

生成摘要时出错

---

## 7. GPT 5.5 biosafety bounty

**原文标题**: GPT 5.5 biosafety bounty

**原文链接**: [https://openai.com/index/gpt-5-5-bio-bug-bounty/](https://openai.com/index/gpt-5-5-bio-bug-bounty/)

生成摘要时出错

---

## 8. What's Missing in the 'Agentic' Story

**原文标题**: What's Missing in the 'Agentic' Story

**原文链接**: [https://www.mnot.net/blog/2026/04/24/agents_as_collective_bargains](https://www.mnot.net/blog/2026/04/24/agents_as_collective_bargains)

生成摘要时出错

---

## 9. Insights into firewood use by early Middle Pleistocene hominins

**原文标题**: Insights into firewood use by early Middle Pleistocene hominins

**原文链接**: [https://www.sciencedirect.com/science/article/pii/S0277379126001824](https://www.sciencedirect.com/science/article/pii/S0277379126001824)

生成摘要时出错

---

## 10. Desmond Morris, 98, Dies; Zoologist Saw Links Between Humans and Apes

**原文标题**: Desmond Morris, 98, Dies; Zoologist Saw Links Between Humans and Apes

**原文链接**: [https://www.nytimes.com/2026/04/20/science/desmond-morris-dead.html](https://www.nytimes.com/2026/04/20/science/desmond-morris-dead.html)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 2 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 3 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 4 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 5 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 6 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 7 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 8 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 9 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 10 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 11 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 12 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 13 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 14 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 15 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 16 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 17 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 18 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 19 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 20 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 21 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 22 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 23 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 24 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 25 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 26 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 27 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 28 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 29 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 30 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 31 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 32 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 33 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 34 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 35 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 36 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 37 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 38 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 39 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 40 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 41 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 42 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 43 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 44 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 45 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 46 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 47 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 48 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 49 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 50 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 51 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 52 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 53 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 54 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 55 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 56 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 57 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 58 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 59 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 60 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 61 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 62 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 63 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 64 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 65 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 66 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 67 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 68 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 69 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 70 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 71 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 72 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 73 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 74 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 75 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 76 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 77 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 78 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 79 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 80 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 81 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 82 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 83 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 84 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 85 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 86 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 87 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 88 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 89 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 90 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 91 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 92 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 93 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 94 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 95 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 96 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 97 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 98 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 99 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 100 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 101 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 102 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 103 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 104 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 105 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 106 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 107 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 108 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 109 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 110 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 111 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 112 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 113 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 114 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 115 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 116 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 117 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 118 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 119 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 120 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 121 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 122 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 123 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 124 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 125 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 126 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 127 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 128 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 129 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 130 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 131 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 132 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 133 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 134 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 135 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 136 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 137 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 138 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 139 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 140 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 141 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 142 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 143 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 144 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 145 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 146 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 147 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 148 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 149 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 150 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 151 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 152 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 153 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 154 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 155 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 156 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 157 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 158 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 159 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 160 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 161 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 162 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 163 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 164 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 165 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 166 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 167 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 168 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 169 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 170 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 171 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 172 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 173 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 174 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 175 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 176 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 177 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 178 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 179 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 180 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 181 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 182 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 183 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 184 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 185 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 186 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 187 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 188 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 189 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 190 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 191 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 192 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 193 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 194 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 195 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 196 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 197 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 198 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 199 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 200 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 201 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 202 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 203 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 204 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 205 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 206 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 207 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 208 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 209 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 210 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 211 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 212 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 213 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 214 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 215 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 216 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 217 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 218 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 219 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 220 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 221 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 222 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 223 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 224 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 225 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 226 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 227 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 228 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 229 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 230 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 231 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 232 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 233 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 234 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 235 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 236 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 237 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 238 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 239 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 240 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 241 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 242 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 243 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 244 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 245 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 246 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 247 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 248 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 249 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 250 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 251 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 252 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 253 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 254 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 255 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 256 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 257 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 258 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 259 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 260 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 261 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 262 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 263 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 264 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 265 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 266 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 267 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 268 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 269 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 270 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 271 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 272 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 273 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 274 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 275 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 276 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 277 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 278 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 279 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 280 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 281 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 282 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 283 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 284 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 285 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 286 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 287 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 288 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 289 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 290 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 291 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 292 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 293 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 294 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 295 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 296 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 297 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 298 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 299 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 300 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 301 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 302 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 303 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 304 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 305 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 306 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 307 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 308 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 309 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 310 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 311 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 312 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 313 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 314 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 315 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 316 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 317 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 318 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 319 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 320 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 321 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 322 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 323 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 324 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 325 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 326 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 327 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 328 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 329 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 330 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 331 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 332 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 333 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 334 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 335 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 336 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 337 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 338 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 339 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 340 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 341 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 342 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 343 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 344 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 345 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 346 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 347 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 348 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 349 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 350 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 351 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 352 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 353 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 354 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 355 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 356 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 357 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 358 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 359 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 360 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 361 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 362 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 363 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 364 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 365 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 366 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 367 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 368 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 369 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 370 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 371 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 372 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 373 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 374 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 375 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 376 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 377 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 378 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 379 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 380 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 381 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 382 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 383 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 384 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 385 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 386 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 387 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 388 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 389 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 390 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 391 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 392 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 393 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 394 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 395 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 396 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 397 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 398 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 399 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 400 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 401 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
