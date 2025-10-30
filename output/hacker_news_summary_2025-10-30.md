# Hacker News 热门文章摘要 (2025-10-30)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Show HN: 用单个HTML文件编写的应用，鼓励我的孩子投资

**原文标题**: Show HN: In a single HTML file, an app to encourage my children to invest

**原文链接**: [https://roberdam.com/en/dinversiones.html](https://roberdam.com/en/dinversiones.html)

该“Show HN”帖子介绍了一款名为 D-investments 的简单 HTML 应用，作者创建它是为了教孩子们关于投资的知识。作者想要阐释复利的力量以及金钱随时间增长的概念。他构建了一个 PWA（渐进式 Web 应用），可以安装在旧智能手机上并贴在冰箱上作为仪表板。

该应用接受诸如孩子姓名、初始投资金额、利率和开始日期等输入。然后，它计算并显示每日、每周和每月的收益，以及更新后的总余额。作者充当他们的“投资代理人”，分配实际的利率以保持他们的参与度。

目标是提供投资如何随时间增长的视觉表现，帮助他们理解复利的魔力。作者认为，这不仅仅是接受礼物，而是一个宝贵的人生课程。该应用是一个单独的 HTML 文件，可以安装在任何支持 PWA 的智能手机上。

---

## 12. 多用户、无服务器数据访问的冷冻鸭湖

**原文标题**: Frozen DuckLakes for Multi-User, Serverless Data Access

**原文链接**: [https://ducklake.select/2025/10/24/frozen-ducklake/](https://ducklake.select/2025/10/24/frozen-ducklake/)

本文介绍了“Frozen DuckLakes”，这是一种使用 DuckDB 创建只读、基于云的数据湖的方法，无需专用的目录数据库服务器。“Frozen DuckLakes”利用云存储（如 AWS S3 或 HTTP）存储 Parquet 数据文件，为多用户数据访问提供了一种无服务器且经济高效的解决方案。

主要优势包括除存储之外的最低开销成本、适用于面向公众的数据、即时 SQL 可访问性以及跨多个云环境的能力。虽然数据是“冻结”在某个时间点的，但数据更新是通过创建新的 Frozen DuckLake 版本来实现的。可以通过版本控制或时间旅行功能访问旧版本。

该过程包括四个步骤：收集 Parquet 数据文件列表，生成 SQL 创建脚本（用于表创建和通过 `ducklake_add_data_files()` 填充数据），创建本地 DuckLake，以及将生成的 DuckDB 文件发布到云存储。`ducklake_add_data_files()` 函数通过仅读取 Parquet 元数据来高效地摄取数据。本文强调，附加期间指定的 `DATA_PATH` 不会被复制或使用。本文还提供了一个使用托管在 GitHub 上的太空任务数据集的实时演示。更新涉及重新生成 DuckLake 或增量添加新文件。讨论了版本控制注意事项，以便在 DuckDB 检测到新的 DuckLake 版本时处理模式升级。

---

## 13. 从第一性原理重新思考Postgres存储并替换EBS

**原文标题**: Replacing EBS and Rethinking Postgres Storage from First Principles

**原文链接**: [https://www.tigerdata.com/blog/fluid-storage-forkable-ephemeral-durable-infrastructure-age-of-agents](https://www.tigerdata.com/blog/fluid-storage-forkable-ephemeral-durable-infrastructure-age-of-agents)

本文介绍了Fluid Storage，一种为代理时代和现代数据工作负载设计的新型分布式块存储架构。文章指出，当前像Amazon EBS这样的“弹性”存储解决方案并非真正弹性，导致成本、扩展和恢复效率低下。

Fluid Storage旨在通过提供以下功能来解决这些问题：

*   **真正的弹性：** 基于实际使用情况无缝地向上和向下扩展卷，消除过度配置和资源浪费。
*   **Fork优先方法：** 即时、零拷贝的Fork和快照，实现快速创建测试和开发环境。
*   **基于使用量的定价：** 客户仅为他们消耗的存储付费。
*   **高性能：** 持续的高IOPS和吞吐量。
*   **强大的持久性：** 通过同步复制实现可靠的数据保护。
*   **兼容性：** 在块层运行，使其与Postgres和其他数据库/文件系统兼容。

Tiger Data的作者构建Fluid Storage是因为他们在Tiger Cloud中管理数千个Postgres实例的经验揭示了EBS在成本、向上/向下扩展性能、弹性和恢复方面的局限性。他们放弃了本地NVMe（由于持久性问题）和类似Aurora的页面服务器架构（由于PostgreSQL fork和复杂性）。相反，他们构建了一个分布式块存储，在存储层解决了这些挑战，为现代数据管理和代理工作流程提供了流畅、可扩展和高效的解决方案。

---

## 14. Ventoy：创建可启动USB驱动器，支持ISO/WIM/IMG/VHD(x)/EFI文件

**原文标题**: Ventoy: Create bootable USB drive for ISO/WIM/IMG/VHD(x)/EFI Files

**原文链接**: [https://github.com/ventoy/Ventoy](https://github.com/ventoy/Ventoy)

Ventoy 是一款开源工具，用于从 ISO/WIM/IMG/VHD(x)/EFI 文件创建可启动 USB 驱动器。它无需重复格式化 USB 驱动器；用户只需将镜像文件复制到驱动器，Ventoy 就会提供一个启动菜单供选择。Ventoy 支持多个镜像文件、浏览本地驱动器以查找可启动文件，以及 MBR 和 GPT 分区样式。它兼容 x86 Legacy BIOS、IA32 UEFI、x86_64 UEFI、ARM64 UEFI 和 MIPS64EL UEFI。

Ventoy 支持广泛的操作系统，包括 Windows、各种 Linux 发行版、类 Unix 系统和 ChromeOS。超过 1200 个 ISO 文件已通过兼容性测试。主要功能包括速度快、易于使用、支持大型 ISO 文件（超过 4GB），以及无需提取即可直接从 ISO/WIM/IMG/VHD(x)/EFI 文件启动。

Ventoy 通过其插件框架提供高级功能，包括持久化、自动安装、主题定制、密码保护以及将文件注入运行时环境的功能。它支持各种文件系统，如 FAT32、exFAT、NTFS、UDF、XFS 和 Ext2/3/4。用户可以访问详细的文档、FAQ 和论坛，开发者接受通过各种平台进行的捐赠。

---

## 15. 缩略语 (我们能把每个词都定义成缩略语吗?)

**原文标题**: Acronymy (Can we define every word as an acronym?)

**原文链接**: [https://acronymy.net/](https://acronymy.net/)

文章“缩略语化”探索了将每个单词定义为首字母缩略词的概念。它提出了一个游戏或项目，用户尝试为单词创建首字母缩略词扩展。该页面显示，数据集中的6.6203%的单词（270231个单词中的17890个）已被定义为首字母缩略词。今日推荐词是“tingling”（刺痛），幽默地定义为“tiny impulses nervously generating little itching neural glow”（微小的冲动紧张地产生轻微的瘙痒神经光芒）。

文章还重点介绍了近期活动，展示了新定义的单词（squirts, tureen, enter, mine, manducate, integrity, nihilistically, oppressive, branches, gay）或列为随机未定义单词的列表。存在指向Twitter帐户（@acronymy.net和@daily.acronymy.net）的链接，表明存在社交媒体组成部分。还提到了排行榜，表明该项目具有竞争性。“关于”部分可能提供了有关项目目标和方法的更多详细信息。本质上，“缩略语化”似乎是一个创造性的文字游戏实验，通过将单词重新想象为首字母缩略词来挑战单词的传统含义。

---

## 16. NaN，非NaN的非数字数字

**原文标题**: NaN, the not-a-number number that isn't NaN

**原文链接**: [https://piccalil.li/blog/nan-the-not-a-number-number-that-isnt-nan/](https://piccalil.li/blog/nan-the-not-a-number-number-that-isnt-nan/)

生成摘要时出错

---

## 17. 以色列要求谷歌和亚马逊使用秘密“暗号”来规避法律命令

**原文标题**: Israel demanded Google and Amazon use secret 'wink' to sidestep legal orders

**原文链接**: [https://www.theguardian.com/us-news/2025/oct/29/google-amazon-israel-contract-secret-code](https://www.theguardian.com/us-news/2025/oct/29/google-amazon-israel-contract-secret-code)

生成摘要时出错

---

## 18. 建立洋葱镜像超级简单

**原文标题**: Spinning Up an Onion Mirror Is Stupid Easy

**原文链接**: [https://flower.codes/2025/10/23/onion-mirror.html](https://flower.codes/2025/10/23/onion-mirror.html)

本文提供了一个逐步指南，介绍了如何使用Caddy作为Web服务器在基于Debian的VPS上创建现有网站的.onion镜像。作者强调了该过程的简单性，指出它仅涉及几个命令和配置行。

步骤包括：

1. **安装Tor:** 使用`apt`安装Tor软件包。
2. **配置Tor:** 编辑`/etc/tor/torrc`文件以禁用SOCKS代理，将Tor作为守护程序运行，设置隐藏服务目录和端口（80），禁用入站连接，并禁用目录服务。
3. **重启Tor:** 使用`systemctl`重启Tor服务。
4. **获取.onion地址:** 从`/var/lib/tor/hidden_service/hostname`文件中检索.onion地址。
5. **配置Caddy:** 可选地向Caddy配置文件添加一个新的站点块，用于.onion地址，尤其是在Caddy配置为仅响应特定域名或IP的情况下。作者指出需要通过纯HTTP提供站点，因为HTTPS证书不适用于.onion地址。
6. **（可选）宣传.onion地址:** 将`Onion-Location`标头添加到主站点的Caddy配置中，以微妙地告知启用Tor的浏览器有关.onion镜像的信息。该标头将用户重定向到.onion站点上的等效页面。

作者最后鼓励读者使用启用Tor的浏览器测试他们的.onion镜像。作者还提到他们的动机是为了言论自由和反审查，并且这样做“因为为什么不呢”。

---

## 19. Minecraft Java版移除混淆

**原文标题**: Minecraft removing obfuscation in Java Edition

**原文链接**: [https://www.minecraft.net/en-us/article/removing-obfuscation-in-java-edition](https://www.minecraft.net/en-us/article/removing-obfuscation-in-java-edition)

《我的世界：Java版》移除代码混淆，简化Mod制作。代码混淆是隐藏部分代码的一种做法，在游戏行业中很常见，但它使Mod制作者难以理解和使用游戏代码。

此前，Mod制作者必须拼凑每个类和函数的作用，但在2019年，《我的世界》发布了“混淆映射”，以帮助将混淆的术语与其原始名称匹配。现在，他们将完全移除混淆，从“混乱坐骑”发布后的第一个快照开始。这意味着变量、字段、方法和类的原始技术名称将默认包含在内。

为了帮助Mod制作者为这一变化做好准备，在即将到来的快照中，无混淆的“实验性发布”版本将与混淆版本一同提供，让他们能够测试他们的工具和工作流程。第一个完全无混淆的版本将是完整版“混乱坐骑”发布后的快照。此举旨在加快Mod制作速度，简化调试过程，并使崩溃日志更易于阅读。《最终用户许可协议》和《使用指南》仍然有效，并且.jar文件中将包含一个链接到EULA的LICENSE文件。鼓励Mod制作者就此过渡提供反馈。

---

## 20. 语言模型是单射的，因此是可逆的。

**原文标题**: Language models are injective and hence invertible

**原文链接**: [https://arxiv.org/abs/2510.15511](https://arxiv.org/abs/2510.15511)

该 arXiv 论文由 Nikolaou 等人于 2025 年 10 月提交，题为“语言模型是单射的，因此是可逆的”，挑战了 Transformer 语言模型由于非线性和归一化而为非单射的普遍假设。作者通过数学证明，这些模型在将离散输入序列映射到连续表示时，实际上是单射的（无损的），这一性质从初始化到训练都得以保持。

他们通过在六个最先进的语言模型上进行的数十亿次冲突测试，对他们的主张进行了经验验证，没有发现任何冲突实例（不同的输入映射到相同的输出）。基于这种单射性，他们引入了 SipIt，一种新颖的算法，可以证明地且高效地在线性时间内从隐藏激活中重建精确的输入文本，从而展示了实际的可逆性。

该论文认为，这种单射性是语言模型的一个基本且可利用的属性，对提高透明度、可解释性和确保这些模型更安全的部署具有重要意义。这项工作贡献了语言模型逆向的理论证明和实用算法，为理解和控制这些强大的系统开辟了新的研究方向。

---

## 21. Typst的数学模式问题

**原文标题**: Typst's Math Mode Problem

**原文链接**: [https://laurmaedje.github.io/posts/math-mode-problem/](https://laurmaedje.github.io/posts/math-mode-problem/)

本文讨论了 Typst 数学模式中关于上下标解析的一个长期存在的问题，特别是涉及函数调用时。核心问题是 Typst 将后跟括号的标识符视为函数调用，导致 Typst 函数（如 `abs(x)`）和数学函数（如 `omega(x)`）之间存在歧义。这影响了上下标的优先级，导致出现不直观的行为，例如 `f_i(x)` 被渲染为 `i(x)` 而不是 `f_i`。

作者解释说，最初的目的是让 Typst 函数调用比上下标结合得更紧密，以使 `abs(x)` 调用能够正常工作，但这导致了意外的优先级问题。恢复到之前的行为 (Typst 0.3) 可以解决下标问题，但会破坏现有的 `abs(x)` 调用。

本文探讨了几种潜在的解决方案：不做任何处理 (A)、恢复到 Typst 0.3 的行为 (B)、运行时解析 (C)、引入 `MathAttachCall` 表达式 (D) 以及要求 Typst 函数调用使用不同的语法 (E)。选项 C 和 D 旨在两全其美，但增加了复杂性并降低了可移植性。选项 E，为 Typst 函数引入哈希标记（`#abs(x)`），可以明确区分，但与 LaTeX 相比，改变了 Typst 的核心特征。

作者最终支持选项 B（恢复到 Typst 0.3 的行为），承认在 `e^(abs(x))` 之类的示例中需要括号，但强调了它提供的更大的清晰度和可预测性。他们认为，对于一个更直观和一致的数学模式来说，需要括号是一个合理的折衷方案。一个实施选项 B 的 PR 目前已开放，并可能被合并。

---

## 22. 关于 Ruby 循环的一些闲谈

**原文标题**: Some Smalltalk about Ruby Loops

**原文链接**: [https://tech.stonecharioteer.com/posts/2025/ruby-loops/](https://tech.stonecharioteer.com/posts/2025/ruby-loops/)

本文从消息传递的角度探讨了 Ruby 的循环，并与 Smalltalk 的“协议胜于语法”哲学进行了类比。作者将 Ruby 的方法与 Python 的方法进行了对比，认为 Ruby 将方法调用视为向对象发送消息，允许对象控制迭代并定义它们如何响应这些消息。相比之下，Python 侧重于属性查找，然后使用 call 调用方法。

作者使用 `.send` 方法解释了 Ruby 中消息传递的概念，并探讨了它如何为 `.times` 等方法定义自定义行为。这可以通过 `PseudoInteger` 和 `LyingPseudoInteger` 等类实现自定义，展示了对象（而非循环语法）如何定义迭代逻辑。本文解释了一种语言如何通过 `.respond_to?` 和 `.method_missing` 拥有内置的消息处理结构。

Enumerable 模块的包含和 `each` 方法的实现被作为 Smalltalk 中 Collection 协议的示例。本文批评了 Ruby 中的 `for` 循环，认为它是污染命名空间并且不符合 Ruby 消息传递范例的语法糖。相反，作者强调使用 `.each` 和 `.times` 等方法来创建符合 Ruby 习惯用法的代码的重要性。最终，作者认为理解消息传递有助于开发者超越语法，设计更好的面向对象的接口。

---

## 23. 古代人如何看待自己

**原文标题**: How ancient people saw themselves

**原文链接**: [https://worldhistory.substack.com/p/how-ancient-people-saw-themselves](https://worldhistory.substack.com/p/how-ancient-people-saw-themselves)

Unable to access the article link.


---

## 24. 唯美主义者的历程

**原文标题**: The Aesthete's Progress

**原文链接**: [https://sydneyreviewofbooks.com/essays/the-aesthetes-progress](https://sydneyreviewofbooks.com/essays/the-aesthetes-progress)

本文概述了一种关于审美观照及其转化力量的哲学观点，主要关注观察者与被观察者之间的关系。它认为，当我们感知到某种事物是美的，我们就超越了个人的自我，成为一个“纯粹无意志的认知主体”。这种客观性使我们能够感知到该对象潜在的“理念”，而不是它的具体、个别实例。

“理念”超越了时间和空间。观察的是哪棵具体的树或者观察者是谁并不重要；重点转移到树存在的基本的、普遍的意义上。这种普遍的意义是“理念”的核心。

至关重要的是，审美观照可以缓解痛苦。通过摆脱我们个人意志和欲望的束缚，我们摆脱了痛苦的根源。摆脱意志影响的“纯粹认知主体”变成了“世界的永恒之眼”，不受个体存在短暂性的影响。

文章最后断言，每个人都存在着双重存在。作为一个受意志驱动的存在，个人会经历痛苦，并受到时间和地点的限制。然而，作为一个“纯粹客观的感知者”，个人参与到客观世界中，而没有痛苦的负担，与所有被感知的事物融为一体。在这种状态下，个人不仅限于他们单一的、痛苦的存在，而是包含了整个被感知的宇宙。

---

## 25. 树莓派Pico位碰撞实现百兆以太网

**原文标题**: Raspberry Pi Pico Bit-Bangs 100 Mbit/S Ethernet

**原文链接**: [https://www.elektormagazine.com/news/rp2350-bit-bangs-100-mbit-ethernet](https://www.elektormagazine.com/news/rp2350-bit-bangs-100-mbit-ethernet)

本文探讨了开发者 Steve Markgraf 的项目“Pico-100BASE-TX”，他在 Raspberry Pi Pico 上纯粹使用软件和 RP2040（以及 RP2350）的可编程 I/O (PIO) 实现了 100 Mbit/s 快速以太网传输。 在 10BASE-T 和 USB 等先前的位碰撞成就的基础上，Markgraf 的实现利用 PIO 和 DMA 以 125 MHz 的符号率进行 MLT-3 编码、4B5B 线路编码和加扰。 这产生了一个功能性的 100 Mbit/s 以太网链路，能够通过 UDP 传输大约 11 Mbyte/s 的数据流，并已通过实时音频和 ADC 数据流进行了演示。

该项目是一个仅发送的验证概念，作者建议使用脉冲变压器或以太网交换机进行隔离。 随附的存储库包含计数器、ADC 流媒体和音频演示等示例。 该库支持 RP2040 和 RP2350 (Pico 2)，并且与标准 Pico SDK 兼容。

本文强调了这项成就对于低成本、高速数据采集和流媒体的潜力，设想了在测试仪器、远程传感器和实验性网络接口中的应用，所有这些都不需要专用 PHY 芯片。 它提出了一个问题：在廉价微控制器上，软件定义的硬件能被推到多远。

---

## 26. 拯救世界的Moderna公司已分崩离析

**原文标题**: Moderna, the company that helped save the world, has unraveled

**原文链接**: [https://www.statnews.com/2025/10/30/moderna-rise-fall-biotech-analysis-from-pandemic-rise-to-mrna-crash/](https://www.statnews.com/2025/10/30/moderna-rise-fall-biotech-analysis-from-pandemic-rise-to-mrna-crash/)

题为“莫德纳，这家曾帮助拯救世界的公司，如今已分崩离析”的文章暗示这家生物技术公司面临重大衰落。标题本身暗示莫德纳的命运发生了戏剧性逆转，这家公司因其在开发新冠疫苗方面的作用而获得全球认可。

这段文字并没有提供太多关于这种分崩离析的原因的细节，而是专注于一个不相关的新闻项目：“STAT Plus：Alnylam提高指导，心脏药物销售额符合预期。” 这两篇文章的并列暗示了莫德纳的困境与另一家制药公司Alnylam的成功之间的对比。

在没有更多背景信息的情况下，我们只能推断莫德纳目前的状态远非其之前的成功。 这种“分崩离析”的可能原因包括疫苗需求下降、新产品开发面临挑战、财务困难、内部管理不善、竞争加剧或对其运营或产品的负面报道。 这篇文章可能深入探讨了这些潜在因素的具体情况，解释了一家曾经因其对全球健康的重大贡献而受到赞扬的公司现在如何面临重大挫折。 文章的日期是2025年10月30日，表明自新冠疫苗最初成功以来已经过去了一段时间。

---

## 27. 汇编实现的iOS Hello-World应用

**原文标题**: Hello-World iOS App in Assembly

**原文链接**: [https://gist.github.com/nicolas17/966a03ce49f949dd17b0123415ef2e31](https://gist.github.com/nicolas17/966a03ce49f949dd17b0123415ef2e31)

本文展示了一个 "Hello-World" iOS 应用的汇编代码。该代码，名为 `yellow.asm`，演示了如何使用 ARM64 汇编语言从头开始构建一个基本的 iOS 应用，绕过 Objective-C 或 Swift。

汇编代码实现了以下功能：

*   **应用程序委托设置：** 创建并注册一个 `AppDelegate` 类，遵循 `UIApplicationDelegate` 协议。它动态地添加一个方法 (`application:didFinishLaunchingWithOptions:`) 来处理应用程序的启动。
*   **UI 创建：** 实例化 `UIWindow`、`UIViewController`，并将视图的背景颜色设置为黄色。它利用 Objective-C 运行时函数，如 `objc_getClass`、`class_createInstance` 和 `objc_msgSend` 来与 UIKit 组件交互。
*   **消息发送：** 广泛使用 `objc_msgSend` 向 Objective-C 对象发送消息，例如设置窗口上的根视图控制器，并使窗口成为关键窗口且可见。
*   **内存管理：** 使用自动释放池 (`objc_autoreleasePoolPush`, `objc_autoreleasePoolPop`) 进行基本的内存管理。
*   **核心功能：** `didFinishLaunching` 函数负责设置用户界面并使其可见。

本文还展示了如何在 `.data` 段中定义字符串，以便与 Objective-C API 一起使用。

注释突出了潜在的优化（同时弹出 x0 和 x1）以及关于 `_objc_autoreleasePoolPop` 之后 x7 寄存器保存的问题。还有人询问构建和部署说明。

---

## 28. Kafka速度快——我用Postgres

**原文标题**: Kafka is Fast – I'll use Postgres

**原文链接**: [https://topicpartition.io/blog/postgres-pubsub-queue-benchmarks](https://topicpartition.io/blog/postgres-pubsub-queue-benchmarks)

本文挑战了一种盲目采用Kafka等复杂技术的趋势，认为在某些情况下，更简单的解决方案，如Postgres，可能就足够了。“小数据”运动和Postgres的复兴，有力地证明了应该优先考虑常识和实用性，而不是受炒作驱动的技术选择。

作者对Postgres作为发布/订阅消息系统和队列的能力进行了基准测试，并将其与Kafka进行了比较。该基准测试使用Postgres原语和至少一次语义重建了一个日志。

**主要发现：**

*   **发布/订阅：** 单个Postgres实例实现了4.8 MB/s的写入吞吐量和24.6 MB/s的读取吞吐量，且延迟合理。一个复制的三节点设置保持了类似的吞吐量，同时将p99端到端延迟增加到186毫秒。文章得出结论，一个简单的三节点Postgres集群可以处理许多常见的Kafka工作负载，且成本较低，每年11,514美元。
*   **队列：** 基准测试的吞吐量较低，受到单表瓶颈的限制。

作者强调，虽然Kafka擅长处理极端规模，但许多组织并不需要这种复杂程度。Postgres提供了一个经过实战检验、可扩展且可靠的替代方案，可以用更少的开发工作量处理大部分专用系统的用例。文章提倡在自动选择Kafka等复杂解决方案之前，仔细考虑项目的具体需求，尤其是在工作负载相对较小的情况下。

---

## 29. 抖动 – 第一部分

**原文标题**: Dithering – Part 1

**原文链接**: [https://visualrambling.space/dithering-part-1/](https://visualrambling.space/dithering-part-1/)

抖动 – 第一部分：本文探讨了抖动这种引人入胜的效果，阐述了它如何创造出比实际使用的颜色变化更多的视觉错觉。抖动巧妙地通过策略性地排列有限颜色的像素（在本例中为黑色和白色）来模拟阴影，从而欺骗眼睛。

作者强调了抖动如何最大限度地利用有限的资源。文章使用灰度图像示例来说明这个概念。 抖动不是将每个像素映射到最接近的可用颜色（黑色或白色），从而导致生硬的过渡和细节的丢失，而是有选择地将一些像素推向相反的颜色，生成特殊的图案，通过不同的像素密度来模拟阴影。

文章介绍了一种使用阈值映射表的简单方法，即有序抖动。阈值映射表是一个表示亮度级别的数值网格。通过将每个像素的亮度与相应的阈值进行比较，像素会变成黑色或白色。 阈值映射表的设计是输出图案的关键，在这些图案中，黑白像素密度与输入图像的阴影相匹配。

作者最后指出，抖动用更少的颜色复制阴影，并策略性地放置这些颜色以保持原始外观。 本文为接下来的两个部分做了铺垫，承诺深入研究创建阈值映射表的算法，并探索另一种抖动算法——误差扩散。 作者还鼓励读者在 X/Twitter 上关注他们。

---

## 30. Uv是过去十年里Python生态系统发生的最好的事情。

**原文标题**: Uv is the best thing to happen to the Python ecosystem in a decade

**原文链接**: [https://emily.space/posts/251023-uv](https://emily.space/posts/251023-uv)

本文赞扬由 Astral 开发的全新开源 Python 工具 uv，认为其是对 Python 生态系统的革命性改进。作者认为 uv 简化了 Python 安装、虚拟环境管理和依赖同步，在速度和效率上超越了现有工具。

uv 的主要特点包括：

*   **快速安装：** 通过一行命令轻松安装，不干扰现有的 Python 安装。
*   **虚拟环境管理：** 使用 `pyproject.toml` 文件无缝集成虚拟环境，以管理依赖项和 Python 版本。
*   **简化工作流程：** 使用 `uv init` 简化项目设置，使用 `uv add` 管理依赖项，使用 `uv sync` 同步环境。`uv run` 命令简化了在正确环境中执行脚本的操作。
*   **版本锁定：** 该工具允许使用 `uv python pin` 锁定特定 Python 版本，确保跨机器环境的一致性。
*   **即时执行：** `uvx`（或 `uv tool run`）命令允许在临时虚拟环境中快速执行诸如 Ruff 或 Jupyter Lab 之类的工具，而无需复杂的设置。

作者强调了 uv 的速度、跨平台兼容性以及通过 `uv.lock` 文件创建可重现 Python 环境的能力。他们分享了使用 uv 管理分布式团队中 Python 安装的个人经验，突出了其对一致性和协作的积极影响。总而言之，本文将 uv 定位为 Python 开发的变革者，为各种任务提供效率和简化。

---

## 31. 互联网运行在自由开源软件之上，域名系统亦如此。

**原文标题**: The Internet runs on free and open source software and so does the DNS

**原文链接**: [https://www.icann.org/en/blogs/details/the-internet-runs-on-free-and-open-source-softwareand-so-does-the-dns-23-10-2025-en](https://www.icann.org/en/blogs/details/the-internet-runs-on-free-and-open-source-softwareand-so-does-the-dns-23-10-2025-en)

本文强调了自由开源软件 (FOSS) 在域名系统 (DNS)（互联网的基础）中的关键作用。ICANN 安全与稳定咨询委员会 (SSAC) 发布了 SAC132 报告，强调了理解和支持 DNS 中的 FOSS 的重要性，尤其是在新的网络安全法规出台的背景下。

该报告认为，由于 FOSS 如此深入地嵌入到 DNS 运营的各个方面，因此有关网络安全的政策决策将直接影响互联网的安全性和弹性。SAC132 旨在为决策者提供非技术性指导，确保法规能够加强而非削弱这一关键基础设施。

该报告清晰地概述了 DNS 和 FOSS 开发模式，分析了美国、英国和欧盟当前关于 DNS 中 FOSS 的网络安全法规，并为决策者提供了支持和保护 FOSS 的实用建议。

SSAC 敦促决策者、技术专家和利益相关者阅读完整报告并参与讨论，以确保由强大且可持续的 FOSS 生态系统支持的安全、稳定且具有弹性的互联网。他们邀请大家参加在都柏林举行的 ICANN84 大会或远程参与。本文承认了为 SAC132 报告做出贡献的 SSAC 成员和专家的贡献。

---

## 32. 3D太阳能塔提高容量系数50%，太阳能表面积增加两倍

**原文标题**: 3D solar tower increases capacity factor 50%, triples solar surface area

**原文链接**: [https://www.pv-magazine.com/2025/10/27/3d-solar-tower-increases-capacity-factor-50-triples-solar-surface-area/](https://www.pv-magazine.com/2025/10/27/3d-solar-tower-increases-capacity-factor-50-triples-solar-surface-area/)

Janta Power获550万美元种子轮融资，用于推进其垂直3D太阳能塔技术，该技术专为空间受限环境设计。这些塔目前正在达拉斯-沃斯堡和慕尼黑等机场进行试点项目，其容量系数比传统太阳能装置高50%，达到约32%，而标准为22%。

单轴跟踪塔的独特几何结构使太阳能表面积暴露量增加两倍，捕捉早晚阳光，形成与能源需求相一致的双峰功率曲线。Janta Power的目标是实现低至0.05美元/千瓦时的平准化度电成本（LCOE）。

该公司提供5千瓦的塔和1.5千瓦的屋顶型号，8.5千瓦和10千瓦的塔正在开发中。这些塔采用钢结构和模块化地基，旨在承受高风，最大限度地减少现场破坏。其3D设计确保全天更平稳的能源输送，减轻电网压力，并减少对调峰电厂的依赖。

---

## 33. GLP-1疗法：其在酒精和物质使用障碍中的新兴作用

**原文标题**: GLP-1 therapeutics: Their emerging role in alcohol and substance use disorders

**原文链接**: [https://academic.oup.com/jes/article/9/11/bvaf141/8277723?login=false](https://academic.oup.com/jes/article/9/11/bvaf141/8277723?login=false)

无法访问文章链接。

---

## 34. 板：新款游戏主机识别实体棋子，并提供开放SDK

**原文标题**: Board: New game console recognizes physical pieces, with an open SDK

**原文链接**: [https://board.fun/](https://board.fun/)

Board是一款新型游戏主机，旨在让人们聚集在一起进行面对面的游戏。它结合了桌游的触感和视频游戏的动态魔力，使用主机识别的实体棋子来控制其24英寸桌面屏幕上的游戏。

该主机拥有开放的SDK，允许未来的游戏开发和扩展其游戏库。 Board配备了12款独家游戏，涵盖街机、策略和动作等类型，专为不同年龄段（6岁以上和8岁以上）和技能水平而设计。这些游戏使用独特的实体棋子进行直观控制，无需传统控制器。 示例包括街机经典、烹饪合作游戏、引导Bloogs的益智游戏、名为Strata的战略方块放置游戏以及间谍冒险。其他游戏包括数字宠物、贪吃蛇游戏、寿司决斗和太空战斗。

Board专为所有人设计，从儿童到祖父母，并支持单人游戏、决斗和团体游戏。常见问题解答部分强调，Board是桌游和视频游戏的融合，强调其社交性、触感和可重玩性，所有这些都在一张实体桌子周围体验。其目标是提供一种独特的游戏体验，既方便又吸引广泛的受众。

---

## 35. AOL将以15亿美元出售给Bending Spoons

**原文标题**: AOL to be sold to Bending Spoons for $1.5B

**原文链接**: [https://www.axios.com/2025/10/29/aol-bending-spoons-deal](https://www.axios.com/2025/10/29/aol-bending-spoons-deal)

无法访问文章链接。

---

## 36. Tailscale 对等节点中继

**原文标题**: Tailscale Peer Relays

**原文链接**: [https://tailscale.com/blog/peer-relays-beta](https://tailscale.com/blog/peer-relays-beta)

Tailscale发布Tailscale对等中继，为客户提供一种可管理的替代方案，以取代Tailscale的DERP服务器来中继网络流量。对等中继可提供更高的吞吐量，媲美直连，并解决了某些环境（特别是防火墙严格或锁定式云基础设施背后的环境）中DERP中继的性能限制。

对等中继在单个UDP端口上运行，并直接集成到Tailscale客户端中，从而简化了部署。 它们优先考虑直接连接，回退到对等中继，然后再到DERP服务器，从而在保持WireGuard加密的同时确保连接性。

这项新功能使客户能够构建确定性的、高吞吐量的中继拓扑，从而在无法直接连接的情况下提高性能。用例包括绕过云NAT、通过网络防火墙中继流量、从DERP服务器卸载流量以及提供对锁定式客户网络的受控访问。

Tailscale对等中继目前处于公开测试阶段，可在所有计划中使用，包括免费层（限制为两个免费对等中继）。 虽然仍在进行改进，但早期合作伙伴已经体验到轻松的部署。 该功能使客户能够更好地控制其网络连接，从而使他们能够轻松灵活地扩展 Tailscale。

---

## 37. IRCd 服务 (2024)

**原文标题**: IRCd service (2024)

**原文链接**: [https://example.fi/blog/ircd.html](https://example.fi/blog/ircd.html)

本文宣布推出一个简单的IRCd服务，托管于example.fi。该服务用AWK（一种传统上不用于IRC服务器的脚本语言）构建，旨在作为一种教育工具，并致敬IRC在在线通信中的先驱作用。本文强调了IRC的历史意义，指出其创建于1988年及其对现代通信平台的影响。

该服务有意地进行了限制，缺少频道和用户列表、主题和操作员功能等特性。建议连接到example.fi的用户使用没有花哨功能的客户端，如带`-nocap`选项的Irssi或Windows上的Hexchat。

本文包含一个连接到IRCd的Telnet示例，展示了一个基本的欢迎消息和一个简陋的“每日消息”（MOTD）。最后，文章分享了一个有趣的事实，即整个服务器代码仅有大约60行AWK和几行bash代码，并且代码将在“准备就绪”时发布。

---

## 38. OpenAI承诺留在加州，为其首次公开募股扫清了道路。

**原文标题**: OpenAI’s promise to stay in California helped clear the path for its IPO

**原文链接**: [https://www.wsj.com/tech/ai/openais-promise-to-stay-in-california-helped-clear-the-path-for-its-ipo-3af1c31c](https://www.wsj.com/tech/ai/openais-promise-to-stay-in-california-helped-clear-the-path-for-its-ipo-3af1c31c)

无法访问文章链接。

---

## 39. 卡洛·罗韦利的激进现实观

**原文标题**: Carlo Rovelli’s radical perspective on reality

**原文链接**: [https://www.quantamagazine.org/carlo-rovellis-radical-perspective-on-reality-20251029/](https://www.quantamagazine.org/carlo-rovellis-radical-perspective-on-reality-20251029/)

本文介绍了理论物理学家卡洛·罗韦利，他以其在圈量子引力和量子力学“关系”诠释方面的工作而闻名。罗韦利的研究挑战了我们对空间和时间的传统理解，认为它们不是现实的基本方面，而是从量子元素的相互作用中涌现出来的。

他的观点深受其反主流文化的青年时代和对质疑既定规范的信念的影响。他强调哲学在物理学中的重要性，认为哲学见解有助于我们更好地理解和解释现有的科学知识，尤其是在应对诸如现实、信息、空间和时间等复杂概念时。

罗韦利提倡一种现实的视角观，即属性只能相对于另一个系统来定义。他认为不存在客观的、终极的真理，而是一个相互作用和有限视角的网络。他认为，接受这种局限性可以实现更诚实、更有效的科学进步。他认为时间的恒定流动并非根本，而是热力学第二定律的产物，一种从我们的角度来看才是“真实”的幻觉。

虽然圈量子引力面临挑战，但罗韦利仍然希望未来的实验，可能涉及宇宙微波背景辐射或微型黑洞的探测，将提供支持性证据。他认为，受那伽朱纳等哲学家影响的关系量子力学观点，提供了一个根据事物之间的关系，而不是作为具有内在属性的独立实体来理解世界的框架。

---

## 40. 有钱胜过有理

**原文标题**: It's better to be rich than right

**原文链接**: [https://www.cnn.com/2025/10/30/business/tesla-meme-stock-nightcap](https://www.cnn.com/2025/10/30/business/tesla-meme-stock-nightcap)

华尔街已从重视基本商业原则转向“氛围交易”心态，主要目标是不顾公司实际业绩或产品可行性，推高股价。

作者以特斯拉为例，强调该公司对机器人出租车和人形机器人等未来技术的依赖，尽管其核心电动汽车业务正面临日益激烈的竞争。特斯拉的大部分股票价值归功于这些未经证实的风险投资，但股价仍在飙升。

类似地，文章指出，尽管人们对其现实世界的效用持怀疑态度，但比特币的表现明显优于标准普尔500指数。那些质疑产品价值的加密货币怀疑论者错过了巨大的收益。

作者观察到，华尔街似乎对“坏”消息免疫，因为投资者已经习惯于“逢低买入”，认为价格必然会反弹。然而，文章警告说，这种策略不可能无限期地持续下去，因为投资者的资源和时间都是有限的。这篇文章认为，这种“氛围交易”方式最终可能导致市场回调，但此类事件发生的时间仍不确定。

---

## 41. Chipotle股票暴跌：失业青年吃不起了

**原文标题**: Chipotle stock craters: young people without jobs cannot afford their food

**原文链接**: [https://finance.yahoo.com/news/chipotle-stock-craters-as-company-says-young-people-without-jobs-cant-afford-their-food-anymore-155415667.html](https://finance.yahoo.com/news/chipotle-stock-craters-as-company-says-young-people-without-jobs-cant-afford-their-food-anymore-155415667.html)

Chipotle's stock plummeted after the company cut its full-year sales outlook for the third consecutive quarter, citing economic pressure on its core customer base, particularly young people aged 25-35. CEO Scott Boatwright attributed the decline to "persistent macroeconomic pressures," including unemployment, student loan repayments, and slower wage growth affecting this demographic. Unemployment for Americans ages 20-24 was 9.2% in August, up from 7.9% a year prior.

The company reported third-quarter revenue of $3 billion, slightly below the expected $3.02 billion. While digital sales comprised 36.7% of total food and beverage revenue, same-store sales grew by only 0.3%, less than the anticipated 1%. Higher menu prices and larger ticket sizes offset a decline in foot traffic.

Chipotle expects the first quarter to be the most challenging, anticipating continued pressure from middle- and low-income consumers. To combat this, the company plans to increase marketing spend, enhance digital experiences, and introduce more menu innovation, including new sides, dips, and limited-time protein offerings. The recent introduction of Adobo Ranch dip may not have provided the intended boost, as analysts suggest Chipotle needs to improve its value proposition, with add-ons like expensive sauces potentially hindering progress.


---

## 42. 自1990年以来，中国新增了相当于得克萨斯州面积的森林。

**原文标题**: China has added forest the size of Texas since 1990

**原文链接**: [https://e360.yale.edu/digest/china-new-forest-report](https://e360.yale.edu/digest/china-new-forest-report)

尽管全球森林砍伐趋势，尤其是在热带地区因农业、畜牧业、火灾和干旱加剧的情况下，一些国家正经历森林再生。一份联合国报告强调了中国显著的植树造林努力，自1990年以来增加了1.73亿英亩的森林，面积相当于得克萨斯州的大小。这一成就主要归功于积极的植树计划，包括旨在遏制沙漠扩张的项目，例如环绕塔克拉玛干沙漠长达2000英里的防护林带。

加拿大、印度和俄罗斯等其他国家也增加了森林覆盖率。发达国家由于农业效率更高，森林砍伐的速度正在放缓或逆转。虽然火灾和干旱仍然导致森林流失，但包括中国和印度在内的这些国家总体上正在增加树木。 这种积极趋势与巴西、印度尼西亚和刚果民主共和国持续的森林砍伐形成鲜明对比，突显了全球森林覆盖变化的复杂局面。文章强调了面对国际社会结束森林砍伐目标时，这些植树造林努力的重要性。

---

## 43. 眼部假体首次使因黄斑变性而丧失的视力得以恢复

**原文标题**: Eye prosthesis is the first to restore sight lost to macular degeneration

**原文链接**: [https://med.stanford.edu/news/all-news/2025/10/eye-prosthesis.html](https://med.stanford.edu/news/all-news/2025/10/eye-prosthesis.html)

生成摘要时出错

---

## 44. 使用 Next.js App Router 一年后的感想以及我们放弃的原因

**原文标题**: One year with Next.js App Router and why we're moving on

**原文链接**: [https://paperclover.net/blog/webdev/one-year-next-app-router](https://paperclover.net/blog/webdev/one-year-next-app-router)

生成摘要时出错

---

## 45. Upwave (YC S12) 正在招聘软件工程师

**原文标题**: Upwave (YC S12) is hiring software engineers

**原文链接**: [https://www.upwave.com/job/8228849002/](https://www.upwave.com/job/8228849002/)

Upwave招聘高级软件工程师

Upwave是一家由Y Combinator和其他投资者支持的品牌成果衡量平台，现招聘一名高级软件工程师加入其远程优先团队。此职位涉及构建API、数据管道和系统，以驱动其平台，该平台处理数十亿次广告曝光并为主要品牌提供洞察。

理想的候选人拥有5年以上经验，具备强大的全栈技能，并侧重于后端（首选Java/Kotlin/Groovy经验），熟悉MySQL和DynamoDB等数据系统，以及AWS（Kubernetes、Terraform）等云平台的使用经验。 具备React等现代前端框架经验者优先。 该职位还要求理解和接受现代人工智能驱动的开发工具。公司正在寻找重视协作、具有主人翁精神并热衷于构建可靠、可扩展系统的人才。

高级软件工程师将在整个技术栈中做出贡献，设计和构建可扩展的后端系统、工程数据管道并提高平台可靠性。 一个关键重点是集成LLM和高级因果推理，以通过人工智能驱动的工具改善用户体验。

Upwave提供现代技术栈、以工程为主导的环境以及影响重大广告决策的机会。薪酬方案包括15万美元至17.5万美元的基本工资+奖金+股权+福利。 他们优先考虑创新、工作与生活平衡以及协作包容的文化。

---

## 46. 美国国家科学基金会如何推动软件定义网络

**原文标题**: How the U.S. National Science Foundation enabled Software-Defined Networking

**原文链接**: [https://cacm.acm.org/federal-funding-of-academic-research/how-the-u-s-national-science-foundation-enabled-software-defined-networking/](https://cacm.acm.org/federal-funding-of-academic-research/how-the-u-s-national-science-foundation-enabled-software-defined-networking/)

本文详细介绍了美国国家科学基金会(NSF)如何在推动软件定义网络(SDN)的开发和应用方面发挥关键作用。网络所有者对路由器供应商主导的传统网络创新缓慢和控制有限感到沮丧，他们寻求对网络行为的更大控制权。SDN应运而生，它将控制平面与数据平面分离，并采用逻辑上集中的控制。

NSF大力投资于解决“互联网僵化”问题，资助了100x100、GENI、FIND和POMI等项目，这些项目培养了一个研究社区，开发了关键的SDN组件，如4D架构、Ethane、OpenFlow和NOX等开源控制器。GENI促进了真实世界的实验，而FIND支持利用SDN的新互联网架构。POMI将SDN研究扩展到移动网络和可编程转发平面。

与此同时，超大规模云公司（谷歌、微软、亚马逊、Facebook）为其庞大的数据中心寻求具有成本效益且可控的网络解决方案。SDN实现了多租户环境的网络虚拟化（以Nicira的NVP和Open vSwitch为首）和广域流量工程（谷歌的B4骨干网）。这种商业应用进一步刺激了学术研究和成功的SDN初创公司的诞生。

SDN的成功将控制权从网络供应商转移到软件程序员手中，从而实现了更大的灵活性、更快的创新和正式的网络验证。虽然最初专注于数据中心，但SDN原则现在在各种网络中普遍存在。本文强调了NSF在资助早期研究和促进与产业界合作方面的远见卓识，从而引发了网络架构的一场革命。

---

## 47. 谁还需要Graphviz，自己就能建一个？

**原文标题**: Who needs Graphviz when you can build it yourself?

**原文链接**: [https://spidermonkey.dev/blog/2025/10/28/iongraph-web.html](https://spidermonkey.dev/blog/2025/10/28/iongraph-web.html)

本文详细介绍了`iongraph`的创建过程，这是一个用于可视化SpiderMonkey的Ion编译器图的自定义工具。开发该工具的原因是对现有工具（如Graphviz）的不满。作者发现Graphviz的输出不稳定，且与源代码的直观连接不足。本文介绍了一种简化的Sugiyama布局算法，该算法经过调整，可以利用控制流图的特定属性：来自循环的有限循环和可约控制流。

该算法分为四个主要步骤：**分层**，根据深度和循环结构将块排序到水平轨道中，以模仿源代码的顺序；**创建虚拟节点**，用于跨层路由边，将向下虚拟节点放置在左侧，向上虚拟节点放置在右侧，以实现一致的视觉流；**拉直边**，通过迭代过程对齐节点和虚拟节点，“缩进”循环并减少摆动；以及**跟踪水平边**，将边排序到并行轨道中以防止视觉重叠，并记录总轨道高度以进行最终布局。

与Graphviz相比，主要改进包括稳定的布局（最大限度地减少编译器传递之间的更改）和反映代码结构的直观节点放置。该算法避免了Sugiyama算法的复杂部分（例如交叉最小化），以优先考虑稳定性和效率。交互式演示（可在桌面上使用）允许用户试验图形可视化。最初的实现非常简洁（大约1000行Javascript代码），并针对编译器图可视化进行了优化。

---

## 48. 超越DNS：从AWS 14小时中断事件中汲取的经验

**原文标题**: More than DNS: Learnings from the 14 hour AWS outage

**原文链接**: [https://thundergolfer.com/blog/aws-us-east-1-outage-oct20](https://thundergolfer.com/blog/aws-us-east-1-outage-oct20)

本文分析了 10 月 20 日 AWS us-east-1 区域发生的 14 小时中断事件，重点关注 DynamoDB、EC2 和 NLB 之间相互关联的故障。作者亲身经历了这次中断，并反对诸如“人才流失”或云固有的不可靠性之类的简单解释。

此次中断始于 DynamoDB 的 DNS 管理系统中潜在的“检查时间到使用时间” (TOCTOU) 竞争条件，导致错误的空 DNS 记录。这引发了一系列连锁故障，因为 EC2 依赖 DynamoDB 的 DropletWorkflow Manager (DWFM)，因此失去了对其物理服务器的控制。DWFM 被大量损坏的租约淹没，进入拥塞崩溃状态，需要人工干预。最后，NLB 由于 EC2 的网络管理器滞后而出现问题，导致健康检查系统中出现不良反馈以及错误的 AZ 故障转移。

作者强调，这次故障是多个相互作用因素的结果，而不是单一的“根本原因”，并倡导采用控制系统分析方法，考虑延迟、垃圾回收、保护机制、状态损坏、警报和人工操作。他强调了理解亚稳态故障状态（EC2 经历的）的重要性，以及健康检查系统中不良反馈回路的潜力。文章的结论是，尽管 AWS 的可靠性总体上非常出色，但该事件表明在设计、实施和运营复杂的生产系统方面仍然存在挑战。

---

## 49. Extropic正在构建热力学计算硬件。

**原文标题**: Extropic is building thermodynamic computing hardware

**原文链接**: [https://extropic.ai/](https://extropic.ai/)

Extropic开发热力学计算硬件，发布"热力学计算：从0到1"启动视频。这意味着Extropic正在进军热力学计算领域，或将突破传统CMOS计算的限制。热力学计算利用热力学原理进行计算，可能在能源效率和新型计算架构方面具有优势。"从0到1"可能指的是开发的初始阶段以及该领域取得重大进展的潜力。目前尚无法提供关于正在开发的硬件、目标应用或所利用的热力学原理的更多具体细节。该公告将Extropic定位为热力学计算这一新兴领域的参与者，致力于构建物理硬件解决方案。

---

## 50. Composer：用强化学习构建快速前沿模型

**原文标题**: Composer: Building a fast frontier model with RL

**原文链接**: [https://cursor.com/blog/composer](https://cursor.com/blog/composer)

生成摘要时出错

---

## 51. 中风幸存软件工程师的建议

**原文标题**: Tips for stroke-surviving software engineers

**原文链接**: [https://blog.j11y.io/2025-10-29_stroke_tips_for_engineers/](https://blog.j11y.io/2025-10-29_stroke_tips_for_engineers/)

为中风（特别是顶叶出血性中风并伴有残留癫痫）幸存的软件工程师提供的实用建议。作者本人也是中风幸存者，强调健康优先于工作表现，并学习管理认知需求的重要性。

关键提示包括：

*   **优先休息：** 一旦感到疲劳、思维模糊、恶心或不寻常的感觉，立即停止工作并休息。
*   **控制你的环境：** 尽量使用耳机、眼罩并在家工作，以减少干扰。创建休息的退路。
*   **为自己争取权益：** 利用法律和员工援助计划，保护自己免受不合理的要求。
*   **单线程工作：** 通过批量处理任务并在开始下一个任务之前完成一个任务，避免上下文切换。
*   **外部化工作记忆：** 使用笔记本、白板和像Gemini这样的AI工具，将信息存储从大脑中卸载出来。
*   **优化你的日程：** 在表现最佳的时间（例如上午）处理要求高的任务，并将不太重要的任务委托给其他时间。
*   **最小化注意力需求：** 尽可能禁用通知并避免同步沟通（例如长时间的会议）。
*   **了解神经学基础：** 作者引用研究表明，顶叶和额叶皮层大量参与要求高的认知任务，而损伤会影响处理认知负荷的能力。

作者承认实施这些改变的困难，并鼓励读者在学习适应新常态时对自己保持耐心。

---

## 52. 评估纽约市街道的感知“幽闭恐惧症”（2024）

**原文标题**: Estimating the Perceived 'Claustrophobia' of New York City's Streets (2024)

**原文链接**: [http://mfranchi.net/posts/claustrophobic-streets/](http://mfranchi.net/posts/claustrophobic-streets/)

本文详细介绍了纽约市人行道“幽闭恐惧症”指标的创建，该指标定义为衡量拥挤程度的指标，包括行人和静态杂物。作者旨在量化在城市环境中感到局促的感觉。

该方法包括几个步骤：使用Shapely库分割纽约市开放数据的行人道几何形状，并将其分割成50英尺的增量。杂物识别涉及实地调查与纽约市开放数据集的匹配，每种杂物类型（例如，公交车站、垃圾桶、树木）都被赋予一个权重，以反映其感知的空间占用。行人流量数据来自Nexar行车记录仪图像，使用YOLOv7-E6E目标检测进行分析以计算行人数量，并按人行道宽度进行标准化。

局限性包括缺少人行道用餐等杂物类型的数据流，以及诸如脚手架等元素的不精确数据，依赖建筑许可证来估计其覆盖面积。

最终的“幽闭恐惧症”得分在社区统计区域（NTA）和人口普查区（CT）级别上进行可视化。地图显示曼哈顿中城、杰克逊高地、法拉盛、布鲁克林市中心和威廉斯堡的幽闭恐惧症程度较高。史泰登岛的水平较低。本文最后提供了按幽闭恐惧症程度排名的前20名和后20名社区，并鼓励读者浏览项目GitHub存储库上的其他可视化和数据。

---

## 53. Grammarly更名为“Superhuman”，推出全新AI助手

**原文标题**: Grammarly rebrands to 'Superhuman,' launches a new AI assistant

**原文链接**: [https://techcrunch.com/2025/10/29/grammarly-rebrands-to-superhuman-launches-a-new-ai-assistant/](https://techcrunch.com/2025/10/29/grammarly-rebrands-to-superhuman-launches-a-new-ai-assistant/)

在收购同名邮件客户端后，Grammarly 正将其品牌重塑为“Superhuman”。核心 Grammarly 产品将保留其名称，但其他收购的产品（如 Coda）未来可能会被重新命名。

该公司还推出了 "Superhuman Go"，这是一款集成到 Grammarly 扩展中的人工智能助手。该助手提供写作建议、电子邮件反馈，并与 Jira、Gmail、Google Drive 和 Google Calendar 等应用程序连接，以自动化诸如记录工单或安排会议等任务。未来的计划包括使该助手能够从 CRM 和内部系统获取数据，以改进电子邮件建议。

所有 Grammarly 用户都可以通过扩展中的切换按钮使用 Superhuman Go，并访问包含剽窃检查器和校对员等工具的代理商店。Grammarly 还提供产品捆绑包，包括每月 12 美元（按年计费）的 Pro 订阅，提供多语言支持；以及每月 33 美元（按年计费）的 Business 计划，其中包括 Superhuman Mail。

该公司旨在将人工智能功能集成到 Coda 和 Superhuman 邮件客户端中，自动从外部和内部来源获取详细信息，以增强文档和电子邮件草稿。此举是 Grammarly 成为更全面的生产力套件的更广泛战略的一部分，使其能够与 Notion 和 Google Workspace 等公司竞争。该公告恰逢 TechCrunch Disrupt 2025 大会。

---

## 54. Apple App Store 上的 uBlock Origin Lite

**原文标题**: uBlock Origin Lite in Apple App Store

**原文链接**: [https://apps.apple.com/in/app/ublock-origin-lite/id6745342698](https://apps.apple.com/in/app/ublock-origin-lite/id6745342698)

uBlock Origin Lite (uBOL)，内容拦截器，现已在 Apple App Store 上架。uBOL 由 Raymond Hill 开发，采用声明式方法，依靠浏览器进行过滤，从而最大限度地减少资源消耗。该扩展的服务工作线程仅在用户与弹出面板或选项页面交互时运行。

该应用自带 uBlock Origin 的默认过滤列表，包括 uBlock Origin 的内置过滤器、EasyList、EasyPrivacy 和 Peter Lowe 的广告和跟踪服务器列表。用户可以通过选项页面启用额外的规则集。

该应用获得了积极评价，用户称赞其在 iPadOS 上的可用性和 Safari 集成。评论员特别提到，与最初的 TestFlight 版本相比，电池性能有所提升。虽然无法使用自己的列表进行自定义，但用户对默认过滤列表感到满意。

根据 App 隐私部分显示，开发者不收集任何来自该应用的数据。该应用兼容 iPhone (iOS 18.5+)、iPad (iPadOS 18.5+)、Mac (macOS 13.5+) 和 Apple Vision (visionOS 2.5+)。 它是免费下载和使用的。

---

## 55. Firefox 扩展其推荐扩展程序

**原文标题**: Firefox expands its Recommended Extensions program

**原文链接**: [https://blog.mozilla.org/addons/2025/10/29/new-recommended-extensions-arrived-thanks-to-our-community-curators/](https://blog.mozilla.org/addons/2025/10/29/new-recommended-extensions-arrived-thanks-to-our-community-curators/)

Firefox扩展了其推荐扩展程序计划，新增了多款符合安全、功能和用户体验高标准的扩展。这些扩展是通过社区驱动的策展项目选出的。

新推荐的扩展包括：

*   **Yomitan：** 一款用于语言学习的词典扩展。
*   **Power Thesaurus：** 一款提供同义词和反义词的工具。
*   **PhotoShow：** 允许用户放大和下载网站上的图片。
*   **Simple Gesture for Android：** 为安卓设备添加触摸手势，用于导航和标签页管理。
*   **Immersive Translate：** 翻译各种媒体内容，包括网页、PDF、电子书和视频字幕。
*   **Time Tracker：** 监控网站使用情况并允许屏蔽浪费时间的网站。
*   **Checker Plus for Gmail：** 直接从 Firefox 工具栏管理 Gmail。
*   **YouTube Search Fixer：** 通过移除干扰功能来简化 YouTube 界面。
*   **Notefox：** 允许用户在网站上留下笔记。
*   **Sink It for Reddit：** 通过彩色编码的评论和暗黑模式等功能改善 Reddit 体验。
*   **Raindrop.io：** 一款用于保存和组织网络内容的工具。
*   **Show Video Controls for Firefox：** 为 WebM 视频启用视频控制。
*   **Chrome Mask：** 将 Firefox 伪装成 Chrome，以访问屏蔽或不支持 Firefox 的网站。

文章还感谢了开发者和 Firefox 推荐扩展顾问委员会的贡献。Firefox 计划在 2026 年进行另一次策展项目，并鼓励开发者和用户提名扩展。

---

## 56. 十分钱的MCU演讲

**原文标题**: I made a 10¢ MCU Talk

**原文链接**: [https://www.atomic14.com/2025/10/29/CH32V003-talking](https://www.atomic14.com/2025/10/29/CH32V003-talking)

本文详细介绍了作者如何将音频播放和语音合成功能移植到一款非常廉价（10美分）的CH32V003微控制器上，该微控制器仅有16KB闪存和2KB内存。

首先，他们利用MCU的PWM输出来实现基本的DAC功能，从而解决了音频播放问题。由于闪存容量有限，必须采用激进的音频压缩技术。经过对不同压缩格式的试验，他们最终选择了2位ADPCM，这使他们能够存储大约7秒的音频。他们甚至创建了一个WAV到2位ADPCM的转换器来简化该过程。

接下来，他们探索了使用“Talkie”库的LPC语音合成技术，该技术对人声进行建模，并且比采样音频所需的存储空间要少得多。这使得他们能够在有限的内存中容纳大量的单词和短语。为了从他们自己的声音生成自定义LPC数据，他们尝试了现有工具，并最终创建了一个简化的在线工具，可以将录音转换为LPC格式。

文章最后强调了这款廉价MCU在音频播放（使用2位ADPCM）和语音合成（使用Talkie LPC库）方面的强大功能。作者还分享了他们的GitHub存储库链接，其中包含代码。

---

## 57. Iommi——Django和弦的首选

**原文标题**: Iommi – your first pick for a Django power chord

**原文链接**: [https://iommi.rocks/](https://iommi.rocks/)

本文介绍 Iommi，它被认为是 Django 内置表单的更优替代方案。Iommi 旨在简化表单的创建和管理，尤其适用于复杂场景和可扩展应用程序。

重点突出的主要优势包括：

*   **可扩展性：** Iommi 旨在处理大规模应用程序的复杂性，而 Django 表单可能需要更多的“胶水代码”才能实现类似的功能。
*   **熟悉的 API 与更智能的默认值：** Iommi 保持了与 Django 表单相似的 API，使 Django 开发人员能够轻松学习，同时融入了更好的默认设置，从而改进了开箱即用的功能。
*   **默认情况下出色的 HTML 和设计系统集成：** Iommi 生成高质量的 HTML，可以与现有设计系统无缝集成，从而可能减少对大量自定义 HTML 模板的需求。
*   **从模型自动生成：** Iommi 可以使用 `include/exclude` 选项直接从 Django 模型自动生成表单，以实现精确的字段选择。
*   **增强的外键部件：** 在外键部件中具有异步搜索功能。
*   **跨对象字段路径：** 利用 Django 熟悉的双下划线表示法来导航相关模型和访问字段。

本质上，Iommi 承诺在 Django 中构建表单时采用更强大、高效和集成的方法，尤其是在需要复杂的表单处理和可扩展性的项目中，提供更流畅的体验和更好的结果。

---

## 58. Crunchyroll 正在毁掉它的字幕。

**原文标题**: Crunchyroll is destroying its subtitles

**原文链接**: [https://daiz.moe/crunchyroll-is-destroying-its-subtitles-for-no-good-reason/](https://daiz.moe/crunchyroll-is-destroying-its-subtitles-for-no-good-reason/)

本文认为，Crunchyroll正在降低其字幕质量，特别是在屏幕文字翻译（排版）的处理上，而且没有任何正当理由。作者强调，从2025年夏季到2025年秋季，字幕呈现效果明显下降，与之前相比，较新的字幕缺乏风格化的定位，以及对话与屏幕文字翻译之间的清晰区分。

文章指出，虽然低质量字幕在Crunchyroll上并非新鲜事（由于第三方授权方），但现在却影响到了第一方字幕。这是一个主要问题，因为动漫非常依赖屏幕文字，需要适当的重叠、定位、字体、颜色和动画来实现有效的本地化（排版）。

作者认为，Crunchyroll简化字幕的做法源于需要遵守Netflix和亚马逊Prime Video等普通流媒体服务较低的字幕标准，Crunchyroll将其动漫转授权给这些平台。这些平台通常限制屏幕文字，并且缺乏高级格式化工具。

文章随后深入探讨了Crunchyroll的历史，指出它最初是一个盗版网站，于2009年转型为合法的流媒体服务。它强调了Crunchyroll早期决定使用粉丝字幕组的Aegisub标准和ASS字幕格式，这导致了定制字幕渲染器的开发，最终融合了重叠和定位等功能。转向HTML5和WebAssembly使得进一步的增强成为可能。作者暗示，为了与其他流媒体平台兼容，这种丰富的历史和专业知识正在被牺牲。

---

## 59. 两年后从AWS到裸金属：解答您关于离开AWS的疑问

**原文标题**: AWS to bare metal two years later: Answering your questions about leaving AWS

**原文链接**: [https://oneuptime.com/blog/post/2025-10-29-aws-to-bare-metal-two-years-later/view](https://oneuptime.com/blog/post/2025-10-29-aws-to-bare-metal-two-years-later/view)

2023年，OneUptime分享了他们从AWS迁移到裸金属服务器的经验，每年节省23万美元。本文旨在解答该文章发布后常见的问题，提供两年的更新，并深入探讨该决策。

现在每年节省超过120万美元，OneUptime通过强调S3、出口流量、EKS和NAT网关的节省，证明了他们选择的合理性，即使有Savings Plans/Reserved Instances也是如此。迁移大约需要一周的工程时间，而持续维护平均每季度花费24个工程师工时，与AWS的成本优化工作量相当。

为了解决“单点故障”问题，他们在法兰克福增加了第二个机架，配备冗余网络、镜像Ceph池和隔离的带外管理。使用Anycast入口通过BGP进行每季度演练故障转移到他们旧的AWS集群，可在亚分钟级别进行流量转移。

硬件摊销期为五年，并计划将旧硬件级联到其分析集群中。延长保修期和冷备件可以降低硬件故障风险。

尽管进行了迁移，OneUptime仍然利用AWS的Glacier进行备份，CloudFront进行边缘缓存，以及短期负载测试环境，强调云最适合弹性需求，而裸金属服务器最适合基础负载。他们保持SOC 2 Type II和ISO 27001认证，并调整流程以适应物理数据中心控制和变更管理。该公司最后分享了关于持续维护的见解、未来共享工具的计划，以及列出了仍然适合使用云的情况。

---

## 60. Tailscale服务

**原文标题**: Tailscale Services

**原文链接**: [https://tailscale.com/blog/services-beta](https://tailscale.com/blog/services-beta)

Tailscale 服务是一项新功能，允许用户以更精细的粒度和精确的访问控制来定义和管理网络资源，即使 Tailscale 无法直接安装在资源上。它为任何可访问的逻辑资源分配虚拟 Tailscale IPv4 和 IPv6 地址 (TailVIP) 和唯一的 MagicDNS 名称，使其成为访问控制的策略单元。

主要优势包括简化连接、精确访问控制和通过 API 实现自动化。Tailscale 服务可以用智能路由和可用性机制取代传统的负载均衡器。早期用户已将其应用于各种场景，包括 CI/CD 管道、内部应用程序访问和高可用性的密钥存储。

每个服务都包含一个 TailVIP、MagicDNS 名称、端点定义和一组广告主机。可以通过 API 或管理控制台定义服务。服务主机必须通过验证才能被视为活动状态，并且用户/设备需要显式授权才能通过 TailVIP 或 MagicDNS 名称访问服务。该服务利用 Tailscale 的高可用性选项，通过区域路由智能地将客户端路由到可用的主机。

Tailscale 服务目前处于公开 Beta 阶段，适用于所有计划。该公司计划未来改进，例如配置审计日志、网络流日志、更广泛的主机目标选项、更多状态验证、用于服务主机注册的 API 集成以及与第三方代理的本机集成。用户可以在管理控制台中开始定义服务，或遵循文档。

---

## 61. 如何沉迷式地调整 WezTerm

**原文标题**: How to Obsessively Tune WezTerm

**原文链接**: [https://rashil2000.me/blogs/tune-wezterm](https://rashil2000.me/blogs/tune-wezterm)

无法访问文章链接。

---

## 62. 癌症生存率具有误导性

**原文标题**: Cancer survival rates are misleading

**原文链接**: [https://www.allendowney.com/blog/2025/10/27/cancer-survival-rates-are-misleading/](https://www.allendowney.com/blog/2025/10/27/cancer-survival-rates-are-misleading/)

本文认为，五年癌症生存率常常具有误导性，不应作为评估筛查有效性或治疗进展的唯一依据。作者对四种常见的错误推断提出了质疑：

1.  **个体生存概率：** 早期诊断后91%的五年生存率并不能保证特定患者有91%的生存机会。 整体健康状况、年龄和检测方法等因素会显著影响个体结果。 通过筛查发现的肿瘤通常生长缓慢，这会扭曲生存率。

2.  **筛查益处：** 早期发现的较高生存率并不能自动证明增加筛查的合理性。 只有当筛查能够发现原本会致命的癌症，且治疗有效，并且收益超过筛查的成本（假阳性和过度诊断）时，筛查才有益处。 本文提出了一个马尔可夫模型，表明即使治疗无效也可能出现高生存率。

3.  **反事实生存：** 将患者的死亡归因于延迟发现，并假设早期发现能够确保生存是存在缺陷的。 生存表没有考虑到即使不接受治疗也不会致命的肿瘤。 假设性的早期诊断也需要考虑超出初始五年窗口期的长期生存率。

4.  **治疗改进：** 随着时间的推移，五年生存率的提高并不自动表明治疗效果更好。 更多的筛查和更敏感的检测方法也会通过发现生长缓慢的癌症或过度诊断良性疾病来提高生存率。

本文强调，只有降低死亡率才能明确证明筛查的有效性。 仅仅依靠五年生存率可能会导致对癌症治疗和筛查效果的错误结论。

---

## 63. 视频速率可调彩色电子纸，具备人眼分辨率

**原文标题**: Video‐rate tunable colour electronic paper with human resolution

**原文链接**: [https://www.nature.com/articles/s41586-025-09642-3#MOESM1](https://www.nature.com/articles/s41586-025-09642-3#MOESM1)

本文介绍了一种名为“视网膜电子纸”的新型电子纸技术，旨在实现适用于沉浸式虚拟现实的超高分辨率显示。该技术利用由WO3纳米盘组成的可电调超材料像素，这些纳米盘在电化学还原时经历可逆的绝缘体到金属的转变，从而能够精确控制纳米级的反射率和对比度。这些超材料像素尺寸约为 560 纳米（超过 25,000 PPI），可能与显示器尺寸对应于瞳孔直径时的视觉分辨率极限相匹配。

与在小像素尺寸下存在亮度和均匀性问题的发光显示器不同，视网膜电子纸利用环境光，无论像素尺寸如何，都能保持高光学对比度。通过精确控制 WO3 纳米盘的尺寸和间距，该系统可以选择性地反射 RGB 颜色并实现全彩色视频功能（>25 Hz）。该技术还表现出高反射率（~80%）、强光学对比度（~50%）和低能耗（~0.5–1.7 mW cm–2）。

本文重点介绍了 WO3 超材料像素的设计和特性，展示了如何通过改变纳米盘直径和间距来实现颜色调节。文章强调了优化子像素排列对于准确混色的重要性，因为超高密度下相邻像素之间存在相互作用。通过重构立体3D图像和高分辨率再现古斯塔夫·克里姆特的《吻》，进一步展示了视网膜电子纸的潜力，展示了其在虚拟现实应用和全彩色显示性能方面的能力。

---

## 64. x86指令编码

**原文标题**: Encoding x86 Instructions

**原文链接**: [https://www-user.tu-chemnitz.de/~heha/hs/chm/x86.chm/x86.htm](https://www-user.tu-chemnitz.de/~heha/hs/chm/x86.chm/x86.htm)

本文深入探讨了x86指令的复杂编码，突显了其作为CISC（复杂指令集计算机）架构的复杂性。 它概述了通用格式，表明指令长度可达15字节，包括修改指令行为的前缀。

本文详细介绍了操作码大小，特别关注ADD指令，以及操作码中的位如何确定数据传输方向（d位）和操作数大小（s位）。 MOD-REG-R/M字节对于指定操作数和寻址模式至关重要，其中MOD字段决定寻址模式，REG字段指示源或目标寄存器，R/M字段定义第二个或单个操作数。

寻址模式包括寄存器间接寻址、位移寻址和寄存器寻址。 SIB（比例索引字节）布局支持更复杂的寻址，将索引寄存器按1、2、4或8的因子缩放。 本文给出了使用各种寻址模式编码不同ADD指令的示例，展示了方向位如何影响操作码的选择。

然后，它解释了立即数操作数的编码，立即数操作数具有独特的格式，'x'位确定常量的大小。 MOD-REG-R/M字节中的REG字段充当操作码扩展。 操作数大小前缀（66h）是32位程序中指定16位操作数所必需的。

最后，它涵盖了指令前缀，如repeat/lock和段覆盖前缀。 诸如“add al, constant”之类的常见指令的较短编码也作为节省空间的优化进行了讨论。

---

## 65. 展示HN：用游戏学德语

**原文标题**: Show HN: Learn German with Games

**原文链接**: [https://www.learngermanwithgames.com/](https://www.learngermanwithgames.com/)

此“Show HN”帖子介绍了一系列旨在帮助用户学习德语的游戏。该平台通过各种游戏提供互动式学习，游戏侧重于语言的不同方面，包括：

*   **数字：** 用于数字与文字相互转换、学习报时以及使用时间缩写形式的游戏。
*   **名词：** 用于掌握德语冠词（der, die, das）以及德语和英语名词互译的游戏。
*   **动词：** 用于练习现在时动词变位以及德语和英语动词互译的游戏。

该平台提供至少 10 款游戏，采用适合移动设备的设计，并允许用户根据学习重点（动词、名词、数字）筛选游戏。这些游戏旨在引人入胜，并以有趣且互动的方式帮助构建词汇和语法技能。

---

## 66. 嵌入式状态：2025年第四季度概览

**原文标题**: State of Embedded: Q4 2025 Overview

**原文链接**: [https://sbcwiki.com/news/articles/state-of-embedded-q4-25/](https://sbcwiki.com/news/articles/state-of-embedded-q4-25/)

2025年第四季度嵌入式单板计算机(SBC)市场出现重大进展，基于ARM的片上系统(SoC)正日益挑战x86平台。

**主要亮点：**

*   **英伟达：** 发布了由GB10 Grace Blackwell 超级芯片驱动的 DGX Spark，但 Jetson 软件支持被取消。传闻中搭载Blackwell Ultra GPU的DGX Station 仍未得到证实。
*   **高通：** 推出了 Snapdragon Oryon X2 (主频达5GHz) 和支持主线支持的 Dragon Q6A SBC，与树莓派竞争。 意外收购Arduino，推出了支持主线支持的 Arduino UNO Q SBC，旨在颠覆IoT/边缘计算市场。
*   **瑞芯微：** 公布了采用下一代Arm Mali Magni GPU的 RK3688 和 RK3668 SoC 的路线图。 内核更新持续进行，开源工作取得进展，包括 Mali G610 的 Vulkan 支持。
*   **联发科：** 专注于 Genio 和 Kompanio SoC 的适当软件支持和上游 Linux 集成。 搭载 MT8196 (Kompanio Ultra 910) 的新款笔记本电脑现已上市。
*   **树莓派：** 推出了 Raspberry Pi 500+，一款内置于键盘并具有 M.2 插槽的升级版 Pi 500。
*   **CIX：** 看到更多产品使用他们的 CD8160 SoC (Radxa Orion O6N & OrangePi 6 Plus)。 主线设备树支持正在推进。
*   **德州仪器：** 专注于汽车应用，并为其开发套件中使用的 Imagination BXS-4-64 GPU 进行持续的驱动程序开发。
*   **其他：** 以 U-Boot 闻名的 DENX 停止运营。 Synaptics 正在发布一款新的SBC，与 Toradex 合作使用 Astra SL1680 SoC。

报告总结说，ARM SBC 生态系统蓬勃发展，这得益于开源计划、AI NPU 和软件增强，对 x86 构成了强有力的挑战。

---

## 67. 绿茶垃圾回收器

**原文标题**: The Green Tea Garbage Collector

**原文链接**: [https://go.dev/blog/greenteagc](https://go.dev/blog/greenteagc)

Go 1.25实验性垃圾收集器Green Tea介绍

此Go博客介绍了Green Tea，一个包含在Go 1.25中的实验性垃圾收集器 (通过 `GOEXPERIMENT=greenteagc` 启用)。它的目标是通过减少标记阶段所花费的时间来提高GC性能，标记阶段约占GC总成本的90%。

文章首先解释了Go的标记-清除垃圾回收算法的基础知识，该算法通过图的洪泛识别可达对象，将其标记为已访问，然后清除不可达对象。问题在于，标准算法效率低下，由于其不规则的访问模式，会在访问堆内存时花费大量时间停滞，而NUMA和每个内核的内存带宽减少等现代CPU趋势加剧了这种情况。

Green Tea通过一个简单而有效的核心概念解决了这个问题：处理页面而不是单个对象。这意味着，不是将单个对象添加到工作列表，而是将页面添加到工作列表，并且扫描按页面而不是按对象进行。这导致更可预测的内存访问模式，从而提高缓存利用率并减少停滞。该博客提供了一个可视化演练，展示了Green Tea 与原始算法相比的表现。

初步结果显示出显著的改进，一些工作负载的GC时间减少了高达40%。 Green Tea已经在Google中使用，并被认为是生产就绪的。Go团队计划在Go 1.26中将其作为默认设置，具体取决于用户反馈。

---

## 68. Microsoft seemingly just revealed that OpenAI lost $11.5B last quarter

**原文标题**: Microsoft seemingly just revealed that OpenAI lost $11.5B last quarter

**原文链接**: [https://www.theregister.com/2025/10/29/microsoft_earnings_q1_26_openai_loss/](https://www.theregister.com/2025/10/29/microsoft_earnings_q1_26_openai_loss/)

生成摘要时出错

---

## 69. What we talk about when we talk about sideloading

**原文标题**: What we talk about when we talk about sideloading

**原文链接**: [https://f-droid.org/2025/10/28/sideloading.html](https://f-droid.org/2025/10/28/sideloading.html)

生成摘要时出错

---

## 70. CISA and NSA share tips on securing Microsoft Exchange servers

**原文标题**: CISA and NSA share tips on securing Microsoft Exchange servers

**原文链接**: [https://www.bleepingcomputer.com/news/security/cisa-and-nsa-share-tips-on-securing-microsoft-exchange-servers/](https://www.bleepingcomputer.com/news/security/cisa-and-nsa-share-tips-on-securing-microsoft-exchange-servers/)

生成摘要时出错

---

## 71. It's insulting to read AI-generated blog posts

**原文标题**: It's insulting to read AI-generated blog posts

**原文链接**: [https://blog.pabloecortez.com/its-insulting-to-read-your-ai-generated-blog-post/](https://blog.pabloecortez.com/its-insulting-to-read-your-ai-generated-blog-post/)

生成摘要时出错

---

## 72. A century of reforestation helped keep the eastern US cool (2024)

**原文标题**: A century of reforestation helped keep the eastern US cool (2024)

**原文链接**: [https://news.agu.org/press-release/a-century-of-reforestation-helped-keep-the-eastern-us-cool/](https://news.agu.org/press-release/a-century-of-reforestation-helped-keep-the-eastern-us-cool/)

生成摘要时出错

---

## 73. Character.ai to bar children under 18 from using its chatbots

**原文标题**: Character.ai to bar children under 18 from using its chatbots

**原文链接**: [https://www.nytimes.com/2025/10/29/technology/characterai-underage-users.html](https://www.nytimes.com/2025/10/29/technology/characterai-underage-users.html)

生成摘要时出错

---

## 74. Quantifying pass-by-value overhead

**原文标题**: Quantifying pass-by-value overhead

**原文链接**: [https://owen.cafe/posts/struct-sizes/](https://owen.cafe/posts/struct-sizes/)

生成摘要时出错

---

## 75. Why imperfection could be key to Turing patterns in nature

**原文标题**: Why imperfection could be key to Turing patterns in nature

**原文链接**: [https://arstechnica.com/science/2025/10/why-imperfection-could-be-key-to-turing-patterns-in-nature/](https://arstechnica.com/science/2025/10/why-imperfection-could-be-key-to-turing-patterns-in-nature/)

生成摘要时出错

---

## 76. Apple will phase out Rosetta 2 in macOS 28

**原文标题**: Apple will phase out Rosetta 2 in macOS 28

**原文链接**: [https://developer.apple.com/documentation/apple-silicon/about-the-rosetta-translation-environment](https://developer.apple.com/documentation/apple-silicon/about-the-rosetta-translation-environment)

生成摘要时出错

---

## 77. How blocks are chained in a blockchain

**原文标题**: How blocks are chained in a blockchain

**原文链接**: [https://www.johndcook.com/blog/2025/10/27/blockchain/](https://www.johndcook.com/blog/2025/10/27/blockchain/)

生成摘要时出错

---

## 78. SwirlDB: Modular-first, CRDT-based embedded database

**原文标题**: SwirlDB: Modular-first, CRDT-based embedded database

**原文链接**: [https://docs.swirldb.org/](https://docs.swirldb.org/)

生成摘要时出错

---

## 79. Show HN: Research Hacker News, ArXiv & Google with Hierarchical Bayesian Models

**原文标题**: Show HN: Research Hacker News, ArXiv & Google with Hierarchical Bayesian Models

**原文链接**: [https://sturdystatistics.com/deepdive-search](https://sturdystatistics.com/deepdive-search)

生成摘要时出错

---

## 80. OS/2 Warp, PowerPC Edition (2011)

**原文标题**: OS/2 Warp, PowerPC Edition (2011)

**原文链接**: [https://www.os2museum.com/wp/os2-history/os2-warp-powerpc-edition/](https://www.os2museum.com/wp/os2-history/os2-warp-powerpc-edition/)

生成摘要时出错

---

## 81. Detour: Dynamic linking on Linux without Libc

**原文标题**: Detour: Dynamic linking on Linux without Libc

**原文链接**: [https://github.com/graphitemaster/detour](https://github.com/graphitemaster/detour)

生成摘要时出错

---

## 82. Hosting SQLite Databases on GitHub Pages (2021)

**原文标题**: Hosting SQLite Databases on GitHub Pages (2021)

**原文链接**: [https://phiresky.github.io/blog/2021/hosting-sqlite-databases-on-github-pages/](https://phiresky.github.io/blog/2021/hosting-sqlite-databases-on-github-pages/)

生成摘要时出错

---

## 83. Generative AI Image Editing Showdown

**原文标题**: Generative AI Image Editing Showdown

**原文链接**: [https://genai-showdown.specr.net/image-editing](https://genai-showdown.specr.net/image-editing)

生成摘要时出错

---

## 84. A Fork in the Road: Deciding Kafka's Diskless Future

**原文标题**: A Fork in the Road: Deciding Kafka's Diskless Future

**原文链接**: [https://jack-vanlightly.com/blog/2025/10/22/a-fork-in-the-road-deciding-kafkas-diskless-future](https://jack-vanlightly.com/blog/2025/10/22/a-fork-in-the-road-deciding-kafkas-diskless-future)

生成摘要时出错

---

## 85. Keep Android Open

**原文标题**: Keep Android Open

**原文链接**: [http://keepandroidopen.org/](http://keepandroidopen.org/)

生成摘要时出错

---

## 86. Collins Aerospace: Sending text messages to the cockpit with test:test

**原文标题**: Collins Aerospace: Sending text messages to the cockpit with test:test

**原文链接**: [https://www.ccc.de/en/disclosure/collins-aerospace-mit-test-test-textnachrichten-bis-ins-cockpit-senden](https://www.ccc.de/en/disclosure/collins-aerospace-mit-test-test-textnachrichten-bis-ins-cockpit-senden)

生成摘要时出错

---

## 87. Movycat – A terminal movie player written in Zig

**原文标题**: Movycat – A terminal movie player written in Zig

**原文链接**: [https://github.com/M64GitHub/movycat](https://github.com/M64GitHub/movycat)

生成摘要时出错

---

## 88. The end of the rip-off economy: consumers use LLMs against information asymmetry

**原文标题**: The end of the rip-off economy: consumers use LLMs against information asymmetry

**原文链接**: [https://www.economist.com/finance-and-economics/2025/10/27/the-end-of-the-rip-off-economy](https://www.economist.com/finance-and-economics/2025/10/27/the-end-of-the-rip-off-economy)

生成摘要时出错

---

## 89. ChatGPT's Atlas: The Browser That's Anti-Web

**原文标题**: ChatGPT's Atlas: The Browser That's Anti-Web

**原文链接**: [https://www.anildash.com//2025/10/22/atlas-anti-web-browser/](https://www.anildash.com//2025/10/22/atlas-anti-web-browser/)

生成摘要时出错

---

## 90. Show HN: Pipelex – Declarative language for repeatable AI workflows

**原文标题**: Show HN: Pipelex – Declarative language for repeatable AI workflows

**原文链接**: [https://github.com/Pipelex/pipelex](https://github.com/Pipelex/pipelex)

生成摘要时出错

---

## 91. The AirPods Pro 3 flight problem

**原文标题**: The AirPods Pro 3 flight problem

**原文链接**: [https://basicappleguy.com/basicappleblog/the-airpods-pro-3-flight-problem](https://basicappleguy.com/basicappleblog/the-airpods-pro-3-flight-problem)

生成摘要时出错

---

## 92. I'm Independently Verifying Go's Reproducible Builds

**原文标题**: I'm Independently Verifying Go's Reproducible Builds

**原文链接**: [https://www.agwa.name/blog/post/verifying_go_reproducible_builds](https://www.agwa.name/blog/post/verifying_go_reproducible_builds)

生成摘要时出错

---

## 93. Alphabet tops $100B quarterly revenue for first time, cloud grows 34%

**原文标题**: Alphabet tops $100B quarterly revenue for first time, cloud grows 34%

**原文链接**: [https://www.cnbc.com/2025/10/29/alphabet-google-q3-earnings.html](https://www.cnbc.com/2025/10/29/alphabet-google-q3-earnings.html)

生成摘要时出错

---

## 94. From VS Code to Helix

**原文标题**: From VS Code to Helix

**原文链接**: [https://ergaster.org/posts/2025/10/29-vscode-to-helix/](https://ergaster.org/posts/2025/10/29-vscode-to-helix/)

生成摘要时出错

---

## 95. JPMorgan Tokenizes Private-Equity Fund on Its Own Blockchain

**原文标题**: JPMorgan Tokenizes Private-Equity Fund on Its Own Blockchain

**原文链接**: [https://www.wsj.com/finance/investing/jpmorgan-tokenizes-private-equity-fund-on-its-own-blockchain-729dadda](https://www.wsj.com/finance/investing/jpmorgan-tokenizes-private-equity-fund-on-its-own-blockchain-729dadda)

生成摘要时出错

---

## 96. Nvidia takes $1B stake in Nokia

**原文标题**: Nvidia takes $1B stake in Nokia

**原文链接**: [https://www.cnbc.com/2025/10/28/nvidia-nokia-ai.html](https://www.cnbc.com/2025/10/28/nvidia-nokia-ai.html)

生成摘要时出错

---

## 97. HTTPS by default

**原文标题**: HTTPS by default

**原文链接**: [https://security.googleblog.com/2025/10/https-by-default.html](https://security.googleblog.com/2025/10/https-by-default.html)

生成摘要时出错

---

## 98. NASA, DARPA Will Test Nuclear Engine for Future Mars Missions

**原文标题**: NASA, DARPA Will Test Nuclear Engine for Future Mars Missions

**原文链接**: [https://www.nasa.gov/news-release/nasa-darpa-will-test-nuclear-engine-for-future-mars-missions/](https://www.nasa.gov/news-release/nasa-darpa-will-test-nuclear-engine-for-future-mars-missions/)

生成摘要时出错

---

## 99. The International Criminal Court wants to become independent of USA technology

**原文标题**: The International Criminal Court wants to become independent of USA technology

**原文链接**: [https://www.heise.de/en/news/International-Criminal-Court-Kicks-Out-Microsoft-10964189.html](https://www.heise.de/en/news/International-Criminal-Court-Kicks-Out-Microsoft-10964189.html)

生成摘要时出错

---

## 100. We need a clearer framework for AI-assisted contributions to open source

**原文标题**: We need a clearer framework for AI-assisted contributions to open source

**原文链接**: [https://samsaffron.com/archive/2025/10/27/your-vibe-coded-slop-pr-is-not-welcome](https://samsaffron.com/archive/2025/10/27/your-vibe-coded-slop-pr-is-not-welcome)

生成摘要时出错

---

