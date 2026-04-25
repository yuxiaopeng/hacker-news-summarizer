# Hacker News 热门文章摘要 (2026-04-25)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Discret 11, the French TV encryption of the 80s

**原文标题**: Discret 11, the French TV encryption of the 80s

**原文链接**: [https://fabiensanglard.net/discret11/](https://fabiensanglard.net/discret11/)

生成摘要时出错

---

## 12. A web-based RDP client built with Go WebAssembly and grdp

**原文标题**: A web-based RDP client built with Go WebAssembly and grdp

**原文链接**: [https://github.com/nakagami/grdpwasm](https://github.com/nakagami/grdpwasm)

生成摘要时出错

---

## 13. 面向人工智能的 Lambda 演算基准

**原文标题**: Lambda Calculus Benchmark for AI

**原文链接**: [https://victortaelin.github.io/lambench/](https://victortaelin.github.io/lambench/)

**LamBench** is a specialized benchmark suite designed by Victor Taelin (v1) to evaluate Artificial Intelligence through the lens of **Lambda Calculus**. 

The benchmark assesses AI performance based on three core pillars:
*   **Intelligence:** The ability to solve complex functional programming problems.
*   **Speed:** The computational efficiency and time-to-solution.
*   **Elegance:** The minimalism and refinement of the resulting code.

The project features a comprehensive problem set and a performance matrix to track and compare how different models handle formal logic and functional computation. LamBench aims to provide a rigorous standard for testing the reasoning capabilities of AI, moving beyond natural language toward formal mathematical structures. The repository and its documentation can be found at [github.com/VictorTaelin/LamBench](https://github.com/VictorTaelin/LamBench).

---

## 14. HEALPix

**原文标题**: HEALPix

**原文链接**: [https://en.wikipedia.org/wiki/HEALPix](https://en.wikipedia.org/wiki/HEALPix)

生成摘要时出错

---

## 15. A Collection of Chronic Medical Conditions Common in Autistic and ADHD Adults [pdf]

**原文标题**: A Collection of Chronic Medical Conditions Common in Autistic and ADHD Adults [pdf]

**原文链接**: [https://allbrainsbelong.org/wp-content/uploads/2023/08/CLINICIAN-GUIDE-Everything-is-Connected-to-Everything-Project-All-Brains-Belong-VT-8.15.23.pdf](https://allbrainsbelong.org/wp-content/uploads/2023/08/CLINICIAN-GUIDE-Everything-is-Connected-to-Everything-Project-All-Brains-Belong-VT-8.15.23.pdf)

生成摘要时出错

---

## 16. Which one is more important: more parameters or more computation? (2021)

**原文标题**: Which one is more important: more parameters or more computation? (2021)

**原文链接**: [https://parl.ai/projects/params_vs_compute/](https://parl.ai/projects/params_vs_compute/)

生成摘要时出错

---

## 17. Commenting and Approving Pull Requests

**原文标题**: Commenting and Approving Pull Requests

**原文链接**: [https://www.jakeworth.com/posts/on-commenting-and-approving-pull-requests/](https://www.jakeworth.com/posts/on-commenting-and-approving-pull-requests/)

生成摘要时出错

---

## 18. Plain text has been around for decades and it’s here to stay

**原文标题**: Plain text has been around for decades and it’s here to stay

**原文链接**: [https://unsung.aresluna.org/plain-text-has-been-around-for-decades-and-its-here-to-stay/](https://unsung.aresluna.org/plain-text-has-been-around-for-decades-and-its-here-to-stay/)

生成摘要时出错

---

## 19. Replace IBM Quantum back end with /dev/urandom

**原文标题**: Replace IBM Quantum back end with /dev/urandom

**原文链接**: [https://github.com/yuvadm/quantumslop/blob/25ad2e76ae58baa96f6219742459407db9dd17f5/URANDOM_DEMO.md](https://github.com/yuvadm/quantumslop/blob/25ad2e76ae58baa96f6219742459407db9dd17f5/URANDOM_DEMO.md)

生成摘要时出错

---

## 20. A 3D Body from Eight Questions – No Photo, No GPU

**原文标题**: A 3D Body from Eight Questions – No Photo, No GPU

**原文链接**: [https://clad.you/blog/posts/questionnaire-mlp/](https://clad.you/blog/posts/questionnaire-mlp/)

生成摘要时出错

---

## 21. Sabotaging projects by overthinking, scope creep, and structural diffing

**原文标题**: Sabotaging projects by overthinking, scope creep, and structural diffing

**原文链接**: [https://kevinlynagh.com/newsletter/2026_04_overthinking/](https://kevinlynagh.com/newsletter/2026_04_overthinking/)

生成摘要时出错

---

## 22. Paraloid B-72

**原文标题**: Paraloid B-72

**原文链接**: [https://en.wikipedia.org/wiki/Paraloid_B-72](https://en.wikipedia.org/wiki/Paraloid_B-72)

生成摘要时出错

---

## 23. Only One Side Will Be the True Successor to MS-DOS – Windows 2.x

**原文标题**: Only One Side Will Be the True Successor to MS-DOS – Windows 2.x

**原文链接**: [https://blisscast.wordpress.com/2026/04/21/windows-2-gui-wonderland-12a/](https://blisscast.wordpress.com/2026/04/21/windows-2-gui-wonderland-12a/)

生成摘要时出错

---

## 24. My audio interface has SSH enabled by default

**原文标题**: My audio interface has SSH enabled by default

**原文链接**: [https://hhh.hn/rodecaster-duo-fw/](https://hhh.hn/rodecaster-duo-fw/)

生成摘要时出错

---

## 25. Humpback whales are forming super-groups

**原文标题**: Humpback whales are forming super-groups

**原文链接**: [https://www.bbc.com/future/article/20260416-the-humpback-super-groups-swarming-the-seas](https://www.bbc.com/future/article/20260416-the-humpback-super-groups-swarming-the-seas)

生成摘要时出错

---

## 26. The mail sent to a video game publisher

**原文标题**: The mail sent to a video game publisher

**原文链接**: [https://www.gamefile.news/p/panic-mail-arco-despelote-time-flies-thank-goodness-teeth](https://www.gamefile.news/p/panic-mail-arco-despelote-time-flies-thank-goodness-teeth)

生成摘要时出错

---

## 27. How to Implement an FPS Counter

**原文标题**: How to Implement an FPS Counter

**原文链接**: [https://vplesko.com/posts/how_to_implement_an_fps_counter.html](https://vplesko.com/posts/how_to_implement_an_fps_counter.html)

生成摘要时出错

---

## 28. Framework Laptop 13 Pro: Major Upgrades and Linux Front and Center

**原文标题**: Framework Laptop 13 Pro: Major Upgrades and Linux Front and Center

**原文链接**: [https://boilingsteam.com/framework-laptop-13-pro-announced/](https://boilingsteam.com/framework-laptop-13-pro-announced/)

生成摘要时出错

---

## 29. Open source memory layer so any AI agent can do what Claude.ai and ChatGPT do

**原文标题**: Open source memory layer so any AI agent can do what Claude.ai and ChatGPT do

**原文链接**: [https://alash3al.github.io/stash?_v01](https://alash3al.github.io/stash?_v01)

生成摘要时出错

---

## 30. Iliad fragment found in Roman-era mummy

**原文标题**: Iliad fragment found in Roman-era mummy

**原文链接**: [https://www.thehistoryblog.com/archives/75877](https://www.thehistoryblog.com/archives/75877)

生成摘要时出错

---

## 31. Show HN: A Karpathy-style LLM wiki your agents maintain (Markdown and Git)

**原文标题**: Show HN: A Karpathy-style LLM wiki your agents maintain (Markdown and Git)

**原文链接**: [https://github.com/nex-crm/wuphf](https://github.com/nex-crm/wuphf)

生成摘要时出错

---

## 32. Education must go beyond the mere production of words

**原文标题**: Education must go beyond the mere production of words

**原文链接**: [https://www.ncregister.com/commentaries/schnell-repairing-the-ruins](https://www.ncregister.com/commentaries/schnell-repairing-the-ruins)

生成摘要时出错

---

## 33. There Will Be a Scientific Theory of Deep Learning

**原文标题**: There Will Be a Scientific Theory of Deep Learning

**原文链接**: [https://arxiv.org/abs/2604.21691](https://arxiv.org/abs/2604.21691)

生成摘要时出错

---

## 34. Email could have been X.400 times better

**原文标题**: Email could have been X.400 times better

**原文链接**: [https://buttondown.com/blog/x400-vs-smtp-email](https://buttondown.com/blog/x400-vs-smtp-email)

生成摘要时出错

---

## 35. PCR is a surprisingly near-optimal technology

**原文标题**: PCR is a surprisingly near-optimal technology

**原文链接**: [https://nikomc.com/2026/04/22/pcr/](https://nikomc.com/2026/04/22/pcr/)

生成摘要时出错

---

## 36. DeepSeek v4

**原文标题**: DeepSeek v4

**原文链接**: [https://api-docs.deepseek.com/news/news260424](https://api-docs.deepseek.com/news/news260424)

生成摘要时出错

---

## 37. Cosmology with Geometry Nodes

**原文标题**: Cosmology with Geometry Nodes

**原文链接**: [https://www.blender.org/user-stories/cosmology-with-geometry-nodes/](https://www.blender.org/user-stories/cosmology-with-geometry-nodes/)

生成摘要时出错

---

## 38. Work with the garage door up (2024)

**原文标题**: Work with the garage door up (2024)

**原文链接**: [https://notes.andymatuschak.org/Work_with_the_garage_door_up](https://notes.andymatuschak.org/Work_with_the_garage_door_up)

生成摘要时出错

---

## 39. Jumping into cold water can stop your heart

**原文标题**: Jumping into cold water can stop your heart

**原文链接**: [https://jorgenmelau.substack.com/p/the-first-sixty-seconds](https://jorgenmelau.substack.com/p/the-first-sixty-seconds)

生成摘要时出错

---

## 40. Iran caused more extensive damage to U.S. military bases than publicly known

**原文标题**: Iran caused more extensive damage to U.S. military bases than publicly known

**原文链接**: [https://www.nbcnews.com/world/iran/iran-caused-extensive-damage-us-military-bases-publicly-known-rcna331853](https://www.nbcnews.com/world/iran/iran-caused-extensive-damage-us-military-bases-publicly-known-rcna331853)

生成摘要时出错

---

## 41. Turbo Vision 2.0 – a modern port

**原文标题**: Turbo Vision 2.0 – a modern port

**原文链接**: [https://github.com/magiblot/tvision](https://github.com/magiblot/tvision)

生成摘要时出错

---

## 42. The Classic American Diner

**原文标题**: The Classic American Diner

**原文链接**: [https://blogs.loc.gov/picturethis/2026/04/the-classic-american-diner/](https://blogs.loc.gov/picturethis/2026/04/the-classic-american-diner/)

生成摘要时出错

---

## 43. Firefox Has Integrated Brave's Adblock Engine

**原文标题**: Firefox Has Integrated Brave's Adblock Engine

**原文链接**: [https://itsfoss.com/news/firefox-ships-brave-adblock-engine/](https://itsfoss.com/news/firefox-ships-brave-adblock-engine/)

生成摘要时出错

---

## 44. GPT-5.5

**原文标题**: GPT-5.5

**原文链接**: [https://openai.com/index/introducing-gpt-5-5/](https://openai.com/index/introducing-gpt-5-5/)

生成摘要时出错

---

## 45. Diatec, known for its mechanical keyboard brand FILCO, has ceased operations

**原文标题**: Diatec, known for its mechanical keyboard brand FILCO, has ceased operations

**原文链接**: [https://gigazine.net/gsc_news/en/20260424-filco-diatec/](https://gigazine.net/gsc_news/en/20260424-filco-diatec/)

生成摘要时出错

---

## 46. Show HN: I've built a nice home server OS

**原文标题**: Show HN: I've built a nice home server OS

**原文链接**: [https://lightwhale.asklandd.dk/](https://lightwhale.asklandd.dk/)

生成摘要时出错

---

## 47. A Man Who Invented the Future

**原文标题**: A Man Who Invented the Future

**原文链接**: [https://hedgehogreview.com/web-features/thr/posts/the-man-who-invented-the-future](https://hedgehogreview.com/web-features/thr/posts/the-man-who-invented-the-future)

生成摘要时出错

---

## 48. I'm done making desktop applications (2009)

**原文标题**: I'm done making desktop applications (2009)

**原文链接**: [https://www.kalzumeus.com/2009/09/05/desktop-aps-versus-web-apps/](https://www.kalzumeus.com/2009/09/05/desktop-aps-versus-web-apps/)

生成摘要时出错

---

## 49. I cancelled Claude: Token issues, declining quality, and poor support

**原文标题**: I cancelled Claude: Token issues, declining quality, and poor support

**原文链接**: [https://nickyreinert.de/en/2026/2026-04-24-claude-critics/](https://nickyreinert.de/en/2026/2026-04-24-claude-critics/)

A veteran software engineer explains why they cancelled their Claude Pro subscription despite being an admirer of the product’s capabilities. While the author initially found Claude Code transformative for productivity, three primary issues led to their departure: poor support, token mismanagement, and declining output quality.

**Key Issues Highlighted:**

*   **Inadequate Customer Support:** The author describes a frustrating experience where technical inquiries regarding token spikes were met with generic, automated responses. Support tickets were closed prematurely without addressing the actual problem, leaving the user with no recourse for technical glitches.
*   **Token and Caching Inefficiency:** The author points to "bad design decisions" regarding how tokens are consumed. Specifically, when the conversation cache expires during forced breaks, users are charged tokens to have the model re-read the same codebase. Additionally, the author encountered undocumented "monthly limit" warnings that contradicted the official documentation.
*   **Model "Laziness":** The post details a decline in output quality, citing an instance where Claude Opus suggested a "cheap workaround" rather than a proper refactor. Correcting these lazy suggestions further exhausted the user’s five-hour token window, making the tool feel less reliable and more expensive over time.

While the author acknowledges that AI quality is subjective and that Anthropic faces significant scaling challenges, they conclude that the combination of technical friction and dismissive service made the Pro subscription unsustainable. Despite the product's potential, the author opted to cancel to avoid the stress of navigating an increasingly restrictive and poorly supported environment.

---

## 50. $8800 house design helps prevent fatal diseases in African children

**原文标题**: $8800 house design helps prevent fatal diseases in African children

**原文链接**: [https://www.science.org/content/article/simple-house-may-help-prevent-multiple-fatal-diseases-african-children](https://www.science.org/content/article/simple-house-may-help-prevent-multiple-fatal-diseases-african-children)

生成摘要时出错

---

## 51. Social media is no longer social

**原文标题**: Social media is no longer social

**原文链接**: [https://bsky.app/profile/pettertornberg.com/post/3mk64uzhdm22z](https://bsky.app/profile/pettertornberg.com/post/3mk64uzhdm22z)

生成摘要时出错

---

## 52. Larry McMurtry's Tall Tales

**原文标题**: Larry McMurtry's Tall Tales

**原文链接**: [https://www.thenation.com/article/culture/larry-mcmurtry-biography/](https://www.thenation.com/article/culture/larry-mcmurtry-biography/)

生成摘要时出错

---

## 53. Show HN: Browser Harness – Gives LLM freedom to complete any browser task

**原文标题**: Show HN: Browser Harness – Gives LLM freedom to complete any browser task

**原文链接**: [https://github.com/browser-use/browser-harness](https://github.com/browser-use/browser-harness)

生成摘要时出错

---

## 54. Panipat: The Rise of the Mughals

**原文标题**: Panipat: The Rise of the Mughals

**原文链接**: [https://www.historytoday.com/archive/feature/panipat-rise-mughals](https://www.historytoday.com/archive/feature/panipat-rise-mughals)

生成摘要时出错

---

## 55. MacBook Neo and how the iPad should be

**原文标题**: MacBook Neo and how the iPad should be

**原文链接**: [https://craigmod.com/essays/ipad_neo/](https://craigmod.com/essays/ipad_neo/)

生成摘要时出错

---

## 56. The Overtom Chess Computer Museum

**原文标题**: The Overtom Chess Computer Museum

**原文链接**: [https://tluif.home.xs4all.nl/chescom/Engindex.html](https://tluif.home.xs4all.nl/chescom/Engindex.html)

生成摘要时出错

---

## 57. Escrow Security for iCloud Keychain

**原文标题**: Escrow Security for iCloud Keychain

**原文链接**: [https://support.apple.com/guide/security/escrow-security-for-icloud-keychain-sec3e341e75d/web](https://support.apple.com/guide/security/escrow-security-for-icloud-keychain-sec3e341e75d/web)

生成摘要时出错

---

## 58. Alberta startup sells no-tech tractors for half price

**原文标题**: Alberta startup sells no-tech tractors for half price

**原文链接**: [https://wheelfront.com/this-alberta-startup-sells-no-tech-tractors-for-half-price/](https://wheelfront.com/this-alberta-startup-sells-no-tech-tractors-for-half-price/)

生成摘要时出错

---

## 59. US special forces soldier arrested after allegedly winning $400k on Maduro raid

**原文标题**: US special forces soldier arrested after allegedly winning $400k on Maduro raid

**原文链接**: [https://www.cnn.com/2026/04/23/politics/us-special-forces-soldier-arrested-maduro-raid-trade](https://www.cnn.com/2026/04/23/politics/us-special-forces-soldier-arrested-maduro-raid-trade)

生成摘要时出错

---

## 60. SDL Now Supports DOS

**原文标题**: SDL Now Supports DOS

**原文链接**: [https://github.com/libsdl-org/SDL/pull/15377](https://github.com/libsdl-org/SDL/pull/15377)

生成摘要时出错

---

## 61. Apple fixes bug that cops used to extract deleted chat messages from iPhones

**原文标题**: Apple fixes bug that cops used to extract deleted chat messages from iPhones

**原文链接**: [https://techcrunch.com/2026/04/22/apple-fixes-bug-that-cops-used-to-extract-deleted-chat-messages-from-iphones/](https://techcrunch.com/2026/04/22/apple-fixes-bug-that-cops-used-to-extract-deleted-chat-messages-from-iphones/)

生成摘要时出错

---

## 62. Zhenguan Zhengyao

**原文标题**: Zhenguan Zhengyao

**原文链接**: [http://www.chinaknowledge.de/Literature/Historiography/zhenguanzhengyao.html](http://www.chinaknowledge.de/Literature/Historiography/zhenguanzhengyao.html)

生成摘要时出错

---

## 63. Jiga (YC W21) Is Hiring

**原文标题**: Jiga (YC W21) Is Hiring

**原文链接**: [https://jiga.io/about-us/](https://jiga.io/about-us/)

生成摘要时出错

---

## 64. FusionCore: ROS 2 sensor fusion (IMU and GPS and encoders)

**原文标题**: FusionCore: ROS 2 sensor fusion (IMU and GPS and encoders)

**原文链接**: [https://github.com/manankharwar/fusioncore](https://github.com/manankharwar/fusioncore)

生成摘要时出错

---

## 65. Writing a C Compiler, in Zig (2025)

**原文标题**: Writing a C Compiler, in Zig (2025)

**原文链接**: [https://ar-ms.me/thoughts/c-compiler-1-zig/](https://ar-ms.me/thoughts/c-compiler-1-zig/)

生成摘要时出错

---

## 66. YC as a Service

**原文标题**: YC as a Service

**原文链接**: [https://ycaas.lol](https://ycaas.lol)

生成摘要时出错

---

## 67. Composition shouldn't be this hard

**原文标题**: Composition shouldn't be this hard

**原文链接**: [https://www.cambra.dev/blog/announcement/](https://www.cambra.dev/blog/announcement/)

生成摘要时出错

---

## 68. Behind-the-Scenes of MacBook Neo Introduction Video

**原文标题**: Behind-the-Scenes of MacBook Neo Introduction Video

**原文链接**: [https://www.youtube.com/shorts/y4DnsCzJTRQ](https://www.youtube.com/shorts/y4DnsCzJTRQ)

生成摘要时出错

---

## 69. 8087 Emulation on 8086 Systems

**原文标题**: 8087 Emulation on 8086 Systems

**原文链接**: [https://www.os2museum.com/wp/learn-something-old-every-day-part-xx-8087-emulation-on-8086-systems/](https://www.os2museum.com/wp/learn-something-old-every-day-part-xx-8087-emulation-on-8086-systems/)

生成摘要时出错

---

## 70. TIPSv2: Advancing Vision-Language Pretraining with Enhanced Patch-Text Alignment

**原文标题**: TIPSv2: Advancing Vision-Language Pretraining with Enhanced Patch-Text Alignment

**原文链接**: [https://gdm-tipsv2.github.io/](https://gdm-tipsv2.github.io/)

生成摘要时出错

---

## 71. Used La Marzocco machines are coveted by cafe owners and collectors

**原文标题**: Used La Marzocco machines are coveted by cafe owners and collectors

**原文链接**: [https://www.nytimes.com/2026/04/20/dining/la-marzocco-espresso-machine.html](https://www.nytimes.com/2026/04/20/dining/la-marzocco-espresso-machine.html)

生成摘要时出错

---

## 72. Cactus, a work-stealing parallel recursion runtime for C

**原文标题**: Cactus, a work-stealing parallel recursion runtime for C

**原文链接**: [https://github.com/xtellect/cactus](https://github.com/xtellect/cactus)

生成摘要时出错

---

## 73. Show HN: Agent Vault – Open-source credential proxy and vault for agents

**原文标题**: Show HN: Agent Vault – Open-source credential proxy and vault for agents

**原文链接**: [https://github.com/Infisical/agent-vault](https://github.com/Infisical/agent-vault)

生成摘要时出错

---

## 74. My phone replaced a brass plug

**原文标题**: My phone replaced a brass plug

**原文链接**: [https://drobinin.com/posts/my-phone-replaced-a-brass-plug/](https://drobinin.com/posts/my-phone-replaced-a-brass-plug/)

生成摘要时出错

---

## 75. Astronomers find the edge of the Milky Way

**原文标题**: Astronomers find the edge of the Milky Way

**原文链接**: [https://skyandtelescope.org/astronomy-news/astronomers-find-the-edge-of-the-milky-way/](https://skyandtelescope.org/astronomy-news/astronomers-find-the-edge-of-the-milky-way/)

生成摘要时出错

---

## 76. Show HN: Tolaria – Open-source macOS app to manage Markdown knowledge bases

**原文标题**: Show HN: Tolaria – Open-source macOS app to manage Markdown knowledge bases

**原文链接**: [https://github.com/refactoringhq/tolaria](https://github.com/refactoringhq/tolaria)

生成摘要时出错

---

## 77. Why I Write (1946)

**原文标题**: Why I Write (1946)

**原文链接**: [https://www.orwellfoundation.com/the-orwell-foundation/orwell/essays-and-other-works/why-i-write/](https://www.orwellfoundation.com/the-orwell-foundation/orwell/essays-and-other-works/why-i-write/)

生成摘要时出错

---

## 78. Show HN: VT Code – Rust TUI coding agent with multi-provider support

**原文标题**: Show HN: VT Code – Rust TUI coding agent with multi-provider support

**原文链接**: [https://github.com/vinhnx/VTCode](https://github.com/vinhnx/VTCode)

生成摘要时出错

---

## 79. MenteDB – open-source memory database for AI agents (Rust)

**原文标题**: MenteDB – open-source memory database for AI agents (Rust)

**原文链接**: [https://github.com/nambok/mentedb](https://github.com/nambok/mentedb)

生成摘要时出错

---

## 80. Your hex editor should color-code bytes

**原文标题**: Your hex editor should color-code bytes

**原文链接**: [https://simonomi.dev/blog/color-code-your-bytes/](https://simonomi.dev/blog/color-code-your-bytes/)

生成摘要时出错

---

## 81. 42 lost pages of the New Testament manuscript discovered

**原文标题**: 42 lost pages of the New Testament manuscript discovered

**原文链接**: [https://phys.org/news/2026-04-lost-pages-testament-manuscript.html](https://phys.org/news/2026-04-lost-pages-testament-manuscript.html)

生成摘要时出错

---

## 82. Could a Claude Code routine watch my finances?

**原文标题**: Could a Claude Code routine watch my finances?

**原文链接**: [https://driggsby.com/blog/claude-code-routine-watch-my-finances](https://driggsby.com/blog/claude-code-routine-watch-my-finances)

生成摘要时出错

---

## 83. Eurosky.social Account

**原文标题**: Eurosky.social Account

**原文链接**: [https://eurosky.tech/accounts/](https://eurosky.tech/accounts/)

生成摘要时出错

---

## 84. Qwen3.6-27B: Flagship-Level Coding in a 27B Dense Model

**原文标题**: Qwen3.6-27B: Flagship-Level Coding in a 27B Dense Model

**原文链接**: [https://qwen.ai/blog?id=qwen3.6-27b](https://qwen.ai/blog?id=qwen3.6-27b)

生成摘要时出错

---

## 85. Tariffs Raised Consumers' Prices, but the Refunds Go Only to Businesses

**原文标题**: Tariffs Raised Consumers' Prices, but the Refunds Go Only to Businesses

**原文链接**: [https://www.nytimes.com/2026/04/24/us/politics/companies-consumers-tariff-refunds.html](https://www.nytimes.com/2026/04/24/us/politics/companies-consumers-tariff-refunds.html)

生成摘要时出错

---

## 86. We found a stable Firefox identifier linking all your private Tor identities

**原文标题**: We found a stable Firefox identifier linking all your private Tor identities

**原文链接**: [https://fingerprint.com/blog/firefox-tor-indexeddb-privacy-vulnerability/](https://fingerprint.com/blog/firefox-tor-indexeddb-privacy-vulnerability/)

生成摘要时出错

---

## 87. Our newsroom AI policy

**原文标题**: Our newsroom AI policy

**原文链接**: [https://arstechnica.com/staff/2026/04/our-newsroom-ai-policy/](https://arstechnica.com/staff/2026/04/our-newsroom-ai-policy/)

生成摘要时出错

---

## 88. What physical ‘life force’ turns biology’s wheels?

**原文标题**: What physical ‘life force’ turns biology’s wheels?

**原文链接**: [https://www.quantamagazine.org/what-physical-life-force-turns-biologys-wheels-20260420/](https://www.quantamagazine.org/what-physical-life-force-turns-biologys-wheels-20260420/)

生成摘要时出错

---

## 89. Familiarity is the enemy: On why Enterprise systems have failed for 60 years

**原文标题**: Familiarity is the enemy: On why Enterprise systems have failed for 60 years

**原文链接**: [https://felixbarbalet.com/familiarity-is-the-enemy/](https://felixbarbalet.com/familiarity-is-the-enemy/)

生成摘要时出错

---

