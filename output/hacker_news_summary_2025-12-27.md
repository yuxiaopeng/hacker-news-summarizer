# Hacker News 热门文章摘要 (2025-12-27)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 英伟达刚刚斥资200亿美元，收购了一家营收未达标75%的公司。

**原文标题**: Nvidia Just Paid $20B for a Company That Missed Its Revenue Target by 75%

**原文链接**: [https://blog.drjoshcsimmons.com/p/nvidia-just-paid-20-billion-for-a](https://blog.drjoshcsimmons.com/p/nvidia-just-paid-20-billion-for-a)

在这篇文章中，Josh C. Simmons博士指出，AI行业目前正处于一个“即将破裂的泡沫”之中，并将英伟达在2025年底收购芯片制造商Groq视为一个主要的预警信号。

据报道，英伟达为Groq支付了200亿美元。Groq专门从事语言处理单元（LPU）的研发，这种芯片的AI推理速度显著快于传统的GPU。Simmons强调了一个巨大的财务差异：就在收购前几个月，Groq的估值曾暴跌75%（从20亿美元降至5亿美元）。他将此次收购定性为旨在扼杀竞争并维持AI硬件垄断地位的“恐慌性购买”。

作者确定了威胁该行业的三个系统性问题：

1.  **能源危机：** AI数据中心正使美国电网面临巨大压力。据预测，十年内它们的耗电量将占到全美总用电量的9%。Simmons声称，科技巨头享受着优惠电价，这实际上是让普通消费者在为不断上涨的成本提供补贴。
2.  **供应商融资（“无限刷钱漏洞”）：** 英伟达被指控通过向OpenAI和CoreWeave等初创企业投资数十亿美元来人为抬高需求，这些企业随后利用这笔资金购买英伟达的芯片。这创造了一种循环经济，英伟达本质上是在“给客户钱，让他们回购自己的产品”。
3.  **OpenAI脆弱的财务状况：** 尽管在市场中处于领先地位，但OpenAI预计每年将烧掉750亿美元。为了实现盈利，该公司年收入需达到约2000亿美元——作者认为这是一个不切实际的天文数字。

Simmons总结称，英伟达的统治地位是建立在防御性收购和循环融资之上的。他警告称，这台“AI提款机”是不可持续的，正趋向于一场重大的市场回调。

---

## 2. 苹果发布开源模型，可将2D照片瞬间转换为3D视图。

**原文标题**: Apple releases open-source model that instantly turns 2D photos into 3D views

**原文链接**: [https://github.com/apple/ml-sharp](https://github.com/apple/ml-sharp)

苹果发布了 SHARP（不到一秒的高清晰度单目视图合成），这是一款开源模型，旨在将单张 2D 照片转换为照片级逼真的 3D 场景。

通过在单次前向传递中利用神经网络回归 3D 高斯表示的参数，SHARP 在标准 GPU 上实现了不到一秒的高分辨率视图合成。这代表了性能上的巨大飞跃，与之前的最先进模型相比，合成时间缩短了三个数量级。

**主要功能和技术亮点包括：**
*   **最先进的质量：** 该模型显著提高了图像保真度，相比之前的基准，LPIPS（学习感知图像块相似度）降低了 25–34%，DISTS 降低了 21–43%。
*   **度量表示：** 3D 输出保持绝对比例，允许在合成环境内进行精确的度量相机移动。
*   **零样本泛化：** SHARP 在各种数据集中表现出稳健的性能，无需特定的重新训练。
*   **兼容性：** 该工具输出与常用公共渲染器兼容的 3D 高斯泼溅 (.ply) 文件，并遵循 OpenCV 坐标约定。

该项目可通过命令行界面 (CLI) 获取，并支持在 CPU、CUDA 和 Apple Silicon (MPS) 上进行模型预测，不过视频轨迹渲染目前需要支持 CUDA 的 GPU。苹果已公开代码和模型权重，鼓励单目 3D 重建领域的进一步发展。

---

## 3. 796层

**原文标题**: Floor796

**原文链接**: [https://floor796.com/](https://floor796.com/)

**Floor796** 是一个宏大且持续进行的协作动画项目，描绘了一个虚构空间站中广阔且不断演进的楼层。该项目主要由艺术家 **085nd7** 创作和维护，以大型、无缝的等距视角绘图形式呈现，并托管在专门的网站上。

该项目最显著的特点是极其密集的**流行文化引用**。它包含数千个精心制作的动画角色、物品和场景，素材源自电影、电视、电子游戏、动漫和互联网迷因。其庞大的规模使其宛如数字动画版的《威力在哪里？》（Where’s Waldo），吸引观众花费数小时去识别那些熟悉的标志性形象——从主流超级英雄到小众邪典经典，应有尽有。

**该项目的主要特点包括：**

*   **交互性：** 用户可以在巨大的画布上平移和缩放。将鼠标悬停在特定角色或物体上，通常会弹出显示其名称及所属作品系列的浮窗。
*   **持续更新：** 这个“楼层”并非静止不变；创作者会频繁添加新区域、新角色和复杂的“彩蛋”，使其成为致敬全球媒体的鲜活作品。
*   **技术细节：** 尽管包含海量的动态元素，动画依然保持流畅。其美术风格维持了统一且高精度的 2D 美学，融合了动画历史上的多种时代风格。

总而言之，Floor796 是数字艺术领域的宏伟成就，也是一部现代神话的详尽档案，通过单一且互联的网页体验，展现了流行文化的广阔版图。

---

## 4. GPG 失效

**原文标题**: Gpg.fail

**原文链接**: [https://gpg.fail](https://gpg.fail)

名为 Gpg.fail 的页面目前仅作为一个简短的状态更新或占位符。其内容“brb, were on it!!!!”表明该网站暂时离线或正处于开发阶段。这一消息暗示管理员已知晓当前状况，并正积极致力于解决技术问题或更新网站内容。

---

## 5. Show HN: Ez FFmpeg – 用简单的英语进行视频编辑

**原文标题**: Show HN: Ez FFmpeg – Video editing in plain English

**原文链接**: [http://npmjs.com/package/ezff](http://npmjs.com/package/ezff)

生成摘要时出错

---

## 6. uv 为何如此之快

**原文标题**: How uv got so fast

**原文链接**: [https://nesbitt.io/2025/12/26/how-uv-got-so-fast.html](https://nesbitt.io/2025/12/26/how-uv-got-so-fast.html)

本文指出，`uv` 惊人的速度主要归功于战略性的设计选择和现代标准，而不仅仅是因为使用了 Rust 语言。虽然编程语言带来了性能提升，但真正的变革源于对现代化 Python 生态系统的利用以及对历史包袱的摒弃。

**核心速度驱动因素：**

*   **现代标准：** 历史上，`pip` 受困于“先有鸡还是先有蛋”的问题，必须执行 `setup.py` 才能发现依赖项。最近的 PEP 提案（518、517、621 和 658）引入了声明式元数据和服务器端 API。这使得 `uv` 能够通过解析 TOML 或通过 HTTP 获取元数据来解析依赖关系，而无需下载或执行软件包代码。
*   **策略性精简：** `uv` 的提速源于它“不做”的事情。它放弃了对旧格式（如 `.egg`）的支持，忽略 `pip.conf`，默认跳过字节码编译，并拒绝修改系统 Python。通过强制执行更严格的规范合规性并忽略防御性的“上限”Python 约束，它避免了复杂的回溯和回退逻辑。
*   **架构优化：** `uv` 的许多优势与语言无关。它使用 HTTP Range 请求仅拉取文件的必要部分，实现并行下载，并使用带有硬链接的全局缓存来避免冗余复制。它还采用了 PubGrub 算法，以实现更智能、更快速的依赖解析。
*   **Rust 的优势：** Rust 通过零拷贝反序列化、线程级并行（避开 Python 的 GIL）以及消除解释器启动开销，提供了最后一层优化。

**结论：**
`uv` 的成功在于基于现代假设的从零开始。尽管 `pip` 背负着十五年的向后兼容性和历史遗留边缘情况的负担，但 `uv` 通过利用静态元数据和高效的架构模式，优先处理 99% 使用场景下的“快速路径”，从而将性能放在首位。

---

## 7. 光纤熔接

**原文标题**: Splice a Fibre

**原文链接**: [https://react-networks-lib.rackout.net/fibre](https://react-networks-lib.rackout.net/fibre)

基于标题“光纤熔接”以及 React Networks 提供的片段，以下是此类技术指南中通常详述的过程简要总结：

**光纤熔接概述**

光纤熔接是将两根光缆连接在一起的专业工艺，旨在确保光信号的连续传递并最大限度地减少光损耗（衰减）。该过程通常分为两种方法：**熔融接续**和**机械接续**。

标准操作步骤包含以下四个关键环节：

1.  **准备工作：** 使用精密工具剥离外护套和聚合物保护涂层，暴露出裸玻璃包层。
2.  **切割：** 这是实现低损耗连接最关键的一步。使用精密光纤切割刀进行整齐的垂直切割，确保端面完全平整。
3.  **连接：**
    *   在**熔融接续**中，利用电弧熔化玻璃端头，并将它们永久熔合在一起。这是高性能网络的首选方法。
    *   在**机械接续**中，通过机械外壳将光纤对齐并固定，并使用折射率匹配膏来辅助光传输。
4.  **保护：** 熔接完成后，将脆弱的接头放入热缩保护套管或熔接盒中，以防止断裂并保护玻璃免受环境因素的影响。

由于提供的内容为占位符（“React Networks - 示例”），本总结反映了标题所示的光纤熔接标准技术工作流。

---

## 8. Show HN: Mysti – Claude, Codex, and Gemini debate your code, then synthesize

**原文标题**: Show HN: Mysti – Claude, Codex, and Gemini debate your code, then synthesize

**原文链接**: [https://github.com/DeepMyst/Mysti](https://github.com/DeepMyst/Mysti)

**Mysti** is a multi-agent AI coding extension for VS Code designed to outperform single-model tools by leveraging the collective intelligence of Claude Code, OpenAI Codex, and Google Gemini. 

The extension’s standout feature is **Brainstorm Mode**, which allows two different AI agents to collaborate on a single task. In "Full Mode," the agents debate, critique each other's logic, and catch edge cases before synthesizing a final, optimized solution. This approach is designed to eliminate the bottlenecks and "black box" limitations often found in single-provider tools like GitHub Copilot or Cursor.

**Key Features include:**
*   **16 Specialized Personas:** Users can tailor the AI’s behavior by selecting roles such as Architect, Debugger, Security Expert, or Performance Tuner.
*   **12 Toggleable Skills:** Modifiers like "Test-Driven," "Concise," and "Auto-Commit" allow for granular control over the AI’s output and workflow.
*   **Permission Controls:** Users can set access levels from "Read-only" to "Full-access," ensuring the AI only modifies files with explicit permission.
*   **No Extra Subscriptions:** Mysti integrates with the AI CLI tools users already own (e.g., `npm install -g @anthropic-ai/claude-code`), meaning there are no additional monthly fees to use the extension.

**Technical Requirements & Licensing:**
To use Mysti, users must have at least one supported CLI tool installed and authenticated. It is released under the **Business Source License 1.1**, making it free for personal, educational, and non-profit use, while requiring a separate license for commercial purposes. Mysti is available now via the VS Code Marketplace.

---

## 9. Intertapes – collection of found cassette tapes from different locations

**原文标题**: Intertapes – collection of found cassette tapes from different locations

**原文链接**: [https://intertapes.net/](https://intertapes.net/)

生成摘要时出错

---

## 10. We Automated Federal Retirements

**原文标题**: We Automated Federal Retirements

**原文链接**: [https://ndstudio.gov/posts/automating-federal-retirements](https://ndstudio.gov/posts/automating-federal-retirements)

生成摘要时出错

---

## 11. Mruby: Ruby for Embedded Systems

**原文标题**: Mruby: Ruby for Embedded Systems

**原文链接**: [https://github.com/mruby/mruby](https://github.com/mruby/mruby)

生成摘要时出错

---

## 12. This PNG shows a different version when loaded in Chrome than in Safari

**原文标题**: This PNG shows a different version when loaded in Chrome than in Safari

**原文链接**: [https://lr0.org/blog/p/pngchanges/](https://lr0.org/blog/p/pngchanges/)

生成摘要时出错

---

## 13. NMH BASIC

**原文标题**: NMH BASIC

**原文链接**: [https://t3x.org/nmhbasic/index.html](https://t3x.org/nmhbasic/index.html)

生成摘要时出错

---

## 14. A Century of Noether's Theorem

**原文标题**: A Century of Noether's Theorem

**原文链接**: [https://arxiv.org/abs/1902.01989](https://arxiv.org/abs/1902.01989)

生成摘要时出错

---

## 15. Detect memory leaks of C extensions with psutil and psleak

**原文标题**: Detect memory leaks of C extensions with psutil and psleak

**原文链接**: [https://gmpy.dev/blog/2025/psutil-heap-introspection-apis](https://gmpy.dev/blog/2025/psutil-heap-introspection-apis)

生成摘要时出错

---

## 16. Faster practical modular inversion

**原文标题**: Faster practical modular inversion

**原文链接**: [https://purplesyringa.moe/blog/faster-practical-modular-inversion/](https://purplesyringa.moe/blog/faster-practical-modular-inversion/)

生成摘要时出错

---

## 17. Exe.dev

**原文标题**: Exe.dev

**原文链接**: [https://exe.dev/](https://exe.dev/)

生成摘要时出错

---

## 18. Always bet on text (2014)

**原文标题**: Always bet on text (2014)

**原文链接**: [https://graydon2.dreamwidth.org/193447.html](https://graydon2.dreamwidth.org/193447.html)

生成摘要时出错

---

## 19. QNX Self-Hosted Developer Desktop

**原文标题**: QNX Self-Hosted Developer Desktop

**原文链接**: [https://devblog.qnx.com/qnx-self-hosted-developer-desktop-initial-release/](https://devblog.qnx.com/qnx-self-hosted-developer-desktop-initial-release/)

生成摘要时出错

---

## 20. The best things and stuff of 2025

**原文标题**: The best things and stuff of 2025

**原文链接**: [https://blog.fogus.me/2025/12/23/the-best-things-and-stuff-of-2025.html](https://blog.fogus.me/2025/12/23/the-best-things-and-stuff-of-2025.html)

生成摘要时出错

---

## 21. Langjam-Gamejam Devlog: Making a language, compiler, VM and 5 games in 52 hours

**原文标题**: Langjam-Gamejam Devlog: Making a language, compiler, VM and 5 games in 52 hours

**原文链接**: [https://github.com/Syn-Nine/gar-lang/blob/main/DEVLOG.md](https://github.com/Syn-Nine/gar-lang/blob/main/DEVLOG.md)

生成摘要时出错

---

## 22. Package managers keep using Git as a database, it never works out

**原文标题**: Package managers keep using Git as a database, it never works out

**原文链接**: [https://nesbitt.io/2025/12/24/package-managers-keep-using-git-as-a-database.html](https://nesbitt.io/2025/12/24/package-managers-keep-using-git-as-a-database.html)

生成摘要时出错

---

## 23. Publishing your work increases your luck

**原文标题**: Publishing your work increases your luck

**原文链接**: [https://github.com/readme/guides/publishing-your-work](https://github.com/readme/guides/publishing-your-work)

生成摘要时出错

---

## 24. New York to require social media platforms to display mental health warnings

**原文标题**: New York to require social media platforms to display mental health warnings

**原文链接**: [https://www.reuters.com/legal/litigation/new-york-require-social-media-platforms-display-mental-health-warnings-2025-12-26/](https://www.reuters.com/legal/litigation/new-york-require-social-media-platforms-display-mental-health-warnings-2025-12-26/)

生成摘要时出错

---

## 25. Verdichtung

**原文标题**: Verdichtung

**原文链接**: [https://alexeygy.github.io/blog/verdichtung/](https://alexeygy.github.io/blog/verdichtung/)

生成摘要时出错

---

## 26. More dynamic cronjobs

**原文标题**: More dynamic cronjobs

**原文链接**: [https://george.mand.is/2025/09/more-dynamic-cronjobs/](https://george.mand.is/2025/09/more-dynamic-cronjobs/)

生成摘要时出错

---

## 27. Show HN: Witr – Explain why a process is running on your Linux system

**原文标题**: Show HN: Witr – Explain why a process is running on your Linux system

**原文链接**: [https://github.com/pranshuparmar/witr](https://github.com/pranshuparmar/witr)

生成摘要时出错

---

## 28. Inside the proton, the ‘most complicated thing you could possibly imagine’ (2022)

**原文标题**: Inside the proton, the ‘most complicated thing you could possibly imagine’ (2022)

**原文链接**: [https://www.quantamagazine.org/inside-the-proton-the-most-complicated-thing-imaginable-20221019/](https://www.quantamagazine.org/inside-the-proton-the-most-complicated-thing-imaginable-20221019/)

生成摘要时出错

---

## 29. How Lewis Carroll computed determinants (2023)

**原文标题**: How Lewis Carroll computed determinants (2023)

**原文链接**: [https://www.johndcook.com/blog/2023/07/10/lewis-carroll-determinants/](https://www.johndcook.com/blog/2023/07/10/lewis-carroll-determinants/)

生成摘要时出错

---

## 30. How Lewis Carroll computed determinants (2023)

**原文标题**: How Lewis Carroll computed determinants (2023)

**原文链接**: [https://www.johndcook.com/blog/2023/07/10/lewis-carroll-determinants/](https://www.johndcook.com/blog/2023/07/10/lewis-carroll-determinants/)

生成摘要时出错

---

## 31. One million (small web) screenshots

**原文标题**: One million (small web) screenshots

**原文链接**: [https://nry.me/posts/2025-10-09/small-web-screenshots/](https://nry.me/posts/2025-10-09/small-web-screenshots/)

生成摘要时出错

---

## 32. Experts explore new mushroom which causes fairytale-like hallucinations

**原文标题**: Experts explore new mushroom which causes fairytale-like hallucinations

**原文链接**: [https://nhmu.utah.edu/articles/experts-explore-new-mushroom-which-causes-fairytale-hallucinations](https://nhmu.utah.edu/articles/experts-explore-new-mushroom-which-causes-fairytale-hallucinations)

生成摘要时出错

---

## 33. An exploration of playing three generations of windows games on macOS

**原文标题**: An exploration of playing three generations of windows games on macOS

**原文链接**: [https://carette.xyz/posts/deep_dive_into_crossover/](https://carette.xyz/posts/deep_dive_into_crossover/)

生成摘要时出错

---

## 34. Show HN: An immutable ostree-based Arch Linux image

**原文标题**: Show HN: An immutable ostree-based Arch Linux image

**原文链接**: [https://github.com/myyc/vyy](https://github.com/myyc/vyy)

生成摘要时出错

---

## 35. Getting Started with Playdate on Ubuntu

**原文标题**: Getting Started with Playdate on Ubuntu

**原文链接**: [https://sethmlarson.dev/getting-started-with-playdate-on-ubuntu](https://sethmlarson.dev/getting-started-with-playdate-on-ubuntu)

生成摘要时出错

---

## 36. Researchers develop a camera that can focus on different distances at once

**原文标题**: Researchers develop a camera that can focus on different distances at once

**原文链接**: [https://engineering.cmu.edu/news-events/news/2025/12/19-perfect-shot.html](https://engineering.cmu.edu/news-events/news/2025/12/19-perfect-shot.html)

生成摘要时出错

---

## 37. SIMD City: Auto-Vectorisation

**原文标题**: SIMD City: Auto-Vectorisation

**原文链接**: [https://xania.org/202512/20-simd-city](https://xania.org/202512/20-simd-city)

生成摘要时出错

---

## 38. LearnixOS

**原文标题**: LearnixOS

**原文链接**: [https://www.learnix-os.com](https://www.learnix-os.com)

生成摘要时出错

---

## 39. Moravec's Paradox and the Robot Olympics

**原文标题**: Moravec's Paradox and the Robot Olympics

**原文链接**: [https://www.physicalintelligence.company/blog/olympics](https://www.physicalintelligence.company/blog/olympics)

生成摘要时出错

---

## 40. Show HN: Xcc700: Self-hosting mini C compiler for ESP32 (Xtensa) in 700 lines

**原文标题**: Show HN: Xcc700: Self-hosting mini C compiler for ESP32 (Xtensa) in 700 lines

**原文链接**: [https://github.com/valdanylchuk/xcc700](https://github.com/valdanylchuk/xcc700)

生成摘要时出错

---

## 41. AI Police Reports: Year in Review

**原文标题**: AI Police Reports: Year in Review

**原文链接**: [https://www.eff.org/deeplinks/2025/12/ai-police-reports-year-review](https://www.eff.org/deeplinks/2025/12/ai-police-reports-year-review)

生成摘要时出错

---

## 42. So I started cloning the Wii U gamepad [video]

**原文标题**: So I started cloning the Wii U gamepad [video]

**原文链接**: [https://www.youtube.com/watch?v=jlbcKuDEBw8](https://www.youtube.com/watch?v=jlbcKuDEBw8)

生成摘要时出错

---

## 43. Why broadband quality matters more than speed

**原文标题**: Why broadband quality matters more than speed

**原文链接**: [https://www.thinkbroadband.com/news/why-broadband-quality-matters-more-than-speed](https://www.thinkbroadband.com/news/why-broadband-quality-matters-more-than-speed)

生成摘要时出错

---

## 44. What happened to all the gold Spain got from the New World? (1985)

**原文标题**: What happened to all the gold Spain got from the New World? (1985)

**原文链接**: [https://www.straightdope.com/21341789/what-happened-to-all-the-gold-spain-got-from-the-new-world](https://www.straightdope.com/21341789/what-happened-to-all-the-gold-spain-got-from-the-new-world)

生成摘要时出错

---

## 45. My insulin pump controller uses the Linux kernel. It also violates the GPL

**原文标题**: My insulin pump controller uses the Linux kernel. It also violates the GPL

**原文链接**: [https://old.reddit.com/r/linux/comments/1puojsr/the_device_that_controls_my_insulin_pump_uses_the/](https://old.reddit.com/r/linux/comments/1puojsr/the_device_that_controls_my_insulin_pump_uses_the/)

生成摘要时出错

---

## 46. Drawing with zero-width characters

**原文标题**: Drawing with zero-width characters

**原文链接**: [https://zw.swerdlow.dev](https://zw.swerdlow.dev)

生成摘要时出错

---

## 47. The Algebra of Loans in Rust

**原文标题**: The Algebra of Loans in Rust

**原文链接**: [https://nadrieril.github.io/blog/2025/12/21/the-algebra-of-loans-in-rust.html](https://nadrieril.github.io/blog/2025/12/21/the-algebra-of-loans-in-rust.html)

生成摘要时出错

---

## 48. Some Junk Theorems in Lean

**原文标题**: Some Junk Theorems in Lean

**原文链接**: [https://github.com/James-Hanson/junk-theorems-in-lean](https://github.com/James-Hanson/junk-theorems-in-lean)

生成摘要时出错

---

## 49. MongoBleed

**原文标题**: MongoBleed

**原文链接**: [https://github.com/joe-desimone/mongobleed/blob/main/mongobleed.py](https://github.com/joe-desimone/mongobleed/blob/main/mongobleed.py)

生成摘要时出错

---

## 50. T-Ruby is Ruby with syntax for types

**原文标题**: T-Ruby is Ruby with syntax for types

**原文链接**: [https://type-ruby.github.io/](https://type-ruby.github.io/)

生成摘要时出错

---

## 51. OrangePi 6 Plus Review: The New Frontier for ARM64 SBC Performance

**原文标题**: OrangePi 6 Plus Review: The New Frontier for ARM64 SBC Performance

**原文链接**: [https://boilingsteam.com/orange-pi-6-plus-review/](https://boilingsteam.com/orange-pi-6-plus-review/)

生成摘要时出错

---

## 52. Unix "find" expressions compiled to bytecode

**原文标题**: Unix "find" expressions compiled to bytecode

**原文链接**: [https://nullprogram.com/blog/2025/12/23/](https://nullprogram.com/blog/2025/12/23/)

生成摘要时出错

---

## 53. FFmpeg has issued a DMCA takedown on GitHub

**原文标题**: FFmpeg has issued a DMCA takedown on GitHub

**原文链接**: [https://twitter.com/FFmpeg/status/2004599109559496984](https://twitter.com/FFmpeg/status/2004599109559496984)

生成摘要时出错

---

## 54. Toys with the highest play-time and lowest clean-up-time

**原文标题**: Toys with the highest play-time and lowest clean-up-time

**原文链接**: [https://joannabregan.substack.com/p/toys-with-the-highest-play-time-and](https://joannabregan.substack.com/p/toys-with-the-highest-play-time-and)

生成摘要时出错

---

## 55. Rob Pike goes nuclear over GenAI

**原文标题**: Rob Pike goes nuclear over GenAI

**原文链接**: [https://skyview.social/?url=https%3A%2F%2Fbsky.app%2Fprofile%2Frobpike.io%2Fpost%2F3matwg6w3ic2s&viewtype=tree](https://skyview.social/?url=https%3A%2F%2Fbsky.app%2Fprofile%2Frobpike.io%2Fpost%2F3matwg6w3ic2s&viewtype=tree)

生成摘要时出错

---

## 56. Stimulant medications affect arousal and reward, not attention networks

**原文标题**: Stimulant medications affect arousal and reward, not attention networks

**原文链接**: [https://www.cell.com/cell/fulltext/S0092-8674(25)01373-X](https://www.cell.com/cell/fulltext/S0092-8674(25)01373-X)

生成摘要时出错

---

## 57. Sandbox: Run untrusted AI code safely, fast

**原文标题**: Sandbox: Run untrusted AI code safely, fast

**原文链接**: [https://github.com/PwnFunction/sandbox](https://github.com/PwnFunction/sandbox)

生成摘要时出错

---

## 58. CorsixTH – An open source clone of Theme Hospital

**原文标题**: CorsixTH – An open source clone of Theme Hospital

**原文链接**: [https://corsixth.com](https://corsixth.com)

生成摘要时出错

---

## 59. What on earth is Kubernetes? (a beginners intro)

**原文标题**: What on earth is Kubernetes? (a beginners intro)

**原文链接**: [https://kylejeong.com/blog/what-is-kubernetes](https://kylejeong.com/blog/what-is-kubernetes)

生成摘要时出错

---

## 60. Gaussian Splatting 3 Ways

**原文标题**: Gaussian Splatting 3 Ways

**原文链接**: [https://github.com/NullandKale/NullSplats](https://github.com/NullandKale/NullSplats)

生成摘要时出错

---

## 61. Overlooked No More: Inge Lehmann, Who Discovered the Earth's Inner Core

**原文标题**: Overlooked No More: Inge Lehmann, Who Discovered the Earth's Inner Core

**原文链接**: [https://www.nytimes.com/2025/12/20/obituaries/inge-lehmann-overlooked.html](https://www.nytimes.com/2025/12/20/obituaries/inge-lehmann-overlooked.html)

生成摘要时出错

---

## 62. Fabrice Bellard Releases MicroQuickJS

**原文标题**: Fabrice Bellard Releases MicroQuickJS

**原文链接**: [https://github.com/bellard/mquickjs/blob/main/README.md](https://github.com/bellard/mquickjs/blob/main/README.md)

生成摘要时出错

---

## 63. Parasites plagued Roman soldiers at Hadrian's Wall

**原文标题**: Parasites plagued Roman soldiers at Hadrian's Wall

**原文链接**: [https://arstechnica.com/science/2025/12/study-roman-soldiers-battled-parasites-at-hadrians-wall/](https://arstechnica.com/science/2025/12/study-roman-soldiers-battled-parasites-at-hadrians-wall/)

生成摘要时出错

---

## 64. Maybe the default settings are too high

**原文标题**: Maybe the default settings are too high

**原文链接**: [https://www.raptitude.com/2025/12/maybe-the-default-settings-are-too-high/](https://www.raptitude.com/2025/12/maybe-the-default-settings-are-too-high/)

生成摘要时出错

---

## 65. MiniMax M2.1: Built for Real-World Complex Tasks, Multi-Language Programming

**原文标题**: MiniMax M2.1: Built for Real-World Complex Tasks, Multi-Language Programming

**原文链接**: [https://www.minimaxi.com/news/minimax-m21](https://www.minimaxi.com/news/minimax-m21)

生成摘要时出错

---

## 66. Migrating my web analytics from Matomo to Umami

**原文标题**: Migrating my web analytics from Matomo to Umami

**原文链接**: [https://stanislas.blog/2025/12/migrating-matomo-to-umami-web-analytics/](https://stanislas.blog/2025/12/migrating-matomo-to-umami-web-analytics/)

生成摘要时出错

---

## 67. Show HN: AutoLISP interpreter in Rust/WASM – a CAD workflow invented 33 yrs ago

**原文标题**: Show HN: AutoLISP interpreter in Rust/WASM – a CAD workflow invented 33 yrs ago

**原文链接**: [https://acadlisp.de/noscript.html](https://acadlisp.de/noscript.html)

生成摘要时出错

---

## 68. Perfect Aircrete, Kitchen Ingredients [video]

**原文标题**: Perfect Aircrete, Kitchen Ingredients [video]

**原文链接**: [https://www.youtube.com/watch?v=z4_GxPHwqkA](https://www.youtube.com/watch?v=z4_GxPHwqkA)

生成摘要时出错

---

## 69. Geometric Algorithms for Translucency Sorting in Minecraft [pdf]

**原文标题**: Geometric Algorithms for Translucency Sorting in Minecraft [pdf]

**原文链接**: [https://douira.dev/assets/document/douira-master-thesis.pdf](https://douira.dev/assets/document/douira-master-thesis.pdf)

生成摘要时出错

---

## 70. An 11-qubit atom processor in silicon with all fidelities from 99.10% to 99.99%

**原文标题**: An 11-qubit atom processor in silicon with all fidelities from 99.10% to 99.99%

**原文链接**: [https://www.nature.com/articles/s41586-025-09827-w](https://www.nature.com/articles/s41586-025-09827-w)

生成摘要时出错

---

## 71. Tiled Art

**原文标题**: Tiled Art

**原文链接**: [https://tiled.art/en/home/?id=SilverAndGold](https://tiled.art/en/home/?id=SilverAndGold)

生成摘要时出错

---

## 72. -tucky (2023)

**原文标题**: -tucky (2023)

**原文链接**: [https://languagelog.ldc.upenn.edu/nll/?p=58650](https://languagelog.ldc.upenn.edu/nll/?p=58650)

生成摘要时出错

---

## 73. Building an AI agent inside a 7-year-old Rails monolith

**原文标题**: Building an AI agent inside a 7-year-old Rails monolith

**原文链接**: [https://catalinionescu.dev/ai-agent/building-ai-agent-part-1/](https://catalinionescu.dev/ai-agent/building-ai-agent-part-1/)

生成摘要时出错

---

## 74. Mostlymatter: A fork of Mattermost by Framasoft

**原文标题**: Mostlymatter: A fork of Mattermost by Framasoft

**原文链接**: [https://packages.framasoft.org/projects/mostlymatter/](https://packages.framasoft.org/projects/mostlymatter/)

生成摘要时出错

---

## 75. Joan Didion and Kurt Vonnegut had something to say. We have it on tape

**原文标题**: Joan Didion and Kurt Vonnegut had something to say. We have it on tape

**原文链接**: [https://www.nytimes.com/2025/12/19/books/james-baldwin-joan-didion-92ny-recordings.html](https://www.nytimes.com/2025/12/19/books/james-baldwin-joan-didion-92ny-recordings.html)

生成摘要时出错

---

## 76. How to Reproduce This Book with LaTeX

**原文标题**: How to Reproduce This Book with LaTeX

**原文链接**: [https://github.com/BenjaminGor/Latex_Notes_Tutorial](https://github.com/BenjaminGor/Latex_Notes_Tutorial)

生成摘要时出错

---

## 77. Hardware Touch, Stronger SSH

**原文标题**: Hardware Touch, Stronger SSH

**原文链接**: [https://www.ubicloud.com/blog/hardware-touch-stronger-ssh](https://www.ubicloud.com/blog/hardware-touch-stronger-ssh)

生成摘要时出错

---

## 78. All my senses are being tortured simultaneously

**原文标题**: All my senses are being tortured simultaneously

**原文链接**: [https://news.lettersofnote.com/p/all-my-senses-are-being-tortured](https://news.lettersofnote.com/p/all-my-senses-are-being-tortured)

生成摘要时出错

---

## 79. I'm a laptop weirdo and that's why I like my new Framework 13

**原文标题**: I'm a laptop weirdo and that's why I like my new Framework 13

**原文链接**: [https://blog.matthewbrunelle.com/im-a-laptop-weirdo-and-thats-why-i-like-my-new-framework-13/](https://blog.matthewbrunelle.com/im-a-laptop-weirdo-and-thats-why-i-like-my-new-framework-13/)

生成摘要时出错

---

## 80. A Proclamation Regarding the Restoration of the Dash

**原文标题**: A Proclamation Regarding the Restoration of the Dash

**原文链接**: [https://blog.nawaz.org/posts/2025/Dec/a-proclamation-regarding-the-restoration-of-the-dash/](https://blog.nawaz.org/posts/2025/Dec/a-proclamation-regarding-the-restoration-of-the-dash/)

生成摘要时出错

---

## 81. Grok and the Naked King: The Ultimate Argument Against AI Alignment

**原文标题**: Grok and the Naked King: The Ultimate Argument Against AI Alignment

**原文链接**: [https://ibrahimcesar.cloud/blog/grok-and-the-naked-king/](https://ibrahimcesar.cloud/blog/grok-and-the-naked-king/)

生成摘要时出错

---

## 82. Simple 3D Packing

**原文标题**: Simple 3D Packing

**原文链接**: [https://github.com/Vrroom/psacking](https://github.com/Vrroom/psacking)

生成摘要时出错

---

## 83. Codex vs. Claude Code (today)

**原文标题**: Codex vs. Claude Code (today)

**原文链接**: [https://build.ms/2025/12/22/codex-vs-claude-code-today/](https://build.ms/2025/12/22/codex-vs-claude-code-today/)

生成摘要时出错

---

## 84. A Knapsack Public Key Cryptosystem Based on Arithmetic in Finite Fields (1988) [pdf]

**原文标题**: A Knapsack Public Key Cryptosystem Based on Arithmetic in Finite Fields (1988) [pdf]

**原文链接**: [https://people.csail.mit.edu/rivest/pubs/CR88.pdf](https://people.csail.mit.edu/rivest/pubs/CR88.pdf)

生成摘要时出错

---

## 85. The Death of the Draftsman

**原文标题**: The Death of the Draftsman

**原文链接**: [https://tecnetinc.com/The%20Death%20of%20the%20Draftsman.html](https://tecnetinc.com/The%20Death%20of%20the%20Draftsman.html)

生成摘要时出错

---

## 86. Tachyon: High frequency statistical sampling profiler

**原文标题**: Tachyon: High frequency statistical sampling profiler

**原文链接**: [https://docs.python.org/3.15/library/profiling.sampling.html](https://docs.python.org/3.15/library/profiling.sampling.html)

生成摘要时出错

---

## 87. Tachyon: High frequency statistical sampling profiler

**原文标题**: Tachyon: High frequency statistical sampling profiler

**原文链接**: [https://docs.python.org/3.15/library/profiling.sampling.html](https://docs.python.org/3.15/library/profiling.sampling.html)

生成摘要时出错

---

## 88. High school student discovers 1.5M potential new astronomical objects

**原文标题**: High school student discovers 1.5M potential new astronomical objects

**原文链接**: [https://www.smithsonianmag.com/smart-news/high-school-student-discovers-1-5-million-potential-new-astronomical-objects-by-developing-an-ai-algorithm-180986429/](https://www.smithsonianmag.com/smart-news/high-school-student-discovers-1-5-million-potential-new-astronomical-objects-by-developing-an-ai-algorithm-180986429/)

生成摘要时出错

---

## 89. The First Web Server

**原文标题**: The First Web Server

**原文链接**: [https://dfarq.homeip.net/the-first-web-server/](https://dfarq.homeip.net/the-first-web-server/)

生成摘要时出错

---

## 90. ZJIT is now available in Ruby 4.0

**原文标题**: ZJIT is now available in Ruby 4.0

**原文链接**: [https://railsatscale.com/2025-12-24-launch-zjit/](https://railsatscale.com/2025-12-24-launch-zjit/)

生成摘要时出错

---

## 91. TurboDiffusion: 100–200× Acceleration for Video Diffusion Models

**原文标题**: TurboDiffusion: 100–200× Acceleration for Video Diffusion Models

**原文链接**: [https://github.com/thu-ml/TurboDiffusion](https://github.com/thu-ml/TurboDiffusion)

生成摘要时出错

---

## 92. Python 3.15’s interpreter for Windows x86-64 should hopefully be 15% faster

**原文标题**: Python 3.15’s interpreter for Windows x86-64 should hopefully be 15% faster

**原文链接**: [https://fidget-spinner.github.io/posts/no-longer-sorry.html](https://fidget-spinner.github.io/posts/no-longer-sorry.html)

生成摘要时出错

---

## 93. The entire New Yorker archive is now digitized

**原文标题**: The entire New Yorker archive is now digitized

**原文链接**: [https://www.newyorker.com/news/press-room/the-entire-new-yorker-archive-is-now-fully-digitized](https://www.newyorker.com/news/press-room/the-entire-new-yorker-archive-is-now-fully-digitized)

生成摘要时出错

---

## 94. Seven Diabetes Patients Die Due to Undisclosed Bug in Abbott's Glucose Monitors

**原文标题**: Seven Diabetes Patients Die Due to Undisclosed Bug in Abbott's Glucose Monitors

**原文链接**: [https://sfconservancy.org/blog/2025/dec/23/seven-abbott-freestyle-libre-cgm-patients-dead/](https://sfconservancy.org/blog/2025/dec/23/seven-abbott-freestyle-libre-cgm-patients-dead/)

生成摘要时出错

---

## 95. Lessons from a year of Postgres CDC in production

**原文标题**: Lessons from a year of Postgres CDC in production

**原文链接**: [https://clickhouse.com/blog/postgres-cdc-year-in-review-2025](https://clickhouse.com/blog/postgres-cdc-year-in-review-2025)

生成摘要时出错

---

## 96. Show HN: Gaming Couch – a local multiplayer party game platform for 8 players

**原文标题**: Show HN: Gaming Couch – a local multiplayer party game platform for 8 players

**原文链接**: [https://gamingcouch.com](https://gamingcouch.com)

生成摘要时出错

---

## 97. Bedlam Cube Solved (ALL 19,186 solutions)

**原文标题**: Bedlam Cube Solved (ALL 19,186 solutions)

**原文链接**: [http://scottkurowski.com/BedlamCube/](http://scottkurowski.com/BedlamCube/)

生成摘要时出错

---

## 98. Former ULA President and CEO Tory Bruno Joins Blue Origin

**原文标题**: Former ULA President and CEO Tory Bruno Joins Blue Origin

**原文链接**: [https://spaceflightnow.com/2025/12/26/former-ula-president-and-ceo-tory-bruno-joins-blue-origin/](https://spaceflightnow.com/2025/12/26/former-ula-president-and-ceo-tory-bruno-joins-blue-origin/)

生成摘要时出错

---

## 99. Show HN: Lamp Carousel – DIY kinetic sculpture powered by lamp heat (2024)

**原文标题**: Show HN: Lamp Carousel – DIY kinetic sculpture powered by lamp heat (2024)

**原文链接**: [https://evan.widloski.com/posts/spinners/](https://evan.widloski.com/posts/spinners/)

生成摘要时出错

---

## 100. Ultimate-Linux: Userspace for Linux in Pure JavaScript

**原文标题**: Ultimate-Linux: Userspace for Linux in Pure JavaScript

**原文链接**: [https://github.com/popovicu/ultimate-linux](https://github.com/popovicu/ultimate-linux)

生成摘要时出错

---

