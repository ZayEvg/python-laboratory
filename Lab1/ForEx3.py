print("Якщо Х <= 7, то F(X) = -3X + 9")
print("Якщо Х > 7, то F(X) = 1/(X - 7)")
x = float(input("Для обчислення значення F(X), введіть Х: "))
if x <= 7:
    print("F(X) = -3X + 9 = " + str(-3*x + 9))
else:
    print("F(X) = 1/(X - 7) = " + str(1/(x - 7)))
