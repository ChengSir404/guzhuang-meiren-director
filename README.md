# 古装美人文生图美化 Skill

一个面向 Codex 的中文 Skill，用来把简短想法完善为层次清楚、安全、可直接交给 ChatGPT 文生图的东方古装人物提示词。

> 这个 Skill 在 Codex 中运行，产出 ChatGPT 文生图提示词；它不会自行调用图片生成工具。

## 特点

- 默认补全 20–25 岁、明确成年的东方古典人物设定。
- 将“漂亮、高级、自然”等抽象词落到五官、皮肤、衣料、动作、光线与镜头细节。
- 自动根据贵女、侠女、才女、琴师、女将、敦煌灵感、志怪人物等身份匹配服装、妆发、饰品、道具与环境。
- 支持剑、弓、马、琴、棋、书、画、花、团扇、灯笼等道具，并让道具真正参与动作和故事。
- 区分朝代考据、东方古典融合、敦煌/神圣意象和故事电影感。
- 内置安全改写：完整不透明服装、非色情动作、不以敏感部位为视觉焦点。
- 默认输出 15 个清晰分区，也支持精简版与基于参考图的改写。

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
│   ├── personal-aesthetic.md
│   └── prompt-architecture.md
├── examples/usage.md
└── scripts/validate_skill.py
```

- `SKILL.md`：能力边界、路由、自动补全与交付规则。
- `personal-aesthetic.md`：可修改的默认审美配置。
- `historical-styling.md`：朝代妆造起点、考据边界与权威资料入口。
- `prompt-architecture.md`：ChatGPT 文生图的分层提示词结构与安全改写方法。

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

验证器检查 frontmatter、Skill 名称、本地引用、UI 元数据、安全核心约束以及仓库噪声文件。GitHub Actions 会在每次推送和 Pull Request 时执行同一检查。

## 贡献

欢迎提交 Issue 或 Pull Request，尤其是：

- 有权威来源支持的朝代服饰、妆容和发饰修正；
- 更自然的动作、道具与环境联动规则；
- 不降低审美表达的安全改写方式；
- ChatGPT 文生图提示词的真实失败案例与窄范围改进。

提交历史考据修正时，请附博物馆、考古报告或学术论文来源，不要以电商页面或影视造型作为唯一依据。

## License

[MIT](LICENSE)
