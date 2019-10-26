print()
print("Работу выполнил: Зайцев Евгений, группа КМ-93")
print()
first_limit = int(input("Введите первую границу диапазона(целое число): "))
second_limit = int(input("Введите вторую границу диапазона(целое число): "))
while first_limit == second_limit or first_limit > second_limit:
    if first_limit == second_limit:
        print("     Границы не должны быть равны")
        first_limit = int(input("Введите первую границу диапазона(целое число): "))
        second_limit = int(input("Введите вторую границу диапазона(целое число): "))
    else:
        print("     Первая граница должна быть больше второй")
        print("Первая граница диапазона: " + str(first_limit))
        second_limit = int(input("Введите вторую границу диапазона(целое число): "))
result = int(0)
if first_limit % 2 == 0:
    changed_first_limit = int(first_limit + 1)
    if second_limit % 2 == 0:
        changed_second_limit = int(second_limit - 1)
        result = changed_first_limit
        while changed_first_limit != changed_second_limit:
            changed_first_limit += 2
            result += changed_first_limit
    else:
        result = changed_first_limit
        while changed_first_limit != second_limit:
            changed_first_limit += 2
            result += changed_first_limit
else:
    if second_limit % 2 == 0:
        changed_second_limit = int(second_limit - 1)
        result = first_limit
        while first_limit != changed_second_limit:
            first_limit += 2
            result += first_limit
    else:
        result = first_limit
        while first_limit != second_limit:
            first_limit += 2
            result += first_limit
print("Результат: " + str(result))