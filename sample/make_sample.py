# Builds sample/bank.sample.json: 20 ORIGINAL demo questions + taxonomy + glossary + 4 demo cards.
# Every question here was written for this repo. Do not add third-party questions to this file.
import json, os, html
H = os.path.dirname(os.path.abspath(__file__))
TAX = json.load(open(os.path.join(H, 'taxonomy.json')))
GL = json.load(open(os.path.join(H, 'glossary.json')))
SUBJ = json.load(open(os.path.join(H, 'subjects.json')))

def p(t): return ''.join(f'<p>{html.escape(x)}</p>' for x in t.split('\n'))

Q = [
 ('quant', '85.5', 'A deposit pays a stated annual rate of 12%, compounded monthly. Its effective annual rate (EAR) is closest to:',
  ['12.00%', '12.68%', '12.36%'], 1,
  'EAR = (1 + 0.12/12)^12 - 1 = 1.01^12 - 1 = 12.68%.',
  'EAR = (1 + 12%/12)^12 - 1 = 12.68%。复利次数越多，EAR 越高于报价利率。', '12.36% 是按季度复利的结果，别看错复利频率。'),
 ('quant', '90.4', 'A fund has a mean annual return of 8% and a standard deviation of 12%. Its coefficient of variation is:',
  ['0.67', '4.00', '1.50'], 2,
  'CV = standard deviation / mean = 12% / 8% = 1.50.',
  'CV = 标准差 / 均值 = 12% / 8% = 1.5，衡量每单位收益承担的风险，越低越好。', '分子分母别颠倒：0.67 是 均值/标准差。'),
 ('econ', '30.0', 'The USD/EUR rate is 1.1000 (USD per EUR) and the JPY/USD rate is 150.00 (JPY per USD). The JPY/EUR cross rate is closest to:',
  ['165.00', '136.36', '150.00'], 0,
  'JPY/EUR = JPY/USD x USD/EUR = 150.00 x 1.1000 = 165.00.',
  'JPY/EUR = (JPY/USD) × (USD/EUR) = 150 × 1.1 = 165。让中间货币 USD 约掉。', '先写成"价格货币/基础货币"，再看哪个货币要约掉。'),
 ('econ', '34.6', 'A government raises spending by 100 and raises taxes by 100 at the same time. Assuming a marginal propensity to consume of 0.8, aggregate demand will most likely:',
  ['decrease', 'increase', 'remain unchanged'], 1,
  'Spending adds 100 to demand directly, while the tax increase reduces consumption by only 0.8 x 100 = 80. The balanced budget multiplier is positive, so aggregate demand increases.',
  '政府支出全额进入需求，加税只让消费减少 MPC × 100 = 80，所以平衡预算乘数为正，总需求增加。', '"收支同增"不是中性政策。'),
 ('corp', '14.0', 'A project costs 100 today and returns 60 at the end of each of the next two years. At a 10% discount rate, its NPV is closest to:',
  ['-4.13', '20.00', '4.13'], 2,
  'NPV = -100 + 60/1.10 + 60/1.10^2 = -100 + 54.55 + 49.59 = 4.13.',
  'NPV = -100 + 60/1.1 + 60/1.1² = 4.13 > 0，接受项目。', '20 是没折现的结果。'),
 ('corp', '15.1', 'A firm is financed 40% with debt costing 6% before tax and 60% with equity costing 12%. The tax rate is 25%. Its WACC is closest to:',
  ['9.0%', '9.6%', '7.8%'], 0,
  'WACC = 0.40 x 6% x (1 - 0.25) + 0.60 x 12% = 1.8% + 7.2% = 9.0%.',
  'WACC = 40% × 6% × (1 - 25%) + 60% × 12% = 9.0%。债务成本要用税后。', '9.6% 忘了税盾。'),
 ('fsa', '31.1', 'A company has days of sales outstanding of 40, days of inventory on hand of 50 and days of payables of 30. Its cash conversion cycle is:',
  ['120 days', '60 days', '20 days'], 1,
  'Cash conversion cycle = DSO + DOH - DPO = 40 + 50 - 30 = 60 days.',
  '现金周期 = 应收天数 + 存货天数 - 应付天数 = 40 + 50 - 30 = 60 天。', '应付天数是减项。'),
 ('fsa', '3.0', 'During a period of rising prices and stable inventory levels, compared with FIFO, a company using LIFO will most likely report:',
  ['higher cost of goods sold', 'higher gross profit', 'higher ending inventory'], 0,
  'With rising prices, LIFO expenses the most recent (higher) costs, so COGS is higher and gross profit and ending inventory are lower than under FIFO.',
  '物价上涨时，LIFO 把最新、更贵的成本计入 COGS，所以 COGS 更高，毛利和期末存货更低。', 'LIFO 只有 US GAAP 允许，IFRS 不允许。'),
 ('equity', '26.3', 'A stock is expected to pay a dividend of 2.00 next year. Dividends grow at 5% forever and the required return is 10%. The stock value is closest to:',
  ['42.00', '20.00', '40.00'], 2,
  'V0 = D1 / (r - g) = 2.00 / (0.10 - 0.05) = 40.00.',
  'Gordon 模型：V0 = D1 / (r - g) = 2 / 5% = 40。', '题目给的是 D1，不用再乘 (1+g)；给 D0 才要乘。'),
 ('equity', '87.0', 'A price-weighted index contains three stocks priced at 10, 20 and 90. If only the 90 stock rises by 10%, the index return is closest to:',
  ['10.0%', '7.5%', '3.3%'], 1,
  'Index level moves from (10+20+90)/3 = 40 to (10+20+99)/3 = 43, a return of 7.5%.',
  '价格加权指数 = 价格平均。高价股涨 10% 让指数从 40 变 43，涨 7.5%。', '价格加权下高价股影响最大，和市值无关。'),
 ('fi', '35.0', 'A two-year bond pays a 5% annual coupon. If its yield to maturity is 6%, its price per 100 of par is closest to:',
  ['100.00', '101.86', '98.17'], 2,
  'Price = 5/1.06 + 105/1.06^2 = 4.72 + 93.45 = 98.17. The coupon is below the yield, so the bond trades at a discount.',
  '价格 = 5/1.06 + 105/1.06² = 98.17。票息率低于收益率，折价交易。', '票息 < YTM 折价，票息 > YTM 溢价。'),
 ('fi', '101.1', 'A bond has a Macaulay duration of 5.00 and a yield to maturity of 4% (annual). If its yield rises by 50 bp, its price will change by approximately:',
  ['-2.40%', '+2.40%', '-2.50%'], 0,
  'ModDur = 5.00 / 1.04 = 4.81. %ΔP ≈ -4.81 x 0.005 = -2.40%.',
  '修正久期 = 5 / 1.04 = 4.81，价格变动 ≈ -4.81 × 0.5% = -2.40%。', '-2.50% 是直接用麦考利久期算的。'),
 ('deriv', '80.2', 'An asset with no carry costs or benefits trades at 100. The annual risk-free rate is 5%. The no-arbitrage price of a one-year forward is closest to:',
  ['95.24', '105.00', '100.00'], 1,
  'F0 = S0 x (1 + r)^T = 100 x 1.05 = 105.00.',
  '无持有成本时 F0 = S0 × (1 + r)^T = 105。', '95.24 是把现货折现了，方向反了。'),
 ('deriv', '72.3', 'A one-year European call on a non-dividend stock costs 5.00. The stock price is 50, the strike is 50 and the risk-free rate is 4%. The price of the matching put is closest to:',
  ['5.00', '6.92', '3.08'], 2,
  'Put-call parity: p = c - S + X/(1+r)^T = 5.00 - 50 + 50/1.04 = 3.08.',
  '平价公式 c + PV(X) = p + S，所以 p = 5 - 50 + 50/1.04 = 3.08。', '平值期权的 call 比 put 贵，因为 PV(X) < S。'),
 ('alt', '1.0', 'A hedge fund grows from 100 to 120 in a year. It charges a 2% management fee on year-end assets and a 20% incentive fee on gains net of the management fee, with no hurdle. The incentive fee is closest to:',
  ['3.52', '4.00', '3.04'], 0,
  'Management fee = 2% x 120 = 2.40. Incentive fee = 20% x (120 - 100 - 2.40) = 3.52.',
  '管理费 = 2% × 120 = 2.4；激励费 = 20% × (20 - 2.4) = 3.52。', '先看激励费是按扣管理费前还是扣管理费后算。'),
 ('alt', '53.5', 'Survivorship bias in hedge fund indexes most likely causes reported index returns to be:',
  ['understated', 'overstated', 'unaffected'], 1,
  'Funds that fail stop reporting and drop out of the index, so the remaining history over-represents successful funds and overstates returns.',
  '失败的基金退出指数，剩下的都是活下来的，所以指数收益被高估。', '不是所有偏差都高估，但 survivorship 和 backfill 偏差会高估。'),
 ('pm', '79.4', 'A portfolio returned 10% with a standard deviation of 16%. The risk-free rate is 2%. Its Sharpe ratio is:',
  ['0.50', '0.63', '0.08'], 0,
  'Sharpe = (10% - 2%) / 16% = 0.50.',
  'Sharpe = (Rp - Rf) / σp = 8% / 16% = 0.5。', '0.63 是没减无风险利率。'),
 ('pm', '78.6', 'The risk-free rate is 3% and the market risk premium is 5%. Under CAPM, the required return on a stock with a beta of 1.2 is:',
  ['9.6%', '6.0%', '9.0%'], 2,
  'E(R) = 3% + 1.2 x 5% = 9.0%.',
  'CAPM：E(R) = Rf + β × 市场风险溢价 = 3% + 1.2 × 5% = 9%。', '给的是风险溢价，不是市场收益率，别再减 Rf。'),
 ('ethics', '43.2', 'An analyst combines public information with non-material, non-public details from a supplier visit and concludes a company will miss earnings. Trading on this conclusion:',
  ['violates Standard II(A)', 'is permitted under the mosaic theory', 'requires the company to confirm first'], 1,
  'Under the mosaic theory, combining public information with non-material non-public information to reach a material conclusion is not a violation.',
  '马赛克理论：公开信息 + 非重大非公开信息拼出的结论可以使用，不违反 II(A)。', '只要其中有一条是重大非公开信息，就不适用马赛克理论。'),
 ('ethics', '46.2', 'A portfolio manager buys a stock for her personal account a few minutes before her firm releases a buy recommendation on it to clients. This most likely:',
  ['is acceptable if the position is small', 'violates Standard VI(B)', 'violates only Standard I(B)'], 1,
  'Standard VI(B) requires client and employer transactions to take priority over personal transactions. Trading ahead of the recommendation violates it regardless of size.',
  'VI(B) 交易优先级：客户和雇主优先，个人账户最后。抢在推荐发布前交易就违规，和金额大小无关。', ''),
]

