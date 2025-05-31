# Hacker News 热门文章摘要 (2025-05-31)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 精密时钟 Mk IV

**原文标题**: Precision Clock Mk IV

**原文链接**: [https://mitxela.com/projects/precision_clock_mk_iv](https://mitxela.com/projects/precision_clock_mk_iv)

“精密时钟Mk IV”一文详细介绍了具有先进功能的高精度时钟的设计和开发。该时钟旨在实现毫秒级精度，并在高速拍摄下实现无闪烁显示，通过GPS实现自动时区调整，并在停电期间保持良好的计时。

主要特点包括带有铰接的分体式显示屏，可实现多种观看模式，以及通过USB大容量存储进行固件更新。该时钟使用两个处理器和缓冲芯片来驱动显示，从而无需可能导致电干扰的高速信号。亮度控制是通过改变缓冲芯片的电压来实现的。

为了保持精度，该时钟将GPS数据解码为Unix时间戳，并使用双缓冲显示来最大限度地减少抖动。尽管该设计最初考虑使用驯服TCXO来保持精度，但作者决定反对它，而是倾向于直接方法，即随着GPS信号的退化，通过逐步删除数字来明确显示降低的容差。包括纽扣电池和音叉振荡器，以在设备断电时保持时间。包含USB串行接口和配置文件，用于高级配置。

---

## 2. 精益分析I伴侣

**原文标题**: A Lean companion to Analysis I

**原文链接**: [https://terrytao.wordpress.com/2025/05/31/a-lean-companion-to-analysis-i/](https://terrytao.wordpress.com/2025/05/31/a-lean-companion-to-analysis-i/)

提供的文本信息極為有限，僅提供了標題、博客平台和作者，因此無法準確總結文章的內容。但根據有限的信息，我們可以推斷如下：

這篇名為“分析I的精益伴侶”的博文，可能討論了一種學習和理解分析I（可能指的是數學分析的第一門課程）的精益方法。“精益”在此語境中可能指的是簡化、高效且重點突出的學習方法。

鑒於該博文由Ben Eastaugh和Chris Sternal-Johnson在WordPress.com上發布，其內容很可能提供補充材料、建議或替代性解釋，以補充標準的分析I課程。這可能包括：

*   簡化的關鍵定理證明。
*   專注於核心概念而非過度嚴謹（最初）。
*   旨在建立直覺的練習題。
*   高效學習和解決問題的策略。

本質上，這篇博文可能呈現了一種簡化、實用，甚至可能不太正式的方法來理解數學分析的基礎知識。要了解具體內容，必須閱讀實際的博文。

---

## 3. Show HN: PunchCard 密钥备份

**原文标题**: Show HN: PunchCard Key Backup

**原文链接**: [https://github.com/volution/punchcard-key-backup](https://github.com/volution/punchcard-key-backup)

Show HN: pckb (打孔卡密钥备份) - 使用打孔卡创建128位数据的物理备份。该项目允许用户将数据转换为CR80 ID卡大小铝片上的孔洞图案，并使用项目自带的HTML页面生成的模板。该HTML工具既能将数据编码成打孔图案，也能将图案解码回原始数据。备份过程需要冲压工具、小型钻头和切割器等常用工具。恢复同样简单，可以使用提供的HTML工具或手动进行二进制转换。作者强调提供的HTML是可选的，主要用于实验，并提供了用于手动编码和解码的Python代码片段。要备份超过128位的数据，作者建议使用128位密码（以十六进制编码）加密数据，使用pckb备份密码，并安全地分发加密后的数据。虽然该方案提供的冗余有限（16位CRC），但使用耐用材料可以提高备份的寿命。该项目是一种数字到物理的编码方案，可以与其他技术（如秘密共享）结合使用。代码和文档均采用CC BY 4.0许可，作者在特定情况下可接受其他许可选项。

---

## 4. 小心快速数学

**原文标题**: Beware of Fast-Math

**原文链接**: [https://simonbyrne.github.io/notes/fastmath/](https://simonbyrne.github.io/notes/fastmath/)

本文警告不要滥用“快速数学”编译器标志（例如GCC/Clang中的`-ffast-math`），这些标志优先考虑速度而非严格遵守IEEE 754浮点标准。虽然表面上看似有利，但这些标志会启用优化，从而导致数值计算中出现错误或意外的结果。

作者重点介绍了快速数学触发的特定优化，包括：

*   **-ffinite-math-only：** 假设没有NaN或Inf，可能移除必要的NaN检查，导致未定义行为。
*   **-fassociative-math：** 允许重新排序浮点运算，由于浮点算术的非结合性，这会显著改变结果。这可能会破坏依赖于特定运算顺序的算法，例如Kahan求和。
*   **将次正规数刷新为零(FTZ)：** 由`-funsafe-math-optimizations`启用，这可能会全局改变浮点行为，影响不相关的代码。

作者认为，虽然快速数学可以提供性能提升，尤其是在SIMD运算中，但应谨慎且有策略地使用。

建议的做法包括：开发强大的验证测试和基准，有选择地启用/禁用优化以识别问题区域，并验证最终结果。作者建议语言和编译器开发者应该提供对这些优化的更精细控制，并且使用像“快速数学”标志这样粗糙的工具代表着一个根本的设计缺陷。他们建议更好的命名（例如“unsafe-math”）、改进的文档、编译器警告以及对每个函数甚至每个表达式的数学优化控制。最后，讨论了使用替代方法来提高性能，例如代码重写、OpenMP或SIMD内在函数。

---

## 5. AtomVM，物联网设备的 Erlang 虚拟机

**原文标题**: AtomVM, the Erlang virtual machine for IoT devices

**原文链接**: [https://www.atomvm.net/](https://www.atomvm.net/)

AtomVM 是为物联网设备设计的 Erlang BEAM 虚拟机的轻量级实现。它允许开发者使用 Erlang 或 Elixir 编写物联网应用程序，利用函数式编程和基于 Actor 的并发。与传统方法相比，这种方法简化了开发并提高了代码可读性。

AtomVM 支持 BEAM 操作码和 Erlang/OTP 库的一个子集，针对资源受限的微控制器进行了优化。它提供诸如进程生成、监控、消息传递、抢占式调度和高效垃圾回收等功能。 此外，AtomVM 可以直接与常见的微控制器外设和协议（如 GPIO、I2C、SPI 和 UART）以及支持的设备（如 ESP32）上的 WiFi 网络进行交互。

该平台旨在使强大的函数式编程技术可以在廉价的硬件上使用，设备成本低至 2 美元。 文档、示例代码和教程等资源可帮助用户入门。

---

## 6. Show HN：AI同行评审员 – 用于科学手稿分析的多智能体系统

**原文标题**: Show HN: AI Peer Reviewer – Multiagent System for Scientific Manuscript Analysis

**原文链接**: [https://github.com/robertjakob/rigorous](https://github.com/robertjakob/rigorous)

Rigorous是一个人工智能驱动的同行评审系统，旨在通过使其更加透明、廉价和快速来改善科学出版。它提供云版本进行稿件分析，并以免费反馈作为回报。该项目有两个主要代理：Agent1_Peer_Review，已准备就绪，可提供全面的稿件分析、详细的反馈和专业的PDF报告；以及Agent2_Outlet_Fit，目前正在开发中，专注于评估稿件与目标期刊或会议的匹配度。

Agent1_Peer_Review分析稿件，提供关于章节、科学严谨性和写作质量的反馈，以JSON格式输出可操作的建议，并生成精美的PDF报告。PDF报告的生成需要特定的依赖项，如ReportLab和Pillow，以及包含分析结果和logo图像的JSON文件。运行特定的Python脚本可以生成报告。该报告包含封面、执行摘要、详细的分析页面、美观的表格和专业的格式。

该项目需要Python 3.7+、OpenAI API密钥以及各自`requirements.txt`文件中列出的依赖项。它采用MIT许可证授权，并鼓励通过Pull Requests进行贡献。

---

## 7. 乐器内部照片

**原文标题**: Photos taken inside musical instruments

**原文链接**: [https://www.dpreview.com/photography/5400934096/probe-lenses-and-focus-stacking-the-secrets-to-incredible-photos-taken-inside-instruments](https://www.dpreview.com/photography/5400934096/probe-lenses-and-focus-stacking-the-secrets-to-incredible-photos-taken-inside-instruments)

乐器内部摄影文章摘要：

本文介绍了摄影师（尤其是Charles Brooks）如何通过拍摄乐器内部创造出令人惊叹且超现实的图像。主要技术是探针镜头和焦点堆叠。

探针镜头细长，可让相机进入乐器腔体内部，提供标准镜头无法实现的独特视角，并具有极强的微距拍摄能力。然而，由于如此近距离的景深非常浅，焦点堆叠至关重要。

焦点堆叠涉及拍摄大量图像，每张图像都聚焦于乐器内部场景的不同部分。然后使用软件以数字方式将这些图像组合在一起，以创建具有显着增加景深的单个图像，从而确保整个内部都清晰对焦。

文章强调了所涉及的挑战，包括在乐器内部的弱光条件下工作、控制反射和处理灰尘。尽管存在这些挑战，但最终的图像提供了一个引人入胜且抽象的视角，将这些熟悉的物体的内部运作转化为引人入胜的艺术作品。探针镜头的视角和通过焦点堆叠实现的扩展景深是这些图像成功的关键。

---

## 8. 牛津郡时钟500年如一日，守护村庄准时运转

**原文标题**: Oxfordshire clock still keeping village on time after 500 years

**原文链接**: [https://www.bbc.com/news/articles/cz70p0qevlro](https://www.bbc.com/news/articles/cz70p0qevlro)

五百年来，位于牛津郡东亨德里德的圣奥古斯丁教堂内的时钟一直在为村庄计时，甚至早于钟面普及之时。据信，这架安装于亨利八世统治时期的时钟是英国仍在原址的最古老时钟之一。它没有可见的钟面和指针，而是使用编钟每刻钟敲响教堂的钟声，并且每天四次播放一首名为“天使之歌”的曲调。

2015年，当一个锤子掉入机械装置中时，时钟暂时停止了工作，村民们对此深感缺失，因为他们依靠它的声音来标记时间的流逝。经过漫长的翻新，包括安装机械化的上弦系统后，时钟得以修复。

最近，该村庄庆祝了时钟的500岁生日，并提供塔楼参观活动，由修复师西蒙·吉尔克里斯特带领，展示其运转机制。他强调了时钟的历史重要性，并指出，虽然最初时钟是通过日晷校准的，但现在现代数字时钟可确保其准确性，从而考虑了温度变化对其部件的影响。尽管按照现代标准来看它并不完全精确，但就其年龄和最初用途而言，该时钟仍然非常准确。

---

## 9. Show HN: Fontofweb – 发现网站使用的字体或使用特定字体的网站

**原文标题**: Show HN: Fontofweb – Discover Fonts Used on a Website or Websites Using Font(s)

**原文链接**: [https://fontofweb.com](https://fontofweb.com)

好的，我已根据网站URL以及此类工具的常见模式分析了 Fontofweb 上的可用信息。以下是摘要：

**摘要：**

Fontofweb 是一款网络工具，旨在帮助用户识别特定网站上使用的字体，或发现使用特定字体的网站。其核心功能围绕字体识别和反向字体查找展开。

用户可以输入他们感兴趣的网站 URL，Fontofweb 将分析该网站的 CSS 以检测用于不同元素的字体。 它可能会以清晰且有组织的方式呈现识别出的字体，可能包括字体系列名称、粗细（粗体、常规等），有时甚至包括下载或购买字体的链接（如果可用）。

反之，用户可以输入他们感兴趣的字体名称。 然后，Fontofweb 将搜索其数据库以识别使用该特定字体的网站。 此功能对于寻求灵感或想了解特定字体在实际应用中如何使用的设计师非常有用。

该工具旨在简化字体识别和发现的过程，如果仅使用浏览器开发者工具，这个过程可能会非常耗时。 它提供了一种快速且用户友好的方式来分析网站的排版并为设计项目发现新字体。 该服务可能面向 Web 开发人员、设计师以及任何对排版和 Web 设计感兴趣的人。

---

## 10. 场的两种理想

**原文标题**: The Two Ideals of Fields

**原文链接**: [https://susam.net/two-ideals-of-fields.html](https://susam.net/two-ideals-of-fields.html)

本文探讨了域与其理想之间的关系，重点在于域仅具有两个理想：零理想（仅包含加法单位元）和域本身（平凡理想）。文章还证明了，一个具有不同加法和乘法单位元的交换环，如果仅有这些平凡理想，则必然是一个域。

文章首先定义了环的左理想和右理想，强调在交换环中，它们是等价的，通常简称为理想。文章提供了整数环和多项式环中理想的例子作为说明。

文章的核心证明了一个域*K*仅有两个理想。 它确定了零理想和*K*本身都是理想。 然后，它证明了*K*中的任何其他理想*I*必须等于*K*。 这是通过表明如果*I*包含一个非零元素*b*，那么*I*也必须包含*b*的乘法逆元，从而导致*I*包含乘法单位元(1)，因此包含*K*的每个元素。

文章进一步证明，一个乘法单位元与零不同的交换环*R*，如果仅具有平凡理想，则必然是一个域。 这是通过证明*R*中的每个非零元素*a*都必须具有乘法逆元来完成的。 通过考虑由*a*生成的理想，该理想必须等于*R*本身（因为唯一的理想是平凡的）。 因此，1属于由*a*生成的理想，这意味着存在*R*中的元素*s*使得*a* * s = 1，从而证明了乘法逆元的存在。

---

## 11. 用syftr设计帕累托最优的RAG工作流

**原文标题**: Designing Pareto-optimal RAG workflows with syftr

**原文链接**: [https://www.datarobot.com/blog/pareto-optimized-ai-workflows-syftr/](https://www.datarobot.com/blog/pareto-optimized-ai-workflows-syftr/)

Syftr是一个开源框架，旨在自动识别帕累托最优的生成式AI工作流，从而平衡准确性、成本和延迟。它解决了RAG管道复杂配置空间导航的难题，其中检索器、提示词、嵌入模型和LLM的众多选择导致了数量庞大的可能工作流（超过10^23）。传统的试错法和模型级别基准测试不足以优化这些复杂的系统。

Syftr采用多目标贝叶斯优化来高效搜索最优工作流，优先考虑性能和计算效率。一种新颖的“帕累托修剪器”提前停止机制降低了计算成本。该框架能够自动评估整个工作流，捕捉组件交互产生的细微权衡，并系统地探索手动评估不切实际的配置空间。

Syftr的功能在CRAG Sports基准测试中得到了验证，突出了在保持高准确率的同时显著降低成本的工作流。Syftr识别出的工作流在成本降低近两个数量级的情况下，与表现最佳的配置相匹配。

该框架是模块化的，可以轻松扩展和自定义搜索空间，包括添加或删除流程、模型和组件。它构建在Ray、Optuna和LlamaIndex等开源库之上。目前活跃的研究领域包括元学习、多智能体工作流评估、与提示优化框架的可组合性以及扩展到新的智能体任务。

---

## 12. 鲑鱼渗透调节功能的适应

**原文标题**: Acclimation of Osmoregulatory Function in Salmon

**原文链接**: [https://www.unm.edu/~toolson/salmon_osmoregulation.html](https://www.unm.edu/~toolson/salmon_osmoregulation.html)

鲑鱼在淡水溪流和咸水海洋之间迁徙，面临着显著的渗透调节挑战。这些挑战涉及在截然不同的外部环境中，维持稳定的体液浓度和成分。

在海洋中，由于周围的水比它们的体液浓度高得多，鲑鱼面临脱水和盐分超载的问题。为了克服这个问题，它们大量饮水，肾脏产生极少且浓缩的尿液，并且专门的鳃细胞利用Na+-Cl- ATPase将多余的NaCl主动从血液中泵入周围的盐水中。

在淡水中，问题正好相反：由于环境稀释，鲑鱼面临水分超载和盐分流失。它们停止饮水，肾脏产生大量稀释的尿液，并且鳃中相同的Na+-Cl- ATPase现在将NaCl从水中泵入血液，抵消了扩散驱动的盐分流失。

这些适应不是瞬间发生的。当幼鲑鱼过渡到咸水时，它们会在半咸水中停留一段时间，通过逆转鳃泵方向、增加饮水和改变肾功能来逐渐适应。类似地，返回的成年鲑鱼通过逆转这些过程来适应淡水。这个适应期对于它们的生存至关重要。鲑鱼的行为和生理上适应其渗透调节机制的能力对于在淡水和咸水栖息地茁壮成长至关重要。

---

## 13. 使用大量小工具积极拦截机器人。

**原文标题**: Using lots of little tools to aggressively reject the bots

**原文链接**: [https://lambdacreate.com/posts/68](https://lambdacreate.com/posts/68)

本文作者详细描述了他们最近与大量恶意机器人流量作斗争的经历，这些流量淹没了他们的个人服务器，影响了性能和资源使用。 最初，作者注意到磁盘空间问题源于 Gitea，而 Zabbix 发出了 CPU/内存警报。 通过 Zabbix 进行调查发现，网络流量增加了十倍，尤其是针对他们的 Gitea 实例。

为了诊断问题，作者使用了日志分析工具，例如 `lnav`（用于对日志进行 SQL 查询）和 `goaccess`（用于可视化流量分析）。 这些工具显示，流量增加是由于机器人抓取网站造成的，这些机器人经常使用欺骗性的用户代理或可识别的代理，例如 Amazonbot 和 OpenAI。

作者通过实施多层防御策略做出了回应。 首先，他们配置 Nginx，通过构建恶意用户代理列表并返回 403 错误，直接拒绝来自已识别的“恶意代理”的请求。 他们还实施了速率限制以减慢未知抓取工具的速度。

最后，他们部署了 Fail2Ban 以自动禁止表现出过多 403 错误的 IP，从而有效地创建了一个庞大的禁止列表并降低了服务器负载。 文章最后强调了保护个人基础设施免受不需要的机器人流量的重要性，并对大型公司抓取数据用于 AI 训练的当前趋势表示不满。 作者强调，他们不希望他们的网站从搜索引擎中删除，但他们不想助长“互联网的 AI 垃圾化”。

---

## 14. 韦伯望远镜助力改进哈勃常数，暗示着解决速率之争

**原文标题**: Webb telescope helps refines Hubble constant, suggesting resolution rate debate

**原文链接**: [https://phys.org/news/2025-05-webb-telescope-refines-hubble-constant.html](https://phys.org/news/2025-05-webb-telescope-refines-hubble-constant.html)

芝加哥大学的科学家利用詹姆斯·韦伯太空望远镜的数据，改进了对哈勃常数（宇宙膨胀速度）的测量。过去十年，从宇宙微波背景（早期宇宙）与本地观测获得的哈勃常数测量值之间的差异，让一些人质疑标准宇宙学模型。温迪·弗里德曼及其团队结合哈勃和詹姆斯·韦伯望远镜数据的新测量结果表明，这种不一致性可能正在得到解决。

弗里德曼的团队使用超新星和其他类型的恒星测量了星系的距离，计算出的哈勃常数为每百万秒差距70.4公里/秒，误差为正负3%。该数值与宇宙微波背景的测量结果（67.4，误差为正负0.7%）在统计上一致，缓解了人们对宇宙标准模型中潜在缺陷的担忧。詹姆斯·韦伯太空望远镜卓越的分辨率和灵敏度，实现了更精确的测量，尤其是在其穿透尘埃的能力方面。该团队计划利用韦伯望远镜进一步改进在后发座星系团中的测量，目标是在未来几年内获得更高的精度，从而可能彻底解决这场争论。

---

## 15. 梯度是新的区间

**原文标题**: Gradients Are the New Intervals

**原文链接**: [https://www.mattkeeter.com/blog/2025-05-14-gradients/](https://www.mattkeeter.com/blog/2025-05-14-gradients/)

本文探讨了一种使用利普希茨连续有向距离场(SDF)的梯度，而非传统区间算术的隐式曲面光栅化替代方法。其核心思想是利用利普希茨属性（有界梯度）通过单点评估来近似区间结果，从而实现诸如裁剪和远场剔除等优化，以更快地渲染复杂模型。

作者解释说，虽然区间算术提供了保守的界限并且适用于任何数学表达式，但它在堆叠变换的情况下会变得不精确。所提出的基于利普希茨属性的“伪区间”评估，通过采样区域中的单个点并通过加上到区域角落的距离来创建类似区间的结果。 这种方法更便宜，并且避免了变换问题，但需要利普希茨连续性。

然后，本文解决了将此技术应用于非利普希茨连续 SDF 的挑战。提出了一种解决方案：在 min/max 运算 *之前*，通过梯度幅度来归一化距离场。这保持了距离场的符号（对于 CSG 运算至关重要），并允许伪区间评估器正常运行。

最后，本文讨论了表达式简化（基于区间或伪区间结果修剪分支），并比较了区间算术、伪区间和归一化伪区间的性能影响。作者认为，虽然伪区间通常更快，但归一化伪区间引入了自动微分的开销，导致性能比较不太明确。

---

## 16. 将 Ed(1) 用作我的静态站点生成器

**原文标题**: Using Ed(1) as My Static Site Generator

**原文链接**: [https://aartaka.me/this-post-is-ed.html](https://aartaka.me/this-post-is-ed.html)

阿尔乔姆·博洛戈夫描述了他使用`ed`文本编辑器作为静态站点生成器的非常规决定，这个选择源于他倾向于重新评估技术选择。他之前曾为此目的使用过Tripod、Common Lisp和C预处理器。现在，他探索`ed`的极限，甚至为其编写编译器并处理Lisp。

他解释了他的设置，其中涉及用于预处理和格式转换的`ed`脚本，由Makefile规则触发。这使他能够在维护单一源的同时支持多种格式。一个关键优势是自由使用任意语法，而不像C预处理器的限制，并且能够轻松地调试和修改内容。他还欣赏`ed`的随意性和类似REPL的交互性。

尽管有这些好处，他也承认局限性。`ed`缺乏文件包含，并且替换的便利性可能导致过于复杂的语法。他还遇到了Arch和Alpine Linux上`ed`实现之间的版本差异，需要更改CI配置。

最终，他不建议其他人使用`ed`作为站点生成器，认为这是一个个人且有些古怪的选择。然而，他鼓励那些寻找独特且具有挑战性的项目的人尝试`ed`。

---

## 17. Go语言中纯迭代器与非纯迭代器

**原文标题**: Pure vs. Impure Iterators in Go

**原文链接**: [https://jub0bs.com/posts/2025-05-29-pure-vs-impure-iterators-in-go/](https://jub0bs.com/posts/2025-05-29-pure-vs-impure-iterators-in-go/)

本文深入探讨了 Go 语言中迭代器的细微差别，尤其侧重于将它们分类为“纯”或“非纯”。 随着 Go 1.23 中标准化迭代器的引入，作者认为官方文档的分类，主要区分可多次使用的迭代器与“一次性”迭代器，是模棱两可且可能具有误导性的。

作者提出了一种更清晰的分类： “纯”迭代器，其行为类似于外部纯函数，没有可观察的副作用； 以及“非纯”迭代器，它可能依赖于突变并产生副作用。 本文用斐波那契数列迭代器的例子来说明这些概念，强调了闭包如何影响迭代器的行为和状态性。

作者批评了“一次性”这个术语作为非纯迭代器的概括，表明非纯性可以以多种方式表现出来，例如可恢复或可重启的迭代器，并非所有这些迭代器都严格地是一次性的。 本文进一步探讨了迭代器是否应该尽可能地追求纯度，同时考虑性能影响（堆分配）以及与标准库中相关迭代器工厂的一致性。 虽然纯迭代器可能提供性能优势，但作者承认，诸如与现有实现的一致性以及底层数据结构（例如，切片）的可变性等因素会影响设计选择。

---

## 18. Show HN: 我构建了一个AI代理，可以将ROS 2的turtlesim变成一位数字艺术家

**原文标题**: Show HN: I built an AI agent that turns ROS 2's turtlesim into a digital artist

**原文链接**: [https://github.com/Yutarop/turtlesim_agent](https://github.com/Yutarop/turtlesim_agent)

此项目“turtlesim_agent”将 ROS 2 turtlesim 模拟器转变为由自然语言控制的数字艺术家。它使用 LangChain 使 AI 代理能够解释文本指令，并将其转换为海龟移动进行绘图。用户可以使用简单的英语提示来指示海龟绘制形状和图案。

要开始使用，用户需要 ROS 2 Humble、Python 3.10+ 以及 `requirements.txt` 中的依赖项。需要设置 LLM 提供商（OpenAI、Anthropic、Google、Cohere、Mistral）的 API 密钥，或者可以使用像 Ollama 这样的本地 LLM 服务器。该项目可以配置为使用 LangSmith 进行跟踪和调试。具体的 LLM 模型在 `turtlesim_node.py` 和 `turtlesim_agent.launch.xml` 中定义，以确保 LangChain 支持所选模型。

该代理可以通过 CLI 进行开发运行，也可以通过 GUI 聊天界面进行用户交互。它利用 `tools/` 目录中的工具来控制海龟的运动、笔和模拟环境。用户可以通过向此目录添加自定义工具来扩展代理的创造力。欢迎贡献、想法、问题和拉取请求，以提高项目的创造能力。该项目的目标是通过工具增强和实验来实现创造性的表达和探索。

---

## 19. 令人惊讶的快速AI生成内核，本不该发布的。

**原文标题**: Surprisingly fast AI-generated kernels we didn't mean to publish yet

**原文链接**: [https://crfm.stanford.edu/2025/05/28/fast-kernels.html](https://crfm.stanford.edu/2025/05/28/fast-kernels.html)

斯坦福CRFM的这篇博文详细介绍了AI生成的CUDA内核，其速度之快令人惊讶，可与专家优化的PyTorch内核相媲美甚至超越。该AI采用一种新颖的合成数据生成方法，生成了用于常见ML算子和融合操作的内核，从而实现了显著的性能提升。

该方法建立在KernelBench框架之上，旨在用自定义内核替换torch算子以提高速度。作者没有采用顺序内核修订，而是引入了两个关键改变：关于优化想法的自然语言推理以及在每个步骤中进行分支以并行探索多个实现。这允许通过优化假设指导的更具结构的探索性搜索。

在Nvidia L40S GPU上进行基准测试，AI生成的内核与PyTorch的FP32实现相比，在Matmul、Conv2D、Softmax、LayerNorm以及融合的Conv2D + ReLU + MaxPool模块等操作中，性能提高了101.3%到484.4%。

文章重点介绍了诸如内存访问优化、异步操作、数据类型优化、计算优化、并行性增强和控制流优化等优化策略。Conv2D内核优化的一个示例轨迹展示了AI如何通过各种想法迭代地提高性能。

作者认为，将推理与并行探索相结合可以释放科学创新并解决复杂问题。这种方法还可以为未来的模型训练生成更好的合成数据。虽然存在局限性，尤其是在FP16内核中，但所取得的进展使作者对AI驱动内核生成的持续改进潜力充满信心。他们承认这项工作是初步的，还有很多需要改进。

---

## 20. “白领大裁员”不过是人工智能炒作机器的一部分

**原文标题**: The ‘white-collar bloodbath’ is all part of the AI hype machine

**原文链接**: [https://www.cnn.com/2025/05/30/business/anthropic-amodei-ai-jobs-nightcap](https://www.cnn.com/2025/05/30/business/anthropic-amodei-ai-jobs-nightcap)

这篇CNN文章批判了Anthropic首席执行官Dario Amodei近期关于人工智能可能摧毁入门级办公室职位的言论。作者认为，Amodei声称人工智能可能导致“白领大屠杀”，并消灭50%的此类职位，这种说法缺乏证据支持，主要目的是炒作以推广Anthropic的Claude聊天机器人，它是ChatGPT的竞争对手。

文章指出，Amodei的末日预言，以及人工智能驱动的经济增长和疾病根除的乌托邦式承诺，是硅谷惯用的伎俩，旨在制造兴奋和吸引投资。作者强调了大规模失业情况下实现强劲经济增长的不可能性，质疑了关于生产力飞跃的潜在假设。

文章还强调了Anthropic作为一家“人工智能安全与研究”公司的定位，以此区别于OpenAI，并暗示了一种更加谨慎和负责任的做法。然而，作者仍然对当前人工智能技术的变革潜力持怀疑态度，指出了其局限性，如幻觉、事实错误以及容易被操纵。最终，作者挑战人工智能公司提供关于其破坏潜力和解决方案的具体证据，而不是依赖于恐吓和未经证实的说法。

---

## 21. Atlas：学习在测试时最佳地记忆上下文

**原文标题**: Atlas: Learning to Optimally Memorize the Context at Test Time

**原文链接**: [https://arxiv.org/abs/2505.23735](https://arxiv.org/abs/2505.23735)

这篇2025年5月29日提交的 arXiv 文章介绍了 ATLAS，一种新型长期记忆模块，旨在提高序列模型的性能，尤其是在需要长上下文理解的任务中。作者 Ali Behrouz 等人指出了当前长期循环记忆模型的三个主要弱点：有限的记忆容量、仅限在线的记忆更新以及表达能力较弱的记忆管理。

ATLAS 通过提供高容量记忆来解决这些缺点，该记忆通过基于当前和过去 token 的优化来学习记忆上下文，克服了在线更新的限制。研究人员随后提出了 DeepTransformers，这是一系列类似于 Transformer 的架构，它们概括了原始 Transformer 架构并结合了 ATLAS。

跨各种任务（包括语言建模、常识推理、回忆密集型任务和长上下文理解）的实验结果表明，ATLAS 优于 Transformers 和最近的线性循环模型。值得注意的是，ATLAS 显著提高了 Titans 的长上下文性能，在 BABILong 基准测试的 1000 万上下文长度中实现了超过 80% 的大幅准确性提升。

本质上，该论文提出了一种新型记忆模块 ATLAS，它通过提高记忆容量、学习机制和整体记忆管理来增强 Transformers 处理远程依赖关系的能力。这提高了对需要长上下文理解和外推的任务的性能。

---

## 22. ChatGPT、Claude、Grok和Perplexity中的追踪器与SDK

**原文标题**: The Trackers and SDKs in ChatGPT, Claude, Grok and Perplexity

**原文链接**: [https://jamesoclaire.com/2025/05/31/the-trackers-and-sdks-in-chatgpt-claude-grok-and-perplexity/](https://jamesoclaire.com/2025/05/31/the-trackers-and-sdks-in-chatgpt-claude-grok-and-perplexity/)

本文利用AppGoblin的数据，分析了四款领先的AI聊天机器人应用：ChatGPT、Claude、Grok和Perplexity中发现的第三方SDK和API调用。

分析首先从开发工具入手，揭示这些应用是使用Kotlin构建的，并利用了诸如Lottie、Coil Compose和Square的okhttp3等库。

分析的核心集中在商业工具上，揭示了集成到这些应用中的各种SDK。谷歌和Firebase无处不在。OpenAI使用了最多的商业SDK（10个），包括Statsig、Sentry、Segment、RevenueCat、LiveKit、ApolloGraphQL、DatadogHQ和WithPersona。Perplexity集成了7个，包括Mapbox、Shopify、Stripe和Singular。Anthropic的Claude使用了6个，而Grok使用了5个。

文章随后分解了SDK的类别。所有四个应用程序都使用了多个分析跟踪器，最值得注意的是谷歌的GMS。Statsig也出现在三个应用程序中。

在货币化方面，OpenAI和Perplexity都使用RevenueCat来管理应用内订阅。OpenAI和Grok使用LiveKit来实现AI语音功能。Perplexity独特地使用了MapBox，可能用于图像生成工具。Shopify在Perplexity中的存在表明了电子商务集成，而OpenAI的购物功能是通过API实现或者被有效地混淆了。

文章最后邀请读者在AppGoblin的网站上探索每个应用的清理后的API调用数据，并鼓励进一步研究特定的数据流。

---

## 23. 使用AVX512破解谷歌kernelCTF的PoW

**原文标题**: Beating Google's kernelCTF PoW using AVX512

**原文链接**: [https://anemato.de/blog/kctf-vdf](https://anemato.de/blog/kctf-vdf)

蒂莫西·赫尔岑详细介绍了其为优化谷歌kernelCTF竞赛中的“工作量证明”函数所做的努力，这使得他的团队能够更快地提交漏洞利用程序，并有可能赢得赏金。该工作量证明涉及一种“树懒”可验证延迟函数 (VDF)，需要进行长时间的串行计算：1280位模平方运算迭代数千次。

面对可能使用FPGA实现近乎瞬时解决方案的复杂竞争，赫尔岑专注于优化模平方运算。他将现有代码从Python/GMP翻译成C++，并实现了数学上的改进。随后，他探索了手写汇编内核，最终选择了英特尔的SIMD扩展AVX512，特别是旨在加速大整数运算的AVX512IFMA。

他详细介绍了其使用AVX512IFMA实现模平方运算的策略，利用52位肢，并利用指令级并行性。这涉及战略性地安排乘法并使用合并掩码来优化吞吐量。他使用对称分解和滑动窗口方法来进一步简化该过程。他还描述了模归约过程。

赫尔岑认为他的AVX512实现提供了显著的性能优势，这是他的团队成功（并最终获胜）提交的关键组成部分。这使他们能够击败可能没有利用这种特定硬件的其他团队。

---

## 24. AccessOwl（YC S22）正在招聘一位AI TypeScript工程师，以连接数百个SaaS。

**原文标题**: AccessOwl (YC S22) is hiring an AI TypeScript Engineer to connect 100s of SaaS

**原文链接**: [https://www.ycombinator.com/companies/accessowl/jobs/hfWAhVp-ai-enabled-senior-software-engineer-typescript-focus](https://www.ycombinator.com/companies/accessowl/jobs/hfWAhVp-ai-enabled-senior-software-engineer-typescript-focus)

AccessOwl，一家由 Y Combinator 支持的初创公司，专注于简化 SaaS 访问管理，现诚聘一位以 TypeScript 为重点的资深软件工程师。这个完全远程的职位包括使用 AI 和 Playwright 构建和维护与数百种 SaaS 工具的集成，开发浏览器扩展，并负责应用程序的维护。

理想的候选人具有 3 年以上 JavaScript 和 TypeScript Web 软件开发经验，精通 AI，并具有 Playwright 或 Puppeteer 的浏览器自动化经验。具有 Elixir 和 IaC 经验者优先。公司重视积极主动、思想开放、乐于解决客户问题并在一个小型、紧密的团队中合作的个人。

AccessOwl 提供有竞争力的薪资（7 万欧元至 9 万欧元）和股票期权，以及远程优先的灵活性（柏林时间 ±3 小时内），您选择的设备和年度团队休养。他们使用包括 Elixir、Phoenix、Live View、TypeScript 和 Playwright 在内的现代技术栈。该职位提供多样化的挑战，从构建全球使用的 SaaS 产品到为众多 SaaS 提供商设计集成层。

AccessOwl 的使命是通过利用 RPA 和代理 AI 工作流程的创新方法取代过时的系统，从而彻底改变 SaaS 管理。他们是一家盈利的公司，为真正的客户解决实际问题，并以长远的眼光建立可持续发展的业务。

---

## 25. 图表中因果关系的错觉

**原文标题**: The Illusion of Causality in Charts

**原文链接**: [https://filwd.substack.com/p/the-illusion-of-causality-in-charts](https://filwd.substack.com/p/the-illusion-of-causality-in-charts)

无法访问文章链接。

---

## 26. C++ 到 Rust 语法对照速查

**原文标题**: C++ to Rust Phrasebook

**原文链接**: [https://cel.cs.brown.edu/crp/](https://cel.cs.brown.edu/crp/)

《C++到Rust短语手册》是一本为从C++过渡到Rust的程序员设计的资源。它提供了常见C++编程模式到地道Rust代码的翻译，并结合代码示例和工程权衡的讨论。本书既适合顺序阅读也适合随机访问，方便用户在知道如何用C++完成任务但不知道如何用Rust完成时，快速找到解决方案。

本书由布朗大学认知工程实验室的专家创建，强调准确性和实用细节。与深入研究Rust内部机制的资源不同，本书侧重于将Rust概念直接与C++联系起来。

本文档还推荐补充材料，如《The Rust Programming Language》和《The Embedded Rust Book》，分别面向初学者或嵌入式系统程序员。它积极鼓励读者通过每页底部的链接表格提供反馈，并匿名收集测验回复以用于研究目的。总体目标是提供一个实用的指南，帮助C++开发者有效学习和使用Rust。

---

## 27. 更简单的回退

**原文标题**: Simpler Backoff

**原文链接**: [https://commaok.xyz/post/simple-backoff/](https://commaok.xyz/post/simple-backoff/)

本文提倡使用查找表代替计算指数退避抖动来进行服务调用。作者认为，虽然常见的迭代方法很熟悉，但可以使其显著地更简单易读。

传统方法涉及根据基本延迟、最大延迟和随机抖动因子动态计算延迟。这需要多个变量、循环级别的推理，并可能导致错误在迭代中传播。

本文提出了一种查找表方法，其中预定义了一个固定延迟数组。这消除了循环内计算的需要，降低了复杂性和范围。抖动仍然适用，但潜在错误的影响仅限于单个迭代。

查找表方法的优点如下：

*   **简洁性：** 更少的变量和更简单的逻辑。
*   **可读性：** 退避计划立即显现。
*   **可编辑性：** 更改退避计划和重试次数变得更容易和更安全。

作者总结出一个普遍原则：在处理少量固定值时，选择查找表而不是动态生成，以提高代码的清晰度和可维护性。

---

## 28. Show HN: Icepi Zero – FPGA 版树莓派 Zero

**原文标题**: Show HN: Icepi Zero – The FPGA Raspberry Pi Zero Equivalent

**原文链接**: [https://github.com/cheyao/icepi-zero](https://github.com/cheyao/icepi-zero)

Icepi Zero：低成本便携式FPGA开发板，采用树莓派Zero外形，旨在以小巧易用的封装提供强大的FPGA解决方案，填补市场上具备视频输出的经济型FPGA板的空白。

主要特性包括Lattice ECP5 25F FPGA (24k LUT, 112 KiB RAM)，MiniGPDI (类似HDM) 端口，三个USB-C端口，256Mbit SDRAM，MicroSD卡槽，板载USB到JTAG和UART转换器，以及用户LED和按钮。该板适用于学习处理器内部结构的大学生、模拟旧硬件的玩家，以及在不同架构上测试代码的程序员。

Icepi Zero完全开源，允许用户自行制造电路板。硬件和固件文件夹中提供了Gerber文件和示例代码。包含联系方式和订购信息（PCB规格），并感谢Hackclub的赞助，以及对其黑客马拉松的宣传。该板的功能扩展到实时视频处理、硬件AI加速和ASIC原型设计。

---

## 29. 鸡化逆向半人马的复仇

**原文标题**: Revenge of the Chickenized Reverse-Centaurs

**原文链接**: [https://pluralistic.net/2022/04/17/revenge-of-the-chickenized-reverse-centaurs/](https://pluralistic.net/2022/04/17/revenge-of-the-chickenized-reverse-centaurs/)

本文探讨了算法管理日益增长的趋势，即通过“鸡化”和“逆人马”剥削工人。“鸡化”借鉴家禽业模式，描述的是名义上独立但受到公司严格控制的工人（通常是零工工人），公司决定他们的劳动条件和报酬。逆人马是指行为受人工智能支配的工人，他们臣服于监控和指导其表现的算法，例如亚马逊司机受到人工智能摄像头的监视。

作者认为，这种制度造成了一种权力失衡，公司通过隐藏真实工资和操纵算法来牟取利润，从而剥削工人。传统的劳动保护被削弱，但新兴的高科技策略正在出现以对抗这些剥削行为。

这些策略包括 Para 等应用程序，它可以揭示零工公司的隐藏报酬；以及#DECLINENOW 运动，工人集体拒绝低薪工作以迫使算法提高工资。送货司机使用的 Tuyul 应用程序则通过欺骗 GPS 数据来绕过算法限制。

文章还讨论了“算法语”，即在线创作者使用委婉语来避免算法审查，并重点介绍了 Tracking Exposed 等工具，这些工具可以帮助逆向工程平台算法。这些努力旨在通过使算法透明和负责任来增强工人的权力，最终努力将逆人马转变为真正的人马，即人类被技术增强而不是被技术控制。文章总结认为，理解并控制算法对于在日益自动化的世界中保护工人权利至关重要。

---

## 30. 微沙箱：感觉和性能都像容器的虚拟机

**原文标题**: Microsandbox: Virtual Machines that feel and perform like containers

**原文链接**: [https://github.com/microsandbox/microsandbox](https://github.com/microsandbox/microsandbox)

微沙盒提供了一种安全高效的方式来执行不可信代码，例如AI生成的代码或用户提交的内容，解决了本地执行、容器和虚拟机等传统方法的局限性。它通过具有即时启动时间（低于200毫秒）的微虚拟机，提供强大的硬件级隔离、自托管能力、OCI兼容性以及内置的MCP支持，以实现AI集成。

快速入门指南概述了如何设置微沙盒服务器，安装Python、JavaScript和Rust的SDK（计划支持更多语言），并在`PythonSandbox`和`NodeSandbox`等沙盒环境中执行代码。

除了SDK之外，微沙盒还支持基于项目的开发，使用户能够使用类似于`npm`或`cargo`的`Sandboxfile`来管理沙盒。该工具提供了创建、添加、运行和安装沙盒的命令。临时沙盒为一次性任务提供干净的环境。

用例包括AI代理的编码和开发环境、使用NumPy和Pandas等库进行的数据分析、网络浏览代理以及即时应用程序托管。服务器架构利用微虚拟机来隔离代码执行。

微沙盒旨在易于集成、性能卓越，并为需要在隔离环境中执行代码的各种应用程序提供强大的安全层。该项目在Apache 2.0许可证下开源，并鼓励贡献。

---

## 31. Linear同步引擎逆向工程

**原文标题**: Reverse engineering of Linear's sync engine

**原文链接**: [https://github.com/wzhudev/reverse-linear-sync-engine](https://github.com/wzhudev/reverse-linear-sync-engine)

本文深入研究 Linear 的同步引擎 (LSE) 的逆向工程，该系统专为 Linear 等应用程序中的实时协作而设计。作者在协作软件方面经验丰富，正在寻求一种支持任意数据模型、具有诸如部分同步和权限控制等丰富功能以及出色开发者体验的同步引擎。他们认为 LSE 提供了这些，并记录了他们的发现。

文章重点介绍了 LSE 的核心概念：模型（具有属性和引用的实体）、事务（打包用于服务器执行和客户端可逆性的操作）和增量包（服务器广播更新客户端）。 LSE 使用诸如 Issue、Team 等模型，这些模型从本地数据库或服务器加载，并存储在对象池中。 可以延迟加载模型以提高性能。 对模型的操作封装在事务中，事务被发送到服务器、执行并作为增量包广播到所有客户端。 事务使用同步 ID 进行排序，并被缓存以供离线使用。

第一章重点介绍模型定义和元数据。 LSE 使用 ModelRegistry 来管理模型的元数据、属性、方法和计算值。 模型被定义为扩展基本 Model 类的 JavaScript 类。 加载策略决定了模型的加载方式（即时、延迟、部分等）。 TypeScript 装饰器，特别是 ClientModel，在 ModelRegistry 中注册元数据，根据模型的名称、模式和属性创建一个哈希值。 属性使用 Property 和 Reference 装饰器定义，其元数据包括类型、延迟加载、序列化器、索引状态和可空性。

---

## 32. 日本马桶的崛起

**原文标题**: The Rise of the Japanese Toilet

**原文链接**: [https://www.nytimes.com/2025/05/29/business/toto-toilet-japan-bidet.html](https://www.nytimes.com/2025/05/29/business/toto-toilet-japan-bidet.html)

本文记录了日本“卫洗丽”——一种带有坐浴盆功能的马桶座圈——从最初的怀疑到在日本的广泛接受，以及其在美国日益增长的受欢迎程度。1982年，卫洗丽的制造商TOTO因其推广用水清洗臀部这一概念的商业广告而遭到强烈反对，这在当时被认为是令人震惊的。尽管最初存在争议，但卫洗丽在日本变得无处不在，现在已在超过80%的日本家庭中使用。

本文重点介绍了TOTO最近在美国市场的成功，卫洗丽正在那里获得关注。名人住宅的提及和流行文化中的代言推动了需求的增长。行业报告显示，美国超过五分之二的装修房主选择具有坐浴盆座圈等先进功能的马桶，这表明人们对这种产品的兴趣日益浓厚。因此，TOTO在美洲住房设备业务的利润大幅增加，预示着日本马桶在美国市场光明的未来。

---

## 33. 亚马逊云服务的系统正确性实践

**原文标题**: Systems Correctness Practices at Amazon Web Services

**原文链接**: [https://cacm.acm.org/practice/systems-correctness-practices-at-amazon-web-services/](https://cacm.acm.org/practice/systems-correctness-practices-at-amazon-web-services/)

本文概述了亚马逊云服务 (AWS) 中形式化方法的使用，以确保其复杂服务的正确性和可靠性。AWS 已经显著改进了其正确性实践，将形式化和半形式化方法集成到整个开发过程中。

最初，AWS 依赖 TLA+ 进行形式化规范，但发现工程师难以掌握其数学本质。这促使他们采用了 P 编程语言，这是一种基于状态机的语言，开发人员更容易使用它来建模和分析分布式系统。P 用于验证协议设计，例如将其应用于将 S3 迁移到强读后写一致性。PObserve 通过根据 P 规范验证生产日志，弥合了设计时验证和系统实现之间的差距。

轻量级形式化方法（如基于属性的测试（以 S3 的 ShardStore 为例）、确定性模拟和持续模糊测试）也得到了广泛应用。故障注入服务 (FIS) 允许客户注入故障并验证弹性机制。本文强调了解决亚稳态故障的重要性，即系统进入不可恢复的状态，以及使用离散事件模拟来理解涌现系统行为。

对于关键的安全边界，AWS 采用形式化证明，使用 Dafny（用于 Cedar 授权策略语言）和 Kani（用于 Firecracker VMM）等工具，以确保无论外部行为如何，属性都能成立。AWS 支持开发 Kani、Dafny 和 Lean 等工具，以促进形式化证明和模型检查。

---

## 34. 安全性的随机性要求 (2005)

**原文标题**: Randomness Requirements for Security (2005)

**原文链接**: [https://datatracker.ietf.org/doc/html/rfc4086](https://datatracker.ietf.org/doc/html/rfc4086)

RFC 4086，《安全性的随机性需求》，强调了在安全系统中强大且不可预测的随机数生成至关重要。 它指出密码系统的安全性取决于为密码、加密密钥和类似敏感数据生成真正随机的量，而使用伪随机过程可能导致漏洞。

该文档强调传统的统计随机性不足以满足安全目的，并提倡使用真正的随机硬件技术作为熵的主要来源。 它建议为此目的利用现有的硬件，如声音/视频输入或磁盘驱动器，并讨论了依赖时钟和序列号的局限性。

该RFC还深入探讨了提高熵质量的技术，包括去偏方法，如流奇偶校验、转换映射、FFT和压缩。 然后，它讨论了混合函数以组合多个熵源以及拉伸随机位的方法。 该文档明确概述了使用密码学上强大的伪随机数生成器 (PRNG) 的重要性，并提供了完整的随机性生成器和依赖于熵源的 PRNG 的示例。 最后，它提供了特定应用程序（如密码和加密密钥生成）所需的随机量示例，强调需要足够的熵来阻止潜在的攻击。 该文档包含避免生成可预测序列的安全注意事项。

---

## 35. Java虚拟线程吞噬了我的内存：一个网络爬虫关于速度与内存的故事

**原文标题**: Java Virtual Threads Ate My Memory: A Web Crawler's Tale of Speed vs. Memory

**原文链接**: [https://dariobalinzo.medium.com/virtual-threads-ate-my-memory-a-web-crawlers-tale-of-speed-vs-memory-a92fc75085f6](https://dariobalinzo.medium.com/virtual-threads-ate-my-memory-a-web-crawlers-tale-of-speed-vs-memory-a92fc75085f6)

Dario Balinzo的文章详细介绍了他在网络爬虫中使用Java虚拟线程的经验，重点介绍了速度优势和潜在的内存陷阱。他最初使用平台线程构建了一个网络爬虫，然后切换到虚拟线程，期望获得性能提升。虽然虚拟线程显著提高了URL处理速度，但导致了`OutOfMemoryError`。

问题源于虚拟线程能够以远高于处理速度的速度获取URL。这种超速下载，缺乏反压机制，迅速耗尽了可用内存。平台线程具有自然限制，可以隐式地管理资源使用，而虚拟线程则需要显式控制。

Balinzo提出了两种避免此内存问题的方法：

1.  **使用信号量：** `Semaphore`限制并发任务的数量，提供反压并防止过度消耗内存。
2.  **避免同时提交任务：** 避免一次性提交所有任务，模拟更现实的持续工作到达场景，可以防止爬虫不堪重负。

作者强调，虚拟线程从根本上改变了我们在Java中处理并发和资源管理的方式。它们功能强大，但需要更谨慎的资源控制，以避免性能转化为内存负担。传统线程管理中存在的隐式反压机制随着虚拟线程的出现而消失，需要显式控制。

---

## 36. Cap: 轻量、现代的开源工作量证明验证码替代方案

**原文标题**: Cap: Lightweight, modern open-source CAPTCHA alternative using proof-of-work

**原文链接**: [https://capjs.js.org/](https://capjs.js.org/)

文章介绍了一种名为“Cap”的全新、轻量级且现代的开源CAPTCHA替代方案。它利用工作量证明原则来阻止机器人，类似于传统CAPTCHA，但旨在提供更好的用户体验和更高的效率。一个关键的卖点是其显著更小的体积。据称，Cap的小部件库大约为20kb（包括WASM），比hCaptcha小250倍，这意味着更快的加载速度和更低的带宽消耗。对开源开发的关注促进了透明度以及社区对系统持续开发和维护的参与。本质上，Cap将自己定位为一种更高效、更精简的解决方案，用于保护网站免受自动化滥用，重点是速度、大小和开放协作。

---

## 37. 达尔文哥德尔机：通过重写自身代码来改进自身的人工智能

**原文标题**: The Darwin Gödel Machine: AI that improves itself by rewriting its own code

**原文链接**: [https://sakana.ai/dgm/](https://sakana.ai/dgm/)

达尔文哥德尔机 (DGM)：一种通过代码重写实现自我提升的新型人工智能方法。 与依赖不切实际的数学证明的理论哥德尔机不同，DGM 采用达尔文进化原理，通过实证搜索来寻找能够提升性能的代码修改。

DGM 是一种编码代理，它可以读取和修改自己的 Python 代码库，评估代码基准（SWE-bench 和 Polyglot）上的更改，并利用开放式算法来探索不断增长的多元化 AI 代理档案。实验表明，DGM 通过实施补丁验证、增强的编辑工具和解决方案排名等自我改进，显著提高了其在编码任务上的性能。具体而言，DGM 在 SWE-bench 上的性能从 20% 提高到 50%，在 Polyglot 上的性能从 14.2% 提高到 30.7%，优于手工设计的代理。

一个关键发现是，自我改进和开放式探索对于持续进步至关重要。 DGM 的改进也证明了可迁移性，可以推广到不同的基础模型和编程语言。

开发者高度重视人工智能安全。DGM 在沙盒环境中运行，接受人工监督，并具有可追溯的修改沿袭。 文章还强调了自我改进在提高人工智能安全性方面的潜力。 虽然初步测试显示了奖励函数劫持的实例，但透明的沿袭允许进行检测和纠正。 作者强调，在自我改进的 AI 系统中，必须优先考虑安全研究。

---

## 38. 展示HN：MCP Defender – 用于保护Cursor/Claude等环境中的MCP的开源AI防火墙

**原文标题**: Show HN: MCP Defender – OSS AI Firewall for Protecting MCP in Cursor/Claude etc

**原文链接**: [https://mcpdefender.com](https://mcpdefender.com)

MCP Defender：保护人工智能应用的安全防火墙

---

## 39. GitHub上的语法索引与语法高亮

**原文标题**: Grammar Index, Syntax Highlighting on GitHub

**原文链接**: [https://github.com/github-linguist/linguist/blob/main/vendor/README.md](https://github.com/github-linguist/linguist/blob/main/vendor/README.md)

此代码片段描述了 GitHub 仓库 "linguist"，它由 "github-linguist" 拥有。该仓库是公开的，且与“语法索引，GitHub 上的语法高亮显示”相关。该仓库已被 fork 4.5 千次，并被标星 1.28 万次，表明其在 GitHub 社区中的受欢迎程度和潜在实用性。该代码片段还提到用户需要登录才能更改通知设置。本质上，它是一个有关处理语法和语法高亮显示功能的流行 GitHub 项目的描述。

---

## 40. 所有5x5 Nonogram

**原文标题**: Every 5x5 Nonogram

**原文链接**: [https://pixelogic.app/every-5x5-nonogram](https://pixelogic.app/every-5x5-nonogram)

文章“所有5x5 Nonogram”可能编录并分析了所有可能的独特5x5 Nonogram谜题。Nonogram，也称为Hanjie、Griddlers或Picross，是一种逻辑谜题，其中网格中的单元格必须根据网格侧面的数字进行着色或留空，以显示隐藏的图片。这些数字表示每行和每列中连续填充单元格块的长度。

这篇文章的主要目的可能是提供一个全面的5x5 Nonogram集合。鉴于网格尺寸相对较小，枚举所有可能的解决方案在计算上是可行的。这篇文章可能会根据难度、对称性或它们产生的图像对这些谜题进行分类。它还可以探讨存在的唯一解的数量以及如何以算法方式生成它们。这篇文章还可能讨论解决5x5 Nonogram的挑战、常用的技巧，并可能为列出的一些谜题提供示例解决方案。完整列出所有可能的5x5 Nonogram对于拼图爱好者和对这些逻辑拼图的属性感兴趣的研究人员来说将是一项宝贵的资源。上述复杂度分析和解决方案策略将进一步提高文章的教育价值。

---

## 41. J语言中的光线追踪

**原文标题**: Ray Tracing in J

**原文链接**: [https://idle.nprescott.com/2020/ray-tracing-in-j.html](https://idle.nprescott.com/2020/ray-tracing-in-j.html)

本文探讨了作者使用J编程语言编写一个极简光线追踪器的经验。作者强调了J语言的简洁性和面向数组的范式，并认为虽然该语言的语法起初可能看似令人生畏，但随着人们逐渐理解其函数式、基于数组的方法，语法障碍会逐渐减少。

作者解释了J语言的隐式编程（没有显式参数的函数），特别是重点介绍了“叉”——一种包含三个动词的序列。他们用定义“平均值”的例子来说明这一点。光线追踪器中使用的几个实用动词，如`magnitude`、`normalize`和`toRGB`，都以隐式风格定义，展示了该语言的表达能力。

文章描述了光线追踪器如何处理反射、碰撞（识别最近的交点），并对`intersect`和`lighting`等更复杂的函数使用显式动词定义。通过`trace`动词，解释了渲染过程，包括设置场景和计算光照。还讨论了“画布”的坐标数组的创建。

最后，文章提到了用于输出渲染图像的`writePPM`动词，并说明了该实现的局限性（没有多个对象或球体变换）。作者最后赞扬了J语言的交互式开发环境、其精心设计的特性以及令人惊讶的速度，甚至与类似的Common Lisp实现相比也是如此。

---

## 42. Valkey一周岁：Redis的社区分支

**原文标题**: Valkey Turns One: Community fork of Redis

**原文链接**: [https://www.gomomento.com/blog/valkey-turns-one-how-the-community-fork-left-redis-in-the-dust/](https://www.gomomento.com/blog/valkey-turns-one-how-the-community-fork-left-redis-in-the-dust/)

本文庆祝 Valkey 一周年。Valkey 是 Redis 公司决定将其数据库闭源后出现的一个社区分支。作者强调了 Valkey 令人惊讶的成功，表明它不仅存活了下来，而且在基准测试中优于 Redis 8.0。

文章详细介绍了 Valkey 8.1.1 和 Redis 8.0 在 AWS c8g.2xl 实例上的性能比较，重点关注 SET 和 GET 操作的吞吐量和延迟。Valkey 实现了明显更高的吞吐量和更低的延迟，尤其是在优化 I/O 线程并将 IRQ 固定到特定内核之后。Valkey 在优化配置下，SET 操作几乎达到了 1M RPS。

作者强调了 I/O 线程对性能提升的重要性，并指出 Valkey 的异步 I/O 线程模型的贡献解锁了显著更好的性能。他还强调需要进行仔细的调整，包括优化连接数、键空间大小和核心绑定，以实现最佳结果。文章提供了在 AWS 上使用 c8g 实例和 EC2 置放群组重现基准测试的具体说明。

虽然作者承认基准测试本身存在不精确性，但他鼓励 Valkey 和 Redis 社区继续追求性能改进。结论强调，性能是一项持续的实践，需要各个领域的专业知识。

---

## 43. 将Excel复制为Markdown表格 (反之亦然)

**原文标题**: Copy Excel to Markdown Table (and vice versa)

**原文链接**: [https://thisdavej.com/copy-table-in-excel-and-paste-as-a-markdown-table/](https://thisdavej.com/copy-table-in-excel-and-paste-as-a-markdown-table/)

thisdavej.com的文章“Excel表格与Markdown表格互转”提供了一种简便的方法，用于在Excel和Markdown格式之间转换表格数据，这是文档编写和在线内容创建中的常见任务。

核心思想是利用管道分隔值（PSV）格式作为中间格式。由于Markdown表格本质上是带有包含连字符的标题行的PSV，因此文章概述了一个将Excel数据快速转换为Markdown兼容PSV的过程。

作者建议以下步骤：

1. **从Excel复制数据。**
2. **将数据粘贴到文本编辑器（如记事本或VS Code）中。** 这会将数据粘贴为制表符分隔值（TSV）。
3. **将所有制表符替换为竖线（|）。** 这可以使用大多数文本编辑器中的“查找和替换”功能快速完成。
4. **在每行的开头和结尾添加竖线。** 这确保了表格结构正确。
5. **在标题行下添加标题分隔线（使用连字符）。** 作者建议手动输入类似`|---|---|---|`的行，以匹配列数。像TextExpander这样的工具可以自动化此过程。

文章还简要提到了反向过程（Markdown到Excel），即将Markdown表格复制到文本编辑器中，将竖线替换为制表符，然后将TSV数据复制并粘贴到Excel中。

本质上，本文提供了一种实用且高效的方法，使用简单的文本操作技术在Excel和Markdown表格之间进行转换，重点是使用“查找和替换”进行手动但直接的转换。

---

## 44. 网页开发仍然可以很有趣，如果你想让它有趣的话。

**原文标题**: Web dev is still fun if you want it to be

**原文链接**: [https://github.com/jchester/bobotw](https://github.com/jchester/bobotw)

作者反思了对现代Web开发的复杂性和官僚主义的幻灭，因此创建了一个简单的排名系统（“最差中的最佳”）作为个人项目。他们有意采用了较旧、较简单的技术（Sinatra、Sequel、SQLite）来重拾早期Web开发的乐趣。

这种刻意的简化包括服务器端渲染、基本的HTML表单和Ruby代码，这都得益于现代计算机的强大处理能力。作者避免了像Rails这样的复杂框架，甚至HTMX，而是选择了一种轻量级的方法。即使与Java相比，由于部署复杂性，SQL和Ruby分别因其强大和熟悉性而更受青睐。

AI辅助被谨慎地用于CSS和初步草稿，但最终需要大量的人工干预。作者做出了几个务实的决定来最大限度地减少复杂性：将标签颜色内联存储，从数据库ID派生图像名称，并实施一个简单的cookie方案来防止重复投票。他们还使用了Phlex进行模板化，在实用性与一丝现代过度工程（如UUIDv7用于cookie）之间取得了平衡。

该项目优先考虑简单性和速度，而不是可扩展性和复杂性，从而产生了一个快速高效的网站。部署就像rsync到VPS并重启进程一样简单。作者总结说，当剥离不必要的复杂性时，Web开发仍然可以令人愉快，并鼓励其他人在简单的编码中找到乐趣。

---

## 45. 硅谷终于又迎来了一家大型电子产品零售商：Micro Center 开业

**原文标题**: Silicon Valley finally has a big electronics retailer again: Micro Center opens

**原文链接**: [https://www.microcenter.com/site/mc-news/article/micro-center-santa-clara-photos.aspx](https://www.microcenter.com/site/mc-news/article/micro-center-santa-clara-photos.aspx)

Micro Center 在圣克拉拉开设了其在硅谷的首家门店，标志着它在阔别多年后重返该地区。2025年5月30日的盛大开业吸引了众多科技爱好者，他们渴望体验该门店的产品。Micro Center 旨在通过其广泛的组件选择、知识渊博的员工和亲身体验的购物方式，来满足 PC 组装者、游戏玩家、创作者和科技爱好者的需求。

该门店备有 CPU、GPU（包括 4000 多张显卡）和 3D 打印机。盛大开业促销活动包括 Windows 台式机、笔记本电脑和显示器的折扣。

这篇文章还重点介绍了一款特殊的、由 NVIDIA 首席执行官签名的镀金 Asus Astral RTX 5090 Dhahab Edition GPU，该 GPU 将在商店展出，之后将被拍卖以用于慈善事业。其他内容包括关于本地 LLM、人工智能代理、人工智能视频克隆、Raspberry Pi 和 3D 打印的 Mac Mini 外壳的文章。该页面还展示了流行的 PC 组件，例如 NVIDIA GeForce RTX 5090 系列显卡和 Ryzen 7 7700X 处理器，以及一台多色 3D 打印机。

---

## 46. 实现 Forth

**原文标题**: Implementing a Forth

**原文链接**: [https://ratfactor.com/forth/implementing](https://ratfactor.com/forth/implementing)

本文鼓励有兴趣创建自己的Forth实现的读者，并提供入门指南。它承认其中涉及的挑战和不确定性，并提供了三种主要方法：移植现有的Forth、构建一个超小型Forth核心，或者围绕一个特定的、小型目标程序设计Forth。

移植，如作者的NasmJF（JonesForth的移植版）所例证的那样，允许利用现有的Forth代码来学习语言实现。创建一个最小的Forth核心涉及定义引导语言其余部分所需的最少数量的字，例如PlanckForth、SmithForth、sectorforth、milliForth、StoneKnifeForth和一个3指令的Forth。第三种方法侧重于创建专门为运行一个非常简单的目标程序而定制的Forth，如作者的Meow5和Snobol4th项目所示。

本文重点介绍了JonesForth源代码、Brad Rodriguez的“Moving Forth”系列、一个关于构建迷你Forth的教程以及R.G. Loeliger的《Threaded Interpretive Languages》等资源。核心信息是拥抱挑战，在实践中学习，并为Forth项目定义一个清晰、可实现的目标。

---

## 47. 人工智能浪潮以来，YC公司行之有效的策略

**原文标题**: What's working for YC companies since the AI boom

**原文链接**: [https://jamesin.substack.com/p/whats-working-for-yc-companies-since](https://jamesin.substack.com/p/whats-working-for-yc-companies-since)

无法访问文章链接。

---

## 48. 射电天文学软件无线电

**原文标题**: Radio Astronomy Software Defined Radio (Rasdr)

**原文链接**: [https://radio-astronomy.org/rasdr](https://radio-astronomy.org/rasdr)

本文介绍了射电天文学软件无线电(RASDR)的概念，该概念强调射电天文SDR的宽带宽、Windows兼容性和详尽的文档。文中重点指出，基于该概念开发了两种硬件接收机设计。但是，目前只有其中一种设计，即RASDR4，正在销售。这意味着RASDR4是RASDR硬件的活跃且可用的迭代版本。

---

## 49. 亚当·里斯与哈勃张力

**原文标题**: Adam Riess and the Hubble tension

**原文链接**: [https://www.theatlantic.com/science/archive/2025/05/adam-riess-hubble-tension/682980/](https://www.theatlantic.com/science/archive/2025/05/adam-riess-hubble-tension/682980/)

本文聚焦于诺贝尔物理学奖得主亚当·里斯以及挑战宇宙学标准模型的“哈勃张力”，即日益增长的差异。里斯在发现暗能量和建立标准模型方面发挥了重要作用，但他现在认为该理论可能存在缺陷。

核心问题在于宇宙膨胀速度的不同测量结果。里斯的团队使用对遥远星系的精确测量来确定当前的膨胀速度，而其他人则通过推断大爆炸的余辉，依赖于标准模型的假设。这两种方法产生不同的结果，从而造成了哈勃张力。

里斯怀疑这种张力表明标准模型存在根本性错误，特别是暗能量的本质。他受到了一些宇宙学家的抵制，他们认为随着更多数据的出现，这种张力将会消失。然而，里斯认为他的测量中已排除了系统性误差。

来自暗能量光谱仪（DESI）的最新数据表明，暗能量的强度可能随着时间的推移而减弱，这进一步挑战了标准模型关于恒定排斥力的假设。如果得到证实，这可能需要彻底修改我们对宇宙命运的理解，可能远离“热寂”的观念，并为替代场景打开大门。最终，来自新天文台的进一步观测将决定标准模型的命运以及我们对宇宙膨胀的理解。

---

## 50. 德布鲁因记法及其用途

**原文标题**: De Bruijn notation, and why it's useful

**原文链接**: [https://blueberrywren.dev/blog/debruijn-explanation/](https://blueberrywren.dev/blog/debruijn-explanation/)

本文介绍了De Bruijn记号（索引和层级）作为解决lambda演算中变量捕获问题的方案，该问题出现在β归约（函数应用）期间。

传统的命名变量在替换时可能导致意外捕获，需要复杂的重命名过程。De Bruijn索引使用自然数来表示变量，其中0表示最近的lambda绑定器，1表示倒数第二个，依此类推。这消除了替换过程中重命名的需要。关键规则是将替换项中的自由变量增加1，每跨越一个绑定器，并将被替换项中的自由变量减少1，以移除绑定器。

De Bruijn层级与之类似，但最小的数字指的是最近最少绑定的项。索引通常被认为“更有用”，因为它们更具局部性；层级需要知道项中的深度。索引简化了创建新绑定器，而层级简化了在绑定器下移动项。

本文还强调了另一个优点：简化了α等价性检查。在变量名上等价的项（α等价）在De Bruijn记号中变得结构相同，允许直接进行相等性比较。最后，本文列出了替代方法，并提供了一个链接，其中对几种方法进行了广泛的比较。

---

## 51. 席德·梅尔的海盗——深度剖析 (2017)

**原文标题**: Sid Meier's Pirates – In-depth (2017)

**原文链接**: [https://shot97retro.blogspot.com/2017/12/sid-meiers-pirates-in-depth-written.html](https://shot97retro.blogspot.com/2017/12/sid-meiers-pirates-in-depth-written.html)

这篇2017年的文章深入评测了1990年发布于Amiga平台的《席德·梅尔的海盗！》。作者表达了对这款游戏及其各种移植版和重制版的深爱，并强调Amiga版本尤为出色。文章突出了Amiga版本的独特之处，特别是其精美的画面以及围绕其调色板的争论，最终得出结论，认为它巧妙地运用技术来显示比通常允许的更多的颜色。

评测涵盖了游戏开放式的本质，它超越了简单的类型划分，允许玩家在受历史启发的背景下追求个人目标。文章详细介绍了可用的各种时期和场景，并赞扬了内容丰富的用户手册作为宝贵的资源。游戏玩法融合了动作、冒险和策略，提供了多样化的道路，例如私掠、寻宝、陆地围攻，甚至浪漫故事。

作者分享了与父亲一起玩游戏的个人轶事，以及它对他们地理知识的影响。他们还进一步讨论了《海盗！》所获得的荣誉，包括来自《电脑游戏世界》和《Amiga世界》的奖项。文章以作者强烈推荐这款游戏，尤其是Amiga版本作为结尾，将其列为他们有史以来最喜欢的游戏之一。作者甚至建议，由于其开放式结构和玩家驱动的叙事，《海盗！》应该被归类为真正的“冒险”体验。文章还提供了视频评测的链接，包括作者本人和一个朋友的评测。

---

## 52. 杰瑞·刘易斯的《小丑之日》在瑞典发现，时隔53年。

**原文标题**: Jerry Lewis's “The Day the Clown Cried” discovered in Sweden after 53 years

**原文链接**: [https://www.thenationalnews.com/arts-culture/film-tv/2025/05/29/jerry-lewis-day-the-clown-cried-discovered/](https://www.thenationalnews.com/arts-culture/film-tv/2025/05/29/jerry-lewis-day-the-clown-cried-discovered/)

杰瑞·刘易斯尘封53年的争议电影《小丑之日》现身瑞典。瑞典演员汉斯·克里斯平声称于1980年盗取了一份完整的工作样片，并一直在私下放映。

克里斯平最近为记者放映了该片，以证明其存在。他还拥有丢失的开场片段，于1990年匿名收到。《小丑之日》讲述了一个被囚禁在纳粹集中营的小丑被迫引诱儿童走向死亡的故事。

克里斯平计划让全世界都能看到这部电影，建议对其进行修复和研究。刘易斯本人于2015年向国会图书馆捐赠了部分片段，将于2024年6月发布，但那些片段并非完整电影。

该电影被搁置的原因归咎于刘易斯与制片人之间关于融资的问题。刘易斯对这部电影的情感复杂，有时希望它能被看到，有时又对其质量感到尴尬。哈里·希勒将这部电影描述为“完美的物体”，因为它存在着严重错位的悲情和喜剧元素。

文章还讨论了其他被认为丢失后又被重新发现的电影，或因其他情况而丢失的电影，例如《风之棋》、《圣女贞德受难记》和被毁坏的《午夜之后伦敦》，以及像《蝙蝠女》这样被有意搁置的电影。

---

## 53. 如何在Postgres中运行定时任务而无需额外基础设施

**原文标题**: How to run cron jobs in Postgres without extra infrastructure

**原文链接**: [https://wasp.sh/blog/2025/05/28/how-to-run-cron-jobs-in-postgress-without-extra-infrastructure](https://wasp.sh/blog/2025/05/28/how-to-run-cron-jobs-in-postgress-without-extra-infrastructure)

本文演示了如何使用PgBoss（一个基于PostgreSQL构建的作业队列）在Wasp（React & Node.js）应用程序中实现调度，无需额外基础设施。

PgBoss利用Postgres的可靠性和可扩展性来管理后台作业，具有事务安全性、重试、超时和调度等功能。 Wasp通过提供声明式作业定义、自动worker设置和类型安全进一步简化了这一点。

本文概述了两种用例：一次性调度作业（使用`delay()`）和重复（CRON）作业，并使用一个网球比分示例应用程序。 它展示了如何调度作业，以在特定时间或使用cron表达式每天发送网球比赛的电子邮件摘要。

本文解释说，对于每天少于1000个作业和轻量级操作的简单副项目和初创公司来说，这种设置是理想的。 但是，对于耗时超过几秒钟、每天处理数千个作业或涉及大量计算的作业，建议使用专用的作业处理系统，以避免影响主应用程序的性能。 它强调从简单的解决方案开始，仅在有具体证据证明其合理时才进行升级。 关键在于，使用Wasp和PgBoss，调度任务可以非常简单，并且不一定需要复杂的基础设施。

---

## 54. Show HN: 智能静音 – 提醒你的 iPhone 在安静场所保持安静

**原文标题**: Show HN: Smart Silence – Remind your iPhone to stay quiet in quiet places

**原文链接**: [https://testflight.apple.com/join/47CJ31VK](https://testflight.apple.com/join/47CJ31VK)

本文档提供了一个全面的指南，指导如何使用 TestFlight 对 iOS、iPadOS、macOS、tvOS 和 visionOS 应用程序和 App Clips 进行 Beta 测试。它概述了接受邀请（通过电子邮件或公开链接）、安装 TestFlight 和 Beta 版应用程序以及向开发者提供反馈的过程。

主要涵盖的方面包括：

*   **

---

## 55. Show HN: W++ – 一款支持 NuGet 的 .NET 平台 Python 风格脚本语言

**原文标题**: Show HN: W++ – A Python-style scripting language for .NET with NuGet support

**原文链接**: [https://github.com/sinisterMage/WPlusPlus](https://github.com/sinisterMage/WPlusPlus)

W++ 是一种新的实验性脚本语言，用于 .NET 框架。它受 Python 的语法和可读性启发，但并非 Python 方言。由 Ofek Bickel 创建，作为一项教育项目，它具有用 C# 编写的完整的分词器、解析器和解释器，并支持 async/await、lambda 表达式、控制流、try/catch 以及用于语法高亮和代码片段的自定义 VSCode 扩展。

主要特点包括：

* 与 .NET 生态系统和 NuGet 包集成。
* 自定义语法、运行时和执行模型。
* 一种独特的“OOPSIE”（面向对象编程有时并不优秀）面向对象原则方法。

虽然其语法与 Python 相似，但 W++ 是一种独特的语言，可编译为 IL，专为 .NET 脚本编写而设计。该项目的 VSCode 扩展已被神秘地从 VSCode 市场中移除，该扩展的下载量超过 33,000 次。创建者愿意解决导致下架的任何问题，并寻求恢复。该项目在 MIT 许可下开源。

---

## 56. 三角形泼溅：用三角形表示的辐射场

**原文标题**: Triangle splatting: radiance fields represented by triangles

**原文链接**: [https://trianglesplatting.github.io/](https://trianglesplatting.github.io/)

三角片渲染：一种基于可微三角片的新型辐射场渲染方法

---

## 57. Show HN: Asdf Overlay – Windows 下的高性能游戏内覆盖层库

**原文标题**: Show HN: Asdf Overlay – High performance in-game overlay library for Windows

**原文链接**: [https://github.com/storycraft/asdf-overlay](https://github.com/storycraft/asdf-overlay)

Asdf Overlay 是一款高性能、易于使用的 Windows 叠加层库，它通过挂钩渲染后端，允许开发者在窗口帧缓冲区之上进行绘制。 它利用 GPU 共享纹理来避免 CPU 密集型的帧缓冲区复制，从而能够在不损失性能的情况下进行任意尺寸的叠加层渲染。

主要特性包括支持多种渲染 API (OpenGL, DX9, DX10, DX11, DX12 和 Vulkan)、GPU 加速的共享叠加层表面以及输入捕获控制。它被用于 Alspotron、Tosu 和游戏内歌词叠加层等项目中。

该库需要 node、pnpm、nightly rustc、cargo 和 MSVC。安装包括设置 Rust targets 和使用 pnpm 安装依赖项并构建项目。文档警告说，DLL 和客户端必须使用相同的 Rust 编译器构建，以避免出现问题。

示例位于 `examples` 目录中，演示了 Node.js 和 Rust 的用法。其中一个示例展示了通过 Left Shift + A 激活的游戏内浏览器叠加层，而其他示例则展示了故障方块和输入捕获功能。调试可以通过使用 DebugView 等外部工具查看的跟踪日志来完成。

该项目采用 MIT 或 Apache-2.0 双重许可。

---

## 58. 原子性和并发

**原文标题**: Atomics and Concurrency

**原文链接**: [https://redixhumayun.github.io/systems/2024/01/03/atomics-and-concurrency.html](https://redixhumayun.github.io/systems/2024/01/03/atomics-and-concurrency.html)

C++原子操作与内存排序：一种高性能并发替代方案

---

## 59. Anthropic 为 Claude 推出语音模式。

**原文标题**: Anthropic launches a voice mode for Claude

**原文链接**: [https://techcrunch.com/2025/05/27/anthropic-launches-a-voice-mode-for-claude/](https://techcrunch.com/2025/05/27/anthropic-launches-a-voice-mode-for-claude/)

Anthropic为其Claude聊天机器人应用推出语音模式，目前为测试版，并将在未来几周内以英语推出。该功能允许用户与Claude进行语音对话，默认使用Claude Sonnet 4模型。当Claude说话时，屏幕上会显示要点，从而实现免提交互。

语音模式允许用户讨论文档和图像，从五种语音选项中选择，并无缝切换文本和语音。对话将在互动后被转录和总结。免费用户在使用量上有上限，付费订阅者则可以使用Google Workspace连接器访问Google日历和Gmail（Google Docs集成仅适用于企业计划）。

此次发布之前，Anthropic首席产品官Mike Krieger确认了语音功能的开发，并探讨了与亚马逊和ElevenLabs的潜在合作。这些讨论的具体结果仍不清楚。

该声明恰逢在加利福尼亚州伯克利举行的TechCrunch Sessions: AI，该活动将于6月5日举行，届时将有来自OpenAI、Anthropic等公司的领导人参加。文章还包括对该活动和相关的AI知识挑战的宣传。

---

## 60. 识别未标记的铁

**原文标题**: Identifying Unmarked Iron

**原文链接**: [https://www.castironcollector.com/unmarked.php](https://www.castironcollector.com/unmarked.php)

鉴别无标记铸铁炊具指南

---

## 61. 微笑的公眾人物

**原文标题**: A Smiling Public Man

**原文链接**: [https://salmagundi.skidmore.edu/articles/1407-a-smiling-public-man](https://salmagundi.skidmore.edu/articles/1407-a-smiling-public-man)

杰弗里·迈耶斯《一位笑容可掬的公众人物》评述了谢默斯·希尼的书信，提供了对这位诗人生活、作品和人际关系的深刻见解。该评论重点介绍了希尼早期的职业生涯，他在伯克利和哈佛的教学经历，以及他与泰德·休斯、切斯瓦夫·米沃什和埃德娜·奥勃良等文学人物的友谊。

文章探讨了希尼与名誉和公共生活的复杂关系。虽然他珍视自己的隐私和创作所需的孤独，但他同时也广泛地参与文学界，参加会议、给出推荐信并接受荣誉。这种不断的旅行和公众曝光与他对创作空间的需求相冲突。

迈耶斯深入研究了希尼的艺术影响，特别是西奥多·罗特克，以及他对艺术家在社会中角色的看法，这反映在他的索福克勒斯《菲罗克忒忒斯》的翻译中。该评论还涉及希尼的个人生活，包括他的婚姻、信仰的丧失以及他偶尔与内疚的斗争。

总而言之，这篇文章将希尼描绘成一个慷慨而敏感的人，他深深地致力于他的朋友和他的事业，但也因他的公众形象以及由此产生的嫉妒而感到负担。他的信件揭示了一个复杂的人物，他需要在孤独和创作空间的需求与名誉的诱惑和义务之间取得平衡。

---

## 62. 你的样本量应该多大？

**原文标题**: How large should your sample size be?

**原文链接**: [https://vickiboykis.com/2015/08/04/how-large-should-your-sample-size-be/](https://vickiboykis.com/2015/08/04/how-large-should-your-sample-size-be/)

本文探讨了处理大型数据集时，样本量应如何选择的问题，尤其是在像R这样可能难以处理超大型数据集的环境中分析数据时。文章的出发点是，许多“大数据”问题可以通过精心选择的样本来解决。

作者以一家名为Goatly的初创公司为例，该公司向山羊养殖场销售药品箱。数据科学家需要预测农场流失率，但由于数据量庞大，无法对整个10万农场的数据库进行回归分析。

文章随后解释了决定样本量的因素：总体规模、误差幅度（置信区间）和置信水平。文章详细说明了如何选择合适的置信水平和误差幅度，并指出商业环境通常使用95%的置信水平。

作者随后提供了一个Python脚本和一个网站，用于计算样本量。基于Goatly的总体规模、95%的置信水平和2%的误差幅度，计算结果显示样本量约为2345个农场。文章总结说，这个更小、更具代表性的样本可以更快地进行分析，并为首席执行官提供结果。最后，文章提到了“检验效力”，可以在获得样本量后进行计算。

---

## 63. Show HN: 增强功能的Git-Add–Interactive

**原文标题**: Show HN: Git-Add–Interactive with Enhancements

**原文链接**: [https://github.com/cwarden/git-add-interactive](https://github.com/cwarden/git-add-interactive)

这个 "Show HN" 帖子介绍了一个用 Go 语言实现的 Git `git add -i` 和 `git add -p` 交互式暂存工具，相比于原来的 Perl 脚本，功能更强大。它提供了相同的核心功能，如交互式文件和代码块选择、带有常用命令 (y/n/s/e/q/a/d) 的补丁模式，以及用于颜色配置和仓库支持的 Git 集成。

这个 Go 版本拥有几个显著的改进：**全局过滤 (G)** 允许用户基于正则表达式模式过滤所有文件中的代码块，从而可以轻松地专注于特定的代码更改。**自动拆分 (S)** 自动将代码块拆分为尽可能小的块，以实现精细控制。**全部接受 (A)** 命令在过滤和拆分后暂存所有剩余可见的代码块，从而简化了工作流程。

其他增强功能包括文件内的本地搜索、显示过滤和自动拆分状态的状态显示，以及跨文件的持久性全局过滤器。

安装过程包括使用 `go build .` 构建二进制文件，并可以选择通过将其移动到 Go bin 目录并更新 `GIT_EXEC_PATH` 来将其安装为默认的 Git 命令。 该帖子详细介绍了如何直接使用该工具或作为 Git 命令使用，涵盖了各种补丁模式和可用命令。 它还概述了架构、测试程序以及与现有 Git 功能的兼容性。 最后，它提供了卸载并恢复到原始 Perl 实现的说明。

---

## 64. 语言建模分词：BPE vs. Unigram语言模型 (2020)

**原文标题**: Tokenization for language modeling: BPE vs. Unigram Language Modeling (2020)

**原文链接**: [https://ndingwall.github.io/blog/tokenization](https://ndingwall.github.io/blog/tokenization)

本文探讨了语言模型中使用的分词方法，特别是比较了字节对编码（BPE）和Unigram语言模型（Unigram LM）。文章认为，尽管BPE很流行（在BERT和GPT-2等模型中使用），但它经常产生模糊单词形态关系的tokenization，可能阻碍学习。文章举例说明了BPE如何误解前缀和后缀。

文章重点介绍了Bostrom和Durrett的研究，他们发现用Unigram LM代替BPE可以更好地保留形态学，并提高下游任务的性能。Unigram LM更频繁地识别常见后缀和前缀，从而产生更好地反映单词结构的分词。

作者重复了这些发现，在维基百科数据上训练了BPE和Unigram LM分词器，并证明Unigram LM正确处理了诸如“destabilizing”之类的单词，通过识别“de-”作为前缀。为了定量评估分词器，作者将其与Merriam-Webster的发音指南进行了比较，发现Unigram LM产生了更多“形态学上合理”的子词。

文章结论是，对于语言模型而言，Unigram LM提供了一种更优越的分词方法。虽然Unigram LM学习需要稍长的时间，但推理速度相当。作者提出了未来的研究方向，包括探索将结构语言学知识（例如，解析树）直接整合到模型架构中的方法。

---

## 65. 基数2^51技巧 (2017)

**原文标题**: The radix 2^51 trick (2017)

**原文链接**: [https://www.chosenplaintext.ca/articles/radix-2-51-trick.html](https://www.chosenplaintext.ca/articles/radix-2-51-trick.html)

文章“基数2^51技巧”解释了一种通过优化进位处理来加速现代CPU上大整数加减运算的技术。传统的“带进位加法”（adc）指令虽然准确，但由于其串行执行以及`adc`未经过高度优化，因此比普通加法（`add`）指令慢。它还阻碍了现代处理器上的并行性。

其核心思想是延迟进位传播。作者建议使用“基数2^51表示法”，而不是直接使用基数2^64（其中每个64位片段代表一个数字）。这涉及将一个大数（例如256位）拆分为更多但更小的“数字”（五个51位或52位肢）。减少后的基数在每个肢中提供“额外的数字”来临时存储加法期间产生的进位，避免立即传播。这允许并行使用更快的`add`指令。

经过多次加法后，一个单独的归一化步骤会传播累积的进位。作者指出，即使考虑到与基数2^51之间相互转换的开销，这种方法在仅经过几次加法后也可能更快。通过将肢视为有符号整数来处理负进位，该概念可以扩展到减法。总之，该技术以寄存器使用量和运算次数为代价，换取了更高的并行性，从而提高了性能。

---

## 66. 玛莎百货何时再次接受在线订单？

**原文标题**: When will M&S take online orders again?

**原文链接**: [https://moneyweek.com/personal-finance/marks-and-spencer-online-order-problems](https://moneyweek.com/personal-finance/marks-and-spencer-online-order-problems)

以下是文章的简要概述：

由于网络攻击，玛莎百货（M&S）的在线服务自2025年4月25日起中断，预计要到7月才能完全恢复。这次攻击预计将导致玛莎百货在2025/26财年的营业利润损失3亿英镑。

虽然客户可以浏览网站并填写购物车，但无法完成购买。此次攻击泄露了一些客户数据，包括联系方式、出生日期和订单历史记录，但玛莎百货保证支付信息和密码未被盗。建议客户警惕潜在的网络钓鱼攻击并重置密码。

该公司已向部分受影响的客户提供礼品卡作为补偿。专家指出，此次中断可能导致直接和间接损失。尽管发生了这起事件，分析师们对玛莎百货的整体表现仍然持乐观态度，并指出食品部门的强劲增长及其正在进行的转型努力。"DragonForce"组织声称对此次攻击负责，该攻击涉及勒索软件。玛莎百货正专注于恢复和加强防御。

---

## 67. Cerebras 在 Llama 4 Maverick (400B) 上实现 2,500T/s

**原文标题**: Cerebras achieves 2,500T/s on Llama 4 Maverick (400B)

**原文链接**: [https://www.cerebras.ai/press-release/maverick](https://www.cerebras.ai/press-release/maverick)

Cerebras 宣布 LLM 推理速度创下新世界纪录，在 Meta 的 Llama 4 Maverick (400B) 模型上，每个用户实现了每秒超过 2,500 个 tokens (TPS)。这超越了 NVIDIA 的 Blackwell GPU 的性能，后者在同一模型上演示了大约 1,000 TPS 每用户。该基准测试由独立公司 Artificial Analysis 进行。

据 Artificial Analysis 称，Cerebras 是唯一在 Meta 的旗舰模型上优于 Blackwell 的推理解决方案。他们测试了其他供应商，如 SambaNova、Amazon、Groq、Google 和 Microsoft Azure，所有这些供应商的 TPS 都显著降低。

Cerebras 首席执行官 Andrew Feldman 强调，该公司卓越的推理速度对于企业 AI 应用至关重要，例如代理、代码生成和复杂推理，在这些应用中，延迟是一个重要的瓶颈。他还强调了 Cerebras 硬件和 API 的可用性，并将其与 NVIDIA 的定制软件优化形成对比，NVIDIA 的定制软件优化大多数用户无法轻易获得。Cerebras 声称其性能是在没有特殊内核优化的情况下实现的，并且可以通过 Meta 的 API 服务访问。

文章强调了速度在 AI 应用中的重要性，尤其是在用户体验和竞争优势方面，并引用了 Google 关于搜索速度的研究结果。Cerebras 将自己定位为 Llama 4 部署的最佳解决方案，为开发者和企业 AI 用户提供更快的推理。

---

## 68. Show HN: 用 Bash 编写的 MCP 服务器 SDK

**原文标题**: Show HN: MCP Server SDK in Bash

**原文链接**: [https://github.com/muthuishere/mcp-server-bash-sdk](https://github.com/muthuishere/mcp-server-bash-sdk)

这个“Show HN”帖子介绍了一个纯 Bash 实现的 MCP（模型上下文协议）服务器 SDK，为 Node.js 或 Python 等较重的运行时环境提供了一个轻量级的替代方案。作者认为许多 MCP 服务器仅仅是 API 封装器，而这个 Bash 实现提供了一个零开销的解决方案。

主要特性包括：通过标准输入/输出（stdio）完全支持 JSON-RPC 2.0 协议，完整的 MCP 协议实现，基于函数命名的动态工具发现，通过 JSON 文件进行外部配置，以及易于使用自定义工具进行扩展。它需要 Bash 和 `jq` 来处理 JSON。

架构包括一个通过 stdio 与基于 Bash 的 MCP 服务器（`moviemcpserver.sh`）交互的 MCP 主机（AI 系统）。服务器核心（`mcpserver_core.sh`）处理协议层，而业务逻辑在工具函数中实现。配置从 JSON 文件加载。

该帖子提供了创建自定义工具的指南，强调了特定的命名约定（`tool_*`），使用 JSON 的参数处理以及定义的成功/错误模式。提供了一个完整的示例，构建了一个“weatherserver.sh”，并附带配置和工具 JSON 文件。还提供了将服务器与 VS Code 和 GitHub Copilot 集成的说明。

最后，该帖子承认了局限性，例如缺乏并发性、有限的内存管理、没有流式响应以及不适用于高吞吐量场景，但认为这些对于 AI 助手和本地工具执行来说是可以接受的权衡。该项目采用 MIT 许可证。

---

## 69. 已知最古老的鲸骨工具可追溯到两万年前

**原文标题**: Oldest known tools made from whale bones dated to 20k years ago

**原文链接**: [https://apnews.com/article/oldest-whale-bone-tools-e5ce1ae2e692b2b4f7b60ea423bacf15](https://apnews.com/article/oldest-whale-bone-tools-e5ce1ae2e692b2b4f7b60ea423bacf15)

以下是基于标题和可能内容的文章摘要：

文章报道了已知最古老的鲸骨工具的发现和年代测定。这些工具在一个特定的考古遗址（可能在亚洲）被发现，估计有大约两万年的历史。这一发现将鲸骨作为工具生产材料的已知时间线向前推进。这项发现的意义在于为晚更新世时期古代人类的足智多谋和适应能力提供了新的见解，表明利用海洋资源的先进狩猎和加工技术比以前认为的更早存在。参与研究的研究人员可能使用了放射性碳定年法或类似方法来确定这些工具的年代。文章很可能会讨论发现的工具类型（例如，尖状器、锥子、刮削器）、它们的潜在用途（例如，狩猎、屠宰、皮革加工）以及对理解早期人类沿海适应和海洋哺乳动物在其生存中的重要性的影响。该发现可能会挑战关于人类沿海地区人口的时间和传播以及他们对海洋资源依赖的现有理论。

---

## 70. 美国制裁云服务商“Funnull”，因其为“杀猪盘”诈骗的主要来源

**原文标题**: U.S. sanctions cloud provider 'Funnull' as top source of 'pig butchering' scams

**原文链接**: [https://krebsonsecurity.com/2025/05/u-s-sanctions-cloud-provider-funnull-as-top-source-of-pig-butchering-scams/](https://krebsonsecurity.com/2025/05/u-s-sanctions-cloud-provider-funnull-as-top-source-of-pig-butchering-scams/)

美国财政部制裁了总部位于菲律宾的Funnull科技公司，该公司为“杀猪盘”加密货币投资诈骗提供基础设施，这些诈骗已使美国人损失超过2亿美元。 Funnull充当内容分发网络（CDN），通过位于美国的云提供商路由恶意流量，从而难以阻止。

Silent Push的研究表明，Funnull托管着宣传赌博网站的域名，这些网站与朝鲜黑客的洗钱活动有关。 美国联邦调查局证实，Funnull的基础设施被用于生成和映射域名到美国云提供商。

虽然亚马逊和微软承诺将Funnull从他们的网络中移除，但Silent Push发现亚马逊仍在托管Funnull服务器。 亚马逊声称正在积极打击滥用行为，并正在调查共享的信息。 该文章强调了由于存在阻止合法网站的风险，以及美国云网络为网络罪犯在地域上锁定受害者提供的优势，因此难以阻止来自美国云网络的流量。

该文章还提到欧盟对Stark Industries Solutions的制裁，该公司是一家与俄罗斯网络攻击和虚假信息宣传活动有关的ISP，该公司也通过美国云提供商路由流量。 尽管摩尔多瓦兄弟伊万和尤里·内库利蒂否认参与网络犯罪，但他们两位联合创始人也受到了制裁。 欧盟表示，Stark使俄罗斯国家支持的行为者能够进行破坏稳定的活动，并将他们隐藏在执法部门之外。

---

## 71. 关于动态语言中以及特别是Racket中的eval函数 (2011)

**原文标题**: On eval in dynamic languages generally and in Racket specifically (2011)

**原文链接**: [https://blog.racket-lang.org/2011/10/on-eval-in-dynamic-languages-generally.html](https://blog.racket-lang.org/2011/10/on-eval-in-dynamic-languages-generally.html)

Matthew Flatt的文章探讨了动态语言（特别是Racket）中`eval`的使用，强调了它的强大功能和潜在陷阱。 `Eval`允许程序动态执行代码，就像指示他人执行任务一样，但会给翻译、优化和程序理解带来复杂性。 作者将其比作用另一种语言指示某人，强调上下文非常重要。

虽然功能强大，但应避免不必要的`eval`使用，因为它使代码更难分析、理解和优化。 `Eval`的良好使用场景包括需要外部输入或将指令分发给其他实体的情况。 关键原则是，使用`eval`的程序员有责任确保被评估的代码在其预期上下文中是有意义的。

在Racket中，由于Racket的多语言特性，`eval`可能会特别棘手。 作者用一个例子说明了这一点，即由于不同的命名空间上下文，`eval`在模块内部和DrRacket的交互窗口中的行为不同。 Racket故意将`eval`默认为空的语言上下文，以迫使程序员考虑语言问题。 该文章强调了有效使用`eval`时需要了解Racket的命名空间工具。

Mike Samuel的评论强调了使语言可分析以确保安全性的重要性，主张限制嵌入式脚本语言的权限，并将`eval`视为一种可以沙盒化的语言嵌入形式。

---

## 72. 用 SQL 和 YAML 构建 API 集成 – 无需 SaaS 锁定，无需拖放式 UI

**原文标题**: Build API integrations with SQL and YAML – no SaaS lock-in, no drag-and-drop UIs

**原文链接**: [https://github.com/paloaltodatabases/sequor](https://github.com/paloaltodatabases/sequor)

Sequor 是一款以 SQL 为中心的 workflow 平台，旨在现代数据栈中构建可靠的 API 集成，为 SaaS 连接器提供了一种开放且可控的替代方案。它将 API 执行与您的数据库统一起来，促进双向数据流动，并支持强大的基于 SQL 的转换、分析和业务逻辑，从而消除了传统 iPaaS 风格集成和 ETL 管道之间的分离。

Sequor 采用代码优先方法，使用 YAML 进行 workflow 定义，Jinja/Python 用于动态参数，SQL 用于逻辑，从而促进软件工程的最佳实践，如版本控制和 CI/CD。集成流程使用诸如 `http_request` (用于 API 调用与数据库集成), `transform` (用于基于 SQL 的数据准备和处理) 和控制语句 (用于强大的错误处理和编排) 等操作构建。

本文档提供了使用 Sequor 进行数据采集（从 BigCommerce 等 API 将数据加载到数据库中）、反向 ETL（从数据库数据在 BigCommerce 等外部系统中创建对象）、复杂数据处理（映射嵌套数据）以及使用 SQL 进行数据转换和分析的示例。它还展示了如何使用条件语句来编排复杂的工作流程。

Sequor 强调集成的所有权、控制和可扩展性，而无需 SaaS 锁定。它使用熟悉的开放技术提供透明的配置。通过 `pip install sequor` 即可简化入门，然后提供快速入门指南和示例集成。可以通过 GitHub 讨论和新闻通讯获得支持和社区参与。

---

## 73. 滋养数十亿人的大气记忆：季风降雨机制

**原文标题**: The atmospheric memory that feeds billions of people: Monsoon rainfall mechanism

**原文链接**: [https://phys.org/news/2025-05-atmospheric-memory-billions-people-monsoon.html](https://phys.org/news/2025-05-atmospheric-memory-billions-people-monsoon.html)

波茨坦气候影响研究所的研究指出了一种新发现的“大气记忆”效应，该效应支配着季风降雨模式，影响着数十亿人。这项发表在《美国国家科学院院刊》上的研究表明，大气可以在较长时期内储存水分，从而形成一种物理记忆，使季风系统能够存在于两种稳定状态：湿和干。

传统上，季风降雨归因于对太阳辐射变化的直接反应。然而，这项研究表明，大气历史，特别是其水分含量，起着至关重要的作用。春季期间，大气积累水蒸气，决定季风降雨的开始。即使在秋季太阳辐射减少时，该储量也能维持降雨。这种“双稳态”意味着在相同水平的太阳辐射下，大气可以干燥或多雨，具体取决于其先前的状态。

研究人员使用观测数据和大气模拟，确定了一个大约35千克/平方米的水分阈值。超过此阈值会触发季风，而低于此阈值则会导致季风停止。这种突然的、基于阈值的响应定义了双稳态。由于污染或全球变暖，对这种动态的破坏可能会对依赖季风的印度、印度尼西亚、巴西和中国的人口造成严重后果。研究人员希望了解这个临界点将有助于开发早期预警系统。

---

## 74. 使 C 和 Python 互相通信

**原文标题**: Making C and Python Talk to Each Other

**原文链接**: [https://leetarxiv.substack.com/p/making-c-and-python-talk-to-each](https://leetarxiv.substack.com/p/making-c-and-python-talk-to-each)

无法访问文章链接。

---

## 75. “风盗”：困扰风电场的神秘效应

**原文标题**: 'Wind theft': The mysterious effect plaguing wind farms

**原文链接**: [https://www.bbc.com/future/article/20250506-renewable-energys-trouble-with-wind-theft](https://www.bbc.com/future/article/20250506-renewable-energys-trouble-with-wind-theft)

海上风电场“风能盗取”问题日益突出，本文对此展开讨论。风电场的风力涡轮机会产生“尾流效应”，降低下游风电场的风速和能源输出。这种尾流可延伸数十甚至超过一百公里，可能导致下游风电场能源产量降低10%或更多。

随着各国为实现净零目标而迅速扩张海上风能，该问题变得愈发紧迫，导致风电场密度越来越大，规模越来越大，尤其是在北海等地区。这种密度增加加剧了尾流效应，并可能导致开发商之间因能源输出减少而产生纠纷。法律专家指出，虽然风本身不能被拥有，但风能盗取的后果，例如投资可行性降低，是显著的。

本文强调需要通过研究和国际合作，更好地理解和管理尾流效应。英国一项研究项目正在对尾流影响进行建模，以改进规划。专家建议将风视为一种共享资源，并制定明确的法规，类似于石油或鱼类等共享海洋资源。他们还警告不要出现“逐水而居”的局面，即各国竞相开发风电场，而不充分考虑环境影响。最终，本文强调了通过合作解决风能盗取问题的重要性，以确保海上风能的成功和公平扩张，从而实现可持续的未来。

---

## 76. Fractran解释器

**原文标题**: Fractran Interpreter

**原文链接**: [https://tjwei.github.io/Fractran/](https://tjwei.github.io/Fractran/)

本文介绍了一个Fractran解释器。Fractran是由约翰·康威创建的一种深奥的、图灵完备的编程语言。

Fractran程序由一个正分数有序列表和一个初始正整数输入'n'组成。程序通过遍历分数列表来执行。在每个步骤中，它找到列表中*第一个*分数'f'，使得'n'和'f'的乘积(nf)是一个整数。然后，'n'通过将其替换为nf的整数结果来更新。

这个过程会重复进行，直到列表中没有分数乘以'n'时能得到一个整数。此时，程序停止。

该解释器似乎提供了诸如选择示例程序、编辑/查看代码、运行/暂停/重启执行、单步执行程序中的一条指令、调整执行速度、查看序列输出（特别是对于素数）以及显示错误列表等功能。它还提供了GitHub上源代码的链接以及来自Wikipedia的Fractran的简要说明。

---

## 77. FLUX.1 Kontext

**原文标题**: FLUX.1 Kontext

**原文链接**: [https://bfl.ai/models/flux-kontext](https://bfl.ai/models/flux-kontext)

FLUX.1 Kontext是来自黑森林实验室的一套新的生成式流动匹配模型，可实现文本和图像驱动的图像生成和编辑。与传统的文本到图像模型不同，FLUX.1 Kontext执行上下文图像生成，允许用户通过文本和图像进行提示，无缝提取和修改视觉概念，以产生新的、连贯的渲染效果。

其主要功能包括角色一致性，允许在多个场景中保留独特元素；局部编辑，用于进行有针对性的修改，而不影响图像的其余部分；风格参考，用于生成新颖场景，同时保留独特风格；以及交互速度，可在生成和编辑过程中实现最小延迟。

该套件包含三个模型：FLUX.1 Kontext [max]，高级模型，优先考虑最高性能、提示一致性和连贯性；FLUX.1 Kontext [pro]，统一模型，专注于快速、迭代的图像编辑，用于精确的区域编辑或完整场景转换；以及FLUX.1 Kontext [dev]，即将推出的开源权重、精简版本。FLUX.1 Kontext模型无需微调或复杂的工作流程即可实现灵活的图像编辑，允许用户逐步添加指令并逐步完善创作，同时保持图像质量和角色一致性。[max]和[pro]模型均提供演示和游乐场访问。

---

## 78. OpenBao 命名空间

**原文标题**: OpenBao Namespaces

**原文链接**: [https://openbao.org/blog/namespaces-announcement/](https://openbao.org/blog/namespaces-announcement/)

OpenBao引入命名空间：增强密钥管理中的多租户和隔离

OpenBao引入了命名空间，这是一项强大的功能，可以增强密钥管理中的多租户和隔离。命名空间是单个OpenBao实例中的逻辑分区，为团队和应用程序提供隔离的环境。每个命名空间都像一个迷你的OpenBao，拥有自己的策略、身份验证、密钥引擎和令牌。

主要优点包括：

*   **安全的多租户：** 隔离租户（团队、组织、应用程序）以防止未经授权的访问。
*   **委派管理：** 授权命名空间管理员独立管理其资源。
*   **可扩展性基础：** 通过启用命名空间和挂载点的延迟加载，成为水平可扩展性的垫脚石。

本文演示了命名空间的使用，通过CLI示例来创建、查找和扫描命名空间，以及在命名空间内启用和使用密钥引擎。它还涵盖了生命周期操作，如策略管理和移动/重命名引擎。

OpenBao 2.3 引入了此功能。用户可以探索命名空间并提供反馈。未来的增强功能包括命名空间密封、非分层命名空间、每个命名空间的存储后端和插件隔离，所有这些都旨在提高灵活性、效率和安全性。欢迎为OpenBao做出贡献。

---

## 79. 手写为何更有利于记忆和学习

**原文标题**: Why Writing by Hand Is Better for Memory and Learning

**原文链接**: [https://www.scientificamerican.com/article/why-writing-by-hand-is-better-for-memory-and-learning/](https://www.scientificamerican.com/article/why-writing-by-hand-is-better-for-memory-and-learning/)

本文认为，手写比打字更有利于记忆和学习，尤其对幼儿而言。最新的脑部活动监测研究表明，与打字相比，手写能激活大脑中负责运动、视觉、感觉处理和记忆的更多区域。

主要论点是手写需要更积极的认知参与。与可能成为被动转录过程的打字不同，手写迫使学生对信息进行优先排序、整合以及与现有知识联系。这种积极的处理方式可以加强参与度和理解力。形成字母的物理动作不同程度地激活了运动皮层，将运动动作与视觉和概念识别联系起来，从而增强记忆力。

专家强调了儿童手写课程的重要性，认为这些活动可以调动运动系统，提高字母识别能力，并有助于区分相似字母。虽然技术提供了效率和公平获取资源等好处，但过度依赖数字设备和“认知卸载”可能会降低大脑活动，并可能导致记忆和运动技能的退化。

因此，本文主张在早期儿童教育中融入手写和绘画活动，以刺激大脑发育并提高学习效果。

---

## 80. 机器人一体倒置3D打印，然后走出打印机。

**原文标题**: Robot is 3D-printed upside-down in one piece, then walks out of the printer

**原文链接**: [https://newatlas.com/robotics/3d-printed-soft-robot-walks/](https://newatlas.com/robotics/3d-printed-soft-robot-walks/)

爱丁堡大学科学家开发了一种用于单片3D打印软体机器人的新方法。其关键创新在于“Flex打印机”，这是一个由易于获得的组件构建的开源、低成本（约500美元）平台，可实现这些机器人的批量生产。

该机器人是一个小型四足动物，由柔性热塑性聚氨酯（TPU）制成。研究人员通过使用更宽的丝材并倒置打印机器人，克服了与打印TPU相关的挑战，如屈曲和下垂。这种倒置方法利用重力来帮助融合各层，从而确保结构完整性。

打印过程大约需要九个小时。完成后，机器人连接到一个气动环形振荡器，该振荡器提供脉冲式气压，依次触发腿部运动，使机器人能够“走”下打印床。这种气动运动消除了对传统电机的需求。

由此产生的机器人作为一个演示器，展示了软体机器人可访问和快速原型制作的潜力。研究人员认为，这项技术可以显著推进软体机器人领域，使其在勘探、医学以及搜索和救援等领域得到广泛应用。Flex打印机的开源性质旨在普及软体机器人的开发并促进创新。

---

## 81. OrioleDB中的桥接索引：架构、内部机制与日常使用？

**原文标题**: Bridged Indexes in OrioleDB: architecture, internals and everyday use?

**原文链接**: [https://www.orioledb.com/blog/orioledb-bridged-indexes](https://www.orioledb.com/blog/orioledb-bridged-indexes)

OrioleDB利用“桥接索引”来支持PostgreSQL在其MVCC感知、基于B树的存储上实现的各种索引访问方法（GIN、GiST等）。由于OrioleDB管理自己的行存储和MVCC，直接集成PostgreSQL现有的索引不可行。“桥接索引”通过在每个表中引入一个自动添加、递增的“索引指针”列（iptr）来解决这个问题。PostgreSQL索引构建在这些iptr值之上，而不是直接的行标识符。

“桥接索引”将iptr映射到主键。当查询使用桥接索引时，引擎执行一个三级查找：IndexAM索引 -> iptr -> 桥接索引 -> 主键获取。这种方法提供了完整的IndexAM兼容性。

通常，当在OrioleDB表上创建非B树索引时，桥接索引会自动创建。但是，可以手动控制桥接的预先创建或删除。

性能方面的考虑包括额外的查找跳跃的开销。对索引列的更新也会产生额外的成本，因为iptr的更改需要更新桥接索引和底层索引。

本质上，桥接索引在OrioleDB的架构和PostgreSQL广泛的索引生态系统的灵活性之间取得了平衡，从而可以使用各种索引类型，如GIN、GiST和pgvector的HNSW，而无需重写索引扩展。

---

## 82. Show HN：Onlook - 面向设计师的开源、可视化游标

**原文标题**: Show HN: Onlook – Open-source, visual-first Cursor for designers

**原文链接**: [https://github.com/onlook-dev/onlook](https://github.com/onlook-dev/onlook)

Onlook：面向设计师的开源可视化代码编辑器，作为Bolt.new和Webflow等工具的浏览器替代方案，借助AI辅助，主要使用Next.js和TailwindCSS，方便地创建网站、原型和设计。该工具允许在浏览器中直接编辑DOM，并进行实时协同设计。

主要功能包括：从文本、图像、模板、Figma导入或GitHub仓库创建Next.js应用，使用类似Figma的界面进行可视化应用编辑，实时预览应用，以及管理品牌资产。它还集成了实时代码编辑、检查点保存、CLI命令、应用市场连接以及通过可分享链接和自定义域名支持的快速应用部署。协作功能包括实时编辑和评论。

Onlook正从可下载的Electron应用（现命名为Onlook Desktop）过渡到基于Web的平台。该编辑器的工作方式是将代码加载到Web容器中，在iFrame中显示预览，索引代码，检测代码以将元素映射到代码位置，然后在用户交互时编辑iFrame和底层代码。AI聊天也具有代码访问权限，可实现智能编辑。该架构旨在潜在地支持各种语言和框架。

欢迎通过 Fork 代码仓库并创建 Pull Request 或打开 Issues 来进行贡献。该项目使用 Next.js、Supabase、Drizzle、TailwindCSS、Bun 和 tRPC 构建，并以 Apache 2.0 许可证授权。

---

## 83. 学习C3

**原文标题**: Learning C3

**原文链接**: [https://alloc.dev/2025/05/29/learning_c3](https://alloc.dev/2025/05/29/learning_c3)

本文记录了作者初次学习C3编程语言的经验。出于好奇，作者探索了C3的特性，并将其与其他语言（特别是C语言）进行了比较，强调了C3旨在以现代特性和优化为基础构建C语言。

作者研究了几个语言特性，从“Hello World”开始，逐步深入到`foreach`和`while`循环、枚举和`switch`语句、用于资源管理的`defer`关键字以及结构体类型等主题。文章深入探讨了C3的错误处理，使用带有故障定义的可选类型，以及用于前置和后置条件的契约式编程。结构体方法和宏也被涵盖，但作者对宏表达了一些保留意见。

主要收获包括C3相对于C的改进，例如`defer`关键字、点语法方法以及使用结构体内的匿名联合体对标记联合体的更简洁实现。作者还探索了C3的独特功能，例如switch语句中的`nextcase`关键字，允许实现Duff设备。虽然印象深刻，但作者对`switch`语句中的显式/隐式中断规则以及可选类型在可选值和错误处理中的组合使用提出了一些小担忧。文章最后总结了作者安装C3并开始计算器项目的计划。

---

## 84. Vrs：受Emacs、Plan 9、Erlang、超媒体启发的个人软件运行时

**原文标题**: Vrs: Personal Software Runtime inspired by Emacs, Plan 9, Erlang, Hypermedia

**原文链接**: [https://github.com/leoshimo/vrs](https://github.com/leoshimo/vrs)

Vrs 是一个个人编程运行时和软件平台，旨在带来愉悦的编程体验，其灵感来源于 Emacs、Erlang、Unix、Plan 9 和超媒体。它在 Recurse Center 构建，目前正处于积极开发阶段，不提供稳定性保证。

Vrs 使用 Lyric，一种定制的 Lisp 方言和虚拟机。 Lyric 支持函数定义、列表操作、关联列表、lambda 表达式、条件语句、模式匹配以及用于动态代码执行的 `eval` 等特性。

Vrs 中的软件作为轻量级进程（绿色线程）运行，通过非阻塞 I/O 在多个核心上调度。 进程是隔离的，并通过邮箱的消息传递进行通信。 服务是可以注册、发现并绑定到其他进程的长期运行的进程，从而实现进程间通信。 内置的发布/订阅机制支持基于全局主题的消息传递。

该文档提供了代码示例，包括一个计数器服务和一个用于 macOS 的系统外观（黑暗模式）服务。

Vrs 包含诸如 `vrsctl` 之类的工具，它是一个 CLI 客户端，用于交互式的 REPL 驱动的工作流程和调试，以及一个用于 Emacs 的 `lyric-mode`，提供语法高亮和以编辑器为中心的开发环境。

---

## 85. 人类程序员仍然优于大型语言模型。

**原文标题**: Human coders are still better than LLMs

**原文链接**: [https://antirez.com/news/153](https://antirez.com/news/153)

尽管大型语言模型在代码生成方面取得了进展，但本文认为人类程序员仍然更胜一筹。

---

## 86. 向量嵌入的可视化探索

**原文标题**: A visual exploration of vector embeddings

**原文链接**: [http://blog.pamelafox.org/2025/05/a-visual-exploration-of-vector.html](http://blog.pamelafox.org/2025/05/a-visual-exploration-of-vector.html)

Pamela Fox的博客文章以可视化的方式介绍了向量嵌入，解释了向量嵌入是什么以及如何使用它们。向量嵌入是将输入（词语、图像等）映射到浮点数列表的过程，在多维空间中表示输入。文章比较了不同的嵌入模型，包括word2vec、text-embedding-ada-002和text-embedding-3-small，突出了它们的特性、维度和相似度空间。文章探讨了余弦相似度和点积等相似度度量方法，解释了它们如何衡量向量的相关性，并指出点积对于单位向量来说速度更快。文章还简要讨论了欧几里得距离和曼哈顿距离等距离度量方法。

向量嵌入的核心应用是向量搜索，它可以找到语义上相似的项目，即使跨语言和跨模态也是如此。文章提到了从穷举搜索到近似最近邻（ANN）算法（如HNSW和IVFFlat）的过渡，以便用于大型数据库。

文章最后介绍了向量压缩技术：量化（标量和二元）和降维。量化通过将浮点数转换为整数或比特来减少每个向量所需的存储空间，而降维（在text-embedding-3-small等模型中可用）可以缩短向量长度。文章推荐了一种“压缩与重评分”方法：使用压缩向量进行索引，使用原始向量进行最终相似度检查。最后，文章提供了指向Jupyter笔记本和作者关于向量嵌入的演讲的链接。

---

## 87. 评论的艺术

**原文标题**: The Art of the Critic

**原文链接**: [https://www.metropolitanreview.org/p/the-art-of-the-critic](https://www.metropolitanreview.org/p/the-art-of-the-critic)

在《评论的艺术》中，尼克·里帕特拉佐内论证了深刻而有见地的文学批评的重要性，并大量借鉴了亨利·詹姆斯的例子。他哀叹当代文学文化中严肃批评的衰落，如今的书评常常沦为改述的宣传或作者访谈，而非真正地参与艺术形式。

里帕特拉佐内强调詹姆斯早期对狄更斯尖锐的批评，以此为例，说明批评能够识别出作者的缺点与他们的方法密不可分。他强调，缺乏天赋或感性的批评毫无用处，而且不应回避诚实的评价，即使是负面的评价。他用詹姆斯关于巴尔扎克的文章来说明，深刻的批评涉及具体性、持续的参与和类比思维，从而打开了作品和作家的生活。

文章指出了一个令人担忧的趋势，即作家从事批评工作报酬过低或完全是志愿性质，并表达了对杂志和报纸越来越不愿发表负面评论的担忧，担心会遭到强烈反对。里帕特拉佐内认为，健康的艺术文化得益于积极参与的受众，而这些受众是通过优秀的批评培养的，优秀的批评可以促进优秀的写作。他以詹姆斯的主张作结，即小说和评论家都必须认真对待自己，而最好的评论家是那些深入研究技艺的人，他们有助于培养人才并提升艺术形式。

---

## 88. 硅电极筛分孔：锂离子电池中稳定、快速的合金化化学

**原文标题**: Sieving pores: stable,fast alloying chemistry of Si -electrodes in Li-ion batt

**原文链接**: [https://www.nature.com/articles/s41467-025-60191-9](https://www.nature.com/articles/s41467-025-60191-9)

本文介绍了一种新型“筛分孔”设计的锂离子电池硅负极，旨在解决体积膨胀、机械应力和电荷转移限制等阻碍硅广泛应用的难题。该设计采用碳支撑结构，内部具有纳米孔主体以适应硅的变形，外部具有亚纳米孔入口，以促进循环过程中的预脱溶剂化和快速离子传输。

亚纳米孔入口的“筛分效应”导致富含无机物的固体电解质界面 (SEI) 的形成，从而在机械上将硅限制在孔内。这种限制产生应力-电压耦合效应，抑制有害的晶体 Li15Si4 的形成。因此，筛分孔硅/碳 (SSC) 复合电极表现出低电极膨胀 (在 1773 mAh g-1 时为 58%)、高初始/循环库仑效率 (93.6%/99.9%) 和最小的容量衰减 (每循环 0.015%)。

包含 SSC 电极的实用软包电池在 2A 电流下经过 1700 次循环后仍保持 80% 的容量，并具有 10 分钟的快速充电能力。SSC 材料采用可扩展的两步化学气相沉积 (CVD) 工艺合成，表明其在工业应用中的可行性。筛分孔设计有效地整合了机械稳定性和快速动力学，从而显着提高了硅负极的循环和倍率性能。

---

## 89. WeatherStar 4000+：天气频道模拟器

**原文标题**: WeatherStar 4000+: Weather Channel Simulator

**原文链接**: [https://weatherstar.netbymatt.com/](https://weatherstar.netbymatt.com/)

提供的文本描述的是“WeatherStar 4000+”，一个气象频道模拟器，具体版本为5.21.8。它似乎是一个旨在模拟气象频道界面并提供天气信息的软件应用程序。

主要特征和元素包括：

*   **位置输入：** 用户可以输入他们的位置以接收本地化的天气信息。
*   **当前状况：** 模拟器旨在显示当前状况，如温度、风力、湿度、露点、云高、能见度和气压。 但是，可能存在数据加载和显示问题，如“正在加载”、“失败”、“无数据”和“正在重试”等消息所示。
*   **每小时预报：** 显示温度、云量百分比和降水百分比的图表。
*   **旅行预报：** 建议用于旅行相关天气信息的选项。
*   **区域观测和年历：** 提供区域天气数据、日出/日落时间和月亮数据。
*   **风暴预测中心展望：** 显示潜在的风暴严重程度级别（边缘型、轻微型、增强型、中等等级、高级）。
*   **未来预报：** 显示星期一的天气预报。
*   **本地雷达：** 提供本地降水量的可视化表示，范围从轻微到严重。
*   **设置和分享：** 用于调整模拟器设置并通过永久链接分享预报信息的选项。 永久链接复制到剪贴板。
*   **技术信息：** 显示软件版本、站点 ID、雷达 ID 和区域 ID。

---

## 90. Catbench向量搜索演示新增Postgres SQL吞吐量和延迟监控

**原文标题**: Catbench Vector Search Demo Has Postgres SQL Throughput, Latency Monitoring Now

**原文链接**: [https://tanelpoder.com/posts/catbench-vector-search-query-throughput-latency-monitoring/](https://tanelpoder.com/posts/catbench-vector-search-query-throughput-latency-monitoring/)

CatBench：Postgres + PgVector演示应用，使用包含2.5万张宠物照片的Kaggle数据集，已更新至0.3版本，改进了向量搜索性能的监控能力。该应用展示了向量相似度搜索如何与常规应用数据集成，使用猫的照片根据外貌相似的猫的购买行为推荐产品。用户可以浏览UI并查看后端SQL查询及其执行计划。

主要新功能是“监控”页面，提供Postgres实例范围内的吞吐量和平均查询执行延迟图表。这允许用户观察不同的配置和工作负载如何影响性能。此次更新还包括一个显示热门查询的表格。一些不太有用的图表已被移至底部，作者指出当前PL/PgSQL循环配置中的Buffer Activity指标存在一些问题。

未来的计划包括整理代码以通过旋转将数据集扩展到900万张照片，为“猫欺诈检测”反向查找查询添加召回质量监控（允许对向量索引类型进行A/B测试），以及重构应用程序以支持其他数据库。目标仍然是提供一个学习工具，用于在完整的应用程序上下文中探索向量相似度搜索，让用户检查查询文本、执行计划和性能指标。

---

## 91. 最小文件

**原文标题**: Smallest Possible Files

**原文链接**: [https://github.com/mathiasbynens/small](https://github.com/mathiasbynens/small)

最小可能文件集：本仓库收集了各种编程、脚本和标记语言以及各种文件类型的最小可能语法有效文件。该项目旨在确定并展示创建每种类型的可运行文件（尽管通常为空或极简）所需的绝对最少代码或数据。

该项目欢迎贡献，涵盖档案文件（ZIP、TAR）、音频文件（MP3、WAV）、文档文件（PDF、RTF）、可执行文件（EXE、ELF、CLASS）、图形文件（BMP、JPG、PNG）、编程语言（C、Java、Python）、标记语言（HTML、XML、JSON）和视频格式（MP4、WEBM）等不同类别的文件类型。每个文件都代表在其各自格式规范内被认为是有效的最低要求。它处理的语言和文件格式列表多种多样且全面。该仓库采用公共领域弃权协议许可。

---

## 92. 有毒的根源，有毒的决策：CEO选拔中的偏见

**原文标题**: Toxic Origins, Toxic Decisions: Biases in CEO Selection

**原文链接**: [https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5270031](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5270031)

论文“毒性起源，毒性决策：CEO选拔中的偏差”研究了产前暴露于污染（特别是居住在未来超级基金场地附近）如何影响CEO选拔以及随后的冒险行为。作者P. Raghavendra Rau、YiLin Wu和Richard Lok-Si Ieong发现，在这些地区出生的人（被称为“超级基金CEO”）更有可能在内部得到晋升。

该研究表明，公司在内部晋升时，常常将运气误认为能力，倾向于那些高方差特征未被完全理解的冒险者。这些超级基金CEO由于产前污染暴露可能改变了风险偏好，因此在内部职位上表现出色。然而，一旦晋升为CEO，他们就会采取风险更高的外部政策和战略，从而导致公司波动性增加，并最终导致整体业绩下降。作者总结说，超级基金CEO的表现具有较低的均值但较高的方差，这突显了CEO选拔过程中的一个缺陷，即公司未能考虑到与可能具有更高风险承受能力的个体相关的固有风险。

---

## 93. 玛丽·米克尔自2019年以来的首份趋势报告，聚焦人工智能

**原文标题**: Mary Meeker's first Trends report since 2019, focused on AI

**原文链接**: [https://www.bondcap.com/reports/tai](https://www.bondcap.com/reports/tai)

在没有获得BOND | BOND发布的实际“自2019年以来Mary Meeker首份聚焦人工智能的趋势报告”的情况下，我只能根据Meeker报告中常见的内容和常见的人工智能趋势提供一份假设性的摘要。

**假想摘要:**

Mary Meeker重返科技趋势舞台，备受期待，主要关注人工智能。该报告可能分析了人工智能在各个行业的*当前采用情况*，突出了快速增长和挑战。预计将看到以下方面的数据：

*   **人工智能基础设施：** 云计算、数据中心以及支持人工智能开发和部署的专用硬件方面的支出。
*   **人工智能人才：** 对熟练的人工智能工程师、研究人员和数据科学家的需求。
*   **人工智能应用：** 人工智能在医疗保健（药物发现、诊断）、金融（欺诈检测、算法交易）、制造业（自动化、预测性维护）和客户服务（聊天机器人、个性化）等领域的具体应用案例。
*   **人工智能模型和数据：** 对大型语言模型（LLMs）的分析，以及高质量数据对于训练有效人工智能系统日益增长的重要性。
*   **人工智能监管：** 关于新兴人工智能治理格局的讨论，包括伦理考量、数据隐私问题和潜在的法规。
*   **人工智能的影响：** 人工智能的经济影响，包括创造和取代就业岗位、提高生产力以及整体经济增长。

该报告可能会确定人工智能生态系统中的主要参与者，包括老牌科技巨头、初创公司和研究机构。它也可能涉及与人工智能相关的风险，例如偏见、错误信息和安全漏洞。按照Meeker一贯的风格，预计会有一个数据丰富的演示，其中包含图表、图形和引人注目的统计数据来支持其主张。总体基调可能对人工智能的潜力持乐观态度，同时承认负责任的开发和部署的重要性。

---

## 94. 开源电路追踪工具

**原文标题**: Open-sourcing circuit tracing tools

**原文链接**: [https://www.anthropic.com/research/open-source-circuit-tracing](https://www.anthropic.com/research/open-source-circuit-tracing)

Anthropic开源电路追踪工具，包括用于生成归因图的库和一个由Neuronpedia托管的交互式前端，以促进大型语言模型（LLM）的可解释性研究。这些工具允许研究人员追踪模型得出特定输出的步骤，以交互方式可视化和注释这些步骤，并通过修改特征值来测试假设。该库支持流行的开源模型，如Gemma-2-2b和Llama-3.2-1b。

正如Anthropic首席执行官Dario Amodei所强调的那样，其目标是弥合人工智能能力与其内部运作理解之间的差距。这些工具已在内部用于研究多步推理和多语言表示。Anthropic鼓励社区参与分析现有图表并开发工具改进方案。该项目由Anthropic Fellows、Decode Research开发，并利用了GemmaScope项目的转码器。提供了包括演示笔记本和代码库在内的资源，供研究人员入门，并通过GitHub欢迎反馈。

---

## 95. 并非你的幻觉：人工智能正在加速变革的步伐

**原文标题**: It's not your imagination: AI is speeding up the pace of change

**原文链接**: [https://techcrunch.com/2025/05/30/its-not-your-imagination-ai-is-speeding-up-the-pace-of-change/](https://techcrunch.com/2025/05/30/its-not-your-imagination-ai-is-speeding-up-the-pace-of-change/)

前“互联网女王”玛丽·米克尔发布报告，强调人工智能发展和应用的“空前”速度和范围，超越了以往移动、社交和云计算等技术革命。这份名为《趋势——人工智能》的报告强调了人工智能使用量的快速增长、年经常性收入高的公司大量涌现以及使用成本的急剧下降。尽管训练人工智能模型的成本可能高达 10 亿美元，但推理成本在两年内下降了 99%。

报告还指出，竞争对手匹配功能的速度很快，尤其是在开源和中国模型方面，以及英伟达、谷歌和亚马逊等公司在专用芯片方面的进步。

人工智能与以往技术革命的不同之处在于财务回报。风险投资家正在大力投资人工智能，但由于需要大规模的基础设施投资，公司正在烧钱。报告总结认为，目前尚不清楚哪些人工智能公司能够实现长期盈利。

---

## 96. 展示HN: Donut Browser，一个浏览器编排器

**原文标题**: Show HN: Donut Browser, a Browser Orchestrator

**原文链接**: [https://donutbrowser.com/](https://donutbrowser.com/)

甜甜圈浏览器：一款免费开源的浏览器管理器，允许用户管理和启动具有独立配置文件的多个浏览器。其主要优势是创建无限数量的本地配置文件，每个配置文件都有自己的设置、扩展程序和数据，从而增强隐私和组织性。

它支持下载和管理多个浏览器，如Chromium和Firefox（但不包括TOR浏览器），并允许在它们之间无缝切换。它还为这些浏览器提供内置的代理支持。甜甜圈浏览器的设计目标是快速和轻量级，最大限度地减少资源使用。

一个独特的功能是可以为特定链接设置默认浏览器，防止它们在错误的浏览器中打开。该软件适用于macOS（包括Apple Silicon和基于Intel的Mac）、Windows和Linux。源代码可在GitHub上获取，强调其对免费和开源的承诺。常见问题解答部分涵盖了有关应用程序用途、支持的浏览器和操作系统、代理配置以及费用的基本问题。

---

## 97. 挪威1903年罕见维京船发现

**原文标题**: Norway's incredibly rare 1903 Viking ship discovery

**原文链接**: [https://www.youtube.com/watch?v=qaOVk4R-5oM](https://www.youtube.com/watch?v=qaOVk4R-5oM)

提供的“文章”极其简短，主要由YouTube关于版权、联系方式、政策和服务条款的样板文字组成。 实际标题“挪威1903年令人难以置信的罕见维京船发现”很有希望，但没有实际内容描述这一发现本身。

因此，摘要只能针对*存在*的信息：

此条目主要由一个标题组成，宣布1903年在挪威发现一艘罕见的维京船。 然而，条目的正文不包含关于船只或发现的任何信息。 相反，它显示了与版权、广告、开发者资源、隐私和服务条款相关的标准YouTube文本。 本质上，除了标题本身，这篇“文章”中没有可供总结的内容。

---

## 98. AI 回应可能包含错误

**原文标题**: AI Responses May Include Mistakes

**原文链接**: [https://www.os2museum.com/wp/ai-responses-may-include-mistakes/](https://www.os2museum.com/wp/ai-responses-may-include-mistakes/)

Michal Necasek博客文章《AI回应可能包含错误》强调了人工智能搜索结果的不可靠性，特别是使用谷歌人工智能查询关于IBM PS/2型号的信息时。作者发现，即使重新运行相同的查询，人工智能也会持续提供不准确和捏造的信息。例如，当搜索“PS/2 Model 280”（不存在的型号）时，人工智能生成了详细但不正确的规格，包括处理器类型、RAM大小和发布年份，且每次回应都有差异。

Necasek指出，人工智能对其错误答案的自信可能会产生误导，尤其是对于可能无法识别这些不准确之处的非专业人士。虽然人工智能偶尔会提供正确的答案（承认“Model 280”不存在），但这种情况很少见。

作者认为，这些人工智能生成的摘要比无用更糟糕，因为它们有可能传播错误信息。评论区也呼应了这一担忧，讨论了人工智能无法承认无知以及可能存在的“氛围编码”问题。评论者还指出，大型语言模型缺乏对确定性的真正理解，并根据统计概率而非实际知识生成回应。共识是，虽然人工智能可能对某些任务有用，但其不可靠性使其不适合研究或需要准确性的场合。

---

## 99. 翻盖手机上网：使用最初的Opera Mini浏览器

**原文标题**: The flip phone web: browsing with the original Opera Mini

**原文链接**: [https://www.spacebar.news/the-flip-phone-web-browsing-with-the-original-opera-mini/](https://www.spacebar.news/the-flip-phone-web-browsing-with-the-original-opera-mini/)

本文探讨了 Opera Mini 的历史遗产。Opera Mini 最初于 2005 年发布，专为处理能力不足以加载完整桌面网站的手机而设计。它巧妙地利用云服务器渲染页面和压缩数据，使低端手机也能访问网络，并大幅节省数据流量。 它曾风靡一时，到 2012 年用户达到 1.69 亿。

文章详细介绍了如何使用 Java 运行时和 MicroEmulator 在现代计算机上复活原始 Java ME 版本的 Opera Mini。 然后深入探讨浏览体验，重点介绍快速拨号、标签管理和内置 RSS feed 阅读器等功能（许多现代浏览器都缺少此功能）。 尽管由于其较旧的 Presto 引擎，在渲染现代网站方面存在一些限制，但 Opera Mini 仍然可以正确访问和显示“轻量级”或过时的网站。

作者指出，Opera Mini 的服务器位于阿姆斯特丹，充当代理服务器，避免了旧浏览器上经常遇到的 SSL 证书问题。 虽然该浏览器会投放插页式广告，但目前它们无法正常运行。

最终，文章承认了 Opera Mini 的历史意义及其持续但有限的功能。 尽管该浏览器不太可能盈利，但它仍然在运营，仍然有一小部分活跃用户在旧功能手机上使用它。 作者鼓励拥有兼容设备的读者在它最终消亡之前尝试一下。 文章最后建议不要使用现代 Opera 和 Opera GX 浏览器，因为该公司存在争议性做法。

---

## 100. 我在班加罗尔创办了一个小型数学俱乐部。

**原文标题**: I started a little math club in Bangalore

**原文链接**: [https://teachyourselfmath.app/club](https://teachyourselfmath.app/club)

Vivek Nathani在班加罗尔创办了一个数学俱乐部，以重拾他在大学时代错过的协作学习体验。毕业后，数学成了一种孤独的追求，他渴望与同伴们共同探索思想的那种经历。

该俱乐部已经在科尔曼加拉的Dialogues Cafe成功举办了两次聚会。第一次聚会于2025年3月15日举行，有7人参加。第二次聚会于2025年5月4日举行，有8人参加。每次会议上，参与者们一起解决一套问题。Vivek感谢@clearlysid、@lifeofadvait和@Sarve___tanvesh在组织聚会方面的帮助。

Vivek表达了他对俱乐部的热情，并鼓励任何对共享数学学习体验产生共鸣的人与他联系。可以通过电子邮件viveknathani2402 at gmail[dot]com或Twitter @viveknathani_联系他。

---

