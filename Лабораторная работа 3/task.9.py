salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
for current_cap in range(1,months + 1):
    current_cap = spend - salary
    spend *= (increase + 1) # 100% цена продукта, повышение на 0.03, поэтому +1
    need_money += current_cap
# TODO Оформить решение

print(round(need_money))
