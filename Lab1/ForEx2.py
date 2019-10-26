print("Введіть координати точки A:")
x = float(input("X = "))
y = float(input("Y = "))
if x == 0 and y == 0:
    print("Точка A знаходиться на осі ОХ та осі ОY")
elif x == 0 and y != 0:
    print("Точка A знаходиться на осі ОY")
elif x != 0 and y == 0:
    print("Точка A знаходиться на осі ОХ")
elif x > 0 and y > 0:
    print("Точка A знаходиться в І чверті")
elif x > 0 and y < 0:
    print("Точка A знаходиться в IV чверті")
elif x < 0 and y > 0:
    print("Точка A знаходиться в ІІ чверті")
elif x < 0 and y < 0:
    print("Точка A знаходиться в ІІІ чверті")
