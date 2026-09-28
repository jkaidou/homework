temperature = float(input("Введите температуру (°C): "))
pressure = int(input("Введите верхнее давление: "))
pulse = int(input("Введите пульс (уд/мин): "))

is_doctor_need = (
    (temperature < 35 or temperature > 38) or
    (pressure < 105 or pressure > 140) or
    (pulse < 55 or pulse > 110)
)

is_mild_malaise = (
    (35 <= temperature < 36 or 37 < temperature <= 38) or
    (105 <= pressure < 110 or 130 < pressure <= 140) or
    (55 <= pulse < 60 or 100 < pulse <= 110)
)

if is_doctor_need:
    print("Результат: Требуется врач")
elif is_mild_malaise:
    print("Результат: Легкое недомогание")
else:
    print("Результат: Нормальное состояние")
