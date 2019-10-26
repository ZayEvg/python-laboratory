candy = float(input("Введіть ціну 1кг цукерок: "))
cakes = float(input("Введіть ціну 1кг печива: "))
print("1)Одна покупка, яка складає 300г цукерок та 400г печива")
print("2)Три покупки, кожна з 2кг печива і 1,8кг цукерок")
count = 0
while count == 0:
    choose = int(input("Оберіть операцію обчислення(1 або 2): "))
    if choose == 1 or choose == 2:
        count = 1
if choose == 1:
    print("Результат: " + str(candy*0.3 + cakes*0.4))
elif choose == 2:
    print("Результат: " + str(3*(cakes*2 + candy*1.8)))