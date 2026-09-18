import math

seat_number = int(input("Введите номер места: "))
compartment_number = math.ceil(seat_number / 4)

print(compartment_number)
