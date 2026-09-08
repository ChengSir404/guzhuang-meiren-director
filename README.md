# 古装美人文生图美化 Skill

一个面向 Codex 的中文 Skill，用来把简短想法完善为层次清楚、安全、可直接交给 ChatGPT 文生图的东方古装人物提示词。

> 这个 Skill 在 Codex 中运行，产出 ChatGPT 文生图提示词；它不会自行调用图片生成工具。

## 特点

- 支持从零新建、整理原稿、参考图引导和失败出图修复；只补必要缺口，详细原稿不另加人物、剧情或风格。
- 未指定时采用20–25岁成年东方人物、真人写实与9:16竖版。年龄、肤色、媒介和画幅等明确要求优先于默认审美。
- 提供五种美貌方向，将美感落到五官、神态、衣料和光色；按实际景别提高面部可读性，保留指定侧脸、全身和大场景，不承诺实际出图质量。
- 根据身份与题材协调妆造、服装、动作和环境，区分朝代考据与古典灵感设计。故事画面强调当下瞬间，静态肖像允许无事件、无道具。
- 以完整不透明服装、自然体态和衣料垂坠表达人物，保持非色情化；根据需要描述整体身材与衣着适配；具体胸型仅在用户明确要求或调用预设时使用。
- 新建默认给连贯完整提示词，复杂画面可用九层导演版；整理保留原稿结构，局部修复优先给替换段落，遵从字数和段数要求。
- 多图参考逐张说明身份、妆造、构图或光色职责及禁止迁移项；当前文字要求优先，参考图只控制被指定且未要求改变的特征。
- 失败修复先看整图与问题区域，只调整必要变量，并在提示词中明确其余保持项；保持项是生成约束，实际结果仍需复查。

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

只改光线，保留其他设定：

```text
使用 $guzhuang-meiren-director 只修改下面原稿的光线段，让脸更清楚；保留脸型、服装、动作与全身构图，只输出替换段：
（粘贴原稿）
```

整理原稿，保留两段：

```text
使用 $guzhuang-meiren-director 整理下面两段提示词，仍保留两段，不新增分区、人物或剧情，只消除重复和矛盾：
（粘贴两段原稿）
```

按需加入丰满衣着轮廓：

```text
使用 $guzhuang-meiren-director 用固定丰满胸型模板，保留原稿年龄、腰线、服装和构图：
（粘贴原稿）
```

默认调用“自然丰满版”；明确说“固定丰满胸型模板加强版”时使用“较丰满版”。两者均服从完整衣着、真实比例与服装结构，不默认露肤或改变年龄、腰线，也不承诺审核或出图效果。详见 [衣着轮廓预设](references/body-silhouette.md)。

按需搭配配饰，可说“用固定腰链模板”或“用固定脚链模板”。默认一个主配饰、少量辅助，已有首饰计入预算；不会自动露腰、改裙长、换鞋或改变构图。具体规则见 [配饰搭配](references/accessory-styling.md)。

更多请求方式见 [examples/usage.md](examples/usage.md)。

## 默认审美与自定义

默认审美偏向东方古典、真人写实、电影感、自然抓拍和有故事的动作。配置集中在 [references/personal-aesthetic.md](references/personal-aesthetic.md)，可以直接修改人物年龄范围、气质、身材表达、妆发、服装、配色、道具和构图偏好。

在明确成年、完整衣着、非色情化的创作范围内，当前明确要求优先；参考图只控制用户指定职责内且未要求改变的特征，其次考虑朝代与身份的必要结构约束，最后应用默认配置。默认故事感不覆盖静态肖像、无道具或其他明确要求。

## 项目结构

```text
guzhuang-meiren-director/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── historical-styling.md
│   ├── art-direction.md
│   ├── beauty-direction.md
│   ├── accessory-styling.md
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
- `control-workflow.md`：约束优先级、补全强度、参考图职责和单变量修复。
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