readings, qs = {}, []
for i, (sj, k, stem, opts, a, en, zh, tip) in enumerate(Q, 1):
    rid = 'D-' + sj
    readings.setdefault(rid, {'id': rid, 'title': next(s['zh'] for s in SUBJ if s['id'] == sj) + ' 示例题', 'subject': sj, 'src': 'demo', 'count': 0})
    readings[rid]['count'] += 1
    m, t = map(int, k.split('.'))
    q = {'id': f'D{i}', 'r': rid, 'sj': sj, 'n': readings[rid]['count'], 's': p(stem), 'o': opts, 'a': a, 'e': p(en), 'z': zh, 'k': [m, t]}
    if tip: q['t'] = tip
    qs.append(q)

JC = {
 '85.5': {'c': '报价利率要按复利频率换算成 EAR 才能比较。复利越频繁，EAR 越高；连续复利是上限。',
          'f': [r'\text{EAR} = \left(1 + \frac{r_s}{m}\right)^{m} - 1', r'\text{EAR}_{\text{continuous}} = e^{r_s} - 1'],
          'p': ['比较不同复利频率的产品，一律换成 EAR', 'm 越大 EAR 越高，但增幅递减'], 't': ['报价利率 ≠ 实际利率'], 's': [['示例讲义', '1-2']]},
 '26.3': {'c': 'Gordon 增长模型假设股利以固定增速 g 永续增长，要求 r > g，适合成熟、分红稳定的公司。',
          'f': [r'V_0 = \frac{D_1}{r - g} = \frac{D_0(1+g)}{r - g}'],
          'p': ['g 必须小于 r，否则模型失效', '对 r 与 g 的差非常敏感'], 't': ['题目给 D0 还是 D1 要看清'], 's': [['示例讲义', '5']]},
 '101.1': {'c': '修正久期衡量收益率变动 1% 时价格的近似百分比变动；麦考利久期是现金流的加权平均回收时间。',
           'f': [r'\text{ModDur} = \frac{\text{MacDur}}{1 + r}', r'\%\Delta P \approx -\text{ModDur} \times \Delta y'],
           'p': ['YTM > 0 时 ModDur < MacDur', '久期估算是线性近似，收益率大幅变动时要加凸性'], 't': ['算价格变动用修正久期，不是麦考利久期'], 's': [['示例讲义', '8-9']]},
 '72.3': {'c': '看跌看涨平价：信托看涨 (call + 无风险债券) 与保护性看跌 (put + 股票) 到期收益相同，所以价格相同。',
          'f': [r'c + \frac{X}{(1+r)^{T}} = p + S'],
          'p': ['只适用于同标的、同行权价、同到期日的欧式期权', '任一项价格偏离都可以套利'], 't': ['X 要折现，S 不折现'], 'b': 1},
}

