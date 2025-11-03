# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-11-03.md)

*最后自动更新时间: 2025-11-03 17:51:28*
## 1. 我们为什么从Python迁移到Node.js

**原文标题**: Why We Migrated from Python to Node.js

**原文链接**: [https://blog.yakkomajuri.com/blog/python-to-node](https://blog.yakkomajuri.com/blog/python-to-node)

Skald上线一周后，将其后端从Python (Django) 重写为 Node.js (Express + MikroORM)，尽管通常建议优先关注产品与市场的契合度，但他们优先考虑了可扩展性。 主要原因是Django中Python的异步能力难以满足需求，对于处理其RAG API平台所需的众多对LLM和嵌入服务的异步API调用来说，它显得笨重且不直观。

作者对Node.js中的异步操作经验丰富，认为Python的异步支持是“打补丁”式的添加，而非核心功能，这导致了复杂性和性能瓶颈。 他们探索了FastAPI等替代方案，但最终选择了Node.js来统一代码库，因为他们的后台工作服务已经用Node.js编写。

迁移后，吞吐量提高了约3倍，并实现了并发处理的能力。 虽然他们怀念Django的易用性和ORM，但他们获得了统一代码库、更好的测试以及对MikroORM的熟悉等好处。 他们承认失去了Python生态系统的丰富性，尤其是在机器学习方面，但接受了这种权衡，以换取效率和可维护性的即时提升。 他们愿意接受对其决定的任何批评，只要能让他们更多地了解Python的异步能力。 他们得出结论，重写是有益且是一次学习经验，并分享了pull request的链接以供审查。

---

## 2. Learning to read Arthur Whitney's C to become Smart (2024)

**原文标题**: Learning to read Arthur Whitney's C to become Smart (2024)

**原文链接**: [https://needleful.net/blog/2024/01/arthur_whitney.html](https://needleful.net/blog/2024/01/arthur_whitney.html)

生成摘要时出错

---

## 3. 社交媒体戒断月

**原文标题**: No Socials November

**原文链接**: [https://bjhess.com/posts/no-socials-november](https://bjhess.com/posts/no-socials-november)

生成摘要时出错

---

## 4. Vim图

**原文标题**: VimGraph

**原文链接**: [https://resources.wolframcloud.com/FunctionRepository/resources/VimGraph/](https://resources.wolframcloud.com/FunctionRepository/resources/VimGraph/)

生成摘要时出错

---

## 5. 反对PGVector 的理由

**原文标题**: The Case Against PGVector

**原文链接**: [https://alex-jacobs.com/posts/the-case-against-pgvector/](https://alex-jacobs.com/posts/the-case-against-pgvector/)

生成摘要时出错

---

## 6. Linux内核的WebAssembly (WASM) 架构支持

**原文标题**: WebAssembly (WASM) arch support for the Linux kernel

**原文链接**: [https://github.com/joelseverin/linux-wasm](https://github.com/joelseverin/linux-wasm)

本文档描述了一个项目，该项目提供脚本以在 WebAssembly (Wasm) 上构建和运行 Linux 系统。该项目利用了几个软件组件：LLVM（已针对 GNU ld 样式链接器脚本进行了修补）、Linux 内核（已针对 Wasm 架构支持、binfmt 和 Web 控制台驱动程序进行了修补）、musl libc（已针对 Wasm 目标支持进行了修补）、BusyBox（已针对 clang/wasm-ld 兼容性和 Wasm 默认配置进行了修补）、一个最小的 initramfs 和一个运行时（基于 JavaScript 的 Wasm 主机示例）。

构建过程包括下载和修补这些组件，然后使用 clang 和 wasm-ld 编译它们。主要挑战包括 musl 不完整的 Wasm 支持，以及 Linux 内核构建系统中的限制，这些限制需要用于交叉编译器安装的无空格路径。生成的系统是一个 Linux 内核，可以在 Wasm 环境中将 .wasm 文件作为可执行文件执行。

该文档提供了在主机上或 Docker 容器中直接运行构建脚本的说明。提供了两种 Docker 容器配置：`linux-wasm-base`（一个具有必要工具的开发环境）和 `linux-wasm-contained`（用于隔离构建）。提供的 `linux-wasm.sh` 脚本管理下载和构建，并提供用于选择性重建组件的选项。运行时提供示例 JavaScript 代码来启动 Wasm 环境并与内核交互。

该文档还强调了由于 Wasm 缺乏 MMU，因此需要在 NOMMU 配置中构建 Linux，并建议对 Wasm 程序使用 `-fPIC/-shared` 或 syscalls 代理，同时指出共享内存和内存保护之间的权衡。

---

## 7. 罗伯特·胡克致戈特弗里德·莱布尼茨的“赛博朋克”信件

**原文标题**: Robert Hooke's "Cyberpunk” Letter to Gottfried Leibniz

**原文链接**: [https://mynamelowercase.com/blog/robert-hookes-cyberpunk-letter-to-gottfried-leibniz/](https://mynamelowercase.com/blog/robert-hookes-cyberpunk-letter-to-gottfried-leibniz/)

This article explores Robert Hooke's 1681 letter to Gottfried Leibniz, arguing it embodies a "cyberpunk" sensibility centuries before the genre existed. The author, who discovered the letter in the Royal Society archives, finds it significant because it demonstrates Hooke's engagement with Leibniz's "Characteristica Universalis," a project to create a universal language for science capable of mechanizing reasoning. This idea, which Norbert Wiener saw as a precursor to cybernetics, is framed as a proto-computer programming language.

The article posits that Hooke's letter goes beyond mere cybernetics. While Leibniz envisioned a system for rational thought, Hooke foresaw the potential for this language to empower individuals and bypass restrictive authorities. He hoped a universally accessible system of thought would allow for the free exploration and testing of ideas without censorship, a key element of cyberpunk's do-it-yourself ethos.

The author connects Hooke's life experiences – a politically charged upbringing, a penchant for hands-on tinkering, and clashes with authority – to this vision. They argue that Hooke's belief in the liberating potential of mechanized reasoning, particularly in challenging established power structures, aligns him with the core tenets of cyberpunk. Therefore, the article proposes that, just as Wiener is considered the patron saint of cybernetics, Hooke should be considered the patron saint of cyberpunk.


---

## 8. 具名颜色所覆盖的RGB空间可视化

**原文标题**: A visualization of the RGB space covered by named colors

**原文链接**: [https://codepen.io/meodai/full/zdgXJj/](https://codepen.io/meodai/full/zdgXJj/)

无法访问文章链接。

---

## 9. Skyfall-GS：从卫星图像合成沉浸式3D城市场景

**原文标题**: Skyfall-GS – Synthesizing Immersive 3D Urban Scenes from Satellite Imagery

**原文链接**: [https://skyfall-gs.jayinnn.dev/](https://skyfall-gs.jayinnn.dev/)

Skyfall-GS：一种生成大规模、可探索、几何精确的三维城市场景的新框架，无需依赖昂贵的3D扫描进行训练。它认识到现有方法因高质量3D数据稀缺而存在的局限性，利用易于获取的卫星图像进行粗略几何建模，并利用开放域扩散模型生成高质量纹理。

其核心创新在于协同这两种数据源，以创建城市街区尺度上的逼真三维环境，从而实现实时的沉浸式探索。Skyfall-GS采用课程驱动的迭代优化策略。这种渐进式方法增强了生成场景的几何完整性和照片级真实纹理，从而产生更高质量的输出。

本质上，Skyfall-GS通过绕过对大量3D标注的需求，解决了创建大规模3D城市环境的挑战。相反，它巧妙地将易于获取的卫星图像与扩散模型相结合，以实现逼真且可探索的3D世界。结果表明，与其他方法相比，不同视角的几何一致性更好，纹理也更逼真。

---

## 10. 为什么Nextcloud用起来感觉很慢

**原文标题**: Why Nextcloud feels slow to use

**原文链接**: [https://ounapuu.ee/posts/2025/11/03/nextcloud-slow/](https://ounapuu.ee/posts/2025/11/03/nextcloud-slow/)

本文探讨了作者对Nextcloud性能的不满，特别是其加载速度缓慢的问题，即使在配置不错的硬件上也是如此。作者认为这种缓慢的根源在于需要下载和执行过多的JavaScript，通常每个页面加载都需要15-20MB，即使压缩后仍有4-5MB，对于一个Web应用程序来说，这还是太多了。

作者指出了导致这种臃肿的具体JavaScript包，例如`core-common.js`、`NotificationsApp.chunk.mjs`，以及Calendar、Files和Notes等应用程序的大型特定JavaScript。他提供了这些应用程序在较慢的连接上加载所需时间的示例，突出了糟糕的用户体验。他举例说明了Tasks应用程序在iPhone上需要5-10秒才能加载。

作者怀疑Nextcloud的架构，及其通过通用库强调统一体验的方式，是根本原因。他认为功能与包大小的比例失调。

为了解决这个问题，作者已经开始用更轻量级的替代品替换一些Nextcloud应用程序，例如用Vikunja处理任务，用Immich处理照片，欣赏它们显著更小的JavaScript体积和更高的速度。虽然作者承认Nextcloud的功能集对其他功能很方便，但他仍然对其性能不满意。

作者承认造成这种情况的潜在原因，例如开发团队工作量过大，但他强调了这对用户体验和可访问性的负面影响。他最后推荐了Alex Russell关于Web性能的研究，以及在开发过程中考虑这些因素的重要性。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 2 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 3 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 4 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 5 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 6 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 7 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 8 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 9 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 10 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 11 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 12 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 13 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 14 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 15 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 16 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 17 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 18 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 19 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 20 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 21 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 22 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 23 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 24 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 25 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 26 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 27 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 28 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 29 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 30 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 31 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 32 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 33 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 34 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 35 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 36 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 37 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 38 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 39 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 40 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 41 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 42 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 43 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 44 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 45 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 46 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 47 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 48 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 49 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 50 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 51 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 52 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 53 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 54 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 55 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 56 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 57 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 58 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 59 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 60 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 61 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 62 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 63 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 64 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 65 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 66 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 67 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 68 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 69 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 70 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 71 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 72 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 73 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 74 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 75 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 76 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 77 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 78 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 79 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 80 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 81 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 82 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 83 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 84 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 85 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 86 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 87 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 88 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 89 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 90 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 91 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 92 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 93 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 94 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 95 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 96 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 97 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 98 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 99 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 100 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 101 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 102 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 103 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 104 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 105 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 106 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 107 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 108 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 109 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 110 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 111 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 112 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 113 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 114 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 115 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 116 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 117 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 118 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 119 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 120 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 121 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 122 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 123 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 124 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 125 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 126 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 127 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 128 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 129 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 130 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 131 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 132 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 133 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 134 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 135 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 136 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 137 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 138 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 139 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 140 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 141 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 142 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 143 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 144 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 145 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 146 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 147 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 148 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 149 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 150 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 151 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 152 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 153 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 154 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 155 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 156 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 157 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 158 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 159 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 160 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 161 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 162 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 163 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 164 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 165 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 166 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 167 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 168 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 169 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 170 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 171 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 172 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 173 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 174 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 175 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 176 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 177 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 178 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 179 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 180 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 181 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 182 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 183 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 184 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 185 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 186 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 187 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 188 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 189 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 190 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 191 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 192 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 193 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 194 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 195 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 196 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 197 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 198 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 199 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 200 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 201 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 202 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 203 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 204 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 205 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 206 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 207 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 208 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 209 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 210 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 211 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 212 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 213 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 214 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 215 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 216 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 217 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 218 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 219 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 220 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 221 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 222 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 223 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 224 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 225 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 226 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 227 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 228 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
