# Hacker News 热门文章摘要 (2026-06-24)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. OpenAI发布首款由博通打造的定制芯片

**原文标题**: OpenAI unveils its first custom chip, built by Broadcom

**原文链接**: [https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/)

OpenAI 发布了首款自研处理器，这是一款名为 Jalapeño 的推理芯片，由其与博通（Broadcom）合作开发。该芯片专为处理推理任务（即运行预构建 AI 模型的过程）而设计，而非资源密集型的预训练阶段，后者预计仍将依赖英伟达（Nvidia）的硬件。

此次发布的一个关键亮点是，OpenAI 利用其自身的 AI 模型辅助了该芯片的开发。初步结果显示，Jalapeño 的能效比显著优于目前最先进的替代产品。通过研发自研芯片，OpenAI 旨在减少对英伟达 GPU 的高度依赖，并降低运行代码模型等实时服务的运营成本。

此举标志着 OpenAI 向垂直整合迈出了战略性的一步。通过设计包括芯片架构、内存系统和网络在内的自有基础设施，OpenAI 可以优化其技术栈的每一个层面。这种做法与谷歌（Google）和亚马逊（Amazon）等竞争对手采用的“AI 加速器”策略如出一辙。

OpenAI 总裁格雷格·布罗克曼（Greg Brockman）强调，该处理器的设计初衷是加速特定的、目前尚未得到充分支持的工作负载。最终，该公司希望通过优化底层基础设施的经济效益，使 Jalapeño 芯片能让其 AI 模型对用户而言变得更快、更可靠且更实惠。

---

## 2. RubyLLM：支持所有主流 AI 提供商的 Ruby 框架

**原文标题**: RubyLLM: A Ruby framework for all major AI providers

