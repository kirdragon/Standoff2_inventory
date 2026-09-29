import random

from player import Player


class Game:

    drop_for_game = [1000, 100, 50, 20]
    skins_drop_rarity = ["Nameless", "Arcane", "Legendary", "Epic", "Rare"]
    lucky_chances = ["skin", "gold"]
    games = ["win", "lose"]
    lucky_golds = [1000, 100, 50, 20]

    def __init__(self, player: Player):
        self.player = player

    def play(self):
        result = random.choices(self.games, weights=[75, 25])[0]
        if result == "lose":
            game_drop = random.choices(self.drop_for_game, weights=[1, 4, 15, 80])[0]
            self.player.add_money(game_drop)
        else:
            game_drop = random.choices(self.drop_for_game, weights=[2, 8, 20, 80])[0]
            self.player.add_money(game_drop)

        lucky_drop = random.choices(self.lucky_chances, weights=[20, 80])[0]
        if lucky_drop == "skin":
            lucky_skin = random.choices(
                self.skins_drop_rarity, weights=[5, 10, 15, 20, 50]
            )[0]
            if lucky_skin == "Nameless":
                self.skins_drop_rarity["Nameless"].append("Кер Голд")

            elif lucky_skin == "Arcane":
                self.skins_drop_rarity["Arcane"].append("М4 Самурай")

            elif lucky_skin == "Legendary":
                self.skins_drop_rarity["Legendary"].append("АКР Некромансер")

            elif lucky_skin == "Epic":
                self.skins_drop_rarity["Epic"].append("Фнфал Тактикал")

            elif lucky_skin == "Rare":
                self.skins_drop_rarity["Rare"].append("М40 Грип")

        if lucky_drop == "gold":
            golds_amount = random.choices(self.lucky_golds, weights=[3, 7, 30, 60])[0]
            if golds_amount == 1000:
                balance += self.lucky_golds[0]

            elif golds_amount == 100:
                balance += self.lucky_golds[1]

            elif golds_amount == 50:
                balance += self.lucky_golds[2]

            else:
                balance += self.lucky_golds[3]
