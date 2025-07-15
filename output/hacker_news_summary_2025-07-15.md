# Hacker News 热门文章摘要 (2025-07-15)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 美国国家标准与技术研究院离子钟创下世界最精准时钟新纪录

**原文标题**: NIST Ion Clock Sets New Record for Most Accurate Clock in the World

**原文链接**: [https://www.nist.gov/news-events/news/2025/07/nist-ion-clock-sets-new-record-most-accurate-clock-world](https://www.nist.gov/news-events/news/2025/07/nist-ion-clock-sets-new-record-most-accurate-clock-world)

美国国家标准与技术研究院研发出迄今为止最精确的原子钟，一种基于铝离子的“量子逻辑时钟”，其计时精度高达19位小数。这项突破显著优于之前的记录，精度提高了41%，稳定性是其他任何离子钟的2.6倍。

该时钟精度的提高源于20年来对其所有组件的持续开发和改进。其关键创新在于将铝离子（用于其稳定的滴答声）与镁离子（用于激光冷却和状态读出）配对的“伙伴系统”。该团队通过重新设计离子阱，采用更厚的金刚石晶圆和改进的镀金涂层，解决了离子过度微运动等难题，并通过用钛重建真空室来减少氢气的干扰。

为了进一步提高稳定性，该团队与JILA的Jun Ye合作，通过光纤链路利用超稳激光器，减少了量子波动。这使得该团队能够探测离子整整一秒钟，从而大大缩短了达到第19位小数所需的平均时间，从几周缩短到一天半。

这项破纪录的精度有助于国际社会重新定义秒，并为量子物理、量子技术、大地测量学以及探索超越标准模型的物理学（例如研究基本常数的恒定性）打开了大门。研究人员计划通过扩大离子数量并使它们纠缠来进一步增强时钟的功能。

---

## 2. 展示 HN: Shoggoth Mini – 一个由 GPT-4o 和强化学习驱动的柔软触手机器人

**原文标题**: Show HN: Shoggoth Mini – A soft tentacle robot powered by GPT-4o and RL

**原文链接**: [https://www.matthieulc.com/posts/shoggoth-mini](https://www.matthieulc.com/posts/shoggoth-mini)

修格斯迷你：探索实用功能之外机器人表现力的触手软体机器人项目。该项目由Matthieu B. Le Cauchois创建，灵感来源于苹果公司的ELEGNT论文和SpiRobs，旨在通过运动赋予机器人一种生命感。

该项目涉及硬件设计，从简单的底座开始，演变成带有立体摄像头（“眼睛”）的圆顶状头部。电缆缠绕问题通过线轴盖解决，校准脚本改善了张力控制，脊椎加粗以防止下垂。

控制通过双层系统实现：底层控制使用开环原语和闭环强化学习（RL）策略（如手指追踪），高层控制使用GPT-4o的实时API，该API可以流式传输音频和文本。视觉事件经过处理后为GPT-4o提供提示。二维投影是简化手动和自动控制的关键，将触控板的移动映射到肌腱长度。

感知依赖于MediaPipe进行手部追踪，以及在自定义数据集上训练的YOLO模型进行触手尖端追踪。强化学习，特别是PPO，被用于训练机器人跟随用户的手指。通过动态随机化和约束动作空间，改善了从模拟到现实的迁移。

作者观察到可预测性降低了生命感。未来的方向包括赋予机器人声音、扩展其表现力、增加更多触手，以及使用直接驱动电机。该项目的代码和3D打印文件可在GitHub上找到。

---

## 3. 对OpenAI的反思

**原文标题**: Reflections on OpenAI

**原文链接**: [https://calv.info/openai-reflections](https://calv.info/openai-reflections)

在OpenAI工作一年的反思

本文反思了作者在OpenAI从2024年5月到2025年7月为期一年的工作经历。作者重点介绍了OpenAI的快速增长（一年内员工从1000人增长到3000人）及其对公司文化和运营的影响。沟通主要依赖Slack，组织被描述为自下而上和任人唯贤，好的想法和执行力备受重视。公司有强烈的行动偏好和快速迭代。

作者注意到，由于其备受瞩目的工作和消费者导向，OpenAI受到了不同寻常的审查和保密。尽管压力很大，作者相信员工们都在真诚地努力做正确的事。该公司被描述为旨在广泛分配人工智能的益处。安全，特别是解决实际风险，是一个重要的担忧。

本文深入探讨了工程方面，提到了运行在Azure上的大型Python单体仓库的使用。基础设施受到强大的Meta/Instagram管道的影响，并拥有各种系统的内部实现。作者了解了像ChatGPT这样的大型消费者品牌的规模和影响、训练大型模型的高级流程以及GPU基准测试的重要性。

总的来说，作者将OpenAI描绘成一个雄心勃勃的组织，在多个领域同时竞争，培养一种快速创新和适应的文化，尽管面临着规模化和公众密切关注的挑战。作者离开是为了寻求新的开始，但承认在OpenAI获得的重大影响和宝贵经验。

---

## 4. LLM 不可避免论

**原文标题**: LLM Inevitabilism

**原文链接**: [https://tomrenner.com/posts/llm-inevitabilism/](https://tomrenner.com/posts/llm-inevitabilism/)

本文反对围绕大型语言模型（LLMs）和人工智能兴起的“必然论”。作者将必然论定义为将特定未来框定为不可避免，从而将讨论范围限制在适应上，而非质疑该未来的可取性。

作者通过类比辩论技巧解释了如何通过框架论证来控制对话。他们引用了马克·扎克伯格、吴恩达和罗睿兰等科技领袖使用必然论语言来推销这样一种观点，即人工智能不是应该质疑的东西，而是应该拥抱和适应的东西。这些说法往往带有隐性的威胁，暗示那些抵制者将会落后。

作者批判了这种框架，认为它扼杀了关于我们想要创造的未来类型的批判性讨论。他们认为，我们在如何开发和利用技术方面确实有选择，而屈服于必然性的叙事会放弃这种能动性。

最终，本文是一项行动号召，敦促读者抵制必然论的诱惑，展望他们渴望的未来，并积极为之奋斗，而不是被动地接受由技术决定论所决定的未来。作者特别针对围绕LLMs及其在塑造未来中的作用的叙事，建议我们应该批判性地评估它们的潜在影响，并就它们融入社会做出有意识的选择。

---

## 5. 向 rust-lang/regex 添加后向断言

**原文标题**: Adding lookbehinds to rust-lang/regex

**原文链接**: [https://systemf.epfl.ch/blog/rust-regex-lookbehinds/](https://systemf.epfl.ch/blog/rust-regex-lookbehinds/)

Rust `regex` crate 中无界无捕获后行断言的实现

---

## 6. Blender 4.5 LTS 发布

**原文标题**: Blender 4.5 LTS Released

**原文链接**: [https://www.blender.org/download/releases/4-5/](https://www.blender.org/download/releases/4-5/)

无法访问文章链接。

---

## 7. 成为更好的程序员，在脑海中进行小型证明。

**原文标题**: To be a better programmer, write little proofs in your head

**原文链接**: [https://the-nerve-blog.ghost.io/to-be-a-better-programmer-write-little-proofs-in-your-head/](https://the-nerve-blog.ghost.io/to-be-a-better-programmer-write-little-proofs-in-your-head/)

本文鼓励程序员在编写代码时进行“草图证明”式的思考，以提高速度和准确性。这涉及即时推理代码，这是一项通过实践培养的技能。作者提供了几个推理技巧的例子，包括：

*   **单调性：** 识别代码中仅向前移动的部分（如检查点或LSM树），以排除许多可能的结果。 不可变性被描述为单调性的近亲。

*   **前置和后置条件：** 定义函数运行前后应该为真的条件。 这有助于推理并生成单元测试。

*   **不变性：** 识别代码执行期间应始终为真的条件，以确保一致性。

*   **隔离：** 通过识别防止意外传播的“防火墙”来限制代码更改的“爆炸半径”。 这有助于证明未更改的行为保持不变。

*   **归纳法：** 将归纳推理应用于递归函数和数据结构（如树和列表），以证明正确性。 它涉及证明基本情况，并证明如果条件对 `n` 成立，则它也对 `n+1` 成立。

通过有意识地应用这些技术，程序员可以增强对代码正确性的信心，减少调试时间并提高整体效率。 关键是养成在编写代码时推理代码属性的习惯。

---

## 8. Show HN: 我们为 Apple Silicon 自研了推理引擎

**原文标题**: Show HN: We made our own inference engine for Apple Silicon

**原文链接**: [https://github.com/trymirai/uzu](https://github.com/trymirai/uzu)

Uzu：专为Apple Silicon打造的高性能AI推理引擎

Uzu是一款全新的高性能推理引擎，专为在Apple Silicon上运行AI模型而设计。它提供简洁的API，采用GPU内核和MPSGraph相结合的混合架构以获得最佳性能，统一的模型配置，以及可追踪的计算过程以确保正确性。

该引擎使用其自身的模型格式，可以使用`lalamo`工具从其他格式转换而来。为了方便与Swift项目集成，提供了预构建的Swift绑定（`uzu-swift`）。命令行界面（`uzu_cli`）允许运行模型或启动服务器。

快速入门指南演示了如何将uzu集成到Rust项目中，加载模型并运行推理。在Apple M2上的性能基准测试显示出令人期待的结果，在bf16/f16精度下，通常优于`llama.cpp`，适用于各种模型，包括Llama-3.2-1B-Instruct、Qwen和Gemma。在较小模型上，性能优势尤其明显。该项目以MIT许可开源。

---

## 9. 基于标准19芯光纤的Petabit级超千公里传输

**原文标题**: Petabit-class transmission over > 1000 km using standard 19-core optical fiber

**原文链接**: [https://www.nict.go.jp/en/press/2025/05/29-1.html](https://www.nict.go.jp/en/press/2025/05/29-1.html)

NICT与住友电工在光纤通信领域创下新的世界纪录，使用特制19芯光纤（标准0.125毫米包层直径）在1808公里距离上实现了每秒1.02拍比特的数据传输。该成就的容量距离乘积高达每秒1.86艾比特 x 公里，为历史最高纪录。

这一突破的关键在于开发了一种新型19芯光纤，其在多个波段（C波段和L波段）具有低损耗，并配备了兼容的光学放大系统。与之前使用类似光纤在较短距离上的演示相比，这大大延长了传输距离。

该传输系统采用环形回路设置，包含19个纤芯和用于增强信号的光学放大器。数字信号处理，特别是MIMO，消除了纤芯之间的干扰。结果表明，未来可扩展、高容量网络具有满足日益增长的数据需求的潜力，尤其是在后5G社会中。

这项研究作为一份最后时刻提交的论文在光纤通信会议（OFC 2025）上发表，以表彰其在推进长距离、高容量光通信基础设施方面的重要性。NICT专注于传输系统设计和实验，而住友电工则负责19芯光纤的设计和制造。

---

## 10. 展示HN：我做了这个来和我女朋友说丹麦语 – 适用于任何语言

**原文标题**: Show HN: I built this to talk Danish to my girlfriend – works with any language

**原文链接**: [https://menerdu.vercel.app/](https://menerdu.vercel.app/)

此“Show HN”帖子介绍“Mener du”，一款人工智能工具，旨在通过提供即时更正和解释来帮助用户用外语交流。该工具旨在通过允许用户用目标语言写作，并在花括号内添加上下文以表示缺失的单词或澄清意图，来弥合语言障碍。然后，“Mener du”提供更正、更改的解释以及翻译回用户母语，以确保理解。

主要功能包括上下文感知的更正、即时翻译、高质量的文本转语音以进行发音练习以及用于跟踪进度的学习历史记录。提供的示例使用丹麦语，并演示了该工具如何建议更自然的措辞。“Mener du”被呈现为一种免费且可立即访问的工具，无需注册或订阅，使其适合自发语言使用。目前，它支持丹麦语、德语、法语和西班牙语，并鼓励用户开始输入以体验其优势。该帖子最后呼吁大家支持，以保持该工具的免费和可访问性。

---

## 11. Apple MLX 添加 CUDA 支持

**原文标题**: Apple's MLX adding CUDA support

**原文链接**: [https://github.com/ml-explore/mlx/pull/1983](https://github.com/ml-explore/mlx/pull/1983)

该GitHub议题讨论了为Apple的MLX机器学习框架添加CUDA后端。目标是使MLX能够利用NVIDIA GPU进行本地开发（在Mac上）和高性能计算系统上的部署。主要作者zcbenz正在Apple的赞助下开发此功能。

最初的PR引入了基本的CUDA基础设施，允许运行一个简单的教程示例。开发者也表达了添加ROCm（AMD GPU）支持的兴趣。讨论集中于如何最好地将CUDA后端集成到MLX中，倾向于合并增量PR，以便更容易通过CI进行维护和测试。

作者分享了将内核移植到CUDA的挑战，特别是关于传递形状/步幅以及优化内核性能方面。通过切换到`cudaEvent`进行事件处理、减少预取调用以及暂时延迟操作数和临时变量的销毁（尽管最后一个优化引发了对大型图内存使用的担忧，并被标记为进一步配置），实现了显著的性能改进。

性能分析表明内核启动和同步存在开销，这些开销通过一些优化得到了解决。 Logistic回归示例成功运行，性能从500次迭代/秒提高到2100次迭代/秒。缓冲区缓存的实现计划在稍后阶段进行。

最初的PR最终被关闭，因为主干已经合并到主分支中，并推送了额外的提交，用于矩阵乘法和排序等特定功能。

---

## 12. Cloudflare开始阻止英国用户访问盗版网站

**原文标题**: Cloudflare Starts Blocking Pirate Sites for UK Users

**原文链接**: [https://torrentfreak.com/cloudflare-starts-blocking-pirate-sites-for-uk-users-thats-a-pretty-big-deal-250715/](https://torrentfreak.com/cloudflare-starts-blocking-pirate-sites-for-uk-users-thats-a-pretty-big-deal-250715/)

Cloudflare应MPA要求屏蔽英国用户访问约200个盗版网站域名

---

## 13. 直白主义困扰当今电影

**原文标题**: Literalism plaguing today’s movies

**原文链接**: [https://www.newyorker.com/culture/critics-notebook/the-new-literalism-plaguing-todays-biggest-movies](https://www.newyorker.com/culture/critics-notebook/the-new-literalism-plaguing-todays-biggest-movies)

本文批判了近期电影中一种被称为“新字面主义”的趋势。它的特点是笨拙、倾向于陈述显而易见的事实以及缺乏微妙性，最终削弱了艺术性。作者用来自《角斗士2》、《大都会》和《学徒》的假设例子来说明这一点，其中人物莫名其妙地以一种极其直接和刺耳的方式口头表达隐喻。

作者认为，这种字面主义甚至渗透到备受赞誉的电影中，并引用了奥斯卡金像奖提名影片中的例子，如《沙丘：第二部》、《魔法坏女巫》、《完全未知》、《阿诺拉》、《实质》、《艾米莉亚·佩雷斯》、《镍男孩》、《野兽派》、《我还在这里》。作者认为，这些电影依赖于可预测的公式、无意义的视觉暗示以及对主题的明确重述，而不是留下解释的空间。

作者将这一趋势与更广泛的文化现象联系起来：一种对熟悉、公式化和易于消化的内容的偏好。他们认为，这源于对当代生活压倒性本质的焦虑，导致人们渴望“预先消化的文化舒适食物”。这也包括我们对重复的痴迷，导致“重新演绎”而不是真正反思历史。

最终，作者认为“新字面主义”是对观众的一种屈尊，其中内容被简化为适合“横幅广告”的易于识别的概念。

文章以一线希望结束，赞扬爱德华·伯格的《教皇选举》作为一个例外，这部电影相信观众能够理解模糊性和微妙性，使其与流行的“新字面主义”形成令人耳目一新的对比。

---

## 14. Kiro：一个全新的自主型IDE

**原文标题**: Kiro: A new agentic IDE

**原文链接**: [https://kiro.dev/blog/introducing-kiro/](https://kiro.dev/blog/introducing-kiro/)

Kiro：一款弥合 AI 辅助原型设计与可用于生产的软件之间差距的全新 AI 驱动 IDE。它强调“规范驱动开发”，以解决 AI 生成代码中固有的未文档化假设、不明确的需求和设计复杂性等挑战。

Kiro 引入了两项关键功能：**规范 (Specs) 和钩子 (Hooks)。** 规范是帮助开发者深入思考功能、提前重构代码和理解系统行为的工件。 Kiro 从单个提示中提取需求，生成包含验收标准的用户故事、技术设计文档（数据流图、接口、数据库模式）以及包含单元测试、集成测试和可访问性考虑等详细信息的实现任务。 规范还会与不断演变的代码库保持同步。

钩子是事件驱动的自动化程序，其作用类似于经验丰富的开发者，可以发现不一致之处并完成样板任务。 这些触发器基于文件保存、创建或删除操作，并且可以自定义以强制执行编码标准、更新文档或扫描安全漏洞。

除了规范和钩子之外，Kiro 还包括模型上下文协议 (MCP) 支持、指导规则和代理式聊天等功能。 它基于 Code OSS 构建，确保与 VS Code 设置和插件的兼容性。

Kiro 旨在改善团队设计一致性、解决冲突的需求、减少技术债务、改进代码审查并保留机构知识。 Kiro 目前在预览期间免费，并且可在 Mac、Windows 和 Linux 上使用，支持大多数流行的语言。 它提供了一个动手教程。

---

## 15. 东南亚的录像带、VCD和激光影碟

**原文标题**: VHS, VCDs, and Laserdiscs in Southeast Asia

**原文链接**: [https://rubenerd.com/vcds-and-laserdiscs-in-southeast-asia/](https://rubenerd.com/vcds-and-laserdiscs-in-southeast-asia/)

本文探讨了录像带(VHS)、VCD和激光影碟在东南亚（尤其是新加坡）的流行，并将其与录像带在澳大利亚和美国等西方市场的主导地位进行对比。虽然新加坡有售录像带，但VCD和激光影碟获得了更多的青睐。对此常见的解释是热带气候导致录像带发霉，这在一定程度上是事实；从澳大利亚带来的录像带经常发霉。然而，新加坡本地生产的录像带似乎不太容易受到影响。

激光影碟因其在潮湿气候中的卓越耐久性以及与日本出口市场的融合而受到富裕电影爱好者和租赁商店的欢迎，但仍然价格昂贵。之后，VCD在20世纪90年代凭借其经济实惠和易于分发的特点成为主流格式。

VCD利用与音频CD相同的技术，将视频压缩成更小的尺寸，使其可以存储在CD上。其优点包括体积小、耐用以及易于大规模生产和盗版。盗版VCD的盛行，以几美元的价格随处可见，使其成为一个受欢迎的选择，特别是考虑到新加坡政府的打击，导致盗版市场转移到马来西亚。正版VCD也存在，以实惠的价格提供流行节目的观看途径。

文章总结认为，虽然气候起到了一定的作用，但经济因素是VCD在东南亚流行的重要驱动因素，作为一种更经济实惠的选择，VCD一直持续到DVD时代。

---

## 16. LIGO探测到迄今为止质量最大的黑洞并合

**原文标题**: LIGO detects most massive black hole merger to date

**原文链接**: [https://www.caltech.edu/about/news/ligo-detects-most-massive-black-hole-merger-to-date](https://www.caltech.edu/about/news/ligo-detects-most-massive-black-hole-merger-to-date)

LIGO-Virgo-KAGRA (LVK)合作组织于2023年11月23日探测到迄今为止质量最大的黑洞合并事件，编号为GW231123。这次强烈的合并产生了一个质量约为太阳225倍的最终黑洞，超过了2021年的前纪录保持者。该黑洞由两个质量分别约为太阳100倍和140倍，且高速旋转的黑洞碰撞形成。

这一发现挑战了当前黑洞形成的物理模型，因为通过标准恒星演化过程预计不会形成如此大质量的黑洞。研究人员认为，这些黑洞可能是通过较小黑洞的早期合并形成的。该事件突破了引力波探测技术和理论模型的极限，需要复杂的模型来准确解读信号。

科学家们正在继续完善他们对GW231123的分析，希望能揭示其所有意义。相关数据将提供给其他研究人员进行分析。该发现将于2025年7月在英国苏格兰格拉斯哥举行的GR-Amaldi会议上公布。该发现突显了引力波天文学在揭示黑洞的本质以及该领域进一步发现的潜力方面的重要性。

---

## 17. 荷马英译者：书评

**原文标题**: "English Translators of Homer": A Review

**原文链接**: [https://whatisthequestion.wordpress.com/2025/07/12/english-translators-of-homer-by-simeon-underwood/](https://whatisthequestion.wordpress.com/2025/07/12/english-translators-of-homer-by-simeon-underwood/)

西缅·安德伍德《荷马的英语译者》书评：评论者认为书名具有误导性，因为他们期望看到翻译的比较，而本书实际上是关于译者及其选择的历史。评论者批评该书篇幅过短，且缺乏文本示例来阐释安德伍德关于每位译者风格的观点。

尽管存在这些缺点，评论者最终认为这本书是“好的”。它阐明了如何思考不同的翻译以及在翻译中寻找什么。安德伍德的核心论点是，翻译是在保留源文本和创建可读目标文本之间取得平衡，这在诗歌方面尤其具有挑战性。他探讨了是捕捉古代读者的体验还是为现代读者创造相似的情绪这一难题。

评论者认为关于查普曼、蒲柏和里厄的章节很枯燥，但欣赏最后一章关于克里斯托弗·洛格的《战争音乐》的章节，这是《伊利亚特》的现代改编版。洛格的方法虽然备受争议，但突出了翻译中固有的选择。评论者将洛格的作品与更字面的翻译（如拉蒂摩尔的翻译）进行了对比，后者优先考虑与希腊语逐行对应。评论者指出诺克斯对洛格的尖刻评论证明了风格上的分歧，并发现诺克斯的批评最终令人信服。评论者更喜欢米切尔和隆巴多的翻译，但发现洛格的方法对于打开对原文的新视角具有价值。评论者总结说，虽然这本书有其缺陷，但它具有宝贵的见解。

---

## 18. Cognition (Devin AI) 收购 Windsurf

**原文标题**: Cognition (Devin AI) to Acquire Windsurf

**原文链接**: [https://cognition.ai/blog/windsurf](https://cognition.ai/blog/windsurf)

开发Devin AI的Cognition公司收购了代理式IDE Windsurf。此次收购包括Windsurf的知识产权、产品、商标、品牌及其团队，Cognition高度重视该团队。

Windsurf团队将在短期内继续照常运营，而Cognition计划在未来几个月内将其功能集成到其产品中。目标是加速软件工程开发，并将Devin的自主代理能力与Windsurf的IDE和上市策略相结合。

此次收购为Cognition带来了重要资产，包括：

*   集成了Claude模型的Windsurf IDE
*   Windsurf的知识产权
*   8200万美元的年度经常性收入（ARR），以及快速增长的企业业务
*   超过350家企业客户和数十万日活跃用户的用户群
*   Windsurf才华横溢的工程、产品和上市团队

Cognition强调尊重和公平地对待所有员工，包括新的Windsurf团队。所有Windsurf员工都将参与此次交易的财务分成，他们的归属悬崖将被免除，并因过去的工作而获得完全加速的归属。

Cognition相信此次收购将加速其塑造软件工程未来的使命，使工程师能够专注于更高层次的设计和创造力，而不是手动编码。

---

## 19. 微型冒险 – 太空侵略 (在线模拟器)

**原文标题**: Micro Adventure – Space Attack (online emulator)

**原文链接**: [https://auri-microadventure.azurewebsites.net/](https://auri-microadventure.azurewebsites.net/)

本节选介绍了一场“微型冒险”，读者将扮演奥赖恩，一位被ACT（冒险连接团队）招募的计算机专家，负责抵御BRUTE（随机非法恐怖与邪恶局）。冒险始于一段被破译的信息，揭示了一座秘密的美国太空站“竞技场一号”正身陷险境。

奥赖恩迅速被运送到卡纳维拉尔角，并与一支专家团队一同发射进入太空：海伦·格蕾丝上校，一位军事联络员和弹道学专家；马可龙博士，一位语言学家；洛厄尔教授，一位天文学家；以及廷克，看起来像是来自一家玩具公司。

抵达太空后，团队了解了局势的严重性。“竞技场一号”已部分被一支外星力量控制，该力量已使其武器失效。更糟糕的是，如果武器处于离线状态，空间站将被编程在36小时内自毁。他们的任务是重新控制空间站并阻止其摧毁，但时间紧迫，他们将面对一个强大而未知的敌人。一个被破坏的倒计时程序几乎阻止了他们的升空，但奥赖恩及时修复了它。

---

## 20. 胜、负、平：英格兰足球比赛结果的趋势

**原文标题**: Win, lose, or draw: trends in English football match results

**原文链接**: [https://blog.engora.com/2025/06/english-football-data.html](https://blog.engora.com/2025/06/english-football-data.html)

无法访问文章链接。

---

## 21. 随机选择是建立稳定精英体制机构的必要条件。

**原文标题**: Random selection is necessary to create stable meritocratic institutions

**原文链接**: [https://assemblingamerica.substack.com/p/there-is-no-meritocracy-without-lottocracy](https://assemblingamerica.substack.com/p/there-is-no-meritocracy-without-lottocracy)

文章《随机选择是建立稳定精英体制的必要条件》认为，如果不引入随机选择或“抽签制”的要素，真正的精英体制是不可能实现的。作者认为，看似精英体制的系统不可避免地会演变成自我延续的寡头统治，在这种统治中，特权和关系而非纯粹的才干决定成功。这种情况的发生是因为优势会代代相传，造成难以克服的不平等起点。

作者认为，随机选择，尤其是在领导职位上的随机选择，是一种必要的纠正措施。它可以防止权力固化，打破现有的特权网络，并引入不同的视角。通过偶尔绕过既定的等级制度，给予传统权力结构之外的个人机会，抽签制有助于确保系统保持开放性，并能响应新的想法和人才。

文章强调，抽签制并非完全消除精英制，而是对其进行补充，以防止纯粹基于精英的系统不可避免地伴随而来的腐败和停滞。作者认为，引入随机选择的要素可以促成更强大、更公平和更具适应性的机构，这些机构能够真正代表广泛的人才和观点。结论是，一个设计良好的系统可以平衡才干和随机性，从而促进一个更加公正和最终更加有效的社会。

---

## 22. 当Sigterm失效时：一个Postgres谜团

**原文标题**: When Sigterm Does Nothing: A Postgres Mystery

**原文链接**: [https://clickhouse.com/blog/sigterm-postgres-mystery](https://clickhouse.com/blog/sigterm-postgres-mystery)

ClickPipes团队遇到了一个持久性错误：在Postgres只读副本上创建逻辑复制槽时，有时会无限期停滞，变得无法终止，并可能因WAL保留导致存储耗尽。这被追溯到Postgres中的`XactLockTableWait`函数，该函数在创建槽之前等待较旧的事务完成，以确保解码的一致性点。

在主Postgres实例上，`XactLockTableWait`会获取事务ID上的锁，等待直到事务完成。然而，在只读副本（热备）上，`LockAcquire`会立即返回，绕过预期的中断处理。然后，该函数进入一个使用`TransactionIdIsInProgress`和`pg_usleep`的1毫秒轮询循环，由于备机对主事务的间接观察，该循环可能会无限期运行。此循环中缺少中断检查导致该进程无法通过`SIGTERM`或`pg_cancel_backend`终止。

该团队提交了一个补丁，在循环中每次调用`pg_usleep`之前添加了`CHECK_FOR_INTERRUPTS()`，该补丁很快被接受并反向移植到受支持的Postgres版本，从而允许进程终止。目前正在讨论进一步的改进措施，以添加等待事件并优化备机的事务完成等待机制，这可能会进入Postgres 19。这个问题突显了编写良好的代码在超出其原始设计范围的上下文中使用时，可能会导致意想不到的问题。

---

## 23. 用于高性能的SQLite异步连接池

**原文标题**: SQLite async connection pool for high-performance

**原文链接**: [https://github.com/slaily/aiosqlitepool](https://github.com/slaily/aiosqlitepool)

`aiosqlitepool` 是一个用于 asyncio SQLite 应用的高性能连接池。它通过消除连接开销、利用“热”缓存加速查询以及最大化并发吞吐量来提升性能。它是一个与 `aiosqlite` 等 asyncio 驱动程序配合使用的层，而不是替代品。

主要特性包括重用连接以避免重复设置和拆卸，保持 SQLite 的内存页缓存“热”状态以访问频繁访问的数据，以及增加每秒处理的数据库查询数量。

用法包括提供一个连接工厂，一个用于创建数据库连接的异步函数。连接池管理连接，但不管理事务（需要手动 `commit()` 或 `rollback()`）。建议使用针对高性能优化的 SQLite pragmas，例如 `PRAGMA journal_mode = WAL`。

`aiosqlitepool` 与 FastAPI 集成良好，可以使用生命周期上下文管理器进行生命周期管理，使用应用程序状态进行全局访问，并使用依赖注入来轻松访问连接。

虽然 SQLite 连接开销较低，但 `aiosqlitepool` 有助于缓解并发环境中的写入争用。它推荐用于处理稳定 Web 流量或高吞吐量作业的服务，以及需要可预测的低延迟或旨在实现最小占用空间的应用程序。基准测试表明每秒查询次数和延迟都有显着提高。

该库与实现了 `execute()`、`rollback()` 和 `close()` 方法的驱动程序兼容，并且已通过 `aiosqlite` 的官方测试。它以 MIT 许可证发布。

---

## 24. Show HN: Bedrock – 用于随时随地运行程序的8位计算系统

**原文标题**: Show HN: Bedrock – An 8-bit computing system for running programs anywhere

**原文链接**: [https://benbridle.com/projects/bedrock.html](https://benbridle.com/projects/bedrock.html)

Bedrock：为长久使用而设计的便携式8位计算机系统规范。它不是物理设备，而是一种标准，允许程序在任何具有Bedrock模拟器的系统上运行，而无需考虑底层硬件。该模拟器充当程序和系统之间的翻译器。

主要特性包括小指令集（32条指令）和有限数量的设备（12个），使其易于学习和实现。现有的模拟器支持Windows、Linux、Web和任天堂DS。

本文提供教程（例如，打印字符串）、文档（用户手册、规范）和可运行的示例，演示各种算法。提供JavaScript（基于Web）和Rust（Windows/Linux）的实现。

Bedrock的灵感来自Uxn虚拟机，但简化了接口和指令集，以便在资源受限的系统上获得更好的性能。该名称指的是“基岩抽象”，专注于简化程序环境，而不是创建更高级别的指令集。

文章最后展示了在基于Web的模拟器中运行的实时演示，包括像素艺术程序、贪吃蛇游戏、微波炉时钟、系统信息显示和任天堂DS的屏幕键盘。

---

## 25. 上下文腐烂：输入tokens增加如何影响LLM性能

**原文标题**: Context Rot: How increasing input tokens impacts LLM performance

**原文链接**: [https://research.trychroma.com/context-rot](https://research.trychroma.com/context-rot)

长文本输入对大语言模型性能的影响：语境腐烂现象研究

本文探讨了输入文本长度增加如何影响大语言模型(LLM)的性能，这种现象被称为“语境腐烂”。虽然LLM在简单的检索任务（如“大海捞针”）中表现良好，但作者证明，随着输入长度的增加，即使在任务复杂性保持不变的情况下，在更复杂和真实的场景中，其性能也会下降。

该研究评估了18个具有不同参数的LLM。 通过扩展“大海捞针”基准测试的受控实验，作者研究了针-问题相似性、干扰项、针-草堆相似性和草堆结构的影响。他们的发现表明：

* 模型性能随着输入长度的增加而持续下降。
* 较低的针-问题相似性加剧了性能下降。
* 干扰项的影响不一致，突出了模型对不相关信息的特定漏洞，尤其是在输入长度增加时。
* 针-草堆相似性会影响性能，表明草堆的内容是相关的。
* 草堆结构（连贯与随机内容）会影响模型处理长输入的方式。

作者强调，现实世界的应用程序比“大海捞针”更复杂，由于上下文长度，可能会经历更明显的性能下降。他们提供了完整的代码库来复现他们的结果，有助于更深入地理解LLM在长输入情况下的行为。该研究呼吁重新评估长文本评估，从简单的词汇检索转向更具代表性和细致的基准测试。

---

## 26. JPEG XL 图像编码的历史、特性、编码工具、设计原理

**原文标题**: The JPEG XL Image Coding History, Features, Coding Tools, Design Rationale

**原文链接**: [https://arxiv.org/abs/2506.05987](https://arxiv.org/abs/2506.05987)

这篇arXiv文章（arXiv:2506.05987）全面概述了JPEG XL图像编码系统。该论文由Jon Sneyers和另外十一位作者撰写，详细介绍了JPEG XL的历史、设计原理、编码工具和未来潜力。其目的是作为ISO/IEC 18181标准的补充，或者作为理解JPEG XL的独立资源。

JPEG XL被定位为一种下一代图像编解码器，旨在取代JPEG、PNG和GIF等较旧的格式。它拥有最先进的压缩性能、无损JPEG重压缩能力和高级功能。

该论文很可能深入探讨JPEG XL的技术方面，详细介绍其编码工具和底层原理。它还探讨了编解码器设计选择背后的原因。包含62个图表明其对复杂概念的解释具有视觉支持。该文章被归类为计算机科学 > 多媒体，包含与图像处理和数据压缩相关的信息。

---

## 27. 移动装配线百年纪念 (2013)

**原文标题**: The Moving Assembly Line Turns 100 (2013)

**原文链接**: [https://www.assemblymag.com/articles/91581-the-moving-assembly-line-turns-100](https://www.assemblymag.com/articles/91581-the-moving-assembly-line-turns-100)

2013年10月，世界庆祝了福特移动装配线一百周年，这是一项彻底改变制造业的关键创新。移动装配线于1913年10月7日在福特高地公园工厂实施，最初将Model T的组装时间从12小时以上大幅缩短至3小时以下，最终缩短至93分钟。这是通过沿150英尺长的底盘线布置140名装配工，并将工作送到他们面前来实现的。

文章强调，装配线并非单一的发明，而是由多种因素推动的演变：满足Model T的需求、借鉴其他行业的实践（肉类包装、邮购和罐头）以及电动工具和输送机的可用性。

克拉伦斯·艾弗里和查尔斯·索伦森等关键人物因他们在实验和实施中的作用而受到重视。索伦森作为福特的生产主管，负责监督架空输送机的安装和整个流程的改进，而艾弗里通常被认为是第一个提出移动生产线概念的人。

文章还驳斥了亨利·福特是唯一发明者的神话，并将功劳归于一个被鼓励进行实验和创新的才华横溢的团队。它进一步强调了由于福特反对专利，因此该流程没有获得专利。

装配线的成功导致Model T的产量激增和价格下降。文章最后总结了三个关键教训：聘用有才华的人并让他们进行实验，借鉴其他行业的最佳实践，以及开发和实施最先进的技术。

---

## 28. 近四分之三的Oracle Java用户表示，他们在过去三年中曾接受过审计。

**原文标题**: Nearly 3 out of 4 Oracle Java users say they've been audited in the past 3 years

**原文链接**: [https://www.theregister.com/2025/07/15/oracle_java_users_audited/](https://www.theregister.com/2025/07/15/oracle_java_users_audited/)

最新调查显示，由于成本上涨和许可复杂，Oracle Java用户面临越来越多的审计，并正在迁移到开源替代方案。该调查由Dimensional Research进行，并由ITAM Forum和Azul委托进行，发现73%的Oracle Java用户在过去三年中接受过审计。为了应对Oracle的许可变更，包括2023年转向按员工定价，近80%的用户已经迁移或计划迁移到开源Java。

Oracle的Java许可政策，包括2020年至2023年间的四次变更，要求用户每三年升级到最新版本以获得免费支持，这促使许多人考虑开源选项。调查强调了这些审计的成本，54%的参与者每年花费超过10万美元来解决不合规问题，27%的参与者花费超过50万美元。

现代软件许可的复杂性以及在各种环境中跟踪应用程序使用的困难被认为是主要挑战。ITAM专业人士强调需要增加资源和管理层支持，以有效管理软件合规性并避免高额罚款。只有一小部分（14%）的Oracle Java用户打算继续使用该供应商的订阅模式，这标志着Java领域发生了重大转变。

---

## 29. 过渡到为 Android 应用和游戏使用 16 KB 页面大小

**原文标题**: Transition to using 16 KB page sizes for Android apps and games

**原文链接**: [https://android-developers.googleblog.com/2025/07/transition-to-16-kb-page-sizes-android-apps-games-android-studio.html](https://android-developers.googleblog.com/2025/07/transition-to-16-kb-page-sizes-android-apps-games-android-studio.html)

Android开发者博客宣布：自2025年11月1日起，Android应用和游戏将过渡到16 KB内存页大小。 针对Android 15+并包含原生C/C++代码的新应用和应用更新，提交到Google Play时*必须*支持16 KB页大小。 仅使用Kotlin/Java的应用已经兼容。

此更改旨在提高性能，使用16 KB页大小的设备将获得性能提升，包括更快的应用启动时间、更长的电池续航时间和更快的相机启动速度。

使用原生C/C++代码的开发者必须重新编译，并可能需要调整代码以实现16 KB兼容性。 Android Studio提供了以下工具来帮助：

*   **APK Analyzer:** 识别原生库并评估16 KB兼容性。
*   **对齐检查:** 警告不兼容的库/APK。
*   **Lint:** 突出显示未进行16 KB对齐的原生库。
*   **Android Gradle插件 (AGP) 8.5.1+ 和 NDK r28+:** 自动启用16 KB对齐。

开发者应消除有关4 KB页大小的硬编码假设，并使用`getpagesize()`或`sysconf(_SC_PAGESIZE)`来动态确定页大小。

测试至关重要，Android Studio提供了一个16 KB模拟器目标。 运行Android 15 QPR1+的兼容设备还提供开发者选项，可以在页面大小之间切换以进行真机测试。

过渡到16 KB页面大小将带来更好的用户体验和性能更高的Android生态系统。

---

## 30. 神经操作系统：由神经网络驱动的操作系统

**原文标题**: NeuralOS: An operating system powered by neural networks

**原文链接**: [https://neural-os.com/](https://neural-os.com/)

NeuralOS：一个通过神经生成模型模拟操作系统的项目。其核心思想是利用神经网络，特别是RNN和扩散模型，来模拟操作系统界面的行为和外观。

该演示允许用户在一个蓝色框内与这个模拟操作系统进行交互。用户可以通过移动鼠标（进行交互）、点击（左键或右键）以及使用键盘打字来控制模拟。"采样步数"设置允许调整模拟的质量和速度，提供了一种权衡。"使用RNN"开关可以在驱动模拟的不同生成模型（RNN或扩散模型）之间切换。"自动输入"会在短暂的空闲期后自动生成帧，在没有直接用户输入的情况下展示操作系统运行。该系统旨在提供一个由人工智能生成的操作系统，并具有逼真的交互体验。该项目的代码可以匿名获取。它包括保持连接以防止超时和刷新模拟的功能。

---

## 31. VMware Workstation：将虚拟化引入x86架构 (2012) [pdf]

**原文标题**: VMware Workstation: Bringing Virtualization to the x86 Architecture (2012) [pdf]

**原文链接**: [https://www.cse.iitb.ac.in/~mythili/virtcc/papers/vmware.pdf](https://www.cse.iitb.ac.in/~mythili/virtcc/papers/vmware.pdf)

无法提供所提供内容的摘要。该文本是一个二进制PDF文件，并非人类可读的文本。虽然标题表明该文档是关于“VMware Workstation: 将虚拟化引入x86架构 (2012)”，但内容已编码，无法解释以提取有关VMware Workstation或虚拟化的信息。

---

## 32. Replicube: 3D着色器解谜游戏，在线演示

**原文标题**: Replicube: 3D shader puzzle game, online demo

**原文链接**: [https://replicube.xyz/staging/](https://replicube.xyz/staging/)

此内容介绍3D着色器解谜游戏“Replicube”。由于您的浏览器不支持 canvas 标签和 JavaScript，无法运行在线演示。因此，您无法体验该内容。

---

## 33. DEWLine博物馆 – 遥远早期预警雷达线

**原文标题**: DEWLine Museum – The Distant Early Warning Radar Line

**原文链接**: [https://dewlinemuseum.com/](https://dewlinemuseum.com/)

本文简要介绍了DEWLine博物馆，据推测该馆致力于展示远程预警雷达线。重点介绍了自封馆长布莱恩·(西蒙)·杰弗里。布莱恩在1960年至1963年期间曾在DEWLine担任雷达技师。他在DEWLine的经历让他对该项目产生了持久的热情。文章还提到，点击地球图标即可获取布莱恩关于他在DEWLine服役的个人轶事和经历。总之，本文是对该博物馆及其馆长的简短介绍，让人们得以窥见他与DEWLine的个人联系。

---

## 34. 我破解了关于一次奇迹般沉船幸存者的百年谜团

**原文标题**: I Solved the Century-Old Mystery of a Miraculous Shipwreck Survivor

**原文链接**: [https://thewalrus.ca/empress-of-ireland-survivor-mystery/](https://thewalrus.ca/empress-of-ireland-survivor-mystery/)

伊芙·拉扎勒斯的文章详细介绍了她对戈登·查尔斯·戴维森故事的调查，戴维森是1914年爱尔兰皇后号沉船事件的幸存者。爱尔兰皇后号是加拿大太平洋铁路公司的一艘船只，与斯托斯塔德号相撞后沉没，夺走的生命比泰坦尼克号还多，但由于其乘客主要是普通的加拿大人，而不是富裕的精英，因此在很大程度上被遗忘了。

拉扎勒斯受休·韦里耶雇佣，韦里耶对戴维森据称奇迹般地游了六公里到岸边的故事着迷，专家认为这是不可能的。韦里耶想验证这一反复声称背后的真相。

拉扎勒斯的研究发现，戴维森是一名博士生，正在进行一次研究旅行。她找到了戴维森的家人和一份至关重要的报纸剪报，上面记载了他自己对这场灾难的描述。这表明，温哥华省报最初报道他游到岸边的说法是记者捏造的。戴维森实际上是被救生艇救起并送往斯托斯塔德号而幸存下来的。

文章还提供了关于皇后号最后一次航行以及导致其沉没事件的背景信息。雾和斯托斯塔德号的加固船体导致了迅速的洪水和人员伤亡。皇后号在短短十四分钟内沉没。

文章最后解释了为什么皇后号悲剧从公众记忆中消失：第一次世界大战的爆发使这一事件黯然失色，许多幸存者，包括戴维森，不久之后就面临着战争的恐怖。拉扎勒斯的调查揭穿了戴维森英勇游泳的神话，揭示了一个多世纪以来一直存在的虚假信息。

---

## 35. AWS Lambda 静默崩溃 – 平台故障，非应用缺陷 [pdf]

**原文标题**: AWS Lambda Silent Crash – A Platform Failure, Not an Application Bug [pdf]

**原文链接**: [https://lyons-den.com/whitepapers/aws-lambda-silent-crash.pdf](https://lyons-den.com/whitepapers/aws-lambda-silent-crash.pdf)

题为“AWS Lambda静默崩溃 – 平台故障，而非应用程序错误”的文档，看起来像是PDF文件的原始数据，而不是一篇可读的文章。其内容由PDF语法和编码数据组成，PDF阅读器会解析这些数据以显示实际文档。因此，我无法总结这篇所谓*文章的内容*。然而，仅根据*标题*，我们可以推断出其主题是：

该标题表明该文档讨论了由于AWS平台本身的底层问题，而非应用程序代码中的错误，导致AWS Lambda函数意外终止（“静默崩溃”）的情况。它暗示该文档旨在帮助读者在对Lambda函数崩溃进行故障排除时，区分应用程序层面的故障和平台层面的故障。理解这种区别对于在使用AWS Lambda的无服务器架构中进行高效调试和问题解决至关重要。

---

## 36. 快速词法分析器的策略

**原文标题**: Strategies for Fast Lexers

**原文链接**: [https://xnacly.me/posts/2025/fast-lexer-strategies/](https://xnacly.me/posts/2025/fast-lexer-strategies/)

创建快速词法分析器的策略：以 purple-garden 语言项目为例

---

## 37. 比利时CVD深度瓦解

**原文标题**: Belgian CVD is deeply broken

**原文链接**: [https://devae.re/posts/belgian-cvd-is-deeply-broken/](https://devae.re/posts/belgian-cvd-is-deeply-broken/)

研究人员报告KBC银行eBanking登录系统漏洞受挫记：比利时CVD体系的崩溃

---

## 38. 构建模块化Rails应用：深入探索Rails引擎

**原文标题**: Building Modular Rails Applications: A Deep Dive into Rails Engines

**原文链接**: [https://www.panasiti.me/blog/modular-rails-applications-rails-engines-active-storage-dashboard/](https://www.panasiti.me/blog/modular-rails-applications-rails-engines-active-storage-dashboard/)

本文提倡使用 Rails 引擎，并以作者构建 "Active Storage Dashboard" gem 的经验为例。该 Dashboard 通过提供用户友好的界面来监控和管理存储的文件，从而解决 Rails 应用程序中使用 Active Storage 时常见的的文件管理问题。

作者强调 Rails 引擎是模块化、可重用的组件，其功能类似于大型宿主应用程序中的小型 Rails 应用程序。它们具有快速功能开发、代码可重用性、逐步分解单体应用以及开源贡献机会等优点。

文章随后深入探讨了 Rails 引擎的结构，重点介绍了 `engine.rb` 文件以及使用 `isolate_namespace` 进行命名空间隔离以防止冲突的重要性。它详细介绍了 Active Storage Dashboard 的关键设计决策和实施策略，包括路由和 URL 生成、灵活的身份验证策略（基于控制器和路由级别）、跨 Rails 版本兼容性、“零外部依赖”理念、数据库无关的实现、高效分页、智能文件预览处理以及用于维护的有用 Rake 任务。

文章最后总结了引擎开发的最佳实践，强调命名空间隔离、提供配置选项以及考虑版本兼容性，以便在 Rails 生态系统中创建真正可重用且有价值的组件。

---

## 39. C++协程高级：将std::future转换为asio::awaitable

**原文标题**: C++ Coroutines Advanced: Converting std:future to asio:awaitable

**原文链接**: [https://www.ddhigh.com/en/2025/07/15/cpp-coroutine-future-to-awaitable/](https://www.ddhigh.com/en/2025/07/15/cpp-coroutine-future-to-awaitable/)

本文详细介绍了一种将`std::future<T>`转换为`asio::awaitable<T>`的方法，以便在C++中与asio协程无缝集成，从而解决处理来自第三方库的异步操作或潜在阻塞任务而不阻塞IO线程的难题。

核心解决方案利用`asio::async_initiate`和一个专用的`asio::thread_pool`在单独的线程中执行`std::future.get()`调用，以防止IO线程阻塞。异常处理使用`std::tuple<std::optional<T>, std::exception_ptr>`实现，以捕获正常结果和异常，从而确保全面的错误管理。至关重要的是，本文强调了通过使用`asio::get_associated_executor`和`asio::post`来保持asio执行器上下文的重要性，以确保最终处理程序调用在正确的上下文中发生。

本文提供了示例代码，演示了该转换在数据库查询和错误处理场景中的用法。它强调了这种方法的优点，包括无缝协程集成、编译时类型安全、性能优化和线程安全。它适用于数据库操作、文件I/O、集成第三方库和处理CPU密集型任务等场景。作者总结说，这种方法为现代C++异步编程提供了一种高效而稳健的解决方案。

---

## 40. 鲜为人知的微软程序或使国防部暴露于黑客攻击之下

**原文标题**: A Little-Known Microsoft Program Could Expose the Defense Department to Hackers

**原文链接**: [https://www.propublica.org/article/microsoft-digital-escorts-pentagon-defense-department-china-hackers](https://www.propublica.org/article/microsoft-digital-escorts-pentagon-defense-department-china-hackers)

ProPublica调查显示，微软利用一个鲜为人知的“数字护卫”项目来维护国防部的计算机系统，可能使敏感数据暴露给中国黑客。这项安排对微软的联邦云计算业务至关重要，它依赖于持有安全许可的美国公民（即护卫）来监督在中国和其他地方的工程师。

核心问题是，这些护卫通常缺乏足够的技术专业知识来充分监控外国工程师，而这些工程师可能拥有更先进的技能。这造成了一种漏洞，可能导致恶意代码在未被发现的情况下被引入。尽管包括一位微软网络安全负责人等人在内的许多人发出了警告，但该公司据称扩大了该项目。

前政府官员和国家安全专家对此表示惊讶和担忧，强调了中国积极的网络威胁。该系统处理敏感但未分类的信息，包括对生命保护和金融安全至关重要的数据。专家表示，如果中国工程师植入恶意代码，护卫们将一无所知。

微软坚称其流程符合美国政府的要求，并且外国员工无法直接访问客户数据。他们强调了对护卫的培训以及名为“Lockbox”的内部审查流程。然而，文章强调护卫可能无法检测到恶意代码。

数字护卫系统的出现源于满足处理敏感数据的严格美国公民要求，同时利用微软全球劳动力的挑战。一位前微软经理将其描述为“阻力最小的路径”，并认为这是在成本更高的替代方案中做出的选择。

---

## 41. RFC：PHP 许可证更新

**原文标题**: RFC: PHP license update

**原文链接**: [https://wiki.php.net/rfc/php_license_update](https://wiki.php.net/rfc/php_license_update)

此RFC提议更新PHP许可证，参照软件数据包交换(SPDX)定义的“BSD 3条款'新'或'修订'许可证”。该许可证是一种宽松的开源许可证，允许用户自由使用、修改和分发该软件，甚至在专有应用程序中。

BSD 3条款许可证的关键特性包括：

*   **使用、修改和分发许可：** 用户被授予广泛的权限，可以以源代码或二进制形式使用、修改和分发该软件。
*   **署名

RFC参考SPDX定义，旨在确保关于提议用于PHP的BSD 3条款许可证的具体条款的清晰性和一致性。此次更新旨在确保PHP许可证保持开放和宽松，从而允许广泛采用该语言并为其做出贡献。

---

## 42. 在 Apache Parquet 中嵌入用户自定义索引

**原文标题**: Embedding user-defined indexes in Apache Parquet

**原文链接**: [https://datafusion.apache.org/blog/2025/07/14/user-defined-parquet-indexes/](https://datafusion.apache.org/blog/2025/07/14/user-defined-parquet-indexes/)

本文演示了如何在不破坏与标准Parquet读取器兼容性的前提下，将用户自定义索引嵌入到Apache Parquet文件中。其核心思想是利用Parquet的页脚元数据和基于偏移量的寻址方式，将索引数据存储在文件主体中，并在页脚中以键/值对的形式记录其位置。

作者认为，这种方法在外部索引的优势（提高查询性能）和Parquet格式的简单性之间取得了平衡，避免了外部索引的缺点，如增加复杂性和同步风险。

本文提供了一个具体的例子，将“唯一值索引”（特定列的一组唯一值）嵌入到Parquet文件中。该索引可用于在查询执行期间高效地修剪文件，跳过那些不包含相关值的文件。该示例演示了如何将索引序列化为二进制格式，将其写入文件主体，在页脚中记录其位置，然后扩展Apache DataFusion的TableProvider以读取和利用该索引进行文件级修剪。

文章强调了这种方法的优势：标准Parquet读取器将简单地忽略未知的索引字节和键/值元数据，而了解自定义索引的引擎可以利用它来实现更快的查询执行。这种方法允许各种索引类型和粒度，从而可以优化文件级、行组级甚至行级的数据访问。

---

## 43. 日本祖父母为孙辈制作等比例龙猫巴士站 (2020)

**原文标题**: Japanese grandparents create life-size Totoro with bus stop for grandkids (2020)

**原文链接**: [https://mymodernmet.com/totoro-sculpture-bus-stop/](https://mymodernmet.com/totoro-sculpture-bus-stop/)

在日本宫崎县高原町，一对70多岁的夫妇为他们的孙子们制作了一个真人大小的龙猫雕像，还配有一个巴士站。受到吉卜力工作室电影《龙猫》中标志性场景的启发，这对祖父母用传统的粉刷技术、水泥、砖块和精心的雕刻，一丝不苟地建造了这个雕像。

这个项目包括建造一个桶状框架，分层浇筑水泥，添加砖块以达到龙猫的丰满形状，并雕刻出角色独特的特征，如眼睛和胡须。他们还建造了一条砖石小路，并设置了巴士站牌。

这个雕像已经成为当地的景点，吸引了来自各地的龙猫粉丝。这对夫妇甚至提供了一把红伞，类似于电影中的那把，供游客在照片中使用。龙猫雕像不仅给他们的孙子们带来了欢乐，也给全球的龙猫爱好者带来了欢乐，使这个小镇成为观光和怀旧的目的地。

---

## 44. 量子力学的世纪

**原文标题**: A Century of Quantum Mechanics

**原文链接**: [https://home.cern/news/news/physics/century-quantum-mechanics](https://home.cern/news/news/physics/century-quantum-mechanics)

本文纪念维尔纳·海森堡1925年7月9日致沃尔夫冈·泡利的关键信件一百周年，这标志着量子力学发展的一个转折点。这封信揭示了海森堡彻底摒弃电子经典轨道概念，并用纯粹基于可观测实验数据的模型取而代之的激进努力。这种方法促成了他具有开创性的“重新诠释”论文，该论文被认为是现代量子理论的出生证明。

本文强调，海森堡的初步工作，经由玻恩、约旦和泡利的进一步发展，演变为矩阵力学，这是量子理论的第一个成熟表述，也是粒子物理标准模型的基础，该模型在欧洲核子研究中心的实验中一直被证明是准确的。

对这个周年纪念日的庆祝活动促使人们反思量子力学的影响，包括其持续存在的挑战、实验创新和技术进步。量子传感器正在扩展到高能应用领域，并且正在探索量子模拟，以克服经典计算在复杂系统建模中的局限性。

尽管量子力学在经验上取得了成功，但本文指出，关于该理论真正含义的基本问题仍然没有得到解答，这引发了关于经典世界涌现、波函数性质以及观察者作用的理论和哲学辩论。海森堡对未来物理学家将进一步解开这些谜团的乐观情绪继续推动着该领域的研究。

---

## 45. 闪电探测器电路

**原文标题**: Lightning Detector Circuits

**原文链接**: [https://techlib.com/electronics/lightningnew.htm](https://techlib.com/electronics/lightningnew.htm)

本文详细介绍了各种雷电探测器电路，主要面向业余爱好者和初学者。首先介绍了一个简单易懂的入门级设计，该设计采用工作频率接近 200 kHz 的调谐电感电路，并结合高输入阻抗达林顿晶体管射频放大器以提高灵敏度。该电路采用微功率设计，从电池中汲取的电流极小。一个关键优势是无需抽头调谐电路。

然后，本文探讨了其他替代设计，包括：

*   **磁性天线版本：** 采用调谐至约 5 kHz 的螺线管式电感器，对远处闪电具有更高的灵敏度，但对某些局部脉冲源的灵敏度降低。
*   **复合晶体管电路：** 用复合晶体管配置取代达林顿晶体管，适用于 CA3096 晶体管阵列。
*   **运算放大器版本：** 使用微功率运算放大器来整流更多的闪电脉冲，从而延长闪光持续时间。但是，此版本容易受到家用电器引起的错误触发，因此不建议常规使用。

通篇，作者都提供了关于元件选择、构建技术和故障排除的实用建议。本文强调视觉清晰度，配有特写照片，并强调理解原理图作为电气连接而非机械布局的重要性。最后，文章以运算放大器版本的一个实际应用结尾，使用它来触发一个大型 LED 闪电灯，以产生视觉效果。

---

## 46. 无损浮点图像压缩

**原文标题**: Lossless Float Image Compression

**原文链接**: [https://aras-p.info/blog/2025/07/08/Lossless-Float-Image-Compression/](https://aras-p.info/blog/2025/07/08/Lossless-Float-Image-Compression/)

本文研究了浮点图像的无损压缩方法，特别是电影合成中使用的多层图像。作者比较了OpenEXR（使用ZIP和即将推出的HTJ2K压缩）、JPEG-XL和一个自定义的“MOP”（网格优化器 + zstd）解决方案。

主要发现：

*   **OpenEXR ZIP：** 良好的基线，也是作者推荐的默认选项。
*   **OpenEXR HTJ2K：** 提供了略优于ZIP的压缩率，但压缩和解压缩性能明显降低。未来在性能和多层优化方面可能有所改进。
*   **JPEG-XL：** 可以实现比OpenEXR更好的压缩率，尤其是在更高的压缩强度下，但压缩和解压缩速度明显较慢。作者认为JPEG-XL目前不太适合多层浮点图像，更适合于可显示图像。
*   **MOP（网格优化器 + zstd）：** 表现出色。仅网格优化器就能提供与EXR HTJ2K相当的压缩，且速度更快。与zstd结合使用时，MOP实现了与高强度JPEG-XL相似的压缩率，但压缩和解压缩速度要快得多。作者认为这是内部无损浮点图像压缩的强大选择。

作者总结说，虽然JPEG-XL具有潜力，但OpenEXR ZIP仍然是一个可靠的选择，并且自定义的MOP解决方案由于其速度和压缩率优势，为内部使用提供了一个引人注目的替代方案。文章还指出，测试是在有限的数据集上进行的，并鼓励进一步探索，尤其是在有损压缩方面。

---

## 47. SCP-055是一种“反模因”，它会在被观察时从记忆中抹除自身。

**原文标题**: SCP-055 is an "antimeme" – it erases itself from memory when observed

**原文链接**: [https://scp-wiki.wikidot.com/scp-055](https://scp-wiki.wikidot.com/scp-055)

SCP-055是一个Keter级SCP项目，被归类为“反模因”，意指会在观察后从记忆中抹除自身。其收容措施是在19号站点的安全水泥房间内，安装法拉第笼，但其建造原因和收容程序均未知。

尽管人员能够观察、拍摄和记录SCP-055，但所有关于其物理外观、性质、行为和起源的细节都会立即被遗忘。这包括SCP基金会获取它的情况。出于未知原因，研究或摧毁SCP-055的尝试均告失败。其潜在威胁等级被认为很高，可能涉及身体伤害，或者更确定的是，模因/精神危险。

分析表明SCP-055可能是一个自主或远程控制的特工，可能正在观察或干预基金会、人类或其他SCP项目。一位研究人员发现，虽然该物体本身无法被记住，但关于它的否定陈述是可以的。例如，人员可以记住“SCP-055不是球形的”，从而使他们能够反复推断出它的存在。调查团队经历了这种记住和忘记的循环带来的痛苦，但长期影响很小。建议包括将能够记住SCP-055的工作人员分配到关键站点。

---

## 48. 美国食品药品监督管理局的崩溃

**原文标题**: The Collapse of the FDA

**原文链接**: [https://www.nytimes.com/2025/07/08/magazine/fda-collapse-rfk-kennedy.html](https://www.nytimes.com/2025/07/08/magazine/fda-collapse-rfk-kennedy.html)

无法访问文章链接。

---

## 49. 将光伏太阳能系统添加到内燃机车辆的影响

**原文标题**: Impacts of adding PV solar system to internal combustion engine vehicles

**原文链接**: [https://www.jstor.org/stable/26169128](https://www.jstor.org/stable/26169128)

无法访问文章链接。

---

## 50. Django二十岁生日快乐

**原文标题**: Happy 20th Birthday, Django

**原文链接**: [https://www.djangoproject.com/weblog/2025/jul/13/happy-20th-birthday-django/](https://www.djangoproject.com/weblog/2025/jul/13/happy-20th-birthday-django/)

本文庆祝Django于2025年7月13日迎来20岁生日，纪念其首次公开提交二十周年。作者Thibaud Colas和Benjamin Balder Bach邀请社区通过专门网站参与庆祝活动，该网站展示全球活动和机会。

庆祝活动包括承诺提供蛋糕、Django知识问答以及社区成就展示。生日庆祝活动的一个重要方面是为Django软件基金会筹款。目标是在未来20天内获得200位新的捐赠者，每人捐赠20美元或以上，其中至少20人成为每月捐赠者。可以通过Django网站、GitHub赞助商或成为企业会员进行捐赠。鼓励捐赠者使用#DjangoBirthday并在社交媒体上标记Django官方账号来分享他们的支持。

截至2025年7月13日，Django软件基金会已筹集到其年度30万美元目标的25.6%（76,707美元）。展望未来，本文强调致力于将Django维护为一个蓬勃发展的Web框架，并承诺在未来多年继续发布版本、保持强大的生态系统和提供支持性的社区。

---

## 51. 数据经纪人向美国海关与边境保护局和移民及海关执法局出售航班信息

**原文标题**: Data brokers are selling flight information to CBP and ICE

**原文链接**: [https://www.eff.org/deeplinks/2025/07/data-brokers-are-selling-your-flight-information-cbp-and-ice](https://www.eff.org/deeplinks/2025/07/data-brokers-are-selling-your-flight-information-cbp-and-ice)

本文揭露了数据经纪商向美国海关与边境保护局（CBP）和移民及海关执法局（ICE）出售敏感航班信息的令人担忧的做法。由主要航空公司拥有和运营的航空公司报告公司（ARC）收集并向CBP和ICE出售乘客数据，包括姓名、航班行程和财务详细信息，绕过搜查令要求，并可能隐藏信息来源。

ARC的旅行情报计划（TIP）拥有超过十亿条旅行记录，引发了人们对执法部门加强监控和潜在滥用的担忧，尤其是在当前移民执法力度加强的背景下。本文强调，航空公司通过ARC，正在通过出售这些敏感数据将利润置于旅客隐私之上。

本文认为，这种做法助长了一种渐趋专制的氛围，政府可以根据国籍、宗教或政治背景追踪并可能针对个人。它还指出了与数据经纪商向执法机构出售位置数据、互联网数据和公用事业记录相关的更广泛的隐私问题。

本文最后呼吁制定“隐私优先”立法，要求对数据处理进行同意，通过“第四修正案不得出售”法案，以防止执法部门在未经司法审查的情况下购买数据，并强制执行数据经纪商注册法。其目标是保护个人隐私，并防止政府利用数据经纪商规避宪法保障。

---

## 52. Cidco MailStation 作为 Z80 开发平台 (2019)

**原文标题**: Cidco MailStation as a Z80 Development Platform (2019)

**原文链接**: [https://jcs.org/2019/05/03/mailstation](https://jcs.org/2019/05/03/mailstation)

本文详细介绍了作者将 Cidco MailStation（一种2000年代的专用电子邮件终端）改造为 Z80 开发平台的历程。MailStation 拥有 Z80 处理器、LCD、键盘和调制解调器，为复古计算爱好者提供了独特的机会。

作者概述了 MailStation 的硬件规格，包括其 Z80 处理器、RAM、闪存、调制解调器、LCD 和键盘。一个关键挑战是 Z80 有限的地址空间，需要内存分页才能访问额外的内存。

可以通过利用 MailStation 的“Clipmail”功能或使用内置的十六进制编辑器来加载自定义代码。作者详细介绍了一个加载程序，该程序通过并行端口使用 LapLink 电缆和代理计算机（后来被 USB 和 WiFi 加载器取代）上传，从而简化了代码注入。

开发环境包括一台运行 OpenBSD 的笔记本电脑，使用 SDCC 编译 C 语言和 Z80 汇编代码。作者强调需要重新实现 MailStation 特定的 LCD 和键盘功能，并创建自定义工具，因为原始开发工具已经过时。

文章重点介绍了对 MailStation 固件进行逆向工程的努力，指出了挑战以及最终转向重新实现必要功能的转变。

主要项目是“msTERM”，一个终端程序，使 MailStation 能够使用其内部调制解调器或并行连接连接到 BBS。这涉及到创建自定义的 putchar 和 getchar 例程、ANSI 转义码解析器以及用于调制解调器通信的中断服务例程。

作者已经发布了 msTERM 代码并鼓励合作，旨在使 MailStation 成为一个更加通用的平台。进一步的项目包括 USB 和 Wifi 加载器，以及一个示例项目，从而简化其他人的 MailStation 开发。

---

## 53. 缓存基准测试

**原文标题**: Cache Benchmarks

**原文链接**: [https://github.com/tidwall/cache-benchmarks](https://github.com/tidwall/cache-benchmarks)

本文档描述了Memcache、Redis、Valkey、Dragonfly和Garnet的缓存基准测试结果。基准测试重点关注吞吐量、延迟（以各种百分位数和绝对最大值衡量）和CPU周期。持久化已禁用，所有连接均为本地UNIX管道。

基准测试是在AWS c8g.8xlarge（32核ARM64）实例上使用`memtier_benchmark`进行的。管道化测试的规模为1、10、25和50。每个基准测试包含31次运行，中位数结果用于在对数尺度上绘图。

每个缓存服务器实例使用`taskset`专用于16个核心，而基准测试工具使用剩余的16个核心。基准测试工具使用256个客户端，均匀分布在16个线程之间，每个线程执行10万次SET和10万次GET操作。预热阶段（不包含在测量中）在缓存服务器启动后执行SET操作的空运行。

本文档还列出了每个缓存软件的版本：Memcached (1.6.38)、Redis (8.0.2)、Valkey (8.1.1)、Dragonfly (1.30.3)和Garnet (1.0.65)。

文档记录了每个缓存服务器的I/O线程配置，包括用于配置其线程池的命令行标志。由`./bench-all.sh`脚本生成的结果存储在`results`目录中，大约需要两周时间才能完成。文档概述了结果的结构，其中包含每个管道大小的吞吐量、延迟和CPU周期部分。

---

## 54. 两个家伙讨厌康卡斯特，于是他们自己建了光纤ISP。

**原文标题**: Two guys hated using Comcast, so they built their own fiber ISP

**原文链接**: [https://arstechnica.com/tech-policy/2025/07/two-guys-hated-using-comcast-so-they-built-their-own-fiber-isp/](https://arstechnica.com/tech-policy/2025/07/two-guys-hated-using-comcast-so-they-built-their-own-fiber-isp/)

塞缪尔·赫尔曼和亚历山大·巴丘对康卡斯特的有线宽带感到不满，于是他们在密歇根州塞林市创立了自己的光纤ISP，名为Prime-One。他们的动机是当地上传速度慢、服务不可靠以及缺乏其他选择。凭借他们在ISP建设方面的经验，他们建立了一个地下光纤网络，目前为1500户家庭中的约100个客户提供服务，每月收费80美元，提供对称千兆互联网，以及其他速度等级、无限流量且无需签订合同。

Prime-One通过本地客户服务、快速维修以及停电补偿和透明的定价来区分自己。他们的竞争对手主要是康卡斯特和Frontier的DSL。另一位密歇根州居民贾里德·毛奇也为他们提供了建议，贾里德·毛奇也建立了自己的光纤ISP。Prime-One最初专注于单户住宅，但计划扩展到多单元建筑和附近城镇，更大的扩张计划尚未公开。康卡斯特已做出回应，升级了其网络并提供具有无限流量的新套餐。

---

## 55. 美国国税局正建立一套与移民及海关执法局共享纳税人数据的系统

**原文标题**: The IRS Is Building a System to Share Taxpayers' Data with ICE

**原文链接**: [https://www.propublica.org/article/trump-irs-share-tax-records-ice-dhs-deportations](https://www.propublica.org/article/trump-irs-share-tax-records-ice-dhs-deportations)

2025年7月，ProPublica报道称，特朗普政府领导下的美国国税局正在开发一套计算机系统，与美国移民及海关执法局（ICE）共享纳税人数据，从而实现大规模驱逐出境。该系统将通过“按需”流程，赋予ICE前所未有的权限，获取他们想要驱逐出境的个人的家庭住址。

该计划遭遇了内部阻力，国税局代理总法律顾问安德鲁·德梅洛因法律方面的担忧拒绝发布数百万个地址，最终遭到解雇。包括前国税局官员和隐私专家在内的批评人士担心，该系统侵犯了纳税人的隐私法，并可能导致使用不正确的地址，从而针对无辜的人。

该蓝图显示了一个自动化系统，国土安全部提交姓名和先前地址的电子表格，国税局则返回存档中的最新地址。专家们担心由于使用姓名匹配而非纳税人识别号码，以及缺乏对国土安全部要求的独立验证，可能出现错误。

白宫为该系统辩护，称其合法且履行了特朗普大规模驱逐出境的竞选承诺。然而，人们仍然担心将协议扩展到包括美国公民的数据。该文章还强调了埃隆·马斯克的 DOGE 的影响力，他重组了国税局的工程人员，并领导了创建主数据库的工作。参议员罗恩·怀登批评该系统容易被滥用，允许对国税局记录进行“钓鱼式搜索”。

---

## 56. Anthropic、Google、OpenAI和XAI获国防部高达2亿美元拨款

**原文标题**: Anthropic, Google, OpenAI and XAI Granted Up to $200M from Defense Department

**原文链接**: [https://www.cnbc.com/2025/07/14/anthropic-google-openai-xai-granted-up-to-200-million-from-dod.html](https://www.cnbc.com/2025/07/14/anthropic-google-openai-xai-granted-up-to-200-million-from-dod.html)

美国国防部（DoD）将向AI公司Anthropic、谷歌、OpenAI和xAI授予高达2亿美元的合同，以加速该机构为国家安全目的采用人工智能。国防部首席数字和人工智能办公室（CDAO）表示，这些奖项将有助于开发先进的人工智能能力，以应对各个任务领域中关键的国家安全挑战。

据国防部称，引入人工智能将增强其支持作战人员和保持对敌战略优势的能力。

值得注意的是，埃隆·马斯克的xAI宣布推出“Grok for Government”，这是一套为美国政府客户量身定制并通过美国总务管理局（GSA）时间表访问的人工智能模型。此前，Grok因生成冒犯性内容而备受争议。OpenAI此前于2024年获得国防部2亿美元的合同，并已推出OpenAI for Government。

---

## 57. 展示HN：HTML迷宫 – 逃离一个用HTML页面构建的诡异迷宫

**原文标题**: Show HN: The HTML Maze – Escape an eerie labyrinth built with HTML pages

**原文链接**: [https://htmlmaze.com/](https://htmlmaze.com/)

HTML迷宫

---

## 58. Clang：-Wexperimental-lifetime-safety：实验性C++生命周期安全分析

**原文标题**: Clang: -Wexperimental-lifetime-safety: Experimental C++ Lifetime Safety Analysis

**原文链接**: [https://github.com/llvm/llvm-project/commit/3076794e924f](https://github.com/llvm/llvm-project/commit/3076794e924f)

本文介绍了 Clang 中实验性的 C++ 生命周期安全分析，该分析通过 `-Wexperimental-lifetime-safety` 标志启用。该分析旨在利用“来源”和“借用”的概念来跟踪指针的生命周期，从而检测诸如释放后使用和悬空指针之类的生命周期违规行为。

更改包括：

*   一个新的头文件 `LifetimeSafety.h`，它定义了数据流分析的入口点 `runLifetimeSafetyAnalysis`。此函数接受一个 `DeclContext`、一个 `CFG`（控制流图）和一个 `AnalysisDeclContext` 作为输入。
*   一个新的诊断组 `LifetimeSafety` 被添加到 `DiagnosticGroups.td` 中，用于对相关警告进行分组。
*   一个虚拟警告 `warn_experimental_lifetime_safety_dummy_warning` 被添加到 `DiagnosticSemaKinds.td` 的 `LifetimeSafety` 组中。这旨在作为一个占位符，将被实际的生命周期安全警告所取代。
*   一个新的源文件 `LifetimeSafety.cpp` 被添加到 `CMakeLists.txt` 中的 `clangAnalysis` 库。
*   两个与分析和测试相关的附加文件。

该分析基于 RFC，可在 [https://discourse.llvm.org/t/rfc-intra-procedural-lifetime-analysis-in-clang/8629](https://discourse.llvm.org/t/rfc-intra-procedural-lifetime-analysis-in-clang/8629) 上获得。添加虚拟警告表明该分析处于早期阶段，真正的警告将在稍后实现。

---

## 59. 使用USB脚踏板进行共振编码

**原文标题**: Using a USB Foot Pedal for Vibe Coding

**原文链接**: [https://coding.napolux.com/using-a-usb-foot-pedal-for-vibe-coding/](https://coding.napolux.com/using-a-usb-foot-pedal-for-vibe-coding/)

本文提倡使用USB脚踏板作为提高编码效率的技巧，尤其是在使用GitHub Copilot等AI辅助编码工具的情况下。核心思想是将脚踏板映射到Tab键，使编码人员无需将手从键盘上移开即可接受自动完成建议。

作者将这个想法归功于一位朋友和一篇现有的Medium文章，然后解释了设置方法：连接一个USB脚踏板并将其配置为模拟Tab键。作者强调了几个好处，包括通过减少手部动作来提高效率、通过减少重复性劳损来改善人体工程学，以及带来更愉快、几乎如音乐般的编码体验。

本文提供了与Mac和Windows操作系统兼容的USB脚踏板示例（尽管Linux兼容性可能有所不同）。这些脚踏板可以自定义以模拟各种按键。

最终，作者将USB脚踏板定位为一项小投资，可以带来显著的生产力提升，并鼓励读者尝试这种“免手动”编码技术。文章以鼓励“氛围编码”结束，并提供联系方式以获取反馈或提出问题。

---

## 60. 千层面电池

**原文标题**: Lasagna Battery Cell

**原文链接**: [https://amazingribs.com/more-technique-and-science/more-cooking-science/reactive-pans/](https://amazingribs.com/more-technique-and-science/more-cooking-science/reactive-pans/)

AmazingRibs.com的文章警告，避免形成“千层面电池”，这是一种电偶腐蚀，当活性金属（如铝箔）与酸性食物（如番茄酱）在活性锅具（如钢锅）中接触时可能发生。

作者Meathead解释说，这种组合会形成一个小电池，酸充当电解质，不同的金属充当电极。这种电化学反应会腐蚀铝箔，产生孔洞，并可能用金属离子污染食物。

文章强调，这不仅会发生在千层面上，还会发生在腌料、盐水中，甚至在使用“德州拐杖”烧烤技术时，用铝箔包裹食物放在钢锅中也会发生。 热量会加速反应。

为了防止这种情况，作者和他的科学顾问Greg Blonder教授建议使用由玻璃、瓷器、珐琅或塑料（仅用于储存）制成的非反应性容器。对于烹饪，建议使用耐热玻璃烹饪千层面。 当使用德州拐杖时，建议使用塑料烤箱袋、牛皮纸或烘焙纸代替铝箔。 还建议使用绝缘烤架，如特氟龙或搪瓷涂层烤架。

一个电偶腐蚀的演示，其中连接到装有番茄酱和盐的钢制玛芬烤盘中的铝箔被腐蚀，展示了该反应的影响。

---

## 61. 展示一下：我做的可以实时多人在线的扫雷游戏

**原文标题**: Show HN: Minesweeper game I built to be real-time Multiplayer

**原文链接**: [https://www.minesweeperpro.com/?v=2.1](https://www.minesweeperpro.com/?v=2.1)

此“Show HN”帖子介绍一款实时多人扫雷游戏。重点功能包括：

*   **多人游戏：** 游戏向其他玩家开放，实现协作式扫雷体验。
*   **速度可变：** 玩家可以选择喜欢的游戏速度：休闲、快速或闪电。
*   **标准机制：** 游戏玩法包括点击/轻触清除单元格，以及右键单击/长按放置旗帜。
*   **积分系统：** 正确操作获得+1分，错误操作扣除3分。这强调了策略性玩法。
*   **奖励系统：** 分数转换为游戏内金币，最高分者获得2倍奖励。
*   **账号福利：** 登录后，玩家可以自定义名称、使用聊天功能并保留金币余额。

该帖子还描述了游戏的功能，包括计分规则和获胜参数。最后，它鼓励用户登录以增强他们的体验，包括自定义玩家名称、参与聊天以及保存游戏内收益。

---

## 62. 电子表格传奇人物米奇·卡普尔耗时45年终获麻省理工学院学位

**原文标题**: It took 45 years, but spreadsheet legend Mitch Kapor finally got his MIT degree

**原文链接**: [https://www.bostonglobe.com/2025/06/24/business/mitch-kapor-mit-degree-bill-aulet/](https://www.bostonglobe.com/2025/06/24/business/mitch-kapor-mit-degree-bill-aulet/)

莲花1-2-3的创始人米奇·卡普尔，在1979年初次离开麻省理工学院项目45年后，终于获得了该校的硕士学位。他重返校园的动力来自于他的朋友兼麻省理工学院教授比尔·奥莱特的一个友善玩笑，奥莱特邀请卡普尔在学校发表演讲。卡普尔当年离开麻省理工学院是为了抓住一个有利可图的机会，将其统计程序适配于VisiCalc。

在创立莲花公司并成为成功的科技企业家和投资者后，卡普尔与妻子发展出一种“弥合差距的投资”理念，专注于支持那些满足服务不足社区需求的企业。HealthSherpa和LendStreet等公司都受益于这种方法。

受奥莱特玩笑的启发，卡普尔决定完成学位所需的学业，其中包括独立研究和一篇论文。他的论文探讨了他的投资策略的根源和发展，强调了这种策略如何经常导致对来自边缘化群体的企业家的支持。卡普尔认为，这种多样性努力的方法在当前的政治气候下尤其具有现实意义。今年5月，74岁的卡普尔获得了学位，标志着一段漫长旅程的结束。

---

## 63. 六位游戏开发者对话电脑游戏杂志 (1984)

**原文标题**: Six Game Devs Speak to Computer Games Mag (1984)

**原文链接**: [https://computeradsfromthepast.substack.com/p/six-game-devs-speak-to-computer-games](https://computeradsfromthepast.substack.com/p/six-game-devs-speak-to-computer-games)

无法访问文章链接。

---

## 64. 奥洛维尔医生1908年的紧身胸衣X光片

**原文标题**: The Corset X-Rays of Dr Ludovic O'Followell (1908)

**原文链接**: [https://publicdomainreview.org/collection/the-corset-x-rays-of-dr-ludovic-o-followell-1908/](https://publicdomainreview.org/collection/the-corset-x-rays-of-dr-ludovic-o-followell-1908/)

维基共享资源上的文章《Ludovic O'Followell医生（1908年）的束身胸衣X光片》展示了Ludovic O'Followell医生于1908年拍摄的放射影像，揭示了束身胸衣对女性骨骼结构和内脏器官的影响。这些X光片直观地描绘了束身胸衣的束缚性及其可能导致肋骨、脊柱和腹部器官移位和变形的潜力。

这些图像的关键信息是长期穿着束身胸衣对身体产生的显著物理影响。图像突出了肋骨的压缩和重塑，下肋骨可能被向内推压，以及肝脏和胃等器官的移位。这为当时对束身胸衣健康后果的担忧提供了视觉证据。

这篇文章是20世纪初医学理解和社会对时尚态度的历史记录。它展示了技术（特别是X光）的不断发展，用于分析和批判束身胸衣等社会习俗。这些图像促进了围绕身体形象、时尚潮流以及与紧身服装相关的潜在健康危害的讨论。本质上，这些X光片有力地视觉呈现了那个时代女性身体所受到的限制。

---

## 65. 展示一下：十年如一日跑步，可视化呈现

**原文标题**: Show HN: Ten years of running every day, visualized

**原文链接**: [https://nodaysoff.run](https://nodaysoff.run)

阿德里安·弗里格里庆祝自2015年7月11日起每日跑步十周年，并通过数据可视化展示了他的旅程。他二十多岁开始跑步，最终致力于每日连跑，并已在七大洲、克服各种身体挑战和天气条件下坚持了下来。

他的数据包括：

*   **总体数据：** 跑步3658天，总计11942英里，1832小时，攀登219000英尺。
*   **值得注意的跑步：** 他前10次最长跑步的列表，最长的一次是2017年11月的33.67英里。
*   **年度里程：** 一张图表展示了他的年度里程，近年来由于工作和生活限制有所下降。
*   **按时间划分的锻炼活动：** 显示他主要是一名晨跑者。
*   **按日划分的平均每日里程：** 说明他过去常常在周六进行更长的跑步，最近更多地转向周三。
*   **跑步距离：** 一英里跑（“保持连跑”）变得更加频繁。
*   **跑步机与户外：** 他更喜欢户外跑步，但在必要时使用跑步机。
*   **配速分布：** 他指出他的轻松配速平均在9:30/英里左右。
*   **心率区间：** 大部分是120-140 bpm范围内的轻松跑。
*   **温度：** 他喜欢在40多度的环境中跑步。
*   **天气状况：** 他在各种天气条件下跑步。
*   **地理：** 他在包括七大洲在内的各个国家/地区跑步，其中大部分里程在美国。
*   **到访的美国州：** 他已在美国50个州中的18个州跑步。
*   **每日记录：** 日历可视化，显示了他过去十年来的每日跑步习惯。

他感谢妻子莫莉在他整个跑步旅程中的支持，并希望继续保持这一连跑十年。该项目使用各种开源工具和API构建。

---

## 66. 用于光标AI、涉嫌50万美元盗窃的代码高亮扩展

**原文标题**: Code highlighting extension for Cursor AI used for $500k theft

**原文链接**: [https://securelist.com/open-source-package-for-cursor-ai-turned-into-a-crypto-heist/116908/](https://securelist.com/open-source-package-for-cursor-ai-turned-into-a-crypto-heist/116908/)

一位区块链开发者因一款针对基于 Visual Studio Code 的 IDE Cursor AI 的恶意代码高亮扩展程序，损失了 50 万美元的加密资产。该扩展在 Open VSX 注册表中可用，伪装成 Solidity 代码的语法高亮器，已被下载超过 54,000 次。然而，它是一个假冒程序，不包含任何语法高亮功能，而是下载并执行恶意的 PowerShell 脚本。

由于 Open VSX 注册表的排名算法优先考虑时间新近度以及下载量等其他因素，该开发者被欺骗安装了该恶意扩展程序，因为它在搜索结果中的排名高于合法的扩展程序。PowerShell 脚本安装了 ScreenConnect（一款远程管理软件），使攻击者能够控制该开发者的计算机。

然后，攻击者使用 ScreenConnect 上传 VBScript，下载更多有效载荷，包括 Quasar 后门程序和一个窃取器，该窃取器从浏览器、电子邮件客户端和加密钱包中收集数据。这使得他们能够窃取该开发者的钱包密码短语并窃取加密货币。

在最初的恶意扩展程序被删除后，攻击者发布了另一个与合法扩展程序同名的假冒程序，并人为地增加了下载量。他们还对其他软件包采用了类似的策略，包括一个名为“solsafe”的 npm 软件包和几个 Visual Studio Code 扩展程序。本文强调了恶意开源软件包日益增长的威胁，并建议在下载工具时保持谨慎，验证其真实性，并使用安全解决方案。

---

## 67. 东亚气溶胶减排可能加剧全球变暖

**原文标题**: East Asian aerosol cleanup has likely contributed to global warming

**原文链接**: [https://www.nature.com/articles/s43247-025-02527-3](https://www.nature.com/articles/s43247-025-02527-3)

This article investigates the link between East Asian efforts to reduce air pollution and the acceleration of global surface warming since 2010. Using simulations from eight Earth System Models, the study demonstrates that a 75% reduction in East Asian sulfate emissions leads to a global annual mean warming of 0.07 ± 0.05 °C. This warming is attributed to the unmasking of greenhouse gas-driven warming previously offset by aerosols.

Key findings include a rapidly evolving global warming trend, warming in the North Pacific, and a top-of-atmosphere radiative imbalance, all consistent with recent observations. The study highlights that East Asian aerosol cleanup is likely a key contributor to both the recent acceleration in global warming rate and Pacific warming trends.

The simulations reveal robust changes in temperature and precipitation due to reduced East Asian aerosol emissions. While the strongest warming (~1°C) occurs near the source region, significant warming also extends to the North Pacific. The study acknowledges inter-model variability and the influence of internal variability, emphasizing the need for large ensemble simulations to accurately quantify climate impacts of regional emissions changes. The findings suggest that the recent efforts to improve air quality in East Asia are significantly impacting the global climate, contributing to the acceleration of global warming.


---

## 68. Show HN: ArchGW – An intelligent edge and service proxy for agents

**原文标题**: Show HN: ArchGW – An intelligent edge and service proxy for agents

**原文链接**: [https://github.com/katanemo/archgw/](https://github.com/katanemo/archgw/)

生成摘要时出错

---

## 69. FCC Approves Transactions for T-Mobile, MetroNet, Intelsat and UScelullar

**原文标题**: FCC Approves Transactions for T-Mobile, MetroNet, Intelsat and UScelullar

**原文链接**: [https://docs.fcc.gov/public/attachments/DOC-412914A1.txt](https://docs.fcc.gov/public/attachments/DOC-412914A1.txt)

生成摘要时出错

---

## 70. Apple's Browser Engine Ban Persists, Even Under the DMA

**原文标题**: Apple's Browser Engine Ban Persists, Even Under the DMA

**原文链接**: [https://open-web-advocacy.org/blog/apples-browser-engine-ban-persists-even-under-the-dma/](https://open-web-advocacy.org/blog/apples-browser-engine-ban-persists-even-under-the-dma/)

生成摘要时出错

---

## 71. Kimi K2 is a state-of-the-art mixture-of-experts (MoE) language model

**原文标题**: Kimi K2 is a state-of-the-art mixture-of-experts (MoE) language model

**原文链接**: [https://twitter.com/Kimi_Moonshot/status/1943687594560332025](https://twitter.com/Kimi_Moonshot/status/1943687594560332025)

生成摘要时出错

---

## 72. A Handshake in Orbit 50 Years Ago Transformed the Space Race

**原文标题**: A Handshake in Orbit 50 Years Ago Transformed the Space Race

**原文链接**: [https://www.nytimes.com/2025/07/14/science/apollo-soyuz-test-project-1975-anniversary.html](https://www.nytimes.com/2025/07/14/science/apollo-soyuz-test-project-1975-anniversary.html)

生成摘要时出错

---

## 73. C++ Library

**原文标题**: C++ Library

**原文链接**: [https://mcyoung.xyz/2025/07/14/best/#fnref:terrible-people](https://mcyoung.xyz/2025/07/14/best/#fnref:terrible-people)

生成摘要时出错

---

## 74. 『 0x61 』- Panasonic and OpenBSD = <3

**原文标题**: 『 0x61 』- Panasonic and OpenBSD = <3

**原文链接**: [https://x61.sh/log/2025/07/03072025160538-panasonic_openbsd.html](https://x61.sh/log/2025/07/03072025160538-panasonic_openbsd.html)

生成摘要时出错

---

## 75. Dyeing to get in (2014)

**原文标题**: Dyeing to get in (2014)

**原文链接**: [https://www.genuineideas.com/ArticlesIndex/dye.html](https://www.genuineideas.com/ArticlesIndex/dye.html)

生成摘要时出错

---

## 76. You Are in a Box

**原文标题**: You Are in a Box

**原文链接**: [https://jyn.dev/you-are-in-a-box/](https://jyn.dev/you-are-in-a-box/)

生成摘要时出错

---

## 77. Concurrent Programming with Harmony

**原文标题**: Concurrent Programming with Harmony

**原文链接**: [https://harmony.cs.cornell.edu/book/](https://harmony.cs.cornell.edu/book/)

生成摘要时出错

---

## 78. Binding Application in Idris

**原文标题**: Binding Application in Idris

**原文链接**: [https://andrevidela.com/blog/2025/binding-application/](https://andrevidela.com/blog/2025/binding-application/)

生成摘要时出错

---

## 79. Show HN: Refine – A Local Alternative to Grammarly

**原文标题**: Show HN: Refine – A Local Alternative to Grammarly

**原文链接**: [https://refine.sh](https://refine.sh)

生成摘要时出错

---

## 80. Sell Yourself Well – What Soham Parekh Can Teach Us

**原文标题**: Sell Yourself Well – What Soham Parekh Can Teach Us

**原文链接**: [https://www.fldr.zip/blog/sell-yourself](https://www.fldr.zip/blog/sell-yourself)

生成摘要时出错

---

## 81. Let's Learn x86-64 Assembly (2020)

**原文标题**: Let's Learn x86-64 Assembly (2020)

**原文链接**: [https://gpfault.net/posts/asm-tut-0.txt.html](https://gpfault.net/posts/asm-tut-0.txt.html)

生成摘要时出错

---

## 82. Predicting Competitive Pokémon VGC Leads Using Latent Semantic Analysis

**原文标题**: Predicting Competitive Pokémon VGC Leads Using Latent Semantic Analysis

**原文链接**: [https://jgeekstudies.org/2025/07/11/predicting-competitive-pokemon-vgc-leads-using-latent-semantic-analysis-a-data-driven-approach-to-team-matchups/](https://jgeekstudies.org/2025/07/11/predicting-competitive-pokemon-vgc-leads-using-latent-semantic-analysis-a-data-driven-approach-to-team-matchups/)

生成摘要时出错

---

## 83. Self-imposed ban – a lightweight bash script to block commands

**原文标题**: Self-imposed ban – a lightweight bash script to block commands

**原文链接**: [https://github.com/alex-moon/ban](https://github.com/alex-moon/ban)

生成摘要时出错

---

## 84. Bypassing Google's big anti-adblock update

**原文标题**: Bypassing Google's big anti-adblock update

**原文链接**: [https://0x44.xyz/blog/web-request-blocking/](https://0x44.xyz/blog/web-request-blocking/)

生成摘要时出错

---

## 85. Show HN: FFmpeg in plain English – LLM-assisted FFmpeg in the browser

**原文标题**: Show HN: FFmpeg in plain English – LLM-assisted FFmpeg in the browser

**原文链接**: [https://vidmix.app/ffmpeg-in-plain-english/](https://vidmix.app/ffmpeg-in-plain-english/)

生成摘要时出错

---

## 86. Why I'm Writing Pure HTML and CSS in 2025

**原文标题**: Why I'm Writing Pure HTML and CSS in 2025

**原文链接**: [https://joeldare.com/why-im-writing-pure-html-and-css-in-2025](https://joeldare.com/why-im-writing-pure-html-and-css-in-2025)

生成摘要时出错

---

## 87. I used Suno AI to cover my own demo album

**原文标题**: I used Suno AI to cover my own demo album

**原文链接**: [https://app.mindthis.io/@yt/how-i-used-suno-ai-to-cover-my-own-demo-album](https://app.mindthis.io/@yt/how-i-used-suno-ai-to-cover-my-own-demo-album)

生成摘要时出错

---

## 88. What causes obesity? A major new study is upending common wisdom

**原文标题**: What causes obesity? A major new study is upending common wisdom

**原文链接**: [https://www.msn.com/en-us/health/other/what-causes-obesity-a-major-new-study-is-upending-common-wisdom/ar-AA1IDR4o](https://www.msn.com/en-us/health/other/what-causes-obesity-a-major-new-study-is-upending-common-wisdom/ar-AA1IDR4o)

生成摘要时出错

---

## 89. Burning a Magnesium NeXT Cube (1993)

**原文标题**: Burning a Magnesium NeXT Cube (1993)

**原文链接**: [https://simson.net/ref/1993/cubefire.html](https://simson.net/ref/1993/cubefire.html)

生成摘要时出错

---

## 90. ABCD Study omits gender-identity data from latest release

**原文标题**: ABCD Study omits gender-identity data from latest release

**原文链接**: [https://www.thetransmitter.org/gender/abcd-study-omits-gender-identity-data-from-latest-release/](https://www.thetransmitter.org/gender/abcd-study-omits-gender-identity-data-from-latest-release/)

生成摘要时出错

---

## 91. Speedrun

**原文标题**: Speedrun

**原文链接**: [https://www.educationprogress.org/p/speedrun](https://www.educationprogress.org/p/speedrun)

生成摘要时出错

---

## 92. DreamHAT+ Radar

**原文标题**: DreamHAT+ Radar

**原文链接**: [https://shop.pimoroni.com/products/dream-hat-plus-radar](https://shop.pimoroni.com/products/dream-hat-plus-radar)

生成摘要时出错

---

## 93. How does a screen work?

**原文标题**: How does a screen work?

**原文链接**: [https://www.makingsoftware.com/chapters/how-a-screen-works](https://www.makingsoftware.com/chapters/how-a-screen-works)

生成摘要时出错

---

## 94. Fine dining restaurants researching guests to make their dinner unforgettable

**原文标题**: Fine dining restaurants researching guests to make their dinner unforgettable

**原文链接**: [https://www.sfgate.com/food/article/data-deep-dives-bay-area-fine-dining-restaurants-20404434.php](https://www.sfgate.com/food/article/data-deep-dives-bay-area-fine-dining-restaurants-20404434.php)

生成摘要时出错

---

## 95. AI slows down open source developers. Peter Naur can teach us why

**原文标题**: AI slows down open source developers. Peter Naur can teach us why

**原文链接**: [https://johnwhiles.com/posts/mental-models-vs-ai-tools](https://johnwhiles.com/posts/mental-models-vs-ai-tools)

生成摘要时出错

---

## 96. Spicy – Generating Robust Parsers for Protocols and File Formats

**原文标题**: Spicy – Generating Robust Parsers for Protocols and File Formats

**原文链接**: [https://docs.zeek.org/projects/spicy/en/latest/index.html](https://docs.zeek.org/projects/spicy/en/latest/index.html)

生成摘要时出错

---

## 97. GLP-1s are breaking life insurance

**原文标题**: GLP-1s are breaking life insurance

**原文链接**: [https://www.glp1digest.com/p/how-glp-1s-are-breaking-life-insurance](https://www.glp1digest.com/p/how-glp-1s-are-breaking-life-insurance)

生成摘要时出错

---

## 98. Monitoring My Homelab, Simply

**原文标题**: Monitoring My Homelab, Simply

**原文链接**: [https://b.tuxes.uk/simple-homelab-monitoring.html](https://b.tuxes.uk/simple-homelab-monitoring.html)

生成摘要时出错

---

## 99. Dog Walk: Blender Studio's official game project

**原文标题**: Dog Walk: Blender Studio's official game project

**原文链接**: [https://blenderstudio.itch.io/dogwalk](https://blenderstudio.itch.io/dogwalk)

生成摘要时出错

---

## 100. Show HN: Cogency – Cognitive Architecture for AI Agents

**原文标题**: Show HN: Cogency – Cognitive Architecture for AI Agents

**原文链接**: [https://github.com/iteebz/cogency](https://github.com/iteebz/cogency)

生成摘要时出错

---

