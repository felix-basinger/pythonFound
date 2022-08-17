import json
with open('hw_77.json', 'w', encoding='utf-8') as write_f, open('hw_7.txt', encoding='utf_8') as f:
    profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f}
    f_up = [i for i in profit.values() if i > 0]
    result = [profit, {'Средняя прибыль компании': round(sum(f_up) / len(f_up))}]

    json.dump(result, write_f, ensure_ascii=False, indent=4)