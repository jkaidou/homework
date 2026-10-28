n = int(input("Введите натуральное число: ")) #input строка, а не число
product = 1 #product & 10% умножиться сама на себя по скрипту ниже

while n > 0: # while n >= 10: цикл остановиться
    digit = n % 10
    product = product * digit
    n //= 10

print(product)