# 翻卡 (flashcards): optional question/answer per knowledge point. Points without one fall back to the knowledge card.
FQ = {
 '85.5': {'q': '同样是 12% 的报价利率，按月复利和按年复利，哪个 EAR 更高？高多少？', 'a': '按月复利更高：EAR = (1 + 0.12/12)^12 - 1 ≈ 12.68%，比按年复利的 12% 高约 0.68 个百分点。'},
 '26.3': {'q': 'Gordon 增长模型什么时候不能用？', 'a': '要求回报率 r 不大于股利增速 g 时模型失效；它也不适合不分红或增速很不稳定的公司。'},
 '101.1': {'q': '修正久期 7、收益率上升 50 个基点，债券价格大约变多少？', 'a': '约下跌 3.5%：-7 × 0.005 = -3.5%。收益率变动大时还要加凸性调整。'},
}

bank = {
 'format': 'studyroom/bank@1',
 'title': '示例题库 (原创演示题)',
 'exam': {'name': 'CFA Level I · 2026', 'weights': {'ethics': 17.5, 'quant': 7.5, 'econ': 7.5, 'fsa': 12.5, 'corp': 7.5, 'equity': 12.5, 'fi': 12.5, 'deriv': 6.5, 'alt': 8.5, 'pm': 10}, 'session': 90, 'secPer': 90, 'note': 'CFA 一级正式考试每场 90 题、135 分钟，平均每题 1.5 分钟。'},
 'subjects': SUBJ,
 'sources': [{'id': 'demo', 'name': '示例题库 (原创)', 'short': '示例'}],
 'readings': list(readings.values()),
 'q': qs, 'kp': TAX, 'gl': GL, 'jc': JC, 'fq': FQ,
}
json.dump(bank, open(os.path.join(H, 'bank.sample.json'), 'w'), ensure_ascii=False, indent=1)
print('questions', len(qs), 'cards', len(JC))
