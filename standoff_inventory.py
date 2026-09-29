from inventory import Inventory
from skin import Skin
from skins import market
from player import Player

def show_market(market):
    output = "\nДобро пожаловать на рынок!\nНа данный момент рынок таков:\n\n"
    raruties = ["Nameless", "Arcane", "Legendary", "Epic", "Rare"]
    for rarity in raruties:
        output += f"{rarity}:"
        for item in market:
            if item["Rarity"] == rarity:
                output += f"\n{item['Name']} {item['Category'] if item['Category'] == 'Stattrack' else ''} - {item['Price']} голды"
        output += "\n\n"
    output = output[:-2]
    return output


def show_inventory(inventory):
    output = ""
    if not any(inventory.values()):
        return "Твой инвентарь пуст!"
    else:
        print("Твой инвентарь содержит:")
        if inventory["Nameless"]:
            output += "Из коллекции Nameless у тебя есть: "
        for i, skin in enumerate(inventory["Nameless"]):
            output += f"{inventory['Nameless'][i]}; "
        if inventory["Arcane"]:
            output += "\nИз коллекции Arcane у тебя есть: "
        for i, skin in enumerate(inventory["Arcane"]):
            output += f"{inventory['Arcane'][i]};"
        if inventory["Legendary"]:
            output += "\nИз коллекции Legendary у тебя есть: "
        for i, skin in enumerate(inventory["Legendary"]):
            output += f"{inventory['Legendary'][i]}; "
        if inventory["Epic"]:
            output += "\nИз коллекции Epic у тебя есть: "
        for i, skin in enumerate(inventory["Epic"]):
            output += f"{inventory['Epic'][i]}; "
        if inventory["Rare"]:
            output += "\nИз коллекции Rare у тебя есть: "
        for i, skin in enumerate(inventory["Rare"]):
            output += f"{inventory['Rare'][i]}; "
        return output
    
print("\nДобро пожаловать в симулятор инвентаря и рынка в стендофф 2!")
while True:
    print(
        f"\nТвой баланс составляет {balance} голды!\n"
        "1. Сыграть катку\n"
        "2. Посмотреть инвентарь\n"
        "3. Рынок\n"
        "4. Выйти"
    )
    choice = int(input("Твой выбор: "))
    output = ""
    if choice == 1:
        
    elif choice == 2:
        print(show_inventory())
    elif choice == 3:
        print(show_market(market))
    elif choice == 4:
        exit_choice = str(
            input(
                "Ты уверен, что хочешь выйти? Весь твой инвентарь будет стерт!\n"
                "Напиши 'Да'или 'Нет': "
            )
        )
        while exit_choice != "Да" and exit_choice != "Нет":
            exit_choice = str(input("Введи 'Да' или 'Нет': "))
        if exit_choice == "Да":
            print("До скорых встреч...")
            break
        else:
            print("Тогда остаешься!")
