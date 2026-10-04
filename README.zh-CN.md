# Evaluating Job Offers

[English](./README.md) | 简体中文

一个用于比较工作 Offer **真实决策价值（real decision value）** 的可复用 Agent Skill。

它不只比较招聘方给出的“年包 / TC”，而是进一步拆解：**固定现金、浮动奖金、股权、税费、社保/公积金等法定福利、真实生活成本、通勤与工时、伴侣/家庭共同生活成本，以及长期职业选择权**。

> 核心问题不是“哪个 Offer 的数字最大”，而是：**哪个 Offer 最终能给你带来更高的可支配收入、更好的资产积累、更合理的时间成本，以及更符合你目标的生活与职业路径。**

## 为什么需要这个 Skill

很多 Offer 对比会直接比较：

```text
月薪 × 薪数 + 奖金 + 股票
```

但现实里，同样写着“45 万年包”的两个 Offer，实际价值可能完全不同：

- “15 薪”里可能只有 12 薪固定，3 个月取决于绩效；
- 高公积金 / 养老金 / employer match 不是现金，但仍然是个人资产；
- 相同税前年薪，在不同税制和城市下的税后现金不同；
- 大城市更高的房租、跨城通勤和搬迁成本可能吃掉工资差；
- 965 与 995 的有效时薪、自由时间和长期可持续性差异很大；
- 两个人同城合租，可能比异地各租一套房每年节省数万元税后支出；
- 更高薪的岗位未必拥有更好的技术成长、平台或未来跳槽选择。

因此，本 Skill 将 Offer 分解为多个独立维度，并明确区分**事实、历史样本和假设**。

## 核心能力

### 先筛选，再比较

优先服务国内校招技术岗位（含机器人/算法），同时保留其他地域路由：按工作地、税务居民身份、币种和年份核实当地规则。核心仍是**现金与资产、生活成本、时间、成长、家庭**五维，并保留多年个人/家庭合并结余、税前年薪等价和休假时间选择权。

- 先按用户硬约束标记可选、排除或待核实，再做偏好比较。高薪或品牌不能抵消已确认的硬约束违反。
- 区分意向、转正实习、附条件 offer、正式录用，核实实际书面条件；转正后薪资不计为实习阶段保证收入。
- 每轮最多追问 1–3 个会改变选择的问题，信息足够时不问，用户要求更少则从其要求。复用已知信息，不把长问卷塞进三个编号，不重复已拒绝的家庭隐私问题。
- 机器人/算法岗核实真实研发、集成、部署和驻场职责，以及导师时间、设备、数据授权和算力。小公司有好导师也可能更适合成长，不能只按规模排序。
- 分开入职自然年、完整 12 个月和稳定全年；补贴、报销、已兑现股权、已含值班时间均只计一次。
- 证据按问题适配，给出有条件建议及反转条件。历史校招薪资不是现价，作者个人结论不是通用事实。

### 1. 规范化薪酬

将招聘方口径拆分为：

- **Guaranteed**：合同或 Offer 明确保证的固定收入；
- **Target**：达到正常绩效时的目标收入；
- **Upside**：高绩效、股价上涨等乐观情景；
- **Risk-adjusted**：根据历史兑现情况和证据，对浮动部分做风险折算。

不会默认把“N 薪”“目标奖金”或全部 RSU grant 当作确定收入。

### 2. 税后现金与真实资产

根据岗位所在地和对应年份，核实并估算：

- 所得税 / payroll tax；
- 社保、养老金等个人缴纳；
- 公积金、401(k)、养老金、employer match 等；
- 奖金和股权的税务处理；
- 当年实际可归属（vest）的股票价值。

同时区分：

- **Spendable cash**：可直接消费/储蓄的税后现金；
- **Restricted wealth**：公积金、退休账户等受限但属于个人的资产。

### 3. 真实生活成本

优先使用**实际办公地点附近**而不是整座城市的平均成本，比较：

- 房租与住房方案；
- 水电网、饮食、交通；
- 搬迁成本；
- 跨城交通；
- 通勤距离与时间。

### 4. Household Mode（家庭 / 伴侣模式）

当 Offer 会影响伴侣或家庭生活时，可以比较：

- 同城共同租房 vs 两地分别租房；
- 双方通勤变化；
- 跨城往返成本；
- 育儿 / 照护成本；
- 家庭整体可储蓄收入。

一个重要原则是：

> **每年节省 2 万元税后生活支出，不等价于只增加 2 万元税前年薪。**

Skill 会在需要时计算“需要增加多少税前年薪，才能抵消某项税后成本”。

### 5. 时间价值与 WLB

可进一步比较：

- 每周工作时长；
- 通勤时间；
- PTO / 年假；
- on-call、出差、周末工作；
- **有效时薪（effective hourly compensation）**；
- 每年可支配自由时间。

### 6. 职业选择权（Career Option Value）

单独分析，而不是强行折算成人民币：

- 岗位实际工作范围；
- 技术壁垒和技能稀缺度；
- Manager / Team；
- 晋升空间；
- 品牌和履历价值；
- 未来可跳行业 / 岗位范围；
- 技术路线被锁定或过时的风险。

## 证据等级

所有关键数据建议标记来源等级：

