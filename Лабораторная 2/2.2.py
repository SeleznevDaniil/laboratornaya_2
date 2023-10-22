salary = int(input("Введите ваш месячный доход: "))
spend = int(input("Введите ваши месячные траты: "))
increase = 3
money_capital = 0
for _ in range(10):
    if salary < spend:
        money_capital = money_capital + spend - salary
    spend = spend * increase / 100
print(money_capital)
