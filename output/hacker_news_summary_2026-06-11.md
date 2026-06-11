# Hacker News 热门文章摘要 (2026-06-11)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 以“受制裁”代码污染 Linux 内核

**原文标题**: Spoiling Linux Kernel with "sanctioned" code

**原文链接**: [https://printserver.ink/blog/spoiling-the-kernel/](https://printserver.ink/blog/spoiling-the-kernel/)

文章《以“受制裁”代码破坏 Linux 内核》探讨了国际地缘政治制裁如何在开源社区内部制造法律障碍。

作者是一位使用 .ru（俄罗斯）域名的开发者，他编写了一个补丁，旨在修复 Linux 内核 OHCI (USB 1.1) 协议栈中一个长期存在的延迟漏洞。尽管该修复方案在技术上是完善的，但却遭到了包括 Greg Kroah-Hartman 在内的核心维护者的冷遇。作者认为，这是由于法律建议警告维护者不要与来自受制裁地区（如俄罗斯、伊朗和朝鲜）的贡献者进行交流，除非这些人能证明自己不隶属于受制裁实体。

作者指出，这种动态以类似于专利侵权的方式“破坏”了 Linux 内核。一旦受制裁国家的贡献者提交了高质量的漏洞修复程序，该特定实现方案就在法律上被“投毒”了。由于社区无法接受来自受制裁来源的代码，而其他开发者也被禁止简单地以自己的名义重新提交或重复使用该特定代码，这导致内核实际上无法采用最直接的问题解决方案。

因此，为了规避法律责任，社区被迫寻找其他效率可能较低的替代方案来修复同样的漏洞。作者总结道，这营造了一种“有罪推定”的环境，即贡献者的来源背景超过了其技术价值，最终阻碍了 Linux 内核的发展。

---

## 2. 游戏机上的网页浏览器

**原文标题**: Web Browsers on Video Game Consoles

**原文链接**: [https://vale.rocks/posts/game-console-browsers](https://vale.rocks/posts/game-console-browsers)

本文探讨了视频游戏机官方网络浏览器的演变，强调了它们早期作为非技术用户经济型互联网入口的作用。

这段历程始于1995年的飞利浦（Philips）CD-i，它提供了一种初步的“简化版互联网”体验。然而，由于内存有限，浏览网页往往会覆盖系统内存，甚至包括游戏存档。1996年，世嘉土星（Sega Saturn）推出了配有PlanetWeb浏览器的Net Link。这是一个重大进步，因为它专门针对电视屏幕进行了优化，支持抗锯齿字体，并具有通过电子邮件发送游戏存档和参与IRC聊天等独特功能。

其他早期尝试还包括苹果万代（Apple Bandai）的Pippin，它运行的是经过“Pippin化”处理的桌面浏览器版本（如Netscape和Internet Explorer）。尽管具备技术实力，但Pippin因成本过高而在商业上宣告失败。任天堂（Nintendo）早期的尝试则更为受限：仅在日本发行的64DD提供了Randnet服务，而Game Boy Color提供的浏览器功能极其有限，只能以黑白形式访问任天堂官方网站。

世嘉Dreamcast标志着早期游戏机浏览器的巅峰，它拥有三个独特的地区版本：Dream Passport（日本）、PlanetWeb（美国）和Dreamkey（欧洲）。通过多次迭代，这些浏览器最终支持了Flash、JavaScript和Java小程序等现代标准。世嘉甚至尝试过小众营销，例如Hello Kitty主题浏览器和“家庭主妇上网”套装。

最后，文章总结道，这些浏览器的发展为我们提供了一个独特的窗口，以此窥见万维网的“稚嫩”时代以及游戏机用户界面的成熟过程。

---

## 3. 变革电源的不是苹果，而是新型晶体管。

**原文标题**: Apple didn't revolutionize power supplies; new transistors did

**原文链接**: [https://www.righto.com/2012/02/apple-didnt-revolutionize-power.html](https://www.righto.com/2012/02/apple-didnt-revolutionize-power.html)

史蒂夫·乔布斯在其传记中声称，罗德·霍尔特（Rod Holt）为 Apple II 设计的开关电源是一项革命性的发明，现代计算机至今仍在“抄袭”这一设计。本文反驳了这一说法，认为电源领域的真正革命是由半导体技术的进步驱动的，而非苹果的设计。

虽然开关电源（SMPS）比传统的线性电源更高效、更小巧、更轻便，但它们并非苹果的发明。这项技术早在 20 世纪 30 年代就已出现，并在 60 年代和 70 年代初期被美国航天局（NASA）、IBM、惠普（HP）和数字设备公司（DEC）广泛使用。到 1977 年 Apple II 发布时，开关电源在小型机、彩色电视以及 Boschert Inc. 等公司的商业产品中已经非常普遍。

作者指出，行业转型的真正催化剂是高压高速开关晶体管的改进，以及 1976 年集成电路（IC）控制器的问世。这些组件简化了开关电源的设计，并使其更具成本效益。

尽管罗德·霍尔特为苹果设计的电源因其创新性（具有交流启动机制和特定的钳位绕组）而获得了专利，但这些特性并未成为行业标准。事实上，行业转向了脉冲宽度调制（PWM）控制器 IC，而苹果在采用这一技术方面实际上动作迟缓，直到 20 世纪 90 年代仍在使用分立元件。最终，现代电源是基于不同的原理和 IC 驱动架构，而非霍尔特的特定电路。Apple II 的电源是对现有趋势的一次成功应用，但它并没有发明支撑当今计算机运行的技术。

---

## 4. OpenAI 拟大幅降价以与 Anthropic 争夺用户

**原文标题**: OpenAI mulls slashing prices as it competes with Anthropic for users

**原文链接**: [https://www.cnbc.com/2026/06/11/openai-mulls-slashing-prices-ahead-of-competition-from-anthropic-wsj.html](https://www.cnbc.com/2026/06/11/openai-mulls-slashing-prices-ahead-of-competition-from-anthropic-wsj.html)

据报道，OpenAI 正考虑大幅下调其人工智能模型的价格，以更好地与竞争对手 Anthropic 竞争。据《华尔街日报》报道，OpenAI 计划降低“token”（用于 AI 使用计费的单位）的成本，以应对 Anthropic 预期的降价举措。

此举正值两家公司竞争加剧之际，双方近期均已提交了首次公开募股（IPO）申请。尽管 OpenAI 长期以来一直是市场领导者，但 Anthropic 的估值近期达到了 9650 亿美元，略高于 OpenAI 在 3 月份 8520 亿美元的估值。目前，OpenAI 对其 GPT-5.5 模型的阶梯订阅费用从每月 8 美元到 100 多美元不等，而 Anthropic 提供的 Claude Pro 服务每月为 17 美元（按年订阅），并设有高端的 Claude Max 档位。

尽管面临定价压力，OpenAI 仍展现出巨大的规模优势。今年 5 月，ChatGPT 成为首个达到 10 亿月活跃用户的应用，仅用三年时间就达成了这一里程碑，增长速度超越了谷歌地图等此前的纪录保持者。这场潜在的价格战标志着 AI 行业进入了一个新阶段，市场份额的争夺不仅取决于技术创新，也取决于激进的定价策略。

---

## 5. 从零构建基础 AI 智能体：长任务规划

**原文标题**: Build a Basic AI Agent from Scratch: Long Task Planning

**原文链接**: [https://medium.com/@rogi23696/build-a-basic-ai-agent-from-scratch-long-task-planning-14e803f9bd6d](https://medium.com/@rogi23696/build-a-basic-ai-agent-from-scratch-long-task-planning-14e803f9bd6d)

在《从零开始构建基础 AI 智能体：长任务规划》中，Roger Oriol 探讨了对话式 AI 智能体在处理复杂、多步骤项目时的局限性。由于大语言模型（LLM）通常针对短文本交互进行了优化，它们往往难以持续关注长期目标。为了解决这一问题，Oriol 引入了一个以两个新工具为核心的自主规划框架：**草稿垫（Scratchpad）**和**待办事项列表（To-do list）**。

**草稿垫**作为一个私有的内存工作区，智能体可以在其中重申目标、梳理现有知识、评估多种方案并预判潜在的失败模式。这种“思维链”过程确保智能体在执行任何行动之前，先对其策略进行逻辑推理。**待办事项列表**则使智能体能够将项目分解为具体步骤并跟踪其状态（如：待处理、进行中、已失败）。该工具强制执行结构化的工作流，包括针对失败任务的重试限制，以及同一时间只能激活一个任务的规则。

该系统的核心组成部分是**经过优化的系统提示词**，它要求智能体：
1. **规划与跟踪：** 分解任务并在每一步之后更新待办事项列表。
2. **重新规划：** 在草稿垫中诊断错误，并在结果偏离预期时调整方向或重试。
3. **验证完成情况：** 使用由三部分组成的“完成检测”流程——验证结构性完成情况、根据原始目标检查输出（如运行测试），以及对未验证的假设进行“不确定性检查”。

通过整合这些规划工具和严谨的系统提示词，智能体从一个简单的聊天机器人演变成了一个能够执行代码库迁移等复杂自主项目的得力助手。

---

## 6. 热力学主宰未来轨道数据中心

**原文标题**: Thermodynamics rules future orbital data centers

**原文链接**: [https://spectrum.ieee.org/orbital-data-centers-heat](https://spectrum.ieee.org/orbital-data-centers-heat)

While tech giants like Nvidia, SpaceX, and Google are racing to establish orbital data centers, a report from ABI Research suggests that the harsh reality of thermodynamics makes space-based computing significantly more difficult and expensive than terrestrial alternatives.

The primary obstacle is **cooling**. In the vacuum of space, conduction and convection are impossible; heat can only be dissipated through radiation. Governed by the Stefan-Boltzmann Law, this creates a "physics tax" where high-power AI chips require massive radiator surface areas. For example, a single 40-kilowatt server rack would require a radiator the size of a pickleball court. Furthermore, exposure to UV light and atomic oxygen degrades these radiators, requiring a 40% increase in launch mass to ensure end-of-life functionality.

Beyond cooling, **ionizing radiation** poses a threat to the "soft" commercial chips (like Nvidia H100s) necessary for AI. To survive, satellites must use heavy shielding or expensive redundancy, driving the total cost of ownership at least ten times higher than Earth-based data centers. Additionally, while solar energy is abundant, every watt of power generated requires a corresponding watt of heat rejection, doubling the structural burden.

Despite these challenges, space-based computing has "killer apps" in niche markets. Processing data directly on Earth-observation satellites can bypass downlink bottlenecks, and onboard AI is becoming essential for real-time collision avoidance in increasingly crowded orbits. To make larger-scale deployment feasible, the industry is exploring innovative designs like origami-inspired folding radiators and liquid-droplet cooling. Ultimately, while the "physics tax" remains high, the need for immediate, localized insight in orbit ensures that space computing remains a critical, albeit difficult, frontier.

---

## 7. CSS: Unavoidable Bad Parts

**原文标题**: CSS: Unavoidable Bad Parts

**原文链接**: [https://matklad.github.io/2026/06/04/css-unavoidable-bad-parts.html](https://matklad.github.io/2026/06/04/css-unavoidable-bad-parts.html)

生成摘要时出错

---

## 8. US House rejects FISA Section 702 extension, warrantless surveillance expires

**原文标题**: US House rejects FISA Section 702 extension, warrantless surveillance expires

**原文链接**: [https://www.axios.com/2026/06/11/fisa-section-702-expiration-pulte-trump-johnson](https://www.axios.com/2026/06/11/fisa-section-702-expiration-pulte-trump-johnson)

生成摘要时出错

---

## 9. Google is finally killing uBlock Origin in Chrome for good

**原文标题**: Google is finally killing uBlock Origin in Chrome for good

**原文链接**: [https://protonprivacy.substack.com/p/google-is-finally-killing-ublock](https://protonprivacy.substack.com/p/google-is-finally-killing-ublock)

生成摘要时出错

---

## 10. Oh good, screwworms are back (2025)

**原文标题**: Oh good, screwworms are back (2025)

**原文链接**: [https://www.marginallycompelling.com/p/oh-good-screwworms-are-back](https://www.marginallycompelling.com/p/oh-good-screwworms-are-back)

生成摘要时出错

---

## 11. OpenAI to acquire Ona to expand Codex

**原文标题**: OpenAI to acquire Ona to expand Codex

**原文链接**: [https://openai.com/index/openai-to-acquire-ona/](https://openai.com/index/openai-to-acquire-ona/)

生成摘要时出错

---

## 12. The Trouble with Font Previews

**原文标题**: The Trouble with Font Previews

**原文链接**: [https://unsung.aresluna.org/the-trouble-with-font-previews/](https://unsung.aresluna.org/the-trouble-with-font-previews/)

生成摘要时出错

---

## 13. Linux latency measurements and compositor tuning

**原文标题**: Linux latency measurements and compositor tuning

**原文链接**: [https://farnoy.dev/posts/linux-latency](https://farnoy.dev/posts/linux-latency)

生成摘要时出错

---

## 14. Galaxy-killing wind discovered in the early universe

**原文标题**: Galaxy-killing wind discovered in the early universe

**原文链接**: [https://ras.ac.uk/news-and-press/research-highlights/galaxy-killing-wind-discovered-early-universe](https://ras.ac.uk/news-and-press/research-highlights/galaxy-killing-wind-discovered-early-universe)

生成摘要时出错

---

## 15. Omniglot: The Online Encyclopedia of Writing Systems and Languages

**原文标题**: Omniglot: The Online Encyclopedia of Writing Systems and Languages

**原文链接**: [https://www.omniglot.com/](https://www.omniglot.com/)

生成摘要时出错

---

## 16. Why AI hasn't replaced software engineers, and won't

**原文标题**: Why AI hasn't replaced software engineers, and won't

**原文链接**: [https://www.normaltech.ai/p/why-ai-hasnt-replaced-software-engineers](https://www.normaltech.ai/p/why-ai-hasnt-replaced-software-engineers)

生成摘要时出错

---

## 17. Show HN: Open-source API Key server written in Go by Ory

**原文标题**: Show HN: Open-source API Key server written in Go by Ory

**原文链接**: [https://github.com/ory/talos/tree/master](https://github.com/ory/talos/tree/master)

生成摘要时出错

---

## 18. Starfish by Peter Watts (1999)

**原文标题**: Starfish by Peter Watts (1999)

**原文链接**: [https://www.rifters.com/real/STARFISH.htm#prelude](https://www.rifters.com/real/STARFISH.htm#prelude)

生成摘要时出错

---

## 19. Reverse engineering the Creative Katana soundbar to control it from Linux

**原文标题**: Reverse engineering the Creative Katana soundbar to control it from Linux

**原文链接**: [https://blog.nns.ee/2026/02/20/katana-v2x-re/](https://blog.nns.ee/2026/02/20/katana-v2x-re/)

生成摘要时出错

---

## 20. AI agent runs amok in Fedora and elsewhere

**原文标题**: AI agent runs amok in Fedora and elsewhere

**原文链接**: [https://lwn.net/SubscriberLink/1077035/c7e7c14fbd60fae9/](https://lwn.net/SubscriberLink/1077035/c7e7c14fbd60fae9/)

生成摘要时出错

---

## 21. Car headlights don't have to be this blinding

**原文标题**: Car headlights don't have to be this blinding

**原文链接**: [https://www.theatlantic.com/technology/2026/06/car-headlights-too-bright-adaptive-beams/687488/](https://www.theatlantic.com/technology/2026/06/car-headlights-too-bright-adaptive-beams/687488/)

生成摘要时出错

---

## 22. Workers are spending over 6 hours a week botsitting AI, fueling job frustration

**原文标题**: Workers are spending over 6 hours a week botsitting AI, fueling job frustration

**原文链接**: [https://www.businessinsider.com/botsitting-ai-hidden-human-labor-at-work-2026-6](https://www.businessinsider.com/botsitting-ai-hidden-human-labor-at-work-2026-6)

生成摘要时出错

---

## 23. How I made a 60fps eInk Monitor, the Modos Flow

**原文标题**: How I made a 60fps eInk Monitor, the Modos Flow

**原文链接**: [https://www.youtube.com/watch?v=nHbA2-_qzH4](https://www.youtube.com/watch?v=nHbA2-_qzH4)

生成摘要时出错

---

## 24. πFS

**原文标题**: πFS

**原文链接**: [https://github.com/philipl/pifs](https://github.com/philipl/pifs)

生成摘要时出错

---

## 25. Cybersecurity researchers aren't happy about the guardrails on Anthropic's Fable

**原文标题**: Cybersecurity researchers aren't happy about the guardrails on Anthropic's Fable

**原文链接**: [https://techcrunch.com/2026/06/10/cybersecurity-researchers-arent-happy-about-the-guardrails-on-anthropics-fable/](https://techcrunch.com/2026/06/10/cybersecurity-researchers-arent-happy-about-the-guardrails-on-anthropics-fable/)

生成摘要时出错

---

## 26. Anthropic requires 30 day data retention for Fable and Mythos

**原文标题**: Anthropic requires 30 day data retention for Fable and Mythos

**原文链接**: [https://support.claude.com/en/articles/15425996-data-retention-practices-for-mythos-class-models](https://support.claude.com/en/articles/15425996-data-retention-practices-for-mythos-class-models)

生成摘要时出错

---

## 27. Poland to jail online streamers of violent crimes and cruelty for up to 5 years

**原文标题**: Poland to jail online streamers of violent crimes and cruelty for up to 5 years

**原文链接**: [https://www.reuters.com/business/media-telecom/poland-jail-online-streamers-violent-crime-rape-cruelty-up-5-years-2026-06-11/](https://www.reuters.com/business/media-telecom/poland-jail-online-streamers-violent-crime-rape-cruelty-up-5-years-2026-06-11/)

生成摘要时出错

---

## 28. Supporting Exchange and beyond

**原文标题**: Supporting Exchange and beyond

**原文链接**: [https://brendan.abolivier.bzh/exchange-pt-2/](https://brendan.abolivier.bzh/exchange-pt-2/)

生成摘要时出错

---

## 29. Vacuum-Form Signage

**原文标题**: Vacuum-Form Signage

**原文链接**: [https://bethmathews.substack.com/p/the-history-behind-the-signs-lighting](https://bethmathews.substack.com/p/the-history-behind-the-signs-lighting)

生成摘要时出错

---

## 30. Sweet Jeebus, macOS 27 Golden Gate Removes the Dumb Icons from Menu Items

**原文标题**: Sweet Jeebus, macOS 27 Golden Gate Removes the Dumb Icons from Menu Items

**原文链接**: [https://daringfireball.net/2026/06/macos_27_golden_gate_removes_the_dumb_icons_from_menu_items](https://daringfireball.net/2026/06/macos_27_golden_gate_removes_the_dumb_icons_from_menu_items)

生成摘要时出错

---

## 31. Every employee's password was stored in a single Excel file

**原文标题**: Every employee's password was stored in a single Excel file

**原文链接**: [https://www.theregister.com/security/2026/06/11/every-employees-password-was-stored-in-a-single-excel-file/5253784](https://www.theregister.com/security/2026/06/11/every-employees-password-was-stored-in-a-single-excel-file/5253784)

生成摘要时出错

---

## 32. Show HN: Extend UI – open-source UI kit for modern document apps

**原文标题**: Show HN: Extend UI – open-source UI kit for modern document apps

**原文链接**: [https://www.extend.ai/ui](https://www.extend.ai/ui)

生成摘要时出错

---

## 33. The Road to the WASM Component Model 1.0

**原文标题**: The Road to the WASM Component Model 1.0

**原文链接**: [https://bytecodealliance.org/articles/the-road-to-component-model-1-0](https://bytecodealliance.org/articles/the-road-to-component-model-1-0)

生成摘要时出错

---

## 34. Euro-Office: First version of the open-source web office is here

**原文标题**: Euro-Office: First version of the open-source web office is here

**原文链接**: [https://www.heise.de/en/news/Euro-Office-First-version-of-the-open-source-web-office-is-here-11322160.html](https://www.heise.de/en/news/Euro-Office-First-version-of-the-open-source-web-office-is-here-11322160.html)

生成摘要时出错

---

## 35. HTML is a native image format, hear me out

**原文标题**: HTML is a native image format, hear me out

**原文链接**: [https://hmml.eddocu.com](https://hmml.eddocu.com)

生成摘要时出错

---

## 36. Who's the smartest corvid?

**原文标题**: Who's the smartest corvid?

**原文链接**: [https://thetyee.ca/Culture/2026/06/05/Whos-the-Smartest-Corvid/](https://thetyee.ca/Culture/2026/06/05/Whos-the-Smartest-Corvid/)

生成摘要时出错

---

## 37. Anthropic walks back policy that could have 'sabotaged' researchers using Claude

**原文标题**: Anthropic walks back policy that could have 'sabotaged' researchers using Claude

**原文链接**: [https://www.wired.com/story/anthropic-responds-to-backlash-on-claudes-secret-sabotage-on-ai-research/](https://www.wired.com/story/anthropic-responds-to-backlash-on-claudes-secret-sabotage-on-ai-research/)

生成摘要时出错

---

## 38. Making a Shading Language for My Offline Renderer

**原文标题**: Making a Shading Language for My Offline Renderer

**原文链接**: [https://agraphicsguynotes.com/posts/making_a_shading_langauge_for_my_offline_renderer/](https://agraphicsguynotes.com/posts/making_a_shading_langauge_for_my_offline_renderer/)

生成摘要时出错

---

## 39. The Economics of Speculative Decoding

**原文标题**: The Economics of Speculative Decoding

**原文链接**: [https://fergusfinn.com/blog/economics-of-speculative-decoding/](https://fergusfinn.com/blog/economics-of-speculative-decoding/)

生成摘要时出错

---

## 40. Vinyl succumbs to Loudness War: more than just collateral damage (2025)

**原文标题**: Vinyl succumbs to Loudness War: more than just collateral damage (2025)

**原文链接**: [https://magicvinyldigital.net/2025/04/27/vinyl-succumbs-to-loudness-war-more-than-just-collateral-damage/](https://magicvinyldigital.net/2025/04/27/vinyl-succumbs-to-loudness-war-more-than-just-collateral-damage/)

生成摘要时出错

---

## 41. CISA tells govt agencies to patch critical exploited flaws in 3 days

**原文标题**: CISA tells govt agencies to patch critical exploited flaws in 3 days

**原文链接**: [https://www.bleepingcomputer.com/news/security/cisa-tells-govt-agencies-to-patch-critical-exploited-flaws-in-3-days/](https://www.bleepingcomputer.com/news/security/cisa-tells-govt-agencies-to-patch-critical-exploited-flaws-in-3-days/)

生成摘要时出错

---

## 42. Apache Burr: Build reliable AI agents and applications

**原文标题**: Apache Burr: Build reliable AI agents and applications

**原文链接**: [https://burr.apache.org/](https://burr.apache.org/)

生成摘要时出错

---

## 43. World Capitals Voronoi

**原文标题**: World Capitals Voronoi

**原文链接**: [https://www.jasondavies.com/maps/voronoi/capitals/](https://www.jasondavies.com/maps/voronoi/capitals/)

生成摘要时出错

---

## 44. Claude Fable 5

**原文标题**: Claude Fable 5

**原文链接**: [https://www.anthropic.com/news/claude-fable-5-mythos-5](https://www.anthropic.com/news/claude-fable-5-mythos-5)

生成摘要时出错

---

## 45. There is a bunch of malware being spotted in the AUR

**原文标题**: There is a bunch of malware being spotted in the AUR

**原文链接**: [https://lists.archlinux.org/archives/list/aur-general@lists.archlinux.org/](https://lists.archlinux.org/archives/list/aur-general@lists.archlinux.org/)

生成摘要时出错

---

## 46. Reading for pleasure is sharply down among schoolkids, report shows

**原文标题**: Reading for pleasure is sharply down among schoolkids, report shows

**原文链接**: [https://www.nbcnews.com/data-graphics/kids-reading-less-lower-levels-department-education-study-rcna348987](https://www.nbcnews.com/data-graphics/kids-reading-less-lower-levels-department-education-study-rcna348987)

生成摘要时出错

---

## 47. Fable 5 Ported the Ladybird Browser to WebAssembly in One Shot and It Cost $552

**原文标题**: Fable 5 Ported the Ladybird Browser to WebAssembly in One Shot and It Cost $552

**原文链接**: [https://twitter.com/HeyPuter/status/2065114471589089729](https://twitter.com/HeyPuter/status/2065114471589089729)

生成摘要时出错

---

## 48. Show HN: I applied Lyapunov stability theory to detect when LLM agents spiral

**原文标题**: Show HN: I applied Lyapunov stability theory to detect when LLM agents spiral

**原文链接**: [https://github.com/vishal-dehurdle/state-harness](https://github.com/vishal-dehurdle/state-harness)

生成摘要时出错

---

## 49. Macaroni – a single HTML file messenger

**原文标题**: Macaroni – a single HTML file messenger

**原文链接**: [https://github.com/vanyapr/makaroshki](https://github.com/vanyapr/makaroshki)

生成摘要时出错

---

## 50. What is it like to be a bat? (1974) [pdf]

**原文标题**: What is it like to be a bat? (1974) [pdf]

**原文链接**: [https://www.sas.upenn.edu/~cavitch/pdf-library/Nagel_Bat.pdf](https://www.sas.upenn.edu/~cavitch/pdf-library/Nagel_Bat.pdf)

生成摘要时出错

---

## 51. Show HN: HelixDB – A graph database built on object storage

**原文标题**: Show HN: HelixDB – A graph database built on object storage

**原文链接**: [https://github.com/HelixDB/helix-db/tree/main](https://github.com/HelixDB/helix-db/tree/main)

生成摘要时出错

---

## 52. 2.4M+ VRChat users' data accessed following cloud breach

**原文标题**: 2.4M+ VRChat users' data accessed following cloud breach

**原文链接**: [https://www.theregister.com/security/2026/06/11/24m-vrchat-users-data-accessed-following-cloud-breach/5254246](https://www.theregister.com/security/2026/06/11/24m-vrchat-users-data-accessed-following-cloud-breach/5254246)

生成摘要时出错

---

## 53. Raspberry Pi 5 – 16GB RAM

**原文标题**: Raspberry Pi 5 – 16GB RAM

**原文链接**: [https://www.adafruit.com/product/6125?src=raspberrypi](https://www.adafruit.com/product/6125?src=raspberrypi)

生成摘要时出错

---

## 54. macOS Container Machines

**原文标题**: macOS Container Machines

**原文链接**: [https://github.com/apple/container/blob/main/docs/container-machine.md](https://github.com/apple/container/blob/main/docs/container-machine.md)

生成摘要时出错

---

## 55. Dutch government retracts plan to host VAT administration in US cloud

**原文标题**: Dutch government retracts plan to host VAT administration in US cloud

**原文链接**: [https://www.nrc.nl/nieuws/2026/06/11/staatssecretaris-draait-de-uitbesteding-van-de-btw-inning-aan-een-amerikaans-bedrijf-ten-dele-terug-want-te-riskant-a4929807](https://www.nrc.nl/nieuws/2026/06/11/staatssecretaris-draait-de-uitbesteding-van-de-btw-inning-aan-een-amerikaans-bedrijf-ten-dele-terug-want-te-riskant-a4929807)

生成摘要时出错

---

## 56. Klondike Solitaire game for curses in 5k of C

**原文标题**: Klondike Solitaire game for curses in 5k of C

**原文链接**: [https://nanochess.org/klondike_in_c.html](https://nanochess.org/klondike_in_c.html)

生成摘要时出错

---

## 57. OpenCV 5 Is Here: The Biggest Leap in Years for Computer Vision

**原文标题**: OpenCV 5 Is Here: The Biggest Leap in Years for Computer Vision

**原文链接**: [https://opencv.org/opencv-5/](https://opencv.org/opencv-5/)

生成摘要时出错

---

## 58. Emerge Career (YC S22) Is Hiring a Founding Growth Marketer

**原文标题**: Emerge Career (YC S22) Is Hiring a Founding Growth Marketer

**原文链接**: [https://www.ycombinator.com/companies/emerge-career/jobs/v0S1AEG-founding-growth-marketer](https://www.ycombinator.com/companies/emerge-career/jobs/v0S1AEG-founding-growth-marketer)

生成摘要时出错

---

## 59. Running Claude Code Offline on an M3 Pro with Qwen3.6

**原文标题**: Running Claude Code Offline on an M3 Pro with Qwen3.6

**原文链接**: [https://har-ki.github.io/claude-code-sre-handbook/handbook/06-air-gapped/](https://har-ki.github.io/claude-code-sre-handbook/handbook/06-air-gapped/)

生成摘要时出错

---

## 60. The Life and Works of Raoul Bott (2002)

**原文标题**: The Life and Works of Raoul Bott (2002)

**原文链接**: [https://arxiv.org/abs/math/0201027](https://arxiv.org/abs/math/0201027)

生成摘要时出错

---

## 61. Antikythera Mechanism

**原文标题**: Antikythera Mechanism

**原文链接**: [https://en.wikipedia.org/wiki/Antikythera_mechanism](https://en.wikipedia.org/wiki/Antikythera_mechanism)

生成摘要时出错

---

## 62. PgDog is funded and coming to a database near you

**原文标题**: PgDog is funded and coming to a database near you

**原文链接**: [https://pgdog.dev/blog/our-funding-announcement](https://pgdog.dev/blog/our-funding-announcement)

生成摘要时出错

---

## 63. Claude Desktop spawns 1.8 GB Hyper-V VM on every launch, even for chat-only use

**原文标题**: Claude Desktop spawns 1.8 GB Hyper-V VM on every launch, even for chat-only use

**原文链接**: [https://github.com/anthropics/claude-code/issues/29045](https://github.com/anthropics/claude-code/issues/29045)

生成摘要时出错

---

## 64. US-Canada border library gets new Quebec-only entrance

**原文标题**: US-Canada border library gets new Quebec-only entrance

**原文链接**: [https://www.bbc.com/news/videos/clyrvrde160o](https://www.bbc.com/news/videos/clyrvrde160o)

生成摘要时出错

---

## 65. Surprise, pay $1000

**原文标题**: Surprise, pay $1000

**原文链接**: [https://forestwalk.ai/blog/surprise-blacksmith-costs/](https://forestwalk.ai/blog/surprise-blacksmith-costs/)

生成摘要时出错

---

## 66. Sequoyah’s syllabary created a written language for the Cherokee

**原文标题**: Sequoyah’s syllabary created a written language for the Cherokee

**原文链接**: [https://www.smithsonianmag.com/innovation/man-created-written-language-cherokee-did-efficiently-elegantly-peers-thought-magic-180988850/](https://www.smithsonianmag.com/innovation/man-created-written-language-cherokee-did-efficiently-elegantly-peers-thought-magic-180988850/)

生成摘要时出错

---

## 67. Smudging the game disc to make speedrunning 'SpongeBob' faster

**原文标题**: Smudging the game disc to make speedrunning 'SpongeBob' faster

**原文链接**: [https://www.inverse.com/input/gaming/the-dirty-secret-that-makes-speedrunning-on-spongebob-a-lot-faster](https://www.inverse.com/input/gaming/the-dirty-secret-that-makes-speedrunning-on-spongebob-a-lot-faster)

生成摘要时出错

---

## 68. A €0.01 bank transfer could compromise a banking AI agent

**原文标题**: A €0.01 bank transfer could compromise a banking AI agent

**原文链接**: [https://blue41.com/blog/how-we-helped-bunq-secure-their-financial-ai-assistant/](https://blue41.com/blog/how-we-helped-bunq-secure-their-financial-ai-assistant/)

生成摘要时出错

---

## 69. Buy a train, bridge or tracks from the Swiss Railway

**原文标题**: Buy a train, bridge or tracks from the Swiss Railway

**原文链接**: [https://sbbresale.ch/](https://sbbresale.ch/)

生成摘要时出错

---

## 70. Authentication issues related to API requests

**原文标题**: Authentication issues related to API requests

**原文链接**: [https://www.githubstatus.com/incidents/fcj3088jg1wx](https://www.githubstatus.com/incidents/fcj3088jg1wx)

生成摘要时出错

---

## 71. How JPL keeps the 13-year-old Curiosity rover doing science

**原文标题**: How JPL keeps the 13-year-old Curiosity rover doing science

**原文链接**: [https://spectrum.ieee.org/curiosity-rover-jpl-mars-science](https://spectrum.ieee.org/curiosity-rover-jpl-mars-science)

生成摘要时出错

---

## 72. Trust Factory

**原文标题**: Trust Factory

**原文链接**: [https://newsletter.kentbeck.com/p/trust-factory](https://newsletter.kentbeck.com/p/trust-factory)

生成摘要时出错

---

## 73. L'Affaire Siloxane

**原文标题**: L'Affaire Siloxane

**原文链接**: [https://mceglowski.substack.com/p/laffaire-siloxane](https://mceglowski.substack.com/p/laffaire-siloxane)

生成摘要时出错

---

## 74. Dealership revoked offer to buy back customer's BMW, blaming wayward AI chatbot

**原文标题**: Dealership revoked offer to buy back customer's BMW, blaming wayward AI chatbot

**原文链接**: [https://www.cbc.ca/news/business/ai-chatbot-bmw-dealership-9.7230226](https://www.cbc.ca/news/business/ai-chatbot-bmw-dealership-9.7230226)

生成摘要时出错

---

## 75. Cheap Iranian drone downed $25M US Army helicopter–maybe by chance

**原文标题**: Cheap Iranian drone downed $25M US Army helicopter–maybe by chance

**原文链接**: [https://arstechnica.com/gadgets/2026/06/cheap-iranian-drone-downed-25-million-us-army-helicopter-maybe-by-chance/](https://arstechnica.com/gadgets/2026/06/cheap-iranian-drone-downed-25-million-us-army-helicopter-maybe-by-chance/)

生成摘要时出错

---

## 76. Mercedes‑Benz starts large‑scale production of electric axial flux motor

**原文标题**: Mercedes‑Benz starts large‑scale production of electric axial flux motor

**原文链接**: [https://media.mercedes-benz.com/en/article/bebac2af-acdc-465a-9538-adb0bf3d8ccf](https://media.mercedes-benz.com/en/article/bebac2af-acdc-465a-9538-adb0bf3d8ccf)

生成摘要时出错

---

## 77. Reviving Papers with Code

**原文标题**: Reviving Papers with Code

**原文链接**: [https://paperswithcode.co/](https://paperswithcode.co/)

生成摘要时出错

---

## 78. GeoLibre 1.0

**原文标题**: GeoLibre 1.0

**原文链接**: [https://geolibre.app/](https://geolibre.app/)

生成摘要时出错

---

## 79. AI Economics for Dummies

**原文标题**: AI Economics for Dummies

**原文链接**: [https://www.mcsweeneys.net/articles/ai-economics-for-dummies](https://www.mcsweeneys.net/articles/ai-economics-for-dummies)

生成摘要时出错

---

## 80. Nobody needs AI to search the Internet, court says in ruling against Google

**原文标题**: Nobody needs AI to search the Internet, court says in ruling against Google

**原文链接**: [https://arstechnica.com/tech-policy/2026/06/nobody-needs-ai-to-search-the-internet-court-says-in-ruling-against-google/](https://arstechnica.com/tech-policy/2026/06/nobody-needs-ai-to-search-the-internet-court-says-in-ruling-against-google/)

生成摘要时出错

---

## 81. Are insecure code completions in PyCharm a vulnerability?

**原文标题**: Are insecure code completions in PyCharm a vulnerability?

**原文链接**: [https://sethmlarson.dev/are-insecure-code-completions-a-vulnerability](https://sethmlarson.dev/are-insecure-code-completions-a-vulnerability)

生成摘要时出错

---

