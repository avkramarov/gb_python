# Запросите у пользователя значения выручки и издержек фирмы. 
# Определите, с каким финансовым результатом работает фирма 
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки). 
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите 
# рентабельность выручки (соотношение прибыли к выручке). 
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

revenue = int(input("Сумма выручки >>>"))
costs = int(input("Сумма издержек >>>"))
if revenue > costs:
    print("Фирма отработала с прибылью")
    profit = revenue - costs
    cost_efficiency = profit / revenue
    print("Рентабельность равна: ", cost_efficiency)
    employees = int(input("Численность персонала >>>"))
    profit_per_employee = profit / employees
    print("Прибыль фирмы в расчете на одного сотрудника: ", profit_per_employee)
elif revenue == costs:
    print("Фирма отработала с нулевой прибылью")   
else:
    print("Фирма отработала с убытком")
