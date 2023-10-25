money_capital = int(input("Введите ваш текущий капитал: "))
salary = int(input("Введите ваш месячный доход: "))
spend = int(input("Введите ваши месячные траты: "))
num = 0
while money_capital + salary >= spend:
    dif = spend - salary
    money_capital = money_capital - dif
    num = num + 1
    spend = spend * 1.05
else:
    print(num)