**原文链接**: [https://rubyllm.com/](https://rubyllm.com/)

**RubyLLM** 是一个统一、轻量级的框架，旨在简化 AI 在 Ruby 应用程序中的集成。它通过为涵盖所有主要供应商（包括 OpenAI、Anthropic (Claude)、Google (Gemini/VertexAI)、xAI、Mistral 以及通过 Ollama 运行的本地模型）的 800 多种模型提供单一、优美的接口，消除了使用多个不一致客户端库带来的阻碍。

**核心特性：**
*   **多模态能力：** 除了标准的文本聊天，该框架还通过简洁的 `with:` 语法处理视觉（图像/视频）、音频转录和文档分析（PDF、CSV 等）。
*   **全面的 AI 工具：** 内置对图像生成 (`paint`)、嵌入 (`embed`) 和内容审核的支持。
*   **高级架构：** 开发者可以创建自定义 **Tools**（允许 AI 执行 Ruby 方法），定义具有特定指令的 **Agents**，并使用 JSON schema 强制执行**结构化输出**。
*   **性能与开发者体验：** 该库经过“实战检验”，且依赖极少（Faraday、Zeitwerk 和 Marcel）。它支持流式响应、基于 Fiber 的并发以及深度思考（Extended Thinking）推理。

**Rails 集成：**
RubyLLM 为 Ruby on Rails 提供了深度集成，包括通过 `acts_as_chat` 实现的 ActiveRecord 支持。它提供了数据库迁移生成器和开箱即用的聊天 UI，让开发者几乎可以瞬间在 `localhost:3000/chats` 部署功能完备的 AI 界面。

总之，RubyLLM 为 Ruby 开发者提供了一个“一站式解决方案”，用于构建从简单聊天机器人到复杂的 RAG（检索增强生成）应用及自主代理的一切，而无需承担管理多种 API 规范的开销。

---

## 3. NSA 在与 Anthropic 的纠纷中失去了对 Mythos 的访问权限

**原文标题**: NSA lost access to Mythos amid Anthropic dispute

**原文链接**: [https://www.nytimes.com/2026/06/23/us/politics/nsa-lost-access-anthropic-tool.html](https://www.nytimes.com/2026/06/23/us/politics/nsa-lost-access-anthropic-tool.html)

无法访问文章链接。

---

## 4. There are a few things that I look back on as my mistakes in the early days

**原文标题**: There are a few things that I look back on as my mistakes in the early days

**原文链接**: [https://twitter.com/ID_AA_Carmack/status/2069799283369345247](https://twitter.com/ID_AA_Carmack/status/2069799283369345247)

In this retrospective, legendary programmer John Carmack reflects on his management and technical mistakes during the early days of id Software, particularly during the development of *Quake*.

Carmack highlights several key areas of regret:

*   **Technical Over-ambition:** He believes *Quake* was too ambitious for its time. He suggests that building on an enhanced *Doom* engine first would have provided a more stable foundation for designers, rather than "rug-pulling" the technology during development. 
*   **Management and Burnout:** Carmack admits to pushing his team too hard with "startup intensity," failing to recognize that a maturing company needs more "slack" to prevent burnout. He also acknowledges reaching his own personal limits of productivity during this era.
*   **Business Structure:** He criticizes the company’s original stock and buy/sell agreements, noting that they created poor incentives. He suggests that the standard Silicon Valley approach of vesting stock would have been a superior model.
*   **Design Culture:** A major point of friction was the requirement for level designers to also be high-end visual artists. This expectation, while set early on, led to internal infighting and the disparagement of designers who focused more on gameplay than aesthetics.

Carmack concludes by specifically apologizing to designer Sandy Petersen for the toxic environment created by these design expectations, acknowledging that the company should have paired specialized artists with designers much earlier.

---

## 5. 我们将 Bunny DNS 设为免费

**原文标题**: We’re making Bunny DNS free

**原文链接**: [https://bunny.net/blog/were-making-bunny-dns-free/](https://bunny.net/blog/were-making-bunny-dns-free/)

生成摘要时出错

---

## 6. PR spam today looks like email spam in the early 2000s

**原文标题**: PR spam today looks like email spam in the early 2000s

**原文链接**: [https://www.greptile.com/blog/prs-on-openclaw](https://www.greptile.com/blog/prs-on-openclaw)

生成摘要时出错

---

## 7. I taught a bucket to speak Git

**原文标题**: I taught a bucket to speak Git

**原文链接**: [https://www.tigrisdata.com/blog/objgit/](https://www.tigrisdata.com/blog/objgit/)

生成摘要时出错

---

## 8. Computer use in Gemini 3.5 Flash

**原文标题**: Computer use in Gemini 3.5 Flash

**原文链接**: [https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/)

生成摘要时出错

---

## 9. Show HN: Nub – A Bun-like all-in-one toolkit for Node.js

**原文标题**: Show HN: Nub – A Bun-like all-in-one toolkit for Node.js

**原文链接**: [https://github.com/nubjs/nub](https://github.com/nubjs/nub)

生成摘要时出错

---

## 10. Stealing Is a Skill

**原文标题**: Stealing Is a Skill

**原文链接**: [https://ben-mini.com/2026/stealing-is-a-skill](https://ben-mini.com/2026/stealing-is-a-skill)

生成摘要时出错

---

## 11. Krea 2: SOTA open-weights 12B image model

**原文标题**: Krea 2: SOTA open-weights 12B image model

**原文链接**: [https://www.krea.ai/blog/krea-2-technical-report](https://www.krea.ai/blog/krea-2-technical-report)

生成摘要时出错

---

## 12. Pull request limits are cutting down the noise

**原文标题**: Pull request limits are cutting down the noise

**原文链接**: [https://github.blog/open-source/maintainers/how-pull-request-limits-are-cutting-down-the-noise/](https://github.blog/open-source/maintainers/how-pull-request-limits-are-cutting-down-the-noise/)

生成摘要时出错

---

## 13. Running Windows Games on a Hobby OS with Wine

**原文标题**: Running Windows Games on a Hobby OS with Wine

**原文链接**: [https://astral-os.org/posts/2026/04/03/wine-on-astral.html](https://astral-os.org/posts/2026/04/03/wine-on-astral.html)

生成摘要时出错

---

## 14. I rewrote PostHog's SQL parser, 70x faster, while barely looking at the code

**原文标题**: I rewrote PostHog's SQL parser, 70x faster, while barely looking at the code

**原文链接**: [https://posthog.com/blog/sql-parser](https://posthog.com/blog/sql-parser)

生成摘要时出错

---

## 15. Show HN: Monolisa v3 – a typeface for developers and creatives

**原文标题**: Show HN: Monolisa v3 – a typeface for developers and creatives

**原文链接**: [https://www.monolisa.dev/](https://www.monolisa.dev/)

生成摘要时出错

---

## 16. Genuinely, my all-time favourite image: Mamenchisaurus hochuanensis

**原文标题**: Genuinely, my all-time favourite image: Mamenchisaurus hochuanensis

**原文链接**: [https://svpow.com/2026/06/04/genuinely-my-all-time-favourite-image-mamenchisaurus-hochuanensis/](https://svpow.com/2026/06/04/genuinely-my-all-time-favourite-image-mamenchisaurus-hochuanensis/)

生成摘要时出错

---

## 17. A Practical Guide to SSH Tunnels: Local and Remote Port Forwarding

**原文标题**: A Practical Guide to SSH Tunnels: Local and Remote Port Forwarding

**原文链接**: [https://labs.iximiuz.com/tutorials/ssh-tunnels](https://labs.iximiuz.com/tutorials/ssh-tunnels)

生成摘要时出错

---

## 18. The Xteink X4 E-Ink Reader

**原文标题**: The Xteink X4 E-Ink Reader

**原文链接**: [https://blog.omgmog.net/post/xteink-x4-e-ink-reader/](https://blog.omgmog.net/post/xteink-x4-e-ink-reader/)

生成摘要时出错

---

## 19. Show HN: peerd – AI agent harness that runs entirely in your browser

**原文标题**: Show HN: peerd – AI agent harness that runs entirely in your browser

**原文链接**: [https://github.com/NotASithLord/peerd](https://github.com/NotASithLord/peerd)

生成摘要时出错

---

## 20. Too many R packages: CRAN is inundated with submissions

**原文标题**: Too many R packages: CRAN is inundated with submissions

**原文链接**: [https://rworks.dev/posts/too-many-R-packages/](https://rworks.dev/posts/too-many-R-packages/)

生成摘要时出错

---

## 21. Why eval startups fail (2025)

**原文标题**: Why eval startups fail (2025)

**原文链接**: [https://thomasliao.com/eval-startups](https://thomasliao.com/eval-startups)

生成摘要时出错

---

## 22. Boffin claims Microsoft's "quantum leap" is invalid due to "basic Python errors"

**原文标题**: Boffin claims Microsoft's "quantum leap" is invalid due to "basic Python errors"

**原文链接**: [https://www.theregister.com/research/2026/06/24/boffin-claims-microsofts-supposed-quantum-leap-does-not-compute-due-to-basic-python-errors/5260489](https://www.theregister.com/research/2026/06/24/boffin-claims-microsofts-supposed-quantum-leap-does-not-compute-due-to-basic-python-errors/5260489)

生成摘要时出错

---

## 23. How a Microsecond-Level Low-Latency Engine Works

**原文标题**: How a Microsecond-Level Low-Latency Engine Works

**原文链接**: [https://medium.com/@DolphinDB_Inc/c-speed-without-c-pain-inside-a-microsecond-level-low-latency-engine-a634f260a4ee](https://medium.com/@DolphinDB_Inc/c-speed-without-c-pain-inside-a-microsecond-level-low-latency-engine-a634f260a4ee)

生成摘要时出错

---

## 24. Journalism is rearranging the deckchairs. It needs to reinvent itself

**原文标题**: Journalism is rearranging the deckchairs. It needs to reinvent itself

**原文链接**: [https://werd.io/journalism-is-rearranging-the-deckchairs-it-needs-to-reinvent-itself/](https://werd.io/journalism-is-rearranging-the-deckchairs-it-needs-to-reinvent-itself/)

生成摘要时出错

---

## 25. For Most of the World, Open-Source AI Is the Only Way Forward

**原文标题**: For Most of the World, Open-Source AI Is the Only Way Forward

**原文链接**: [https://techstrong.ai/articles/for-most-of-the-world-open-source-ai-is-the-only-way-forward/](https://techstrong.ai/articles/for-most-of-the-world-open-source-ai-is-the-only-way-forward/)

生成摘要时出错

---

## 26. Show HN: Pure Effect – Reproduce production bugs on your laptop without a DB

**原文标题**: Show HN: Pure Effect – Reproduce production bugs on your laptop without a DB

**原文链接**: [https://pure-effect.org](https://pure-effect.org)

生成摘要时出错

---

## 27. Haystack: Open-Source AI Framework for Production Ready Agents, RAG

**原文标题**: Haystack: Open-Source AI Framework for Production Ready Agents, RAG

**原文链接**: [https://haystack.deepset.ai/](https://haystack.deepset.ai/)

生成摘要时出错

---

## 28. Raspberry Pi Pico W as USB Wi-Fi Adapter

**原文标题**: Raspberry Pi Pico W as USB Wi-Fi Adapter

**原文链接**: [https://gitlab.com/baiyibai/pico-usb-wifi](https://gitlab.com/baiyibai/pico-usb-wifi)

生成摘要时出错

---

## 29. Founding a company in Germany: €9600, 152 days and I still can't send an invoice

**原文标题**: Founding a company in Germany: €9600, 152 days and I still can't send an invoice

**原文链接**: [https://paolino.me/founding-a-company-in-germany/](https://paolino.me/founding-a-company-in-germany/)

生成摘要时出错

---

## 30. Ashby (YC W19) Is Hiring EMEA Engineers Who Can Design

**原文标题**: Ashby (YC W19) Is Hiring EMEA Engineers Who Can Design

**原文链接**: [https://www.ashbyhq.com/careers?ashby_jid=87b96eef-edc1-4de4-adb6-d460126d02f8&utm_source=hn](https://www.ashbyhq.com/careers?ashby_jid=87b96eef-edc1-4de4-adb6-d460126d02f8&utm_source=hn)

生成摘要时出错

---

## 31. Edsger Dijkstra's Library (Housed and Archived in Leuven, Belgium)

**原文标题**: Edsger Dijkstra's Library (Housed and Archived in Leuven, Belgium)

**原文链接**: [https://www.dijkstrascry.com/inventory](https://www.dijkstrascry.com/inventory)

生成摘要时出错

---

## 32. CAPTCHAs have failed for 20 years

**原文标题**: CAPTCHAs have failed for 20 years

**原文链接**: [https://www.browserbase.com/blog/why-captchas-are-getting-harder](https://www.browserbase.com/blog/why-captchas-are-getting-harder)

生成摘要时出错

---

## 33. Systems optimization should be part of CI/CD

**原文标题**: Systems optimization should be part of CI/CD

**原文链接**: [https://ucbskyadrs.github.io/blog/levi/](https://ucbskyadrs.github.io/blog/levi/)

生成摘要时出错

---

## 34. Statistics that live in your SQL

**原文标题**: Statistics that live in your SQL

**原文链接**: [https://kolistat.com/blog/the-stats-duck-v0-6-0/](https://kolistat.com/blog/the-stats-duck-v0-6-0/)

生成摘要时出错

---

## 35. Windage – free browser remake of Scorched Earth

**原文标题**: Windage – free browser remake of Scorched Earth

**原文链接**: [https://windage.online/](https://windage.online/)

生成摘要时出错

---

## 36. "Fix" MacBook Neo Cursor Lag: Record 1 Pixel of the Screen Every 10 Seconds

**原文标题**: "Fix" MacBook Neo Cursor Lag: Record 1 Pixel of the Screen Every 10 Seconds

**原文链接**: [https://gist.github.com/retroplasma/ec21767d0a8380c7ea9c2fbee1c7d6bf](https://gist.github.com/retroplasma/ec21767d0a8380c7ea9c2fbee1c7d6bf)

生成摘要时出错

---

## 37. François Englert (1932 – 2026)

**原文标题**: François Englert (1932 – 2026)

**原文链接**: [https://home.cern/francois-englert-1932-2026/](https://home.cern/francois-englert-1932-2026/)

生成摘要时出错

---

## 38. Qualcomm to Acquire Modular

**原文标题**: Qualcomm to Acquire Modular

**原文链接**: [https://www.modular.com/blog/qualcomm-to-acquire-modular](https://www.modular.com/blog/qualcomm-to-acquire-modular)

生成摘要时出错

---

## 39. Qwen-AgentWorld: Language World Models for General Agents

**原文标题**: Qwen-AgentWorld: Language World Models for General Agents

**原文链接**: [https://arxiv.org/abs/2606.24597](https://arxiv.org/abs/2606.24597)

生成摘要时出错

---

## 40. Exploiting vulnerabilities in Johnson and Johnson web apps

**原文标题**: Exploiting vulnerabilities in Johnson and Johnson web apps

**原文链接**: [https://eaton-works.com/2026/06/24/jnj-webapp-hacks/](https://eaton-works.com/2026/06/24/jnj-webapp-hacks/)

生成摘要时出错

---

## 41. Minimus container images are now free

**原文标题**: Minimus container images are now free

**原文链接**: [https://images.minimus.io/](https://images.minimus.io/)

生成摘要时出错

---

## 42. Rhombus Language 1.0

**原文标题**: Rhombus Language 1.0

**原文链接**: [https://blog.racket-lang.org/2026/06/rhombus-v1.0.html](https://blog.racket-lang.org/2026/06/rhombus-v1.0.html)

生成摘要时出错

---

## 43. Quebec town recognizes trees as living beings with rights

**原文标题**: Quebec town recognizes trees as living beings with rights

**原文链接**: [https://www.cbc.ca/news/canada/montreal/terrasse-vaudreil-quebec-tree-rights-9.7243634](https://www.cbc.ca/news/canada/montreal/terrasse-vaudreil-quebec-tree-rights-9.7243634)

生成摘要时出错

---

## 44. Nvidia's 45°C cooling design cuts data center water use to near zero

**原文标题**: Nvidia's 45°C cooling design cuts data center water use to near zero

**原文链接**: [https://blogs.nvidia.com/blog/liquid-cooling-ai-factories/](https://blogs.nvidia.com/blog/liquid-cooling-ai-factories/)

生成摘要时出错

---

## 45. Reducing tick density along recreational trails in Ottawa, Canada

**原文标题**: Reducing tick density along recreational trails in Ottawa, Canada

**原文链接**: [https://www.sciencedirect.com/science/article/pii/S1877959X26000476](https://www.sciencedirect.com/science/article/pii/S1877959X26000476)

生成摘要时出错

---

## 46. Why big AI labs are hiring so many philosophers

**原文标题**: Why big AI labs are hiring so many philosophers

**原文链接**: [https://www.economist.com/science-and-technology/2026/06/24/why-big-ai-labs-are-hiring-so-many-philosophers](https://www.economist.com/science-and-technology/2026/06/24/why-big-ai-labs-are-hiring-so-many-philosophers)

生成摘要时出错

---

## 47. Home Broadband Is 5G's Surprise Killer App

**原文标题**: Home Broadband Is 5G's Surprise Killer App

**原文链接**: [https://spectrum.ieee.org/fixed-wireless-access](https://spectrum.ieee.org/fixed-wireless-access)

生成摘要时出错

---

## 48. Announcing Mozilla.org, a New 501(C)(3) Nonprofit

**原文标题**: Announcing Mozilla.org, a New 501(C)(3) Nonprofit

**原文链接**: [https://blog.mozilla.org/en/mozilla/news/announcing-mozilla-org-new-non-profit/](https://blog.mozilla.org/en/mozilla/news/announcing-mozilla-org-new-non-profit/)

生成摘要时出错

---

## 49. Millimeter wave technology drills 100 meters into granite

**原文标题**: Millimeter wave technology drills 100 meters into granite

**原文链接**: [https://www.thinkgeoenergy.com/quaise-energy-achieves-100-meters-of-drilling-using-millimeter-wave-technology/](https://www.thinkgeoenergy.com/quaise-energy-achieves-100-meters-of-drilling-using-millimeter-wave-technology/)

生成摘要时出错

---

## 50. Usbliter8: an A12/A13 SecureROM Exploit

**原文标题**: Usbliter8: an A12/A13 SecureROM Exploit

**原文链接**: [https://ps.tc/pages/blog-usbliter8.html](https://ps.tc/pages/blog-usbliter8.html)

生成摘要时出错

---

## 51. Medical diagnosis AIs can be tricked into telling whose data trained them

**原文标题**: Medical diagnosis AIs can be tricked into telling whose data trained them

**原文链接**: [https://www.theregister.com/ai-and-ml/2026/06/24/medical-diagnosis-ais-can-be-tricked-into-telling-whose-data-trained-them/5261501](https://www.theregister.com/ai-and-ml/2026/06/24/medical-diagnosis-ais-can-be-tricked-into-telling-whose-data-trained-them/5261501)

生成摘要时出错

---

## 52. In memory of the man who put red and green squiggles under words

**原文标题**: In memory of the man who put red and green squiggles under words

**原文链接**: [https://devblogs.microsoft.com/oldnewthing/20260622-00/?p=112451](https://devblogs.microsoft.com/oldnewthing/20260622-00/?p=112451)

生成摘要时出错

---

## 53. Remaking BBC test cards to teach you video processing

**原文标题**: Remaking BBC test cards to teach you video processing

**原文链接**: [https://www.youtube.com/watch?v=U_6HxPkrgcg](https://www.youtube.com/watch?v=U_6HxPkrgcg)

生成摘要时出错

---

## 54. Dirty Little Zine – a tool for making an 8 page printable Zine

**原文标题**: Dirty Little Zine – a tool for making an 8 page printable Zine

**原文链接**: [https://dirtylittlezine.com/](https://dirtylittlezine.com/)

生成摘要时出错

---

## 55. Vulnerability reports are not special anymore

**原文标题**: Vulnerability reports are not special anymore

**原文链接**: [https://words.filippo.io/vuln-reports/](https://words.filippo.io/vuln-reports/)

生成摘要时出错

---

## 56. Jerry's Map

**原文标题**: Jerry's Map

**原文链接**: [http://www.jerrysmap.com/the-map](http://www.jerrysmap.com/the-map)

生成摘要时出错

---

## 57. Ex-Meta CTO Says It's a Great Time to Build a Hard Tech Company

**原文标题**: Ex-Meta CTO Says It's a Great Time to Build a Hard Tech Company

**原文链接**: [https://news.crunchbase.com/venture/hard-tech-infrastructure-moat-schroepfer-gigascale/](https://news.crunchbase.com/venture/hard-tech-infrastructure-moat-schroepfer-gigascale/)

生成摘要时出错

---

## 58. A man was gifted his dream car by Kevin Mitnick, who he helped put in prison

**原文标题**: A man was gifted his dream car by Kevin Mitnick, who he helped put in prison

**原文链接**: [https://www.thedrive.com/news/this-man-was-gifted-his-dream-car-by-the-notorious-hacker-he-put-in-prison](https://www.thedrive.com/news/this-man-was-gifted-his-dream-car-by-the-notorious-hacker-he-put-in-prison)

生成摘要时出错

---

## 59. FUTO Swipe – A new swipe typing model

**原文标题**: FUTO Swipe – A new swipe typing model

**原文链接**: [https://swipe.futo.tech/](https://swipe.futo.tech/)

生成摘要时出错

---

## 60. Retracted: Paper claiming immunochemotherapy more effective in morning

**原文标题**: Retracted: Paper claiming immunochemotherapy more effective in morning

**原文链接**: [https://www.nature.com/articles/s41591-026-04508-1](https://www.nature.com/articles/s41591-026-04508-1)

生成摘要时出错

---

## 61. Vector Graphics in Lil

**原文标题**: Vector Graphics in Lil

**原文链接**: [http://beyondloom.com/blog/vectorgraphics.html](http://beyondloom.com/blog/vectorgraphics.html)

生成摘要时出错

---

## 62. Qualcomm to Acquire Modular

**原文标题**: Qualcomm to Acquire Modular

**原文链接**: [https://investor.qualcomm.com/news-events/press-releases/news-details/2026/Qualcomm-to-Acquire-Modular/default.aspx](https://investor.qualcomm.com/news-events/press-releases/news-details/2026/Qualcomm-to-Acquire-Modular/default.aspx)

生成摘要时出错

---

## 63. Is AI 'one big bubble'? Behind the tech sell-off

**原文标题**: Is AI 'one big bubble'? Behind the tech sell-off

**原文链接**: [https://www.npr.org/2026/06/23/nx-s1-5867633/ai-selloff-tech-stocks-bubble-nasdaq](https://www.npr.org/2026/06/23/nx-s1-5867633/ai-selloff-tech-stocks-bubble-nasdaq)

生成摘要时出错

---

## 64. Fired by Google for creating the Google workspace CLI

**原文标题**: Fired by Google for creating the Google workspace CLI

**原文链接**: [https://twitter.com/JPoehnelt/status/2069482265953087602](https://twitter.com/JPoehnelt/status/2069482265953087602)

生成摘要时出错

---

## 65. F* file system – file search that reads SSD directly bypassing OS kernel

**原文标题**: F* file system – file search that reads SSD directly bypassing OS kernel

**原文链接**: [https://github.com/dmtrKovalenko/ffs](https://github.com/dmtrKovalenko/ffs)

生成摘要时出错

---

## 66. The Teensy Executable Revisited

**原文标题**: The Teensy Executable Revisited

**原文链接**: [https://www.muppetlabs.com/~breadbox/software/tiny/revisit.html](https://www.muppetlabs.com/~breadbox/software/tiny/revisit.html)

生成摘要时出错

---

## 67. Cointegration and Long-Horizon Forecasting (2025)

**原文标题**: Cointegration and Long-Horizon Forecasting (2025)

**原文链接**: [https://www.philadelphiafed.org/the-economy/cointegration-and-long-horizon-forecasting](https://www.philadelphiafed.org/the-economy/cointegration-and-long-horizon-forecasting)

生成摘要时出错

---

## 68. Steam Machine launches today

**原文标题**: Steam Machine launches today

**原文链接**: [https://store.steampowered.com/news/group/45479024/view/685257114654870245](https://store.steampowered.com/news/group/45479024/view/685257114654870245)

生成摘要时出错

---

## 69. Samsung demonstrates 3D stacked FETs with triple nanosheet channels at 42nm

**原文标题**: Samsung demonstrates 3D stacked FETs with triple nanosheet channels at 42nm

**原文链接**: [https://semiconductor.samsung.com/news-events/tech-blog/from-gaa-to-3d-stacked-fet-expanding-the-transistor-into-the-third-dimension/](https://semiconductor.samsung.com/news-events/tech-blog/from-gaa-to-3d-stacked-fet-expanding-the-transistor-into-the-third-dimension/)

生成摘要时出错

---

## 70. Show HN: An ASCII 3D Rendering Engine

**原文标题**: Show HN: An ASCII 3D Rendering Engine

**原文链接**: [https://glyphcss.com](https://glyphcss.com)

生成摘要时出错

---

## 71. The deadly rise of giant trucks and SUVs

**原文标题**: The deadly rise of giant trucks and SUVs

**原文链接**: [https://www.nytimes.com/interactive/2026/06/21/us/trucks-suv-pedestrian-crashes.html](https://www.nytimes.com/interactive/2026/06/21/us/trucks-suv-pedestrian-crashes.html)

生成摘要时出错

---

## 72. A deadly fungus that can infect cats and people is spreading

**原文标题**: A deadly fungus that can infect cats and people is spreading

**原文链接**: [https://www.sciencenews.org/article/deadly-fungus-cats-people-spreading](https://www.sciencenews.org/article/deadly-fungus-cats-people-spreading)

生成摘要时出错

---

## 73. Finding the best dog treat with statistics

**原文标题**: Finding the best dog treat with statistics

**原文链接**: [https://www.wespiser.com/posts/2026-06-19-best-dog-treat.html](https://www.wespiser.com/posts/2026-06-19-best-dog-treat.html)

生成摘要时出错

---

## 74. Signs you're a dangerous terrorist: using Signal, moving zines

**原文标题**: Signs you're a dangerous terrorist: using Signal, moving zines

**原文链接**: [https://werd.io/signs-youre-a-dangerous-terrorist-using-signal-moving-zines/](https://werd.io/signs-youre-a-dangerous-terrorist-using-signal-moving-zines/)

生成摘要时出错

---

## 75. Printing Gaussian Splats

**原文标题**: Printing Gaussian Splats

**原文链接**: [https://www.patreon.com/DanyBittel/posts/printing-splats-161333338](https://www.patreon.com/DanyBittel/posts/printing-splats-161333338)

生成摘要时出错

---

## 76. The Coming Loop

**原文标题**: The Coming Loop

**原文链接**: [https://lucumr.pocoo.org/2026/6/23/the-coming-loop/](https://lucumr.pocoo.org/2026/6/23/the-coming-loop/)

生成摘要时出错

---

## 77. Inventing the Future, One Lisp Machine at a Time

**原文标题**: Inventing the Future, One Lisp Machine at a Time

**原文链接**: [https://www.patrickdomanico.com/bpm/2026/06/16/inventing-the-future-one-lisp-machine-at-a-time/](https://www.patrickdomanico.com/bpm/2026/06/16/inventing-the-future-one-lisp-machine-at-a-time/)

生成摘要时出错

---

## 78. Reid Hoffman says SpaceX 'not an AI company', xAI 'complete train wreck'

**原文标题**: Reid Hoffman says SpaceX 'not an AI company', xAI 'complete train wreck'

**原文链接**: [https://fortune.com/2026/06/24/reid-hoffman-spacex-musk-openai-anthropic-gen-z-mistake/](https://fortune.com/2026/06/24/reid-hoffman-spacex-musk-openai-anthropic-gen-z-mistake/)

生成摘要时出错

---

## 79. Apple is going to raise device prices, but when?

**原文标题**: Apple is going to raise device prices, but when?

**原文链接**: [https://daringfireball.net/linked/2026/06/22/apple-device-prices-when](https://daringfireball.net/linked/2026/06/22/apple-device-prices-when)

生成摘要时出错

---

## 80. QSOE: QNX-inspired OS with dual-kernel architecture

**原文标题**: QSOE: QNX-inspired OS with dual-kernel architecture

**原文链接**: [https://qsoe-dev.blogspot.com/2026/06/qsoe-project-v01-is-released.html](https://qsoe-dev.blogspot.com/2026/06/qsoe-project-v01-is-released.html)

生成摘要时出错

---

## 81. Swift Package Index joins Apple

**原文标题**: Swift Package Index joins Apple

**原文链接**: [https://swiftpackageindex.com/blog/swift-package-index-joins-apple](https://swiftpackageindex.com/blog/swift-package-index-joins-apple)

生成摘要时出错

---

## 82. White House app auto-downloads to government phones, can't be uninstalled

**原文标题**: White House app auto-downloads to government phones, can't be uninstalled

**原文链接**: [https://www.wired.com/story/story/government-workers-cant-get-the-white-houses-app-off-their-phones/](https://www.wired.com/story/story/government-workers-cant-get-the-white-houses-app-off-their-phones/)

生成摘要时出错

---

## 83. Lift4D: Harmonizing Single-View 3D Estimation for 4D Reconstruction In-the-Wild

**原文标题**: Lift4D: Harmonizing Single-View 3D Estimation for 4D Reconstruction In-the-Wild

**原文链接**: [https://lift4d.github.io/](https://lift4d.github.io/)

生成摘要时出错

---

## 84. The worthlessness of Vitamin D is mildly exaggerated

**原文标题**: The worthlessness of Vitamin D is mildly exaggerated

**原文链接**: [https://dynomight.net/vitamin-d/](https://dynomight.net/vitamin-d/)

生成摘要时出错

---

## 85. Show HN: TikZ Editor – WYSIWYG editor for figures in LaTeX

**原文标题**: Show HN: TikZ Editor – WYSIWYG editor for figures in LaTeX

**原文链接**: [https://tikz.dev/editor/](https://tikz.dev/editor/)

生成摘要时出错

---

## 86. Qualcomm Is Acquiring Modular

**原文标题**: Qualcomm Is Acquiring Modular

**原文链接**: [https://twitter.com/clattner_llvm/status/2069769232477192354](https://twitter.com/clattner_llvm/status/2069769232477192354)

生成摘要时出错

---

## 87. Flock CEO: "They're Gonna Enforce Immigration No Matter What Flock Does"

**原文标题**: Flock CEO: "They're Gonna Enforce Immigration No Matter What Flock Does"

**原文链接**: [https://ipvm.com/reports/flock-ceo-immigration](https://ipvm.com/reports/flock-ceo-immigration)

生成摘要时出错

---

## 88. Lithp.py (~2008)

**原文标题**: Lithp.py (~2008)

**原文链接**: [https://fogus.me/fun/lithp/](https://fogus.me/fun/lithp/)

生成摘要时出错

---

## 89. AI's Affordability Crisis

**原文标题**: AI's Affordability Crisis

**原文链接**: [https://blog.dshr.org/2026/06/ais-affordability-crisis.html](https://blog.dshr.org/2026/06/ais-affordability-crisis.html)

生成摘要时出错

---

## 90. Show HN: Graphical SQL Builder and Debugger

**原文标题**: Show HN: Graphical SQL Builder and Debugger

**原文链接**: [https://github.com/webofmarius/SQLJoiner](https://github.com/webofmarius/SQLJoiner)

生成摘要时出错

---

## 91. DiffusionBench: Towards Holistic Evaluation of Generative Diffusion Transformers

**原文标题**: DiffusionBench: Towards Holistic Evaluation of Generative Diffusion Transformers

**原文链接**: [https://github.com/End2End-Diffusion/diffusion-bench](https://github.com/End2End-Diffusion/diffusion-bench)

生成摘要时出错

---

## 92. Meta Pauses Employee-Tracking Program Following Internal Data Leak

**原文标题**: Meta Pauses Employee-Tracking Program Following Internal Data Leak

**原文链接**: [https://www.wired.com/story/meta-pauses-employee-tracking-program-following-internal-security-breach/](https://www.wired.com/story/meta-pauses-employee-tracking-program-following-internal-security-breach/)

生成摘要时出错

---

## 93. Giant Banana Pulled Over: Driver Says Cops Have Stopped Him 100s of Times

**原文标题**: Giant Banana Pulled Over: Driver Says Cops Have Stopped Him 100s of Times

**原文链接**: [https://cowboystatedaily.com/2026/06/18/giant-banana-pulled-over-in-montana-driver-says-cops-have-stopped-him-100s-of-times/](https://cowboystatedaily.com/2026/06/18/giant-banana-pulled-over-in-montana-driver-says-cops-have-stopped-him-100s-of-times/)

生成摘要时出错

---

## 94. Unlimited OCR: One-shot long-horizon parsing

**原文标题**: Unlimited OCR: One-shot long-horizon parsing

**原文链接**: [https://github.com/baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR)

生成摘要时出错

---

## 95. Deep dive into iroh: Replacement for WireGuard or P2P layer for your application

**原文标题**: Deep dive into iroh: Replacement for WireGuard or P2P layer for your application

**原文链接**: [https://kerkour.com/iroh-v1-p2p](https://kerkour.com/iroh-v1-p2p)

生成摘要时出错

---

## 96. Algorithmic Monocultures in Hiring

**原文标题**: Algorithmic Monocultures in Hiring

**原文链接**: [https://hai.stanford.edu/news/ai-hiring-tools-can-yield-racial-bias-and-systemic-rejection](https://hai.stanford.edu/news/ai-hiring-tools-can-yield-racial-bias-and-systemic-rejection)

生成摘要时出错

---

## 97. Mistral OCR 4

**原文标题**: Mistral OCR 4

**原文链接**: [https://mistral.ai/news/ocr-4/](https://mistral.ai/news/ocr-4/)

生成摘要时出错

---

## 98. Slate Auto's electric truck starts at $24,950 with 205 miles of range

**原文标题**: Slate Auto's electric truck starts at $24,950 with 205 miles of range

**原文链接**: [https://electrek.co/2026/06/24/slate-electric-truck-24950-price/](https://electrek.co/2026/06/24/slate-electric-truck-24950-price/)

生成摘要时出错

---

## 99. Orion 1.1 for macOS is out, with containers

**原文标题**: Orion 1.1 for macOS is out, with containers

**原文链接**: [https://orionbrowser.com/updates/versions/1.1](https://orionbrowser.com/updates/versions/1.1)

生成摘要时出错

---

## 100. San Diego photologs from the 1970s

**原文标题**: San Diego photologs from the 1970s

**原文链接**: [https://www.beautifulpublicdata.com/san-diego-photologs-from-the-1970s/](https://www.beautifulpublicdata.com/san-diego-photologs-from-the-1970s/)

生成摘要时出错

---

