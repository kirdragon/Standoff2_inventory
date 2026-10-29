from skin import Skin
from skins import market
from player import Player

player = Player("Роман", 0)


def getString(message):
    while True:
        value = input(message).strip()
        if value:
            return value
        print("Ошибка! Значение не может быть пустым!")


def getInt(message, min, max):
    while True:
        try:
            value_input = int(input(message))
            if min <= value_input <= max:
                return value_input
            print(f"Ошибка! Введи число от {min} до {max}:")
        except ValueError:
            print(f"Ошибка! Введи целое число от {min} до {max}:")


def show_market(market: list[Skin]):
    output = "\nДобро пожаловать на рынок!\nНа данный момент рынок таков:\n\n"
    raruties = ["Nameless", "Arcane", "Legendary", "Epic", "Rare"]
    for rarity in raruties:
        output += f"{rarity}:"
        for item in market:
            if item.rarity == rarity:
                output += f"\n{item.name} {item.category if item.category == 'Stattrack' else ''} - {item.price} голды"
        output += "\n\n"
    output = output[:-2]
    return output


print("\nДобро пожаловать в симулятор инвентаря и рынка в стендофф 2!")
while True:
    print(
        f"\nТвой баланс составляет {player.balance} голды!\n"
        "1. Сыграть катку\n"
        "2. Посмотреть инвентарь\n"
        "3. Рынок\n"
        "4. Выйти"
    )
    choice = getInt("Выбор: ", 1, 4)
    output = ""
    if choice == 1:
        pass
    elif choice == 2:
        print(player.inventory.show_skins())
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
