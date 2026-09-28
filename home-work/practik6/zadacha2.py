pocket = int(input("Введите номер кармана: "))

if pocket < 0 or pocket > 36:
    print("Ошибка ввода")
elif pocket == 0:
    print("Зеленый")
else:
    color= " "
    if 1 <= pocket <= 10:
        # 1-10: нечетные - красный, четные - черный
        color = "Красный" if pocket % 2 != 0 else "Черный"
    elif 11 <= pocket <= 18:
        # 11-18: нечетные - черный, четные - красный
        color = "Черный" if pocket % 2 != 0 else "Красный"
    elif 19 <= pocket <= 28:
        # 19-28: нечетные - красный, четные - черный
        color = "Красный" if pocket % 2 != 0 else "Черный"
    elif 29 <= pocket <= 36:
        # 29-36: нечетные - черный, четные - красный
        color = "Черный" if pocket % 2 != 0 else "Красный"

    print(color)
