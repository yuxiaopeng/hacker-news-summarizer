# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-10-30.md)

*最后自动更新时间: 2025-10-30 17:50:37*
## 1. Affinity Studio 现已免费

**原文标题**: Affinity Studio now free

**原文链接**: [https://www.affinity.studio/get-affinity](https://www.affinity.studio/get-affinity)

无法访问文章链接。

---

## 2. 发布HN：Propolis (YC X25) – 自动测试你的网络应用的浏览器代理

**原文标题**: Launch HN: Propolis (YC X25) – Browser agents that QA your web app autonomously

**原文链接**: [https://app.propolis.tech/#/launch](https://app.propolis.tech/#/launch)

蜂胶 (YC X25 毕业生) 正在推出一款浏览器代理，旨在自主地对 Web 应用程序进行质量保证 (QA)。该工具旨在自动化质量保证流程，减少测试中涉及的人工工作量，并提高 Web 应用程序的可靠性。 虽然提供的标题和介绍性文本并未明确详细说明具体功能，但暗示蜂胶利用浏览器代理来导航和与 Web 应用程序交互，可能执行预定义的测试用例或探索应用程序的功能，以识别错误和潜在问题。 本质上，蜂胶致力于为 Web 应用程序 QA 提供自动化解决方案，从而节省开发人员的时间和资源，同时确保更高质量的软件。

---

## 3. 987654321 / 123456789

**原文标题**: 987654321 / 123456789

**原文链接**: [https://www.johndcook.com/blog/2025/10/26/987654321/](https://www.johndcook.com/blog/2025/10/26/987654321/)

本文探讨了在任意进制*b*下形成的两个数之间的关系：`num(b)`是将数字按降序连接而成，而`denom(b)`是将数字按升序连接而成。作者注意到最初的观察结果，即987654321 / 123456789非常接近于8。

主要发现是，对于任何大于2的进制*b*，比率`num(b) / denom(b)`非常接近于整数*b* - 2。具体而言，该比率等于 (b-2) + (b-1)/denom(b)。作者通过Python代码进行了演示，验证了从3到1000的进制的这一结论。作者解释说，在像16进制这样的进制中，小数部分非常小，可能会因浮点精度限制而丢失，从而导致整数结果。

作者认为，虽然证明很简单，但很繁琐，因此选择包含Python脚本而不是正式的证明。更重要的是，他们认为计算演示可以作为数学证明的有价值的补充，提供另一种形式的验证，并可能揭示在传统证明中可能被忽视的细节。作者总结说，程序和证明虽然都容易出错，但不太可能共享相同的错误。

---

## 4. ZOZO的物理模拟接触求解器

**原文标题**: ZOZO's Contact Solver for physics-based simulations

**原文链接**: [https://github.com/st-tech/ppf-contact-solver](https://github.com/st-tech/ppf-contact-solver)

ZOZO接触求解器是一款强大且可扩展的工具，用于基于物理的壳、固体和杆的仿真，强调精度和性能。其亮点包括无穿透接触求解、可扩展至超过1.5亿个接触、基于GPU的单精度处理以提高缓存效率、严格的应变限制、有限元方法驱动的精度和大规模并行性。

该求解器已Docker密封，可直接使用，包含用于交互式示例的JupyterLab界面，并提供文档完善的Python API。它已为云准备就绪，可轻松部署在AWS、vast.ai和RunPod等主要平台上，并且在使用后不留痕迹。

主要功能包括动态网格创建、最少的网格数据准备、用于直观API的方法链以及用于所有前端功能的单一导入。文档全面，API详细信息、参数和日志记录功能可通过GitHub Pages访问，并提供交互式linting辅助。示例仿真涵盖各种场景（编织、堆叠等），并提供AWS使用预算估算。GitHub Actions运行压力测试以确保可靠性，并进行显式相交检查。大型示例正在开发中。

---

## 5. 展示一下：我做了一个用于代码审查的热图差异查看器

**原文标题**: Show HN: I made a heatmap diff viewer for code reviews

**原文链接**: [https://0github.com](https://0github.com)

此“Show HN”帖子介绍了一个代码审查热图差异查看器，旨在突出显示需要特别关注的代码更改。该查看器使用热图以可视化方式呈现代码差异中的复杂性和潜在问题，超越了基本的错误检测，从而识别出需要“再看一眼”的区域。

其核心思想不仅是标记潜在错误，还要标记代码的复杂性、不寻常的模式或潜在的安全漏洞。该系统的实现方法是在任何GitHub拉取请求URL中将“github.com”替换为“0github.com”。

在底层，该工具会克隆存储库，使用GPT-5 Codex分析每个差异，并生成一个JSON数据结构，然后将其转换为彩色热图。作者提供了示例拉取请求供测试。该热图查看器是开源的，可在GitHub上找到。本质上，该工具旨在通过引导审查者关注最关键和可能存在问题的代码更改来提高代码审查效率。

---

## 6. 耳朵不做傅里叶变换

**原文标题**: The ear does not do a Fourier transform

**原文链接**: [https://www.dissonances.blog/p/the-ear-does-not-do-a-fourier-transform](https://www.dissonances.blog/p/the-ear-does-not-do-a-fourier-transform)

本文解释了耳蜗（内耳中负责听觉的部分）如何处理声音。它阐明耳蜗**不执行傅里叶变换**——一种常见的信号分析方法，该方法优先考虑精确的频率分解，但牺牲了时间精度。

相反，耳蜗利用基底膜分离频率，不同的位置与不同的频率共振，形成一种音位分布。基底膜上的毛细胞将这些振动转化为电信号。此过程创建的滤波器介于小波和Gabor函数之间。这意味着耳蜗在频率和时间分辨率之间进行权衡，为高频提供高时间分辨率，为低频提供高频率分辨率。

本文认为，这种特殊的滤波方案是表示自然声音的一种有效方式，可以减少冗余。研究表明，特定的时频权衡取决于声音的类型（环境声音、动物发声或人类语音）。人类语音似乎占据了独特的时频空间。本文强调了与生态相关的表征的重要性，表明听觉等感觉系统经过优化，以对环境中与行为相关的信息进行处理。文章最后暗示了高效编码和神经元计算的生物物理学，这些内容将在下次讲座中介绍。

---

## 7. 美国拒绝加入70多国签署的联合国网络犯罪条约

**原文标题**: US declines to join more than 70 countries in signing UN cybercrime treaty

**原文链接**: [https://therecord.media/us-declines-signing-cybercrime-treaty?](https://therecord.media/us-declines-signing-cybercrime-treaty?)

包括英国、欧盟、中国和俄罗斯在内的70多个国家在河内签署了联合国打击网络犯罪公约，旨在建立打击数字犯罪的全球框架。该条约侧重于国际合作、能力建设和追踪网络罪犯，解决诸如非法资金流动、勒索软件攻击以及利用互联网进行恐怖主义、人口贩运和洗钱等问题。联合国估计网络犯罪每年造成10.5万亿美元的损失，并认为该条约将帮助各国政府，特别是全球南方国家，打击网络犯罪。

值得注意的是，美国没有签署该条约，称其“仍在审查”该条约。

该公约引入了首个电子证据收集和共享的全球框架，并将依赖互联网的犯罪行为定为犯罪，包括未经同意的图像共享。它还建立了一个24/7全天候国际合作网络。

然而，该条约面临着来自科技行业和人权组织的批评。担忧包括可能将网络安全研究定为犯罪、数据请求过于宽泛，以及威权政权可能滥用该条约进行监视和压制，从而可能影响数字自由并助长“网络威权主义”。尽管存在这些担忧，联合国秘书长古特雷斯强调有必要保护线上和线下基本人权，并强调该条约在克服跨境数字证据共享障碍方面的潜力。

---

## 8. 面板价格下跌推动全球太阳能繁荣，美国除外

**原文标题**: Falling panel prices lead to global solar boom, except for the US

**原文链接**: [https://arstechnica.com/science/2025/10/theres-a-global-boom-in-solar-except-in-the-united-states/](https://arstechnica.com/science/2025/10/theres-a-global-boom-in-solar-except-in-the-united-states/)

尽管太阳能电池板价格下跌推动了全球可再生能源的繁荣，但美国却落后了，这主要是由于特朗普总统领导下的政策转变。中国在太阳能生产和安装方面处于领先地位，大幅降低了可再生能源硬件的成本，使太阳能发电在全球范围内越来越有吸引力，即使在石油大国也是如此。

在全球范围内，可再生能源正在迅速扩张，印度、沙特阿拉伯和南非等国家也在拥抱太阳能。随着个人和企业寻求可靠的电力来源，小型太阳能装置也在增加。然而，挑战依然存在，包括需要改进的储能、电网基础设施以及消费者和产业从化石燃料的转型。虽然可再生能源发电取得了成功，但将其他行业过渡到电力则更为复杂。

尽管中国在可再生能源方面取得了令人瞩目的增长，但煤炭仍然发挥着重要作用，市场改革可能会影响未来的增长。在美国，激励措施的取消和项目的阻止正在阻碍可再生能源的发展。这种放缓可能会导致美国无法实现全球气候目标并失去在清洁能源领域的影响力，从而可能导致更高的电价和对化石燃料的依赖。

---

## 9. Qt Creator 18 发布

**原文标题**: Qt Creator 18 Released

**原文链接**: [https://www.qt.io/blog/qt-creator-18-released](https://www.qt.io/blog/qt-creator-18-released)

Qt Creator 18 has been released, featuring experimental development container support for automating project environment setup using "devcontainer.json" files and Docker containers. The update includes a redesigned Welcome mode with an Overview tab offering personalized tutorials and Qt blog highlights. Notifications have been integrated into progress popups, with an option to revert to banner style. Tabbed editors are now an option, alongside improved code navigation tools.

C++ support is enhanced with Clangd/LLVM updated to version 21.1, plus fixes for new C++ features and quick fixes for brace removal and static data member definition. QML Language Server settings allow usage of the latest server versions regardless of the project's Qt version. GitHub Enterprise environments are now supported for GitHub Copilot.

Project settings files (".user") are moved to a ".qtcreator/" subdirectory, with compatibility for older files. Project mode allows filtering kits and separates Run settings into Deploy Settings and Run Settings. Run configurations can now be synced across kits. CMake projects gain Test Preset support and a "ct" Locator filter for CTest.

Device configuration is improved with auto-detection of tools on remote Linux devices. Auto-reconnect to devices at startup is a new setting. Rsync deployment is fixed for remote builds and targets. The update also includes Git improvements, like staging and unstaging files directly within the commit editor. Qt Creator 18 is available through the Qt Online Installer, Qt Account Portal, and open-source download page.


---

## 10. 自由软件吓坏普通人

**原文标题**: Free software scares normal people

**原文链接**: [https://danieldelaney.net/normal/](https://danieldelaney.net/normal/)

名为《自由软件吓坏普通人》的短文可能认为，自由软件尽管具有潜在优势，但由于其复杂性或与专有软件的差异，面临着普及挑战。作者可能认为，“自由软件”一词或与其相关的概念（如开源、许可证、命令行、自定义）会让普通电脑用户望而却步。

核心观点可能是，自由软件*被认为*难用、缺乏支持或需要技术专长，阻碍了其广泛应用。“普通人”可能指的是习惯于具有简单界面和随时可用的商业支持的专有软件解决方案的普通用户。

作者可能建议，需要更好的营销、简化的用户界面、改进的支持资源或自由软件的品牌重塑，以克服这种“恐惧”，使其更容易被大众接受。 这篇文章可能强调了心理障碍，并着重说明了为什么自由软件尽管具有技术优点，却未能吸引普通用户。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 2 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 3 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 4 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 5 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 6 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 7 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 8 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 9 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 10 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 11 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 12 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 13 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 14 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 15 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 16 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 17 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 18 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 19 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 20 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 21 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 22 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 23 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 24 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 25 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 26 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 27 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 28 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 29 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 30 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 31 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 32 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 33 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 34 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 35 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 36 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 37 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 38 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 39 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 40 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 41 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 42 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 43 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 44 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 45 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 46 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 47 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 48 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 49 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 50 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 51 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 52 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 53 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 54 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 55 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 56 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 57 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 58 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 59 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 60 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 61 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 62 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 63 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 64 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 65 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 66 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 67 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 68 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 69 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 70 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 71 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 72 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 73 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 74 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 75 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 76 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 77 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 78 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 79 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 80 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 81 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 82 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 83 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 84 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 85 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 86 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 87 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 88 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 89 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 90 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 91 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 92 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 93 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 94 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 95 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 96 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 97 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 98 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 99 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 100 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 101 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 102 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 103 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 104 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 105 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 106 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 107 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 108 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 109 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 110 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 111 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 112 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 113 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 114 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 115 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 116 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 117 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 118 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 119 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 120 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 121 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 122 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 123 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 124 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 125 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 126 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 127 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 128 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 129 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 130 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 131 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 132 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 133 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 134 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 135 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 136 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 137 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 138 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 139 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 140 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 141 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 142 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 143 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 144 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 145 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 146 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 147 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 148 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 149 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 150 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 151 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 152 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 153 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 154 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 155 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 156 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 157 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 158 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 159 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 160 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 161 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 162 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 163 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 164 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 165 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 166 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 167 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 168 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 169 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 170 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 171 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 172 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 173 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 174 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 175 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 176 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 177 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 178 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 179 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 180 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 181 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 182 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 183 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 184 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 185 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 186 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 187 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 188 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 189 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 190 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 191 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 192 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 193 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 194 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 195 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 196 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 197 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 198 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 199 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 200 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 201 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 202 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 203 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 204 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 205 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 206 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 207 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 208 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 209 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 210 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 211 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 212 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 213 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 214 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 215 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 216 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 217 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 218 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 219 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 220 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 221 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 222 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 223 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 224 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
