# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-11-24.md)

*最后自动更新时间: 2026-11-24 03:32:08*
## 1. 《华尔街日报》社论：恢复黄的CEO职务将付出重大的国家安全和政治代价

**原文标题**: WSJ Editorial: Restoring Huang as CEO will have major NatSec and political costs

**原文链接**: [https://www.wsj.com/opinion/nvidia-jensen-huang-donald-trump-130e644c](https://www.wsj.com/opinion/nvidia-jensen-huang-donald-trump-130e644c)

无法访问文章链接。

---

## 2. 安全地狱的下一层

**原文标题**: The next circle of security hell

**原文链接**: [https://blogs.gentoo.org/mgorny/2026/10/27/the-next-circle-of-security-hell/](https://blogs.gentoo.org/mgorny/2026/10/27/the-next-circle-of-security-hell/)

在《安全地狱的下一层》中，作者指出软件安全形势已显著恶化，正演变为维护者无法承受的“噩梦”。这种衰落是由几个交织在一起的因素驱动的：

*   **“垃圾信息”泛滥：** AI 辅助报告和漏洞赏金猎人的兴起使项目中充斥着大量低质量的漏洞报告。维护者必须耗费巨大精力对这些报告进行分拣，而其中许多报告不仅无效，而且对实际攻击向量缺乏细致的理解。
*   **表演式安全：** 安全扫描器和自动化工具往往缺乏区分理论风险与实际风险的背景信息。因此，维护者被迫从事“毫无意义”的工作——例如不必要的版本升级，或修复并不适用于其特定发行版的漏洞——仅仅是为了满足扫描器的要求并安抚担忧的用户。
*   **上游管理中的结构性失效：** 大多数项目尚未准备好进行专业的安全处理。开发者经常将安全修复与重大的 API 变更、新功能或未经测试的代码捆绑在一起，而不是提供独立的补丁或 LTS 分支。这迫使下游维护者为了解决单个漏洞而不得不应对破坏性变更。
*   **依赖关系的复杂性：** 随着软件变得日益复杂，维护深度依赖树的负担已变得难以承受。当上游维护者失效时，工作量会转移到下游，从而导致维护者倦怠。

作者总结道，整个生态系统正走向崩溃边缘。这种“安全地狱”催生了信任危机，导致维护者开始捆绑依赖项并陷入孤立工作。最终，分拣“垃圾信息”和应对糟糕发布实践所带来的持续压力，正威胁着开源协作开发的本质。

---

## 3. LLM 应该如何看待计算机？

**原文标题**: How should an LLM see a computer?

**原文链接**: [https://www.greptile.com/blog/trex-computer-use](https://www.greptile.com/blog/trex-computer-use)

本文探讨了大语言模型（LLM）与计算机界面交互的最有效方式，重点比较了视觉截图与基于文本的“无障碍树”（accessibility trees）的使用效果。虽然智能体通常利用截图来“观察”屏幕，但作者指出，受图像压缩和分辨率变化的影响，将视觉数据转换为精确像素坐标的过程极易出错。

为了优化其 QA 智能体 **TREX**，作者在 172 项 OSWorld 任务上测试了七款 OpenAI 模型（涵盖从 GPT-4o 到假设的 GPT-6.1 Sol）。他们测试了三种配置：
1. **仅截图：** 模型根据图像预测坐标。
2. **无障碍树 + 坐标：** 模型参考元素的文本映射，但仍需输出像素坐标。
3. **无障碍树 + ID 点击：** 模型通过特定 ID 选择元素，完全绕过了坐标计算。

**核心发现：**
*   **模型性能是关键：** 对于性能较弱的模型（如 GPT-4.1 或 GPT-5.2），无障碍树和 ID 点击模式带来了突破性提升，通常能使其性能翻倍。
*   **高端模型收益递减：** 最强大的模型（GPT-6 系列）仅凭截图即可表现卓越（成功率超过 80%）。对于这些模型，引入无障碍树并未带来统计学上的显著改进。
*   **混合模式的必要性：** 作者观察到无障碍树往往不完整，无法识别基于画布（canvas）的应用、游戏或文本重叠等视觉缺陷。

**结论：**
基于上述结果，**TREX** 采用了混合方案。它以截图作为主要的上下文来源，并在可能的情况下利用无障碍树通过 ID 进行点击。该策略使智能体能够可靠地实现 UI 测试自动化，并捕捉到传统代码审查可能遗漏的拉取请求（PR）中的漏洞。作者计划在具备更强视觉能力的模型发布后，重新评估这一平衡点。

---

## 4. 为超级任天堂打造无线网络适配器

**原文标题**: Building a wireless network adapter for the Super Nintendo

**原文链接**: [https://boland.dev/snet/](https://boland.dev/snet/)

本文详细介绍了“超级网络适配器”（Super Network Adapter）的开发过程，这是一款通过手柄接口连接超级任天堂（SNES）的无线外设。凭借电子和软件领域的专业背景，作者将该设备的开发视为一次“16位未来主义”的实践，旨在将复古硬件与现代云端及 AI 功能相结合。

**硬件与连接**
由于 SNES 缺乏原生网络接口，该适配器利用了手柄接口的同步串行总线。硬件采用双芯片架构：树莓派 RP2350A 负责处理主机的 5V 逻辑和串行通信（速度可达约 30 KB/s），而 ESP32-C3 则作为 Wi-Fi 协处理器。设备可直接由主机或通过 USB 供电，并采用理想二极管电路以防止调试期间的电流倒灌。

**核心功能**
*   **存档同步：** 通过自定义工具对 ROM 进行补丁处理，适配器能将电池供电的 SRAM 存档自动同步到 WebDAV 服务器。这使玩家可以在原始硬件与 RetroArch 等模拟器之间无缝切换。为最大限度降低延迟，系统仅传输修改后的数据“块”。
*   **AI 对话：** 通过对《众神的三角力量》等游戏打补丁，作者集成了大语言模型（特别是 Claude 3.5 Opus），将静态 NPC 文本替换为动态的、具备上下文感知能力的对话。为克服 LLM 的延迟，适配器采用了“投机性生成”技术，在玩家靠近 NPC 时便预先生成回复。
*   **用户界面：** Wi-Fi 配置既可以通过专用的 SNES 设置 ROM 完成，也可以通过扫描电视上显示的二维码，进入适配手机端的强制网络门户进行操作。

该项目以一个定制设计的 3D 打印外壳收尾，外壳配有用于状态指示灯的导光管，成功地将这款 20 世纪 90 年代的游戏机带入了现代互联时代。

---

## 5. Show HN：3D 驾驶环游我的村庄

**原文标题**: Show HN: Drive around my village in 3D

**原文链接**: [https://cherwellvalleymotorclub.app](https://cherwellvalleymotorclub.app)

这个名为“3D 环游我的村庄”（Drive around my village in 3D）的项目最初发布于 Hacker News 的“Show HN”板块，该板块通常是开发者向技术社区展示个人作品的平台。

该应用是一个交互式 3D 模拟程序，允许用户虚拟游览现实世界中的村庄。根据现有信息，该项目与切尔韦尔谷（Cherwell Valley）地区相关，并特别提到了切尔韦尔谷汽车俱乐部（Cherwell Valley Motor Club）。

尽管目前提供的内容较少且显示处于“加载中……”状态，但该工具的主要目标是通过本地化的 3D 环境提供沉浸式的网页端驾驶体验，这可能是利用地图数据或自定义 3D 建模来还原村庄的地形与道路。

---

## 6. 苹果在 9 年后将我的开源应用从欧盟 App Store 下架

**原文标题**: Apple removed my open-source app from EU App Stores after 9 years

**原文链接**: [https://github.com/glushchenko/fsnotes/discussions/2056](https://github.com/glushchenko/fsnotes/discussions/2056)

乌克兰开发者 Oleksandr Glushchenko 报告称，苹果公司在开源笔记应用 **FSNotes** 上架九年后，已将其从所有欧洲 App Store 中移除。此次下架并未给出明确解释，苹果公司同时还扣留了该开发者 10 月份的销售款项。

尽管 Glushchenko 是乌克兰合法注册的个体经营者，并已提交所有必要的合规文件（包括针对《欧盟数字服务法案》(DSA) 的要求），但他表示，自 2026 年 11 月 5 日以来，苹果公司一直对其支持请求置之不理。

该开发者强调了这种行政沉默带来的严重影响，指出突然下架抹去了应用的搜索排名、曝光率和声誉，正在摧毁近十年的发展成果。Glushchenko 强调，虽然 FSNotes 在 GitHub 上仍然保持免费且开源，但 App Store 收入的损失危及了项目的长期可持续性。他还对乌克兰开发者面临的独特困难表示沮丧，感觉自己的业务正受到对待受制裁国家般的严苛审查。

Glushchenko 的公开信旨在请求苹果公司审查其文件并提供透明的解决途径。他呼吁科技界分享他的遭遇，以引起 App Store 团队的关注，并直言这种做法“正在扼杀独立开发”。

---

## 7. 不要将 SSH 密钥保存在磁盘上

**原文标题**: Don't keep your SSH keys on disk

**原文链接**: [https://jola.dev/posts/you-cant-afford-ssh-keys-disk](https://jola.dev/posts/you-cant-afford-ssh-keys-disk)

In this article, Johanna Larsson argues that storing private SSH keys directly on a computer's disk is a security risk, as they can be exfiltrated by malicious code. To mitigate this exposure, she details a transition to using Bitwarden’s SSH agent to manage keys securely.

**Key Implementation Steps:**
*   **Storage:** Import existing private keys into Bitwarden and delete the local files from the disk.
*   **Configuration:** Enable the "SSH agent" feature within Bitwarden’s app settings.
*   **System Integration:** Update the `~/.ssh/config` file to point the `IdentityAgent` to the Bitwarden socket (`~/.bitwarden-ssh-agent.sock`) and export the `SSH_AUTH_SOCK` environment variable in the terminal configuration (e.g., `.zshrc`).
*   **Authentication:** Set the vault to prompt for permission at preferred intervals, allowing for a balance between security and convenience, often using biometric authentication like Touch ID to unlock the vault.

**Additional Benefits:**
The author also advocates for using SSH keys for Git commit signing instead of traditional GPG keys. By configuring Git to use the SSH agent for signatures, users can prove authorship of their code. This setup ensures that creating a commit and pushing it to a repository require separate authorizations, adding an extra layer of security.

**Conclusion:**
Larsson concludes that while there are minor ergonomic hurdles—such as the desire for better keyboard/biometric shortcuts for specific "approve" prompts—the shift away from disk-based keys provides significant peace of mind with minimal disruption to daily workflows.

---

## 8. 整数与指针的区别是什么？ (2018)

**原文标题**: What's the difference between an integer and a pointer? (2018)

**原文链接**: [https://blog.regehr.org/archives/1621](https://blog.regehr.org/archives/1621)

生成摘要时出错

---

## 9. 是的，1700万行Lean代码确实很多。

**原文标题**: Yes, 17M lines of Lean is a lot

**原文链接**: [https://micjm.com/blog/yes-17m-lines-of-lean-is-a-lot/](https://micjm.com/blog/yes-17m-lines-of-lean-is-a-lot/)

This article explores whether the 17 million lines of Lean code used in the recent proof of the Riemann hypothesis is as massive as it sounds by comparing it to existing Lean repositories.

The author investigated two primary sources:
*   **Mathlib:** This collection of famous human-generated proofs contains over 250 Lean files, none of which come close to the 17-million-line mark.
*   **Reservoir:** A registry of over 900 Lean packages, including AI-assisted projects. While a few projects exceed 17 million lines, they often consist of script-generated data checks or massive AI-produced outputs. For example, an AI-generated proof of Fermat’s Last Theorem reached 27 million lines—roughly 450 times longer than the 60,000-line human-led project it was based on.

The author concludes that 17 million lines is indeed an extraordinary scale. The data suggests a growing divide between human-comprehensible proofs and AI-generated versions, where the latter can be hundreds of times more verbose than human-written code.

---

## 10. The horse made the state

**原文标题**: The horse made the state

**原文链接**: [https://aeon.co/essays/the-origins-of-the-state-are-not-agrarian-but-pastoralist](https://aeon.co/essays/the-origins-of-the-state-are-not-agrarian-but-pastoralist)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-11-24](output/hacker_news_summary_2026-11-24.md) |
| 2 | [2026-11-22](output/hacker_news_summary_2026-11-22.md) |
| 3 | [2026-11-19](output/hacker_news_summary_2026-11-19.md) |
| 4 | [2026-11-21](output/hacker_news_summary_2026-11-21.md) |
| 5 | [2026-11-18](output/hacker_news_summary_2026-11-18.md) |
| 6 | [2026-11-20](output/hacker_news_summary_2026-11-20.md) |
| 7 | [2026-11-14](output/hacker_news_summary_2026-11-14.md) |
| 8 | [2026-11-15](output/hacker_news_summary_2026-11-15.md) |
| 9 | [2026-11-13](output/hacker_news_summary_2026-11-13.md) |
| 10 | [2026-11-17](output/hacker_news_summary_2026-11-17.md) |
| 11 | [2026-11-07](output/hacker_news_summary_2026-11-07.md) |
| 12 | [2026-11-11](output/hacker_news_summary_2026-11-11.md) |
| 13 | [2026-11-08](output/hacker_news_summary_2026-11-08.md) |
| 14 | [2026-11-12](output/hacker_news_summary_2026-11-12.md) |
| 15 | [2026-11-10](output/hacker_news_summary_2026-11-10.md) |
| 16 | [2026-11-01](output/hacker_news_summary_2026-11-01.md) |
| 17 | [2026-11-06](output/hacker_news_summary_2026-11-06.md) |
| 18 | [2026-11-03](output/hacker_news_summary_2026-11-03.md) |
| 19 | [2026-11-05](output/hacker_news_summary_2026-11-05.md) |
| 20 | [2026-11-04](output/hacker_news_summary_2026-11-04.md) |
| 21 | [2026-10-27](output/hacker_news_summary_2026-10-27.md) |
| 22 | [2026-10-28](output/hacker_news_summary_2026-10-28.md) |
| 23 | [2026-10-29](output/hacker_news_summary_2026-10-29.md) |
| 24 | [2026-10-31](output/hacker_news_summary_2026-10-31.md) |
| 25 | [2026-10-30](output/hacker_news_summary_2026-10-30.md) |
| 26 | [2026-10-24](output/hacker_news_summary_2026-10-24.md) |
| 27 | [2026-10-23](output/hacker_news_summary_2026-10-23.md) |
| 28 | [2026-10-25](output/hacker_news_summary_2026-10-25.md) |
| 29 | [2026-10-22](output/hacker_news_summary_2026-10-22.md) |
| 30 | [2026-10-26](output/hacker_news_summary_2026-10-26.md) |
| 31 | [2026-10-19](output/hacker_news_summary_2026-10-19.md) |
| 32 | [2026-10-18](output/hacker_news_summary_2026-10-18.md) |
| 33 | [2026-10-17](output/hacker_news_summary_2026-10-17.md) |
| 34 | [2026-10-21](output/hacker_news_summary_2026-10-21.md) |
| 35 | [2026-10-20](output/hacker_news_summary_2026-10-20.md) |
| 36 | [2026-10-13](output/hacker_news_summary_2026-10-13.md) |
| 37 | [2026-10-11](output/hacker_news_summary_2026-10-11.md) |
| 38 | [2026-10-15](output/hacker_news_summary_2026-10-15.md) |
| 39 | [2026-10-14](output/hacker_news_summary_2026-10-14.md) |
| 40 | [2026-10-12](output/hacker_news_summary_2026-10-12.md) |
| 41 | [2026-10-16](output/hacker_news_summary_2026-10-16.md) |
| 42 | [2026-10-09](output/hacker_news_summary_2026-10-09.md) |
| 43 | [2026-10-07](output/hacker_news_summary_2026-10-07.md) |
| 44 | [2026-10-08](output/hacker_news_summary_2026-10-08.md) |
| 45 | [2026-10-10](output/hacker_news_summary_2026-10-10.md) |
| 46 | [2026-10-06](output/hacker_news_summary_2026-10-06.md) |
| 47 | [2026-10-03](output/hacker_news_summary_2026-10-03.md) |
| 48 | [2026-10-02](output/hacker_news_summary_2026-10-02.md) |
| 49 | [2026-10-05](output/hacker_news_summary_2026-10-05.md) |
| 50 | [2026-10-01](output/hacker_news_summary_2026-10-01.md) |
| 51 | [2026-10-04](output/hacker_news_summary_2026-10-04.md) |
| 52 | [2026-09-29](output/hacker_news_summary_2026-09-29.md) |
| 53 | [2026-09-30](output/hacker_news_summary_2026-09-30.md) |
| 54 | [2026-09-25](output/hacker_news_summary_2026-09-25.md) |
| 55 | [2026-09-27](output/hacker_news_summary_2026-09-27.md) |
| 56 | [2026-09-26](output/hacker_news_summary_2026-09-26.md) |
| 57 | [2026-09-28](output/hacker_news_summary_2026-09-28.md) |
| 58 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 59 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 60 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 61 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 62 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 63 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 64 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 65 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 66 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 67 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 68 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 69 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 70 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 71 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 72 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 73 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 74 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 75 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 76 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 77 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 78 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 79 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 80 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 81 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 82 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 83 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 84 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 85 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 86 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 87 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 88 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 89 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 90 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 91 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 92 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 93 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 94 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 95 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 96 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 97 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 98 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 99 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 100 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 101 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 102 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 103 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 104 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 105 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 106 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 107 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 108 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 109 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 110 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 111 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 112 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 113 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 114 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 115 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 116 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 117 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 118 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 119 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 120 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 121 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 122 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 123 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 124 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 125 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 126 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 127 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 128 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 129 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 130 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 131 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 132 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 133 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 134 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 135 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 136 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 137 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 138 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 139 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 140 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 141 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 142 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 143 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 144 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 145 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 146 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 147 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 148 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 149 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 150 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 151 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 152 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 153 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 154 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 155 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 156 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 157 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 158 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 159 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 160 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 161 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 162 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 163 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 164 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 165 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 166 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 167 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 168 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 169 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 170 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 171 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 172 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 173 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 174 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 175 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 176 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 177 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 178 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 179 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 180 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 181 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 182 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 183 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 184 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 185 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 186 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 187 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 188 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 189 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 190 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 191 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 192 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 193 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 194 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 195 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 196 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 197 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 198 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 199 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 200 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 201 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 202 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 203 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 204 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 205 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 206 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 207 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 208 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 209 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 210 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 211 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 212 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 213 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 214 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 215 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 216 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 217 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 218 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 219 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 220 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 221 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 222 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 223 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 224 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 225 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 226 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 227 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 228 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 229 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 230 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 231 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 232 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 233 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 234 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 235 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 236 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 237 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 238 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 239 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 240 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 241 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 242 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 243 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 244 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 245 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 246 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 247 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 248 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 249 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 250 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 251 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 252 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 253 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 254 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 255 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 256 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 257 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 258 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 259 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 260 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 261 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 262 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 263 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 264 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 265 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 266 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 267 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 268 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 269 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 270 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 271 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 272 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 273 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 274 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 275 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 276 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 277 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 278 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 279 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 280 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 281 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 282 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 283 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 284 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 285 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 286 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 287 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 288 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 289 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 290 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 291 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 292 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 293 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 294 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 295 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 296 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 297 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 298 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 299 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 300 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 301 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 302 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 303 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 304 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 305 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 306 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 307 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 308 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 309 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 310 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 311 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 312 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 313 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 314 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 315 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 316 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 317 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 318 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 319 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 320 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 321 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 322 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 323 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 324 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 325 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 326 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 327 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 328 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 329 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 330 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 331 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 332 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 333 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 334 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 335 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 336 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 337 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 338 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 339 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 340 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 341 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 342 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 343 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 344 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 345 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 346 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 347 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 348 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 349 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 350 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 351 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 352 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 353 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 354 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 355 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 356 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 357 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 358 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 359 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 360 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 361 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 362 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 363 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 364 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 365 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 366 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 367 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 368 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 369 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 370 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 371 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 372 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 373 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 374 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 375 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 376 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 377 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 378 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 379 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 380 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 381 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 382 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 383 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 384 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 385 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 386 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 387 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 388 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 389 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 390 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 391 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 392 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 393 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 394 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 395 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 396 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 397 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 398 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 399 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 400 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 401 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 402 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 403 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 404 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 405 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 406 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 407 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 408 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 409 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 410 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 411 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 412 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 413 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 414 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 415 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 416 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 417 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 418 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 419 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 420 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 421 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 422 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 423 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 424 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 425 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 426 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 427 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 428 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 429 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 430 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 431 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 432 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 433 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 434 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 435 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 436 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 437 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 438 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 439 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 440 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 441 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 442 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 443 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 444 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 445 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 446 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 447 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 448 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 449 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 450 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 451 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 452 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 453 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 454 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 455 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 456 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 457 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 458 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 459 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 460 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 461 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 462 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 463 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 464 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 465 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 466 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 467 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 468 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 469 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 470 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 471 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 472 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 473 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 474 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 475 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 476 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 477 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 478 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 479 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 480 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 481 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 482 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 483 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 484 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 485 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 486 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 487 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 488 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 489 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 490 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 491 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 492 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 493 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 494 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 495 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 496 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 497 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 498 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 499 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 500 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 501 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 502 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 503 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 504 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 505 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 506 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 507 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 508 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 509 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 510 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 511 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 512 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 513 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 514 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 515 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 516 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 517 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 518 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 519 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 520 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 521 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 522 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 523 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 524 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 525 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 526 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 527 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 528 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 529 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 530 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 531 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 532 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 533 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 534 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 535 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 536 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 537 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 538 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 539 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 540 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 541 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 542 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 543 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 544 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 545 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 546 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 547 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 548 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 549 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 550 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 551 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 552 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 553 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 554 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 555 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 556 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 557 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 558 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 559 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 560 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 561 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 562 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 563 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 564 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 565 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 566 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 567 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 568 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 569 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 570 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 571 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 572 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 573 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 574 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 575 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 576 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 577 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 578 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 579 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 580 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 581 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 582 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 583 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 584 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 585 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 586 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 587 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 588 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 589 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 590 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 591 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 592 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 593 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 594 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 595 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 596 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 597 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 598 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 599 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 600 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 601 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 602 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 603 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 604 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 605 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 606 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 607 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 608 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
