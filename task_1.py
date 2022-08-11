from sys import argv

name, prod, sal, prem = argv

print('NAME OF SCRIPT: ', name)
print('\n<<< Рассчет заработной платы сотрудника >>>')
print('PRODUCTION IN HOURS: ', prod)
print('RATE PER HOUR: ', sal)
print('PREMIUM: ', prem)
print((int(prod) * int(sal)) + int(prem))
