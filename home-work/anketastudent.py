print("=== АНКЕТА СТУДЕНТА ===")

last_name = input("Введите фамилию: ")
first_name = input("Введите имя: ")
age = input("Введите возраст: ")
predmet = input("Введите ваш любимый(ые) предмет(ы): ")
hobby = input("Ваше хобби / увлечения: ")

print("\n=== РЕЗУЛЬТАТЫ АНКЕТИРОВАНИЯ ===")
print(f"Студент: {last_name} {first_name}")
print(f"Возраст: {age} лет")
print(f"Любимые предметы: {predmet}" )
print(f"Увлечения: {hobby}")
print("================================")
