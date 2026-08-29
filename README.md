# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-08-29.md)

*最后自动更新时间: 2026-08-29 01:16:55*
## 1. 苏美尔王表是否与古气候事件吻合？

**原文标题**: Does the Sumerian King List Align with Paleoclimate Events?

**原文链接**: [https://www.vectorian.be/articles/2026-06-07/sumerian-king-list-paleoclimate-alignment-explorer/](https://www.vectorian.be/articles/2026-06-07/sumerian-king-list-paleoclimate-alignment-explorer/)

本文评估了一项推测性假设，即《苏美尔王表》（SKL）中大洪水前八位国王异常漫长的统治期，代表了对史前气候变迁或地质事件的扭曲记忆。

为了验证这一点，作者将总计241,200年的统治时长按比例缩放至地质时间尺度，并将该序列的终点锚定在距今1.16万年前（新仙女木期结束）。利用高斯核评分系统测量接近程度，研究者将得出的统治分界线与包含104个第四纪事件（包括海因里希事件、火山喷发和太阳质子事件）的目录进行了对比。

研究者采用了严格的统计控制，包括：
*   **置换检验：** 将实际统治顺序与相同数值的所有可能重组序列进行对比。
*   **多重比较调整：** 使用Benjamini-Hochberg q值，以抵消对多个目录和带宽进行测试的影响。
*   **比较年代学：** 测试其他古代序列（如《圣经》中的寿命、曼涅托记载的神之统治期以及基什第一王朝统治者），以观察无关数据产生偶然吻合的难易程度。

**结果：**
分析未发现统计学意义上的显著证据证明《苏美尔王表》与古气候记录相一致。主要分析得出的p值为0.350，调整后的q值为0.622。即使是最有利的探索性结果（p = 0.021），在经过多重比较调整后也未能达到显著水平（q = 0.222）。

作者得出结论认为，虽然由于锚点和目录选择具有灵活性，导致“寻找匹配项并非难事”，但《苏美尔王表》的特定顺序并不比随机概率或无关的古代文献表现得更好。该研究仍具有探索性，并指出了相关局限，如事件目录的人为编撰性质以及未计入定年不确定性等。

---

## 2. GUI 应当完全由键盘驱动。

**原文标题**: GUIs should be fully keyboard-driven

**原文链接**: [https://ckardaris.com/blog/2026/08/28/keyboard-driven-guis.html](https://ckardaris.com/blog/2026/08/28/keyboard-driven-guis.html)

在本文中，作者探讨了终端用户界面（TUI）与图形用户界面（GUI）之间持续存在的争论，并特别挑战了“TUI 因支持键盘驱动而更优越”这一普遍观点。

尽管作者承认“留在终端”确实很方便，但他们认为，键盘友好性并非 TUI 的固有优势，而恰恰反映了当前许多 GUI 实现的不足。从理论上讲，GUI 是 TUI 的超集，这意味着 GUI 可以——也应该——提供 TUI 所能提供的一切功能，包括完整的键盘导航。

作者强调，主要的 GUI 框架指南（如 GNOME 人机界面指南）已经提倡为每项操作提供完整的键盘访问支持。为了证明其可行性，作者提到在自研的 GUI 应用程序 Klisi 中实现了全面的键盘快捷键。

核心观点是，在 GUI 中提供完全由键盘驱动的体验取决于开发者的“意愿”，而非技术上的可行性。开发者不应在用户体验上妥协；相反，他们应通过确保应用程序可以完全通过键盘导航，努力使 GUI 应用程序尽可能直观、高效。这种方法结合了 GUI 的视觉优势与终端的高速和高产。

---

## 3. Boot a Virtual iPhone via Apple's Virtualization.framework

**原文标题**: Boot a Virtual iPhone via Apple's Virtualization.framework

**原文链接**: [https://github.com/Lakr233/vphone-cli](https://github.com/Lakr233/vphone-cli)

生成摘要时出错

---

## 4. Htmx 4.0

**原文标题**: Htmx 4.0

**原文链接**: [https://four.htmx.org/announcements/2026-08-28-htmx-4.0.0-is-released](https://four.htmx.org/announcements/2026-08-28-htmx-4.0.0-is-released)

htmx 团队发布了 **htmx 4.0.0**，这是一次重大更新，将该库的内部实现从 `XMLHttpRequest` 迁移到了 `fetch()` API。虽然该库在很大程度上仍与 2.x 版本兼容，但存在三个主要的破坏性变更：

1. **显式属性继承：** 属性不再默认继承。用户现在必须显式地在属性后追加 `:inherited`（例如 `hx-confirm:inherited`），才能使其应用于子元素。
2. **标准化事件：** 事件名称已得到清理，并重组为一致的 `htmx:phase:action` 格式。
3. **历史记录管理：** 为了避免第三方 JavaScript 修改导致的问题，历史记录支持不再将页面缓存到 `localStorage` 中。相反，它会在返回导航时重新获取内容。

新功能包括对 **morph swaps** 和 **`<hx-partial>` 标签** 的原生支持，后者为复杂的带外（out-of-band）更新提供了更清晰的语法。此版本还引入了多个新扩展，包括 `hx-preload`、`hx-alpine-compat` 和 **hx-live**（一种旨在与 htmx 紧密集成的新型前端脚本解决方案）。

为了方便迁移，团队提供了一个 **CLI 升级检查工具**以及专门的“技能”文件，以帮助 **LLM**（大语言模型）辅助过渡。

值得注意的是，虽然 4.0.0 现已发布，但为了防止使用未指定版本的 CDN URL 的网站出现故障，2.x 版本在 NPM 上将保留 “latest” 标签直至 2027 年初。团队强调 2.x 版本将继续得到无限期支持，因此用户没有立即升级的压力。

---

## 5. 美国对 A/I Collective 的制裁

**原文标题**: U.S. sanctions against the A/I Collective

**原文链接**: [https://www.inventati.org/](https://www.inventati.org/)

A/I (Autistici/Inventati) is an autonomous anticapitalist collective established in 2001 to champion digital rights and free communication. Born from the radical activist movement, the group provides a platform for digital self-defense, offering tools to individuals and collectives seeking to communicate outside the influence of state control or commercial data exploitation.

The collective operates as a volunteer-run entity rooted in principles of solidarity and self-organization. All services are provided free of charge, with a strict policy against the commoditization or monitoring of personal user data. To maintain its independence and radical stance, A/I relies exclusively on voluntary donations and avoids all forms of commercial compensation.

Access to A/I's services is restricted to non-commercial use and is granted based on shared political affinity. Unlike automated platforms, each account request is processed manually by a volunteer through a dialogical process to ensure the applicant aligns with the group’s manifesto and privacy policies. To protect user security, all request records are anonymized and eventually destroyed. 

While the provided content serves as the collective's mission statement and service guide, the title indicates that the organization is currently navigating or responding to U.S. sanctions. To join the platform, the collective requires all potential users to strictly adhere to their policy and manifesto.

---

## 6. 现如今，仅仅是漏洞的传闻就足以让人挖掘出利用手段。

**原文标题**: Just the rumour of a bug is enough to find an exploit these days

**原文链接**: [https://anil.recoil.org/notes/rumour-is-the-exploit](https://anil.recoil.org/notes/rumour-is-the-exploit)

本文探讨了网络安全领域的一个关键转变：人工智能驱动的“代理型攻击系统”仅凭传闻或简要描述即可将漏洞武器化。作者以最近 OCaml `cohttp` 库中的一个路径遍历漏洞作为案例研究，指出在公开拉取请求（PR）发布仅十分钟后，自动化探测便开始攻击其服务器。

文章的核心论点是，开源软件（OSS）的“缺陷经济学”（bugonomics）已达到临界点：大语言模型（LLM）能在数秒内生成攻击载荷，而人类维护者仍受困于手动分类、验证和复杂的下游发布周期。这导致了“负日”（negative-day）漏洞的出现，即攻击行为发生在补丁发布之前。虽然谷歌等大公司采用了自动化微更新，但开源维护者缺乏基础设施，也难以获取受安全护栏限制的“前沿”AI模型来进行同等规模的防御。

为了应对这一挑战，作者提出了三项主要策略：
1. **私有开发基础设施：** 强化“信任网络”系统和私有仓库，使维护者能在不向自动化监控器泄露元数据的情况下协作。
2. **持续发布：** 转向类似于 Chrome 或 Linux 的快速发布模式，尽管这需要克服跨生态系统软件包管理的重重障碍。
3. **主动虚拟补丁：** 实施自动化的协议层防御（如“antibotty”网络），一旦识别出某类漏洞，即可在全网部署缓解措施，为永久性修复争取时间。

最后，作者指出，开源社区必须转向模型辅助、工具验证的工作流，以应对机器生成威胁的激增，并呼吁加强对形式化规范（如 Lean/OxCaml）的研究，以及获取更多如 Glasswing 等防御性 AI 项目的访问权限。

---

## 7. PPWR让本已脆弱的桌游行业再遭重创

**原文标题**: PPWR lands another blow to an precarious tabletop industry

**原文链接**: [https://www.rascal.news/ppwr-lands-another-blow-to-an-already-precarious-tabletop-industry/](https://www.rascal.news/ppwr-lands-another-blow-to-an-already-precarious-tabletop-industry/)

欧盟新颁布的《包装及包装废物法规》（PPWR）正为小型桌面角色扮演游戏（TTRPG）行业带来显著的行政和财务障碍。虽然该框架旨在促进环境可持续性，但它以复杂的要求取代了旧指令，许多独立出版商发现这些要求几乎难以应对。

主要挑战在于“生产者责任延伸”（EPR）政策。由于缺乏统一的欧盟体系，设计师必须遵守所有27个成员国各自特定的注册流程、标签要求和迥异的收费结构。像 Black Armada 和 Genesis of Legend 这样的小型出版商表示，研究并维持每个国家的合规性所需的资源成本极高。因此，为了规避潜在的罚款和“错综复杂”的法律陷阱，已有数位创作者停止或暂停向欧盟发货。

法规本身的模糊性使问题进一步复杂化。创作者们正艰难地界定何为“包装”——例如，一次性热缩膜属于规则涵盖范围，而游戏盒则可能被视为产品的组成部分。这些不确定性，加之《通用产品安全法规》（GPSR）和波动的国际关税等近期障碍，导致一些设计师将 PPWR 视为向国际市场销售实体商品的“致命一击”。

尽管 PPWR 的环保目标普遍得到支持，但业内专业人士认为，“一刀切”的立法方式未能考虑到微型企业。如果不对小微企业实施豁免或简化流程，其结果很可能是欧盟客户面临价格上涨、对高成本第三方分销商的依赖，或者是独立 TTRPG 产品完全退出欧洲市场。

---

## 8. 盗梦空间风格的逐向导航弯曲地图

**原文标题**: Inception-style curved map for turn-by-turn directions

**原文链接**: [https://www.orbify.eu/demo/](https://www.orbify.eu/demo/)

Orbify 是一个导航技术平台，目前正在展示其 “Demo 2 - v72” 版本，并引入了“重塑导航”的概念。该系统的核心功能是专为逐向导航设计的《盗梦空间》风格弯曲地图。

该地图从电影《盗梦空间》的视觉特效中汲取灵感，利用地平线的弯曲或“折叠”视角来显示前方路线。这项专有技术目前正处于专利申请中（编号：PCT/EP2026/058725），标志着一种不同于传统平面或标准 3D 地图界面的独特空间可视化方案。

总之，Orbify 旨在通过用动态的弯曲视觉环境取代传统布局，从而革新 GPS 导航的用户体验。

---

## 9. Identifying fake cosmetics using AI

**原文标题**: Identifying fake cosmetics using AI

**原文链接**: [https://groverlab.org/hnbfpr/2026-08-26-ai-counterfeit-cosmetics.html](https://groverlab.org/hnbfpr/2026-08-26-ai-counterfeit-cosmetics.html)

生成摘要时出错

---

## 10. Curvature Beziers: Improving on a timeless recipe

**原文标题**: Curvature Beziers: Improving on a timeless recipe

**原文链接**: [https://acko.net/blog/curvature-beziers/](https://acko.net/blog/curvature-beziers/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 2 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 3 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 4 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 5 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 6 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 7 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 8 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 9 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 10 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 11 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 12 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 13 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 14 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 15 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 16 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 17 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 18 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 19 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 20 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 21 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 22 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 23 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 24 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 25 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 26 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 27 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 28 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 29 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 30 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 31 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 32 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 33 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 34 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 35 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 36 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 37 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 38 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 39 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 40 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 41 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 42 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 43 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 44 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 45 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 46 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 47 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 48 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 49 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 50 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 51 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 52 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 53 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 54 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 55 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 56 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 57 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 58 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 59 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 60 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 61 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 62 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 63 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 64 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 65 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 66 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 67 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 68 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 69 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 70 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 71 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 72 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 73 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 74 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 75 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 76 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 77 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 78 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 79 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 80 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 81 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 82 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 83 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 84 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 85 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 86 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 87 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 88 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 89 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 90 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 91 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 92 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 93 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 94 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 95 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 96 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 97 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 98 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 99 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 100 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 101 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 102 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 103 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 104 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 105 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 106 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 107 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 108 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 109 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 110 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 111 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 112 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 113 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 114 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 115 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 116 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 117 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 118 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 119 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 120 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 121 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 122 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 123 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 124 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 125 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 126 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 127 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 128 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 129 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 130 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 131 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 132 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 133 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 134 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 135 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 136 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 137 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 138 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 139 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 140 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 141 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 142 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 143 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 144 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 145 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 146 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 147 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 148 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 149 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 150 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 151 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 152 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 153 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 154 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 155 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 156 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 157 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 158 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 159 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 160 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 161 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 162 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 163 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 164 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 165 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 166 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 167 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 168 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 169 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 170 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 171 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 172 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 173 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 174 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 175 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 176 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 177 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 178 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 179 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 180 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 181 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 182 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 183 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 184 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 185 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 186 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 187 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 188 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 189 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 190 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 191 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 192 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 193 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 194 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 195 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 196 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 197 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 198 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 199 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 200 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 201 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 202 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 203 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 204 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 205 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 206 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 207 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 208 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 209 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 210 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 211 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 212 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 213 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 214 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 215 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 216 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 217 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 218 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 219 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 220 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 221 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 222 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 223 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 224 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 225 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 226 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 227 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 228 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 229 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 230 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 231 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 232 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 233 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 234 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 235 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 236 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 237 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 238 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 239 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 240 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 241 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 242 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 243 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 244 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 245 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 246 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 247 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 248 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 249 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 250 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 251 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 252 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 253 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 254 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 255 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 256 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 257 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 258 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 259 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 260 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 261 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 262 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 263 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 264 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 265 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 266 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 267 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 268 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 269 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 270 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 271 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 272 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 273 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 274 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 275 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 276 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 277 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 278 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 279 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 280 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 281 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 282 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 283 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 284 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 285 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 286 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 287 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 288 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 289 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 290 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 291 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 292 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 293 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 294 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 295 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 296 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 297 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 298 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 299 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 300 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 301 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 302 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 303 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 304 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 305 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 306 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 307 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 308 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 309 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 310 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 311 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 312 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 313 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 314 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 315 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 316 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 317 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 318 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 319 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 320 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 321 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 322 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 323 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 324 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 325 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 326 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 327 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 328 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 329 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 330 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 331 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 332 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 333 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 334 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 335 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 336 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 337 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 338 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 339 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 340 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 341 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 342 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 343 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 344 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 345 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 346 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 347 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 348 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 349 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 350 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 351 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 352 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 353 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 354 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 355 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 356 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 357 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 358 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 359 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 360 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 361 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 362 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 363 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 364 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 365 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 366 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 367 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 368 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 369 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 370 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 371 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 372 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 373 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 374 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 375 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 376 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 377 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 378 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 379 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 380 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 381 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 382 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 383 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 384 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 385 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 386 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 387 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 388 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 389 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 390 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 391 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 392 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 393 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 394 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 395 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 396 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 397 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 398 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 399 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 400 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 401 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 402 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 403 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 404 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 405 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 406 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 407 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 408 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 409 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 410 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 411 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 412 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 413 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 414 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 415 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 416 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 417 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 418 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 419 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 420 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 421 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 422 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 423 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 424 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 425 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 426 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 427 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 428 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 429 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 430 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 431 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 432 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 433 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 434 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 435 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 436 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 437 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 438 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 439 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 440 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 441 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 442 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 443 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 444 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 445 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 446 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 447 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 448 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 449 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 450 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 451 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 452 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 453 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 454 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 455 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 456 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 457 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 458 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 459 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 460 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 461 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 462 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 463 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 464 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 465 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 466 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 467 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 468 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 469 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 470 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 471 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 472 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 473 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 474 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 475 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 476 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 477 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 478 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 479 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 480 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 481 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 482 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 483 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 484 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 485 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 486 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 487 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 488 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 489 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 490 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 491 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 492 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 493 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 494 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 495 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 496 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 497 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 498 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 499 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 500 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 501 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 502 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 503 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 504 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 505 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 506 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 507 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 508 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 509 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 510 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 511 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 512 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 513 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 514 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 515 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 516 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 517 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 518 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 519 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 520 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 521 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 522 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 523 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 524 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 525 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
