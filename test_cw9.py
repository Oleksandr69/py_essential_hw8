def sum(n_1, n_2):
    return n_1 + n_2

def minus(n_1, n_2):
    return n_1 - n_2

def div(n_1, n_2):
    return n_1 / n_2

def mult(n_1, n_2):
    return n_1 * n_2

def calc_save(result):
    try:
        with open("calc.txt", "x") as f:
            f.write(result)
    except FileExistsError:
        with open("calc.txt", "a") as f:
            f.write(result)

def view_history():
    with open("calc.txt", "r") as f:
        data = list(f.readlines()[-3:])
    return [line.replace("\n", "") for line in data]

while True:
    choice = input("Виберіть операцію ( '+' '-' '*' '/'), або 'stop' для виходу : ")
    if choice == "stop":
        break
    number_1 = int(input("Введіть перше число: "))
    number_2 = int(input("Введіть друге число: "))   
    if choice == "+":
        calc_save(f"\n{number_1} + {number_2} = {sum(number_1, number_2)}")
    elif choice == "-":
        calc_save(f"\n{number_1} - {number_2} = {minus(number_1, number_2)}")
    elif choice == "/":
        calc_save(f"\n{number_1} / {number_2} = {div(number_1, number_2)}")
    elif choice == "*":
        calc_save(f"\n{number_1} * {number_2} = {mult(number_1, number_2)}")
    else:
        print("Зробіть вірний вибір!")

# with open("calc.txt", "r") as f:
#     data = f.readlines()[-1:]

print(view_history())


# # ======================================================