| 标签 | 含义 |
|---|---|
| `Offer` | 用户手中的正式 Offer / 合同 / HR 明确书面信息 |
| `Official` | 政府、公司官方规则或公开文件 |
| `Employee report` | 当前 / 前员工、候选人的自报信息 |
| `Historical` | 往届 Offer、历史奖金、历史薪资样本 |
| `Assumption` | 缺少可靠信息时明确写出的假设 |

当多个来源冲突时，优先展示冲突，并使用保守 Base Case，而不是制造虚假的精确数字。

## 输出示例

可以直接提问：

- “比较这三个 Offer 的税后收入和一年实际能存多少钱。”
- “这个 Offer 写 15 薪，但 3 个月都是绩效奖金，真实价值是多少？”
- “我和伴侣在两个不同园区工作，比较一起租房和各自租房。”
- “一个 965 的 38 万 Offer 和一个 995 的 48 万 Offer，实际差距有多大？”
- “上海的岗位需要比杭州高多少年薪，才值得为了异地和住房成本过去？”
- “把职业成长、WLB、现金收入和家庭生活一起比较。”

推荐输出结构：

先给简短的有条件建议和硬约束/录用状态筛选，再按需要展开下列内容。短问题可合并栏目，缺失数据标未知，不强制填满表格；末尾追问遵守每轮上限。

1. 证据与假设；
2. 薪酬标准化表；
3. 税后现金与资产表；
4. 生活成本 / Household Mode；
5. 工时与有效时薪；
6. 职业选择权；
7. 敏感性 / Break-even 分析；
8. 仍需向 HR 或团队确认的问题。

## 安装

将整个 `evaluating-job-offers/` 目录复制到支持 Agent Skills 的客户端技能目录即可。

客户端识别入口是：

```text
SKILL.md
```

完整工作流应同时保留三个参考文件、示例和许可证：

```text
references/
examples/
LICENSE
```

完整目录：

```text
evaluating-job-offers/
├── SKILL.md
├── README.md
├── README.zh-CN.md
├── LICENSE
├── references/
│   ├── input-schema.md
│   ├── calculation-model.md
│   └── evidence-and-research.md
├── examples/
│   └── china-household-example.md
└── tests/
    ├── scenarios.md
    ├── behavioral-cases.json
    ├── validation-report.md
    ├── test_structure.py
    └── test_structure.sh
```

Codex 可使用内置 skill-installer 的安装脚本，参数为 `--repo cn-amz/evaluating-job-offers --path . --name evaluating-job-offers --ref <已审核提交>`。默认安装目录为 `~/.codex/skills/evaluating-job-offers`，设置 `CODEX_HOME` 时使用其 `skills/` 子目录。先比较同名目录，安装脚本会拒绝覆盖；安装后下一轮可用，无须增加运行依赖。

## 验证方式

运行 `python tests/test_structure.py`；原 `bash tests/test_structure.sh` 继续保留为冒烟检查。两者均为**结构检查，不是行为测试**。旧案例保留在 [tests/scenarios.md](tests/scenarios.md)，新增虚构请求位于 [tests/behavioral-cases.json](tests/behavioral-cases.json)。在独立上下文分别运行无技能、旧技能和新技能回答，不向答题代理提供评分标准，再人工核对原始输出。单次样本不能证明稳定通过率；本轮结果及限制见 [tests/validation-report.md](tests/validation-report.md)。

## 设计原则

- **不相信 headline TC，先拆固定与浮动。**
- **不硬编码某一国家税率，按 jurisdiction + date 查询最新规则。**
- **不把受限资产和可花现金混为一谈。**
- **不把招聘 JD 的薪资上限当成实际 Offer。**
- **不把员工自报当官方事实，但可以作为兑现率和 WLB 的经验样本。**
- **不制造单一“最优分数”掩盖真实权衡。**
- 当用户没有明确偏好时，展示 trade-off frontier，而不是擅自决定人生优先级。

## 相关开源项目

在设计本 Skill 时参考了以下公开项目：

- [Paramchoudhary/ResumeSkills - offer-comparison-analyzer](https://github.com/Paramchoudhary/ResumeSkills/tree/main/.agents/skills/offer-comparison-analyzer)
- [yanliudesign/offer-toolkit-skill](https://github.com/yanliudesign/offer-toolkit-skill)

这些项目已经很好地覆盖了 TC、多年收入、非货币因素和职业风险等问题。本项目进一步聚焦于：

> **after-tax cash + statutory benefits + real living cost + time + household economics + evidence provenance**

即：从“比较工作”进一步走到“比较每个 Offer 实际能买到的生活”。

## 注意事项

本项目用于辅助分析和决策，不构成税务、法律、投资或劳动关系专业意见。税率、社保、公积金、养老金和其他制度会随地区和年份变化，涉及真实决策时应核对最新官方规则和本人 Offer 条款。

## License

补充阅读包括阿秀的 offer 选择文章、牛客历史算法校招自述与通用 reverse-interview 提问，链接及适用边界见 [references/evidence-and-research.md](references/evidence-and-research.md)。只引用来源并原创归纳，不复制第三方正文、录用函或个人背景；外部内容保留原权利，不因本项目 MIT 许可而重新授权。新测试均为虚构，不写入用户私事。

MIT License，见 [LICENSE](./LICENSE)。
