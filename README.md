# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-06-22.md)

*最后自动更新时间: 2026-06-22 20:29:52*
## 1. window.showDirectoryPicker 开启了全新的世界

**原文标题**: window.showDirectoryPicker opens up a whole new world

**原文链接**: [https://steveharrison.dev/showdirectorypicker-opens-up-a-whole-new-world/](https://steveharrison.dev/showdirectorypicker-opens-up-a-whole-new-world/)

本文探讨了 Chrome 的 `window.showDirectoryPicker()` API 的潜力，该 API 允许用户授予网站对本地目录的读写访问权限。这项技术推动了“本地优先”的软件模式，让用户能够完全掌控自己文件系统中的数据，而无需依赖外部云服务。

为了演示该 API 的功能，作者在不手动编写任何代码的情况下，利用 AI 助手 Claude 生成了两个复杂的原型：
*   **照片管理界面：** 灵感源自苹果的 Aperture，这款基于浏览器的应用允许用户直接在电脑上查看、整理和移动本地图像文件。
*   **基于节点的合成应用：** 灵感源自苹果的 Shake，该工具可实现图像处理和多边形合成。

作者总结道，这一 API 为 Web 开发开启了一个“全新的世界”。通过弥合浏览器界面与本地存储之间的鸿沟，它为强大的专业工具（如基于 WebGPU 的视频编辑器）铺平了道路，使其在具备 Web 界面灵活性的同时，兼具本地文件管理的性能与隐私性。

---

## 2. Show HN：CleverCrow：为你最喜欢的项目赠送代币

**原文标题**: Show HN: CleverCrow: give tokens to your favorite projects

**原文链接**: [https://clevercrow.io](https://clevercrow.io)

**CleverCrow** 是一个旨在优化 AI 驱动的开源贡献流程，同时保护维护者免受“AI 垃圾”（低质量、自动化的合并请求）困扰的平台。它颠覆了传统的贡献模式，允许社区资助特定的议题（Issues），随后由维护者通过受控的 AI 智能体来解决这些问题。

**运作机制：**
1.  **社区资助：** 支持者针对特定的 GitHub 议题承诺小额捐助。一旦资金池达到一定规模，维护者即可选择启动一次“运行”（Run）。
2.  **维护者指导：** AI 智能体在无凭证沙箱中起草开发计划。维护者在代码编写开始前审核并迭代该计划。
3.  **沙箱执行：** 智能体执行获批计划并创建一个草稿合并请求（Draft PR）。关键在于，智能体在隔离环境中运行，无法直接访问 Git 或仓库令牌。
4.  **审核与合并：** 维护者审核代码差异，并可要求进行最多五轮修改。未经人工明确批准，任何内容都不会被合并。
5.  **透明计费：** 资金用于支付 AI 算力成本及 10% 的平台费。一旦议题被合并或关闭，所有剩余资金将自动退回支持者的钱包。

**核心优势：**
*   **对于维护者：** 消除使用 AI 智能体的财务成本和“提示词调试”的麻烦，同时确保维护者保留绝对的把关权。它还充当了过滤器，帮助优先处理社区真正重视的问题。
*   **对于支持者：** 提供了一种可靠的方式来表达对功能重要性的诉求。即使某个仓库尚未加入 CleverCrow，支持者也可以通过承诺资金来“推动”维护者加入。
*   **安全性：** 通过采用“受控隔离”的沙箱架构，平台确保 AI 智能体永远不具备破坏代码库的凭证。

本质上，CleverCrow 将开源维护转变为一种受资助的、AI 辅助的工作流，由社区支付算力费用，而维护者把控最终方向。

---

## 3. A New Book on Plagiarism

**原文标题**: A New Book on Plagiarism

**原文链接**: [https://www.commentary.org/articles/joseph-epstein/plagiarism-writing-politics-arts/](https://www.commentary.org/articles/joseph-epstein/plagiarism-writing-politics-arts/)

生成摘要时出错

---

## 4. DHL将采用新型风力驱动货船运输货物

**原文标题**: DHL Set to Transport Goods on New Wind-Powered Cargo Ships

**原文链接**: [https://www.wsj.com/pro/sustainable-business/dhl-set-to-transport-goods-on-new-wind-powered-cargo-ships-eca5d5a0](https://www.wsj.com/pro/sustainable-business/dhl-set-to-transport-goods-on-new-wind-powered-cargo-ships-eca5d5a0)

**概要：DHL 将启用新型风力辅助动力货轮运输货物**

DHL 全球货运（DHL Global Forwarding）已达成一项战略合作伙伴关系，将启用四艘新型风力辅助动力货轮，这标志着该公司在海运脱碳化进程中迈出了重要一步。该项目是与摩根大通（J.P. Morgan Premier Ship Lease）以及海运能源公司 Purus 合作开展的。

**核心亮点：**
*   **技术应用：** 这些船只将配备机械帆（具体为吸力帆），通过利用风能来补充传统发动机动力。根据航线和天气条件，这种风力推进技术预计可减少高达 30% 的燃油消耗和温室气体排放。
*   **可持续发展目标：** 此举是 DHL 集团“2050 年使命”的一部分，该使命旨在到 2050 年实现物流相关净零排放。通过将这些船舶纳入其运输网络，DHL 为客户提供了更具可持续性的航运选择，助力其减少“范围 3”排放。
*   **行业背景：** 航运业正面临国际海事组织 (IMO) 日益增长的压力，要求在 2050 年左右实现净零排放。随着行业寻求摆脱对重油的依赖，DHL 的投资反映了物流领军企业转向替代动力方式的趋势。
*   **时间线：** 新型风力辅助船舶预计将于 2024 年至 2026 年间交付并投入运营。

这一合作伙伴关系凸显了全球物流领域的转型：传统航运方式正通过可持续技术进行重塑，以满足日益严苛的环保法规和企业可持续发展要求。

---

## 5. 警察局长利用 Flock 系统跟踪女性，凸显了搜查令的必要性。

**原文标题**: Flock-Powered Police Chiefs Stalking Women Shows Why Warrants Are Needed

**原文链接**: [https://ipvm.com/reports/police-chiefs-track](https://ipvm.com/reports/police-chiefs-track)

IPVM的这篇文章指出，高级执法人员反复滥用Flock Safety的车牌识别（LPR）技术，这表明迫切需要建立司法搜查令制度。

核心证据是一系列有记录的“职务违法”行为，涉及警察局长利用该系统跟踪恋人及竞争对手。伊利诺伊州假日山（Holiday Hills）警察局长在2026年6月的一起案件凸显了这一趋势：他因追踪前伴侣并查询竞争对手的车牌近180次，被控职务违法重罪。司法研究所已在多个州发现至少18起类似案件，涉及不同级别的警官利用Flock系统监视情妇和前配偶。

文章指出，Flock的公司宣传存在重大矛盾。尽管Flock声称其技术追踪的是“车辆而非人”，但其首席法律官（CLO）承认，追踪前伴侣是该系统最常见的滥用形式。此外，由于车牌在法律上与个人所有权挂钩，追踪车辆实际上已成为追踪个人的变相手段。

作者强调，由于负责政策和培训的警察局长本人往往就是违法者，内部纪律措施已不足以解决问题。因此，文章主张在对存储的LPR数据进行常规、被动搜索时，应要求提供搜查令。文章认为，这一要求将使LPR技术遵循与GPS追踪器（美国诉琼斯案）和手机定位数据（卡朋特诉美国案）相同的法律先例。支持者指出，现有的“紧急情况”例外条款已允许在真正的紧急状态下无需搜查令即可访问数据，这在确保公共安全不受影响的同时，也能防止该工具被用于私人跟踪。

---

## 6. 慕尼黑 1991：当前人工智能热潮的根源

**原文标题**: Munich 1991: The Roots of the Current AI Boom

**原文链接**: [https://people.idsia.ch/~juergen/ai-boom-roots-munich-1991.html](https://people.idsia.ch/~juergen/ai-boom-roots-munich-1991.html)

在《慕尼黑1991：当前AI热潮的根源》一文中，于尔根·施密德胡伯（Jürgen Schmidhuber）指出，推动当今人工智能革命的基础性数学突破，起源于1990年至1991年间他在慕尼黑工业大学（TUM）的实验室。尽管现代“AI热潮”通常被认为始于2012年之后的大数据和高性能GPU时代，但施密德胡伯断言，核心算法早在几十年前就已经确立。

关键里程碑总结如下：

*   **LSTM（长短期记忆网络）：** 1991年，施密德胡伯的学生塞普·霍克赖特（Sepp Hochreiter）在其毕业论文中发现了“梯度消失问题”，并提出了LSTM的基础架构。该架构最终成为语音识别、翻译和文本转语音领域的行业标准，通过谷歌、苹果和亚马逊等公司为数十亿人提供服务。
*   **Transformer与注意力机制：** 施密德胡伯强调了他1991年关于“快速权重编程器”的研究，他称其在功能上等同于现代的线性Transformer。该系统允许一个神经网络通过一种类似注意力的机制，学习为另一个神经网络编写权重。
*   **生成对抗网络（GANs）：** 文中提到了1990-1991年关于“人工好奇心”的论文，这些研究引入了两个神经网络相互竞争的对抗博弈。这一原理早于并奠定了现代GAN的基础。
*   **分层深度学习：** 他在1991年开发的“神经分块器”系统开创了分层循环神经网络的先河，用以解决涉及长时间滞后和复杂序列的问题。

施密德胡伯总结道，1990-1991这个“奇迹年”为深度学习模型提供了蓝图，这些模型如今驱动着从智能手机助手到ChatGPT等各类高级生成式AI。他强调，虽然现代算力使这些工具无处不在，但当前AI热潮的核心“大脑”早在30多年前就在慕尼黑构建完成了。

---

## 7. 投资者首次可实时掌握英国债券市场动态

**原文标题**: Investors get real-time view of UK bond market activity for the first time

**原文链接**: [https://www.fca.org.uk/news/press-releases/investors-get-real-time-view-uk-bond-market-activity-first-time](https://www.fca.org.uk/news/press-releases/investors-get-real-time-view-uk-bond-market-activity-first-time)

英国推出了首个由 **ETS Connect UK** 运营的实时债券综合交易报告（consolidated tape）。这项新服务为投资者提供了英国债券市场价格和交易数据的单一、综合来源，取代了以往数据分散在多个来源的碎片化系统。

此次上线遵循了 2025 年 12 月实施的透明度规则变更，该变更显著增加了实时报告量。公司债券交易报告率从不足 5% 提升至 75% 以上，而政府债券报告率则从 30% 提升至约 80%。随着该系统的推出，英国成为北美以外首个建立债券综合交易报告的国家。

**该服务的主要细节包括：**
*   **覆盖范围：** 涵盖了 98% 的相关债券交易，不包括交易所交易票据（ETN）和交易所交易商品（ETC）。
*   **监管：** 英国金融行为监管局（FCA）将根据一份为期五年的合同对 ETS Connect UK 进行监督，以确保数据的质量和及时性。
*   **选拔过程：** ETS Connect UK 是在 2025 年 3 月的竞争性招标后获任的；Ediphy 对该任命提出的法律挑战已于 2026 年 5 月终止。

来自 FCA、英国金融协会（UK Finance）和国际资本市场协会（ICMA）的行业领袖对这一进展表示赞赏，称其将增强市场流动性、价格发现功能以及英国作为金融枢纽的全球竞争力。该系统的推出是更广泛透明度计划的核心组成部分，FCA 已经在着手为股票和 ETF 建立类似的综合交易报告。

最终，该报告提供了一个可靠的“单一事实来源”，使更广泛的投资者能够做出更明智的决策，并增强了英国资本市场的整体效率。

---

## 8. 为什么数位板品牌不愿协作开发 Linux FLOSS 驱动

**原文标题**: Why Drawing Tablet Brands Won't Collaborate on Linux Floss Drivers

**原文链接**: [https://www.davidrevoy.com/article1154/why-drawing-tablet-brands-wont-collaborate-on-linux-floss-drivers](https://www.davidrevoy.com/article1154/why-drawing-tablet-brands-wont-collaborate-on-linux-floss-drivers)

一位专注于 Linux 兼容绘图板的 YouTube 硬件评测者，近期尝试在主要制造商（高漫、绘王和 XpPen）与 Linux 内核输入开发者之间建立协作。多年来，作者一直通过手动逆向工程硬件规格，协助开发者 Peter Hutterer 和 Benjamin Tissoire 在 `udev-hid-bpf` 项目下开发开源驱动。

为了寻求更高效的“直接合作”模式，作者联系了这些品牌背后的技术团队。尽管调研发现深圳绘王趋势科技负责了多个竞争品牌的技术开发，但这些品牌最终均拒绝了直接合作的提议。

核心障碍在于 Linux 开源基础架构中历史遗留的“Wacom”品牌烙印。诸如 `libwacom` 和 `wacom-hid-descriptors` 等绘图板支持核心仓库，尽管已兼容众多品牌，却仍沿用着行业最大竞争对手的名字。高漫和绘王担心，参与其中意味着要与 Wacom 主导的项目共享规格，且此类命名会削弱其自身的品牌身份。

作者指出，虽然通过 `hid-recorder` 等逆向工具可以轻松获取规格，但将通用基础架构以特定品牌命名的“设计决策失误”造成了严重的跨企协作障碍。因此，作者不得不回归手动逐一记录设备规格的原始方式，并继续依靠志愿者开发者来维护 Linux 兼容性。作者总结道，在基础架构实现品牌中立之前，该行业不太可能在官方开源驱动开发上达成协作。

---

## 9. Granularity comes at a cost

**原文标题**: Granularity comes at a cost

**原文链接**: [https://www.sidhantbansal.com/2026/Granularity-comes-at-a-cost/](https://www.sidhantbansal.com/2026/Granularity-comes-at-a-cost/)

生成摘要时出错

---

## 10. Maria Isabel Sánchez Vegara on Her 100th "Little People, Big Dreams" Book

**原文标题**: Maria Isabel Sánchez Vegara on Her 100th "Little People, Big Dreams" Book

**原文链接**: [https://www.amightygirl.com/blog?p=36753](https://www.amightygirl.com/blog?p=36753)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 2 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 3 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 4 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 5 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 6 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 7 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 8 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 9 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 10 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 11 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 12 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 13 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 14 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 15 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 16 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 17 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 18 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 19 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 20 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 21 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 22 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 23 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 24 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 25 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 26 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 27 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 28 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 29 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 30 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 31 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 32 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 33 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 34 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 35 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 36 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 37 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 38 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 39 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 40 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 41 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 42 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 43 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 44 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 45 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 46 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 47 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 48 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 49 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 50 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 51 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 52 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 53 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 54 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 55 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 56 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 57 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 58 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 59 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 60 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 61 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 62 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 63 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 64 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 65 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 66 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 67 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 68 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 69 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 70 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 71 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 72 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 73 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 74 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 75 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 76 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 77 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 78 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 79 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 80 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 81 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 82 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 83 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 84 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 85 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 86 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 87 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 88 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 89 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 90 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 91 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 92 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 93 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 94 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 95 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 96 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 97 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 98 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 99 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 100 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 101 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 102 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 103 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 104 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 105 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 106 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 107 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 108 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 109 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 110 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 111 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 112 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 113 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 114 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 115 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 116 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 117 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 118 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 119 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 120 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 121 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 122 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 123 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 124 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 125 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 126 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 127 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 128 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 129 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 130 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 131 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 132 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 133 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 134 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 135 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 136 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 137 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 138 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 139 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 140 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 141 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 142 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 143 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 144 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 145 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 146 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 147 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 148 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 149 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 150 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 151 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 152 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 153 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 154 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 155 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 156 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 157 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 158 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 159 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 160 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 161 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 162 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 163 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 164 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 165 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 166 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 167 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 168 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 169 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 170 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 171 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 172 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 173 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 174 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 175 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 176 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 177 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 178 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 179 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 180 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 181 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 182 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 183 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 184 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 185 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 186 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 187 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 188 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 189 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 190 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 191 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 192 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 193 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 194 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 195 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 196 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 197 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 198 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 199 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 200 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 201 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 202 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 203 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 204 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 205 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 206 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 207 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 208 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 209 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 210 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 211 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 212 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 213 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 214 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 215 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 216 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 217 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 218 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 219 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 220 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 221 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 222 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 223 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 224 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 225 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 226 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 227 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 228 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 229 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 230 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 231 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 232 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 233 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 234 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 235 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 236 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 237 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 238 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 239 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 240 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 241 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 242 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 243 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 244 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 245 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 246 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 247 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 248 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 249 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 250 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 251 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 252 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 253 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 254 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 255 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 256 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 257 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 258 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 259 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 260 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 261 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 262 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 263 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 264 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 265 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 266 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 267 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 268 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 269 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 270 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 271 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 272 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 273 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 274 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 275 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 276 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 277 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 278 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 279 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 280 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 281 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 282 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 283 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 284 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 285 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 286 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 287 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 288 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 289 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 290 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 291 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 292 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 293 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 294 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 295 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 296 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 297 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 298 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 299 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 300 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 301 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 302 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 303 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 304 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 305 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 306 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 307 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 308 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 309 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 310 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 311 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 312 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 313 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 314 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 315 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 316 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 317 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 318 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 319 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 320 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 321 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 322 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 323 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 324 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 325 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 326 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 327 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 328 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 329 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 330 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 331 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 332 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 333 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 334 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 335 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 336 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 337 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 338 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 339 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 340 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 341 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 342 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 343 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 344 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 345 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 346 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 347 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 348 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 349 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 350 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 351 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 352 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 353 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 354 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 355 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 356 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 357 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 358 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 359 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 360 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 361 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 362 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 363 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 364 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 365 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 366 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 367 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 368 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 369 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 370 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 371 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 372 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 373 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 374 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 375 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 376 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 377 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 378 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 379 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 380 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 381 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 382 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 383 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 384 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 385 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 386 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 387 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 388 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 389 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 390 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 391 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 392 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 393 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 394 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 395 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 396 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 397 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 398 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 399 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 400 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 401 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 402 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 403 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 404 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 405 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 406 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 407 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 408 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 409 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 410 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 411 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 412 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 413 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 414 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 415 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 416 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 417 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 418 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 419 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 420 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 421 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 422 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 423 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 424 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 425 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 426 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 427 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 428 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 429 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 430 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 431 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 432 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 433 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 434 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 435 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 436 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 437 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 438 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 439 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 440 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 441 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 442 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 443 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 444 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 445 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 446 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 447 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 448 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 449 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 450 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 451 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 452 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 453 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 454 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 455 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 456 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 457 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 458 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 459 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
