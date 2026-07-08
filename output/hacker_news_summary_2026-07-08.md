# Hacker News 热门文章摘要 (2026-07-08)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Chatto 现已开源

**原文标题**: Chatto is now Open Source

**原文链接**: [https://www.hmans.dev/blog/chatto-is-open-source](https://www.hmans.dev/blog/chatto-is-open-source)

在名为《Chatto 现已开源》的博文中，开发者 Hendrik Mans 宣布他的聊天应用项目 Chatto 已从潜在的商业产品转型为采用 MIT 许可证的开源项目。

Mans 最初将 Chatto 开发为 Discord 和 Slack 等平台的现代、轻量级替代方案。在意识到自己不再希望将其作为商业 SaaS 业务运营后，他决定公开代码，以确保其对社区的效用，并允许他人托管自己的私人通信中心。

**Chatto 的主要特性和细节包括：**

*   **用途：** 专为小型社区、朋友圈和家庭设计，旨在提供私密、无干扰的对话环境。
*   **核心功能：** 该平台支持有序频道、私信、富文本/Markdown 支持、文件上传（通过 AWS S3）以及表情符号回应。
*   **技术栈：** 该应用基于 **React**、**TypeScript** 和 **Tailwind CSS** 构建。它利用 **Pusher** 实现实时消息传递，并拥有简洁的响应式界面。
*   **自托管：** 通过开源该项目，Mans 使用户能够自托管该应用，从而完全掌控自己的数据和基础设施。

这一举措标志着从利润驱动模式向社区导向模式的转变。Mans 鼓励开发者在 GitHub 上探索该代码库，无论是将其作为自己项目的基石，还是仅仅为了学习其在实时 Web 技术方面的实现。

---

## 2. Mistral 的 Robostral Navigate：一款最先进的机器人导航模型

**原文标题**: Mistral's Robostral Navigate: a state of the art robotics navigation model

**原文链接**: [https://mistral.ai/news/robostral-navigate/](https://mistral.ai/news/robostral-navigate/)

Mistral AI 推出了 **Robostral Navigate**，这是一款专为自主机器人导航设计的 8B 参数模型。该模型的一大特色是仅使用**单目 RGB 摄像头**即可实现最先进的性能，无需昂贵的激光雷达 (LiDAR) 或深度传感器。

在 R2R-CE（连续环境中的房到房）基准测试中，该模型在未知环境下的**成功率达到 76.6%**。这一表现比之前的多传感器系统高出 4.5 个百分点，比最出色的单摄像头方案高出 9.7 个百分点。该模型能够理解自然语言指令，并通过“指向”（预测目标图像坐标）或在目标不可见时使用局部位移来进行导航。

**核心技术亮点：**
*   **自主研发**：该模型完全从零开始构建，而非依赖现有的开源视觉语言模型 (VLM)，重点关注物体定位等接地 (grounding) 能力。
*   **基于模拟的训练**：Mistral 在 6,000 个模拟场景中生成了 40 万条轨迹，构建了稳健的数据集。
*   **高效性**：通过使用“前缀缓存”策略，团队将训练 token 数量减少了 **22 倍**，将数月的训练时间缩短至数天。
*   **强化学习**：在监督训练之后，团队应用了名为 CISPO 的在线强化学习算法，通过让模型在试错中学习，使成功率进一步提升了 3.2%。

Robostral Navigate 与硬件无关，可适配各种尺寸的轮式、足式及飞行机器人。Mistral 将其视为迈向统一具身智能 (Embodied AI) 的基础性一步，在物流、制造和酒店服务等领域具有即时应用价值。

---

## 3. Grok 4.5

**原文标题**: Grok 4.5

**原文链接**: [https://x.ai/news/grok-4-5](https://x.ai/news/grok-4-5)

On July 8, 2026, SpaceXAI announced the launch of **Grok 4.5**, its most advanced model to date, specifically optimized for coding, agentic tasks, and professional knowledge work. Trained on NVIDIA GB300 GPUs using large-scale reinforcement learning, the model focuses on "per-token intelligence" to handle complex, multi-step engineering challenges.

**Key Highlights:**
*   **Performance:** Grok 4.5 excels in STEM and software engineering benchmarks, rivaling or exceeding models like GPT 5.5 and Opus 4.8. It notably ranks #1 on Harvey's Legal Agent Benchmark and shows high resolve rates on SWE Bench Pro.
*   **Speed and Efficiency:** The model operates at "fast-model" speeds of 80 tokens per second. SpaceXAI emphasizes its "token efficiency," claiming it can resolve tasks using roughly 4.2x fewer output tokens than competitors, significantly reducing latency and operational costs.
*   **Office Integration:** Beyond coding, Grok 4.5 is integrated into "Grok Build" for office productivity. It can generate complex Excel models with web research, design native PowerPoint diagrams, and draft professional prose in Word.
*   **Coding Prowess:** The model supports end-to-end application development—from Rust and C++ tasks to Three.js simulations—often requiring only a single prompt to reach production-ready results.

**Availability and Pricing:**
Grok 4.5 is priced competitively at **$2 per million input tokens** and **$6 per million output tokens**. It is available immediately via the SpaceXAI console, Grok Build, and the Cursor code editor. While currently available in most regions, availability in the EU is expected to follow in mid-July 2026.

---

## 4. GPT‑Live

**原文标题**: GPT‑Live

**原文链接**: [https://openai.com/index/introducing-gpt-live/](https://openai.com/index/introducing-gpt-live/)

生成摘要时出错

---

## 5. SWE-1.7 智能水平接近 GPT 5.5 与 Opus

**原文标题**: SWE-1.7 Reach Near GPT 5.5 and Opus Intelligence

**原文链接**: [https://cognition.com/blog/swe-1-7](https://cognition.com/blog/swe-1-7)

生成摘要时出错

---

## 6. Decoding the obfuscated bash script on a Uniqlo t-shirt

**原文标题**: Decoding the obfuscated bash script on a Uniqlo t-shirt

**原文链接**: [https://tris.sherliker.net/blog/obfuscated-self-evaluating-bash-script-by-cdn-akamai-being-supplied-to-consumers-via-retail-stores/](https://tris.sherliker.net/blog/obfuscated-self-evaluating-bash-script-by-cdn-akamai-being-supplied-to-consumers-via-retail-stores/)

生成摘要时出错

---

## 7. Show HN: Microsoft releases Flint, a visualization language for AI agents

**原文标题**: Show HN: Microsoft releases Flint, a visualization language for AI agents

**原文链接**: [https://microsoft.github.io/flint-chart/#/](https://microsoft.github.io/flint-chart/#/)

生成摘要时出错

---

## 8. What Do We Know About the Microplastics Inside Us?

**原文标题**: What Do We Know About the Microplastics Inside Us?

**原文链接**: [https://e360.yale.edu/features/cassandra-rauert-interview](https://e360.yale.edu/features/cassandra-rauert-interview)

生成摘要时出错

---

## 9. Cloudflare Meerkat - Globally distributed consensus

**原文标题**: Cloudflare Meerkat - Globally distributed consensus

**原文链接**: [https://blog.cloudflare.com/meerkat-introduction/](https://blog.cloudflare.com/meerkat-introduction/)

生成摘要时出错

---

## 10. EU now one step away from reviving private message scanning rules

**原文标题**: EU now one step away from reviving private message scanning rules

**原文链接**: [https://cyberinsider.com/eu-now-one-step-away-from-reviving-private-message-scanning-rules/](https://cyberinsider.com/eu-now-one-step-away-from-reviving-private-message-scanning-rules/)

生成摘要时出错

---

## 11. GitLost: We Tricked GitHub's AI Agent into Leaking Private Repos

**原文标题**: GitLost: We Tricked GitHub's AI Agent into Leaking Private Repos

**原文链接**: [https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos/](https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos/)

生成摘要时出错

---

## 12. OpenBSD has a use-after-free allowing local privilege escalation to root

**原文标题**: OpenBSD has a use-after-free allowing local privilege escalation to root

**原文链接**: [https://nvd.nist.gov/vuln/detail/cve-2026-57589](https://nvd.nist.gov/vuln/detail/cve-2026-57589)

生成摘要时出错

---

## 13. Show HN: Follow London Trains in 3D

**原文标题**: Show HN: Follow London Trains in 3D

**原文链接**: [https://ride.nexttrain.london/](https://ride.nexttrain.london/)

生成摘要时出错

---

## 14. TypeScript 7

**原文标题**: TypeScript 7

**原文链接**: [https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/)

生成摘要时出错

---

## 15. EVE Online's Carbon engine is now open source: Fenris Creations explains why

**原文标题**: EVE Online's Carbon engine is now open source: Fenris Creations explains why

**原文链接**: [https://www.gamesindustry.biz/eve-onlines-carbon-engine-is-now-open-source-fenris-creations-explains-why](https://www.gamesindustry.biz/eve-onlines-carbon-engine-is-now-open-source-fenris-creations-explains-why)

生成摘要时出错

---

## 16. TabFont – guitar tabs rendered as you type

**原文标题**: TabFont – guitar tabs rendered as you type

**原文链接**: [https://philatype.com/tabfont/](https://philatype.com/tabfont/)

生成摘要时出错

---

## 17. Apple to increase spend with Broadcom to produce billions more U.S. chips

**原文标题**: Apple to increase spend with Broadcom to produce billions more U.S. chips

**原文链接**: [https://www.apple.com/newsroom/2026/07/apple-to-increase-spend-with-broadcom-to-produce-billions-more-us-chips/](https://www.apple.com/newsroom/2026/07/apple-to-increase-spend-with-broadcom-to-produce-billions-more-us-chips/)

生成摘要时出错

---

## 18. Japan's Hayabusa2 probe to conduct flyby of Torifune asteroid

**原文标题**: Japan's Hayabusa2 probe to conduct flyby of Torifune asteroid

**原文链接**: [https://www3.nhk.or.jp/nhkworld/en/news/20260705_01/](https://www3.nhk.or.jp/nhkworld/en/news/20260705_01/)

生成摘要时出错

---

## 19. How to Build a Minimal ZFS NAS Without Synology, QNAP, TrueNAS (2024)

**原文标题**: How to Build a Minimal ZFS NAS Without Synology, QNAP, TrueNAS (2024)

**原文链接**: [https://neil.computer/notes/how-to-setup-minimal-zfs-nas-without-truenas/](https://neil.computer/notes/how-to-setup-minimal-zfs-nas-without-truenas/)

生成摘要时出错

---

## 20. NoiseLang: Where N = 5 is a Dirac delta

**原文标题**: NoiseLang: Where N = 5 is a Dirac delta

**原文链接**: [https://manualmeida.dev/articles/noiselang/](https://manualmeida.dev/articles/noiselang/)

生成摘要时出错

---

## 21. Geosql: A Claude/Codex skill for geospatial data

**原文标题**: Geosql: A Claude/Codex skill for geospatial data

**原文链接**: [https://github.com/dekart-xyz/geosql](https://github.com/dekart-xyz/geosql)

生成摘要时出错

---

## 22. Tenda firmware (multiple versions) contains hidden authentication backdoor

**原文标题**: Tenda firmware (multiple versions) contains hidden authentication backdoor

**原文链接**: [https://kb.cert.org/vuls/id/213560](https://kb.cert.org/vuls/id/213560)

生成摘要时出错

---

## 23. Chat Control 1.0 and 2.0 Explained

**原文标题**: Chat Control 1.0 and 2.0 Explained

**原文链接**: [https://fightchatcontrol.eu/chat-control-overview](https://fightchatcontrol.eu/chat-control-overview)

生成摘要时出错

---

## 24. Every postcard tells a story

**原文标题**: Every postcard tells a story

**原文链接**: [https://observer.co.uk/style/features/article/every-postcard-tells-a-story](https://observer.co.uk/style/features/article/every-postcard-tells-a-story)

生成摘要时出错

---

## 25. Catastrophe theory; geniuses and maniacs (2011)

**原文标题**: Catastrophe theory; geniuses and maniacs (2011)

**原文链接**: [http://glassbottomblog.blogspot.com/2011/01/catastrophe-theory-geniuses-and-maniacs.html](http://glassbottomblog.blogspot.com/2011/01/catastrophe-theory-geniuses-and-maniacs.html)

生成摘要时出错

---

## 26. Structure and Interpretation of Computer Programs Video Lectures (1986)

**原文标题**: Structure and Interpretation of Computer Programs Video Lectures (1986)

**原文链接**: [https://ocw.mit.edu/courses/6-001-structure-and-interpretation-of-computer-programs-spring-2005/video_galleries/video-lectures/](https://ocw.mit.edu/courses/6-001-structure-and-interpretation-of-computer-programs-spring-2005/video_galleries/video-lectures/)

生成摘要时出错

---

## 27. Copy That Floppy – Cambridge guide for preserving data from fragile floppy disks

**原文标题**: Copy That Floppy – Cambridge guide for preserving data from fragile floppy disks

**原文链接**: [https://www.digipres.org/the-floppy-guide/](https://www.digipres.org/the-floppy-guide/)

生成摘要时出错

---

## 28. Ants: Who looks after the injured in a colony?

**原文标题**: Ants: Who looks after the injured in a colony?

**原文链接**: [https://www.uni-wuerzburg.de/en/news-and-events/news/detail/news/ameisen-kolonie-verletzte-pflegt/](https://www.uni-wuerzburg.de/en/news-and-events/news/detail/news/ameisen-kolonie-verletzte-pflegt/)

生成摘要时出错

---

## 29. GAO: DOE Is Prematurely Excluding Less Expensive Options for Nuclear Cleanup

**原文标题**: GAO: DOE Is Prematurely Excluding Less Expensive Options for Nuclear Cleanup

**原文链接**: [https://www.gao.gov/products/gao-26-108193](https://www.gao.gov/products/gao-26-108193)

生成摘要时出错

---

## 30. PlayStation can delete all your digital games after 3 years of inactivity (EU)

**原文标题**: PlayStation can delete all your digital games after 3 years of inactivity (EU)

**原文链接**: [https://www.flatpanelshd.com/news.php?subaction=showfull&id=1783340582](https://www.flatpanelshd.com/news.php?subaction=showfull&id=1783340582)

生成摘要时出错

---

## 31. Canada's only watchmaking school still ticking after 80 years

**原文标题**: Canada's only watchmaking school still ticking after 80 years

**原文链接**: [https://www.cbc.ca/news/canada/montreal/canada-s-only-watchmaking-school-9.7254211](https://www.cbc.ca/news/canada/montreal/canada-s-only-watchmaking-school-9.7254211)

生成摘要时出错

---

## 32. Local, CPU-Friendly, High-Quality TTS (Text-to-Speech) with Kokoro

**原文标题**: Local, CPU-Friendly, High-Quality TTS (Text-to-Speech) with Kokoro

**原文链接**: [https://ariya.io/2026/03/local-cpu-friendly-high-quality-tts-text-to-speech-with-kokoro/](https://ariya.io/2026/03/local-cpu-friendly-high-quality-tts-text-to-speech-with-kokoro/)

生成摘要时出错

---

## 33. Home made GPU escalated quickly [video]

**原文标题**: Home made GPU escalated quickly [video]

**原文链接**: [https://www.youtube.com/watch?v=qMR3IXF2sWw](https://www.youtube.com/watch?v=qMR3IXF2sWw)

生成摘要时出错

---

## 34. The difference between "today's task" and "accretive work"

**原文标题**: The difference between "today's task" and "accretive work"

**原文链接**: [https://pluralistic.net/2026/07/02/canonization/](https://pluralistic.net/2026/07/02/canonization/)

生成摘要时出错

---

## 35. Show HN: Kastor – Terraform-style specs for AI agents

**原文标题**: Show HN: Kastor – Terraform-style specs for AI agents

**原文链接**: [https://github.com/weirdGuy/kastor](https://github.com/weirdGuy/kastor)

生成摘要时出错

---

## 36. It seems that the age of reading might be a short anomaly in human history

**原文标题**: It seems that the age of reading might be a short anomaly in human history

**原文链接**: [https://www.theatlantic.com/magazine/2026/08/reading-crisis-postliterate-age/687618/](https://www.theatlantic.com/magazine/2026/08/reading-crisis-postliterate-age/687618/)

生成摘要时出错

---

## 37. Herdr: One terminal to rule them all

**原文标题**: Herdr: One terminal to rule them all

**原文链接**: [https://herdr.dev/](https://herdr.dev/)

生成摘要时出错

---

## 38. LineageOS Statistics

**原文标题**: LineageOS Statistics

**原文链接**: [https://stats.lineageos.org](https://stats.lineageos.org)

生成摘要时出错

---

## 39. Show HN: Davit, a Apple Containers UI

**原文标题**: Show HN: Davit, a Apple Containers UI

**原文链接**: [https://davit.app](https://davit.app)

生成摘要时出错

---

## 40. Automate Excel with Python: From manual grind to one-click workflow

**原文标题**: Automate Excel with Python: From manual grind to one-click workflow

**原文链接**: [https://nostarch.com/automate-excel-with-python](https://nostarch.com/automate-excel-with-python)

生成摘要时出错

---

## 41. Show HN: Rowboat – Open-source, local-first alternative to Claude Desktop

**原文标题**: Show HN: Rowboat – Open-source, local-first alternative to Claude Desktop

**原文链接**: [https://github.com/rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat)

生成摘要时出错

---

## 42. Meta's glasses will turn off the camera if you tamper with the privacy light

**原文标题**: Meta's glasses will turn off the camera if you tamper with the privacy light

**原文链接**: [https://www.theverge.com/gadgets/962514/meta-privacy-light-tampering-smart-glasses-update](https://www.theverge.com/gadgets/962514/meta-privacy-light-tampering-smart-glasses-update)

生成摘要时出错

---

## 43. Show HN: Neil the Seal Game

**原文标题**: Show HN: Neil the Seal Game

**原文链接**: [https://neiltheseal.app/](https://neiltheseal.app/)

生成摘要时出错

---

## 44. Why we built yet another Postgres connection pooler

**原文标题**: Why we built yet another Postgres connection pooler

**原文链接**: [https://pgdog.dev/blog/why-yet-another-connection-pooler](https://pgdog.dev/blog/why-yet-another-connection-pooler)

生成摘要时出错

---

## 45. IEEE Rolls Out Large Language Models Training Course

**原文标题**: IEEE Rolls Out Large Language Models Training Course

**原文链接**: [https://spectrum.ieee.org/large-language-models-ieee-course](https://spectrum.ieee.org/large-language-models-ieee-course)

生成摘要时出错

---

## 46. Dangling Pointer

**原文标题**: Dangling Pointer

**原文链接**: [https://en.wikipedia.org/wiki/Dangling_pointer](https://en.wikipedia.org/wiki/Dangling_pointer)

生成摘要时出错

---

## 47. 9 Mothers (YC P26) Is Hiring in Austin, TX

**原文标题**: 9 Mothers (YC P26) Is Hiring in Austin, TX

**原文链接**: [https://9mothers.com/careers](https://9mothers.com/careers)

生成摘要时出错

---

## 48. Firefox new Wrexham shirt sponsor

**原文标题**: Firefox new Wrexham shirt sponsor

**原文链接**: [https://www.nytimes.com/athletic/7427454/2026/07/08/wrexham-firefox-shirt-sponsor/](https://www.nytimes.com/athletic/7427454/2026/07/08/wrexham-firefox-shirt-sponsor/)

生成摘要时出错

---

## 49. l: A new runtime for k and q

**原文标题**: l: A new runtime for k and q

**原文链接**: [https://lv1.sh/](https://lv1.sh/)

生成摘要时出错

---

## 50. Jim's TrueType QR Code Font

**原文标题**: Jim's TrueType QR Code Font

**原文链接**: [https://github.com/jimparis/qr-font](https://github.com/jimparis/qr-font)

生成摘要时出错

---

## 51. StreetComplete: Fixing OpenStreetMap, one tiny quest at a time

**原文标题**: StreetComplete: Fixing OpenStreetMap, one tiny quest at a time

**原文链接**: [https://streetcomplete.app/](https://streetcomplete.app/)

生成摘要时出错

---

## 52. Grok 4.5

**原文标题**: Grok 4.5

**原文链接**: [https://cursor.com/blog/grok-4-5](https://cursor.com/blog/grok-4-5)

生成摘要时出错

---

## 53. Windows Drops Under 60% in Global Desktop OS Share for the First Time in Years

**原文标题**: Windows Drops Under 60% in Global Desktop OS Share for the First Time in Years

**原文链接**: [https://linuxiac.com/windows-drops-under-60-in-global-desktop-os-share-for-the-first-time-in-years/](https://linuxiac.com/windows-drops-under-60-in-global-desktop-os-share-for-the-first-time-in-years/)

生成摘要时出错

---

## 54. Notes on Software Quality

**原文标题**: Notes on Software Quality

**原文链接**: [https://anthonyhobday.com/blog/20260410](https://anthonyhobday.com/blog/20260410)

生成摘要时出错

---

## 55. Every new car sold in the European Union must include a driver monitoring camera

**原文标题**: Every new car sold in the European Union must include a driver monitoring camera

**原文链接**: [https://allaboutcookies.org/eu-mandatory-distracted-driver-system](https://allaboutcookies.org/eu-mandatory-distracted-driver-system)

生成摘要时出错

---

## 56. Scheme Is a Hoot

**原文标题**: Scheme Is a Hoot

**原文链接**: [https://gracefulliberty.com/notes/scheme-is-a-hoot/](https://gracefulliberty.com/notes/scheme-is-a-hoot/)

生成摘要时出错

---

## 57. Show HN: Chiptune Radio

**原文标题**: Show HN: Chiptune Radio

**原文链接**: [https://chiptune-radio.alephvoid.com/](https://chiptune-radio.alephvoid.com/)

生成摘要时出错

---

## 58. 30papers.com – Ilya's 30 essential ML papers, in a beginner friendly format

**原文标题**: 30papers.com – Ilya's 30 essential ML papers, in a beginner friendly format

**原文链接**: [https://30papers.com/](https://30papers.com/)

生成摘要时出错

---

## 59. How did Windows 95 decide that a setup program ran?

**原文标题**: How did Windows 95 decide that a setup program ran?

**原文链接**: [https://devblogs.microsoft.com/oldnewthing/20260707-00/?p=112508](https://devblogs.microsoft.com/oldnewthing/20260707-00/?p=112508)

生成摘要时出错

---

## 60. How did Windows 95 decide that a setup program ran?

**原文标题**: How did Windows 95 decide that a setup program ran?

**原文链接**: [https://devblogs.microsoft.com/oldnewthing/20260707-00/?p=112508](https://devblogs.microsoft.com/oldnewthing/20260707-00/?p=112508)

生成摘要时出错

---

## 61. Fixing analog audio on the $2.58 HDMI-to-VGA adapter

**原文标题**: Fixing analog audio on the $2.58 HDMI-to-VGA adapter

**原文链接**: [https://nyanpasu64.gitlab.io/blog/hdmi-vga-dac-audio/](https://nyanpasu64.gitlab.io/blog/hdmi-vga-dac-audio/)

生成摘要时出错

---

## 62. FDA rejects petition to set PFAS limits in food

**原文标题**: FDA rejects petition to set PFAS limits in food

**原文链接**: [https://www.theguardian.com/us-news/2026/jul/08/us-food-and-drug-administration-rejects-petition-to-set-pfas-limits-in-food](https://www.theguardian.com/us-news/2026/jul/08/us-food-and-drug-administration-rejects-petition-to-set-pfas-limits-in-food)

生成摘要时出错

---

## 63. The Second Derivative: Why No One Understands the AI Boom

**原文标题**: The Second Derivative: Why No One Understands the AI Boom

**原文链接**: [https://www.groundbrkr.com/p/the-second-derivative-why-no-one](https://www.groundbrkr.com/p/the-second-derivative-why-no-one)

生成摘要时出错

---

## 64. AI Meets Cryptography 1: What AI Found in Cloudflare's Circl

**原文标题**: AI Meets Cryptography 1: What AI Found in Cloudflare's Circl

**原文链接**: [https://blog.zksecurity.xyz/posts/circl-bugs/](https://blog.zksecurity.xyz/posts/circl-bugs/)

生成摘要时出错

---

## 65. Automating AI Away

**原文标题**: Automating AI Away

**原文链接**: [https://replicated.live/blog/away](https://replicated.live/blog/away)

生成摘要时出错

---

## 66. In San Francisco, Some Home Sellers Now Ask for OpenAI or Anthropic Stock

**原文标题**: In San Francisco, Some Home Sellers Now Ask for OpenAI or Anthropic Stock

**原文链接**: [https://www.nytimes.com/2026/07/08/technology/san-francisco-home-sales-openai-anthropic-ipo.html](https://www.nytimes.com/2026/07/08/technology/san-francisco-home-sales-openai-anthropic-ipo.html)

生成摘要时出错

---

## 67. Show HN: Pug.sh – open-source product analytics

**原文标题**: Show HN: Pug.sh – open-source product analytics

**原文链接**: [https://pug.sh/](https://pug.sh/)

生成摘要时出错

---

## 68. A better way to tie gym shorts (or any drawstring) [video]

**原文标题**: A better way to tie gym shorts (or any drawstring) [video]

**原文链接**: [https://www.youtube.com/watch?v=3R0Lp86GEBk](https://www.youtube.com/watch?v=3R0Lp86GEBk)

生成摘要时出错

---

## 69. Microsoft fire idTech team at Id software

**原文标题**: Microsoft fire idTech team at Id software

**原文链接**: [https://gamefromscratch.com/microsoft-fire-idtech-team-at-id-software/](https://gamefromscratch.com/microsoft-fire-idtech-team-at-id-software/)

生成摘要时出错

---

## 70. Amazon aims to raise $25B from bond sale

**原文标题**: Amazon aims to raise $25B from bond sale

**原文链接**: [https://www.reuters.com/legal/transactional/amazon-aims-raise-25-billion-bond-sale-bloomberg-news-reports-2026-07-07/](https://www.reuters.com/legal/transactional/amazon-aims-raise-25-billion-bond-sale-bloomberg-news-reports-2026-07-07/)

生成摘要时出错

---

## 71. The Art of Computer Programming by Donald E. Knuth

**原文标题**: The Art of Computer Programming by Donald E. Knuth

**原文链接**: [https://www-cs-faculty.stanford.edu/~knuth/taocp.html](https://www-cs-faculty.stanford.edu/~knuth/taocp.html)

生成摘要时出错

---

## 72. Camera with transparent display launches for the equivalent of $29

**原文标题**: Camera with transparent display launches for the equivalent of $29

**原文链接**: [https://www.notebookcheck.net/Camera-with-transparent-display-launches-for-the-equivalent-of-29.1334495.0.html](https://www.notebookcheck.net/Camera-with-transparent-display-launches-for-the-equivalent-of-29.1334495.0.html)

生成摘要时出错

---

## 73. 98% isn't much

**原文标题**: 98% isn't much

**原文链接**: [https://whynothugo.nl/journal/2026/07/03/98-isnt-very-much/](https://whynothugo.nl/journal/2026/07/03/98-isnt-very-much/)

生成摘要时出错

---

## 74. A brewing battle: More IT workers want unions. The industry doesn't

**原文标题**: A brewing battle: More IT workers want unions. The industry doesn't

**原文链接**: [https://www.computerworld.com/article/4191760/brewing-battle-more-tech-workers-want-unions-but-the-industry-doesnt.html](https://www.computerworld.com/article/4191760/brewing-battle-more-tech-workers-want-unions-but-the-industry-doesnt.html)

生成摘要时出错

---

## 75. Chat Control passed first round in EU Parliament

**原文标题**: Chat Control passed first round in EU Parliament

**原文链接**: [https://www.heise.de/en/news/Showdown-in-Strasbourg-The-unexpected-return-of-Chat-Control-1-0-11356680.html](https://www.heise.de/en/news/Showdown-in-Strasbourg-The-unexpected-return-of-Chat-Control-1-0-11356680.html)

生成摘要时出错

---

## 76. MacSurf 1.68 – NetSurf on OS 9 Released

**原文标题**: MacSurf 1.68 – NetSurf on OS 9 Released

**原文链接**: [https://github.com/mplsllc/macsurf/releases/tag/v1.86](https://github.com/mplsllc/macsurf/releases/tag/v1.86)

生成摘要时出错

---

## 77. An interactive explorer for Benford's Law across real datasets

**原文标题**: An interactive explorer for Benford's Law across real datasets

**原文链接**: [https://vatsalbakshi.com/blog/benfords-law/](https://vatsalbakshi.com/blog/benfords-law/)

生成摘要时出错

---

## 78. We're extending access to Fable 5 on all paid plans through July 12

**原文标题**: We're extending access to Fable 5 on all paid plans through July 12

**原文链接**: [https://twitter.com/claudeai/status/2074548242386178258](https://twitter.com/claudeai/status/2074548242386178258)

生成摘要时出错

---

## 79. Show HN: Free Mermaid Diagram Editor

**原文标题**: Show HN: Free Mermaid Diagram Editor

**原文链接**: [https://moxiedocs.com/mermaid-diagram-editor](https://moxiedocs.com/mermaid-diagram-editor)

生成摘要时出错

---

## 80. OpenWrt One – Open Hardware Router

**原文标题**: OpenWrt One – Open Hardware Router

**原文链接**: [https://openwrt.org/toh/openwrt/one](https://openwrt.org/toh/openwrt/one)

生成摘要时出错

---

## 81. Why skilled workers come to Germany and then leave again

**原文标题**: Why skilled workers come to Germany and then leave again

**原文链接**: [https://www.dw.com/en/germany-migrants-skilled-workers-integration-labor-market-bureaucracy-language-housing/a-77853162](https://www.dw.com/en/germany-migrants-skilled-workers-integration-labor-market-bureaucracy-language-housing/a-77853162)

生成摘要时出错

---

## 82. Computational Balloon Twisting: The Theory of Balloon Polyhedra [pdf]

**原文标题**: Computational Balloon Twisting: The Theory of Balloon Polyhedra [pdf]

**原文链接**: [https://cccg.ca/proceedings/2008/paper34full.pdf](https://cccg.ca/proceedings/2008/paper34full.pdf)

生成摘要时出错

---

## 83. CoMaps – FOSS Offline Maps

**原文标题**: CoMaps – FOSS Offline Maps

**原文链接**: [https://www.comaps.app/](https://www.comaps.app/)

生成摘要时出错

---

## 84. China sentences official to death for taking $325M in bribes

**原文标题**: China sentences official to death for taking $325M in bribes

**原文链接**: [https://www.bbc.com/news/articles/c33y0n1v1xjo](https://www.bbc.com/news/articles/c33y0n1v1xjo)

生成摘要时出错

---

## 85. The revenge of the philosophy majors

**原文标题**: The revenge of the philosophy majors

**原文链接**: [https://www.nytimes.com/2026/07/05/business/philosophy-majors-ai-jobs.html](https://www.nytimes.com/2026/07/05/business/philosophy-majors-ai-jobs.html)

生成摘要时出错

---

## 86. First Principles of Model Routing

**原文标题**: First Principles of Model Routing

**原文链接**: [https://try.works/first-principles-of-model-routing](https://try.works/first-principles-of-model-routing)

生成摘要时出错

---

## 87. Reform UK leader 'in real trouble' against Count Binface

**原文标题**: Reform UK leader 'in real trouble' against Count Binface

**原文链接**: [https://www.mirror.co.uk/news/uk-news/nigel-farage-resigns-clacton-live-37401478](https://www.mirror.co.uk/news/uk-news/nigel-farage-resigns-clacton-live-37401478)

生成摘要时出错

---

## 88. Pure-Python symbolic regression that rediscovered Kepler's law from 8 data point

**原文标题**: Pure-Python symbolic regression that rediscovered Kepler's law from 8 data point

**原文链接**: [https://github.com/ariel95500-create/gp-elite](https://github.com/ariel95500-create/gp-elite)

生成摘要时出错

---

## 89. Show HN: PostgreSQL performance and cost across 23 EC2 instance types

**原文标题**: Show HN: PostgreSQL performance and cost across 23 EC2 instance types

**原文链接**: [https://postgres.saneengineer.com](https://postgres.saneengineer.com)

生成摘要时出错

---

## 90. The most unbelievable things about life before smartphones (2020)

**原文标题**: The most unbelievable things about life before smartphones (2020)

**原文链接**: [https://mattruby.substack.com/p/the-most-unbelievable-things-about](https://mattruby.substack.com/p/the-most-unbelievable-things-about)

生成摘要时出错

---

## 91. Kernel anti-cheat is an overreach

**原文标题**: Kernel anti-cheat is an overreach

**原文链接**: [https://nooneshappy.com/article/kernel-anti-cheat-is-an-overreach/](https://nooneshappy.com/article/kernel-anti-cheat-is-an-overreach/)

生成摘要时出错

---

## 92. Out of the Armchair

**原文标题**: Out of the Armchair

**原文链接**: [https://literaryreview.co.uk/out-of-the-armchair](https://literaryreview.co.uk/out-of-the-armchair)

生成摘要时出错

---

## 93. The family keeping watch over a 52-year-old pot of soup

**原文标题**: The family keeping watch over a 52-year-old pot of soup

**原文链接**: [https://www.wsj.com/arts-culture/food-cooking/the-family-keeping-watch-over-a-52-year-old-pot-of-soup-1e72f115](https://www.wsj.com/arts-culture/food-cooking/the-family-keeping-watch-over-a-52-year-old-pot-of-soup-1e72f115)

生成摘要时出错

---

## 94. GitHub Freno: cooperative, highly available throttler service

**原文标题**: GitHub Freno: cooperative, highly available throttler service

**原文链接**: [https://github.com/github/freno](https://github.com/github/freno)

生成摘要时出错

---

## 95. Dolosse – a South African invention used over the world

**原文标题**: Dolosse – a South African invention used over the world

**原文链接**: [https://thisbugslife.com/2021/11/21/dolosse-a-south-african-invention-used-over-the-world/](https://thisbugslife.com/2021/11/21/dolosse-a-south-african-invention-used-over-the-world/)

生成摘要时出错

---

## 96. Historic Photos of NASA's Cavernous Wind Tunnels

**原文标题**: Historic Photos of NASA's Cavernous Wind Tunnels

**原文链接**: [https://www.theatlantic.com/photo/2018/05/historic-photos-of-nasas-cavernous-wind-tunnels/560660/](https://www.theatlantic.com/photo/2018/05/historic-photos-of-nasas-cavernous-wind-tunnels/560660/)

生成摘要时出错

---

## 97. Show HN: Halo – open-source, tamper-evident runtime evidence for AI agents

**原文标题**: Show HN: Halo – open-source, tamper-evident runtime evidence for AI agents

**原文链接**: [https://github.com/bkuan001/halo-record](https://github.com/bkuan001/halo-record)

生成摘要时出错

---

## 98. Show HN: Fast, native Mac file manager (filters, fuzzy find, 9 MB, no Electron)

**原文标题**: Show HN: Fast, native Mac file manager (filters, fuzzy find, 9 MB, no Electron)

**原文链接**: [https://whimfiles.com](https://whimfiles.com)

生成摘要时出错

---

## 99. Show HN: Docx-CLI: agents read/edit Word docs using 1/2 the time and tokens

**原文标题**: Show HN: Docx-CLI: agents read/edit Word docs using 1/2 the time and tokens

**原文链接**: [https://github.com/kklimuk/docx-cli](https://github.com/kklimuk/docx-cli)

生成摘要时出错

---

## 100. C++ Details of Asymmetric Fences

**原文标题**: C++ Details of Asymmetric Fences

**原文链接**: [https://nekrozqliphort.github.io/posts/membarrier/](https://nekrozqliphort.github.io/posts/membarrier/)

生成摘要时出错

---

