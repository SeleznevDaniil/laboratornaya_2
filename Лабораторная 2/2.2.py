salary = int(input("Введите ваш месячный доход: "))
spend = int(input("Введите ваши месячные траты: "))
money_capital = 0
for i in range(10):
    money_capital = (spend - salary) + money_capital
    spend = spend * 1.03
print(money_capital)
