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

最小安装只需要：

```text
SKILL.md
```

建议同时保留：

```text
references/
examples/
tests/
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
    └── test_structure.sh
```

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

MIT License，见 [LICENSE](./LICENSE)。
