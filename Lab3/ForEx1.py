print()
print("Выполнил: Зайцев Евгений, группа КМ-93")
print()
text = str("Fifth aftermath some another words sociopath xenolith footbath ")
word = str()
forEx = "1"
while forEx == "1":
    for x in range(len(text)):
        if text[x] == " ":
            slc1 = slice(len(word) - 2, len(word))
            if word[slc1] == "th":
                print("Before: " + str(word))
                slc2 = slice(-len(word) + 3, len(word))
                print("After: " + str(word[slc2]))
            word = str()
        else:
            word += text[x]
    forEx = input("\n1 - Продолжить, \nНе 1 - Выход:    " + "")
    print()