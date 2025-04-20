# Hacker News 热门文章摘要 (2025-04-20)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Zig编译时不会做的事

**原文标题**: Things Zig Comptime Won't Do

**原文链接**: [https://matklad.github.io/2025/04/19/things-zig-comptime-wont-do.html](https://matklad.github.io/2025/04/19/things-zig-comptime-wont-do.html)

本文《Zig编译时不会做的事》强调了Zig编译时特性有意设置的限制，认为这些限制尽管具有表现力，但有助于其优雅性和易用性。

作者强调，Zig中的编译时代码通过模拟目标架构来避免“宿主泄漏”，这与其他一些语言的编译时代码在宿主机上运行、可能导致不一致的情况不同。Zig也缺乏类似于D和Rust等语言中的“#eval”或动态源码生成机制。相反，Zig依赖于通过`comptime`关键字进行的部分求值和特化，这需要某些参数的编译时知识。

文章进一步指出，Zig的元编程系统不允许在语言语法中直接使用自定义语法或DSL。虽然可以通过字符串实现自定义语法，但Zig也避免使用运行时类型信息（RTTI），要求在编译时完全特化类型元编程。

关键的是，Zig不允许向生成的类型添加方法，这意味着自定义类型的API必须手动编写。最后，编译时操作是完全隔离的，禁止任何输入/输出（IO）操作，从而确保隐蔽、可重现和安全的编译。作者总结说，这些限制虽然具有约束性，但使Zig的元编程特性更易于管理和预测。任何需要IO的构建时操作，如数据库交互，都可以由Zig的构建系统处理。

---

## 2. Gemma 3 QAT 模型：将人工智能带入消费级 GPU

**原文标题**: Gemma 3 QAT Models: Bringing AI to Consumer GPUs

**原文链接**: [https://developers.googleblog.com/en/gemma-3-quantized-aware-trained-state-of-the-art-ai-to-consumer-gpus/](https://developers.googleblog.com/en/gemma-3-quantized-aware-trained-state-of-the-art-ai-to-consumer-gpus/)

谷歌开发者博客宣布Gemma 3量化感知训练优化版模型发布，显著降低内存需求，使先进AI技术可在NVIDIA RTX 3090等消费级GPU上运行。

---

## 3. 图灵绘图

**原文标题**: Turing-Drawings

**原文链接**: [https://github.com/maximecb/Turing-Drawings](https://github.com/maximecb/Turing-Drawings)

图灵绘图：一个基于JavaScript+HTML5的演示，展示了随机生成的图灵机在2D画布上创作图像和动画。该项目（网址：http://maximecb.github.io/Turing-Drawings/）以修改后的BSD许可证发布。核心思想是，这些随机生成的图灵机，尽管规则简单，却能产生令人惊讶的复杂和视觉上有趣的图案。列表中的名称（分形、扫描、矩阵等）例证了该系统所实现的各种美学效果，暗示了从简单计算过程中可能出现的各种可能性和意想不到的美。作者还提到撰写了一篇博客文章来进一步解释该项目，表明有更深入的见解和解释可供参考。本质上，该项目探索了基本计算模型中固有的涌现创造力。

---

## 4. 健康的土壤是隐藏的秘诀。

**原文标题**: Healthy soil is the hidden ingredient

**原文链接**: [https://www.nature.com/articles/d41586-025-01026-x](https://www.nature.com/articles/d41586-025-01026-x)

这篇《自然》杂志的文章《健康的土壤是隐藏的要素》强调了土壤健康的关键重要性，尤其是在面临严重土壤退化的欧盟和西班牙的背景下。 欧盟估计，其60-70%的土壤是不健康的，每年造成500亿欧元的损失。 西班牙的土壤侵蚀率在欧洲最高（14.2吨/公顷/年），可以作为一个案例研究。

这篇文章介绍了格拉纳达大学的地理学家Jesús Rodrigo Comino，他的研究重点是开发可持续的土壤管理实践，尤其是在葡萄园中。 他利用地理制图系统和人工智能为农民创建工具，帮助他们就灌溉、覆盖作物和耕作做出明智的决策。

Rodrigo Comino还参与了SOILCRATES项目，该项目是欧盟“欧洲土壤协议”的一部分，旨在建立田间试验点，以合作研究可持续土壤，并提高公众对土壤健康重要性的认识。

这篇文章还探讨了气候变化的影响，指出气温升高、降水减少以及更频繁的极端降雨事件，这些都影响着土壤健康。 虽然关于葡萄园的结论性数据仍在收集，但趋势表明开花期提前，并且由于集中降雨导致土壤侵蚀加剧。

---

## 5. 锯齿状AGI：o3、Gemini 2.5及后续一切

**原文标题**: Jagged AGI: o3, Gemini 2.5, and everything after

**原文链接**: [https://www.oneusefulthing.org/p/on-jagged-agi-o3-gemini-25-and-everything](https://www.oneusefulthing.org/p/on-jagged-agi-o3-gemini-25-and-everything)

伊森·莫里克讨论了o3和Gemini 2.5 Pro等人工智能模型的最新进展，以及它们是否代表通用人工智能（AGI）的争论。他强调了泰勒·科文基于o3令人印象深刻的能力，断言其为AGI的观点，并展示了o3仅凭一个提示就能创建营销计划、徽标和网站，以及其地理定位能力等例子。

莫里克介绍了“锯齿状AGI”的概念，描述了人工智能的不均衡能力，它擅长复杂任务，却在简单任务上失败，例如o3在一个修改过的脑筋急转弯上的失败。尽管存在这些不一致性，但这些模型在各种任务中的通用能力和表现仍然值得注意。

鉴于定义的模糊性，他质疑这些模型是否真正构成AGI，但认为它们代表了一种“锯齿状AGI”，其重要性足以影响工作和生活，同时也承认其不可靠性需要人工监督。

莫里克承认，即使实现了AGI，其影响也可能不会立即显现，因为社会和组织适应缓慢。然而，像o3这样的模型的代理能力，使其能够独立分解复杂目标并执行多步骤计划，可能会加速采用。最终，他得出结论，人工智能整合的轨迹仍然不确定，可能逐渐改变，也可能快速转型，并强调在“锯齿状地带”中航行，为未来做好准备的重要性。

---

## 6. 哪一年：猜猜每张照片拍摄于哪一年

**原文标题**: Which year: guess which year each photo was taken

**原文链接**: [https://whichyr.com/](https://whichyr.com/)

猜年份：一款令人着迷且寓教于乐的图片猜谜游戏，挑战玩家猜测历史照片的拍摄年份。玩家使用时间轴滑块在1850年至2025年间选择年份。猜测越接近实际年份，获得的分数越高。

游戏提供“数字揭示”提示功能，让玩家在遇到困难时解锁正确年份的一个数字，但每个数字在每局游戏中只能揭示一次。“每日挑战”每天提供一组新的照片，让玩家测试他们的知识，与他人比较分数，并跟踪他们随时间的进步。该游戏旨在测试和提高视觉记忆和历史知识。

---

## 7. Weave (YC W25) 招聘创始工程师

**原文标题**: Weave (YC W25) is hiring a founding engineer

**原文链接**: [https://www.ycombinator.com/companies/weave-3/jobs](https://www.ycombinator.com/companies/weave-3/jobs)

Weave (YC W25)，一家专注于提高工程团队效率的软件公司，正在招聘两位创始工程师：一位人工智能工程师和一位产品工程师。两个职位均位于加州奥克兰或旧金山，薪资范围为 14 万美元至 20 万美元，股权为 0.50% 至 2.00%。人工智能工程师职位至少需要 1 年的经验，而产品工程师职位对所有经验水平开放，包括应届毕业生。Weave 强调其为工程团队构建最佳软件的使命。该公司资金充足，由顶级投资者支持，盈利且增长迅速。Weave 成立于 2024 年，目前活跃于旧金山。创始人是 Andrew Churchill 和 Adam Cohen。

---

## 8. 向旧金山蹒跚

**原文标题**: Slouching Towards San Francisco

**原文链接**: [https://rachdele.substack.com/p/slouching-towards-san-francisco](https://rachdele.substack.com/p/slouching-towards-san-francisco)

无法访问文章链接。

---

## 9. 加拿大各地的家庭画廊隐于市井

**原文标题**: Home galleries are hiding in plain sight across Canada

**原文链接**: [https://www.cbc.ca/arts/home-galleries-are-hiding-in-plain-sight-across-canada-1.7503886](https://www.cbc.ca/arts/home-galleries-are-hiding-in-plain-sight-across-canada-1.7503886)

加拿大各地家庭画廊兴起：艺术自主与生活成本驱动

---

## 10. 可启动容器时代的Linux主题之乐

**原文标题**: The Joy of Linux Theming in the Age of Bootable Containers

**原文链接**: [https://blues.win/posts/joy-of-linux-theming/](https://blues.win/posts/joy-of-linux-theming/)

本文探讨了在可引导容器时代使用 Linux 主题的乐趣，特别是使用 `bootc` 项目。作者回顾了过去自定义桌面环境的经验以及配置损坏带来的挫败感。`Bootc` 提供了一种解决方案，允许将操作系统定义为 Containerfile，从而实现轻松的实验和回滚功能。这种方法减轻了经常困扰传统 Linux 自定义方法的配置漂移和系统损坏问题。

作者将 `bootc` 与 shell 脚本、`systemd-sysext` 和 Nix 等其他方法进行了对比，认为 `bootc` 提供了更出色的灵活性、安全性和工具。一个关键优势是，如果更改破坏了系统，可以轻松恢复到之前的容器状态。

本文还深入探讨了在可引导容器时代，什么构成“Linux 发行版”的问题。作者反思了他们的项目 Blue95（一个带有特定主题的 Fedora Xfce Atomic 镜像），并质疑它是否符合发行版的定义。作者指出，Containerfile 和完整的发行版之间的界限正变得越来越模糊。一些人认为流行的基于 `bootc` 的项目是发行版，即使它们构建在现有的发行版之上。尽管定义不明确，但作者得出结论，创建和使用他们自己主题的可引导容器是一种个人满足感的来源，因为它表达了他们的创造力。

---

## 11. 1980年代玩具机械臂启发现代机器人技术

**原文标题**: A 1980s toy robot arm inspired modern robotics

**原文链接**: [https://www.technologyreview.com/2025/04/17/1114456/toy-armatron-modern-robotics-ai-nostalgia/](https://www.technologyreview.com/2025/04/17/1114456/toy-armatron-modern-robotics-ai-nostalgia/)

本文探讨了20世纪80年代的简易玩具机械臂Armatron如何启发了一代现代机器人工程师。作者回忆了他童年对Armatron的痴迷，强调了其由单一电机和复杂齿轮箱驱动的纯机械设计。

随后，文章深入讲述了Armatron在Tomy的开发者渡边宏之的故事，揭示了他的灵感来源于一份报纸剪报和无线电遥控直升机。尽管缺乏正规的工程教育，渡边的独创性设计却给当时的专业机器人工程师留下了深刻印象。

通过波士顿动力公司和加州大学伯克利分校的工程师们的轶事，展现了Armatron的影响力。波士顿动力公司的机械设计工程师Adam Borrell认为Armatron激发了他对机器人的兴趣。加州大学伯克利分校的教授Eric Paulos利用Armatron的限制作为灵感，激励他的学生创造性地解决问题。

文章最后强调了Armatron的持久魅力，这体现在通过在线社区和DIY改造重新发现它。渡边表示很高兴看到人们仍然对这款玩具的机制感到惊叹，强调了实践好奇心在机器人领域的价值。文章断言，即使随着人工智能在机器人领域的兴起，该领域仍然需要像Armatron这样的模拟玩具所培养的创造力和问题解决能力。

---

## 12. 树莓派激光雷达扫描仪

**原文标题**: Raspberry Pi Lidar Scanner

**原文链接**: [https://github.com/PiLiDAR/PiLiDAR](https://github.com/PiLiDAR/PiLiDAR)

本文详细介绍了一个名为PiLiDAR的DIY项目，该项目使用树莓派创建一个360° 3D全景扫描仪。该项目集成了LiDAR技术（LDRobot LD06、LD19或STL27L）、树莓派HQ摄像头和一个步进电机，以实现自动化扫描。

核心功能包括自定义LiDAR串口驱动程序、CRC包完整性检查、硬件PWM校准、2D可视化、通过恒定曝光和白平衡的鱼眼照片创建全景图以及3D场景组装。该项目利用Open3D进行可视化和导出（PCD、PLY、e57），并包含对齐多个扫描和表面网格化的技术，尽管后者在树莓派本身上是资源密集型的。

硬件设置涉及特定的LiDAR型号、相机镜头、树莓派4、带有驱动器的步进电机和一个电源。本文提供了各种组件的详细接线图和设置说明，包括电源按钮功能、加速度计集成、CPU风扇控制和扫描按钮注册。

软件设置包括配置UART权限、启用硬件PWM、安装必要的库（如RPi Hardware PWM和Hugin用于全景拼接）以及管理USB端口电源。本文描述了LiDAR型号的串行协议，以及使用Plotly进行远程Open3D可视化以及自动将扫描转储到USB存储的说明。还提供了故障排除技巧和有用的参考资料。

---

## 13. 解决积分百年 (2020)

**原文标题**: 100 Years to Solve an Integral (2020)

**原文链接**: [https://liorsinai.github.io/mathematics/2020/08/27/secant-mercator.html](https://liorsinai.github.io/mathematics/2020/08/27/secant-mercator.html)

利奥·西奈的文章《百年求解的积分》探讨了正割函数积分 ∫sec(x) dx 的历史背景。虽然现在这是个标准的微积分问题，但在几个世纪前，它曾是一个巨大的挑战，源于对精确地图绘制的需求。

赫拉德斯·墨卡托在1569年创建他的世界地图时遇到了这个积分，这是一项至关重要的导航工具，但他无法解析地解决它，而是使用了近似值。ln|sec(x) + tan(x)| + c 的解于1645年被偶然发现，并在1668年正式证明，几乎在墨卡托最初的需求一个世纪之后。

这篇文章解释了墨卡托投影，强调了它如何独特地保留角度，使其成为导航的理想选择，因为它确保了恒向线（恒定方位的线）看起来是直的。这种投影需要确定每个纬度的拉伸因子，最终导致了正割积分的出现。

西奈进一步深入研究了历史上对数学表格，尤其是三角函数表的依赖，因为这是现代计算器出现之前计算的辅助工具。爱德华·赖特发表了墨卡托地图方程的表格，约翰·纳皮尔引入了对数，这两者都有助于简化导航和地图绘制的计算。该积分的发现与某人一丝不苟地计算表格密切相关。

---

## 14. Show HN: 我做了一个AI，可以将GitHub代码库转换成简易教程

**原文标题**: Show HN: I built an AI that turns GitHub codebases into easy tutorials

**原文链接**: [https://github.com/The-Pocket/Tutorial-Codebase-Knowledge](https://github.com/The-Pocket/Tutorial-Codebase-Knowledge)

此“Show HN”帖子介绍了一款AI代理，它能从GitHub代码库中自动生成适合初学者的教程。该AI使用Pocket Flow框架（一个100行的LLM框架）构建，可抓取存储库、分析代码结构并识别核心抽象，以创建带有可视化的、易于理解的教程。

该帖子提供了YouTube开发教程和Substack帖子的链接，供那些有兴趣自己构建AI代理的人参考。它还展示了为流行的GitHub存储库（如AutoGen、FastAPI、NumPy和Requests）生成的示例教程，演示了该AI以更简单的方式解释复杂代码的能力。

该AI可用于GitHub存储库和本地目录。用户可以指定要包含和排除的文件、要分析的最大文件大小以及教程的输出语言。要开始使用，用户需要克隆存储库、安装依赖项、配置其LLM API密钥（默认为Gemini Pro），并使用适当的参数（存储库URL或目录、包含/排除模式、语言等）运行`main.py`脚本。该帖子重点介绍了使用Agentic Coding与Pocket Flow来加速开发过程，从而使AI代理（如Cursor AI）能够自动化代码生成。

---

## 15. 未来的技能不是“人工智能”，而是“专注”。

**原文标题**: The skill of the future is not 'AI', but 'Focus'

**原文链接**: [https://www.carette.xyz/posts/focus_will_be_the_skill_of_the_future/](https://www.carette.xyz/posts/focus_will_be_the_skill_of_the_future/)

大型语言模型（LLM）在为工程师提供强大工具的同时，过度依赖它们会带来重大风险：解决问题的能力下降，特别是专注力。作者承认LLM可以自动化任务、生成代码和辅助调试，从而释放时间来解决复杂问题。然而，LLM容易产生幻觉、不一致和偏差，因此需要仔细审查其输出结果。

核心担忧是工程师可能会过度依赖LLM生成的现成解决方案，尤其是在解决熟悉的问题时，导致自身解决问题的能力退化。作者强调理解LLM生成解决方案背后的“原因”的重要性，而不是简单地盲目接受它们。掌握基本技能对于解决复杂问题至关重要，而过度依赖LLM会阻碍这些技能的培养和维护。

作者将LLM与搜索引擎进行了对比，认为搜索引擎在探索和利用之间提供了选择，而LLM主要鼓励立即利用。移除探索可能会导致利用过程的不稳定。文章最后表达了担忧，即快速交付解决方案的压力导致工程师失去专注力，而这种技能需要练习。作者质疑未来应对复杂挑战的能力是否将完全依赖于人工智能，而不是人类的聪明才智。

---

## 16. OpenAI 究竟为何要收购 Windsurf？

**原文标题**: Why on Earth is OpenAI buying Windsurf?

**原文链接**: [https://theahura.substack.com/p/tech-things-openai-buys-windsurf](https://theahura.substack.com/p/tech-things-openai-buys-windsurf)

我无法访问该文章链接。

---

## 17. 数学和故事的注意力跨度 (2019)

**原文标题**: Attention Spans for Math and Stories (2019)

**原文链接**: [https://www.jeremykun.com/2019/03/26/attention-spans-for-math-and-stories/](https://www.jeremykun.com/2019/03/26/attention-spans-for-math-and-stories/)

故事讲述是让儿童和成人参与数学的关键工具，特别是对于那些觉得数学令人生畏的人。作者通过个人经历强调，即使是 5 岁的儿童，当数学概念以引人入胜的故事形式呈现时，也更容易接受。

作者通过实例说明了这一点，例如通过“热爱数学的男孩”向 5 岁的孩子介绍素数，并使用精心设计的虚构故事让夏令营的孩子们参与活动。核心概念是，故事提供动力，创造归属感，并将学习转变为自然而愉快的过程。

本文强调了通过讲故事使数学正常化的重要性，并将其与直接教学或强制练习等方法形成对比。它表明，当数学融入叙事和家庭生活时，可以减轻数学焦虑。作者还讨论了如何通过编造关于他们勇敢事迹的古怪故事，来帮助童子军队伍中较小的成员感到受欢迎。

作者认为，随着一个人对数学越来越适应，故事的重点可以转移，数学对象和定理成为中心人物和情节驱动力。他们提倡更多以故事为中心的数学内容，并强调 YouTube 频道 Numberphile 和漫画系列 Beast Academy 等例子。最终目标是学会讲好故事，从而为所有人培养与数学更深入、更易于理解的联系。

---

## 18. 我们给PRO/VENIX做一个刚好够用的，C89之前的TCP/IP协议栈，采用Slirp-CK。

**原文标题**: Let's give PRO/VENIX a barely adequate, pre-C89 TCP/IP stack, featuring Slirp-CK

**原文链接**: [http://oldvcr.blogspot.com/2025/04/lets-give-provenix-barely-adequate-pre.html](http://oldvcr.blogspot.com/2025/04/lets-give-provenix-barely-adequate-pre.html)

本文详细介绍了一个项目，该项目旨在为运行 PRO/VENIX V2.0（基于 System V 的 Unix 移植版本）的 DEC Professional 380 创建一个极简的 TCP/IP 协议栈。 目标是为缺乏原生 TCP/IP 支持的系统提供基本的网络功能，使用机器较慢的串口 (4800bps) 和 RFC 1055 SLIP 协议。

作者的目标是一个“勉强够用”的协议栈，由于处理能力有限且连接速度慢，因此优先考虑客户端任务。 预期的应用程序包括检查网络连接 (ICMP)、DNS 查找 (UDP)、设置系统时间 (NTP) 以及通过简单的协议（如未加密的 HTTP/1.x）下载数据。

该协议栈将受到高度约束，避免使用现代 C 库，并且对底层系统做出很少的假设。 代码编写将考虑到可移植性，旨在在需要时轻松转换为汇编语言。 为了简单起见，每个客户端程序将单独处理自己的原始数据包，避免多套接字复杂性。

本文还提供了有关 DEC Professional 系列、PRO/VENIX 及其网络功能受限的原因的历史背景。 它强调了将现代网络协议栈移植到具有原始 C 编译器和有限资源的旧系统所面临的挑战。 作者正在使用连接到基于 Fedora 的工作站上的两个带有零调制解调器的 USB 串口加密狗来测试该系统。

---

## 19. 图书管理员很危险

**原文标题**: Librarians are dangerous

**原文链接**: [https://bradmontague.substack.com/p/librarians-are-dangerous](https://bradmontague.substack.com/p/librarians-are-dangerous)

无法访问文章链接。

---

## 20. 研究人员开发出皮秒级闪存设备

**原文标题**: Researchers develop picosecond-level flash memory device

**原文链接**: [https://www.fudan.edu.cn/en/2025/0417/c344a145016/page.htm](https://www.fudan.edu.cn/en/2025/0417/c344a145016/page.htm)

本文片段主要关注一项最新进展：**研究人员已创造出一种能够在皮秒级速度下运行的闪存设备。** 这是传达的最重要信息。

该片段还通过一份近期文章列表提供了背景信息，暗示闪存的开发是最新消息（日期为2025年4月17日）。 其他文章虽然存在，但与闪存新闻没有直接关系，可能只是为了展示该出版物的近期报道。

因此，核心要点是宣布了一种新的、速度明显更快的闪存设备。

---

## 21. Show HN：预览 GitHub Flavored Markdown 的独立应用/GitHub CLI 扩展

**原文标题**: Show HN: A Standalone/GitHub CLI Extension to Preview GitHub Flavored Markdown

**原文链接**: [https://github.com/thiagokokada/gh-gfm-preview](https://github.com/thiagokokada/gh-gfm-preview)

`gh-gfm-preview` 是一个 Go 程序和 GitHub CLI 扩展，用于离线预览 GitHub Flavored Markdown (GFM) 文件。它提供了一种快速、无依赖的方式来在本地渲染 Markdown，使用 `yuin/goldmark` 库模拟 GitHub 的渲染风格。它是 `yusukebe/gh-markdown-preview` 的一个硬分叉，后者依赖于 GitHub Markdown API 并且需要互联网连接。

主要特性包括离线操作、速度快、没有外部依赖（除了二进制文件本身）、零配置、实时重新加载、自动浏览器打开、自动端口查找和优雅降级。它支持大多数 GFM 特性，包括表情符号、警报、语法高亮（通过 `alecthomas/chroma`）、章节链接、MathJax、Mermaid 图表、GeoJSON/TopoJSON 图表和 STL 3D 图表。但是，需要 GitHub 访问的特性（如提及人员）不受支持。

可以通过 `go run`、Nix（如果启用了 flakes）或作为 GitHub CLI 扩展进行安装。使用方法很简单，运行 `gh gfm-preview` 加上文件名（或者它会自动检测 `README`）。它提供了深色/浅色模式选项、禁用自动打开和重新加载选项、指定主机/端口选项以及详细输出选项。

该工具适用于像 Neovim 这样的编辑器中的离线 Markdown 预览，如提供的配置代码段所示。开发涉及通过 `go generate` 和 `go build` 分别生成资产和构建。文章还链接到相关项目，如 GitHub CLI、Grip、`github-markdown-css` 和原始的 `gh-markdown-preview` 项目。

---

## 22. 令人费解的学院派 Emacs

**原文标题**: Perplexingly Book-Learned Emacs

**原文链接**: [https://lars.ingebrigtsen.no/2025/04/17/perplexingly-book-learned-emacs/](https://lars.ingebrigtsen.no/2025/04/17/perplexingly-book-learned-emacs/)

作者探索使用Perplexity AI API来解决查找特定作者新出版书籍的问题，由于缺乏能够区分新作与重印版或修订版的全面数据库，这项任务变得困难。在苦苦挣扎于现有数据库之后，作者注册了Perplexity AI，并创建了一个简单的Emacs库（perplexity.el）来查询API。

作者使用提示来列出特定作者的书籍，然后过滤掉已经拥有的书籍。虽然API访问很简单，但结果并不一致，存在LLM幻觉和可变响应时间。作者观察到，书籍列表在不同查询之间有所不同。然而，作者成功地找到了一些作者以前未知的新书，展示了其一定的效用。

作者详细介绍了对艾米·亨佩尔和梅根·惠伦等作者的试验，注意到不同程度的成功和不一致。在购买了几本通过该过程发现的书籍后，作者添加了Emacs命令，以便快速访问Bookshop.org和Goodreads。最后，作者将Perplexity与Gemini和OpenAI用于相同的任务进行了比较，发现类似的局限性。作者得出结论，即使存在不足和不一致，Perplexity仍然为发现追踪作者的新书提供了一个在某种程度上有用，甚至出乎意料的解决方案。关键的局限性似乎是Perplexity不愿意执行过多的搜索。

---

## 23. 人群尺度下通过刺激单个感光细胞实现的新型色彩

**原文标题**: Novel color via stimulation of individual photoreceptors at population scale

**原文链接**: [https://www.science.org/doi/10.1126/sciadv.adu1052](https://www.science.org/doi/10.1126/sciadv.adu1052)

无法访问文章链接。

---

## 24. 克劳德代码：自主编码的最佳实践

**原文标题**: Claude Code: Best practices for agentic coding

**原文链接**: [https://www.anthropic.com/engineering/claude-code-best-practices](https://www.anthropic.com/engineering/claude-code-best-practices)

我阅读了Anthropic网站上关于“Claude Code：代理式编码的最佳实践”的文章。以下是摘要：

该文章讨论了利用Anthropic的AI助手Claude进行“代理式编码”的最佳实践，在这种模式下，Claude可以更自主地解决编码任务。其核心原则是通过提供清晰的指导并允许其在定义的参数范围内独立做出编码决策，从而使Claude能够处理复杂的任务。

主要最佳实践包括：

*   **清晰的任务分解：** 将大型编码项目分解为更小、定义明确的子任务。 这使得Claude可以专注于特定功能并降低出错的可能性。
*   **结构化提示：** 利用结构化提示技术，例如提供示例、指定输入/输出格式以及明确定义约束。 这可以提高Claude对预期结果的理解。
*   **迭代开发：** 鼓励通过频繁审查和完善Claude的代码来采用迭代方法。 就需要改进的领域提供反馈，并允许Claude从错误中学习。
*   **测试和验证：** 强调严格测试和验证的重要性。 生成测试用例并指示Claude运行它们，以帮助识别和修复错误。 该文章还建议使用Claude来*生成*测试用例。
*   **上下文管理：** 仔细管理提供给Claude的上下文，因为它会影响其性能。 提供相关的代码片段、文档和示例来指导其编码工作。 避免用不必要的信息使其不堪重负。
*   **角色扮演：** 指示Claude采用特定的角色或身份，例如“高级软件工程师”或“专家Python程序员”，以指导其编码风格和决策。 这可以提高代码质量和可维护性。
*   **渐进式改进：** 鼓励Claude不断改进其自己的代码，例如通过提出改进可读性、效率或安全性的建议。

该文章强调，虽然Claude可以自动化编码的许多方面，但人工监督对于确保质量、正确性和安全性仍然至关重要。 通过遵循这些最佳实践，开发人员可以有效地利用Claude来加速他们的编码工作流程并更有效地构建复杂的软件应用程序。

---

## 25. 人尽皆知你的位置，第二部分：亲自尝试并分享结果

**原文标题**: Everyone knows your location, Part 2: try it yourself and share the results

**原文链接**: [https://timsh.org/everyone-knows-your-location-part-2-try-it-yourself/](https://timsh.org/everyone-knows-your-location-part-2-try-it-yourself/)

本文是关于应用程序位置数据共享的前一篇帖子的后续。作者提供了一个指南和一个Python笔记本，以帮助读者自行调查应用程序流量，从而发现可能令人惊讶的数据收集和共享行为。其目标是众包关于哪些应用程序收集和共享位置和其他敏感数据的信息。

作者详细介绍了如何使用mitmproxy拦截和记录应用程序流量，然后提供了一个Python笔记本，其中包含过滤和分析数据的说明，用于查找诸如位置和IDFA之类的特定关键字。还包括域流量的可视化，揭示了诸如Unity、Google的Doubleclick和Applovin等广告网络的主导地位。

该指南概述了如何在计算机上设置mitmproxy，配置移动设备以通过代理路由流量，然后捕获应用程序流量数据。然后，该笔记本有助于基于关键字的过滤，以查找数据收集的特定实例。作者强调了手动审查的重要性，以避免遗漏可能至关重要的数据点。

最后，作者邀请读者通过一个表格贡献他们的发现，该表格会填充一个共享的Google表格，并强调需要在提交之前编辑个人信息。作者承认该方法的简单性，但认为它在自动化和手动分析之间提供了良好的平衡，以避免遗漏可能有趣的细节。

---

## 26. Rust 中漂亮的有限状态机模式 (2016)

**原文标题**: Pretty State Machine Patterns in Rust (2016)

**原文链接**: [https://hoverbear.org/blog/rust-state-machine-pattern/](https://hoverbear.org/blog/rust-state-machine-pattern/)

本文探讨了实现状态机的不同 Rust 设计模式，重点在于编译时安全性和代码清晰度。文章首先定义了状态机及其在各种应用中的重要性，强调了强制执行有效状态转换的必要性。

作者提出了三种实现方法：

1.  **枚举：** 一种基于枚举的基础方法，其中状态是枚举的变体。此方法简单，但缺乏编译时转换强制执行，并存在运行时错误和重复的 match 语句。

2.  **带转换的结构体：** 为每个状态使用不同的结构体，并使用 `From` 和 `Into` 特性来定义有效的转换。这为转换提供了编译时安全性，并在转换过程中消耗旧状态，但会导致代码重复和共享状态管理困难。

3.  **泛型：** 最复杂的方法，使用泛型结构体 `BottleFillingMachine<S>`，其中 `S` 代表当前状态作为类型参数。`From` 实现用于定义 `BottleFillingMachine<Waiting>`、`BottleFillingMachine<Filling>` 和 `BottleFillingMachine<Done>` 之间允许的转换。这实现了编译时安全性、清晰的错误消息，并允许在 `BottleFillingMachine` 结构体中共享状态。这种方法在编译时保证、可读性和减少代码重复之间提供了最佳平衡。

文章总结说，泛型方法提供了最多的优势，确保了在编译时进行有效的转换，并提供易于理解的错误消息，同时还允许共享状态并遵守 Rust 的类型安全和性能原则。

---

## 27. 安卓手机闲置三天后将自动重启

**原文标题**: Android phones will soon reboot themselves after sitting unused for three days

**原文链接**: [https://arstechnica.com/gadgets/2025/04/android-phones-will-soon-reboot-themselves-after-sitting-unused-for-3-days/](https://arstechnica.com/gadgets/2025/04/android-phones-will-soon-reboot-themselves-after-sitting-unused-for-3-days/)

本文讨论了通过 Google Play 服务更新 (v25.14) 为 Android 设备带来的一项新功能，该功能将在闲置三天后自动重启已锁定的手机。这种“闲置重启”通过强制手机进入“首次解锁前 (BFU)”状态来增强安全性。在 BFU 状态下，生物识别和基于位置的解锁将被禁用，需要密码或 PIN 码才能访问，并且所有数据都将被加密，从而大大增加了提取数据的难度，即使使用高级工具也是如此。

该更新类似于苹果的“闲置重启”，旨在最大限度地减少手机在无人触碰时保持未加密状态的时间。该更新将在未来几周内静默推出，无需用户操作，这展示了 Google 通过 Play 服务更新在各种 Android 设备上改进安全性的能力。 虽然 Google 通过 Play 服务进行集中控制引起了一些担忧，但在这种情况下，它可以实现快速而广泛的安全增强。 作者 Ryan Whitwam 强调，即使手机长时间处于闲置状态并插上电源，此举也将限制存储在手机上的个人数据的暴露。

---

## 28. OAuth在MCP安全中的作用

**原文标题**: OAuth's Role in MCP Security

**原文链接**: [https://defensiblesystems.substack.com/p/oauths-role-in-mcp-security](https://defensiblesystems.substack.com/p/oauths-role-in-mcp-security)

无法访问文章链接。

---

## 29. 硅谷人行道按钮疑被黑客入侵，模仿马斯克、扎克声音

**原文标题**: Silicon Valley crosswalk buttons apparently hacked to imitate Musk, Zuck voices

**原文链接**: [https://www.paloaltoonline.com/technology/2025/04/12/silicon-valley-crosswalk-buttons-apparently-hacked-to-imitate-musk-zuckerberg-voices/](https://www.paloaltoonline.com/technology/2025/04/12/silicon-valley-crosswalk-buttons-apparently-hacked-to-imitate-musk-zuckerberg-voices/)

上周，红木城、门洛帕克和帕洛阿尔托的斑马线按钮遭黑客入侵，播放了马克·扎克伯格和埃隆·马斯克的模仿声音。这些篡改后的信息包含了一些有争议且通常带有讽刺意味的言论，并被归于这些科技巨头。

受影响的地点包括红木城的阿圭洛街角、百老汇和马歇尔街，帕洛阿尔托市中心以及门洛帕克Meta总部附近。 假扎克伯格的声音讨论了人工智能和社会影响，而假马斯克的声音则发表了粗俗的笑话和带有讽刺意味的评论。

帕洛阿尔托和红木城的城市官员禁用了受影响斑马线的语音提示功能，以防止进一步的干扰并确保公共安全。帕洛阿尔托确定有12个市中心路口受到影响。 红木城确定了四个地点。

门洛帕克表示，受影响的斑马线由加州交通局 (Caltrans) 运营，而不是该市。 加州交通局证实其在门洛帕克和帕洛阿尔托的斑马线受到了影响，并停用了音频。 他们正在努力尽快恢复全部功能，目前的斑马线正在定时运行。 所有受影响城市的官员都强调，篡改城市基础设施是非法且危险的。

---

## 30. 英国首例接受子宫移植的女性诞下婴儿

**原文标题**: First baby born in UK to woman with transplanted womb

**原文链接**: [https://www.bbc.com/news/articles/c78jd517z87o](https://www.bbc.com/news/articles/c78jd517z87o)

在突破性进展中，36岁的格蕾丝·戴维森成为英国首位接受子宫移植后分娩的女性。格蕾丝天生患有MRKH综合征，2023年通过一项开创性手术接受了她姐姐艾米的子宫。2025年2月，她和丈夫安格斯迎来了女儿艾米，以纪念格蕾丝的姐姐和捐赠者。

这次成功分娩标志着生殖医学领域的一个重要里程碑，为英国成千上万天生子宫功能不全的女性带来了希望。历时17小时的移植手术涉及一个由30多名医务人员组成的团队。移植后，格蕾丝第一次来了月经，并在第一次试管婴儿尝试中怀孕。

自格蕾丝移植后，该手术团队又进行了三例使用已故捐赠者子宫的移植手术，并计划作为临床试验的一部分总共进行15例移植手术。该团队由外科医生伊莎贝尔·基罗加和理查德·史密斯博士领导。“英国子宫移植”正在资助这些手术，并积极为进一步的手术筹集资金。

婴儿通过剖腹产分娩。在格蕾丝和安格斯生育第二个孩子后，捐赠的子宫将被移除，届时格蕾丝可以停止服用免疫抑制剂药物。艾米宝宝的出生被誉为“小小的奇迹”，并为其他患有子宫因素不孕症的女性带来了希望，此前她们唯一的选择是代孕或收养。

---

## 31. 独特的声响缓解晕动症

**原文标题**: A unique sound alleviates motion sickness

**原文链接**: [https://www.nagoya-u.ac.jp/researchinfo/result-en/2025/04/20250408-01.html](https://www.nagoya-u.ac.jp/researchinfo/result-en/2025/04/20250408-01.html)

名古屋大学研究人员发现，一种特定的低频声音（100赫兹），被称为“声音香料®”，可以缓解晕动症。由香川拓己和加藤正志领导的这项研究发表在《环境健康与预防医学》杂志上，结果表明，即使在移动车辆中阅读或使用驾驶模拟器的参与者，暴露于这种声音一分钟也能减轻恶心和头晕等晕动症症状。

据信，这种声音通过刺激内耳中的椭圆囊和球囊（负责平衡和空间定位的器官）来激活前庭系统。实验包括在通过秋千、模拟器或乘车诱发晕动症之前，让志愿者接触这种声音。结果表明，这种声音增强了交感神经的激活，并减轻了头昏眼花等症状。

研究人员强调了这种声音的安全性，其水平远低于工作场所的噪音标准。他们认为这项技术提供了一种安全有效的对抗晕动症的方法，并计划进一步开发它，以便在各种旅行场景中使用，包括航空和海上旅行。这项研究强调了基于声音的干预措施在管理常见疾病方面的潜力。

---

## 32. 也许Meta的Llama声称是开源的，是因为欧盟的AI法案。

**原文标题**: Maybe Meta's Llama claims to be open source because of the EU AI act

**原文链接**: [https://simonwillison.net/2025/Apr/19/llama-eu-ai-act/](https://simonwillison.net/2025/Apr/19/llama-eu-ai-act/)

本文探讨了一种理论，即 Meta 坚持将其 Llama 模型标记为“开源”，尽管其不符合开源定义，可能是出于欧盟人工智能法案的战略动机。作者研究了该法案，其中为开源人工智能模型提供了特殊豁免，重点关注序言 89 和 102 以及第 2(12) 条。

作者使用 Gemini 2.5 Flash 分析该法案并提取对开源的提及，发现该法案并不要求模型符合 OSI 标准才能在其框架内被视为开源。它将“自由和开源”定义为允许用户自由访问、使用、修改和重新分发模型，并可能包含标准条件，例如署名或类似的发行条款。关键在于该法案侧重于可访问性和使用权，而不是严格遵守 OSI 定义。

作者得出结论，Meta 将“开源”用于 Llama 可能受到这些欧盟人工智能法案豁免的影响，即使这与传统的开源含义不符。作者承认自己是外行，并且使用 LLM 进行法律分析存在风险，但证明其使用是为了理解该文件。最后，文章提到，这种滥用该术语的策略早于欧盟人工智能法案，并参考了 Meta 的 React 库。

---

## 33. Go语言中的分层设计

**原文标题**: Layered Design in Go

**原文链接**: [https://jerf.org/iri/post/2025/go_layered_design/](https://jerf.org/iri/post/2025/go_layered_design/)

本文详述了一种用于 Go 程序的层次化设计方法，该方法源于 Go 语言对循环包依赖的限制。作者强调，理解并利用此约束对于可维护和可扩展的 Go 代码至关重要。

其核心思想是将包层次结构可视化为有向无环图，根据其导入依赖关系将包排列在不同的层级中。底层包没有内部依赖，而较高层级的包则导入较低层级的包。这种结构并非规定性的，而是 Go 语言规则的基本结果。

作者认为，这种层次化方法本身就是一种可靠的设计方法，尽管有时会导致更深的导入链。它与诸如可净化子组件等函数式编程原则非常协调，并确保理解一个包只需要理解代码库的一个有限子集。

当遇到循环依赖错误时，作者建议进行彻底的分析，以查明循环的确切来源，通常会识别出特定代码的“可断开链接”。解决方案包括：

1.  **移动功能：** 将违规代码重新定位到其逻辑所属的包中。
2.  **创建第三个包：** 将共享代码提取到一个新包中，供两个原始包导入。

这些重构提高了概念清晰度并改进了包设计。虽然可以应用更高级别的设计模式，但它们必须在 Go 语言分层架构的约束范围内运行，避免依赖循环依赖。

---

## 34. 纯几何理论的电磁学

**原文标题**: Electromagnetism as a Purely Geometric Theory

**原文链接**: [https://iopscience.iop.org/article/10.1088/1742-6596/2987/1/012001](https://iopscience.iop.org/article/10.1088/1742-6596/2987/1/012001)

提供的文本并非文章，而是Radware Bot Manager的验证码消息。这是一种安全措施，用于验证访问网站的用户是人类而非机器人。消息指示需要勾选方框以确认身份。如果用户遇到问题，请联系网站支持团队并提供问题截图。“事件ID”是验证码失败尝试的唯一标识符，可能用于故障排除。

因此，由于它不是文章，而是一个安全提示，所以无法对“文章”进行总结。 其中不包含有关电磁学或几何理论的信息。

---

## 35. Ssl.com：绕过DCV并为任何MX主机名签发伪造证书

**原文标题**: Ssl.com: DCV bypass and issue fake certificates for any MX hostname

**原文链接**: [https://bugzilla.mozilla.org/show_bug.cgi?id=1961406](https://bugzilla.mozilla.org/show_bug.cgi?id=1961406)

此漏洞报告详细描述了SSL.com域名控制验证(DCV)过程中的一个严重漏洞，特别是关于"发送电子邮件至DNS TXT联系人"(BR 3.2.2.4.14)方法。报告者ragtime_knoll5n发现，SSL.com错误地验证域名所有权，将用于验证的电子邮件地址的主机名（"@"后面的部分）与请求的域名相关联，即使不存在合法连接。

报告者通过为测试域的子域创建一个TXT记录来证明这一点，该记录的值包含来自aliyun.com的电子邮件地址(myusername@aliyun.com)。当请求该测试域的证书并选择该电子邮件进行验证时，SSL.com错误地将aliyun.com添加到报告者验证的域名列表中。这使得报告者随后能够请求并收到aliyun.com和www.aliyun.com的有效SSL证书，尽管他们没有获得授权这样做。

这构成了一项重大的安全风险，允许未经授权的个人获取他们不拥有或控制的域名的证书，可能导致网络钓鱼攻击、中间人攻击和其他恶意活动。

SSL.com已确认该漏洞报告，正在调查该问题，并已暂时禁用受影响的域名验证方法（3.2.2.4.14），用于SSL/TLS证书，以便进行调查。他们预计将在2025年4月21日之前提供初步报告。

---

## 36. Tini：容器中一个微小但有效的`init`程序

**原文标题**: Tini: A tiny but valid `init` for containers

**原文链接**: [https://github.com/krallin/tini](https://github.com/krallin/tini)

Tini：容器的极简`init`进程

Tini 是一个极简的 `init` 进程，专为在容器内（主要为 Docker）运行而设计。它解决了僵尸进程累积等问题，确保正确的信号处理（如 SIGTERM），并以透明的方式运行，无需更改现有的 Docker 镜像。

要使用 Tini，请将可执行文件添加到您的容器，并将其设置为入口点，将您的应用程序和参数传递给 Tini。Docker 1.13 及更高版本包含 Tini，可通过 `--init` 标志启用。预构建的镜像可用，并且存在适用于 Alpine Linux 和 NixOS 的软件包。

Tini 提供以下功能：

*   **详细程度：** 可调整的输出级别，用于调试。
*   **子收割：** 在未作为 PID 1 运行时，可以注册为子收割机（Linux >= 3.4）。
*   **退出代码重映射：** 重映射退出代码（例如，Java 应用程序退出时返回 143）。
*   **进程组杀死：** 将信号发送到整个子进程组。
*   **父进程死亡信号：** 配置 Tini 在其父进程退出时收到的信号。

建议通过签名或校验和验证下载的二进制文件。静态链接版本可实现最大的兼容性。文章还解释了如何从源代码构建 Tini 以及它如何处理进程管理。

---

## 37. 澳大利亚沙漠的图像揭示卫星污染

**原文标题**: An image of the Australian desert illuminates satellite pollution

**原文链接**: [https://www.thisiscolossal.com/2025/04/a-stunning-image-of-the-australian-desert-illuminates-the-growing-problem-of-satellite-pollution/](https://www.thisiscolossal.com/2025/04/a-stunning-image-of-the-australian-desert-illuminates-the-growing-problem-of-satellite-pollution/)

约书亚·罗泽尔斯在澳大利亚尖峰石阵沙漠拍摄的精美照片，展示了日益严重的卫星污染问题。罗泽尔斯本想捕捉星迹，却发现他的照片充斥着卫星轨迹。他汇集了 343 张不同的照片，合成了一张图像，突显了夜空中人造物体日益增长的密度。

文章指出，SpaceX 公司于 2019 年发射的星链是转折点，引发了各公司发射卫星的竞赛。轨道上的卫星数量已超过 10,000 颗，预计将急剧增加，仅 SpaceX 就计划再发射 40,000 颗。

罗泽尔斯的作品以视觉形式呈现了天文学家们表达的担忧，他们警告说，卫星的激增将加剧光污染，并阻碍太空研究。他们强调，卫星行业缺乏监管是导致这种污染不受控制增长的主要因素。

文章重点介绍了像国际天文学联合会黑暗与宁静天空保护中心这样的组织所做的努力，他们正在倡导对夜空进行监管和保护。

---

## 38. 不要强迫孩子学数学

**原文标题**: Don't force your kids to do math

**原文链接**: [https://blog.avocados.ovh/posts/how-to-force-your-kids-to-do-math/](https://blog.avocados.ovh/posts/how-to-force-your-kids-to-do-math/)

本文反对强迫孩子学习数学，提倡以玩乐和好奇心驱动的方式进行学习。作者的“一条规则”是如果孩子表现出不感兴趣，应立即停止数学活动，强调数学应该感觉像玩耍，而不是工作。

作者强调从小将数学融入日常生活，培养孩子与生俱来的好奇心。这包括计数、命名和解释周围的世界，并强调父母对数学的真正热情具有感染力。作者分享了使用游戏、故事和现实场景（如购物或乘坐火车）来使数学更具吸引力的例子。通过玩耍进行重复练习也很关键。

然而，作者告诫不要将个人热情强加于孩子身上，认识到分享兴趣和制造不当压力之间的微妙平衡。他承认孩子们可能不会总是公开表达不适，父母必须注意自己在推动活动时的自我意识。作者指出，他的儿子的兴趣自然地从结构化的数学游戏转向了其他方面，这也没关系。

最终，目标不仅仅是数学能力，而是培养孩子与生俱来的学习、探索和惊叹世界的渴望。作者优先培养孩子与生俱来的学习热情，而不是正规的数学教育，并强调了目睹儿子对知识的好奇心（例如他对无限概念的着迷）的喜悦。

---

## 39. 修复1992年六人Galaxian3剧场版大型电玩机台

**原文标题**: Restoring the Galaxian3 Theatre 6, 1992 six player arcade machine

**原文链接**: [https://philwip.com/2025/04/14/galaxian-3-project-revival/](https://philwip.com/2025/04/14/galaxian-3-project-revival/)

本文详细介绍了位于新罕布什尔州纳舒厄市Fun World游戏厅的一台1992年产稀有Galaxian3 Theatre 6六人街机游戏的修复项目。2024年3月的初步评估显示，该机器存在玩家输入故障、声音缺失和投影仪图像模糊等问题。由Phil Bennett领导的团队确定只有玩家1和2可以使用。核心问题被追溯到有故障的PSN PCB。

文章提供了硬件概述，详细介绍了包括Master、Slave、DSP、PGN、OBJ、V-MIX、C-RAM、RSO和Sound PCB等各种PCB的复杂系统架构，以及Pioneer LaserDisc播放器和Yamaha音频放大器。

一个主要重点是游戏数据的保存。团队成功地使用配备校准Pioneer HLD-X0 MUSE播放器的Domesday Duplicator设置数字化了LaserDisc，并从PCB上转储了ROM数据，包括一个未转储的Project Dragoon修订版（缺少一个ROM）。

对PSN PCB进行了广泛的台式测试和原理图追踪，以诊断玩家输入问题。虽然最初怀疑是RSO PCB的问题，但后来排除了这种可能性。

计划在2025年3月再次前往，带着更多的知识、先进的诊断设备和一位投影仪专家，以解决玩家输入问题并维修投影仪，最终目标是完全修复这款游戏。

---

## 40. 在视频生成中，将输入帧上下文打包进下一帧预测模型

**原文标题**: Packing Input Frame Context in Next-Frame Prediction Models for Video Generation

**原文链接**: [https://lllyasviel.github.io/frame_pack_gitpage/](https://lllyasviel.github.io/frame_pack_gitpage/)

本文介绍了一种视频生成模型，该模型以令人印象深刻的效率实现了高质量的结果。主要进展包括仅使用 6GB 笔记本电脑 GPU 内存，即可使用 13B 参数模型以每秒 30 帧 (fps) 的全速生成视频，且无需依赖时间步蒸馏。

该模型旨在方便个人和实验室进行实验，允许在单个 8xA100/H100 节点上以 64 的批量大小对 13B 视频模型进行微调。此外，即使在个人硬件上，推理也是可行的；RTX 4090 可以以每帧 2.5 秒（未优化）或使用 teacache 优化以每帧 1.5 秒的速度生成帧。

该方法被描述为“视频扩散，但感觉像图像扩散”，这意味着该架构和训练方法允许简化的扩散过程，可能利用了图像扩散模型的进步。核心创新似乎是高效地打包输入帧上下文，从而使该模型能够以相对较低的计算资源生成高分辨率、高帧率的视频。

---

## 41. Eccfrog512ck2：增强型 512 位魏尔斯特拉斯椭圆曲线 [pdf]

**原文标题**: Eccfrog512ck2: An Enhanced 512-Bit Weierstrass Elliptic Curve [pdf]

**原文链接**: [https://arxiv.org/abs/2504.09584](https://arxiv.org/abs/2504.09584)

这篇arXiv文章 (arXiv:2504.09584)，于2025年4月13日提交，介绍了一种新的512位魏尔斯特拉斯椭圆曲线，名为“Eccfrog512ck2”。该论文由Víctor Duarte Melo和William J. Buchanan撰写，论证了需要超越常用的NIST P256 (secp256r1)和secp256k1曲线的安全级别，后两者提供128位安全性。虽然像NIST P-521、Curve 448和Brainpool-P512这样的曲线实现了256位安全性，但作者提出Eccfrog512ck2作为一种性能更高的替代方案。

其主要论点是，与NIST P-521相比，Eccfrog512ck2提供256位安全性，同时性能得到增强。具体来说，该论文指出Eccfrog512ck2在标量乘法中实现了61.5%的加速，在点生成中实现了33.3%的加速。此外，该曲线被设计为能够抵抗侧信道攻击，并避免像MOV攻击这样的漏洞。该论文被归类于密码学和安全（cs.CR）类别下。

---

## 42. 冰岛选举制度 (2024)

**原文标题**: The Icelandic Voting System (2024)

**原文链接**: [https://smarimccarthy.is/posts/2024-11-25-voting-system/](https://smarimccarthy.is/posts/2024-11-25-voting-system/)

本文解释了冰岛的两比例代表制投票系统，该系统也应用于挪威以及瑞士和德国的一些地区。该系统包括将席位划分为选区席位（CS）和调整席位（AS）。

首先，在每个选区中使用洪特法则（V/(s+1)）分配CS，即得票数（V）除以已分配席位数（s+1）的商最高的政党获得席位。这个过程重复进行，直到所有CS都被分配完毕。

接下来，在全国范围内分配AS以纠正比例失调。各政党必须通过5%的门槛才有资格参与分配。理想情况下，AS分配应最大限度地减少熵，正如Balinski & DeMange所证明的那样，但冰岛使用了一种近似方法，该方法不具备单调性，导致出现政党得票数增加却失去席位的情况。这种不准确的方法有利于较大的政党。

作者建议将AS的数量增加到总席位的50%甚至100%，以减少选票不平等和地方保护主义。作为一种替代投票制度，作者推荐“多数裁决”，该制度对每位选民对每个政党的评价进行分级，从而避免阿罗不可能定理。

最后，作者提到了与Þorkell Helgason共同创建的投票系统模拟器，该模拟器可以比较不同的投票系统，包括冰岛的投票系统和最佳熵方法。

---

## 43. 用于开发机器人滑冰步态的滑冰模型 [pdf] (2020)

**原文标题**: Models of Ice Skating for the Development of Robotic Ice Skating Gaits [pdf] (2020)

**原文链接**: [https://www2.eecs.berkeley.edu/Pubs/TechRpts/2021/EECS-2021-162.pdf](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2021/EECS-2021-162.pdf)

这份题为《冰上滑行模型用于开发机器人冰上滑行步态》的2020年PDF文档，似乎是构成该文章核心的原始、可能未经编辑的数据。遗憾的是，由于所呈现的PDF数据的编码和压缩性质（包括类似PostScript的命令和二进制信息），如果没有渲染和解释整个文档，直接进行语义摘要提取是不可能的。

然而，根据标题和隐含的常见研究主题，这篇文章可能探讨：

*   **冰上滑行的数学和物理模型：** 深入理解人类冰上滑行所涉及的力学和动力学。这可能涉及运动学模型（运动）、动力学模型（力）和摩擦模型，以模拟冰刀与冰面之间的相互作用。
*   **机器人步态开发：** 利用已开发的模型来设计和实现稳定且高效的机器人冰上滑行步态。这涉及解决复杂的控制问题，以协调机器人的肢体并在光滑表面上导航时保持平衡。
*   **模拟和实验：** 通过模拟验证提出的模型和步态，并可能随后在专为冰上滑行设计的物理机器人平台上进行实验测试。

本质上，该研究可能将人类冰上滑行的理论模型与实际的机器人应用相结合，旨在创造能够执行复杂冰上滑行动作的机器人。所提供的内容不直接适用于提取具体结果或方法，但暗示了研究的性质。

---

## 44. 体验时代欢迎您 [pdf]

**原文标题**: Welcome to the Era of Experience [pdf]

**原文链接**: [https://storage.googleapis.com/deepmind-media/Era-of-Experience%20/The%20Era%20of%20Experience%20Paper.pdf](https://storage.googleapis.com/deepmind-media/Era-of-Experience%20/The%20Era%20of%20Experience%20Paper.pdf)

这份名为“欢迎来到体验时代”的文档是一个PDF文件。然而，所提供的内容并非可读的文章，而是PDF本身的原始、压缩数据。它由PDF指令、对象定义、压缩数据流（FlateDecode）和交叉引用表组成，全部为二进制格式。

因此，仅凭提供的PDF源代码，无法总结“欢迎来到体验时代”这篇文章的内容。原始代码无法提供关于主题、论点、结论或任何其他可以被总结的要素的见解。需要一个PDF阅读器来解码二进制数据并呈现实际内容，才能被理解并进行总结。

---

## 45. 网络已崩坏 – 僵尸网络（第二部分）

**原文标题**: The Web Is Broken – Botnet Part 2

**原文链接**: [https://jan.wildeboer.net/2025/04/Web-is-Broken-Botnet-Part-2/](https://jan.wildeboer.net/2025/04/Web-is-Broken-Botnet-Part-2/)

网络已坏 - 僵尸网络（二）：人工智能驱动的网络爬取泛滥，文章讨论了其背后僵尸网络的作用。作者指出，存在一个不光彩的市场，公司通过激励应用开发者在其应用中集成“网络共享”SDK，实际上是将毫无戒心的用户变成了僵尸网络的参与者。这些僵尸网络利用用户的网络带宽进行网络爬虫、暴力破解攻击和其他恶意活动。

文章以Infatica等公司为例，称它们提供“住宅代理”，实质上是出售对受感染应用用户网络连接的访问权限。作者认为，这种商业模式助长了侵略性的人工智能网络爬取，类似于DDoS攻击，会压垮小型网络服务器。

文章批评了那些集成此类SDK的应用开发者，指责他们散布恶意软件并制造僵尸网络成员。文章还感叹普通用户和服务器管理员难以检测到这些隐藏的SDK及其相关的网络流量。

作者得出结论，由于这些不道德公司的行为和当前的“人工智能”炒作，所有网络爬取都应被视为滥用行为。网站管理员只能不断地阻止这些僵尸流量，这使得维护在线服务变得越来越困难。作者敦促苹果、微软和谷歌等平台采取行动来打击这些行为。

---

## 46. Show HN: 哥德巴赫猜想验证至 4*10^18+7*10^13

**原文标题**: Show HN: Goldbach Conjecture up to 4*10^18+7*10^13

**原文链接**: [https://medium.com/@jay_gridbach/grid-computing-shatters-world-record-for-goldbach-conjecture-verification-1ef3dc58a38d](https://medium.com/@jay_gridbach/grid-computing-shatters-world-record-for-goldbach-conjecture-verification-1ef3dc58a38d)

中田裕昭 (@jay_gridbach) 宣布验证哥德巴赫猜想的新世界纪录，将验证范围扩展到4×10¹⁸ + 7×10¹³。他开发了网格计算系统“Gridbach”来实现这一目标。

哥德巴赫猜想，即每个大于2的偶数自然数都可以表示为两个质数之和，仍然未被证明。Gridbach超越了T. Oliveira e Silva在2013年验证的4×10¹⁸这一先前纪录。中田的目标是达到500万兆，并愿意发表论文以获得官方认可。

Gridbach是一个基于云的分布式系统，可通过PC和智能手机访问，无需登录或安装应用程序。用户通过使用高性能WASM在浏览器中运行计算来做出贡献。每个任务覆盖1亿个数字，在设备上只需几秒钟。该项目的灵感来自SETI@home。

该系统采用JAMStack架构和WASM。中田还介绍了“哥德巴赫岭”的概念，代表素数对中较小素数的最大值。核心计算算法已在GitHub上开源为一个Go命令行工具，使用优化的埃拉托斯特尼筛法。中田邀请读者参与并贡献力量，以进一步推进验证。

---

## 47. 英国方言地图 (2023)

**原文标题**: A Map of British Dialects (2023)

**原文链接**: [https://starkeycomics.com/2023/11/07/map-of-british-english-dialects/](https://starkeycomics.com/2023/11/07/map-of-british-english-dialects/)

本文描述了一幅详细但不可否认并不完善的英国英语方言地图。作者强调了英国境内方言的巨大多样性，即使是相邻城镇之间也常常存在差异。该地图是多年研究的成果，结合了现有研究、调查以及来自专注的在线社区的反馈。

作者承认在地图上呈现复杂的语言现实存在固有的局限性。“方言”的定义是主观的，方言边界是模糊和渐变的，而不是清晰的界限，并且一些方言的定义更多地取决于社会因素，而不是地理因素，例如多元文化伦敦英语。作者还明确表示，该地图侧重于英国英语，不包括苏格兰语（被认为是单独的语言）、爱尔兰语、威尔士语和其他本土语言。虽然北爱尔兰由于存在自认为是英国人的人口而被包括在内，但作者承认该地区的复杂性。

尽管存在不足，该地图旨在展示英国英语方言的丰富多样性，并展示作者对该主题的着迷。作者鼓励读者在其网站上探索其他相关地图，并通过Patreon支持他们的工作。

---

## 48. 氛围编程不是低质量工作的借口

**原文标题**: Vibe Coding is not an excuse for low-quality work

**原文链接**: [https://addyo.substack.com/p/vibe-coding-is-not-an-excuse-for](https://addyo.substack.com/p/vibe-coding-is-not-an-excuse-for)

好的，我已阅读了来自所提供URL的文章《氛围编码不是低质量工作的借口》。

以下是摘要：

文章批评了“氛围编码”的概念，作者将其定义为在编码时优先考虑个人乐趣和直觉，有时会牺牲最佳实践、可维护性和协作。作者认为，虽然享受工作很重要，但不应以此为借口来生产低于标准的代码。

核心论点是，“氛围编码”如果过度使用，可能会导致几个负面后果，包括增加技术债务、难以让新团队成员上手、降低代码可重用性，并最终导致软件质量下降。作者强调，专业的软件开发是一项团队工作，需要遵守标准并注重长期可维护性。

文章强调了在个人乐趣与软件开发的实际情况之间取得平衡的重要性。虽然拥抱创造力和探索很有价值，但不应以牺牲生产可靠、易于理解和可维护的代码为代价。即使在“氛围编码”时，良好的软件工程实践，如编写清晰的文档、遵循编码规范和进行彻底的测试，也至关重要。

作者提倡一种有意识的编码方法，即在考虑个人偏好的同时，也要考虑项目和团队的需求。他们认为可以实现一种健康的平衡：在工作中找到乐趣，同时保持高质量和专业水准。氛围编码可以成为过程的一部分，但不应作为借口或替代健全的编码实践。

---

## 49. 航空旅行规划的计算复杂度[pdf] (2003)

**原文标题**: Computational Complexity of Air Travel Planning [pdf] (2003)

**原文链接**: [http://www.demarcken.org/carl/papers/ITA-software-travel-complexity/ITA-software-travel-complexity.pdf](http://www.demarcken.org/carl/papers/ITA-software-travel-complexity/ITA-software-travel-complexity.pdf)

由于文件为PDF格式，其内容以部分无法读取的二进制代码表示，我无法直接访问和解读该文档的内容，因此无法提供关于《航空旅行规划的计算复杂度》这篇文章的准确摘要。因此，我无法基于您提供的PDF文档内容创建摘要。

---

## 50. Meta的垄断使其成为靠得住的顺境朋友

**原文标题**: Meta's Monopoly Made It a Fair-Weather Friend

**原文链接**: [https://www.wired.com/story/plaintext-ftc-meta-trial-mark-zuckerberg/](https://www.wired.com/story/plaintext-ftc-meta-trial-mark-zuckerberg/)

本文批评Meta偏离其在Facebook上连接朋友和家人的最初使命，认为该公司优先考虑利润和用户参与度，通过网红内容和耸人听闻的新闻而非真正的社交连接来实现这一目标。作者强调，Meta的内部调查显示用户希望看到更多来自朋友的内容，但平台却越来越多地呈现陌生人和盈利内容创作者的帖子。

文章认为，这种转变是由病毒式内容和定向广告的盈利能力驱动的，而非用户偏好。扎克伯格承认Facebook已变得更像一个娱乐平台，这被视为承认了这种偏离。

作者将这一变化与Meta涉嫌的垄断行为联系起来，认为该公司的统治地位使其得以忽视其核心用户群。文章回顾了对Instagram和WhatsApp的收购，认为这些是消除威胁的反竞争举措。

作者提到了正在进行的反垄断审判，并认为Meta能够优先考虑娱乐和个性化广告，恰恰*是因为*它锁定了一个庞大的、寻求与朋友和家人联系的用户群。尽管现在提供了一个“朋友”标签，但文章的结论是，用户已经迁移到其他地方，突显了Meta背离其最初社交关注的后果。作者使用这个新功能来说明核心问题：它存在，但很少有人使用它，因为Facebook已经驱使用户不再分享个人内容。

---

## 51. 如何从零开始用张量核心编写快速矩阵乘法 (2024)

**原文标题**: How to Write a Fast Matrix Multiplication from Scratch with Tensor Cores (2024)

**原文链接**: [https://alexarmbr.github.io/2024/08/10/How-To-Write-A-Fast-Matrix-Multiplication-From-Scratch-With-Tensor-Cores.html](https://alexarmbr.github.io/2024/08/10/How-To-Write-A-Fast-Matrix-Multiplication-From-Scratch-With-Tensor-Cores.html)

利用Tensor Core在CUDA上优化矩阵乘法内核(HGEMM)的旅程

---

## 52. 汇编语言的艺术 (2010)

**原文标题**: The Art of Assembly Language (2010)

**原文链接**: [https://www.plantation-productions.com/Webster/www.artofasm.com/Linux/HTML/AoATOC.html](https://www.plantation-productions.com/Webster/www.artofasm.com/Linux/HTML/AoATOC.html)

汇编语言的艺术 (2010) 是一本关于汇编语言编程的综合指南，特别是使用高级汇编 (HLA) 语言。它以教科书的形式组织，涵盖了从基本概念到高级技术的广泛主题。

本书从入门材料开始，包括 HLA 的安装和基本程序结构。然后逐步讲解基本概念，如数字系统、数据组织（位、字节、字）和逻辑运算。它还介绍了浮点运算、字符编码（ASCII、Unicode）和其他数据表示。

本书的大部分内容专门介绍 Intel 80x86 架构，包括寻址模式、内存组织（堆栈、堆）、CPU 设计、指令集架构和内存层次结构。它深入研究了指令编码和优化技术。

本书还涵盖了高级数据结构，包括字符串、字符集、数组、记录、联合和变体类型。它还包括如何处理日期和时间以及文件 I/O 操作的示例。

书中还讨论了过程、函数和模块化编程，包括如何使用包含文件、单元和 makefile 管理大型程序。后面的章节涵盖算术和逻辑表达式、使用 FPU 的浮点运算以及使用表进行高效计算。最后，它探讨了使用 TRY..ENDTRY 语句的异常处理。本书经常强调“整合应用”部分，以巩固本章的概念。

---

## 53. 流星余迹通信

**原文标题**: Meteor Burst Communications

**原文链接**: [https://ronaldelliott.com/mbc.html](https://ronaldelliott.com/mbc.html)

流星余迹通信（MBC）利用流星在大气层中留下的电离尾迹进行超视距远程通信。早期的研究和JANET及SNOTEL等系统证明了其可行性。虽然该技术在20世纪80年代的使用有限，但微处理器的进步现在提供了显著的性能改进潜力。

MBC的工作原理是将无线电波从流星尾迹反射出去。这些尾迹通常由毫克级的流星形成，寿命短且零星出现，因此需要围绕统计预测来设计系统。可用尾迹的频率随昼夜和季节变化。优化涉及平衡频率、天线增益和发射功率等因素。

现代微处理器有助于快速和自适应的信号处理，有可能提高吞吐量和可靠性。这些改进，加上加密，使MBC成为国家安全行动的可靠选择。

MBC系统由主站、远程终端以及可选组件（如加密和服务信道）组成。标准化的程序和可适应的软件进一步提高了性能。

MBC的主要优势包括连接范围（视距和超视距）、限制非预期接收者的接收机会以及固有的距离限制（约1,200英里）。人们已经认识到其潜在的军事应用，并且通过使用现代微处理器，可以改进战术军事应用。使用可变信号参数的自适应信令技术可以缓解以前的限制，如低数据速率和噪声敏感性。

---

## 54. Monsky定理

**原文标题**: Monsky's Theorem

**原文链接**: [https://mathmondays.com/monskys-theorem](https://mathmondays.com/monskys-theorem)

Monsky定理指出，正方形无法被分割成奇数个面积相等的三角形。证明结合了数论、组合数学和代数工具。核心要素是斯佩纳引理和2-adic赋值。

斯佩纳引理处理将多边形分割成三角形的情况，其中顶点被涂成红色、绿色或蓝色，并遵守“斯佩纳着色”规则。这些规则规定，没有一个面包含所有三种颜色，并且边界上有奇数个“紫色”线段（红-蓝端点）。该引理保证在这种着色中至少存在一个“三色”三角形（每种颜色各一个）。

该证明涉及模2计数紫色线段，以证明存在奇数个三色三角形。

2-adic赋值，记为ν₂，衡量一个数被2整除的程度。它从有理数扩展到实数（尽管省略了这种扩展的细节）。

该证明的关键在于一种基于2-adic赋值的特定着色方案：如果ν₂(x) > 0且ν₂(y) > 0，则点(x, y)被涂成红色；如果ν₂(x) ≤ 0且ν₂(x) ≤ ν₂(y)，则涂成绿色；如果ν₂(y) ≤ 0且ν₂(y) < ν₂(x)，则涂成蓝色。至关重要的是，没有三个共线点可以拥有所有三种颜色。

将这种着色应用于单位正方形的分割，表明该着色是斯佩纳着色。然后，证明三色三角形*K*的面积必须满足ν₂(K) ≤ -1。由于分割成*n*个三角形时，每个三角形的面积是1/*n*，且*n*是奇数，因此ν₂(1/*n*) = 0，从而导致矛盾，因此这种分割是不可能的。

---

## 55. 展示HN：Undercutf1 – 具有车手追踪、可变延迟的 F1 实时计时 TUI

**原文标题**: Show HN: Undercutf1 – F1 Live Timing TUI with Driver Tracker, Variable Delay

**原文链接**: [https://github.com/JustAman62/undercut-f1](https://github.com/JustAman62/undercut-f1)

Undercutf1 是一个开源的、基于终端（TUI）的应用程序，用于查看 Formula 1 实时计时数据，灵感来源于 FastF1 项目。它使用 UndercutF1.Data 库连接到 F1 实时计时数据流，处理数据，并记录会话以便稍后重播。

主要功能包括一个带有实时分段时间、轮胎信息和差距的计时塔显示；进站策略概览；比赛控制消息；赛道地图上的车手追踪器（支持 iTerm2/Kitty Graphics Protocol）；逐圈计时历史；以及通过本地机器学习实现的团队无线电转录。

用户可以调整数据延迟以与直播同步。该应用程序可以作为 dotnet 工具、独立可执行文件、使用 Docker 镜像或直接从源代码安装。它支持实时会话和使用下载或示例数据的预先录制的会话重播。

可以通过 `config.json` 文件、命令行参数或环境变量进行配置，从而自定义数据目录、日志记录详细程度、API 启用和比赛控制消息通知。数据记录在会话特定目录中的 `subscribe.txt` 和 `live.txt` 文件中以供重播。该工具是非官方的，与 Formula 1 公司无关。

---

## 56. 秘鲁古代灌溉系统因文化将沙漠变为农田。

**原文标题**: Peru's ancient irrigation systems turned deserts into farms because of culture

**原文链接**: [https://theconversation.com/perus-ancient-irrigation-systems-succeeded-in-turning-deserts-into-farms-because-of-the-culture-without-it-the-systems-failed-251199](https://theconversation.com/perus-ancient-irrigation-systems-succeeded-in-turning-deserts-into-farms-because-of-the-culture-without-it-the-systems-failed-251199)

本文探讨了古秘鲁灌溉系统将沙漠变为农田的成功之处，并将其与现代类似系统所面临的挑战进行了对比。文章认为，这些古代系统成功的关键不仅在于基础设施，还在于围绕它们形成的文化——融入其技术解决方案的信仰、行为和规范。

作者是一位考古学家，他强调秘鲁的前西班牙社会面临着与今天类似的气候挑战，包括缺水和频繁的自然灾害。他们的解决方案包括灵活、多功能的基础设施，旨在适应旱季和山洪暴发。他们使用带有渡槽的运河作为沉积物陷阱和堰坝来控制洪水、捕获沉积物并补充地下水位。

西班牙人最初认识到这些运河系统的重要性并对其进行了改造，但他们的努力最终失败，导致缺水和土地退化。这种失败以及现代农业工业实践的困境，归因于技术与文化背景的分离。文章强调，像依赖消失的冰川融水的查维莫奇克项目这样的现代项目，存在着优先考虑短期收益而牺牲长期韧性的风险。

作者总结认为，理解和纳入支持古代灌溉实践的文化知识体系对于开发应对现代气候挑战的可持续解决方案至关重要。 这包括保护土著语言、考古遗址，并促进与长期适应气候变化的社区的合作。

---

## 57. 干旱导致英国人反抗罗马军团，研究发现

**原文标题**: British rebellion against Roman legions caused by drought, research finds

**原文链接**: [https://www.theguardian.com/uk-news/2025/apr/17/british-rebellion-against-roman-legions-caused-by-drought-research-finds](https://www.theguardian.com/uk-news/2025/apr/17/british-rebellion-against-roman-legions-caused-by-drought-research-finds)

公元364至366年间英国南部一系列严重干旱如何促成了公元367年针对罗马统治的关键性叛乱“蛮族阴谋”？本文对此进行了探讨。研究人员利用橡树年轮记录重建了降水水平，发现这些年份的降雨量明显低于周围时期。

连续干旱会摧毁农业，导致饥荒和社会不稳定。研究表明，这削弱了罗马的防御，减少了向哈德良长城等关键地区的粮食供应，并助长了军队的逃亡。

由此造成的军事和社会崩溃为皮克特人、斯哥特人和撒克逊人入侵英国创造了机会，造成重大破坏，俘虏或杀害了罗马指挥官。虽然考古和书面证据有限，但气候数据为叛乱的催化剂提供了一个合理的解释。

研究人员还发现，在同一时期，罗马帝国各地发生的战争与干旱年份之间存在相关性。该研究强调了极端气候条件、社会动荡和冲突之间的潜在联系，并将之与现代对气候变化后果的担忧联系起来。文章认为，干旱加剧了罗马不列颠固有的脆弱性，最终导致了一场促成其衰落的完美风暴。

---

## 58. Haujobb和Sweet16的演示曲“心灵”

**原文标题**: Demo "The Mind" by Haujobb and Sweet16

**原文链接**: [https://www.lexaloffle.com/bbs/?pid=145596](https://www.lexaloffle.com/bbs/?pid=145596)

“hellfire”的博客文章宣布发布了“The Mind”，这是Haujobb & Sweet16为Revision demoparty的“幻想游戏机”比赛创作的新演示作品。该演示作品专为Pico-8平台设计，并使用了多卡功能。目前，它只能在线观看。

该文章提供了几种访问演示作品的方式：在线观看链接，Pouet上的完整源代码存档下载链接，Youtube视频，以及一个解释音乐创作过程的视频。用户还可以通过在Pico-8中使用命令“load #themind1”后接“run”来直接加载和运行演示作品，这将下载必要的数据卡。

更新提到，由于Zep的贡献，“The Mind”现在可以直接在BBS中运行。该文章提供了卡带文件和论坛帖子的链接。“Hellfire”还包括了他们创建的其他卡带的链接。最后，他们分享了展示一些视觉效果的独立文件链接，特别是“Interference”和“Neuronal network”，其中包含了隧道渲染、光栅效果和像素艺术等各种效果的演示。该文章鼓励观众提供反馈和讨论。

---

## 59. 一致性哈希环

**原文标题**: Consistent Hash Ring

**原文链接**: [https://gallery.selfboot.cn/en/algorithms/hashring](https://gallery.selfboot.cn/en/algorithms/hashring)

本文解释了一致性哈希环的概念和优势，这是一种特殊的哈希算法，用于分布式系统中的数据分发和负载均衡。它解决了分布式系统中添加/删除节点时尽量减少数据迁移的挑战。

文章强调了将哈希值映射到环形结构的核心概念，其中服务器被分配位置。然后，数据存储在从数据的哈希位置顺时针方向遇到的第一个服务器上。这种方法限制了节点更改期间的数据重新分配。

文章进一步解释了虚拟节点对于提高数据分布均匀性的重要性。虚拟节点是物理节点的虚拟副本，增加了环上的分配点数量，并平衡了数据负载。文章强调了虚拟节点对数据分布的影响，可视化了它们如何减少数据倾斜并平衡物理节点上的负载。

文章还概述了一致性哈希环的优势，包括可扩展性、负载均衡和高可用性，并讨论了其劣势，例如对哈希函数的依赖、系统复杂性的增加以及初始节点数量的重要性。最后，它列出了在分布式系统中的各种应用，如分布式缓存（Memcached）、分布式存储、负载均衡和分布式数据库，展示了其在实际场景中的效用。

---

## 60. 德州官员被邀操纵州彩票

**原文标题**: Texas Officials Invited the Rigging of the State Lottery

**原文链接**: [https://www.nytimes.com/2025/04/20/us/rigged-texas-lottery.html](https://www.nytimes.com/2025/04/20/us/rigged-texas-lottery.html)

2023年，据称德克萨斯州彩票官员协助操纵州彩票，允许职业赌徒购买几乎所有可能的数字组合，从而确保赢得数千万美元的奖金。这一披露引发了德克萨斯州参议院、州长格雷格·阿博特和总检察长肯·帕克斯顿的愤怒和调查，导致德克萨斯州众议院取消了彩票的资金。

州参议员鲍勃·霍尔将此情况描述为“我们政府内部的犯罪企业”。尽管事件曝光，但肇事者仍然逍遥法外。《纽约时报》披露了新的细节和视频证据，表明该州彩票委员会在确保获得头奖方面发挥了重要作用。该计划涉及以零售商身份出现的店面打印大量彩票，以及彩票打印机与一名前毒品走私犯之间的通信，而中奖者则将其身份隐藏在一家位于特拉华州的空壳公司背后。该事件凸显了一种更广泛的观点，即系统被操纵，进一步削弱了公众的信任。

---

## 61. 介于生死之间的动物

**原文标题**: The Animals That Exist Between Life and Death

**原文链接**: [https://nautil.us/the-animals-that-exist-between-life-and-death-1202592/](https://nautil.us/the-animals-that-exist-between-life-and-death-1202592/)

这篇Nautilus文章探讨了引人入胜的“隐生”现象，以轮虫为例，这种微小的动物似乎可以通过在极度干燥的环境中生存，存在于生死之间。文章追溯了这一发现的历史，始于17世纪安东尼·范·列文虎克最初的观察，他目睹了轮虫在干燥很长一段时间后复活。这引发了关于生命、死亡以及两者之间可能存在的临界状态的哲学问题。

文章强调，几个世纪以来，科学家们一直在努力理解这一现象，最初受到怀疑，后来又受到有限技术的阻碍。大卫·凯林在20世纪中叶对“隐生”的阐述，将重点转移到使生物能够在这种状态下生存的生理机制上。研究表明，一些生物，如丰年虾和线虫，利用海藻糖来保护它们在干燥期间的细胞，而轮虫则利用晚期胚胎发生富集（LEA）蛋白来稳定细胞膜。

轮虫的韧性并非没有代价，因为干燥会导致DNA损伤，而它们在复水后会有效地修复这些损伤。值得注意的是，轮虫已经整合了大量的非动物DNA，可能有助于它们的生存，从而引发了关于进化起源的问题。文章最后指出，关于轮虫是否在其休眠状态下衰老，以及生命和死亡是否真的是仅有的两种状态，科学界和哲学界仍在争论。它们并非简单地“死亡”或“活着”，这种简单的二分法毫无意义。

---

## 62. Zack：Zig语言的简易回测引擎

**原文标题**: Zack: A Simple Backtesting Engine in Zig

**原文链接**: [https://github.com/zerotech-studio/zack](https://github.com/zerotech-studio/zack)

Zack：一个用Zig编写的轻量级回测引擎，旨在根据历史市场数据测试交易策略。它通过处理历史OHLCV数据、生成交易信号、模拟订单执行和管理虚拟投资组合来模拟交易。选择Zig是因为它的性能、内存控制和简洁性。

该引擎通过事件循环运行。它首先加载配置和数据，然后逐个遍历数据条。对于每个数据条，它处理数据，更新投资组合价值，并展望下一个数据条。当前策略（目前是“买入并持有”策略）根据预定义的规则和投资组合的状态生成交易信号。如果生成信号，投资组合确定订单细节，然后将其发送到执行处理程序进行模拟。执行处理程序使用下一个数据条的开盘价来模拟成交延迟。然后更新投资组合，循环继续。最后，引擎记录性能结果。

Zack中实现的“买入并持有”策略在数据条的开盘价超过配置的阈值时生成买入信号，并持有仓位直到回测结束。配置通过JSON文件管理模拟参数和特定于策略的设置。引擎期望OHLCV数据采用CSV格式。该项目结构清晰，包含用于配置、数据、源代码（包括CSV解析、数据处理程序、策略、投资组合和执行处理程序等引擎组件）以及实用程序的独立目录。

要运行Zack，您需要安装Zig，然后克隆存储库并执行`zig build run`。输出提供回测性能摘要，包括初始资本、最终权益、总回报和结束持仓。未来的工作包括实施更多的性能指标、策略和技术指标，以及添加单元测试。

---

## 63. 弗兰肯斯坦的`__init__`

**原文标题**: Frankenstein's `__init__`

**原文链接**: [https://ohadravid.github.io/posts/2025-04-19-frank/](https://ohadravid.github.io/posts/2025-04-19-frank/)

本文幽默地讲述了一名开发者调试Python服务中偶发性`AttributeError`的冒险经历。问题的根源最终追溯到`FooBarWidget`类对其`__init__`方法的奇特实现。

`test_foobar()`测试有时会失败，因为在调用`close()`方法时，`FooBarWidget`对象缺少`should_exit`属性。该属性本应在`FooWidget`类的`__init__`方法中初始化。

问题在于：`FooBarWidget`的`__init__`方法会生成一个新的线程，该线程随后调用父类的`__init__`方法 (`FooWidget.__init__(self)`) 并启动`run()`方法。

作者解释说，采用这种不寻常的方法是为了避免在初始化`zmq.Socket`（无法在线程之间移动）时阻塞主线程。依赖于在`FooWidget.__init__`中创建的套接字的`run()`方法也需要在单独的线程中运行。因此，没有在主线程中创建套接字，而是将`__init__`和`run()`都卸载到新线程中。

问题出现的原因是，`FooBarWidget`的`close()`方法可能在新线程完成`FooWidget`属性初始化*之前*被调用，从而导致`AttributeError`。尽管解决了问题，作者还是谴责这种实现方式无视理智和常识。

---

## 64. 小鸡仔成了美国最抢手的商品

**原文标题**: Baby chickens became America's hottest commodity

**原文链接**: [https://grist.org/economics/how-baby-chickens-became-americas-hottest-commodity/](https://grist.org/economics/how-baby-chickens-became-americas-hottest-commodity/)

禽流感推高鸡蛋价格，引发全国抢购雏鸡热潮，使其成为炙手可热的商品。像默多克牧场和家居用品店这样的商店正经历前所未有的需求，雏鸡在几小时内售罄，孵化场也积压了几个月的订单。

虽然禽流感显著提高了鸡蛋价格，但雏鸡短缺主要是由需求增加而非雏鸡供应减少驱动的。人们正在转向在家养鸡，以实现自给自足并对抗不断上涨的鸡蛋成本。

像斯科特·拜尔这样的专家指出，经济衰退通常会激发人们对后院农场的兴趣。然而，这种趋势引发了人们对养鸡所需长期投入的担忧，有些人会在新鲜感过后抛弃或杀死这些家禽。包括鸡舍、饲料和冬季护理在内的启动成本也可能很高。

尽管存在潜在挑战，但如果方法得当，养鸡既经济又环保。虽然目前雏鸡价格虚高，但专家预测，需求最终会稳定下来，商业鸡蛋生产将会恢复，未来可能会出现盈余和鸡蛋价格打折的情况。目前，孵化场正在努力满足对雏鸡的巨大需求。

---

## 65. 是时候应对耐药性真菌感染了

**原文标题**: High time to tackle drug-resistant fungal infections

**原文链接**: [https://www.nature.com/articles/d41586-025-01177-x](https://www.nature.com/articles/d41586-025-01177-x)

自然杂志文章强调耐药性真菌感染（特别是耳念珠菌）日益增长的威胁以及采取行动的紧迫性。真菌感染是重要的死亡原因，并且由于农业杀菌剂的使用，它们对现有治疗方法的抵抗力正在增强。尽管世界卫生组织的报告强调后期试验中抗真菌药物的数量有限，但该文章强调了在抗菌素耐药性讨论中对真菌感染的忽视。

主要挑战包括真菌感染诊断的困难，尤其是在中低收入国家，以及真菌细胞与人类细胞的相似性，这使得药物开发变得复杂。文章提倡增加对基础研究的投资，以识别新的药物靶点并了解真菌遗传学，从而改进检测和治疗策略。

该文章还建议建立临床试验网络，以促进研究和标准化协议。一个主要担忧是农业和医学中使用类似化合物所产生的交叉耐药性。解决方案包括对杀菌剂使用的更严格规定、对替代杀菌剂的研究以及负责任的废物管理。文章最后强调，工业界、政府和慈善资助者需要合作，以应对耐药性真菌日益增长的威胁，尤其考虑到气候变化等因素可能会加剧这个问题。

---

## 66. 大型语言模型的谱系推断

**原文标题**: Inferring the Phylogeny of Large Language Models

**原文链接**: [https://arxiv.org/abs/2404.04671](https://arxiv.org/abs/2404.04671)

本文介绍了一种名为“PhyloLM”的新方法，用于推断大型语言模型（LLM）的系统发育并预测其性能。作者Nicolas Yax、Pierre-Yves Oudeyer和Stefano Palminteri将传统上用于进化生物学的系统发育算法应用于LLM领域。

PhyloLM计算基于LLM输出相似性的系统发育距离度量。然后，该度量用于构建树状图，直观地表示模型之间的关系。作者证明这些树状图准确地反映了一组111个开源和45个闭源LLM之间的已知关系。

重要的是，本文表明PhyloLM计算的系统发育距离可以预测LLM在标准基准上的性能。这表明PhyloLM可用于以经济高效的方式评估LLM的能力，即使无法访问透明的训练信息。

本质上，PhyloLM将群体遗传学的概念转化为机器学习，提供了一种评估LLM开发、关系和能力的工具。本文强调了这种方法在提供对LLM进化和性能预测的见解方面的潜力。该研究涉及计算机科学（计算与语言、机器学习），并与群体与进化（q-bio.PE）相一致，突出了该工作的跨学科性质。

---

## 67. 在伊朗喝咖啡为何变得如此复杂

**原文标题**: Why drinking coffee in Iran has become so complicated

**原文链接**: [https://adelbordbari.github.io/etc/2025-04-16-coffee/](https://adelbordbari.github.io/etc/2025-04-16-coffee/)

本文幽默地批判了伊朗现代咖啡文化，并将其与该国历史上咖啡饮用的简单性进行了对比。文章以讽刺的笔调开篇，描述了当代伊朗咖啡馆中繁琐而矫揉造作的点单过程。

作者认为，这些新型咖啡馆与其说是为了卖咖啡，不如说是为了贩卖一种生活方式，侧重于详尽的描述、单一产地的咖啡豆以及饮用优质咖啡所带来的身份地位。这种趋势是由营销策略驱动的，这些策略细分客户，迎合那些想要简单咖啡、追求“体验”或渴望获得适合在Instagram上分享的内容的人群。

作者认为，这一趋势源于消费者的不安全感和欲望，他们将咖啡作为一种地位象征和身份信号。咖啡馆无情地利用了这种欲望，出售的是成为咖啡鉴赏家的*概念*，而不仅仅是一种饮料。

作者承认，在德黑兰和伊斯法罕等城市，咖啡馆正成为工作和社交的中心，但他强调，这种精心设计的咖啡文化在很大程度上是一种商业噱头，与过去更简单、更真实的咖啡馆体验相去甚远。核心问题在于，享受咖啡的简单性在这种戏剧化的氛围中消失了。

最后，文章悲观地总结道，这种趋势可能会持续下去，因为太多的利益相关者都投入其中，使得找到一杯简单直接的咖啡变得困难。

---

## 68. Calypsi：一系列C编译器和汇编语言交叉编译器工具链

**原文标题**: Calypsi: A series of C compiler and assembly language cross compiler tool chains

**原文链接**: [https://github.com/hth313/Calypsi-tool-chains](https://github.com/hth313/Calypsi-tool-chains)

Calypsi是一系列闭源的C编译器和汇编语言交叉编译工具链，专为复古和业余爱好者社区设计，未来计划扩展到嵌入式编程目标。最新版本5.10支持包括MOS 6502、WDC 65816、Motorola 68000和HP Nut等目标。支持的主机平台包括Arch Linux、基于Debian的Linux (Ubuntu 20.04)、基于Fedora的Linux (Fedora 40，Nut除外)、macOS x86和Windows 64位。

Calypsi工具链具有符合ISO C 99标准的编译器，支持高达64位的整数类型、浮点运算、结构体/联合体/类型定义以及变长数组。优化编译器生成源代码级别的调试信息，并支持ELF/DWARF、十六进制输出和特定于目标的输出格式。还包含一个源代码调试器。

虽然这些工具是闭源的，但可免费用于业余爱好（不包括商业应用）。HP-41 Nut目标是一个例外，它采用BSD许可，可免费用于商业用途。

该文档还列出了利用Calypsi的开源项目，按目标处理器分类，提供板级支持包和“Hello World”示例。此外，它还提供联系方式，用于反馈和捐赠，并附带捐赠是受欢迎的声明。

---

## 69. 基于GNU Radio和Codec2的开源SDR中DMR调制解调器实现

**原文标题**: Open Source DMR Modem Implementation in SDR with GNU Radio and Codec2

**原文链接**: [https://qradiolink.org/open-source-DMR-transceiver-implementation.html](https://qradiolink.org/open-source-DMR-transceiver-implementation.html)

基于GNU Radio和Codec2的SDR开源DMR调制解调器实现

---

## 70. 我们能信任CVE吗？

**原文标题**: Can We Trust CVE?

**原文链接**: [https://opensourcesecurity.io/2025/04-can-we-trust-cve/](https://opensourcesecurity.io/2025/04-can-we-trust-cve/)

本文探讨了围绕CVE（常见漏洞和暴露）计划的信任危机，这场危机由资金问题和缺乏透明沟通引发。作者认为，由于响应延迟、含糊不清的声明以及对未来缺乏明确性，CVE计划以及NVD（国家漏洞数据库）已经侵蚀了公众信任。

本文批评了VulnCon的举办时机以及对资金危机的迟缓反应。

作者认为，人们对CVE的现有信任已经减弱，并呼吁建立一种基于开放和透明的新方法。文章随后评估了替代的漏洞情报计划：

*   **OWASP全球漏洞情报统一框架：** 一个去中心化的开源项目，具有潜力，因其知名基础和具名作者而获得7/10的信任评分。
*   **EUVD（欧洲漏洞数据库）：** 由欧洲法律支持，在欧洲范围内提供强制信任，因“晦涩难懂的网站”而获得5/10的评分，但法规保证了信任。
*   **GCVE（由CIRCL运营）：** 因其不明确的隶属关系和可能具有误导性的声明而引发担忧。最初信任评分为1/10，在发现更多信息后修改为5/10。
*   **CVE基金会：** 因缺乏透明度、匿名成员以及与现有CVE结构的可疑联系而受到批评，获得1/10的信任评分。

文章最后强调了信任对于任何CVE替代方案的重要性，并建议监控OWASP项目。

---

## 71. Show HN：本地Web视频编辑器，AI字幕，基于音量自动剪辑

**原文标题**: Show HN: Web Video editor, 100% local, AI subtitle, auto cut based on volume

**原文链接**: [https://silenceslicer.com](https://silenceslicer.com)

"Show HN"文章介绍"Silence Slicer"，一款强调隐私和本地处理的在线视频编辑器。其主要特点是完全在用户浏览器内运行，无需下载或上传。这意味着视频数据保留在用户设备上，解决了隐私问题。该编辑器提供AI字幕生成和基于音量水平的自动剪辑（可能是为了删除静音或不需要的音频片段）。核心价值在于提供私密便捷且不损害数据安全的视频编辑体验。该文章明确指出，该应用程序需要JavaScript才能运行。

---

## 72. AI设计抗蛇毒血清：阻断致命蛇毒的新蛋白

**原文标题**: AI-Designed Antivenoms: New Proteins to Block Deadly Snake Toxins

**原文链接**: [https://plentyofroom.beehiiv.com/p/antivenoms-with-ai-designed-proteins](https://plentyofroom.beehiiv.com/p/antivenoms-with-ai-designed-proteins)

《有的是空间》的这篇文章探讨了一种利用人工智能设计的蛋白质生产抗蛇毒血清的有前景的新方法。传统的抗蛇毒血清通过给动物接种毒液来生产，成本高昂、生产缓慢、会产生副作用，而且通常效果不佳，尤其是在蛇咬伤普遍的低资源环境中。

研究人员正在使用人工智能驱动的蛋白质设计，特别是 RFdiffusion 算法，来创造可以结合并中和眼镜蛇和其他蛇毒液中的毒素的蛋白质。他们专注于 α-神经毒素和细胞毒素，这两个家族都属于 3FTxs 毒素组。该过程包括使用晶体学数据进行靶标分析，使用 RFdiffusion 生成结合剂，并使用 ProteinMPNN 和 AlphaFold2 进行优化。

研究人员开发了三种关键结合剂：SHRT（针对短链 α-神经毒素）、LNG（针对长链 α-神经毒素）和 CYTX（针对眼镜蛇细胞毒素）。SHRT 和 LNG 表现出纳摩尔级的结合亲和力，并在体外完全中和了 α-神经毒素活性，并在体内保护小鼠免受致命剂量的侵害。CYTX 在体内的功效有限，需要进一步优化。

与传统方法相比，人工智能设计的抗蛇毒血清具有以下几个优点：更高的亲和力、最小的交叉反应、在大肠杆菌中经济高效的生产、在低资源环境中使用的高热稳定性，以及同时靶向多个毒素家族的潜力。这篇文章强调了人工智能在应对重大全球健康挑战方面的实际应用，但也承认在这些人工智能设计的抗蛇毒血清广泛应用之前，还需要进一步的研究和开发。

---

## 73. 从源代码引导 Rustc

**原文标题**: Bootstrapping Rustc from Source

**原文链接**: [https://github.com/dtolnay/bootstrap](https://github.com/dtolnay/bootstrap)

本文概述了一种从源代码引导 Rust 编译器 (rustc) 的方法，避免依赖从互联网下载的预编译 Rust 二进制文件。它解决了 rustc 以 Rust 编写，通常需要现有 Rust 编译器进行构建的难题。

该方法利用 mrustc，一个用 C++ 实现的 Rust 编译器，能够编译较旧版本的 rustc 和 cargo。该过程在 Debian chroot 中执行，以获得一致的环境，并使用 firejail 阻止构建期间的网络访问。

其动机源于提高 rustc 可重现性的愿望。理想情况下，此引导链将与官方发布链收敛，从而实现哈希验证并检测潜在的篡改。最终目标是在信誉良好的组织之间建立独立的引导链，使他们能够通过哈希匹配来证明官方 rustc 版本的完整性。这种多样化的确认过程将显著提高用户对官方版本安全性和可信度的信心，即使在高安全性的情况下也是如此。

这些步骤包括：安装 debootstrap 和 firejail，克隆存储库，下载 mrustc 和必要的 rustc 源代码，初始化 chroot 环境，进入被阻止网络的 chroot，以及执行构建脚本。请注意，引导 rustc 需要大量的磁盘空间（rustc 1.83 大约需要 140 GB）。

---

## 74. 神经突

**原文标题**: Neurite

**原文链接**: [https://github.com/satellitecomponent/Neurite](https://github.com/satellitecomponent/Neurite)

Neurite：一个开源项目，开发一种新型数字界面，将分形几何与思维导图技术相融合，以创建一个几乎无限的工作空间。它利用在可定制分形景观上叠加的物理模拟图中连接的节点（文本、图像、视频、代码、AI 代理），提供一种独特的组织思想和想法的方式。

主要功能包括实时分形导航和定制（Mandelbrot 集等）、用于 AI 节点之间协同通信的多代理 UI，以及 FractalGPT，一个以思维图形式响应的 AI Zettelkasten。 Neurite 支持同步知识管理，在思维导图工作空间和基于文本的笔记之间进行双向同步，提供自定义格式和笔记创建。它还与 Wolfram Alpha 和 Wikipedia 等外部知识源集成。

Neural API 允许高级用户使用 Neurite 的函数构建自定义交互。 Neurite Desktop 是一个独立于浏览器的版本，可以在分形画布中打开多个浏览器窗口，并在链接节点中提供无限制的网页浏览。 该平台允许用户将各种媒体类型直接嵌入到 Mandelbrot 集中，并提供用于执行 Neurite 代码的函数调用面板。

---

## 75. 15,000行经过验证的密码学代码现已登陆Python

**原文标题**: 15,000 lines of verified cryptography now in Python

**原文链接**: [https://jonathan.protzenko.fr/2025/04/18/python.html](https://jonathan.protzenko.fr/2025/04/18/python.html)

本文详细介绍了如何成功地将 HACL* 密码学库中经过验证的 15,000 行 C 代码集成到 Python 中，以替换其以前可能存在漏洞的哈希相关基础设施。在 SHA3 漏洞的驱动下，作者带头开展了该项目，历时 2.5 年，并得到了多个个人和 HACS 研讨会的重大贡献。

此次集成对 Python 用户是透明的，并且没有损失任何功能。HACL* 经过调整以满足 Python 的特定要求，包括 Blake2 的新模式、SHA3 的新 API、构建系统抽象、针对分配失败的适当错误管理以及优化的 HMAC 实现。

一个关键的技术挑战在于开发一个完全通用且经过验证的块算法流式 API。这允许高效处理不同长度的密码学输入，并能够提取中间哈希值而不会使算法状态失效。作者强调了在构建过程中确保跨各种编译器和架构兼容性的复杂性，尤其是在 HMAC 和 AVX2 实现方面。内存分配失败处理也通过引入选项类型来传播错误得到解决。

文章最后介绍了通过一个简单的 shell 脚本在 Python 中轻松更新 HACL* 代码的方法，展示了集成的可维护性。作者强调，这种成功的集成证明了经过验证的密码学对于大型项目的成熟度和实际应用准备情况。

---

## 76. 你每天犯下三项重罪 (2013)

**原文标题**: You Commit Three Felonies a Day (2013)

**原文链接**: [https://kottke.org/13/06/you-commit-three-felonies-a-day](https://kottke.org/13/06/you-commit-three-felonies-a-day)

你每天犯下三项重罪

---

## 77. 美国法院记录全文搜索

**原文标题**: Full Text Search of US Court records

**原文链接**: [https://www.judyrecords.com/](https://www.judyrecords.com/)

这篇短文介绍了“judyrecords”——一个提供超过7.4亿美国法院案件访问权限的搜索引擎。它定位为一个免费的公共记录搜索工具。文章还提到该网站有使用条款、信息详情（“信息”）和API访问等部分，暗示了开发者集成该服务的可能性。 总之，这篇文章将judyrecords推广为搜索美国法院记录的资源。

---

## 78. 轻松的电子游戏可以缓解压力和焦虑。

**原文标题**: Cozy video games can quell stress and anxiety

**原文链接**: [https://www.reuters.com/business/retail-consumer/cozy-video-games-can-quell-stress-anxiety-2025-01-27/](https://www.reuters.com/business/retail-consumer/cozy-video-games-can-quell-stress-anxiety-2025-01-27/)

轻松游戏：缓解压力和焦虑的新选择

轻松游戏以其低风险的游戏玩法、舒缓的叙事和令人平静的视觉效果为特点，作为缓解压力和焦虑的工具正日益普及。路透社的文章强调，这些游戏通常专注于诸如耕种、制作、建造和探索等活动，而没有激烈的战斗或压力，从而为玩家提供一种控制感和成就感，这可能具有治疗作用。

文章指出，《动物森友会》、《星露谷物语》和《Unpacking》是该类型的典型例子。这些游戏提供了一个安全且可预测的环境，玩家可以在其中放松身心、表达创造力，并在没有现实世界责任的情况下体验一种联系感。

文章中采访的专家认为，这些游戏中重复、可预测的任务以及进步感可能特别有助于控制焦虑。缺乏时间压力以及对培养和创造的关注使玩家可以摆脱压倒性的想法，并找到一种平和与平静的感觉。此外，社交方面，例如在《动物森友会》中访问朋友的岛屿，可以提供一种社区和联系感，从而对抗孤立感。文章总结说，虽然不能替代专业的心理健康治疗，但轻松游戏可以成为自我保健和减轻压力的宝贵工具。

---

## 79. Ansible: 纯粹的实用主义

**原文标题**: Ansible: Pure (Only in Its) Pragmatism

**原文链接**: [https://andrejradovic.com/blog/ansible/](https://andrejradovic.com/blog/ansible/)

本文对 Ansible 进行了务实的评估，强调了其使用十年后的优势和劣势。Ansible 定位为远程管理系统的工具，通过幂等性来强制执行所需状态。它利用基于 YAML 的 DSL 与 Jinja2 模板，并拥有庞大的社区和通过 Ansible Galaxy 提供的广泛插件库。

作者强调了 Ansible 基于文件的组织结构及其对 YAML 风格的坚持。尽管因其简单性（全局变量，缺乏命名空间）而受到批评，但这种简单性有助于其易用性。Ansible 擅长于自动化跨 Windows 和 Linux 等不同平台的日常系统管理任务，为 API 提供一致的接口。

与 shell 脚本相比，Ansible 提供了可靠性、幂等性和一致的接口。虽然 Puppet、Saltstack 和 Chef 提供了替代方案，但 Ansible 作为功能齐全的无代理解决方案脱颖而出，可实现“顺手拈来”式的配置。然而，其无代理性质意味着它无法强制执行持续合规性。

作者认为 Ansible 最适合确保宠物机器上的特定配置，是 shell 脚本的优秀替代方案。其主要优势包括庞大的社区、丰富的资源和 AI 语言模型支持。在需要全面基础设施即代码的场景中，它表现不足，而 Puppet 或现代 OpenTofu + Packer 方法是首选。尽管存在缺陷，但 Ansible 仍然是跨多台机器执行简单、常见任务（尤其是与 API 交互）的宝贵且不可替代的工具。

---

## 80. 氢燃料电池公交车与纯电动公交车：欧洲公共交通的现实检验

**原文标题**: Hydrogen vs. Battery Buses: A European Transit Reality Check

**原文链接**: [https://cleantechnica.com/2025/04/14/hydrogen-vs-battery-buses-a-european-transit-reality-check/](https://cleantechnica.com/2025/04/14/hydrogen-vs-battery-buses-a-european-transit-reality-check/)

氢燃料巴士与纯电动巴士：欧洲现实考察——以布鲁塞尔和阿伯丁为例，高昂成本和供应问题导致其转向纯电动巴士。科隆利用工业副产品氢，欧塞尔则采用专门的绿色氢生产，但普遍存在氢气泄漏影响气候效益的问题。伍珀塔尔燃烧塑料生产氢的成功性存疑。博尔扎诺和格罗宁根/德伦特等地使用氢燃料巴士，但也大量投资于更具成本效益和实用性的纯电动巴士。埃森/米尔海姆、波城和蒙彼利埃的试验凸显氢燃料巴士的挑战，包括补贴撤回、成本高昂和技术问题。蒙彼利埃甚至因运营成本远高于纯电动巴士而取消氢燃料巴士计划。伦敦保留了氢燃料巴士车队，但新增采购侧重于纯电动车型。总体趋势表明，虽然氢燃料巴士正在探索中，但纯电动巴士正成为欧洲公共交通脱碳更可行和可扩展的解决方案。

---

## 81. 为了性能使用原始循环？

**原文标题**: Raw Loops for Performance?

**原文链接**: [https://www.sandordargo.com/blog/2025/04/16/raw-loops-for-performance](https://www.sandordargo.com/blog/2025/04/16/raw-loops-for-performance)

本文探讨了用 C++20 ranges 替换原始循环进行数据转换的性能影响，起因是作者对 Sean Parent 提倡的原始循环的反感。作者比较了使用 `push_back` 的原始循环、使用 `std::ranges::transform` 的基于 ranges 的转换，以及使用 `emplace_back` 和 `reserve` 进行优化的原始循环。

作者修改了 `ToData` 结构体来跟踪构造函数调用，结果表明 ranges 版本以惰性方式执行转换，从而在转换管道中减少了调用次数，但在将视图物化为向量时引入了额外的移动操作。使用 `emplace_back` 进行优化的原始循环避免了不必要的复制和移动操作，从而实现了最少的构造函数调用。

使用 Quick Bench 的基准测试表明，优化的原始循环比 ranges 版本更快，而原始循环最慢。但是，作者强调，根据用例以及是否存在其他瓶颈（如网络调用或数据库交互），性能差异可能微不足道。文章总结说，虽然 ranges 提供了可读性优势，但它们可能并不总是提供卓越的性能。建议在上下文中衡量性能，并在性能差异不显著时优先考虑可读性。文章建议不要在没有 `reserve` 的情况下使用 `push_back`，因为它会带来性能损失。

---

## 82. 无电源SSD耐久性调查发现数据丢失和性能问题

**原文标题**: Unpowered SSD endurance investigation finds data loss and performance issues

**原文链接**: [https://www.tomshardware.com/pc-components/storage/unpowered-ssd-endurance-investigation-finds-severe-data-loss-and-performance-issues-reminds-us-of-the-importance-of-refreshing-backups](https://www.tomshardware.com/pc-components/storage/unpowered-ssd-endurance-investigation-finds-severe-data-loss-and-performance-issues-reminds-us-of-the-importance-of-refreshing-backups)

Tom's Hardware文章：长期断电SSD存在数据丢失和性能下降风险

这篇文章来自Tom's Hardware，讨论了长期断电的SSD可能存在数据丢失和性能下降的风险。文章重点介绍了科技博主HTWingNut的一项实验，他测试了四块“Leven JS-600”固态硬盘在断电两年后的表现。其中两块硬盘是“全新”的（使用极少），另外两块是“磨损”的（写入了280TB的数据，超过了60TBW的额定值）。

“磨损”的SSD表现出明显的性能下降和文件损坏，验证数据所需的时间明显更长，并出现了坏扇区。“全新”的SSD虽然最初通过了数据完整性检查，但显示出硬件ECC恢复错误的显著增加，表明驱动器的健康状况正在下降。

该实验强调，与传统硬盘不同，SSD在长期断电的情况下可能会丢失数据。SSD的耐久性等级与其在使用后断电时可以保留数据的时间有关。虽然样本量很小，但结果表明，将备份或重要文件长期存储在断电的SSD上存在风险。建议定期刷新SSD上的备份和数据。评论区突出了用户在使用类似问题时的经历，强化了文章的警示信息。一位用户甚至指出，超出TBW额定值使用的SSD更容易发生数据丢失。

---

## 83. 实战大型语言模型

**原文标题**: Hands-On Large Language Models

**原文链接**: [https://github.com/HandsOnLLM/Hands-On-Large-Language-Models](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models)

《动手学大型语言模型》，作者Jay Alammar和Maarten Grootendorst称之为“图解LLM书籍”，是一本使用大型语言模型（LLM）的实用指南，附带GitHub仓库中的代码示例。本书强调视觉学习，包含近300个图表，涵盖了必要的工具和概念，并推荐使用Google Colab来运行示例。

目录涵盖从令牌和嵌入等入门概念到高级主题，如提示工程、使用检索增强生成（RAG）的语义搜索、多模态LLM、微调以及创建文本嵌入模型。该仓库包括使用conda和PyTorch进行本地安装的设置指南。

本书受到了Andrew Ng、Nils Reimers和Josh Starmer等人工智能专家的好评，他们称赞其清晰的解释、实用的例子以及对LLM技术的全面覆盖。评论员强调了它在理解LLM的生成、表示和检索应用方面的价值。

除了核心内容外，作者还提供了关于Mamba、量化、Stable Diffusion、混合专家、推理LLM和DeepSeek-R1等主题的额外指南。文章最后鼓励用户如果觉得本书对他们的研究有价值，请引用它。

---

## 84. 在OS X下使用USB软盘构建条带RAID (2004)

**原文标题**: USB Floppy Disk Striped RAID Under OS X (2004)

**原文链接**: [http://web.archive.org/web/20040202110812/http://ohlssonvox.8k.com/fdd_raid.htm](http://web.archive.org/web/20040202110812/http://ohlssonvox.8k.com/fdd_raid.htm)

2004年，丹尼尔·“刀锋”·奥尔森记录了他使用Mac OS X 10.2.4创建USB软盘驱动器(FDD) RAID的实验。在“为什么不呢？”的驱动下，奥尔森使用了一台iMac、五个Y-E DATA 1X USB软驱、五个随机软盘和一个通用供电USB集线器。他想看看是否可以使用USB软驱创建一个RAID，这个想法在他的Windows XP机器上失败了。

他通过USB集线器将驱动器连接到iMac，并使用磁盘工具以MS DOS格式格式化每个软盘，将它们标记为1-5。使用磁盘工具的条带RAID功能，他将软盘合并为一个4.22 MB的驱动器（重命名为“floppy raid”）。

尽管容量有限且缺乏便携性，奥尔森强调了软盘集群令人惊讶的酷炫速度。他用了32秒传输了一个3.6 MB的MP3文件，比单个驱动器快。他得出结论，他想进一步扩展RAID，但需要更多的USB端口和集线器。

后来，他更新了这个项目，使用Y-E DATA 2X速USB软驱创建了一个更快的FDD RAID，将同一MP3的传输时间缩短到16秒。他还尝试了SONY记忆棒RAID，但发现它不太吸引人。他呼吁捐款以进一步推进他的FDD RAID项目，目标是建立一个127个驱动器的设置。他还推广了他最喜欢的乐队 Riviera 和 JKAT Designs。

---

## 85. 超文本电视

**原文标题**: Hypertext TV

**原文链接**: [https://hypertext.tv/](https://hypertext.tv/)

这似乎是一个虚构的“超文本电视”的菜单或界面，该系统以频道形式呈现各种互动且可能具有实验性的内容。该菜单模仿了老式电视的界面，并带有视觉效果，例如“扫描线”以及可调节的图像设置，如“亮度”、“颜色”、“色调”、“水平”和“垂直”。

超文本电视的核心是频道阵容，范围从01频道到09频道。这些频道提供多样化的内容类型：游戏、艺术、音乐、个人博客、诗歌、“一次性”节目、“探索空间”、档案和一个“杂项”类别。每个频道下列出了具体的节目名称，暗示了内容的古怪和潜在的前卫性（例如，游戏频道的“368只鸡”，音乐频道的“跳舞的老板”，诗歌频道的“第四维思维研究所”）。

该界面提供了导航控件（上/下、选择/调整、左/右），以及“添加网站”或“报告问题”的选项，暗示该平台可能允许用户生成内容或反馈。最后，还有一个“退出菜单”选项，表明这只是一个更大系统中的一个屏幕。“电视指南测试人员名单”的存在表明这是一个原型或实验性系统，而不是商业发布的产品。

---

## 86. 海洋铁肥化

**原文标题**: Ocean Iron Fertilization

**原文链接**: [https://www.whoi.edu/know-your-ocean/ocean-topics/climate-weather/ocean-based-climate-solutions/iron-fertilization/](https://www.whoi.edu/know-your-ocean/ocean-topics/climate-weather/ocean-based-climate-solutions/iron-fertilization/)

铁施肥是一种二氧化碳移除(CDR)技术，它通过向海洋表面添加铁来刺激浮游植物生长。浮游植物像陆地植物一样，利用光合作用将阳光、水和二氧化碳转化为食物和氧气。在许多海洋区域，铁是一种限制性营养物质，添加铁可以引发从太空可见的大规模浮游植物繁殖。

这些繁殖可以从大气中移除大量的二氧化碳，模仿诸如沙尘暴和火山爆发等自然事件。冰芯记录表明，富含铁的尘埃沉降到海洋中与全球气温降低和大气二氧化碳减少之间存在联系。

然而，铁施肥的有效性取决于碳下沉到海洋深处进行长期封存（至少一个世纪）。早期实验表明，添加铁会导致浮游植物繁殖，但碳下沉的程度并非总是被测量。硅藻是一种产生硅基外壳的浮游植物，它们更有可能下沉，从而有可能将碳从大气中移除。

尽管这种方法具有潜力，但也存在潜在风险，例如海洋生态系统中养分分配的改变，或者来自释放毒素的硅藻的有害藻华。科学家们目前正在研究如何透明地进行实验，以及将铁引入海洋表面的意外后果。他们正在开发新技术来调查碳移除并追踪其在海洋中的运动。铁施肥可能是一系列CDR活动中相对便宜的组成部分，但不应取代减少化石燃料使用的迫切需求。

---

## 87. 展示一下：我做了一个能放进二维码里的类Doom游戏

**原文标题**: Show HN: I made a Doom-like game fit inside a QR code

**原文链接**: [https://github.com/Kuberwastaken/backdooms](https://github.com/Kuberwastaken/backdooms)

Kuber Mehta创作了“The Backdooms”，一款受DOOM启发的游戏，被压缩成单个二维码。扫描该二维码即可在网页浏览器中直接启动一个完全可玩的离线游戏，展示了一种创新的轻量级Web应用托管方法。

该项目突出了使用Zlib搭配Gzip解压流和Base64编码的极端压缩技术，以便将游戏装入二维码有限的存储容量中。一个自解压的HTML包装器，利用浏览器的DecompressionStream API，动态地解压并执行游戏。它与支持DecompressionStream的浏览器（Edge、Yandex、Opera）移动设备兼容。

生成二维码涉及使用Python以及`qrcode`和`pillow`库将HTML文件转换为二维码图像。该脚本尝试通过调整二维码大小并使用最低的纠错级别来适应数据。如果数据超过二维码的限制，则会抛出错误。

作者博客上详细介绍了开发过程，其中涉及大量的尝试和错误。该项目以MIT许可证发布，鼓励其他人探索基于二维码的游戏。鸣谢id Software、matttkc和Toby Fox的各自贡献。

---

## 88. 警察算法说莉娜处于“中等”风险，然后她就被杀害了

**原文标题**: Police algorithm said Lina was at 'medium' risk. Then she was killed

**原文链接**: [https://www.bbc.co.uk/news/articles/clyw7g4zxwzo](https://www.bbc.co.uk/news/articles/clyw7g4zxwzo)

这篇BBC新闻文章调查了西班牙女性莉娜的死亡，她被前伴侣杀害，此前警方算法VioGén评估她的风险等级为“中等”。VioGén在西班牙被广泛用于评估家庭暴力 повторного 回溯风险，并相应分配警力资源。该算法使用35个问题将风险分为“可忽略不计”到“极端”。

尽管莉娜的风险评估为“中等”，并且她申请了限制令但被驳回，她还是在家中被杀害。这一事件引发了对VioGén有效性的质疑，以及它是否充分保护了妇女。虽然警方认为VioGén是一种宝贵的工具，可以帮助精确跟踪受害者案件，但批评人士认为这导致决策和资源分配的放弃。

该文章强调了对VioGén缺乏独立审计。Eticas公司进行的一项外部审计，通过访谈和公共数据发现，许多被伴侣杀害的妇女此前都报告过虐待行为，并且被评估为“可忽略不计”或“中等”风险。然而，官员们驳斥了这项审计，理由是其无法访问VioGén数据。

虽然西班牙内政部为VioGén及其对降低妇女在警方保护下遭受暴力概率的积极影响辩护，但文章指出需要进一步研究该算法如何影响警方和法院的决策。莉娜的死亡凸显了在家庭暴力案件中仅仅依赖算法风险评估的潜在失败，以及当系统未能准确预测危险时造成的毁灭性后果。

---

## 89. 法官裁定对手机信号塔数据的全面搜索违宪

**原文标题**: Judge Rules Blanket Search of Cell Tower Data Unconstitutional

**原文链接**: [https://www.404media.co/judge-rules-blanket-search-of-cell-tower-data-unconstitutional/](https://www.404media.co/judge-rules-blanket-search-of-cell-tower-data-unconstitutional/)

内华达州法官裁定“塔状数据倾倒”违宪

内华达州一位法官裁定，“塔状数据倾倒”，即执法部门收集特定时期内连接到某个基站的所有手机的数据的做法，是违宪的。这一裁决出自科里·斯普尔洛克一案，他被指控犯有毒品交易和雇凶杀人罪。该裁决标志着第九巡回法院辖区内的法院首次处理塔状数据倾倒的合宪性问题。

法官米兰达·M·杜认为，塔状数据倾倒违反了第四修正案对非法搜查和扣押的保护。然而，她拒绝压制在斯普尔洛克案件中获得的证据，理由是“善意例外”，辩称警官在当时是出于对搜查令有效性的信任才采取行动的。法官还指出，她的法院似乎是第九巡回法院中第一个得出这一结论的法院。

该案件突出了执法部门破案能力与个人隐私权之间的冲突。虽然塔状数据倾倒可能捕捉到数千名无辜用户的数据，但法官认为，由于涉案警官在签发搜查令时认为其合法，因此该证据可以采纳。密西西比州也曾出现类似的裁决，随后被司法部上诉。最高法院此前曾在*Carpenter v. United States*一案中处理过手机位置数据问题，但拒绝就塔状数据倾倒的具体问题作出裁决。最高法院有可能最终会对塔状数据倾倒问题作出裁决。

---

## 90. 地壳深处有生命

**原文标题**: There's Life Inside Earth's Crust

**原文链接**: [https://www.noemamag.com/theres-life-inside-earths-crust/](https://www.noemamag.com/theres-life-inside-earths-crust/)

凯伦·G·劳埃德的文章《地球地壳内部有生命》探索了迷人的“地内生命”世界，这些微生物在地球深层地下生物圈中茁壮成长。这些生物挑战了我们对生命的理解，它们在没有阳光或氧气的情况下生存，呼吸铀和砷等元素，并且以极长的时间尺度存在，可能长达数十万年。

文章深入探讨了这些缓慢进化的物种如何适应地质节律，并强调了它们的存在对我们理解进化及其驱动因素具有重要意义。地内生命并非孤立存在；它们在调节地球氧气水平、解毒废物以及可能影响地球对气候变化的反应方面发挥着关键作用。

文章强调了这些微生物对气候变化的潜在影响，尤其是在永久冻土地区，融化可能会释放大量碳。此外，文章还提到了利用这些微生物进行碳捕获与封存（CCS）以减缓温室气体排放的潜力。

最后，文章考察了深海采矿对可再生能源技术所需金属可能造成的环境后果，特别是其对影响更广泛行星过程的微生物生态系统的影响。劳埃德强调，迫切需要了解地内生命在塑造我们星球未来方面的作用，尤其是在面对气候变化的情况下。

---

## 91. 横扫巴尔干的英式情景喜剧 (2023)

**原文标题**: The British sitcom that swept through the Balkans (2023)

**原文链接**: [https://blog.samizdata.co/p/how-a-british-sitcom-swept-through-the-balkans](https://blog.samizdata.co/p/how-a-british-sitcom-swept-through-the-balkans)

本文探讨了英国情景喜剧《只有傻瓜和马》（Only Fools and Horses）在巴尔干地区，特别是塞尔维亚、克罗地亚、波斯尼亚和黑山等地出人意料的受欢迎程度。该剧在英国大获成功，但在巴尔干地区的收视率和搜索兴趣甚至更高。在塞尔维亚-克罗地亚语中，它被称为“Mućke”，在马其顿语中被称为“Spletki”。

作者通过该剧在 IMDb 上的高评分和 Google Trends 数据来展示其在巴尔干地区的吸引力。文章提到，扮演 Boycie 的 John Challis 甚至获得了塞尔维亚荣誉公民身份，并制作了一部名为《Boycie in Belgrade》的纪录片。贝尔格莱德甚至有一家以“只有傻瓜”为主题的餐厅，名为“Kafe Mucke”。

文章认为，该剧引起巴尔干观众共鸣的原因在于共享的文化相似性，如足智多谋、创业精神和对向上流动的渴望。来自巴尔干粉丝在各种出版物上的引言强化了这一观点，表明剧中人物的奋斗和愿望具有相关性。

作者最后建议重看《只有傻瓜和马》，同时警告不要观看美国翻拍的试播集。文章还包括关于教皇访问匈牙利和波兰最近选举的后记，以及作者提供数据分析或可视化服务的意愿。

---

## 92. 双子座2.5闪电

**原文标题**: Gemini 2.5 Flash

**原文链接**: [https://developers.googleblog.com/en/start-building-with-gemini-25-flash/](https://developers.googleblog.com/en/start-building-with-gemini-25-flash/)

谷歌已通过 Google AI Studio 和 Vertex AI 上的 Gemini API 发布了 Gemini 2.5 Flash 的早期预览版。此模型以 Gemini 2.0 Flash 为基础，在保持速度和成本效益的同时，显著提高了推理能力。Gemini 2.5 Flash 的一个关键特性是其混合推理能力，允许开发者启用或禁用“思考”过程，甚至为其设置令牌预算（0-24576）。这使得能够对质量、成本和延迟之间的权衡进行细粒度控制。

“思考”过程允许模型分解复杂任务并生成更准确、更全面的答案。当思考预算设置为 0 时，模型可在保持 2.0 Flash 快速速度的同时提高性能。该模型会根据提示的复杂性自动确定思考量。

Gemini 2.5 Flash 在性价比方面表现出色，并在高难度提示上表现出强大的性能。现在可以通过 Google AI Studio、Vertex AI 和 Gemini 应用中的 Gemini API 访问它。谷歌鼓励开发者尝试 `thinking_budget` 参数，并探索可控推理的优势。API 参考、思考指南和代码示例等资源可在开发者文档和 Gemini Cookbook 中找到。

---

## 93. 最著名的二氧化碳吸收剂

**原文标题**: The most famous carbon dioxide absorber

**原文链接**: [https://www.howequipmentworks.com/apollo_13/](https://www.howequipmentworks.com/apollo_13/)

本文讲述了阿波罗13号的故事，突出了二氧化碳吸收器在宇航员生存中的关键作用。阿波罗13号于1970年发射，在氧气罐爆炸时面临一场近乎致命的危机，爆炸使服务舱瘫痪，危及三名宇航员的生命。

由于被迫转移到为两名宇航员在月球短暂停留而设计的登月舱，宇航员们面临着氧气、水和电力供应的日益减少。地球上的工程师们争分夺秒地节约电力和水，而宇航员们则忍受着冰冷的温度和严格限制的饮水量。

一个严峻的挑战出现了：登月舱内二氧化碳水平的上升。登月舱和指令舱都配备了含有氢氧化锂的二氧化碳吸收器来清除二氧化碳。然而，登月舱的供应量不足以维持三名宇航员四天的用量。此外，登月舱使用圆形吸收器容器，而指令舱则使用方形容器。

本文为戏剧性的高潮奠定了基础，宇航员们必须找到一种方法，使方形的指令舱吸收器适应登月舱的圆形端口，这对于他们的生存至关重要。本文突出了克服这种危及生命的情况所需的创造性和紧迫性。

---

## 94. 埃文斯书中DDD示例的UML图

**原文标题**: UML diagram for the DDD example in Evans' book

**原文链接**: [https://github.com/takaakit/uml-diagram-for-ddd-example-in-evans-book](https://github.com/takaakit/uml-diagram-for-ddd-example-in-evans-book)

本项目提供了UML图，展示了Eric Evans的领域驱动设计(DDD)书籍中的示例，特别是货物运输系统。这些图基于GitHub上的`dddsample-core`项目，旨在可视化战略和战术DDD的实现。

本项目包括以下几个图：

*   **用户-系统交互：** 一个序列图，概述了诸如货物追踪和预订等关键交互。
*   **领域模型概览：** 一个类图，描述了基本的领域元素及其关系。
*   **“ABC123”货物的领域对象：** 一个对象图，显示了特定货物实例的快照。
*   **总体结构：** 一个类图，展示了系统结构，包含预订和运输网络上下文。
*   **行为图：** 通信图，详细描述了初始化、货物追踪、货物预订、路线建议和路线分配场景。
*   **有向图：** 可视化预订和运输网络上下文中的分类器和关系。

本项目使用Spring技术，并包含对Evans的DDD书籍、`dddsample-core` GitHub存储库以及必要的软件下载链接（Astah Professional/UML/Viewer 和 m+ 插件）的引用。 本项目在Creative Commons Zero (CC0)下获得许可，其中包含的库在BSD和MIT许可下获得许可。 鼓励用户报告任何已识别的错误。

---

## 95. 达尔文的孩子们在《物种起源》手稿上乱涂乱画 (2014)

**原文标题**: Darwin's children drew all over the “On the Origin of Species” manuscript (2014)

**原文链接**: [https://theappendix.net/posts/2014/02/darwins-children-drew-vegetable-battles-on-the-origin-of-species](https://theappendix.net/posts/2014/02/darwins-children-drew-vegetable-battles-on-the-origin-of-species)

本杰明·布林的《达尔文的孩子们在<物种起源>手稿上乱涂乱画》一文，通过展示达尔文的孩子们在他的手稿和妻子艾玛的日记上所作的绘画和涂鸦，探索了达尔文遗产中轻松的一面。这些有趣的添加物让我们得以一窥达尔文的家庭生活和他开创性工作的背景。

文章重点介绍了在达尔文《物种起源》手稿背面发现的绘画，其中包括归功于他的儿子弗朗西斯的“水果和蔬菜士兵之战”。其他一些画作似乎受到达尔文作品的启发，以惊人的细节描绘了自然。一幅儿童视角下的达尔文家庭住宅图，可能显示了达尔文的“思考路径”，也包含在其中。

艾玛·达尔文的日记被视为了解家庭生活的另一扇窗口，展示了她自己的绘画才华以及孩子们对日记页面的顽皮破坏。

文章还提到了达尔文女儿安妮的悲剧性去世，包括一张与她生活相关的纪念品盒子的照片以及达尔文对她的回忆录中的一段摘录。它将安妮的去世与达尔文信仰的转变联系起来，突出了他的个人生活和科学追求的纠缠。这篇文章强调了记住历史人物的人文背景的重要性。

---

## 96. 分子钟：细菌在光合作用广泛发生前很久就已利用氧气

**原文标题**: Molecular clock: bacteria used oxygen long before widespread photosynthesis

**原文链接**: [https://phys.org/news/2025-04-molecular-clock-analysis-bacteria-oxygen.html](https://phys.org/news/2025-04-molecular-clock-analysis-bacteria-oxygen.html)

本文报道了一项发表在《科学》杂志上的新研究，该研究利用分子钟分析重建了细菌进化的时间线，尤其关注了对氧气的适应。冲绳科学技术大学院大学（OIST）的研究人员及其合作者结合了基因组数据、化石记录和地球的地球化学历史，以了解大约23亿年前大氧化事件（GOE）前后细菌的进化方式。

该研究的关键发现是，一些细菌谱系可能早在GOE之前近9亿年就能利用氧气，表明有氧代谢早于广泛的产氧光合作用。研究团队利用机器学习来预测古代基因组中的氧气利用情况，并考虑了真核生物化石（线粒体和叶绿体）来完善其时间线。

他们的研究结果表明，所有现代细菌的最后共同祖先存在于44-39亿年前。GOE之后，有氧细菌谱系的进化速度快于厌氧细菌谱系，表明氧气在塑造细菌进化中发挥了重要作用。这项研究突出了结合不同类型的数据（基因组、化石、地球化学）和机器学习来理解微生物进化的力量，特别是对于化石记录有限的生物。这种方法有可能被用于研究其他性状及其与地质时期地球不断变化的环境的相互作用。

---

## 97. 如果你用人工智能替我写便条，别指望我会读它。

**原文标题**: If you use AI to write me that note, don't expect me to read it

**原文链接**: [https://www.fastcompany.com/91317959/if-you-use-ai-to-write-me-that-note-dont-expect-me-to-read-it](https://www.fastcompany.com/91317959/if-you-use-ai-to-write-me-that-note-dont-expect-me-to-read-it)

无法访问文章链接。

---

## 98. 如何巧妙地指出老板的错误

**原文标题**: How to Tell Your Boss They're Wrong–Tactfully

**原文链接**: [https://hbr.org/2025/04/how-to-tell-your-boss-theyre-wrong-tactfully](https://hbr.org/2025/04/how-to-tell-your-boss-theyre-wrong-tactfully)

如何委婉地指出老板的错误：一篇哈佛商业评论文章探讨了在不损害职业关系的前提下，如何反驳上级的挑战。文章重点介绍了老板提出员工认为有缺陷或不切实际的策略或想法的情景。

文章解决的核心问题是*如何*有效地表达这些担忧。 它强调需要技巧和勇气来避免对抗。 文章建议，决定*如何*提出你的论点，无论是通过战略性提问还是直接陈述，都至关重要。

关键在于以一种容易接受的方式表达你的异议。文章指出，必须仔细考虑语气、语言和方法，以确保你的信息能够有效地传递，而不会损害你与经理的关系。 本质上，这篇文章提供了向上管理、应对困难对话以及磨练人际交往技能的指导，以便在必要时尊重地挑战老板的想法。

---

## 99. 美国低估了制造业回流的难度。

**原文标题**: America underestimates the difficulty of bringing manufacturing back

**原文链接**: [https://www.molsonhart.com/blog/america-underestimates-the-difficulty-of-bringing-manufacturing-back](https://www.molsonhart.com/blog/america-underestimates-the-difficulty-of-bringing-manufacturing-back)

莫尔森·哈特认为，近期实施的关税不会使制造业回归美国，反而可能损害经济。他基于14个理由，这些理由源于他在美国和中国制造业方面丰富的经验。

核心论点包括：

*   **关税不够高：** 美国制造成本过高，工业供应链薄弱，即使有关税，在中国制造仍然更便宜。
*   **工业供应链薄弱：** 美国缺乏许多商品的强大工业供应链，与其消费供应链不同。必要的零部件主要在亚洲制造。
*   **缺乏技术诀窍：** 美国已经丧失了制造许多产品的知识和专业技能，包括像半导体这样的关键部件。
*   **劳动力效率低下：** 与中国劳动力相比，美国劳动力更昂贵、更不可靠、技能更低。
*   **基础设施不足：** 美国缺乏必要的基础设施，特别是发电和运输网络，以支持制造业的大规模回归。
*   **时间滞后：** 建设新工厂和建立高效生产需要数年时间，超过了当前的总统任期。
*   **不确定性和复杂性：** 频繁的变化和令人困惑的关税实施造成不确定性，阻碍了对美国制造业的投资。
*   **美国人不想要制造业工作：** 作者认为，大多数美国人对制造业工作的艰苦和通常令人不快的性质不感兴趣。
*   **劳动力短缺：** 即使我们将制造业带回美国，也没有足够的工人来填补这些制造业工作。

哈特总结认为，要重振美国制造业，需要转变根本性的方法，解决供应链缺陷、劳动力技能和基础设施限制，而不是仅仅依靠关税。

---

## 100. 微型轮腿机器人

**原文标题**: Micro Wheeled legged Robot

**原文链接**: [https://github.com/MuShibo/Micro-Wheeled_leg-Robot](https://github.com/MuShibo/Micro-Wheeled_leg-Robot)

本文介绍了一种微型轮腿机器人，它是同类产品中最小的。它具有双轮腿，并采用基于 ESP32 的主控板、L6234PD013TR 无刷电机驱动器、用于车轮位置的 AS5600 编码器（I2C 接口）和用于平衡的 MPU6050 IMU（也是 I2C 接口）。该项目包括详细的机械和 PCB 文档，用于制造，并附有零件清单，指明需要 3D 打印/CNC 铣削的组件以及需要购买的组件。

该机器人的软件基于 Arduino IDE，并使用 simpleFOC 库进行电机控制。它通过 WiFi 以 AP 或 STA 模式进行无线通信，并使用 WebSocket 协议进行远程控制。该控制界面可通过各种操作系统上的 Web 浏览器访问。

要使用该机器人，用户需要连接电池、打开电源，并等待涉及电机校准和腿部运动的初始化序列。重启后，他们连接到机器人的 WiFi 网络，并通过特定的 IP 地址访问控制界面。然后，手动稳定机器人，并通过 Web 界面指示其站立，从而实现基于摇杆的控制。该项目是开源的，贡献者为穆世博和李雨峰。

---

