import random

market = [
    [
        {
            "Name": "Karambit Gold",
            "Rarity": "Nameless",
            "Collection": "Nameless",
            "Price": 150000,
        },
        {
            "Name": "AWM treasure Hunter",
            "Rarity": "Nameless",
            "Collection": "Nameless",
            "Price": 110000,
        },
        {
            "Name": "AWM Sport V2",
            "Rarity": "Nameless",
            "Collection": "Nameless",
            "Price": 80000,
        },
        {
            "Name": "USP Genesis",
            "Rarity": "Nameless",
            "Collection": "Nameless",
            "Price": 55000,
        },
        {
            "Name": "G22",
            "Rarity": "Nameless",
            "Collection": "Nameless",
            "Price": 38000,
        },
    ]
]
inventory = {
    "Nameless": [],
    "Arcane": [],
    "Legendary": [],
    "Epic": [],
    "Rare": [],
}
drop_for_game = [1000, 100, 50, 20]
balance = 0
skins_drop_rarity = ["Nameless", "Arcane", "Legendary", "Epic", "Rare"]
lucky_chances = ["skin", "golds"]
games = ["win", "lose"]
lucky_golds = [1000, 100, 50, 20]
print("\nДобро пожаловать в симулятор инвентаря и рынка в стендофф 2!")
while True:
    print(
        f"\nТвой баланс составляет {balance} голды!\n"
        "1. Сыграть катку\n"
        "2. Посмотреть инвентарь\n"
        "3. Выйти"
    )
    choice = int(input("Твой выбор: "))
    output = ""
    if choice == 1:
        ind = random.choices(games, weights=[75, 25])[0]

        if ind == "lose":
            game_drop = random.choices(drop_for_game, weights=[1, 4, 15, 80])[0]
            balance += game_drop
            print(f"Ты проиграл! За свою игру ты получаешь: {game_drop} голды")
        else:
            game_drop = random.choices(drop_for_game, weights=[2, 8, 20, 80])[0]
            balance += game_drop
            print(f"Ты выиграл! За свою игру ты получаешь: {game_drop} голды")
        lucky_drop = random.choices(lucky_chances, weights=[20, 80])[0]
        if lucky_drop == "skin":
            lucky_skin = random.choices(skins_drop_rarity, weights=[5, 10, 15, 20, 50])[
                0
            ]
            if lucky_skin == "Nameless":
                inventory["Nameless"].append("Кер Голд")
                print("ААААА ТЕБЕ ВЫПАЛ КЕР ГОЛД!!!")

            elif lucky_skin == "Arcane":
                inventory["Arcane"].append("М4 Самурай")
                print("Поздравляю! Тебе выпала аркана за удачу!")

            elif lucky_skin == "Legendary":
                inventory["Legendary"].append("АКР Некромансер")
                print("Поздравляю! Тебе выпал Некромансер за удачу!")

            elif lucky_skin == "Epic":
                inventory["Epic"].append("Фнфал Тактикал")
                print("Поздравляю! Тебе выпал Фнфал тактикал за удачу!")

            elif lucky_skin == "Rare":
                inventory["Rare"].append("М40 Грип")
                print("Лох, тебе выпал м 40 грип")
        if lucky_drop == "golds":
            golds_amount = random.choices(lucky_golds, weights=[3, 7, 30, 60])[0]
            if golds_amount == 1000:
                balance += lucky_golds[0]
                print(f"За удачу ты получаешь: {golds_amount} голды")
            elif golds_amount == 100:
                balance += lucky_golds[1]
                print(f"За удачу ты получаешь: {golds_amount} голды")
            elif golds_amount == 50:
                balance += lucky_golds[2]
                print(f"За удачу ты получаешь: {golds_amount} голды")
            else:
                balance += lucky_golds[3]
                print(f"За удачу ты получаешь: {golds_amount} голды")
    elif choice == 2:
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

        print(output)
    elif choice == 3:
        exit_choice = str(
            input("Ты уверен, что хочешь выйти? Весь твой инвентарь будет стерт!\n")
        )
        if exit_choice == "да" or exit_choice == "Да":
            print("До скорых встреч...")
            break
        else:
            print("Тогда остаешься!")
