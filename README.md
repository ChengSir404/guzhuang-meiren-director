# 古装美人文生图美化 Skill

一个面向 Codex 的中文 Skill，用来把简短想法完善为层次清楚、安全、可直接交给 ChatGPT 文生图的东方古装人物提示词。

> 这个 Skill 在 Codex 中运行，产出 ChatGPT 文生图提示词；它不会自行调用图片生成工具。

## 特点

- 默认补全 20–25 岁、明确成年的东方古典人物设定。
- 将“漂亮、高级、自然”等抽象词落到五官、皮肤、衣料、动作、光线与镜头细节。
- 内置明艳贵气、清艳含蓄、明媚灵秀、冷艳英气、圣洁华美五种美貌方向；默认采用 9:16 竖版，并以紧凑景别、足够大的人物与脸部占比、双眼同焦和清晰面光保证脸部质量。
- 自动根据贵女、侠女、才女、琴师、女将、敦煌灵感、志怪人物等身份匹配服装、妆发、饰品、道具与环境。
- 先建立“人物身份 + 决定性瞬间 + 情绪潜台词”的画面核，再统一造型语言、视觉主次、镜头、光色与环境反馈，避免参数清单感。
- 支持梨形、沙漏形、直筒形、倒三角形、苹果形等成年身材，以及水滴形、圆润形、圆盘/浅盘形等完整衣着下的胸部轮廓，并自动匹配身份、服装和动作。
- 支持剑、弓、马、琴、棋、书、画、花、团扇、灯笼等道具，并让道具真正参与动作和故事。
- 区分朝代考据、东方古典融合、敦煌/神圣意象和故事电影感。
- 内置安全改写：完整不透明服装、非色情动作、不以敏感部位为视觉焦点。
- 新建默认输出连贯完整提示词，复杂画面可用九层导演版；整理保留原稿结构，局部修复优先提供替换段落，遵从用户字数和段数要求。
- 新增四模式控制：从零新建、整理长提示词、参考图引导、失败出图修复；详细原稿不会被擅自扩写成另一幅画。
- 多张参考图会逐张分配“身份、服装、姿态构图、色彩材质、场景氛围”等职责，并声明禁止迁移项，降低脸被服装参考人物替换的风险。
- 失败修复采用单主变量策略：先看整图再看脸部，冻结已经正确的内容，只修最上游问题，避免每次改稿都把人物和画面重新随机。

## 安装

将仓库克隆到 Codex 的个人 Skill 目录：

```bash
git clone https://github.com/ChengSir404/guzhuang-meiren-director.git ~/.codex/skills/guzhuang-meiren-director
```

重新打开 Codex 任务后，Skill 会出现在可用 Skill 列表中。

## 使用

直接点名 Skill：

```text
使用 $guzhuang-meiren-director 美化：一位清冷侠女站在竹林里。
```

也可以只给少量信息，让 Skill 自动补全：

```text
使用 $guzhuang-meiren-director 写一版宋韵才女弈棋的 ChatGPT 文生图提示词。
```

```text
使用 $guzhuang-meiren-director 把这段提示词改成安全版本，保留敦煌神圣感和成年女性的柔美气质。
```

更多请求方式见 [examples/usage.md](examples/usage.md)。

## 默认审美与自定义

默认审美偏向东方古典、真人写实、电影感、自然抓拍和有故事的动作。配置集中在 [references/personal-aesthetic.md](references/personal-aesthetic.md)，可以直接修改人物年龄范围、气质、身材表达、妆发、服装、配色、道具和构图偏好。

当前请求、参考图和指定朝代始终高于默认配置。

## 项目结构

```text
guzhuang-meiren-director/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── historical-styling.md
│   ├── art-direction.md
│   ├── beauty-direction.md
│   ├── body-silhouette.md
│   ├── control-workflow.md
│   ├── personal-aesthetic.md
│   ├── quality-bar.md
│   └── prompt-architecture.md
├── examples/usage.md
├── examples/director-prompts.md
├── examples/behavioral-cases.md
└── scripts/validate_skill.py
```

- `SKILL.md`：能力边界、路由、自动补全与交付规则。
- `personal-aesthetic.md`：可修改的默认审美配置。
- `art-direction.md`：画面命题、人物辨识度、视觉主次、色彩材质与叙事瞬间规则。
- `beauty-direction.md`：惊艳美貌类型、眉眼与妆容设计、脸部景别、对焦、遮挡和用光规则。
- `body-silhouette.md`：成年女性体态、身材、胸部衣着轮廓及身份匹配规则。
- `control-workflow.md`：任务模式、内部画面契约、约束优先级、参考图角色映射和单变量修复。
- `quality-bar.md`：常见失败症状的修复矩阵；长篇标杆按需读取 [examples/director-prompts.md](examples/director-prompts.md)。
- `historical-styling.md`：朝代妆造起点、考据边界与权威资料入口。
- `prompt-architecture.md`：ChatGPT 文生图的分层提示词结构与安全改写方法。

## 设计取舍

本项目吸收了公开 Skill 中可迁移的工作方法，但没有复制平台专用参数或固定人脸模板：

- 参考 [OpenAI Image Generation Skill](https://github.com/openai/skills/tree/main/skills/.system/imagegen) 的输入图角色标注、保持项复述、按输入具体程度控制补全，以及小步迭代。
- 参考 [Professional Portrait Skill](https://github.com/lovstudio/professional-portrait-skill) 的身份优先、最小充分修改和“整图 + 脸部区域”质量检查。
- 参考 [Replicate Prompt Images Skill](https://github.com/replicate/skills/tree/main/skills/prompt-images) 的自然语言、明确空间关系和从简单修改开始迭代。
- 保留九层分区的可读性，但不采用固定复用同一套脸、长度无限、8K/HDR 质量词、装饰词库随机拼装或默认突出身体部位的方案；这些做法容易造成模板脸、权重稀释和画面失焦。

## 安全与考据边界

- 所有人物默认明确成年，服装完整、不透明，动作非色情化。
- 当原始要求接近裸露、色情化或真实宗教对象性感化时，Skill 会保留非性化的审美意图并自动改写为安全版本。
- 历史参考用于提高时代一致性，不等于学术级复原。严格考据时仍应核对具体时期、地域、身份、场合和最新研究。
- ChatGPT 的产品规则可能更新，实际生成始终以平台当时适用的政策和模型能力为准。

## 验证

本地运行：

```bash
python3 scripts/validate_skill.py
```

验证器检查 frontmatter、Skill 名称、本地引用、UI 元数据、入口路由标记以及仓库噪声文件。GitHub Actions 在推送和 Pull Request 时执行同一检查。它不执行模型，也不证明指令遵循或出图质量。

修改行为规则后，按 [行为回归用例](examples/behavioral-cases.md) 实际生成提示词并逐项核对输出；不要把关键词出现视作行为通过。涉及出图效果时另做同输入、同模型设置的前后对比。

## 贡献

欢迎提交 Issue 或 Pull Request，尤其是：

- 有权威来源支持的朝代服饰、妆容和发饰修正；
- 更自然的动作、道具与环境联动规则；
- 不降低审美表达的安全改写方式；
- ChatGPT 文生图提示词的真实失败案例与窄范围改进。

提交历史考据修正时，请附博物馆、考古报告或学术论文来源，不要以电商页面或影视造型作为唯一依据。

## License

[MIT](LICENSE)
