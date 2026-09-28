x1 = int(input("Введите координату x1: "))
y1 = int(input("Введите координату y1: "))
x2 = int(input("Введите координату x2: "))
y2 = int(input("Введите координату y2: "))

if (x1 + y1) % 2 == (x2 + y2) % 2:
    print("YES")
else:
    print("NO")
