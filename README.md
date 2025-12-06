# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-12-06.md)

*最后自动更新时间: 2025-12-06 17:46:40*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 2 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 3 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 4 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 5 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 6 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 7 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 8 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 9 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 10 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 11 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 12 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 13 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 14 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 15 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 16 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 17 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 18 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 19 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 20 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 21 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 22 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 23 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 24 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 25 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 26 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 27 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 28 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 29 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 30 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 31 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 32 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 33 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 34 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 35 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 36 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 37 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 38 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 39 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 40 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 41 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 42 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 43 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 44 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 45 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 46 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 47 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 48 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 49 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 50 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 51 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 52 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 53 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 54 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 55 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 56 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 57 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 58 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 59 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 60 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 61 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 62 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 63 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 64 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 65 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 66 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 67 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 68 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 69 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 70 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 71 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 72 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 73 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 74 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 75 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 76 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 77 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 78 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 79 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 80 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 81 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 82 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 83 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 84 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 85 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 86 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 87 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 88 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 89 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 90 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 91 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 92 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 93 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 94 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 95 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 96 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 97 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 98 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 99 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 100 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 101 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 102 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 103 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 104 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 105 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 106 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 107 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 108 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 109 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 110 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 111 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 112 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 113 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 114 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 115 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 116 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 117 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 118 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 119 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 120 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 121 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 122 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 123 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 124 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 125 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 126 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 127 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 128 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 129 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 130 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 131 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 132 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 133 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 134 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 135 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 136 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 137 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 138 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 139 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 140 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 141 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 142 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 143 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 144 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 145 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 146 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 147 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 148 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 149 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 150 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 151 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 152 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 153 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 154 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 155 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 156 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 157 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 158 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 159 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 160 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 161 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 162 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 163 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 164 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 165 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 166 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 167 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 168 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 169 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 170 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 171 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 172 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 173 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 174 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 175 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 176 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 177 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 178 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 179 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 180 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 181 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 182 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 183 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 184 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 185 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 186 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 187 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 188 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 189 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 190 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 191 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 192 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 193 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 194 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 195 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 196 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 197 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 198 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 199 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 200 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 201 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 202 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 203 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 204 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 205 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 206 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 207 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 208 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 209 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 210 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 211 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 212 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 213 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 214 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 215 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 216 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 217 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 218 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 219 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 220 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 221 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 222 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 223 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 224 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 225 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 226 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 227 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 228 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 229 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 230 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 231 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 232 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 233 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 234 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 235 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 236 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 237 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 238 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 239 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 240 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 241 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 242 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 243 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 244 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 245 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 246 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 247 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 248 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 249 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 250 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 251 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 252 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 253 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 254 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 255 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 256 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 257 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 258 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 259 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 260 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 261 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
