# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-06-09.md)

*最后自动更新时间: 2026-06-09 19:46:48*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 2 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 3 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 4 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 5 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 6 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 7 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 8 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 9 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 10 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 11 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 12 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 13 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 14 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 15 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 16 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 17 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 18 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 19 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 20 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 21 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 22 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 23 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 24 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 25 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 26 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 27 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 28 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 29 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 30 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 31 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 32 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 33 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 34 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 35 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 36 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 37 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 38 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 39 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 40 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 41 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 42 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 43 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 44 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 45 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 46 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 47 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 48 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 49 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 50 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 51 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 52 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 53 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 54 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 55 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 56 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 57 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 58 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 59 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 60 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 61 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 62 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 63 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 64 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 65 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 66 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 67 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 68 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 69 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 70 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 71 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 72 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 73 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 74 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 75 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 76 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 77 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 78 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 79 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 80 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 81 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 82 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 83 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 84 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 85 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 86 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 87 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 88 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 89 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 90 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 91 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 92 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 93 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 94 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 95 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 96 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 97 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 98 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 99 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 100 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 101 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 102 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 103 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 104 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 105 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 106 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 107 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 108 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 109 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 110 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 111 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 112 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 113 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 114 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 115 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 116 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 117 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 118 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 119 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 120 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 121 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 122 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 123 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 124 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 125 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 126 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 127 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 128 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 129 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 130 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 131 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 132 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 133 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 134 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 135 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 136 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 137 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 138 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 139 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 140 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 141 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 142 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 143 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 144 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 145 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 146 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 147 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 148 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 149 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 150 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 151 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 152 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 153 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 154 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 155 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 156 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 157 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 158 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 159 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 160 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 161 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 162 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 163 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 164 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 165 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 166 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 167 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 168 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 169 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 170 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 171 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 172 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 173 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 174 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 175 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 176 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 177 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 178 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 179 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 180 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 181 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 182 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 183 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 184 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 185 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 186 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 187 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 188 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 189 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 190 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 191 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 192 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 193 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 194 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 195 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 196 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 197 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 198 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 199 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 200 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 201 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 202 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 203 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 204 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 205 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 206 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 207 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 208 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 209 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 210 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 211 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 212 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 213 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 214 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 215 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 216 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 217 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 218 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 219 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 220 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 221 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 222 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 223 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 224 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 225 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 226 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 227 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 228 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 229 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 230 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 231 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 232 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 233 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 234 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 235 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 236 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 237 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 238 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 239 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 240 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 241 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 242 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 243 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 244 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 245 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 246 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 247 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 248 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 249 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 250 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 251 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 252 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 253 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 254 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 255 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 256 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 257 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 258 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 259 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 260 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 261 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 262 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 263 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 264 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 265 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 266 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 267 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 268 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 269 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 270 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 271 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 272 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 273 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 274 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 275 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 276 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 277 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 278 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 279 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 280 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 281 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 282 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 283 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 284 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 285 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 286 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 287 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 288 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 289 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 290 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 291 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 292 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 293 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 294 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 295 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 296 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 297 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 298 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 299 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 300 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 301 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 302 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 303 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 304 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 305 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 306 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 307 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 308 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 309 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 310 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 311 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 312 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 313 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 314 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 315 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 316 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 317 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 318 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 319 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 320 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 321 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 322 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 323 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 324 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 325 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 326 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 327 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 328 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 329 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 330 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 331 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 332 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 333 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 334 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 335 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 336 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 337 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 338 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 339 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 340 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 341 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 342 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 343 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 344 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 345 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 346 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 347 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 348 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 349 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 350 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 351 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 352 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 353 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 354 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 355 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 356 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 357 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 358 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 359 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 360 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 361 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 362 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 363 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 364 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 365 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 366 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 367 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 368 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 369 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 370 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 371 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 372 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 373 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 374 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 375 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 376 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 377 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 378 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 379 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 380 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 381 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 382 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 383 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 384 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 385 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 386 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 387 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 388 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 389 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 390 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 391 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 392 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 393 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 394 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 395 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 396 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 397 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 398 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 399 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 400 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 401 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 402 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 403 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 404 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 405 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 406 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 407 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 408 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 409 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 410 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 411 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 412 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 413 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 414 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 415 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 416 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 417 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 418 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 419 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 420 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 421 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 422 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 423 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 424 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 425 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 426 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 427 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 428 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 429 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 430 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 431 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 432 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 433 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 434 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 435 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 436 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 437 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 438 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 439 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 440 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 441 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 442 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 443 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 444 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 445 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 446 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
