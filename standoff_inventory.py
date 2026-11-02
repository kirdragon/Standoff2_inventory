from market import load_market, get_skin_by_name
from player import Player, get_or_create_player
from game import Game
from models import SkinRecord

market = load_market()

player_id = get_or_create_player("Роман")
player = Player(player_id)

game = Game(player, market)


def getYesorNo(message):
    print(message)

    while True:
        choice = input().strip()

        if choice not in ("Да", "Нет"):
            print('Введи либо "Да", либо "Нет"')
        else:
            return choice


def getString(message):
    while True:
        value = input(message).strip()

        if value:
            return value

        print("Ошибка! Значение не может быть пустым!")


def getInt(message, min_value, max_value):
    while True:
        try:
            value = int(input(message))

            if min_value <= value <= max_value:
                return value

            print(f"Ошибка! Введи число от {min_value} до {max_value}:")

        except ValueError:
            print(f"Ошибка! Введи целое число от {min_value} до {max_value}:")


def show_market(market: list[SkinRecord]):
    output = "\nДобро пожаловать на рынок!\nНа данный момент рынок таков:\n\n"

    rarities = ["Nameless", "Arcane", "Legendary", "Epic", "Rare"]

    for rarity in rarities:
        output += f"{rarity}:"

        for item in market:
            if item.rarity.name == rarity:
                category = "StatTrack" if item.category.name == "StatTrack" else ""

                output += f"\n{item.name} {category} " f"- {item.price} голды"

        output += "\n\n"

    return output.rstrip()


print("\nДобро пожаловать в симулятор инвентаря и рынка в Standoff 2!")

while True:
    print(
        f"\nТвой баланс составляет {player.gold} голды!\n"
        "1. Сыграть катку\n"
        "2. Посмотреть инвентарь\n"
        "3. Рынок\n"
        "4. Купить скин\n"
        "5. Продать скин\n"
        "6. Выйти"
    )

    choice = getInt("Выбор: ", 1, 6)

    if choice == 1:
        print(game.play())

    elif choice == 2:
        print(player.inventory.show_skins())

    elif choice == 3:
        print(show_market(market))

    elif choice == 4:
        print(show_market(market))

        name = getString("Напиши название скина, который хочешь купить: ")

        skins = get_skin_by_name(name)

        if skins is None:
            print("Скина с таким названием нет. " "Пиши его точь-в-точь как на рынке.")

        elif len(skins) == 1:
            skin = skins[0]

            category = "StatTrack" if skin.category.name == "StatTrack" else ""

            print(
                f"Найден {skin.rarity.name} {skin.name} {category} "
                f"со стоимостью {skin.price} голды"
            )

            if player.gold < skin.price:
                print("Но у тебя недостаточно голды для покупки.")

            else:
                purchase_choice = getYesorNo("Ты уверен, что хочешь его купить?")

                if purchase_choice == "Да":
                    if player.spend_money(skin.price):
                        player.inventory.add_skin(skin.id)
                        print("Скин куплен!")
                    else:
                        print("Не удалось совершить покупку.")

                else:
                    print("Тогда пока!")

        else:
            print("Найдены следующие скины:\n")

            for i, skin in enumerate(skins, 1):
                category = "StatTrack" if skin.category.name == "StatTrack" else ""

                print(
                    f"{i}. {skin.rarity.name} {skin.name} {category} "
                    f"со стоимостью {skin.price} голды\n"
                )

            player_choice = getInt(
                "Какой скин ты хочешь выбрать? Напиши цифру: ", 1, len(skins)
            )

            skin = skins[player_choice - 1]

            if player.gold < skin.price:
                print("Но у тебя недостаточно голды для покупки.")

            else:
                purchase_choice = getYesorNo("Ты уверен, что хочешь его купить?")

                if purchase_choice == "Да":
                    if player.spend_money(skin.price):
                        player.inventory.add_skin(skin.id)
                        print("Скин куплен!")
                    else:
                        print("Не удалось совершить покупку.")

                else:
                    print("Тогда пока!")

    elif choice == 5:
        print(player.inventory.show_skins())
        print("Продажа скинов пока не реализована.")

    elif choice == 6:
        exit_choice = getYesorNo(
            "Ты уверен, что хочешь выйти? Твой прогресс будет сохранён!\n"
            'Напиши "Да" или "Нет": '
        )

        if exit_choice == "Да":
            print("До скорых встреч...")
            break

        else:
            print("Тогда остаёшься!")
