# Створіть список товарів в інтернет-магазині. Серіалізуйте його 
# за допомогою pickle та збережіть у JSON.
import json
import pickle
import os

PATH = os.path.abspath(__file__+"/..")
# print(os.listdir(PATH))
# os.remove(os.path.join(PATH, "calc.txt"))
def read_list():
    # with open(os.path.join(PATH, "list_of_goods.json"), "r", encoding="utf-8") as f:
    #     list = json.load(f)
    with open(os.path.join(PATH, "list_of_good.pkl"), "rb") as f:
        list_pkl = pickle.load(f)
        # print(list_pkl)
    return list_pkl

def write_list(data):
    with open(os.path.join(PATH, "list_of_goods.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    with open(os.path.join(PATH, "list_of_good.pkl"), "wb") as f:
        pickle.dump(data, f)

def is_name_in_goods(product_name):
    data = read_list()
    name_list = []
    for item in data:
        name_list.append(item["name"])
    if product_name in name_list:
        return True
    else:
        return False
          
while True:
    choice = input("1 - add goods, 2 - get goods, 0 - exit: ")
    if choice == "0":
        break
    elif choice == "1":
        product_name = input("Введіть назву: ")
        product_cost = input("Введіть вартість: ")
        
        if is_name_in_goods(product_name):
            print("Ви ввели вже існуючий ключ")   
        else:
            data = read_list()
            new_data = {"name": product_name, "cost": product_cost}
            data.append(new_data)
            write_list(data)

    elif choice == "2":
        data = read_list()
        get_goods = input("Введіть назву: ")
        if is_name_in_goods(get_goods):
            for item in data:
                # print(item["name"])
                if get_goods == item["name"]:
                    print(f"Маємо '{get_goods}' вартістю: {item["cost"]}.")
        else:      
            print (f"Товару '{get_goods}' не знайдено.")
    else:
        print("Зробіть свій вибір вірно")