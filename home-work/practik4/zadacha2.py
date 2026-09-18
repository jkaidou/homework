import math

x1 = float(input("Введите число x1: "))
y1 = float(input("Введите число y1: "))
x2 = float(input("Введите число x2: "))
y2 = float(input("Введите число y2: "))

distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
print(distance)
