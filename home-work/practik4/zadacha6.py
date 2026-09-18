import math

x_degrees = float(input("Введите действительное число x: "))
x_radians = math.radians(x_degrees)

result = math.sin(x_radians) + math.cos(x_radians) + (math.tan(x_radians) ** 2)

print(result)
