# Hacker News 热门文章摘要 (2026-06-09)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Claude 寓言 5

**原文标题**: Claude Fable 5

**原文链接**: [https://www.anthropic.com/news/claude-fable-5-mythos-5](https://www.anthropic.com/news/claude-fable-5-mythos-5)

2026年6月9日，Anthropic 宣布推出 **Claude Fable 5** 和 **Claude Mythos 5**。这两款全新的“神话级”（Mythos-class）模型代表了 AI 能力的尖端跨越。Fable 5 专为通用场景设计，并集成了安全特性；而 Mythos 5 则是解除安全限制的专业版本，初期通过“透翅蝶计划”（Project Glasswing）向政府及网络安全合作伙伴开放。

**核心能力：**
*   **软件工程：** Fable 5 展现出高度的自主性，能够将耗时数月的代码库迁移任务缩短至一天内完成。
*   **科学研究：** Mythos 5 已展现出设计新型蛋白质复合物、生成原创生物学假设以及进行自主基因组研究的能力。
*   **视觉与记忆：** 该模型可以执行复杂的视觉任务，例如根据截图重建 Web 应用，或仅依靠原始视觉输入玩《宝可梦：火红》。其改进后的记忆力可确保在处理数百万个 Token 时保持性能一致。
*   **知识工作：** Fable 5 在金融和分析基准测试中处于领先地位，展现出“资深研究科学家级别”的推理能力。

**安全与定价：**
为了应对网络安全和生物领域的风险，Fable 5 采用了“回退”（fallback）系统。如果查询被标记为高风险，系统会自动将任务重定向至较旧的 **Claude Opus 4.8**。这一安全机制在不到 5% 的会话中触发，确保了强大性能与安全性之间的平衡。

该系列模型的定价为每百万输入 Token 10 美元，每百万输出 Token 50 美元——与之前的“Mythos”预览版相比，成本显著降低。此次发布标志着 AI 从标准助手向高度自主的智能体系统转变的重要里程碑。

---

## 2. 脱欧十年：经济

**原文标题**: Brexit Ten Years On: The Economy

**原文链接**: [https://ukandeu.ac.uk/brexit-ten-years-on-the-economy/](https://ukandeu.ac.uk/brexit-ten-years-on-the-economy/)

在英国脱欧公投近十年后，乔纳森·波特斯（Jonathan Portes）教授指出，脱欧在结构上削弱了英国经济，其影响表现为“渐进且累积的拖累”，而非突然的崩溃。核心的权衡——即以放弃与欧盟的深度融合来换取国内自主权——导致英国经济规模比未脱欧的情形缩小了几个百分点。

重点影响包括：

*   **贸易**：虽然《贸易与合作协定》避免了关税，但却引入了显著的非关税壁垒。据估计，货物贸易比反事实情形低10-15%，小企业受行政成本的影响尤为严重。尽管高价值数字服务保持了韧性，但金融等受监管行业已失去大量市场准入。
*   **生产力与投资**：脱欧的不确定性和贸易强度的下降抑制了投资，加剧了英国长期的生产力危机。预算责任办公室（OBR）估计，长期生产力将受损约4%。
*   **移民**：欧盟人员自由流动的终结导致酒店餐饮业和农业等部门出现劳动力短缺。然而，非欧盟移民的激增在总量上弥补了这些缺口。虽然这支撑了GDP总量，但对人均GDP的影响仍不明确。
*   **自主权**：监管差异化和新的非欧盟贸易协定带来的经济收益十分有限，普遍认为不足以抵消退出单一市场的成本。

波特斯总结称，尽管英国已经适应并避免了传统意义上的经济危机，但关于持续存在的“脱欧惩罚”的证据正日益确凿。即使是像2025年《共同谅解》这样对双边关系的递进式改善，也无法复制单一市场的经济价值。脱欧留下的主要遗产是一个贸易强度降低、投资减少、且应对原有财政和地区挑战能力削弱的经济体。

---

## 3. 像1993年那样制作图形

**原文标题**: Making Graphics Like it's 1993

**原文链接**: [https://staniks.github.io/articles/catlantean-3d-blog-1/](https://staniks.github.io/articles/catlantean-3d-blog-1/)

《像 1993 年那样制作图像》（Making Graphics Like it’s 1993）详细记录了《Catlantean 3D》的开发过程。这是一款即将推出的第一人称射击游戏，完全基于 90 年代早期的技术限制从零开始构建。开发者自设的规则包括 320x240 的分辨率、固定的 256 色调色板，以及自定义构建的渲染与音频系统，坚决摒弃现代引擎和“AI 垃圾”。

核心挑战在于基于调色板的渲染。为了在没有现代着色器的情况下模拟光照，开发者使用了预计算的“颜色映射（colormap）”矩阵。这使得引擎能够根据与玩家的距离，以 $O(1)$ 的复杂度查找更暗的颜色变体。通过利用 Oklab 色彩空间和“色相偏移”，开发者确保光照过渡在感知上自然且生动，而非显得平淡或灰暗。

素材创作分为三个主要工作流：
1. **预渲染精灵：** 为了节省制作复杂动画的时间，开发者在 Blender 中进行建模和绑定。随后通过专门的 Python 脚本将其渲染为 2D 纹理，并应用调色板量化以保持复古美感。
2. **手绘素材：** 诸如状态栏头像和拾取物品等需要“灵魂”和高辨识度的元素，均采用逐像素手绘。作者指出，手绘对于在低分辨率下传达情感和保持清晰度至关重要。
3. **程序化纹理：** 通过脚本组合手绘艺术，从而高效生成环境纹理。

作者强调，“一致的像素缩放”——即严格保持每世界单位 64 像素的比例——对于视觉协调感至关重要。该项目最终认为，90 年代图像的“锐利感”源于技术限制下被迫做出的刻意选择。通过在这些界限内工作，开发者旨在打造一种精致且具有确定性的体验，捕捉 VGA 时代最真实的神韵。

---

## 4. 与 Mythos 合作的体验

**原文标题**: What it feels like to work with Mythos

**原文链接**: [https://www.oneusefulthing.org/p/what-it-feels-like-to-work-with-mythos](https://www.oneusefulthing.org/p/what-it-feels-like-to-work-with-mythos)

在这篇文章中，Ethan Mollick 评测了首个“神话级”（Mythos-class）AI 模型 **Claude 5 Fable**。他将其描述为能力的重大飞跃，从根本上改变了人与 AI 的关系。

**核心能力与表现**
Fable 能够连续数小时执行复杂且长达数页的任务规格，表现远超以往模型。Mollick 强调了它自主处理“严肃”项目的能力，例如：
*   **自主研究：** 通过启动子代理研究了 2,200 多份飞行时刻表、铁路数据和学术论文，创建出一张精密的等时线图。
*   **软件开发：** 构建了名为“Concord”的复杂数据分析工具，用于校准人类与 AI 的判断——该项目由 AI 耗时 9.5 小时独立完成。
*   **创意工程：** 在不使用外部图像素材的情况下，纯粹利用数学和代码生成游戏。

**从“巫师”到“赞助人”的转变**
Mollick 的核心论点是用户的角色发生了转变。以往的 AI 需要人类进行“引导”（即巫师模式），而与 Fable 合作的感觉更像是成为一名**赞助人**。用户提供简报并委托任务，AI 则像是一个“工作室”，自行管理工作流，启动对抗性代理来检查工作，并做出成千上万个自主微决策。

**局限性与担忧**
尽管功能强大，Fable 也有明显的缺点：
*   **黑箱化：** 由于 AI 会自主运行数小时，其决策过程对用户是不可见的。
*   **高昂成本：** 其价格是之前模型的两倍，且 Token 消耗极快。
*   **严格的护栏：** 该模型具有极其敏感的安全触发机制，经常会因此回退到性能较低的版本。

**结论**
Mollick 总结道，随着 AI 从工具转变为协作伙伴，人类工作的重点正在从**关注过程转向关注结果**。我们不再是具体工作的执行者，而是任务的下达者和结果的评审者。

---

## 5. 一颗巨星可能在一次极其罕见的爆炸中自我毁灭。

**原文标题**: A giant star may have destroyed itself in one of the rarest explosions

**原文链接**: [https://phys.org/news/2026-05-giant-star-destroyed-universe-rarest.html](https://phys.org/news/2026-05-giant-star-destroyed-universe-rarest.html)

无法访问文章链接。

---

## 6. 微软开源工具遭到入侵，旨在窃取 AI 开发者的密码。

**原文标题**: Microsoft's open source tools were hacked to steal passwords of AI developers

**原文链接**: [https://techcrunch.com/2026/06/08/microsofts-open-source-tools-were-hacked-to-steal-passwords-of-ai-developers/](https://techcrunch.com/2026/06/08/microsofts-open-source-tools-were-hacked-to-steal-passwords-of-ai-developers/)

微软已在 GitHub 上禁用了至少 70 个开源项目，此前黑客成功在代码中植入了窃取密码的恶意软件。此次攻击专门针对 AI 开发者使用的工具，包括与 Microsoft Azure、VS Code 相关的工具，以及针对 Claude 和 Gemini 等 AI 平台的命令行界面。

该恶意软件旨在开发者使用受损工具时外泄密码和敏感凭据。虽然受影响的用户总数尚不明确，但微软证实已通知了“少数”可能下载了恶意内容的客户。在经过安全审查后，部分存储库已恢复，但随着调查的持续，其他存储库仍处于离线状态。

最早发现此次黑客攻击的 Cloudsmith 和 OpenSourceMalware 安全专家指出，此次事件似乎是对 Durable Task 项目的“再次入侵”，该项目此前曾在 5 月中旬被攻破。这表明最初的威胁可能并未被完全清除，或者有新的漏洞被利用。

此次事件被归类为“供应链攻击”，即黑客通过破坏广泛使用的代码，进而获取大量用户系统和数据的访问权限。虽然开源项目经常成为攻击目标，但像微软这样拥有雄厚资源的科技巨头在短时间内两次遭受如此规模的攻击，实属罕见。微软正在继续调查，并表示如果需要采取进一步行动，将通过既定的支持渠道联系更多客户。

---

## 7. 因豁免请求被拒，苹果决定不在欧盟推出 Siri。

**原文标题**: Apple decided not to roll out Siri in EU after denied request for exemption

**原文链接**: [https://www.reuters.com/business/apple-failed-make-its-ai-tool-comply-eu-regulations-eu-commission-says-2026-06-09/](https://www.reuters.com/business/apple-failed-make-its-ai-tool-comply-eu-regulations-eu-commission-says-2026-06-09/)

Unable to access the article link.

---

## 8. The LD_DEBUG environment variable (2012)

**原文标题**: The LD_DEBUG environment variable (2012)

**原文链接**: [https://bnikolic.co.uk/blog/linux-ld-debug.html](https://bnikolic.co.uk/blog/linux-ld-debug.html)

生成摘要时出错

---

## 9. Biff.core: system composition for Clojure web apps

**原文标题**: Biff.core: system composition for Clojure web apps

**原文链接**: [https://biffweb.com/p/core/](https://biffweb.com/p/core/)

生成摘要时出错

---

## 10. FCC wants to kill burner phones by forcing telecoms to get all customers' IDs

**原文标题**: FCC wants to kill burner phones by forcing telecoms to get all customers' IDs

**原文链接**: [https://www.404media.co/fcc-wants-to-kill-burner-phones-by-forcing-telecoms-to-get-all-customers-ids/](https://www.404media.co/fcc-wants-to-kill-burner-phones-by-forcing-telecoms-to-get-all-customers-ids/)

生成摘要时出错

---

## 11. Is Grep All You Need? How Agent Harnesses Reshape Agentic Search

**原文标题**: Is Grep All You Need? How Agent Harnesses Reshape Agentic Search

**原文链接**: [https://arxiv.org/abs/2605.15184](https://arxiv.org/abs/2605.15184)

生成摘要时出错

---

## 12. OpenCV 5 Is Here: The Biggest Leap in Years for Computer Vision

**原文标题**: OpenCV 5 Is Here: The Biggest Leap in Years for Computer Vision

**原文链接**: [https://opencv.org/opencv-5/](https://opencv.org/opencv-5/)

生成摘要时出错

---

## 13. Can LLMs Beat Classical Hyperparameter Optimization Algorithms?

**原文标题**: Can LLMs Beat Classical Hyperparameter Optimization Algorithms?

**原文链接**: [https://arxiv.org/abs/2603.24647](https://arxiv.org/abs/2603.24647)

生成摘要时出错

---

## 14. Let's Encrypt bans certificate usage in any US sanctioned territory [pdf]

**原文标题**: Let's Encrypt bans certificate usage in any US sanctioned territory [pdf]

**原文链接**: [https://letsencrypt.org/documents/LE-SA-v1.7-June-04-2026-diff.pdf](https://letsencrypt.org/documents/LE-SA-v1.7-June-04-2026-diff.pdf)

生成摘要时出错

---

## 15. Show HN: Cost.dev (YC W21) – making agents cost-aware and cheaper to call

**原文标题**: Show HN: Cost.dev (YC W21) – making agents cost-aware and cheaper to call

**原文链接**: [https://cost.dev/](https://cost.dev/)

生成摘要时出错

---

## 16. The iPhone's Last Stand?

**原文标题**: The iPhone's Last Stand?

**原文链接**: [https://stratechery.com/2026/the-iphones-last-stand/](https://stratechery.com/2026/the-iphones-last-stand/)

生成摘要时出错

---

## 17. Show HN: GentleOS – A pair of hobby OSes for vintage 32-bit and 16-bit PCs

**原文标题**: Show HN: GentleOS – A pair of hobby OSes for vintage 32-bit and 16-bit PCs

**原文链接**: [https://github.com/luke8086/gentleos32](https://github.com/luke8086/gentleos32)

生成摘要时出错

---

## 18. Show HN: Gravity – interactive solar-system simulator, from Newton to Einstein

**原文标题**: Show HN: Gravity – interactive solar-system simulator, from Newton to Einstein

**原文链接**: [https://qunabu.github.io/Gravity/](https://qunabu.github.io/Gravity/)

生成摘要时出错

---

## 19. Emerge Career (YC S22) Is Hiring a Founding Growth Marketer

**原文标题**: Emerge Career (YC S22) Is Hiring a Founding Growth Marketer

**原文链接**: [https://www.ycombinator.com/companies/emerge-career/jobs/v0S1AEG-founding-growth-marketer](https://www.ycombinator.com/companies/emerge-career/jobs/v0S1AEG-founding-growth-marketer)

生成摘要时出错

---

## 20. Unified Controllable and Faithful Text-to-CAD Generation with LLMs

**原文标题**: Unified Controllable and Faithful Text-to-CAD Generation with LLMs

**原文链接**: [https://arxiv.org/abs/2604.19773](https://arxiv.org/abs/2604.19773)

生成摘要时出错

---

## 21. Rayforce

**原文标题**: Rayforce

**原文链接**: [https://github.com/RayforceDB/rayforce](https://github.com/RayforceDB/rayforce)

生成摘要时出错

---

## 22. I Think Rutger Bregman and the School for Moral Ambition Are Full of Shit

**原文标题**: I Think Rutger Bregman and the School for Moral Ambition Are Full of Shit

**原文链接**: [https://louwrentius.com/i-think-rutger-bregman-the-school-for-moral-ambition-are-full-of-shit.html](https://louwrentius.com/i-think-rutger-bregman-the-school-for-moral-ambition-are-full-of-shit.html)

生成摘要时出错

---

## 23. Forever Young: how one molecule can lock plants in a youthful state (2025)

**原文标题**: Forever Young: how one molecule can lock plants in a youthful state (2025)

**原文链接**: [https://omnia.sas.upenn.edu/story/biologist-scott-poethig-plants-never-age](https://omnia.sas.upenn.edu/story/biologist-scott-poethig-plants-never-age)

生成摘要时出错

---

## 24. Using Optical Aberrations to Distinguish Real Astronomical Transients

**原文标题**: Using Optical Aberrations to Distinguish Real Astronomical Transients

**原文链接**: [https://arxiv.org/abs/2606.08319](https://arxiv.org/abs/2606.08319)

生成摘要时出错

---

## 25. Show HN: Learn from 30 historical figures, open source, nonprofit, self-hosted

**原文标题**: Show HN: Learn from 30 historical figures, open source, nonprofit, self-hosted

**原文链接**: [https://github.com/chipmates/agoracosmica](https://github.com/chipmates/agoracosmica)

生成摘要时出错

---

## 26. Thi.ng – open-source building blocks for computational design and art

**原文标题**: Thi.ng – open-source building blocks for computational design and art

**原文链接**: [https://thi.ng](https://thi.ng)

生成摘要时出错

---

## 27. Cleaning up after AI rockstar developers

**原文标题**: Cleaning up after AI rockstar developers

**原文链接**: [https://www.codingwithjesse.com/blog/rockstar-developers/](https://www.codingwithjesse.com/blog/rockstar-developers/)

生成摘要时出错

---

## 28. The Effective Sample Size

**原文标题**: The Effective Sample Size

**原文链接**: [https://alex.smola.org/posts/40-effective-sample-size/](https://alex.smola.org/posts/40-effective-sample-size/)

生成摘要时出错

---

## 29. Painting the Internet: A Different Kind of Warhol Worm [pdf]

**原文标题**: Painting the Internet: A Different Kind of Warhol Worm [pdf]

**原文链接**: [https://cspages.ucalgary.ca/~aycock/papers/artworm.pdf](https://cspages.ucalgary.ca/~aycock/papers/artworm.pdf)

生成摘要时出错

---

## 30. An introduction to functional analysis for science and engineering

**原文标题**: An introduction to functional analysis for science and engineering

**原文链接**: [https://arxiv.org/abs/1904.02539](https://arxiv.org/abs/1904.02539)

生成摘要时出错

---

## 31. Corrupting a ZFS File on Purpose

**原文标题**: Corrupting a ZFS File on Purpose

**原文链接**: [https://oshogbo.com/blog/90/](https://oshogbo.com/blog/90/)

生成摘要时出错

---

## 32. 'Sloppenheimer:' Amazon Employees Mock the Company's AI on Slack

**原文标题**: 'Sloppenheimer:' Amazon Employees Mock the Company's AI on Slack

**原文链接**: [https://www.404media.co/sloppenheimer-amazon-employees-mock-the-companys-ai-on-slack/](https://www.404media.co/sloppenheimer-amazon-employees-mock-the-companys-ai-on-slack/)

生成摘要时出错

---

## 33. Job: Head of Stonehenge

**原文标题**: Job: Head of Stonehenge

**原文链接**: [https://www.english-heritage.org.uk/about/our-people/careers-with-us/job-search/default-job-page/?jobRef=16449](https://www.english-heritage.org.uk/about/our-people/careers-with-us/job-search/default-job-page/?jobRef=16449)

生成摘要时出错

---

## 34. CEOs Who Think AI Replaces Their Employees Are Just Bad CEOs

**原文标题**: CEOs Who Think AI Replaces Their Employees Are Just Bad CEOs

**原文链接**: [https://www.techdirt.com/2026/06/09/ceos-who-think-ai-replaces-their-employees-are-just-bad-ceos/](https://www.techdirt.com/2026/06/09/ceos-who-think-ai-replaces-their-employees-are-just-bad-ceos/)

生成摘要时出错

---

## 35. Adopting the Parallel DWARF linker in dsymutil

**原文标题**: Adopting the Parallel DWARF linker in dsymutil

**原文链接**: [https://jonasdevlieghere.com/post/dsymutil-parallel-linker/](https://jonasdevlieghere.com/post/dsymutil-parallel-linker/)

生成摘要时出错

---

## 36. Where is the AI jobs crisis?

**原文标题**: Where is the AI jobs crisis?

**原文链接**: [https://www.apollo.com/wealth/the-daily-spark/where-is-the-ai-jobs-crisis](https://www.apollo.com/wealth/the-daily-spark/where-is-the-ai-jobs-crisis)

生成摘要时出错

---

## 37. Amazon employees ask Seattle to put the brakes on new data centers

**原文标题**: Amazon employees ask Seattle to put the brakes on new data centers

**原文链接**: [https://www.theverge.com/ai-artificial-intelligence/945809/amazon-employees-seattle-data-center-moratorium](https://www.theverge.com/ai-artificial-intelligence/945809/amazon-employees-seattle-data-center-moratorium)

生成摘要时出错

---

## 38. Porting the ThinkPad X61 to Coreboot

**原文标题**: Porting the ThinkPad X61 to Coreboot

**原文链接**: [https://blog.aheymans.xyz/post/thinkpad_x61/](https://blog.aheymans.xyz/post/thinkpad_x61/)

生成摘要时出错

---

## 39. The beauty and simplicity of the good old C-style void* in C++

**原文标题**: The beauty and simplicity of the good old C-style void* in C++

**原文链接**: [https://giodicanio.com/2026/06/05/how-to-declare-a-c-plus-plus-function-that-takes-a-blob-of-memory/](https://giodicanio.com/2026/06/05/how-to-declare-a-c-plus-plus-function-that-takes-a-blob-of-memory/)

生成摘要时出错

---

## 40. Eagle Computer: The rise and fall of an early PC clone

**原文标题**: Eagle Computer: The rise and fall of an early PC clone

**原文链接**: [https://dfarq.homeip.net/eagle-computer-the-rise-and-fall-of-an-early-pc-clone/](https://dfarq.homeip.net/eagle-computer-the-rise-and-fall-of-an-early-pc-clone/)

生成摘要时出错

---

## 41. Old'aVista – The most powerful guide to the old Internet

**原文标题**: Old'aVista – The most powerful guide to the old Internet

**原文链接**: [https://oldavista.com/](https://oldavista.com/)

生成摘要时出错

---

## 42. H2JVM – A Haskell Library for Writing JVM Bytecode

**原文标题**: H2JVM – A Haskell Library for Writing JVM Bytecode

**原文链接**: [https://discourse.haskell.org/t/h2jvm-a-haskell-library-for-writing-jvm-bytecode/14182](https://discourse.haskell.org/t/h2jvm-a-haskell-library-for-writing-jvm-bytecode/14182)

生成摘要时出错

---

## 43. Apple reveals new AI architecture built around Google Gemini models

**原文标题**: Apple reveals new AI architecture built around Google Gemini models

**原文链接**: [https://www.macrumors.com/2026/06/08/apple-reveals-new-ai-architecture/](https://www.macrumors.com/2026/06/08/apple-reveals-new-ai-architecture/)

生成摘要时出错

---

## 44. Judge Learns Both Sides Used AI, Cancels Trial, Kicks Everyone Off the Case

**原文标题**: Judge Learns Both Sides Used AI, Cancels Trial, Kicks Everyone Off the Case

**原文链接**: [https://www.404media.co/judge-learns-lawyers-on-both-sides-of-case-used-ai-cancels-trial-kicks-everyone-off-the-case/](https://www.404media.co/judge-learns-lawyers-on-both-sides-of-case-used-ai-cancels-trial-kicks-everyone-off-the-case/)

生成摘要时出错

---

## 45. Meta ordered by EU to allow rival AI chatbots back on WhatsApp for free

**原文标题**: Meta ordered by EU to allow rival AI chatbots back on WhatsApp for free

**原文链接**: [https://www.reuters.com/world/eu-regulators-order-meta-allow-rival-ai-chatbots-free-access-whatsapp-2026-06-09/](https://www.reuters.com/world/eu-regulators-order-meta-allow-rival-ai-chatbots-free-access-whatsapp-2026-06-09/)

生成摘要时出错

---

## 46. xAI is looking more like a datacentre REIT than a frontier lab

**原文标题**: xAI is looking more like a datacentre REIT than a frontier lab

**原文链接**: [https://martinalderson.com/posts/xais-new-rental-business/](https://martinalderson.com/posts/xais-new-rental-business/)

生成摘要时出错

---

## 47. Show HN: Performative-UI – A react component library of design tropes

**原文标题**: Show HN: Performative-UI – A react component library of design tropes

**原文链接**: [https://vorpus.github.io/performativeUI/](https://vorpus.github.io/performativeUI/)

生成摘要时出错

---

## 48. Solar Energy Saves Europeans $135M a Day

**原文标题**: Solar Energy Saves Europeans $135M a Day

**原文链接**: [https://cleantechnica.com/2026/06/08/solar-energy-saves-europeans-135-million-a-day/](https://cleantechnica.com/2026/06/08/solar-energy-saves-europeans-135-million-a-day/)

生成摘要时出错

---

## 49. AI profitability is mathematically impossible

**原文标题**: AI profitability is mathematically impossible

**原文链接**: [https://old.reddit.com/r/BetterOffline/comments/1tzwnhi/ai_profitability_is_mathematically_impossible/](https://old.reddit.com/r/BetterOffline/comments/1tzwnhi/ai_profitability_is_mathematically_impossible/)

生成摘要时出错

---

## 50. Anthropic Kept Every Promise It Could Afford

**原文标题**: Anthropic Kept Every Promise It Could Afford

**原文链接**: [https://techtrenches.dev/p/anthropic-kept-every-promise-it-could](https://techtrenches.dev/p/anthropic-kept-every-promise-it-could)

生成摘要时出错

---

## 51. Siri AI

**原文标题**: Siri AI

**原文链接**: [https://www.apple.com/apple-intelligence/](https://www.apple.com/apple-intelligence/)

生成摘要时出错

---

## 52. EU-banned pesticides found in rice, tea and spices

**原文标题**: EU-banned pesticides found in rice, tea and spices

**原文链接**: [https://www.foodwatch.org/en/eu-banned-pesticides-found-in-rice-tea-and-spices](https://www.foodwatch.org/en/eu-banned-pesticides-found-in-rice-tea-and-spices)

生成摘要时出错

---

## 53. Anti-social: It's fads, not friends, which now dominate social media feeds

**原文标题**: Anti-social: It's fads, not friends, which now dominate social media feeds

**原文链接**: [https://www.bbc.com/worklife/article/20260520-how-social-media-ceased-to-be-social](https://www.bbc.com/worklife/article/20260520-how-social-media-ceased-to-be-social)

生成摘要时出错

---

## 54. TRPL: A copylet license that treats API usage as derivate works

**原文标题**: TRPL: A copylet license that treats API usage as derivate works

**原文链接**: [https://trplfoundation.org/](https://trplfoundation.org/)

生成摘要时出错

---

## 55. Apple bets cheaper AI will woo small developers

**原文标题**: Apple bets cheaper AI will woo small developers

**原文链接**: [https://techcrunch.com/2026/06/08/apple-bets-cheaper-ai-will-woo-small-developers/](https://techcrunch.com/2026/06/08/apple-bets-cheaper-ai-will-woo-small-developers/)

生成摘要时出错

---

## 56. I'm building a parallel internet, and it's called The Thinnernet

**原文标题**: I'm building a parallel internet, and it's called The Thinnernet

**原文链接**: [https://inavoyage.blogspot.com/2026/06/im-building-parallel-internet-and-its.html](https://inavoyage.blogspot.com/2026/06/im-building-parallel-internet-and-its.html)

生成摘要时出错

---

## 57. Launch HN: Intuned (YC S22) – Build and run reliable browser automations as code

**原文标题**: Launch HN: Intuned (YC S22) – Build and run reliable browser automations as code

**原文链接**: [https://intunedhq.com](https://intunedhq.com)

生成摘要时出错

---

## 58. Even light drinking raises risk of cancer, heart disease, and early death

**原文标题**: Even light drinking raises risk of cancer, heart disease, and early death

**原文链接**: [https://www.eurekalert.org/news-releases/1131274](https://www.eurekalert.org/news-releases/1131274)

生成摘要时出错

---

## 59. MiMo-v2.5-Pro-UltraSpeed: 1T model with 1000 tokens per second

**原文标题**: MiMo-v2.5-Pro-UltraSpeed: 1T model with 1000 tokens per second

**原文链接**: [https://mimo.xiaomi.com/blog/mimo-tilert-1000tps](https://mimo.xiaomi.com/blog/mimo-tilert-1000tps)

生成摘要时出错

---

## 60. Albania Is Not for Sale: Kushner's $4B Resort Triggers'Flamingo Revolution'

**原文标题**: Albania Is Not for Sale: Kushner's $4B Resort Triggers'Flamingo Revolution'

**原文链接**: [https://www.yacnews.com/albania-is-not-for-sale-kushners-4-billion-resort-triggers-flamingo-revolution-asset-freeze-and-an-eu-warning/](https://www.yacnews.com/albania-is-not-for-sale-kushners-4-billion-resort-triggers-flamingo-revolution-asset-freeze-and-an-eu-warning/)

生成摘要时出错

---

## 61. How much do amd64 microarchitecture levels help in Go?

**原文标题**: How much do amd64 microarchitecture levels help in Go?

**原文链接**: [https://lemire.me/blog/2026/06/06/how-much-do-amd64-microarchitecture-levels-help-in-go/](https://lemire.me/blog/2026/06/06/how-much-do-amd64-microarchitecture-levels-help-in-go/)

生成摘要时出错

---

## 62. SAT-Physical Thermodynamic Framework: treating constraints as a thermal system

**原文标题**: SAT-Physical Thermodynamic Framework: treating constraints as a thermal system

**原文链接**: [https://github.com/alikamp/SAT_HARDNESS_P-NP](https://github.com/alikamp/SAT_HARDNESS_P-NP)

生成摘要时出错

---

## 63. BofA Warns Investors Should Take Profits Now in US Equities

**原文标题**: BofA Warns Investors Should Take Profits Now in US Equities

**原文链接**: [https://catenaa.com/markets/equities/bofa-warns-investors-should-take-profits-now-in-us-equities/](https://catenaa.com/markets/equities/bofa-warns-investors-should-take-profits-now-in-us-equities/)

生成摘要时出错

---

## 64. Data Center Boom Exposes GOP Faultlines over Local Control

**原文标题**: Data Center Boom Exposes GOP Faultlines over Local Control

**原文链接**: [https://www.texasobserver.org/data-center-boom-rural-gop-local-control/](https://www.texasobserver.org/data-center-boom-rural-gop-local-control/)

生成摘要时出错

---

## 65. Apple Core AI Framework

**原文标题**: Apple Core AI Framework

**原文链接**: [https://developer.apple.com/documentation/coreai/](https://developer.apple.com/documentation/coreai/)

生成摘要时出错

---

## 66. Datacenter boom keeps dirty coal plants alive in the US

**原文标题**: Datacenter boom keeps dirty coal plants alive in the US

**原文链接**: [https://www.theregister.com/on-prem/2026/04/22/datacenter-boom-keeps-dirty-coal-plants-alive-in-the-us/5219820](https://www.theregister.com/on-prem/2026/04/22/datacenter-boom-keeps-dirty-coal-plants-alive-in-the-us/5219820)

生成摘要时出错

---

## 67. OCaml Onboarding: Introduction to the Dune build system

**原文标题**: OCaml Onboarding: Introduction to the Dune build system

**原文链接**: [https://ocamlpro.com/blog/2025_07_29_ocaml_onboarding_introduction_to_dune/](https://ocamlpro.com/blog/2025_07_29_ocaml_onboarding_introduction_to_dune/)

生成摘要时出错

---

## 68. Apple made a request to the EC to be exempted from interop obligations under DMA

**原文标题**: Apple made a request to the EC to be exempted from interop obligations under DMA

**原文链接**: [https://audiovisual.ec.europa.eu/en/media/video/I-290903](https://audiovisual.ec.europa.eu/en/media/video/I-290903)

生成摘要时出错

---

## 69. Passing DBs through continuations

**原文标题**: Passing DBs through continuations

**原文链接**: [https://remy.wang/blog/cps.html](https://remy.wang/blog/cps.html)

生成摘要时出错

---

## 70. Social Security funds could run short by 2032, program's Trustees warn

**原文标题**: Social Security funds could run short by 2032, program's Trustees warn

**原文链接**: [https://www.npr.org/2026/06/09/nx-s1-5850279/social-security-funds-trustees-congress](https://www.npr.org/2026/06/09/nx-s1-5850279/social-security-funds-trustees-congress)

生成摘要时出错

---

## 71. Are you expected to run five Python type-checkers now?

**原文标题**: Are you expected to run five Python type-checkers now?

**原文链接**: [https://pyrefly.org/blog/too-many-type-checkers/](https://pyrefly.org/blog/too-many-type-checkers/)

生成摘要时出错

---

## 72. US publishers tell Common Crawl to stop scraping and delete archive

**原文标题**: US publishers tell Common Crawl to stop scraping and delete archive

**原文链接**: [https://pressgazette.co.uk/media_law/common-crawl-ai-news-publishers-scraping-cease-and-desist-letter/](https://pressgazette.co.uk/media_law/common-crawl-ai-news-publishers-scraping-cease-and-desist-letter/)

生成摘要时出错

---

## 73. Looking Forward to Postgres 19: Query Hints

**原文标题**: Looking Forward to Postgres 19: Query Hints

**原文链接**: [https://www.pgedge.com/blog/looking-forward-to-postgres-19-query-hints](https://www.pgedge.com/blog/looking-forward-to-postgres-19-query-hints)

生成摘要时出错

---

## 74. macOS 27 Beta Breaks the Ability to Boot Asahi Linux

**原文标题**: macOS 27 Beta Breaks the Ability to Boot Asahi Linux

**原文链接**: [https://www.phoronix.com/news/macOS-27-Beta-Breaks-Asahi](https://www.phoronix.com/news/macOS-27-Beta-Breaks-Asahi)

生成摘要时出错

---

## 75. Replies to comments on my "LLMs are eroding my career" post

**原文标题**: Replies to comments on my "LLMs are eroding my career" post

**原文链接**: [https://human-in-the-loop.bearblog.dev/replies-to-comments-on-my-llms-are-eroding-my-career-post/](https://human-in-the-loop.bearblog.dev/replies-to-comments-on-my-llms-are-eroding-my-career-post/)

生成摘要时出错

---

## 76. Show HN: Gitdot – A better GitHub. Open-source, written in Rust

**原文标题**: Show HN: Gitdot – A better GitHub. Open-source, written in Rust

**原文链接**: [https://gitdot.io/](https://gitdot.io/)

生成摘要时出错

---

## 77. The better the autopilot the worse the pilot

**原文标题**: The better the autopilot the worse the pilot

**原文链接**: [https://julienreszka.com/blog/the-better-the-autopilot-the-worse-the-pilot/](https://julienreszka.com/blog/the-better-the-autopilot-the-worse-the-pilot/)

生成摘要时出错

---

## 78. WWDC 2026: Apple is Folding

**原文标题**: WWDC 2026: Apple is Folding

**原文链接**: [https://cupertinolens.com/2026/06/09/wwdc-2026-apple-is-folding/](https://cupertinolens.com/2026/06/09/wwdc-2026-apple-is-folding/)

生成摘要时出错

---

## 79. Massachusetts bans sale of precise location data in new privacy rights bill

**原文标题**: Massachusetts bans sale of precise location data in new privacy rights bill

**原文链接**: [https://techcrunch.com/2026/06/08/massachusetts-votes-to-pass-new-privacy-rights-bill-that-bans-sale-of-precise-location-data/](https://techcrunch.com/2026/06/08/massachusetts-votes-to-pass-new-privacy-rights-bill-that-bans-sale-of-precise-location-data/)

生成摘要时出错

---

## 80. CRDTs merge concurrent edits. Why not concurrent creation?

**原文标题**: CRDTs merge concurrent edits. Why not concurrent creation?

**原文链接**: [https://loro.dev/blog/mergeable-containers](https://loro.dev/blog/mergeable-containers)

生成摘要时出错

---

## 81. Thunderbird Littering My Home

**原文标题**: Thunderbird Littering My Home

**原文链接**: [https://thefoggiest.dev/2026/06/04/thunderbird-littering-my-home](https://thefoggiest.dev/2026/06/04/thunderbird-littering-my-home)

生成摘要时出错

---

## 82. Confidential submission of draft S-1 to the SEC

**原文标题**: Confidential submission of draft S-1 to the SEC

**原文链接**: [https://openai.com/index/openai-submits-confidential-s-1/](https://openai.com/index/openai-submits-confidential-s-1/)

生成摘要时出错

---

## 83. Apple Watch for Your Kids

**原文标题**: Apple Watch for Your Kids

**原文链接**: [https://www.apple.com/apple-watch-for-your-kids/](https://www.apple.com/apple-watch-for-your-kids/)

生成摘要时出错

---

## 84. Zig Structs of Arrays (2024)

**原文标题**: Zig Structs of Arrays (2024)

**原文链接**: [https://andreashohmann.com/zig-struct-of-arrays/](https://andreashohmann.com/zig-struct-of-arrays/)

生成摘要时出错

---

## 85. Splash Is a Colour Format

**原文标题**: Splash Is a Colour Format

**原文链接**: [https://www.todepond.com/lab/splash/](https://www.todepond.com/lab/splash/)

生成摘要时出错

---

## 86. Dopamine Fracking

**原文标题**: Dopamine Fracking

**原文链接**: [https://igerman.cc/blog/dopamine-fracking/](https://igerman.cc/blog/dopamine-fracking/)

生成摘要时出错

---

## 87. Life is too short for a slow terminal

**原文标题**: Life is too short for a slow terminal

**原文链接**: [https://mijndertstuij.nl/posts/life-is-too-short-for-a-slow-terminal/](https://mijndertstuij.nl/posts/life-is-too-short-for-a-slow-terminal/)

生成摘要时出错

---

## 88. Meta ordered by EU to allow rival AI chatbots back on WhatsApp for free

**原文标题**: Meta ordered by EU to allow rival AI chatbots back on WhatsApp for free

**原文链接**: [https://ec.europa.eu/commission/presscorner/home/en](https://ec.europa.eu/commission/presscorner/home/en)

生成摘要时出错

---

## 89. FrontierCode

**原文标题**: FrontierCode

**原文链接**: [https://cognition.ai/blog/frontier-code](https://cognition.ai/blog/frontier-code)

生成摘要时出错

---

## 90. Stop the Apple Music app from launching

**原文标题**: Stop the Apple Music app from launching

**原文链接**: [https://lowtechguys.com/musicdecoy/](https://lowtechguys.com/musicdecoy/)

生成摘要时出错

---

## 91. North Korean spies spent months in-person to drain $285M from Drift

**原文标题**: North Korean spies spent months in-person to drain $285M from Drift

**原文链接**: [https://www.coindesk.com/business/2026/04/30/north-korean-hackers-are-moving-faster-they-account-for-76-of-crypto-exploits-this-year-trmlabs](https://www.coindesk.com/business/2026/04/30/north-korean-hackers-are-moving-faster-they-account-for-76-of-crypto-exploits-this-year-trmlabs)

生成摘要时出错

---

## 92. Building from zero after addiction, prison, and a felony

**原文标题**: Building from zero after addiction, prison, and a felony

**原文链接**: [https://gavinray97.github.io/blog/building-from-zero-after-addiction-prison-felony](https://gavinray97.github.io/blog/building-from-zero-after-addiction-prison-felony)

生成摘要时出错

---

## 93. Two vendors run 91% of the secure email gateway market for US public companies

**原文标题**: Two vendors run 91% of the secure email gateway market for US public companies

**原文链接**: [https://ciphercue.com/blog/email-triopoly-us-public-companies-2026](https://ciphercue.com/blog/email-triopoly-us-public-companies-2026)

生成摘要时出错

---

## 94. 1worldflag: A blue dot on a transparent background

**原文标题**: 1worldflag: A blue dot on a transparent background

**原文链接**: [https://1worldflag.com/](https://1worldflag.com/)

生成摘要时出错

---

## 95. Fooling Go's X.509 Certificate Verification

**原文标题**: Fooling Go's X.509 Certificate Verification

**原文链接**: [https://danielmangum.com/posts/fooling-go-x509-certificate-verification/](https://danielmangum.com/posts/fooling-go-x509-certificate-verification/)

生成摘要时出错

---

## 96. SpaceX to lower thousands of Starlink satellites in 2026 as collisions rise

**原文标题**: SpaceX to lower thousands of Starlink satellites in 2026 as collisions rise

**原文链接**: [https://www.euronews.com/next/2026/01/03/spacex-to-lower-thousands-of-starlink-satellites-in-2026-as-collisions-rise-company-says](https://www.euronews.com/next/2026/01/03/spacex-to-lower-thousands-of-starlink-satellites-in-2026-as-collisions-rise-company-says)

生成摘要时出错

---

## 97. Switzerland wil have a referendum to cap population at 10M

**原文标题**: Switzerland wil have a referendum to cap population at 10M

**原文链接**: [https://www.admin.ch/en/sustainability-initiative](https://www.admin.ch/en/sustainability-initiative)

生成摘要时出错

---

## 98. Why are cells small?

**原文标题**: Why are cells small?

**原文链接**: [https://burrito.bio/essays/what-limits-a-cells-size](https://burrito.bio/essays/what-limits-a-cells-size)

生成摘要时出错

---

## 99. Meta account recovery allowed unauthenticated access to full account PII

**原文标题**: Meta account recovery allowed unauthenticated access to full account PII

**原文链接**: [https://twitter.com/IntCyberDigest/status/2063406949354311935](https://twitter.com/IntCyberDigest/status/2063406949354311935)

生成摘要时出错

---

## 100. Surveillance is not safety: A statement on the UK's latest threat to privacy [pdf]

**原文标题**: Surveillance is not safety: A statement on the UK's latest threat to privacy [pdf]

**原文链接**: [https://signal.org/blog/pdfs/2026-06-08-uk-surveillance-is-not-safety.pdf](https://signal.org/blog/pdfs/2026-06-08-uk-surveillance-is-not-safety.pdf)

生成摘要时出错

---

