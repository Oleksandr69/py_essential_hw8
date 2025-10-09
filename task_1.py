import random
# Напишіть скрипт, який створює текстовий файл і записує до нього
# 10000 випадкових дійсних чисел. Створіть ще один скрипт, який
# читає числа з файлу та виводить на екран їхню суму.
# ==============================================
# file = open("text.txt", "r")
# print(file.read())
# file.close()
# ==============================================
# with open("text.txt", "r") as f:
#     data = f.read()
# print(data)
# ==============================================

with open("number.txt", "w") as f:
    for _ in range(10):
        f.write(f"{random.random()}, ")
    f.write(f"{random.random()}, ")
with open("number.txt", "r") as f:
    data = f.read()

list_number = data.split(", ")
list_number.pop()

sum = 0
for number in list_number:
    sum += float(number)
print()
print(f"Сума випадкових чисел: {round(sum, 2)}.")

    
    
