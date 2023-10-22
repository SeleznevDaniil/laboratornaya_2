money_capital = int(input("Введите ваш текущий капитал: "))
salary = int(input("Введите ваш месячный доход: "))
spend = int(input("Введите ваши месячные траты: "))
increase = 5
num = 0
while money_capital + salary >= spend:
    spend = spend * increase / 100
    num = num + 1
else:
    print(num)

