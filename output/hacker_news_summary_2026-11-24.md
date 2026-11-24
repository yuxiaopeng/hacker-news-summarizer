# Hacker News 热门文章摘要 (2026-11-24)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. New York Bans Subscription and Post-Purchase Fees on Cars

**原文标题**: New York Bans Subscription and Post-Purchase Fees on Cars

**原文链接**: [https://www.governor.ny.gov/news/money-your-pockets-governor-hochul-signs-bill-restricting-exploitative-vehicle-subscription](https://www.governor.ny.gov/news/money-your-pockets-governor-hochul-signs-bill-restricting-exploitative-vehicle-subscription)

生成摘要时出错

---

## 12. Let's Meet in the Middle

**原文标题**: Let's Meet in the Middle

**原文链接**: [https://george.mand.is/2026/11/lets-meet-in-the-middle/](https://george.mand.is/2026/11/lets-meet-in-the-middle/)

生成摘要时出错

---

## 13. Elixir HLS makes FPGA circuits from functions written in Elixir

**原文标题**: Elixir HLS makes FPGA circuits from functions written in Elixir

**原文链接**: [https://github.com/elixir-hls/elixir-hls](https://github.com/elixir-hls/elixir-hls)

生成摘要时出错

---

## 14. You Can Seize Everything (The U.S. is reviving pirate law)

**原文标题**: You Can Seize Everything (The U.S. is reviving pirate law)

**原文链接**: [https://www.npr.org/2026/11/20/nx-s1-6049085/iran-oil-tanker-prize-law-court](https://www.npr.org/2026/11/20/nx-s1-6049085/iran-oil-tanker-prize-law-court)

生成摘要时出错

---

## 15. The Beauty of Artists' Studios

**原文标题**: The Beauty of Artists' Studios

**原文链接**: [https://spectator.com/article/the-beauty-of-artists-studios/](https://spectator.com/article/the-beauty-of-artists-studios/)

生成摘要时出错

---

## 16. Show HN: PlaceBench – Testing AI on opening and closing hours (and last trains)

**原文标题**: Show HN: PlaceBench – Testing AI on opening and closing hours (and last trains)

**原文链接**: [https://github.com/voygr-tech/placebench](https://github.com/voygr-tech/placebench)

生成摘要时出错

---

## 17. Crafting Targeted MP4 Fuzzers

**原文标题**: Crafting Targeted MP4 Fuzzers

**原文链接**: [https://atredis.com/blog/2026/11/16/crafting-targeted-mp4-fuzzers/](https://atredis.com/blog/2026/11/16/crafting-targeted-mp4-fuzzers/)

生成摘要时出错

---

## 18. Brake Check: Hijacking Trailer Brakes over Bluetooth

**原文标题**: Brake Check: Hijacking Trailer Brakes over Bluetooth

**原文链接**: [https://elementdigital.com.au/blog/brake-check-trailer-brakes-over-bluetooth/](https://elementdigital.com.au/blog/brake-check-trailer-brakes-over-bluetooth/)

生成摘要时出错

---

## 19. Was software just always too complex for humans?

**原文标题**: Was software just always too complex for humans?

**原文链接**: [https://anil.recoil.org/notes/software-too-complex-for-humans](https://anil.recoil.org/notes/software-too-complex-for-humans)

生成摘要时出错

---

## 20. MRAM Basics: How Magnetic Memory Is Replacing Embedded Flash

**原文标题**: MRAM Basics: How Magnetic Memory Is Replacing Embedded Flash

**原文链接**: [https://www.allaboutcircuits.com/technical-articles/mram-basics-how-magnetic-memory-is-replacing-embedded-flash/](https://www.allaboutcircuits.com/technical-articles/mram-basics-how-magnetic-memory-is-replacing-embedded-flash/)

生成摘要时出错

---

## 21. Cyberleek posted the GTA 6 Xbox build executable

**原文标题**: Cyberleek posted the GTA 6 Xbox build executable

**原文链接**: [https://www.reddit.com/r/GamingLeaksAndRumours/comments/1y3jzqe/cyberleek_posted_the_gta_6_xbox_build_executable/](https://www.reddit.com/r/GamingLeaksAndRumours/comments/1y3jzqe/cyberleek_posted_the_gta_6_xbox_build_executable/)

生成摘要时出错

---

## 22. Levent Alpöge comments on his Riemann Hypothesis proof

**原文标题**: Levent Alpöge comments on his Riemann Hypothesis proof

**原文链接**: [https://twitter.com/__alpoge__/status/2124987173439209561](https://twitter.com/__alpoge__/status/2124987173439209561)

生成摘要时出错

---

## 23. Show HN: Hermit CRM – Free open-source CRM for solopreneurs

**原文标题**: Show HN: Hermit CRM – Free open-source CRM for solopreneurs

**原文链接**: [https://hermitcrm.io/](https://hermitcrm.io/)

生成摘要时出错

---

## 24. Americans Trust Neither Republicans nor Democrats to Protect Free Speech

**原文标题**: Americans Trust Neither Republicans nor Democrats to Protect Free Speech

**原文链接**: [https://reason.com/2026/11/20/americans-trust-neither-republicans-nor-democrats-to-protect-free-speech/](https://reason.com/2026/11/20/americans-trust-neither-republicans-nor-democrats-to-protect-free-speech/)

生成摘要时出错

---

## 25. Claude Ship

**原文标题**: Claude Ship

**原文链接**: [https://claude.com/resources/articles/introducing-claude-ship](https://claude.com/resources/articles/introducing-claude-ship)

生成摘要时出错

---

## 26. Anatomia Di Tor – The Tor Protocol, Byte by Byte

**原文标题**: Anatomia Di Tor – The Tor Protocol, Byte by Byte

**原文链接**: [https://github.com/aleff-github/onion-routing-anatomy](https://github.com/aleff-github/onion-routing-anatomy)

生成摘要时出错

---

## 27. Short Nvidia Fund Halted After 91% Wipeout

**原文标题**: Short Nvidia Fund Halted After 91% Wipeout

**原文链接**: [https://www.wsj.com/livecoverage/stock-market-today-dow-sp-500-nasdaq-11-23-2026/card/short-nvidia-fund-halted-after-91-wipeout-myoKEHNFkGcseucDUC48](https://www.wsj.com/livecoverage/stock-market-today-dow-sp-500-nasdaq-11-23-2026/card/short-nvidia-fund-halted-after-91-wipeout-myoKEHNFkGcseucDUC48)

生成摘要时出错

---

## 28. Mutex poisoning is not for everyone

**原文标题**: Mutex poisoning is not for everyone

**原文链接**: [https://bertptrs.nl/2026/11/16/mutex-poisoning-is-not-for-everyone.html](https://bertptrs.nl/2026/11/16/mutex-poisoning-is-not-for-everyone.html)

生成摘要时出错

---

## 29. XNU Linux: Full OS X GUI Userspace on Linux

**原文标题**: XNU Linux: Full OS X GUI Userspace on Linux

**原文链接**: [https://github.com/AFK-surf/xnulinux](https://github.com/AFK-surf/xnulinux)

生成摘要时出错

---

## 30. VisualDrive Server – drop-in replacement for Sharepoint/OneDrive

**原文标题**: VisualDrive Server – drop-in replacement for Sharepoint/OneDrive

**原文链接**: [https://www.axiorema.com/visualdrive-server/](https://www.axiorema.com/visualdrive-server/)

生成摘要时出错

---

## 31. Treemap of the Riemann Hypothesis Lean Proof

**原文标题**: Treemap of the Riemann Hypothesis Lean Proof

**原文链接**: [https://pengowray.github.io/riemann-zeta-proof-visualizer/](https://pengowray.github.io/riemann-zeta-proof-visualizer/)

生成摘要时出错

---

## 32. A Beginner's Guide to Local AI with Inkling, Qwen, and Unsloth

**原文标题**: A Beginner's Guide to Local AI with Inkling, Qwen, and Unsloth

**原文链接**: [https://www.gpupartner.com/blog/beginners-guide-local-ai-inkling-qwen-unsloth](https://www.gpupartner.com/blog/beginners-guide-local-ai-inkling-qwen-unsloth)

生成摘要时出错

---

## 33. Amazon drone crashes into house after delivering shampoo

**原文标题**: Amazon drone crashes into house after delivering shampoo

**原文链接**: [https://www.freep.com/story/news/local/michigan/2026/11/22/ntsb-weighs-probe-of-amazon-drone-crash-in-huntington-woods/92915982007/](https://www.freep.com/story/news/local/michigan/2026/11/22/ntsb-weighs-probe-of-amazon-drone-crash-in-huntington-woods/92915982007/)

生成摘要时出错

---

## 34. Reviving the Donkey Car with Erlang

**原文标题**: Reviving the Donkey Car with Erlang

**原文链接**: [https://underjord.io/reviving-the-donkey-car-with-erlang.html](https://underjord.io/reviving-the-donkey-car-with-erlang.html)

生成摘要时出错

---

## 35. AI is massively speeding up AI research

**原文标题**: AI is massively speeding up AI research

**原文链接**: [https://linch.substack.com/p/ai-is-already-massively-speeding](https://linch.substack.com/p/ai-is-already-massively-speeding)

生成摘要时出错

---

## 36. Toyota, Nissan, and Honda to standardize parts to lower costs

**原文标题**: Toyota, Nissan, and Honda to standardize parts to lower costs

**原文链接**: [https://www.caranddriver.com/news/a74490092/toyota-nissan-honda-standardize-parts-lower-costs/](https://www.caranddriver.com/news/a74490092/toyota-nissan-honda-standardize-parts-lower-costs/)

生成摘要时出错

---

## 37. Vibed – describe an app, then keep changing it

**原文标题**: Vibed – describe an app, then keep changing it

**原文链接**: [https://github.com/frazik-main/.vibed](https://github.com/frazik-main/.vibed)

生成摘要时出错

---

## 38. GL.iNet Security Notice 2026-11-20

**原文标题**: GL.iNet Security Notice 2026-11-20

**原文链接**: [https://www.gl-inet.com/en-us/blogs/blog/glinet-security-notice-2026-11-20](https://www.gl-inet.com/en-us/blogs/blog/glinet-security-notice-2026-11-20)

生成摘要时出错

---

## 39. Show HN: Amni-CAD – parametric CAD with stress and flow simulation in a browser

**原文标题**: Show HN: Amni-CAD – parametric CAD with stress and flow simulation in a browser

**原文链接**: [https://amni-scient.com/amni-cad](https://amni-scient.com/amni-cad)

生成摘要时出错

---

## 40. The New Docker: Built to Run on Trust

**原文标题**: The New Docker: Built to Run on Trust

**原文链接**: [https://www.docker.com/blog/meet-the-new-docker-built-to-run-on-trust/](https://www.docker.com/blog/meet-the-new-docker-built-to-run-on-trust/)

生成摘要时出错

---

## 41. A Partial Evaluator for C

**原文标题**: A Partial Evaluator for C

**原文链接**: [https://phoenix.labri.fr/software/tempo/](https://phoenix.labri.fr/software/tempo/)

生成摘要时出错

---

## 42. The struggle for freedom: How BSD escaped AT&T licensing

**原文标题**: The struggle for freedom: How BSD escaped AT&T licensing

**原文链接**: [https://fosscomics.com/posts/16.%20BSD%20Unix%20Part%206%20-%20The%20Struggle%20for%20Freedom/](https://fosscomics.com/posts/16.%20BSD%20Unix%20Part%206%20-%20The%20Struggle%20for%20Freedom/)

生成摘要时出错

---

## 43. Perplexity and Intelligence

**原文标题**: Perplexity and Intelligence

**原文链接**: [https://openai.com/index/perplexity-and-intelligence/](https://openai.com/index/perplexity-and-intelligence/)

生成摘要时出错

---

## 44. The Birds of GTA 6: A Field Guide to Vice City and Leonida's Wildlife

**原文标题**: The Birds of GTA 6: A Field Guide to Vice City and Leonida's Wildlife

**原文链接**: [https://www.audubon.org/magazine/birds-of-gta-6-field-guide-vice-city-wildlife](https://www.audubon.org/magazine/birds-of-gta-6-field-guide-vice-city-wildlife)

生成摘要时出错

---

## 45. The Usefulness of Useless Knowledge [pdf] (1939)

**原文标题**: The Usefulness of Useless Knowledge [pdf] (1939)

**原文链接**: [https://www.ias.edu/sites/default/files/library/UsefulnessHarpers.pdf](https://www.ias.edu/sites/default/files/library/UsefulnessHarpers.pdf)

生成摘要时出错

---

## 46. Two "suspicious clusters" on Polymarket Made Over $340k on Huang Comeback

**原文标题**: Two "suspicious clusters" on Polymarket Made Over $340k on Huang Comeback

**原文链接**: [https://www.wsj.com/livecoverage/stock-market-today-dow-sp-500-nasdaq-11-23-2026/card/two-groups-of-polymarket-accounts-made-over-340-000-on-huang-comeback-Lan2T0TwbJPNsyhmQHGq](https://www.wsj.com/livecoverage/stock-market-today-dow-sp-500-nasdaq-11-23-2026/card/two-groups-of-polymarket-accounts-made-over-340-000-on-huang-comeback-Lan2T0TwbJPNsyhmQHGq)

生成摘要时出错

---

## 47. Jensen Huang's Apology May Be the Only Correct Use of AI

**原文标题**: Jensen Huang's Apology May Be the Only Correct Use of AI

**原文链接**: [https://www.theatlantic.com/newsletters/2026/11/jensen-huang-ai-apology-nvidia/689366/](https://www.theatlantic.com/newsletters/2026/11/jensen-huang-ai-apology-nvidia/689366/)

生成摘要时出错

---

## 48. You shouldn't do application-level sharding

**原文标题**: You shouldn't do application-level sharding

**原文链接**: [https://planetscale.com/blog/why-you-shouldnt-do-app-level-sharding](https://planetscale.com/blog/why-you-shouldnt-do-app-level-sharding)

生成摘要时出错

---

## 49. Agent swarm trying to solve P vs. NP

**原文标题**: Agent swarm trying to solve P vs. NP

**原文链接**: [https://pequalnp.com/](https://pequalnp.com/)

生成摘要时出错

---

## 50. Pill to treat pancreatic cancer hailed as 'biggest breakthrough in decades'

**原文标题**: Pill to treat pancreatic cancer hailed as 'biggest breakthrough in decades'

**原文链接**: [https://www.theguardian.com/society/2026/nov/20/pill-pancreatic-cancer-breakthrough-daraxonrasib](https://www.theguardian.com/society/2026/nov/20/pill-pancreatic-cancer-breakthrough-daraxonrasib)

生成摘要时出错

---

## 51. Dirac's Theorem at a Dinner Party

**原文标题**: Dirac's Theorem at a Dinner Party

**原文链接**: [https://prideout.net/blog/dirac-dinner-party/](https://prideout.net/blog/dirac-dinner-party/)

生成摘要时出错

---

## 52. Jon's Arm Reference will be discontinued on 4 Dec, per request of Arm's legal

**原文标题**: Jon's Arm Reference will be discontinued on 4 Dec, per request of Arm's legal

**原文链接**: [https://twitter.com/jonpalmisc/status/2124924098057011629](https://twitter.com/jonpalmisc/status/2124924098057011629)

生成摘要时出错

---

## 53. Cathedral floor emerges in Sudan, revealing one of the biggest medieval churches

**原文标题**: Cathedral floor emerges in Sudan, revealing one of the biggest medieval churches

**原文链接**: [https://apnews.com/article/sudan-antiquities-nubia-cathedral-1b16f67da881ee5592de4481ee55c527](https://apnews.com/article/sudan-antiquities-nubia-cathedral-1b16f67da881ee5592de4481ee55c527)

生成摘要时出错

---

## 54. What Happened to Silicon Valley?

**原文标题**: What Happened to Silicon Valley?

**原文链接**: [https://www.oreilly.com/radar/what-happened-to-silicon-valley/](https://www.oreilly.com/radar/what-happened-to-silicon-valley/)

生成摘要时出错

---

## 55. Nyx, the Oldest Internet Service Provider

**原文标题**: Nyx, the Oldest Internet Service Provider

**原文链接**: [https://nyx.net/](https://nyx.net/)

生成摘要时出错

---

## 56. One man's quest to end daylight savings

**原文标题**: One man's quest to end daylight savings

**原文链接**: [https://www.newyorker.com/magazine/2026/11/30/one-mans-quest-to-end-daylight-savings](https://www.newyorker.com/magazine/2026/11/30/one-mans-quest-to-end-daylight-savings)

生成摘要时出错

---

## 57. Support for Office 2021 has ended

**原文标题**: Support for Office 2021 has ended

**原文链接**: [https://diamondgeezer.blogspot.com/2026/10/support-for-office-2021-has-ended.html](https://diamondgeezer.blogspot.com/2026/10/support-for-office-2021-has-ended.html)

生成摘要时出错

---

## 58. 16-Year-Old Founded an AI Missile Startup. He's Targeting 'Cost per Kill'

**原文标题**: 16-Year-Old Founded an AI Missile Startup. He's Targeting 'Cost per Kill'

**原文链接**: [https://www.wired.com/story/henrijs-dandzbergs-polemos-missiles-ai-warfare/](https://www.wired.com/story/henrijs-dandzbergs-polemos-missiles-ai-warfare/)

生成摘要时出错

---

## 59. Why is there no thank you emoji?

**原文标题**: Why is there no thank you emoji?

**原文链接**: [https://jenniferdaniel.substack.com/p/thank-you-for-not-smashing-delete](https://jenniferdaniel.substack.com/p/thank-you-for-not-smashing-delete)

生成摘要时出错

---

## 60. The AI bubble hasn't burst, but it has significantly deflated

**原文标题**: The AI bubble hasn't burst, but it has significantly deflated

**原文链接**: [https://www.rnz.co.nz/news/world/2757034/the-ai-bubble-hasn-t-burst-but-it-has-significantly-deflated](https://www.rnz.co.nz/news/world/2757034/the-ai-bubble-hasn-t-burst-but-it-has-significantly-deflated)

生成摘要时出错

---

## 61. Assume People Are Not Interested in Your Blog Post

**原文标题**: Assume People Are Not Interested in Your Blog Post

**原文链接**: [https://danielsada.tech/blog/assume-people-are-not-interested-in-your-blog-post/](https://danielsada.tech/blog/assume-people-are-not-interested-in-your-blog-post/)

生成摘要时出错

---

## 62. Rust GPUI-Kit with components

**原文标题**: Rust GPUI-Kit with components

**原文链接**: [https://gpui-kit.com/](https://gpui-kit.com/)

生成摘要时出错

---

## 63. Ladybird's First Alpha Release

**原文标题**: Ladybird's First Alpha Release

**原文链接**: [https://simonwillison.net/2026/Nov/23/ladybird/](https://simonwillison.net/2026/Nov/23/ladybird/)

生成摘要时出错

---

## 64. Earth's ozone hole has grown to a size not seen in a decade

**原文标题**: Earth's ozone hole has grown to a size not seen in a decade

**原文链接**: [https://www.sciencedaily.com/releases/2026/11/261110042546.htm](https://www.sciencedaily.com/releases/2026/11/261110042546.htm)

生成摘要时出错

---

## 65. Verifying formal models of Raft implementations

**原文标题**: Verifying formal models of Raft implementations

**原文链接**: [https://antithesis.com/blog/2026/verifying-formal-models/](https://antithesis.com/blog/2026/verifying-formal-models/)

生成摘要时出错

---

## 66. Show HN: Console.tty – terminal emulator in browser console

**原文标题**: Show HN: Console.tty – terminal emulator in browser console

**原文链接**: [https://github.com/cpendery/console.tty](https://github.com/cpendery/console.tty)

生成摘要时出错

---

## 67. 87% of the Anthropic power will come from gas and 11% from coal in 2028

**原文标题**: 87% of the Anthropic power will come from gas and 11% from coal in 2028

**原文链接**: [https://betterdatacenterproject.com/2026/11/16/how-ai-is-powered-a-breakdown-of-byop-and-grid-power/](https://betterdatacenterproject.com/2026/11/16/how-ai-is-powered-a-breakdown-of-byop-and-grid-power/)

生成摘要时出错

---

## 68. I joined the NTP Pool, but not with my Stratum 1 Pi

**原文标题**: I joined the NTP Pool, but not with my Stratum 1 Pi

**原文链接**: [https://www.jeffgeerling.com/blog/2026/i-joined-the-ntp-pool/](https://www.jeffgeerling.com/blog/2026/i-joined-the-ntp-pool/)

生成摘要时出错

---

## 69. Masullo on the Riemann Hypothesis

**原文标题**: Masullo on the Riemann Hypothesis

**原文链接**: [https://johncarlosbaez.wordpress.com/2026/11/22/masullo-on-the-riemann-hypothesis/](https://johncarlosbaez.wordpress.com/2026/11/22/masullo-on-the-riemann-hypothesis/)

生成摘要时出错

---

## 70. Show HN: Narayanastra – agentless Linux rootkit scanner (eBPF, io_uring) in Rust

**原文标题**: Show HN: Narayanastra – agentless Linux rootkit scanner (eBPF, io_uring) in Rust

**原文链接**: [https://github.com/Tekush1/narayanastra](https://github.com/Tekush1/narayanastra)

生成摘要时出错

---

## 71. Show HN: Lightweight Agentic CMS on Cloudflare – API, MCP, CLI, Web

**原文标题**: Show HN: Lightweight Agentic CMS on Cloudflare – API, MCP, CLI, Web

**原文链接**: [https://docs.microfeed.org/](https://docs.microfeed.org/)

生成摘要时出错

---

## 72. A Better Vocabulary for Testing

**原文标题**: A Better Vocabulary for Testing

**原文链接**: [https://alperenkeles.com/posts/vocab-for-testing/](https://alperenkeles.com/posts/vocab-for-testing/)

生成摘要时出错

---

## 73. Lean verification of the Riemann Hypothesis

**原文标题**: Lean verification of the Riemann Hypothesis

**原文链接**: [https://leanprover-community.github.io/blog/posts/riemann-hypothesis/](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)

生成摘要时出错

---

## 74. LittleBit: Ultra Low-Bit Quantization via Latent Factorization (2025)

**原文标题**: LittleBit: Ultra Low-Bit Quantization via Latent Factorization (2025)

**原文链接**: [https://arxiv.org/abs/2506.13771](https://arxiv.org/abs/2506.13771)

生成摘要时出错

---

## 75. 0rwx – A simple model of AI usage, inspired by Unix permissions

**原文标题**: 0rwx – A simple model of AI usage, inspired by Unix permissions

**原文链接**: [https://0rwx.com/](https://0rwx.com/)

生成摘要时出错

---

## 76. Wikipedia explainers lost a median 40% of views since 2022, biographies lost 9%

**原文标题**: Wikipedia explainers lost a median 40% of views since 2022, biographies lost 9%

**原文链接**: [https://growtika.com/blog/wikipedia-traffic-study](https://growtika.com/blog/wikipedia-traffic-study)

生成摘要时出错

---

## 77. Progress map for the Lean formalization of Alessandro Masullo's manuscript

**原文标题**: Progress map for the Lean formalization of Alessandro Masullo's manuscript

**原文链接**: [https://claude.ai/artifact/CtQyX8qfYAF822bgHJHHE3](https://claude.ai/artifact/CtQyX8qfYAF822bgHJHHE3)

生成摘要时出错

---

## 78. Levent Alpöge claims proof of the Generalized Riemann Hypothesis [pdf]

**原文标题**: Levent Alpöge claims proof of the Generalized Riemann Hypothesis [pdf]

**原文链接**: [https://alpo.ge/remark.pdf](https://alpo.ge/remark.pdf)

生成摘要时出错

---

## 79. A miniature San Francisco with live buses, planes and boats

**原文标题**: A miniature San Francisco with live buses, planes and boats

**原文链接**: [https://smallsf.com/](https://smallsf.com/)

生成摘要时出错

---

## 80. California Legislators Passed a Bill Targeting ICE Contractors. Newsom Vetoed It

**原文标题**: California Legislators Passed a Bill Targeting ICE Contractors. Newsom Vetoed It

**原文链接**: [https://truthout.org/articles/ca-legislators-passed-a-bill-targeting-ice-contractors-newsom-vetoed-it/](https://truthout.org/articles/ca-legislators-passed-a-bill-targeting-ice-contractors-newsom-vetoed-it/)

生成摘要时出错

---

## 81. Slopstrap – Make your site look hastily vibecoded

**原文标题**: Slopstrap – Make your site look hastily vibecoded

**原文链接**: [https://slopstrap.mikelacher.com/](https://slopstrap.mikelacher.com/)

生成摘要时出错

---

## 82. Apparently Criminals Don't Have Free Will, but Elites Do

**原文标题**: Apparently Criminals Don't Have Free Will, but Elites Do

**原文链接**: [https://www.robkhenderson.com/p/apparently-criminals-dont-have-free](https://www.robkhenderson.com/p/apparently-criminals-dont-have-free)

生成摘要时出错

---

## 83. The AI conversation we're not having

**原文标题**: The AI conversation we're not having

**原文链接**: [https://www.gnanaguru.com/blog/things-two-years-in-ai-taught-me/](https://www.gnanaguru.com/blog/things-two-years-in-ai-taught-me/)

生成摘要时出错

---

## 84. Harvard CS 2881R AI Safety

**原文标题**: Harvard CS 2881R AI Safety

**原文链接**: [https://boazbk.github.io/mltheoryseminar/](https://boazbk.github.io/mltheoryseminar/)

生成摘要时出错

---

## 85. US to blacklist Asian AI firm Megaspeed

**原文标题**: US to blacklist Asian AI firm Megaspeed

**原文链接**: [https://www.bbc.co.uk/news/articles/cv98xpg5dg5zo](https://www.bbc.co.uk/news/articles/cv98xpg5dg5zo)

生成摘要时出错

---

## 86. Norway links energy firm cyberattacks to critical Azure API Management flaw

**原文标题**: Norway links energy firm cyberattacks to critical Azure API Management flaw

**原文链接**: [https://www.theregister.com/security/2026/11/23/norway-links-energy-firm-cyberattacks-to-critical-azure-api-management-flaw/5311598](https://www.theregister.com/security/2026/11/23/norway-links-energy-firm-cyberattacks-to-critical-azure-api-management-flaw/5311598)

生成摘要时出错

---

## 87. Localcode, open source agentic coding on your Mac with one command

**原文标题**: Localcode, open source agentic coding on your Mac with one command

**原文链接**: [https://github.com/mjwsolo/localcode](https://github.com/mjwsolo/localcode)

生成摘要时出错

---

## 88. The Quartz Page

**原文标题**: The Quartz Page

**原文链接**: [http://www.quartzpage.de/index.html](http://www.quartzpage.de/index.html)

"The Quartz Page" is a comprehensive, ongoing digital resource dedicated to the study of the mineral quartz. Its primary objective is to provide an exhaustive database covering the formation, physical properties, and global locations of all quartz varieties.

The content is organized into several key scientific and descriptive categories:

*   **Mineralogy and Properties:** The site offers technical data on the chemical and physical characteristics of quartz, its crystal structure, and its role as a rock-forming mineral within the silica group.
*   **Crystallography:** Detailed sections explain crystal habits, twinning, growth forms, and macroscopic structures, supplemented by renderings and data.
*   **Varieties:** A significant portion of the resource distinguishes between **macrocrystalline** varieties (such as amethyst, citrine, smoky quartz, and rose quartz) and **cryptocrystalline** varieties (including agate, chalcedony, jasper, and onyx).
*   **Special Topics and Locations:** The site explores niche subjects like Alpine-type fissures, inclusions, and specific regional specimens such as Herkimer "diamonds" and Gwindels.

Designed as an educational tool for enthusiasts and researchers alike, the project includes an extensive specimen list, literature references, and an index. As an evolving project, it continues to expand with new sections and updated mineralogical information.

---

