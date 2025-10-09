# Модифікуйте вихідний код сервісу зі скорочення посилань з ДЗ 7
# заняття курсу Python Starter так, щоб він зберігав базу посилань
# на диску і не «забув» при перезапуску. За бажанням можете ознайомитися
# з модулем shelve (https://docs.python.org/3/library/shelve.html),
# який у даному випадку буде дуже зручним та спростить виконання
# завдання.
import json
# import os
# PATH = os.path.abspath(__file__+"/..")

def read_links():
    with open("links.json", "r", encoding="utf-8") as f:
        links = json.load(f)
    return links

def write_links(data):
    with open("links.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def is_key_in_keys(name_key):
    data = read_links()
    link_keys = []
    for item in data:
        for key in item.keys():
            # print(key)
            link_keys.append(key)
    if name_key in link_keys:
        return True
    else:
        return False
while True:
    choice = input("1 - add link, 2 - get link, 0 - exit: ")
    if choice == "0":
        break
    elif choice == "1":
        my_value = input("Введіть посилання: ")
        my_name = input("Введіть коротку назву: ")
        if is_key_in_keys(my_name):
            print("Ви ввели вже існуючий ключ")   
        else:
            data = read_links()
            new_data = {my_name: my_value}
            data.append(new_data)
            write_links(data)

    elif choice == "2":
        data = read_links()
        get_link = input("Введіть коротку назву посилання: ")
        if is_key_in_keys(get_link):
            for item in data:
                if get_link in item.keys():
                    print(f"За назвою '{get_link}' маємо посилання: {item.get(get_link)}.")
        else:      
            print (f"За ключем '{get_link}' посилання не знайдено.")
    else:
        print("Зробіть свій вибір вірно")
# ============================================
