# Hacker News 热门文章摘要 (2025-12-06)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 微型核心Linux：一个带图形桌面的23MB Linux发行版

**原文标题**: Tiny Core Linux: a 23 MB Linux distro with graphical desktop

**原文链接**: [http://www.tinycorelinux.net/](http://www.tinycorelinux.net/)

Tiny Core Linux 是一个高度模块化、超小型的 Linux 发行版，旨在提供一个极简的图形桌面环境。它基于小型内核和根文件系统构建，基础的 "Core" 版本仅 11MB，包含必要的组件。"TinyCore" 在此基础上扩展了基本的 FLTK/FLWM 桌面环境，总计约 16MB。"CorePlus" 提供了一个更简单的入门方式，预先打包了桌面选择和安装的扩展。

Tiny Core 的一个关键理念是用户自定义和控制。它启动速度快，驻留在 RAM 中，允许用户根据需要添加应用程序和硬件支持，可以通过从在线存储库安装扩展或直接编译来实现。这使其适用于各种用途，包括桌面、上网本、设备和服务器。

该项目鼓励社区参与，用户可以通过打包应用程序和硬件支持来做出贡献。Tiny Core Linux 团队提倡开放的开发模式，并通过论坛和 IRC 提供支持。其主要目标是创建一个便携式且可定制的图形桌面，可以从各种介质启动，并支持用户选择的各种应用程序和硬件。

---

## 2. HTML作为论文的可访问格式

**原文标题**: HTML as an Accessible Format for Papers

**原文链接**: [https://info.arxiv.org/about/accessible_HTML.html](https://info.arxiv.org/about/accessible_HTML.html)

arXiv推出“实验性”HTML格式论文，提升残障用户可访问性。研究可访问性是一项关键且紧迫的问题。此举旨在提供PDF的替代方案，因为PDF可能难以被屏幕阅读器和其他辅助技术有效处理。

鉴于arXiv 90%的提交内容为LaTeX格式，转换为HTML格式因LaTeX的可扩展性而面临技术挑战。转换过程需要快速且自动化，以维持arXiv的服务。由于潜在的转换错误，HTML版本被标记为“实验性”，但社区对可访问论文的需求推动了beta版本的发布。

鼓励用户阅读HTML论文并报告问题，优先考虑功能性而非PDF格式的精确复制。HTML格式旨在更好地适应不同的设备，包括移动设备，尽管可能存在布局差异，但比PDF更具优势。

作者可以通过遵循LaTeX标记最佳实践来做出贡献。鼓励开发人员帮助改进LaTeX到HTML的转换过程。出版商和会议组织者可以通过确保推荐的.cls文件供作者使用支持的软件包来提供帮助。

arXiv感谢残疾科学家、LaTeX项目以及NIST的LaTeXML团队的支持和专业知识，使该项目成为可能。该项目旨在不断改进HTML转换过程，并邀请社区持续提供反馈。

---

## 3. GrapheneOS是唯一提供完整安全补丁的安卓操作系统。

**原文标题**: GrapheneOS is the only Android OS providing full security patches

**原文链接**: [https://grapheneos.social/@GrapheneOS/115647408229616018](https://grapheneos.social/@GrapheneOS/115647408229616018)

GrapheneOS是唯一提供完整安全补丁的安卓操作系统。

---

## 4. 触摸大象 – TPUs

**原文标题**: Touching the Elephant – TPUs

**原文链接**: [https://considerthebulldog.com/tte-tpu/](https://considerthebulldog.com/tte-tpu/)

触摸大象 - TPU：本文探讨了谷歌张量处理器（TPU）的开发和设计理念，TPU是专用于深度学习的专用硬件加速器。本文将TPU的成功与摩尔定律和登纳德缩放的放缓进行了对比，突出了领域特定加速的需求。文章认为，TPU的成功植根于对神经网络至关重要的线性代数原语的专注。

本文详细介绍了TPUv1的架构，重点介绍了其256x256矩阵乘法单元（MXU），并强调了该设备精简的设计。第一代TPU优先考虑推理，针对低延迟进行了优化，并消除了不必要的功能，如缓存层级、分支预测和多线程。它利用了脉动阵列来最大化算术强度，并通过仔细的运行时调度来最小化控制开销。

TPUv2解决了TPUv1的局限性，特别是对于训练神经网络而言。它引入了诸如支持反向传播、更高精度梯度和更多样化的激活函数等功能。该设计摆脱了紧密耦合的架构，实现了一个双核芯片，具有可编程向量单元、本地SRAM、每个内核更小的128x128 MXU和高带宽内存（HBM）。还引入了BF16浮点格式的使用，突出了训练期间动态范围的重要性。文章强调了算术进步之外的导线缩放改进如何使设计团队能够专注于关键瓶颈。

---

## 5. Z-Image：拥有60亿参数的强大高效图像生成模型

**原文标题**: Z-Image: Powerful and highly efficient image generation model with 6B parameters

**原文链接**: [https://github.com/Tongyi-MAI/Z-Image](https://github.com/Tongyi-MAI/Z-Image)

Z-Image：一款高效的图像生成模型，拥有60亿参数，采用单流扩散Transformer架构(S3-DiT)，以实现最大化的参数效率。提供三种变体：

*   **Z-Image-Turbo:** 蒸馏版本，在企业级GPU上提供亚秒级推理延迟，并可适配16G VRAM消费级设备。擅长逼真图像生成、双语文本渲染和指令遵循。

*   **Z-Image-Base:** 未蒸馏的基础模型，供社区进行微调和自定义开发。

*   **Z-Image-Edit:** 针对图像编辑任务进行微调，支持使用自然语言提示进行创造性的图生图生成。

Z-Image-Turbo的性能可与领先模型相媲美，并在开源模型中取得了最先进的结果。该模型可以通过PyTorch或Diffusers使用，并提供安装和使用说明。

该模型使用一种新颖的蒸馏算法“Decoupled-DMD”，该算法独立地识别和优化CFG增强（CA）和分布匹配（DM）。此外，它还利用“DMDR”，该算法协同整合了强化学习（RL）和分布匹配蒸馏（DMD），以改善语义对齐、美学质量和高频细节。该项目欢迎社区贡献，提供引用，并积极招聘研究科学家和工程师。

---

## 6. 贝尔格莱德 Linux 安装节

**原文标题**: Linux Instal Fest Belgrade

**原文链接**: [https://dmz.rs/lif2025_en](https://dmz.rs/lif2025_en)

Linux安装节贝尔格莱德站将于2025年12月9日下午6点至晚上9点在贝尔格莱德Jagićeva 5号数学系JAG3教室举行。本次活动旨在帮助参与者在经验丰富的Linux用户的帮助下，在他们的笔记本电脑上安装Linux操作系统。根据兴趣，可能还会提供关于命令行、Git、Web服务和C编程等主题的短期培训。

活动推荐Debian（及其衍生版本，如Ubuntu、Mint和Zorin）或Fedora作为适合初学者的Linux发行版，并指出无论选择哪个特定发行版，都可以运行所有Linux程序。安装节是“终结10”活动的一部分，旨在推广Linux作为Windows 10的友好替代品，Windows 10因其用户不友好的功能和资源需求而受到批评。Linux被认为是一种更环保的替代方案。

参与者可以选择在虚拟机中安装Linux，与现有操作系统并存，或者完全替换Windows。在参加活动之前，选择后两种选项的用户应备份系统分区中的数据。还建议通过DistroSea网站在线浏览不同的Linux发行版。

本次活动由专注于去中心化和自由知识共享的Decentrala组织，随后将于12月16日和23日举办两次额外的Linux初学者活动。参与者还可以捐赠有缺陷的电子设备，由Ponovo组织进行维修，以促进电子垃圾减量。

---

## 7. Infisical（YC W23）正在招聘工程师，构建现代开源安全堆栈

**原文标题**: Infisical (YC W23) Is Hiring Engineers to Build the Modern OSS Security Stack

**原文链接**: [https://www.ycombinator.com/companies/infisical/jobs/2pwGcK9-senior-full-stack-engineer-us-canada](https://www.ycombinator.com/companies/infisical/jobs/2pwGcK9-senior-full-stack-engineer-us-canada)

Infisical（Y Combinator W23孵化的初创公司）正在招聘一名资深全栈工程师，加入他们的团队，构建现代开源安全堆栈。Infisical提供统一的平台，用于管理密钥、证书和特权访问，面向人工智能时代。他们已从Y Combinator和谷歌等投资者处筹集了1900万美元，并为Hugging Face和Lucid等客户提供服务。

理想的候选人应具有3年以上经验，对JavaScript生态系统（React.js、Node.js、TypeScript）有深刻的理解，对细节有极高的关注，并具有行动导向。加分项包括Go语言经验、DevOps知识、初创公司经验、开源贡献和强大的沟通能力。

该职位涉及开发和维护功能，致力于Infisical PKI和SSH等较新的产品线，并在安全领域尝试人工智能应用。Infisical强调快速增长、所有权和解决复杂问题。

Infisical提供具有竞争力的薪酬（薪资16万-25万美元，股权0.05%-0.25%），午餐津贴和工作设备预算等福利，以及远程优先的工作环境，在旧金山设有办公室，并定期举行团队聚会。工程师将在塑造公司的未来、做出关键技术决策和应对可扩展性挑战方面发挥关键作用。

---

## 8. 用Immich自托管照片

**原文标题**: Self-hosting my photos with Immich

**原文链接**: [https://michael.stapelberg.ch/posts/2025-11-29-self-hosting-photos-with-immich/](https://michael.stapelberg.ch/posts/2025-11-29-self-hosting-photos-with-immich/)

作者在使用 Google Photos 同步时遇到问题后，详细介绍了使用 Immich 自行托管照片的历程。他们概述了硬件设置，使用运行 Proxmox 的 Ryzen 7 Mini PC 作为 VM 主机。专门为 Immich 创建了一个运行 NixOS 的新 VM。

作者描述了安装过程，强调了使用 NixOS 进行声明式配置，并利用 Tailscale 通过自定义域名安全地、基于 VPN 访问 Immich 服务器。

文章的大部分内容集中在初始照片导入上。作者最初在使用官方 Immich CLI 时遇到了超时问题，并且不支持 Google Takeout 元数据。随后，他们转向了第三方工具 immich-go，该工具通过在上传期间暂停后台任务并正确处理 Google Takeout 档案，有效地解决了这些问题。

文章还介绍了如何设置 Immich iPhone 应用程序以进行自动照片备份，并指出了应用程序备份设置可能存在的混淆，并建议禁用通知。讨论了备份策略，强调了备份 UPLOAD_LOCATION 全部内容的重要性。

作者将 Immich 与另一个自托管选项 Ente 进行了对比，解释了他们更喜欢 Immich 的更简单范围。他们最后赞扬了 Immich 的速度和整体功能，但建议改进官方 CLI 和 iPhone 应用程序配置。

---

## 9. 使用光电鼠标构建的紧凑型相机

**原文标题**: A compact camera built using an optical mouse

**原文链接**: [https://petapixel.com/2025/11/13/this-guy-built-a-compact-camera-using-an-optical-mouse/](https://petapixel.com/2025/11/13/this-guy-built-a-compact-camera-using-an-optical-mouse/)

Reddit用户Dycus利用旧光电鼠标的传感器，打造了一台功能正常的相机。这并非首个将光电鼠标改装成相机的项目，但Dycus经过约65小时的工作，设计了一款功能齐全的相机，拥有多种功能，并安装在定制的3D打印外壳中。

光电鼠标使用光电管和光线来检测移动，Dycus将其改造为捕捉图像。最终的相机能够捕捉低分辨率（30x30像素）、64级灰度的黑白图像。

尽管分辨率较低，该相机仍具备多种功能，包括单张拍摄、四张连拍和全景（“涂抹”拍摄）等多种拍摄模式，可控曝光以及32kB的机内存储空间，最多可存储48张照片。它还可以记录并将运动转化为绘图，模拟标准鼠标功能。

虽然与现代相机相比图像质量不高，但Dycus强调了趣味性，并将其与Game Boy Camera进行比较。尽管分辨率较低，但得益于更高的色彩深度（64级灰度），该相机能够捕捉到可识别的图像。该项目突出了重新利用技术的创造潜力和DIY项目的乐趣。

---

## 10. 绘制奇观：蜜蜂地图

**原文标题**: Mapping Amazing: Bee Maps

**原文链接**: [https://maphappenings.com/2025/11/06/bee-maps/](https://maphappenings.com/2025/11/06/bee-maps/)

本文题为“绘制惊奇：蜜蜂地图”，详细介绍了数字地图创建的历史，从 20 世纪 80 年代的艰难起源到今天。文章重点介绍了维护准确和最新的地图所面临的挑战，尤其是在需要高度详细“高清地图”的自动驾驶汽车出现之后。

文章随后介绍了蜜蜂地图（Bee Maps），这是一家由 Ariel Seidman 创立的公司，该公司采用了一种独特的地图数据收集方法。蜜蜂地图没有依赖于一小批专用车辆，而是使用由配备了其专用硬件（类似行车记录仪）的用户组成的网络来持续捕获地图数据。驾驶员因其贡献而获得 HONEY 加密货币的激励。

蜜蜂地图的商业模式现在是一种订阅服务，提供硬件，这些硬件提供诸如事故报告视频记录和保险折扣遥测等好处。商业车队获得了更全面的监控功能。

蜜蜂地图的优势在于其庞大且不断增长的数据收集网络，远大于传统地图公司的车队。这使得能够实现更全面的覆盖和更频繁的数据更新。蜜蜂地图将这些数据许可给 TomTom、HERE、Mapbox、Lyft、Trimble、MAXAR 和 VW 等主要参与者。尽管特斯拉等拥有大量车辆摄像头数据的公司可能构成竞争，但蜜蜂地图的开放数据许可和地理覆盖范围使其具有显着优势。

---

## 11. Claude实现的单次反编译超乎预期的有效性

**原文标题**: The unexpected effectiveness of one-shot decompilation with Claude

**原文链接**: [https://blog.chrislewis.au/the-unexpected-effectiveness-of-one-shot-decompilation-with-claude/](https://blog.chrislewis.au/the-unexpected-effectiveness-of-one-shot-decompilation-with-claude/)

本文详细介绍了作者使用 Claude Opus 4.5 在“一次性”反编译工作流程中成功实验《滑雪少年2》的案例。作者开发了一个系统，可以自动将函数输入给 Claude 进行反编译，与手动操作相比，在短时间内取得了显著进展。

该工作流程由四个主要部分组成：**评分器**（根据指令和分支计数等因素对更简单的函数进行优先级排序）、**Claude**（执行反编译）、**工具**（提供 Claude 所需实用程序的类 Unix 脚本）和 **驱动程序**（管理循环、处理错误并记录进度）。该系统成功的关键在于工具中明确、清晰的指令和错误处理，以防止 Claude 卡住。

作者强调了工具中防御性编码的重要性，并强调了通过提示工程和优化的工具实现的 token 效率改进。虽然 Codex 令人失望，但 Claude 能够始终如一地遵循指令和反编译函数的能力显示出巨大的潜力。文章总结说，LLM 可以显著加速反编译项目，将瓶颈从人力转移到计算能力和对高级模型的访问。然而，人类的专业知识对于清理和记录 LLM 生成的代码仍然至关重要，以确保可读性和可维护性。作者鼓励读者为《滑雪少年2》反编译项目做出贡献。

---

## 12. 我如何在国产NanoKVM上发现一个隐藏麦克风

**原文标题**: How I discovered a hidden microphone on a Chinese NanoKVM

**原文链接**: [https://telefoncek.si/2025/02/2025-02-10-hidden-microphone-on-nanokvm/](https://telefoncek.si/2025/02/2025-02-10-hidden-microphone-on-nanokvm/)

本文详细介绍了作者对Sipeed NanoKVM（一款低成本的中国硬件KVM切换器）的安全审计。虽然该设备因其经济性和功能性（允许远程计算机控制，无需在目标机器上安装软件）而受到称赞，但它存在严重的安全缺陷。

作者发现了许多漏洞，包括默认密码、启用带有该默认密码的SSH访问、缺乏CSRF保护、硬编码的加密密钥、依赖中国DNS服务器，以及与Sipeed在中国的服务器进行更新和闭源组件通信。tcpdump和aircrack等黑客工具的存在引起了进一步的担忧。

最令人震惊的是，NanoKVM包含一个隐藏的、高质量的麦克风，没有明确记录，并且预装了所有必要的录音工具。这使得音频录音和潜在的网络流传输变得容易，构成了严重的隐私风险。

作者将这些问题归因于仓促的开发和疏忽，不一定是恶意意图。尽管存在这些问题，该设备的开源特性允许安装自定义软件，并且已经有用户致力于移植Debian和Ubuntu等Linux发行版。作者建议在安装自定义软件时移除麦克风，以提高安全性。

文章最后对各种设备（不仅仅是中国产的设备）中隐藏的功能提出了更广泛的担忧，并强调了苹果和谷歌等大型科技公司在语音助手方面的隐私问题。最后，作者提供了关于如何测试内置麦克风进行验证的说明。

---

## 13. 逃往六十年代旧金山的少年们

**原文标题**: Kids who ran away to 1960s San Francisco

**原文链接**: [https://www.fieldnotes.nautilus.quest/p/the-kids-who-ran-away-to-1960s-san](https://www.fieldnotes.nautilus.quest/p/the-kids-who-ran-away-to-1960s-san)

非营利组织创始人泽尔达在读完《女巫之季》后，回忆起她一时兴起去旧金山公共图书馆拜访的经历，书中讲述了哈克贝利之家，一个20世纪60年代为离家出走的青少年提供的避难所。被创始人拉里·贝格斯牧师的故事所吸引，她发现了离家出走的青少年写给贝格斯的存档信件。

她描述了查阅档案的过程，包括处理脆弱文件的仪式感。沉浸在信件中，她被青少年们绝望的衷心故事和贝格斯富有同情心、不带评判的回应所感动。她反思了这些青少年的潜在生活，以及跨越时空与他们建立联系的感觉。

泽尔达还分享了一个意外的发现，即《女巫之季》的作者大卫·塔尔博特之前也在同一间房间里研究过，查阅了相同的文献。她将20世纪60年代在旧金山寻求新未来的离家出走的青少年，与当今在城市中寻求机会的年轻科技创始人进行了比较。她总结说，这次经历强化了遵循好奇心和探索世界提供的机会的重要性。

最后，她提到哈克贝利之家仍在运营，并提供了捐款方式的信息。她还宣传了自己的非营利组织“鹦鹉螺”，并鼓励读者订阅她的Substack。

---

## 14. Cloudflare 2025年12月5日故障

**原文标题**: Cloudflare outage on December 5, 2025

**原文链接**: [https://blog.cloudflare.com/5-december-2025-outage/](https://blog.cloudflare.com/5-december-2025-outage/)

2025年12月5日，Cloudflare发生了一次25分钟的中断（08:47-09:12 UTC），影响了大约28%的HTTP流量。根本原因是由于与缓解CVE-2025-55182 React Server Components漏洞相关的配置更改触发了一个错误。

具体而言，Cloudflare增加了WAF的缓冲区大小以保护React用户，但同时使用全局配置系统禁用了内部WAF测试工具。在FL1代理中，这种组合导致了一个错误，从而导致HTTP 500错误。规则模块内发生了一个Lua异常，源于尝试执行一个已通过killswitch禁用的规则集操作失败，突显了一个先前未检测到的代码错误。

该事件影响了使用旧版FL1代理并部署了Cloudflare托管规则集的客户。中国网络提供的流量未受影响。

Cloudflare承认这次中断是不可接受的，尤其是在2025年11月18日发生类似事件之后。他们正在优先考虑项目，以防止配置更改对未来产生广泛影响，包括增强的推出和版本控制、简化的紧急措施能力以及“故障开放”错误处理。虽然这些更改未能及时部署以防止本次中断，但Cloudflare正在锁定网络更改，直到更好的缓解和回滚系统到位。下周将发布这些弹性项目的详细分析。

---

## 15. 消失的沉默 (2010)

**原文标题**: The Absent Silence (2010)

**原文链接**: [https://www.ursulakleguin.com/blog/3-the-absent-silence](https://www.ursulakleguin.com/blog/3-the-absent-silence)

在《缺席的沉默》中，厄休拉·勒奎恩讲述了她使用谷歌在线搜索若泽·萨拉马戈的一句特定引言时，遭遇的令人沮丧的经历。几次搜索无果后，她最初怀疑是审查，想象着可能有人因为萨拉马戈的无神论和对宗教人物的批评而删除了这句话。

然而，她发现问题出在她自己的搜索词上；使用准确的短语“上帝是宇宙的沉默”立即产生了所需的结果。这一经历引导她更深入地反思谷歌作为大型信息提供者的角色。

勒奎恩纠结于谷歌的可访问性和秘密性之间的悖论。虽然谷歌提供了浩瀚的知识，但其收集和处理信息的方法仍然是严密保守的商业机密。她将此与公共图书馆进行了对比，后者与公众建立在相互信任的基础上，公开分享他们如何获取和管理信息。

她认为，像谷歌这样的公司，即使怀有善意，也会优先考虑利润和增长，可能将公共利益置于次要地位。这种内在的冲突引发了人们对在秘密面纱下运作的信息来源的信任度担忧。勒奎恩最后质疑，即使是那些运营谷歌的人，是否完全理解他们行为的含义。

---

## 16. 费雪Pixter玩具上的PalmOS

**原文标题**: PalmOS on FisherPrice Pixter Toy

**原文链接**: [https://dmitry.gr/?r=05.Projects&proj=27.%20rePalm#pixter](https://dmitry.gr/?r=05.Projects&proj=27.%20rePalm#pixter)

本文详细介绍了Dmitry.GR将PalmOS移植到 Fisher-Price Pixter Color 和 Pixter Multimedia 玩具上的努力，这些玩具具有彩色屏幕和 ARM SoC。作者最初专注于 Pixter Color，通过逆向工程 ROM 在卡带上创建可启动的 PalmOS 镜像。这涉及到为 ROM 制作特定的头文件，以便被 Pixter 识别。

一个重要的障碍是 Pixter Color 的硬件设计选择，特别是没有字节通道选择线的 16 位外部总线。这使得必须使用 8 位宽的 RAM，从而减慢了内存访问速度。此外，发现 Sharp LH75411 SoC 非常精简，缺少诸如缓存、MMU、MPU 和对齐检查等功能。缺少对齐检查也意味着异常向量固定在 0x00000000。

尽管存在这些限制，但在 SoC 的 16KB TCM 和 32KB eSRAM 的帮助下，成功启动了一个基本的 PalmOS 镜像，用于更快的内存访问。作者还设计了一个带有 NOR 闪存和 RAM 的定制卡带板。整个项目的目标是证明在硬件限制下，在这种意想不到的平台上运行 PalmOS 的可行性。

---

## 17. 精神分裂症患者误将智能冰箱广告当成精神病发作

**原文标题**: Schizophrenia sufferer mistakes smart fridge ad for psychotic episode

**原文链接**: [https://old.reddit.com/r/LegalAdviceUK/comments/1pc7999/my_schizophrenic_sister_hospitalised_herself/](https://old.reddit.com/r/LegalAdviceUK/comments/1pc7999/my_schizophrenic_sister_hospitalised_herself/)

无法访问文章链接。

---

## 18. 奈飞将收购华纳兄弟

**原文标题**: Netflix to Acquire Warner Bros

**原文链接**: [https://about.netflix.com/en/news/netflix-to-acquire-warner-bros](https://about.netflix.com/en/news/netflix-to-acquire-warner-bros)

无法访问文章链接。

---

## 19. Wolfram计算服务

**原文标题**: Wolfram Compute Services

**原文链接**: [https://writings.stephenwolfram.com/2025/12/instant-supercompute-launching-wolfram-compute-services/](https://writings.stephenwolfram.com/2025/12/instant-supercompute-launching-wolfram-compute-services/)

斯蒂芬·沃尔夫勒姆发布 Wolfram 计算服务，这是一种无缝扩展 Wolfram 语言计算的简化方式。它允许用户提交计算任务到 Wolfram 基础设施上运行，从而无需本地资源即可处理计算密集型任务。

主要功能包括 `RemoteBatchSubmit` 函数，该函数自动处理依赖关系并支持符号表达式，从而实现各种结果，如数值数据、图像和视频。用户可以根据核心数和内存选择各种机器配置，或者使用 `RemoteBatchMapSubmit` 利用大规模并行性，将计算分布在多个核心和机器上。

文章提供了示例，展示了如何使用 Wolfram 计算服务执行从计算几何到搜索特定元胞自动机规则的任务。该服务是完全可编程的，允许用户设置机器类型、时间/信用约束和通知等选项。可以通过 Web 仪表板或以编程方式通过 Wolfram 语言监控作业。完成的结果会临时存储，可以使用 CloudPut 永久存储。

Wolfram 还提到了即将推出的 Wolfram HPCKit，该工具使拥有大规模计算设施的组织能够与 RemoteBatchSubmit 集成。未来的计划包括支持同步远程计算以及在大型或异构机器上运行远程内核。本质上，Wolfram 计算服务将超级计算机能力普及给 Wolfram 语言用户，使其可用于广泛的应用。

---

## 20. Gemini 3 Pro：视觉人工智能的前沿

**原文标题**: Gemini 3 Pro: the frontier of vision AI

**原文链接**: [https://blog.google/technology/developers/gemini-3-pro-vision/](https://blog.google/technology/developers/gemini-3-pro-vision/)

Gemini 3 Pro 是 Google DeepMind 最新且功能最强大的多模态 AI 模型，在理解文档、空间关系、屏幕和视频方面表现出最先进的性能。它擅长复杂的视觉推理，并在各种视觉任务中设定了新的基准。

主要进展包括：

*   **文档理解：** Gemini 3 Pro 可以准确解析具有交错图像、手写文本和嵌套表格的复杂、非结构化文档。它可以“反渲染”文档，将其转换为结构化代码，并在表格和图表中执行复杂的推理，甚至在某些基准测试中优于人类。
*   **空间理解：** 该模型表现出强大的空间感知能力，使其能够理解物理世界。它可以指向图像中的特定位置，并提供像素精确的坐标，并使用开放词汇表引用来识别物体，适用于机器人和 AR/XR 等应用。
*   **屏幕理解：** Gemini 3 Pro 的空间能力扩展到理解桌面和移动操作系统屏幕，从而促进重复性任务的自动化、质量保证测试、用户引导和 UX 分析。
*   **视频理解：** 该模型显著提高了视频理解能力，通过高帧率处理捕捉快速细节，并推理因果关系。它可以从长篇视频中提取知识，并将其转化为可运行的应用程序或结构化代码。

实际应用涵盖各个领域，包括教育（解决复杂的图表并提供逐步的家庭作业帮助）、医学影像（在医学推理和影像基准测试中取得最佳性能）以及法律/金融（分析密集的报告和复杂的文件）。

开发者可以控制媒体分辨率，以平衡保真度和成本，使用高分辨率处理详细任务，而使用低分辨率处理简单的任务。开发者可以访问开发者文档或在 Google AI Studio 中试用该模型以开始使用。

---

## 21. 从零开始制造微型0.1cc二冲程发动机

**原文标题**: Making tiny 0.1cc two stroke engine from scratch

**原文链接**: [https://youtu.be/nKVq9u52A-c?si=KVY6AK7tsudqnbJN](https://youtu.be/nKVq9u52A-c?si=KVY6AK7tsudqnbJN)

这篇文章"压根不能算文章。它只是一个标题：“从零开始制造微型0.1cc二冲程发动机”，外加标准的YouTube页脚。

因此，关键信息是某人计划记录完全从零开始制造一台极小0.1cc二冲程发动机的过程，很可能是在YouTube上。如果YouTube上最终有相关内容，预计将涵盖这种微型发动机的设计、制造和组装。目标受众可能是业余爱好者、机械师、工程师以及任何对模型发动机、DIY项目和精密工程感兴趣的人。

---

## 22. 神机 D 原生 Linux 开源移动系统 – Rev. 1.1 硬件架构

**原文标题**: Divine D native Linux open-source mobile system – Rev. 1.1 Hardware Architecture

**原文链接**: [https://docs.dawndrums.tn/blog/dd-rev1.1-arch/](https://docs.dawndrums.tn/blog/dd-rev1.1-arch/)

Divine D Rev. 1.1 对其开源移动系统进行了重大的硬件升级和改进。主要改进包括增加了microSD Express (Spec 7.x)，通过 PCIe 2.0 Gen 2 x1 提供更快的存储速度，以及支持高达 8K 60Hz 的 Micro HDMI 输出，实现高清显示能力。

一个重要的新增功能是集成的 LoRa 收发器，可为 IoT 应用和网状网络实现远距离、低功耗通信。电源管理得到改进，配备了新的负载和电池电源开关，以及一个欠压 (UV) 电池监视器，可防止低电量情况下的启动循环。电池开关可完全断开与负载的连接，并能够在仅使用充电器的情况下启动。

其他功能包括用于增强用户反馈的触觉引擎、用于系统状态的新 LED 指示灯以及用于通用配件连接的扩展型 18 针磁吸式弹簧针接口。mini-PCIe 连接器被 M.2 B-key 连接器取代，用于 GSM 和 4G 模块集成，从而优化了空间。该系统还整合了基于 Rev. 1.0 测试的设计修复，并弃用了 SPI Nor。

---

## 23. 离开英特尔

**原文标题**: Leaving Intel

**原文链接**: [https://www.brendangregg.com/blog//2025-12-05/leaving-intel.html](https://www.brendangregg.com/blog//2025-12-05/leaving-intel.html)

本文宣布作者在英特尔工作三年半后离职，重点介绍了其主要贡献并回顾了这段经历。作者详细介绍了开源贡献，包括AI火焰图和GPU亚秒级偏移热图，以及在Linux发行版中实现堆栈步行的工作。他们还提到了参与eBPF安全监控以及在USENIX SREcon APAC 2023担任领导职务，并发表了六次会议主题演讲。

作者的大部分工作都集中在云计算上。他们参与了110次客户会议，并制定了一项全面的云战略，其中包含33项旨在提高英特尔云竞争力的建议。该战略包括一个19个英特尔团队之间互动的可视化地图，被誉为一种新颖的跨公司视角。

作者承认英特尔由于招聘冻结和公司最艰难的时期而面临挑战。尽管如此，他们对自己的贡献表示满意，并分享了积极的回忆，包括与Linus Torvalds和Pat Gelsinger的互动。他们还提到遇到了Harshad Sane，一位曾在Netflix帮助过他们的云支持工程师，现在也在那里工作。

虽然作者下一步的重点将是执行云战略建议，但他们希望英特尔能够继续推行这些举措，尽管它们面临挑战。作者将其战略和支持材料留给英特尔领导层，祝愿公司成功。

---

## 24. Netflix的AV1之旅：从安卓到电视及其他

**原文标题**: Netflix’s AV1 Journey: From Android to TVs and Beyond

**原文链接**: [https://netflixtechblog.com/av1-now-powering-30-of-netflix-streaming-02f592242d80](https://netflixtechblog.com/av1-now-powering-30-of-netflix-streaming-02f592242d80)

以下是Netflix技术博客文章“Netflix的AV1之旅：从Android到电视及其他”的摘要：

该文章详细介绍了Netflix多年来在其流媒体服务中实施AV1视频编解码器的历程。 与AVC等旧版编解码器相比，AV1提供了显著的压缩效率改进，从而降低了带宽消耗并提高了视频质量，尤其是在互联网连接受限或拥堵的情况下。

Netflix最初在Android移动设备上推出了AV1支持，选择了一个计算需求较低的播放环境，以优化电池寿命和设备兼容性。 这使他们能够获得经验并改进其AV1编码和播放流程。

下一个重要步骤是将AV1支持扩展到电视和其他流媒体设备。 这带来了不同的挑战，因为电视平台具有更广泛的硬件功能。 Netflix与设备制造商和芯片供应商合作，以确保在各种电视型号上实现无缝的AV1播放。 他们专注于优化这些设备的解码器实现。

该文章强调，AV1现在支持约30%的Netflix流媒体播放量。 这种显著的采用归功于Netflix工程师、设备合作伙伴和开源AV1社区 (AOMedia) 的共同努力。 此外，他们继续改进其AV1编码方案和播放策略，以最大限度地提高其对全球观众的好处。 AV1的使用在带宽可用性较低的地区尤其有益，可以提供更好的观看体验。 这段旅程还在继续，Netflix致力于进一步扩大AV1的采用范围，并探索该编解码器的新应用。

---

## 25. 我被监控了吗？——检查你的车牌是否被监视

**原文标题**: Have I been Flocked? – Check if your license plate is being watched

**原文链接**: [https://haveibeenflocked.com/](https://haveibeenflocked.com/)

好的，我已经访问并阅读了 https://haveibeenflocked.com/ 这篇文章。以下是摘要：

HaveIBeenFlocked.com 是一个网站，允许个人检查他们的车牌是否被 Flock Safety 自动车牌识别 (ALPR) 摄像头扫描过。Flock Safety 将其 ALPR 技术推销给执法部门和社区，用于减少犯罪和安全目的。该网站旨在提供关于车辆被收集和存储数据的透明度。

该网站的核心功能是车牌搜索。用户输入他们的车牌号码和州来提交请求。然后，该网站会针对数据库（可能来自公共记录、信息自由法案请求和其他来源）进行检查，以查看该车牌是否已被识别为与特定的 Flock Safety 客户相关联。

文章强调，在网站上找到您的车牌 *并不* 意味着执法部门已经访问了您的数据。它仅表明您的车辆已被订阅组织（可能是邻里协会、房主协会或警察部门）拥有和运营的 Flock Safety 摄像头扫描过。

该网站还提供有关 Flock Safety 技术、数据保留政策和隐私问题的资源和信息。它讨论了滥用的可能性以及了解这种技术如何在当地社区部署和监管的重要性。此外，它还提供有关如何请求访问或删除您在 Flock Safety 中的车牌数据的指南，尽管这些请求的有效性可能有所不同。从本质上讲，该网站使个人能够更了解通过 ALPR 技术对其车辆进行的潜在监控。

---

## 26. Frinkiac – 《辛普森一家》3M截图

**原文标题**: Frinkiac – 3M "The Simpsons" Screencaps

**原文链接**: [https://frinkiac.com/](https://frinkiac.com/)

Frinkiac是一个基于网络的搜索引擎和meme/GIF生成器，专门提供《辛普森一家》的截图。它索引了该动画电视剧的300多万张截图，用户可以通过输入对话或关键词搜索特定时刻。当输入搜索词时，Frinkiac会识别并显示相关的截图以及相关的字幕。

该网站的主要功能是方便创建meme和GIF。用户可以在选定的截图中添加自定义文本来创建meme，或者将多个截图串联起来创建动画GIF。这使得用户可以轻松地引用和重新利用《辛普森一家》中的标志性时刻，用于在线幽默和评论。

本质上，Frinkiac提供了一个可搜索的《辛普森一家》视觉档案，使用户能够快速找到并将该节目的内容重新混合成新的、可共享的格式。庞大的截图数据库以及易于使用的meme和GIF生成工具使其成为该节目的粉丝以创造性的方式参与和分享其内容的流行资源。

---

## 27. Rust 防御性编程模式

**原文标题**: Patterns for Defensive Programming in Rust

**原文链接**: [https://corrode.dev/blog/defensive-programming/](https://corrode.dev/blog/defensive-programming/)

本文介绍了一系列 Rust 中的防御性编程模式，重点在于能够提高代码健壮性并防止错误的惯用法，尤其是在代码演变时。它强调使用编译器来强制执行不变性，并减少对隐式假设的依赖。

这些模式包括：

*   **使用切片模式匹配代替直接索引向量：** 这确保了向量访问与长度检查相结合，防止 panic 并迫使程序员考虑诸如空向量之类的边缘情况。
*   **在初始化期间显式列出所有结构体字段，而不是使用 `..Default::default()`：** 这确保了始终显式处理新字段，防止使用意外的默认值，并在编译时捕获缺失的初始化。或者，解构 Default 实例以获得便利性和安全性之间的平衡。
*   **在 trait 实现（例如 `PartialEq`）中解构结构体：** 此模式确保在结构体定义更改时考虑所有字段，提示开发者决定是否应将新字段包含在 trait 的逻辑中。
*   **对于可能失败的转换，使用 `TryFrom` 代替 `From`：** 这使失败的可能性变得明确，并鼓励快速失败，而不是继续使用可能存在缺陷的数据。
*   **避免在 `match` 语句中使用通配符 `_` 模式：** 强制编译器在向枚举添加新变体时发出警告，提示您显式处理它们。
*   **对于未使用的变量，使用描述性名称代替 `_` 占位符：** 提高代码可读性，并更容易理解哪些变量被跳过以及原因。
*   **临时可变性：** 通过影子和作用域块限制可变变量的作用域。
*   **防御性处理构造器：** 创建一个私有字段，以强制所有代码路径都使用单个构造器来验证结构体成员。对于库，使用 `#[non_exhaustive]` 和内部模块方法进行更严格的控制。

---

## 28. 速度为何重要

**原文标题**: Why Speed Matters

**原文链接**: [https://lemire.me/blog/2025/12/05/why-speed-matters/](https://lemire.me/blog/2025/12/05/why-speed-matters/)

无法访问文章链接。

---

## 29. 保证仅一次处理的幂等键

**原文标题**: Idempotency keys for exactly-once processing

**原文链接**: [https://www.morling.dev/blog/on-idempotency-keys/](https://www.morling.dev/blog/on-idempotency-keys/)

Gunnar Morling的文章讨论了幂等性键，这是一种在分布式系统中实现精确一次处理的方法，即使不能保证精确一次交付。其核心思想是消费者使用这些键来识别和忽略他们已经处理过的重复消息。

文章随后探讨了不同类型的幂等性键：

*   **UUID：** 简单但需要存储所有过去的UUID，这对于高容量系统来说是不切实际的。添加时间戳（UUIDv7或ULID）可以检测“过时”的消息。
*   **单调递增序列：** 对于消费者来说效率更高，因为他们只需要存储已处理的最高键。然而，生成这些序列对于生产者来说可能具有挑战性，尤其是在多线程环境中，可能会产生性能瓶颈。

作者建议使用数据库事务日志来派生单调递增的幂等性键，利用现有的事务序列化。通过使用诸如Debezium之类的变更数据捕获(CDC)工具，生产者可以持久化发送消息的意图，而单线程进程可以根据它们在日志中的位置（例如，Postgres的LSN）分配键。这种方法避免了生产者端直接生成单调递增键相关的瓶颈。

文章最后概述了权衡：UUID适用于要求不高的场景，而基于日志的单调递增序列为高容量系统提供了空间高效的重复检测，但引入了操作复杂性（CDC管道）。

---

## 30. JavaScript多线程缺失的标准库

**原文标题**: The missing standard library for multithreading in JavaScript

**原文链接**: [https://github.com/W4G1/multithreading](https://github.com/W4G1/multithreading)

Multithreading.js 是一个 TypeScript 库，旨在为 JavaScript 带来强大的、受 Rust 启发的并发原语，以解决缺乏标准多线程库的问题。它利用 Web Workers 实现真正的并行性，同时抽象化了诸如工作线程管理、序列化和 SharedArrayBuffer 处理等复杂性。

主要特性包括托管式工作线程池、共享内存原语（互斥锁、读写锁、条件变量、共享 JSON 缓冲区）、模块的作用域导入以及用于高效数据传输的移动语义（可转移对象被移动，其他对象被克隆）。`spawn()` 函数是运行工作线程中任务的主要入口点。

该库强调通过诸如互斥锁、读写锁和条件变量等同步原语来实现安全的数据共享，并推荐使用异步方法以避免阻塞工作线程。SharedJsonBuffer 实现了 JSON 对象的高效共享内存，并使用 Proxies 实现部分更新。它还提供 MPMC 通道，用于工作线程之间的高级通信。

工作线程内的模块加载通过对动态 `import()` 调用的支持而得到简化，可处理外部库和相对文件的路径解析。浏览器兼容性需要跨域隔离才能使用同步原语，这通过特定的服务器标头强制执行。CSP 配置需要进行调整，以允许数据和 blob URL。该库提供了一个全面的 API，用于管理运行时、内存、共享内存和同步。

---

## 31. 伊凡·苏泽兰 Sketchpad 1963 年演示 [视频]

**原文标题**: Ivan Sutherland Sketchpad Demo 1963 [video]

**原文链接**: [https://www.youtube.com/watch?v=6orsmFndx_o](https://www.youtube.com/watch?v=6orsmFndx_o)

提供的文本并非文章，而是YouTube视频底部的标准页脚信息，列出了与YouTube政策、服务条款、版权信息、广告、开发和隐私相关的各种链接。此外，还注明了NFL Sunday Ticket是Google LLC的产品。

本质上，它是出现在YouTube页面底部的样板法律和资源信息。它没有提供关于Ivan Sutherland Sketchpad Demo 1963视频本身的实际内容。总而言之，此文本提供了与YouTube平台相关的法律和信息链接，但未提供有关Ivan Sutherland Sketchpad Demo 1963视频内容的任何信息。

---

## 32. 腺苷在快速抗抑郁作用共同通路上的作用：咖啡悖论

**原文标题**: Adenosine on the common path of rapid antidepressant action: The coffee paradox

**原文链接**: [https://genomicpress.kglmeridian.com/view/journals/brainmed/aop/article-10.61373-bm025c.0134/article-10.61373-bm025c.0134.xml](https://genomicpress.kglmeridian.com/view/journals/brainmed/aop/article-10.61373-bm025c.0134/article-10.61373-bm025c.0134.xml)

本文提出，尽管腺苷与抑郁症和焦虑症之间存在看似矛盾的关联，但它在各种治疗方法的快速抗抑郁作用中起着至关重要的作用。文章将这一观点称为“咖啡悖论”，因为咖啡因是一种众所周知的腺苷拮抗剂，可能会加剧某些人的焦虑，但相反，增强腺苷的策略可能会产生快速的抗抑郁效果。

作者认为，不同的抗抑郁治疗方法，如氯胺酮、睡眠剥夺和电休克疗法（ECT），都会汇聚到影响腺苷信号通路上。他们假设，这些治疗方法虽然机制不同，但最终会导致腺苷水平的增加或腺苷受体活性的增强，从而产生缓解抑郁症状的下游效应。

文章可能讨论了支持该假设的证据，可能包括临床前和临床研究，表明腺苷参与了这些治疗方法的抗抑郁效果。它可能强调了这些治疗方法影响腺苷的潜在机制，例如调节其释放、代谢或受体表达。

作者可能得出结论，靶向腺苷信号传导可能代表了一种有希望的治疗策略，可用于开发新型的、快速起效的抗抑郁药。 需要进一步的研究来充分了解腺苷在抑郁症中的复杂作用，并优化基于腺苷的干预措施的治疗潜力，同时减轻潜在的副作用。“咖啡悖论”强调了腺苷作用的复杂性和细微差别，突出表明在开发此类治疗方法时需要仔细考虑背景和个体差异。

---

## 33. 《椅子公司》是一部关于使用电脑多么有趣的剧。

**原文标题**: 'The Chair Company' Is a Show About How Fun It Is to Use the Computer

**原文链接**: [https://defector.com/the-chair-company-is-a-show-about-how-fun-it-is-to-use-the-computer](https://defector.com/the-chair-company-is-a-show-about-how-fun-it-is-to-use-the-computer)

Brian Feldman的文章《“椅子公司”是一部关于使用电脑乐趣的剧集》分析了由蒂姆·罗宾逊饰演罗恩·特罗斯珀的HBO剧集，突显了其对电脑使用的独特描绘。 该剧有别于以往将互联网用户描绘成“沉迷网络”的社交媒体成瘾者或技术能力不足人士的常见形象。相反，它赞扬了高效在线数据检索和解析这种常被忽视的技能，这是许多普通电脑用户都具备的能力。

Feldman认为，该剧的魅力在于其对平凡数字任务的真实刻画，例如浏览网站页脚和使用高级搜索技术来挖掘信息。 他觉得这部剧很贴近生活，因为它描绘了网络侦查的挫折和胜利，例如在公司网站上搜索晦涩的联系信息。

这篇文章强调，该剧将互联网描绘成一个可以探索的地方，这种技能正变得越来越稀缺，因为网络正集中在大型平台上，以及由人工智能驱动的工具为用户做出选择。 最终，“椅子公司”呈现了一种怀旧的视角，回顾了在互联网上挖掘的乐趣，即使这会导致荒谬和意想不到的情况。 虽然该剧的叙事可能不连贯，但它有效地传达了一个男人的故事，他从让互联网引导他陷入麻烦中找到了快乐。

---

## 34. Show HN: HCB Mobile – 17岁开发的金融App，月处理600万美元

**原文标题**: Show HN: HCB Mobile – financial app built by 17 y/o, processing $6M/month

**原文链接**: [https://hackclub.com/fiscal-sponsorship/mobile/](https://hackclub.com/fiscal-sponsorship/mobile/)

"Show HN"：HCB Mobile发布，一款由17岁Mohamad Mortada为Hack Club Bank (HCB) 开发的财务管理应用。HCB为超过6500个由青年主导的非营利组织、俱乐部和黑客马拉松提供诸如非营利组织地位、银行账户、捐款收集和借记卡等金融服务，每月处理600万美元。

HCB Mobile旨在简化这些组织的财务管理，使他们能够跟踪余额和交易、通过手机接受点击支付捐款、发行/管理借记卡（包括将其添加到数字钱包）、以及上传/匹配收据。

该应用使用Expo (React Native) 构建，允许iOS和Android使用同一代码库。 Mohamad克服了技术挑战，例如创建Expo模块来桥接原生代码和优化技术。他还应对了与Apple和Google的复杂应用程序审查流程，以获得点击支付和推送配置的权利。

Mohamad强调了该应用程序在帮助年轻人运行有影响力的项目中的重要性，并提到HCB也支持成人主导的组织。他鼓励读者下载该应用程序，并强调HCB接受新的非营利组织申请，不收取启动费用或最低余额。

---

## 35. 潮汐比你想象的更奇怪

**原文标题**: Tides are weirder than you think

**原文链接**: [https://signoregalilei.com/2025/11/12/tides-are-weirder-than-you-think/](https://signoregalilei.com/2025/11/12/tides-are-weirder-than-you-think/)

本文解释了潮汐的复杂性，超越了科学课上月球引力的基本解释。文章首先强调了准确预测潮汐对于全球航运的重要性，并肯定了为实现这一目标所付出的历史努力。

文章将复杂性分解为四个层次。首先，它确认了月球引力因差异引力而导致潮汐，在地球相对的两侧产生水的凸起。其次，它解释了太阳的影响，导致了朔望大潮和小潮。第三，地球的倾斜影响潮汐的时间和类型，导致每天一次高潮和一次低潮的情况。最后，也是最重要的，文章强调陆地破坏了理想的天文模型，产生了复杂的波浪模式和区域差异。

这些陆地导致了无潮点的产生，并且在预测潮汐时需要考虑港口和沿海地区的独特形状。历史上的潮汐预测机，例如开尔文勋爵的，通过结合天文组件和本地数据来自动化计算。作者最后承认他们的解释仍然不完整，暗示了涌潮等现象的存在，并提醒读者潮汐比人们通常理解的更为复杂。

---

## 36. 永续合约，详解

**原文标题**: Perpetual futures, explained

**原文链接**: [https://www.bitsaboutmoney.com/archive/perpetual-futures-explained/](https://www.bitsaboutmoney.com/archive/perpetual-futures-explained/)

Patrick McKenzie的《永续合约详解》深入探讨了加密货币市场中永续合约（Perps）的机制和风险，并强调了其在交易量中的主导地位。永续合约允许投机者利用杠杆进行投机，从而降低交易所和做市商的资本要求。与传统期货不同，永续合约没有到期日，并且通过资金费率机制每天多次结算，赢家由输家支付。

文章解释了“基差交易”，即经验丰富的参与者利用永续合约和现货市场之间的价格差异，从资金费率差中获利，同时保持delta中性。这也有助于使永续合约价格与现货价格保持一致。然而，永续合约也存在固有风险，因为其高杠杆（通常超过传统市场的监管限制）以及潜在的清算风险。

McKenzie强调了对交易所信任的重要性，因为做市商需要抵押仓位以保证支付。一个重大风险是自动减仓（ADL），如果输家和交易所的保险基金无法支付所有支出，赢家的利润将被追溯性地减少。这突出了尾部风险：在剧烈的价格波动期间，系统可能没有足够的资金来支付给所有赢家。对于进行基差交易的人来说，ADL尤其痛苦。文章总结说，虽然永续合约为投机和套利提供了机会，但它们需要仔细理解杠杆、清算风险以及自动减仓的潜在风险。

---

## 37. 张伯伦再次阻止其车库门开启器与智能家居集成

**原文标题**: Chamberlain blocks smart home integrations with its garage door openers – again

**原文链接**: [https://www.theverge.com/tech/839294/chamberlain-myq-garage-door-opener-update-blocks-aftermarket-controllers](https://www.theverge.com/tech/839294/chamberlain-myq-garage-door-opener-update-blocks-aftermarket-controllers)

尚博伦集团再次通过其新的Security+ 3.0平台限制智能家居与其车库门开启器的集成。这项技术阻止了Ratgdo和Tailwind等售后控制器连接到苹果HomeKit、亚马逊Alexa和谷歌Home等流行的智能家居平台。这一举动迫使用户使用尚博伦的MyQ应用程序，该程序充斥着广告和订阅，或者使用数量有限的、大多需要付费订阅的批准合作伙伴。

这对尚博伦来说并不新鲜。他们停止了HomeKit桥接器，结束了谷歌助手集成，并阻止了非官方的Home Assistant集成。这使得第三方控制器对想要控制自己硬件的用户更具吸引力。

Security+ 3.0使用完全无线通信，使得第三方配件使用的有线解决方法变得不可能。该公司声称Security+ 3.0保护消费者免受假冒配件的侵害，但第三方制造商和用户认为这是将他们锁定在MyQ生态系统中的一种方式。

虽然尚博伦拥有很大的市场份额，但仍有一些替代方案可用。 Genie和Kwikset提供了更开放的平台。虽然会比以前更复杂，但售后制造商正在研究针对尚博伦新技术的解决方案。一个简单的解决方法是Third Reality的车库门控制器，它使用机械手指按下标准尚博伦遥控器上的按钮。这与Matter集成，并允许任何智能家居系统控制车库门。

---

## 38. 吃豆人和童年奇想的火花

**原文标题**: PC-Man and the spark of childhood wonder

**原文链接**: [https://intotheverticalblank.com/2025/12/02/interview-greg-kuperberg/](https://intotheverticalblank.com/2025/12/02/interview-greg-kuperberg/)

本文探讨了早期PC游戏开发领域以及格雷格·库珀伯格的工作。库珀伯格是一位青少年程序员，在20世纪80年代初为IBM PC创建了三款令人印象深刻的街机游戏：《伞兵》(Paratrooper)、《PC吃豆人》(PC-Man) 和《J-Bird》。

作者史蒂夫·富尔顿回忆起童年时代电子游戏和电脑所点燃的“火花”，并质疑如今的孩子们是否仍然拥有这种火花。 他偶然发现了《PC吃豆人》这款吃豆人的克隆游戏，并对其质量印象深刻，尤其是考虑到当时IBM PC的局限性。《PC吃豆人》甚至超越了雅达利的吃豆人移植版，这促使富尔顿去调查库珀伯格及其公司猎户座软件。

本文重点介绍了库珀伯格开发这些游戏时的年轻（14-15岁）、他使用汇编语言的编程技巧、他直接操作PC内存以提高性能，以及他成功发布三款备受好评的作品。 作者将库珀伯格快节奏的街机游戏与通常与IBM PC相关的更“严肃”的软件进行了对比。

本文描述了库珀伯格在《PC吃豆人》中迷宫的旋转，这是由于PC的屏幕更宽，以及如何使用亚像素抖动技术来创建更多颜色。 文章以富尔顿和库珀伯格之间的电子邮件交流结束，并承诺在故事结尾提供完整的采访。

---

## 39. CHIP-8模拟器制作指南（2020）

**原文标题**: Guide to making a CHIP-8 emulator (2020)

**原文链接**: [https://tobiasvl.github.io/blog/write-a-chip-8-emulator/](https://tobiasvl.github.io/blog/write-a-chip-8-emulator/)

创建 CHIP-8 解释器的概要指南

---

## 40. 让RSS更有趣

**原文标题**: Making RSS More Fun

**原文链接**: [https://matduggan.com/making-rss-more-fun/](https://matduggan.com/making-rss-more-fun/)

本文概述了作者创建 Firefox 扩展程序 “Timewaster Pro” 的过程，该扩展旨在让用户更愉快地消费小型网络的内容，类似于 TikTok 的被动发现体验。作者对传统 RSS 阅读器感到不满，并受到已停用的 StumbleUpon 的启发，构建了一个工具，可以从 RSS 源中随机提供网站，允许用户赞成、反对或举报内容。

其核心功能包括抓取 RSS 源（来自 Kagi 的小型网络 Github）、索引页面，并将其呈现给用户。赞成票会影响网站的展示频率，从而创建一个社区驱动的“高质量”内容过滤器。该扩展程序设有一个排行榜，通过奖励那些提交热门网站的用户来激励用户参与。

该项目使用 FastAPI 和 SQLAlchemy 构建，并采用 SQLite 数据库（因其易用性），优先考虑简单性，避免过度收集数据。作者特意采用了 80 年代末/90 年代初的复古 Apple OS 美学风格，以表明这不是一个严肃的现代服务。虽然对初步结果感到满意，但作者承认存在一些键盘快捷键问题和 manifest.json 的不确定性。源代码将在项目更加稳定后发布。未来的计划包括对内容进行分类以实现个性化推荐，并为被大量反对的网站建立审查队列。

---

## 41. 自闭症的迷惑近亲

**原文标题**: Autism's confusing cousins

**原文链接**: [https://www.psychiatrymargins.com/p/autisms-confusing-cousins](https://www.psychiatrymargins.com/p/autisms-confusing-cousins)

《自闭症的困惑“表亲”》一文中，Awais Aftab探讨了越来越多的人自我诊断或被诊断为自闭症的现象，同时质疑这些诊断的准确性。Aftab认为，许多归因于自闭症的症状，如眼神交流不适、不擅长闲聊以及专注于爱好等，也可能表明其他疾病，主要是焦虑症。

该文章强调了自闭症作为一种诊断的“模仿性病毒式传播”，认为人们被其吸引是因为它似乎涵盖了他们的笨拙、羞涩和社交困难。然而，Aftab强调，选择并非在自闭症和虚无之间，而是在自闭症和一系列其他诊断可能性之间，包括分裂型人格障碍、分裂型人格障碍、强迫症、边缘型人格障碍、社交焦虑症、社交沟通障碍以及创伤相关障碍。

作者随后概述了DSM-5中自闭症的诊断标准，并指出其范围广泛，从重度自闭症到高功能个体。文章区分了自闭症及其“表亲”，解释了每种疾病的特定细微差别。例如，分裂型人格涉及对人际关系的真正不感兴趣，而分裂型人格涉及奇怪的信念和感知体验。强迫型人格源于焦虑驱动的完美主义，而自闭症的常规提供可预测性或感官调节。

最后，文章指出了诊断社交沟通障碍与自闭症的挑战，主要是由于前者缺乏资源和支持，以及临床医生诊断自闭症的实际激励。他还指出，创伤可以模仿自闭症。Aftab的核心信息是鼓励对出现类似自闭症症状的个体进行差异诊断的仔细考量，以确保准确诊断和适当治疗。

---

## 42. 蜕皮代码 (2024)

**原文标题**: Skin-Shedding Code (2024)

**原文链接**: [https://registerspill.thorstenball.com/p/skin-shedding-code](https://registerspill.thorstenball.com/p/skin-shedding-code)

Thorsten Ball的《蜕皮代码》(2024)探讨了“粉碎”代码的概念，这是软件公司Zed常见的做法。与重构不同，粉碎涉及一种更激进的方法：完全重写代码的很大一部分，甚至删除起关键作用的函数，以便以更好的方式重建它们。

文章重点介绍了Zed的这种做法的例子，开发人员自信地删除和重建代码，以满足新的需求或改进现有功能。一个主要的UI框架重写就体现了这一点，最终形成了一个实质性的pull request。作者强调了“没有代码是神圣的”这种心态，使得这种激进的重写成为可能。

虽然承认粉碎代码所需的最初的担忧和信心，但Ball质疑为什么这种做法在Zed如此有效。他思考这种成功是否源于创始人对代码库的深刻理解、他们在文本编辑器开发方面的丰富经验、团队的技能、Rust的使用，或者粉碎本身谨慎的、有范围的性质，从而避免了重建期间的功能蔓延。

最终，Ball得出结论，定期、有范围的粉碎对代码库是有益的。它们消除了累积的垃圾，并允许开发人员从理想状态重新构想各个部分，而不考虑之前的投入。这种不断的更新使代码库保持干净和适应性，就像一条蛇蜕皮一样，不断进化并丢弃不再需要的东西。

---

## 43. YouTube被抓包AI编辑视频并添加误导性AI摘要

**原文标题**: YouTube caught making AI-edits to videos and adding misleading AI summaries

**原文链接**: [https://www.ynetnews.com/tech-and-digital/article/bj1qbwcklg](https://www.ynetnews.com/tech-and-digital/article/bj1qbwcklg)

YouTube未经创作者知情或同意，秘密使用人工智能修改视频，引发里克·贝亚托和雷特·舒尔等知名YouTube用户的批评。YouTube承认，这些包括锐化、磨皮和细微面部调整的人工智能增强功能是“一项有限测试”的一部分。

虽然YouTube声称人工智能增强旨在“澄清、减少噪音并提高整体视频清晰度”，但批评者认为该公司正在误导性地淡化人工智能的参与程度。像塞缪尔·伍利这样的专家强调，机器学习是人工智能的一个子集，这引发了人们对内容真实性的担忧，以及与观众之间信任的潜在侵蚀。

贝亚托和舒尔注意到他们的视频中存在不一致之处，促使他们进行调查并公开表达担忧，从而引发了这一问题。这导致YouTube承认了人工智能实验。

这场争议凸显了一种更广泛的趋势，即人工智能在在线内容到达观众之前对其进行预处理。虽然智能手机公司长期以来一直使用人工智能来增强图像，但未经授权使用人工智能编辑视频引发了伦理问题，尤其是在新闻和教育等准确性和真实性至关重要的领域。虽然像贝亚托这样的一些创作者对YouTube的创新保持乐观，但批评者警告说，未公开的人工智能修饰为媒体操纵和破坏信任树立了一个令人不安的先例。

---

## 44. 65XX系列CPU附加指令 (1996)

**原文标题**: Extra Instructions Of The 65XX Series CPU (1996)

**原文链接**: [http://www.ffd2.com/fridge/docs/6502-NMOS.extra.opcodes](http://www.ffd2.com/fridge/docs/6502-NMOS.extra.opcodes)

这份由亚当·瓦迪编写的文档，详细介绍了65XX/85XX系列CPU中未公开或“非法”的操作码，特别是Commodore官方未认可的操作码。它列出了105个此类操作码（总共256个可能的操作码减去151个合法的操作码），通常被称为未定义、未公开或非官方操作码。

该文档描述了每个未公开操作码的功能、支持的寻址模式、周期数，并提供了等效标准指令的示例代码。这些操作码通常结合了两个标准6502指令的操作。一些讨论的操作码包括：

*   **ASO/SLO:** 对内存执行ASL运算，然后与累加器进行OR运算。
*   **RLA:** 对内存执行ROL运算，然后与累加器进行AND运算。
*   **LSE/SRE:** 对内存执行LSR运算，然后与累加器进行EOR运算。
*   **RRA:** 对内存执行ROR运算，然后与累加器进行ADC运算。
*   **AXS/SAX:** 将A和X进行AND运算，并将结果存储在内存中。
*   **LAX:** 从内存中加载A和X。
*   **DCM/DCP:** 对内存执行DEC运算，然后与A进行CMP运算。
*   **INS/ISC:** 对内存执行INC运算，然后从A中进行SBC运算。
*   **ALR:** A与立即数进行AND运算，然后执行LSR运算。
*   **ARR:** A与立即数进行AND运算，然后执行ROR运算（行为类似于ADC）。
*   **XAA:** 将X传输到A，然后A与立即数进行AND运算。
*   **OAL:** A与#$EE进行OR运算，与立即数进行AND运算，存储在A和X中。
*   **SAX:** A和X进行AND运算，减去立即数，然后存储在X中。
*   **NOP:** 无操作。
*   **SKB:** 跳过下一个字节。
*   **SKW:** 跳过下一个字（两个字节）。
*   **HLT:** 导致微处理器崩溃。
*   **TAS:** 将A和X进行AND运算，得到栈指针，再次与目标地址的一部分进行AND运算，存储在内存中。
*   **SAY:** 将Y寄存器的内容进行AND运算，并将结果存储在内存中。
*   **XAS:** 将X寄存器的内容进行AND运算，并将结果存储在内存中。
*   **AXA:** 将 A AND X AND 操作数目标地址高字节 + 1 的结果存储到内存。
*   **ANC:** A与立即数进行AND运算，根据A的第7位设置进位标志。
*   **LAS:** 将内存与栈指针进行AND运算，并将结果存储在累加器、X寄存器和栈指针中。

作者指出，某些操作码（XAA，OAL）在不同机器上的行为存在一些不一致之处，并警告存在潜在的寻址问题。作者还驳斥了其他来源关于某些操作码存在的说法。

---

## 45. CSS实现的Fizz Buzz

**原文标题**: Fizz Buzz in CSS

**原文链接**: [https://susam.net/fizz-buzz-in-css.html](https://susam.net/fizz-buzz-in-css.html)

本文探讨了仅使用 CSS 解决 Fizz Buzz 问题的方法，特别着眼于以最少的 CSS 代码行数实现，每行一个选择器和声明块。作者 Susam Pal 规定，所有输出文本，包括数字以及 "Fizz" 和 "Buzz" 这两个词，都必须直接来自 CSS 样式表，禁止 HTML 中包含纯文本或依赖列表标记来生成数字。

Pal 提出的解决方案使用四行 CSS：
1. `li { counter-increment: n }` - 初始化并为每个列表项递增计数器 'n'。
2. `li:not(:nth-child(5n))::before { content: counter(n) }` - 在不是 5 的倍数的每个列表项前显示计数器值。
3. `li:nth-child(3n)::before { content: "Fizz" }` - 在 3 的倍数的列表项前显示 "Fizz"。
4. `li:nth-child(5n)::after { content: "Buzz" }` - 在 5 的倍数的列表项后显示 "Buzz"。

文章否定了使用有序列表来隐式提供数字的方法，认为这违反了所有输出都必须来自 CSS 的要求。虽然有些人可能会尝试最小化 CSS 的字节数，但作者专注于最小化行数。提供的解决方案，在最小化（移除空格）后，大小为 152 字节。Pal 挑战读者使用嵌套选择器和替代 HTML 元素等技术来进一步减少代码的字节数。

---

## 46. 阿尔伯特·迈克尔逊的谐波分析仪 (2014) [pdf]

**原文标题**: Albert Michelson's Harmonic Analyzer (2014) [pdf]

**原文链接**: [https://engineerguy.com/fourier/pdfs/albert-michelsons-harmonic-analyzer.pdf](https://engineerguy.com/fourier/pdfs/albert-michelsons-harmonic-analyzer.pdf)

此文档似乎是一个包含元数据和二进制数据的PDF文件。根据标题“阿尔伯特·迈克尔逊的谐波分析仪 (2014)”，该文件可能与阿尔伯特·迈克尔逊的谐波分析仪（一种用于傅里叶分析和合成的机械模拟计算机）有关。然而，文档的内容并非人类可读的文本，而是由PDF结构元素和压缩数据流（可能是图像或字体）组成。因此，无法总结关于迈克尔逊谐波分析仪的*文章*的实际内容，只能总结文件本身的技术特征。它是一个PDF文件（版本1.7），包含各种对象，如交叉引用表、数据流、元数据和页面描述。数据流包含与文档结构和内容相关的压缩信息，可能包括渲染文章所需的文本、图像和字体。

---

## 47. 物理学家证明宇宙并非模拟。

**原文标题**: Physicists prove the Universe isn't a simulation after all

**原文链接**: [https://www.sciencedaily.com/releases/2025/11/251110021052.htm](https://www.sciencedaily.com/releases/2025/11/251110021052.htm)

UBC Okanagan大学物理学家通过数学证明，我们的宇宙不可能是计算机模拟，这对于科幻爱好者来说无疑是一个打击。Mir Faizal博士及其合作者利用哥德尔不完备性定理证明，现实需要“非算法理解”，而这是任何计算都无法复制的。这挑战了流行的模拟假设，该假设认为我们的宇宙是嵌套在另一个宇宙中的模拟。

这项研究超越了将现实视为在空间中移动的物体的传统物理学，深入研究了量子引力，其中空间和时间是从更深层的纯信息“柏拉图领域”中产生的。然而，即使是这种基于信息结构的理论，也无法仅通过计算来描述现实。哥德尔定理强调了“哥德尔真理”的存在，这些真理是真实的，但无法使用算法计算来证明。

科学家们认为，由于物理学的基本定律产生了空间和时间，它们无法被包含在其中。对现实进行完整且一致的描述需要更根本的东西：非算法理解。由于模拟本质上是算法化的，因此基于非算法理解的宇宙不可能是模拟。这项研究将长期争论的模拟假设置于数学和物理理论的基础之上，有可能提供一个明确的答案：宇宙不可能是模拟的。

---

## 48. 2025年编程解谜：AI版 – 彼得·诺维格 著

**原文标题**: Advent of Code 2025: The AI Edition – By Peter Norvig

**原文链接**: [https://github.com/norvig/pytudes/blob/main/ipynb/Advent-2025-AI.ipynb](https://github.com/norvig/pytudes/blob/main/ipynb/Advent-2025-AI.ipynb)

好的，根据标题和有限的上下文，这里有一个简洁的总结：

材料标题为“2025年代码降临：人工智能版 - 作者Peter Norvig”。这表明计算机科学和人工智能领域的知名人物Peter Norvig正在创建一个专注于人工智能的流行代码降临编程解谜系列。

代码降临是每年12月直到圣诞节期间每天发布的一系列编程挑战。这些谜题通常涉及算法思维和问题解决。

这个由Norvig创建并设定在2025年的特定版本，可能会以专门设计用于测试和利用人工智能概念和技术的难题为特色。这可能涉及以下任务：

*   **机器学习：** 训练模型来解决难题、分类数据或预测结果。
*   **自然语言处理：** 分析基于文本的难题、生成回复或理解指令。
*   **搜索与优化：** 开发人工智能代理来导航复杂环境或找到最佳解决方案。
*   **知识表示与推理：** 构建能够推理事实和规则以解决问题的系统。

所提供的存储库信息（“norvig/pytudes”）表明，代码示例、解决方案或支持材料可能在Norvig用户名下的一个名为“pytudes”的公共GitHub存储库中找到。大量的fork和star表明这是一个受欢迎且备受推崇的存储库，暗示了以人工智能为中心的“代码降临”的潜在质量和趣味性。

---

## 49. 大多数技术问题都是人的问题。

**原文标题**: Most technical problems are people problems

**原文链接**: [https://blog.joeschrag.com/2023/11/most-technical-problems-are-really.html](https://blog.joeschrag.com/2023/11/most-technical-problems-are-really.html)

本文认为，许多技术问题源于潜在的人的问题。作者回顾了一次试图重构一个充满技术债务的大型、问题代码库的个人经历，最终意识到核心问题不是技术性的，而是对变革的抵制和管理层缺乏理解。

技术债务通常源于需求定义不清、销售设定的不切实际的截止日期、过时的技术选择、被动的管理决策以及个人主义等因素。作者强调，在尝试解决现有问题之前，首先需要通过防止技术债务的进一步产生来止损。

作者驳斥了工程师在“无政治”真空中工作的理想化概念，强调了向非技术利益相关者沟通技术问题和重构价值的重要性，并需使用商业语言。赢得他们的信任并展示进展至关重要。

文章总结指出，无论选择何种职业道路，高级工程师都需要强大的跨职能协作能力，而这在传统的计算机科学教育中往往被忽视。虽然技术精湛的“工程师中的工程师”很有价值，但将技术专长与识别和规避项目风险的能力相结合的“抬头编码者”对于大型项目同样重要。本质上，在解决复杂的软件开发挑战时，人际交往能力与纯粹的技术能力同样重要，甚至更重要。

---

## 50. Show HN: Kraa – 万能写作应用

**原文标题**: Show HN: Kraa – Writing App for Everything

**原文链接**: [https://kraa.io/about](https://kraa.io/about)

"Show HN: Kraa – 一款适用于所有场景的写作应用" 一文介绍了新的写作应用 Kraa。尽管提供的内容非常有限，但我们可以推断出 Kraa 是一款旨在处理各种写作任务的通用写作工具，正如其标语“适用于所有场景的写作应用”所暗示的那样。它在 Hacker News 上分享（"Show HN"）表明其创建者正在寻求来自技术社区的反馈和关注。在没有更多细节的情况下，我们无法得知其具体功能、目标受众、定价模式或平台可用性，但标题和标语都强烈强调了其涵盖所有写作场景的方法。

---

## 51. Nimony (Nim 3.0) 设计原则

**原文标题**: Nimony (Nim 3.0) Design Principles

**原文链接**: [https://nim-lang.org/araq/nimony.html](https://nim-lang.org/araq/nimony.html)

本文概述了 Nimony 背后的设计原则，Nimony 是一款旨在发展成为 Nim 3.0 的新型编译器，重点关注内存安全、实时性能和简化的语言体验。其核心目标是支持嵌入式系统，这意味着广泛的适用性。

Nimony 强调通过析构函数和移动语义实现自动内存管理（MM），这与 Nim 2.0 的有效方法相呼应。 `mm:atomicArc` 是唯一的 MM 开关，并且正在开发一种新型循环收集，使用 `.cyclic` 编译指示来标记可能循环的对象。

错误处理旨在简化。Nimony 倾向于在对象内编码错误状态，而不是使用异常或和类型。当对象级别的错误指示不可行时，则使用线程局部错误变量。传统的异常处理方式仍然存在，但需要为可能引发异常的例程添加 `{.raises.}` 注解，以显式标记隐藏的控制流。引入了一个新的 `ErrorCode` 枚举，用于跨库的统一错误传播，其设计考虑了映射到标准错误代码的可能性。

内存不足（OOM）错误的处理方式独特：失败的容器会调用可重写的 `oomHandler`。来自 `new` 的空返回值在 `{.raises}` 例程中被视为 `ErrorCode.OutOfMemError`。泛型代码会进行完整的类型检查，利用 Nim 的概念来获得更好的错误消息和 IDE 建议。

并发和并行通过 `spawn` 统一，由调度器在运行时确定。引入并行 for 循环来实现结构化并行。编译器插件促进了元编程，它是 Nim 宏的演变。模块插件可以根据注解转换整个模块。

---

## 52. 使用git rebase --onto的堆叠差异

**原文标题**: Stacked Diffs with git rebase —onto

**原文链接**: [https://dineshpandiyan.com/blog/stacked-diffs-with-rebase-onto/](https://dineshpandiyan.com/blog/stacked-diffs-with-rebase-onto/)

本文阐述了如何使用`git rebase --onto`有效管理堆叠式差异（依赖PR）。堆叠式差异将大型功能分解为更小、可审查的PR，从而提高审查速度和代码质量。挑战在于，当基础分支（通常是`main`）或父功能分支更新时，如何保持这些依赖分支的同步。

作者对比了常规的`git rebase`与`git rebase --onto`，突出了后者能够精确地将特定提交从一个基础移动到另一个基础的能力。常规地在堆叠分支上进行rebase会导致重复提交和冲突。`git rebase --onto`通过指定新的基础、旧的基础和要rebase的分支来避免这种情况，有效地将旧的基础*之后*的提交重放到新的基础之上。

成功的关键在于使用“标记分支”。当创建一个依赖分支（例如，从`feature-1`创建`feature-2`）时，会创建一个指向父分支（`feature-1`）当前状态的标记分支（`feature-2-base`）。在将`feature-1` rebase到`main`之后，`git rebase --onto feature-1 feature-2-base feature-2`会将`feature-2`的提交移动到更新后的`feature-1`上。关键是，然后将标记分支更新为指向新的`feature-1` HEAD。

文章还介绍了在父功能分支合并后清理历史记录的方法，使用交互式rebase（`git rebase -i main`）从依赖分支的历史记录中删除已合并的父分支中的提交。作者强调了强制推送的必要性以及增加合并冲突的可能性，建议不要堆叠太深。尽管增加了复杂性，但文章认为堆叠式差异的优势大于付出的努力。

---

## 53. 弗兰克·盖里去世了

**原文标题**: Frank Gehry has died

**原文链接**: [https://www.bbc.co.uk/news/articles/c5y2p22z9gno](https://www.bbc.co.uk/news/articles/c5y2p22z9gno)

弗兰克·盖里，上世纪最具影响力的建筑师之一，去世，享年96岁。盖里以其前卫和实验性的解构主义风格而闻名，其建筑突破始于他对圣莫尼卡住宅的重新设计，后来因1997年西班牙毕尔巴鄂古根海姆博物馆（覆盖钛金属）而声名鹊起。他对几何形状、未完成材料以及后来的3D建模的非常规使用，创造了引人注目、雕塑般的建筑，挑战了建筑规范。

盖里最具代表性的建筑包括普利兹克音乐厅、盖里大厦、路易威登基金会、布拉格的跳舞的房子、西班牙的马奎斯酒店和洛杉矶的华特迪士尼音乐厅。尽管一些作品最初受到批评，但他挑战传统的渴望成为他遗产的标志。

盖里于1989年荣获普利兹克建筑奖，他的影响超越了美学；毕尔巴鄂古根海姆博物馆引发了“毕尔巴鄂效应”，通过文化投资振兴了当地经济。致敬强调了他通过建筑与人们的情感互动，以及他通过先进技术不断追求冒险的设计。他的遗孀贝塔·伊莎贝尔·阿奎莱拉，两个女儿莱斯利和布里纳，以及两个儿子亚历杭德罗和塞缪尔健在。

---

## 54. 浏览器处理Base64数据的速度有多快？

**原文标题**: How fast can browsers process base64 data?

**原文链接**: [https://lemire.me/blog/2025/11/29/how-fast-can-browsers-process-base64-data/](https://lemire.me/blog/2025/11/29/how-fast-can-browsers-process-base64-data/)

无法访问文章链接。

---

## 55. 我们给5个大语言模型各10万美元炒股8个月

**原文标题**: We gave 5 LLMs $100K to trade stocks for 8 months

**原文链接**: [https://www.aitradearena.com/research/we-ran-llms-for-8-months](https://www.aitradearena.com/research/we-ran-llms-for-8-months)

文章“我们给了5个LLM模型10万美元交易股票8个月”可能探讨了一项真实实验，其中五个大型语言模型(LLM)被给予10万美元（可能是在模拟或真实交易环境中），并被要求在八个月内交易股票。文章的主要目的可能是评估使用人工智能，特别是LLM，进行自动化股票交易的性能和可行性。

文章中预期包含的关键信息包括：

*   **使用的具体LLM模型：** 确定使用了哪些模型（例如，GPT-4，LLaMA等）对于理解实验的参数和潜在偏差至关重要。
*   **LLM模型采用的交易策略：** 如何指示LLM模型进行交易？给予了它们什么数据（例如，新闻，财务报告，市场数据）？它们利用了什么算法或策略？
*   **性能指标：** 如何衡量LLM模型的成功（例如，投资回报率（ROI），夏普比率，最大回撤，相对于基准指数的超额收益）？
*   **遇到的挑战：** 实验期间出现了哪些限制或意外问题？LLM模型在特定市场条件下是否遇到困难？
*   **结果分析：** LLM模型的表现优于还是劣于人类交易者或标准基准？可以得出关于LLM模型在股票交易中的有效性的什么结论？
*   **伦理考量：** 实验是否引起任何伦理问题，例如潜在的市场操纵或不公平优势？

最终，文章旨在提供关于人工智能驱动的股票交易潜力的经验证据和见解，以及当前LLM模型是否能够做出有利可图的投资决策。

---

## 56. Sam Altman的DRAM交易

**原文标题**: Sam Altman’s DRAM Deal

**原文链接**: [https://www.mooreslawisdead.com/post/sam-altman-s-dirty-dram-deal](https://www.mooreslawisdead.com/post/sam-altman-s-dirty-dram-deal)

摩尔定律已死的Tom认为，近期DRAM价格上涨和短缺是由于OpenAI激进采购原始晶圆所致，引发恐慌并加剧了本已脆弱的市场。据报道，2025年10月，OpenAI秘密与三星和SK海力士达成了协议，获得了全球40%的DRAM供应，令业界震惊。作者认为，这一举动，加上OpenAI囤积未完成晶圆而非成品内存模块，表明其意图限制供应，阻碍AI竞赛中的竞争对手。

市场之所以特别脆弱，是因为多种因素耗尽了通常的安全库存：2025年整个夏季的关税不确定性导致采购减少。价格一直在下跌，阻碍了大规模收购。由于担心美国报复，向预算品牌（通常在中国运营）转售旧DRAM制造设备的情况停滞不前。

文章详细描述了这种情况如何导致超大规模企业、原始设备制造商和OpenAI的竞争对手之间出现恐慌性购买。作者预测各种硬件类别将出现严重短缺和价格上涨，并按“倒霉”程度对产品进行排名。RAM和SSD已经出现大幅涨价。预计小型预装PC公司和Radeon GPU（尤其是据报道已取消的RX 9070 GRE 16GB）将受到严重影响。Nvidia GPU有一定的缓冲，但高容量型号已被搁置。笔记本电脑和手机最终也会感受到压力。PlayStation提前计划，而Steam Machine的命运取决于Valve是否提前获得了RAM。作者对OpenAI的财务透明度表示担忧，并敦促进一步调查其活动。

---

## 57. 如果我们的祖先感觉不到像我们一样的疼痛，会怎样？

**原文标题**: What if our ancestors didn't feel pain the way we do

**原文链接**: [https://www.theatlantic.com/magazine/2026/01/human-ancestors-emotion-history/684959/](https://www.theatlantic.com/magazine/2026/01/human-ancestors-emotion-history/684959/)

情感与感官史学家罗布·博迪斯认为，我们不能假定过去的人们以与今天相同的方式体验情感，包括痛苦。他挑战了保罗·埃克曼等心理学家普及的、在皮克斯动画电影《头脑特工队》等媒体中得到体现的普世的、与生俱来的情感的观点。博迪斯认为，将我们当前的情感理解投射到历史人物身上是不准确的，因为人性的可变的，并受特定文化和历史背景的影响。

他提出了“体验相对性”，认为在不同时代，人类的所有感受和感知体验对我们来说都是陌生的。他借鉴了神经科学，参考了莉萨·费尔德曼·巴雷特的研究，该研究强调大脑的可塑性及其对文化塑造的“概念和类别”的依赖，以创造情感。

博迪斯用中世纪木匠敲到拇指的例子来说明，事件的频率、宗教信仰和对痛苦的文化理解等因素如何影响他对疼痛的体验。他提倡一种多学科的方法，结合艺术史、神学和考古学来重建塑造过去体验的条件。最终，博迪斯的作品质疑了“人”的定义的本身，尤其是在人工智能进步的背景下，并鼓励人们更深入地了解人类在不同时代经历的多样性。

---

## 58. UniFi 5G

**原文标题**: UniFi 5G

**原文链接**: [https://blog.ui.com/article/introducing-unifi-5g](https://blog.ui.com/article/introducing-unifi-5g)

UniFi 5G Max 系列旨在提供强大、多功能且易于部署的 5G 网络解决方案。其设计时尚，且能在各种环境中高效运行。

---

## 59. Framework Laptop 13 通过升级套件获得12核ARM处理器

**原文标题**: Framework Laptop 13 gets ARM processor with 12 cores via upgrade kit

**原文链接**: [https://www.notebookcheck.net/Framework-Laptop-13-gets-ARM-processor-with-12-cores-via-upgrade-kit.1177930.0.html](https://www.notebookcheck.net/Framework-Laptop-13-gets-ARM-processor-with-12-cores-via-upgrade-kit.1177930.0.html)

MetaComputing推出基于ARM架构的Framework Laptop 13和迷你PC升级方案，为Intel、AMD和骁龙X系列处理器提供替代方案。该升级套件的主板采用CIX CP8180芯片组，拥有8个ARM Cortex-A720性能核心（高达2.6 GHz加速）和4个Cortex-A520效率核心，共计12个核心。它还包括一个拥有十个核心的ARM Immortalis-G720 GPU和一个具有30 TOPS性能的AI加速器。

虽然性能可能无法与骁龙X Elite或旗舰智能手机芯片相媲美，但应该足以满足日常任务。然而，早期测试表明空闲功耗较高（约16W），可能会影响与Framework Laptop 13的55Wh电池搭配时的电池续航时间。 这项升级可能最吸引开发者。

MetaComputing ARM AI PC 套件已在线发售。配备16GB RAM、1TB SSD和一个迷你PC机箱的基础型号售价为549美元。包含Framework Laptop 13的捆绑包售价为999美元。升级至32GB RAM需要额外支付100美元。全球免费送货，但价格不包括进口费用和税费。

---

## 60. 宝马PHEV：安全熔断器更换费用极其昂贵

**原文标题**: BMW PHEV: Safety fuse replacement is extremely expensive

**原文链接**: [https://evclinic.eu/2025/12/04/2021-phev-bmw-ibmucp-21f37e-post-crash-recovery-when-eu-engineering-becomes-a-synonym-for-unrepairable-generating-waste/](https://evclinic.eu/2025/12/04/2021-phev-bmw-ibmucp-21f37e-post-crash-recovery-when-eu-engineering-becomes-a-synonym-for-unrepairable-generating-waste/)

无法访问文章链接。

---

## 61. 为什么你的模型这么大？ (2023)

**原文标题**: Why are your models so big? (2023)

**原文链接**: [https://pawa.lt/braindump/tiny-models/](https://pawa.lt/braindump/tiny-models/)

文章《为什么你的模型这么大？(2023)》质疑了所有应用都需要数十亿参数的大型语言模型（LLM）的必要性。文章承认在需要通用性和类人响应的任务（例如，聊天机器人）中需要更大的模型，但作者认为，许多用例，如SQL自动完成或结构化数据提取，都可以由更小的、特定于任务的模型有效地处理。这些任务通常需要有限的上下文窗口，并不依赖于广泛的通用知识。

核心论点围绕大型模型的高推理成本。这包括原始计算能力和部署所需的基础设施，导致每次用户与模型交互时都会产生大量费用。作者设想了一个由更小的、更专业的模型主导的未来，这些模型甚至可以在浏览器中训练和部署。这种方法将大大降低推理成本，并使LLM对于特定的、定义明确的任务更易于访问和高效。作者对这些较小模型的潜力持乐观态度，认为即使只有1500万个参数的模型也足以满足许多实际应用的需求。

---

## 62. DNS over TLS with LetsEncrypt

**原文标题**: DNS over TLS with LetsEncrypt

**原文链接**: [https://blog.hardill.me.uk/2025/12/06/dns-over-tls-with-letsencrypt/](https://blog.hardill.me.uk/2025/12/06/dns-over-tls-with-letsencrypt/)

生成摘要出错

---

## 63. 法官暗示自由软件保护协会在Vizio GPL案件中胜诉

**原文标题**: Judge Signals Win for Software Freedom Conservancy in Vizio GPL Case

**原文链接**: [https://fossforce.com/2025/12/judge-signals-win-for-software-freedom-conservancy-in-vizio-gpl-case/](https://fossforce.com/2025/12/judge-signals-win-for-software-freedom-conservancy-in-vizio-gpl-case/)

本文探讨了软件自由保护协会 (SFC) 起诉 Vizio 据称违反通用公共许可证 (GPL) 的案件，原因是 Vizio 未能为其 SmartCast 电视中使用的 Linux、BusyBox 和其他 GPL 许可软件提供源代码。该案件的关键在于 Vizio 未向消费者提供源代码，而这是 GPL 许可证的要求。

加州法官发布了一项初步裁决，支持 SFC 的立场，认为 Vizio 有义务提供源代码。然而，该裁决并非最终裁决，尚待进一步讨论。

本文强调，法律先例通常支持像 GPL 这样的开源许可条款。它重点介绍了过去的 GPL 执行诉讼，特别是软件自由法律中心针对 Monsoon Multimedia、Xterasys 和 Verizon 等公司提起的诉讼，这些诉讼均以合规承诺告终。

本文还指出，现已被沃尔玛收购的 Vizio 拥有足够的资源来进行强有力的法律辩护。文章指出，沃尔玛计划将 Vizio 打造为沃尔玛和山姆会员店独有的自有品牌。

---

## 64. 富有同情心的老顽固：为何我们必须扎根现实世界

**原文标题**: Compassionate Curmudgeon: Why we must root ourselves in the real world

**原文链接**: [https://theamericanscholar.org/compassionate-curmudgeon/](https://theamericanscholar.org/compassionate-curmudgeon/)

罗伯特·扎列茨基的《富有同情心的老顽固》通过大卫·贝瑟·伍兹的新传记，探索了阿图尔·叔本华的生活和哲学。文章强调了叔本华对“Selbstdenken”（独立思考）的坚持，这与简单接受既定观念形成对比，他挑战黑格尔的失败尝试就是例证。

叔本华以其悲观主义和孤独著称，他认为生活本质上充满痛苦，最好从未出生。扎列茨基认为，这种看似黯淡的观点源于叔本华对扎根于现实世界并将推理建立在具体经验而非抽象理想之上的强调。

叔本华的哲学围绕着“生存意志”，这是一种不断追求自我保护和繁衍的斗争，驱动着人类的存在。然而，这种斗争被同情心所缓和，叔本华认为同情心是人类经验的一个基本方面。这种同情心促使他倡导废除奴隶制、监狱改革和动物权利，反映了他尽量减少伤害和帮助他人的信念。尽管叔本华被认为是厌世者，但他的同代人认识到他潜在的同情心，扎列茨基认为，鉴于当今世界的状况，这种品质可能会与今天的读者产生更强烈的共鸣。

---

## 65. 框架赞助CachyOS

**原文标题**: Framework Sponsors CachyOS

**原文链接**: [https://discuss.cachyos.org/t/framework-sponsorship-for-cachyos/19376](https://discuss.cachyos.org/t/framework-sponsorship-for-cachyos/19376)

CachyOS宣布获得Framework赞助，硬件合作助力开源Linux发展

---

## 66. 肾移植患者死于狂犬病捐献者器官

**原文标题**: Kidney Recipient Dies After Transplant from Organ Donor Who Had Rabies

**原文链接**: [https://www.nytimes.com/2025/12/06/health/rabies-death-skunk-kidney-transplant.html](https://www.nytimes.com/2025/12/06/health/rabies-death-skunk-kidney-transplant.html)

无法访问文章链接。

---

## 67. Show HN: Pbnj – A minimal, self-hosted pastebin you can deploy in 60 seconds

**原文标题**: Show HN: Pbnj – A minimal, self-hosted pastebin you can deploy in 60 seconds

**原文链接**: [https://pbnj.sh/](https://pbnj.sh/)

生成摘要时出错

---

## 68. Spectral rendering, part 3: Spectral vs. RGB

**原文标题**: Spectral rendering, part 3: Spectral vs. RGB

**原文链接**: [https://momentsingraphics.de/SpectralRendering3Results.html](https://momentsingraphics.de/SpectralRendering3Results.html)

生成摘要时出错

---

## 69. Roko's Dancing Basilisk

**原文标题**: Roko's Dancing Basilisk

**原文链接**: [https://boston.conman.org/2025/12/02.1](https://boston.conman.org/2025/12/02.1)

生成摘要时出错

---

## 70. Build your own compressed-sensing 1-pixel camera

**原文标题**: Build your own compressed-sensing 1-pixel camera

**原文链接**: [https://www.instructables.com/Single-Pixel-Camera-Using-an-LED-Matrix/](https://www.instructables.com/Single-Pixel-Camera-Using-an-LED-Matrix/)

生成摘要时出错

---

## 71. NeurIPS 2025 Best Paper Awards

**原文标题**: NeurIPS 2025 Best Paper Awards

**原文链接**: [https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/](https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/)

生成摘要时出错

---

## 72. Influential study on glyphosate safety retracted 25 years after publication

**原文标题**: Influential study on glyphosate safety retracted 25 years after publication

**原文链接**: [https://www.lemonde.fr/en/environment/article/2025/12/03/influential-study-on-glyphosate-safety-retracted-25-years-after-publication_6748114_114.html](https://www.lemonde.fr/en/environment/article/2025/12/03/influential-study-on-glyphosate-safety-retracted-25-years-after-publication_6748114_114.html)

生成摘要时出错

---

## 73. StardustOS: Library operating system for building light-weight Unikernels

**原文标题**: StardustOS: Library operating system for building light-weight Unikernels

**原文链接**: [https://github.com/StardustOS](https://github.com/StardustOS)

生成摘要时出错

---

## 74. Why we built Lightpanda in Zig

**原文标题**: Why we built Lightpanda in Zig

**原文链接**: [https://lightpanda.io/blog/posts/why-we-built-lightpanda-in-zig](https://lightpanda.io/blog/posts/why-we-built-lightpanda-in-zig)

生成摘要时出错

---

## 75. Why are 38 percent of Stanford students saying they're disabled?

**原文标题**: Why are 38 percent of Stanford students saying they're disabled?

**原文链接**: [https://reason.com/2025/12/04/why-are-38-percent-of-stanford-students-saying-theyre-disabled/](https://reason.com/2025/12/04/why-are-38-percent-of-stanford-students-saying-theyre-disabled/)

生成摘要时出错

---

## 76. CUDA-l2: Surpassing cuBLAS performance for matrix multiplication through RL

**原文标题**: CUDA-l2: Surpassing cuBLAS performance for matrix multiplication through RL

**原文链接**: [https://github.com/deepreinforce-ai/CUDA-L2](https://github.com/deepreinforce-ai/CUDA-L2)

生成摘要时出错

---

## 77. The Debug Adapter Protocol is a REPL protocol in disguise

**原文标题**: The Debug Adapter Protocol is a REPL protocol in disguise

**原文链接**: [https://zignar.net/2025/06/23/debug-adapter-protocol-is-a-repl-protocol/](https://zignar.net/2025/06/23/debug-adapter-protocol-is-a-repl-protocol/)

生成摘要时出错

---

## 78. Synadia and TigerBeetle Pledge $512k to the Zig Software Foundation

**原文标题**: Synadia and TigerBeetle Pledge $512k to the Zig Software Foundation

**原文链接**: [https://tigerbeetle.com/blog/2025-10-25-synadia-and-tigerbeetle-pledge-512k-to-the-zig-software-foundation/](https://tigerbeetle.com/blog/2025-10-25-synadia-and-tigerbeetle-pledge-512k-to-the-zig-software-foundation/)

生成摘要时出错

---

## 79. Ghostty is now non-profit

**原文标题**: Ghostty is now non-profit

**原文链接**: [https://mitchellh.com/writing/ghostty-non-profit](https://mitchellh.com/writing/ghostty-non-profit)

生成摘要时出错

---

## 80. Kenyan court declares law banning seed sharing unconstitutional

**原文标题**: Kenyan court declares law banning seed sharing unconstitutional

**原文链接**: [https://apnews.com/article/kenya-seed-sharing-law-ruling-ad4df5a364299b3a9f8515c0f52d5f80](https://apnews.com/article/kenya-seed-sharing-law-ruling-ad4df5a364299b3a9f8515c0f52d5f80)

生成摘要时出错

---

## 81. Valve reveals it’s the architect behind a push to bring Windows games to Arm

**原文标题**: Valve reveals it’s the architect behind a push to bring Windows games to Arm

**原文链接**: [https://www.theverge.com/report/820656/valve-interview-arm-gaming-steamos-pierre-loup-griffais](https://www.theverge.com/report/820656/valve-interview-arm-gaming-steamos-pierre-loup-griffais)

生成摘要时出错

---

## 82. Intellectual Fly Is Open

**原文标题**: Intellectual Fly Is Open

**原文链接**: [https://bcantrill.dtrace.org/2025/12/05/your-intellectual-fly-is-open/](https://bcantrill.dtrace.org/2025/12/05/your-intellectual-fly-is-open/)

生成摘要时出错

---

## 83. Show HN: Radioactive Pooping Knights

**原文标题**: Show HN: Radioactive Pooping Knights

**原文链接**: [https://minichessgames.com/#/play/pooping-knights](https://minichessgames.com/#/play/pooping-knights)

生成摘要时出错

---

## 84. Show HN: Tacopy – Tail Call Optimization for Python

**原文标题**: Show HN: Tacopy – Tail Call Optimization for Python

**原文链接**: [https://github.com/raaidrt/tacopy](https://github.com/raaidrt/tacopy)

生成摘要时出错

---

## 85. It’s time to free JavaScript (2024)

**原文标题**: It’s time to free JavaScript (2024)

**原文链接**: [https://javascript.tm/letter](https://javascript.tm/letter)

生成摘要时出错

---

## 86. Show HN: Onlyrecipe 2.0 – I added all features HN requested – 4 years later

**原文标题**: Show HN: Onlyrecipe 2.0 – I added all features HN requested – 4 years later

**原文链接**: [https://onlyrecipeapp.com/?url=https://www.allrecipes.com/turkish-pasta-recipe-8754903](https://onlyrecipeapp.com/?url=https://www.allrecipes.com/turkish-pasta-recipe-8754903)

生成摘要时出错

---

## 87. The Forgotten Roman Ruins of the ‘Pompeii of the Middle East’

**原文标题**: The Forgotten Roman Ruins of the ‘Pompeii of the Middle East’

**原文链接**: [https://news.artnet.com/art-world/huge-jerash-jordan-pompeii-middle-easy-2708480](https://news.artnet.com/art-world/huge-jerash-jordan-pompeii-middle-easy-2708480)

生成摘要时出错

---

## 88. Wine 11.0 RC1 – Run Windows Applications on Linux, BSD, Solaris and macOS

**原文标题**: Wine 11.0 RC1 – Run Windows Applications on Linux, BSD, Solaris and macOS

**原文链接**: [https://gitlab.winehq.org/wine/wine/-/releases/wine-11.0-rc1](https://gitlab.winehq.org/wine/wine/-/releases/wine-11.0-rc1)

生成摘要时出错

---

## 89. 为Plush编程语言构建复制式垃圾回收器

**原文标题**: Building a Copying GC for the Plush Programming Language

**原文链接**: [https://pointersgonewild.com/2025-11-29-building-a-copying-gc-for-the-plush-programming-language/](https://pointersgonewild.com/2025-11-29-building-a-copying-gc-for-the-plush-programming-language/)

生成摘要时出错

---

## 90. How elites could shape mass preferences as AI reduces persuasion costs

**原文标题**: How elites could shape mass preferences as AI reduces persuasion costs

**原文链接**: [https://arxiv.org/abs/2512.04047](https://arxiv.org/abs/2512.04047)

生成摘要时出错

---

## 91. PGlite – Embeddable Postgres

**原文标题**: PGlite – Embeddable Postgres

**原文链接**: [https://pglite.dev/](https://pglite.dev/)

生成摘要时出错

---

## 92. Show HN: I was reintroduced to computers: Raspberry Pi

**原文标题**: Show HN: I was reintroduced to computers: Raspberry Pi

**原文链接**: [https://airoboticist.blog/2025/12/01/i-was-reintroduced-to-computers-raspberry-pi/](https://airoboticist.blog/2025/12/01/i-was-reintroduced-to-computers-raspberry-pi/)

生成摘要时出错

---

## 93. Ways of Seeing by John Berger

**原文标题**: Ways of Seeing by John Berger

**原文链接**: [https://www.ways-of-seeing.com/](https://www.ways-of-seeing.com/)

生成摘要时出错

---

## 94. Anthropic acquires Bun

**原文标题**: Anthropic acquires Bun

**原文链接**: [https://bun.com/blog/bun-joins-anthropic](https://bun.com/blog/bun-joins-anthropic)

生成摘要时出错

---

## 95. Tunnl.gg

**原文标题**: Tunnl.gg

**原文链接**: [https://tunnl.gg](https://tunnl.gg)

生成摘要时出错

---

## 96. The differences between an IndyCar and a F1 car

**原文标题**: The differences between an IndyCar and a F1 car

**原文链接**: [https://www.openwheelworld.net/en/indycar101/76/IndyCar_vs_Formula_1_cars](https://www.openwheelworld.net/en/indycar101/76/IndyCar_vs_Formula_1_cars)

生成摘要时出错

---

## 97. I have been writing a niche history blog for 15 years

**原文标题**: I have been writing a niche history blog for 15 years

**原文链接**: [https://resobscura.substack.com/p/why-i-have-been-writing-a-niche-history](https://resobscura.substack.com/p/why-i-have-been-writing-a-niche-history)

生成摘要时出错

---

## 98. At IT School with Apple Lisa

**原文标题**: At IT School with Apple Lisa

**原文链接**: [https://blisscast.wordpress.com/2024/06/04/apple-lisa-gui-wonderland-3/](https://blisscast.wordpress.com/2024/06/04/apple-lisa-gui-wonderland-3/)

生成摘要时出错

---

## 99. Trick users and bypass warnings – Modern SVG Clickjacking attacks

**原文标题**: Trick users and bypass warnings – Modern SVG Clickjacking attacks

**原文链接**: [https://lyra.horse/blog/2025/12/svg-clickjacking/](https://lyra.horse/blog/2025/12/svg-clickjacking/)

生成摘要时出错

---

## 100. Transparent leadership beats servant leadership

**原文标题**: Transparent leadership beats servant leadership

**原文链接**: [https://entropicthoughts.com/transparent-leadership-beats-servant-leadership](https://entropicthoughts.com/transparent-leadership-beats-servant-leadership)

生成摘要时出错

---

