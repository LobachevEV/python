import json
from functools import partial
from operator import lt

if __name__ == '__main__':
    firm_profit_dict = {}
    with open('firm_report.txt', encoding='utf-8') as firm_report:
        for line in firm_report:
            name, _, revenue, loss = map(lambda s: s.strip().strip('.'), line.split())
            profit = float(revenue) - float(loss)
            firm_profit_dict[name] = profit

    gt_then_0 = partial(lt, 0)
    positive_profit = list(filter(gt_then_0, firm_profit_dict.values()))
    average_profit = sum(positive_profit) / len(positive_profit)

    with open("profit_report.json", 'w') as profit_report:
        json.dump([firm_profit_dict, {'average_profit': average_profit}], profit_report)
