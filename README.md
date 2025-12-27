# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-12-27.md)

*最后自动更新时间: 2025-12-27 17:45:33*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 2 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 3 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 4 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 5 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 6 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 7 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 8 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 9 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 10 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 11 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 12 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 13 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 14 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 15 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 16 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 17 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 18 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 19 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 20 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 21 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 22 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 23 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 24 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 25 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 26 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 27 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 28 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 29 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 30 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 31 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 32 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 33 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 34 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 35 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 36 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 37 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 38 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 39 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 40 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 41 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 42 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 43 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 44 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 45 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 46 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 47 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 48 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 49 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 50 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 51 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 52 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 53 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 54 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 55 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 56 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 57 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 58 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 59 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 60 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 61 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 62 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 63 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 64 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 65 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 66 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 67 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 68 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 69 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 70 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 71 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 72 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 73 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 74 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 75 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 76 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 77 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 78 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 79 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 80 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 81 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 82 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 83 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 84 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 85 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 86 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 87 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 88 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 89 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 90 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 91 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 92 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 93 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 94 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 95 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 96 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 97 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 98 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 99 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 100 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 101 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 102 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 103 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 104 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 105 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 106 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 107 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 108 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 109 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 110 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 111 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 112 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 113 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 114 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 115 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 116 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 117 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 118 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 119 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 120 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 121 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 122 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 123 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 124 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 125 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 126 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 127 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 128 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 129 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 130 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 131 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 132 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 133 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 134 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 135 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 136 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 137 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 138 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 139 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 140 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 141 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 142 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 143 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 144 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 145 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 146 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 147 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 148 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 149 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 150 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 151 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 152 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 153 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 154 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 155 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 156 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 157 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 158 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 159 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 160 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 161 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 162 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 163 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 164 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 165 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 166 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 167 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 168 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 169 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 170 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 171 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 172 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 173 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 174 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 175 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 176 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 177 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 178 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 179 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 180 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 181 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 182 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 183 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 184 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 185 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 186 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 187 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 188 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 189 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 190 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 191 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 192 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 193 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 194 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 195 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 196 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 197 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 198 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 199 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 200 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 201 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 202 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 203 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 204 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 205 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 206 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 207 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 208 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 209 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 210 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 211 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 212 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 213 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 214 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 215 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 216 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 217 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 218 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 219 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 220 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 221 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 222 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 223 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 224 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 225 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 226 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 227 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 228 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 229 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 230 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 231 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 232 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 233 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 234 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 235 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 236 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 237 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 238 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 239 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 240 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 241 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 242 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 243 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 244 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 245 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 246 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 247 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 248 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 249 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 250 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 251 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 252 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 253 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 254 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 255 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 256 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 257 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 258 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 259 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 260 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 261 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 262 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 263 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 264 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 265 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 266 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 267 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 268 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 269 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 270 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 271 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 272 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 273 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 274 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 275 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 276 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 277 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 278 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 279 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 280 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 281 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 282 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
