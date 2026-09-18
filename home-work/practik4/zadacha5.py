total_minutes = int(input("Введите кол-во минут: "))

hours = total_minutes // 60
remaining_minutes = total_minutes % 60

print(f"{total_minutes} минут - это {hours} час {remaining_minutes} минут.")
