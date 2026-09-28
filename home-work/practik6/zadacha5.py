x1 = int(input("Введите координату x1: "))
y1 = int(input("Введите координату y1: "))
x2 = int(input("Введите координату x2: "))
y2 = int(input("Введите координату y2: "))

if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
    print("YES")
else:
    print("NO")
