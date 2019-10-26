x = float(input("Введите значение Х (Х не = 0): "))
while x == 0:
    x = float(input("Введите значение Х (Х не = 0): "))
n = int(input("Введите верхнюю границу n (целое число, больше 0): "))
while n <= 0:
    n = int(input("Введите верхнюю границу n (целое число, больше 0): "))
result = float()
for count in range(n + 1):
    result += x + count
print("При Х = " + str(x) + " и границе n = " + str(n) + ", ∑(x+i)/x^2 = " + str(result/x**2))