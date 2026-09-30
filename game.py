import random
from skins import market

from player import Player


class Game:

    drop_for_game = [1000, 100, 50, 20]
    skins_drop_rarity = ["Nameless", "Arcane", "Legendary", "Epic", "Rare"]
    lucky_chances = ["skin", "gold"]
    games = ["win", "lose"]
    lucky_golds = [1000, 100, 50, 20]
    categories = ["regular", "stattrack", "knife"]
    answer = ""

    def __init__(self, player: Player):
        self.player = player

    def play(self):
        result = random.choices(self.games, weights=[75, 25])[0]
        if result == "lose":
            game_drop = random.choices(self.drop_for_game, weights=[1, 4, 15, 80])[0]
            self.player.add_money(game_drop)
            self.answer += f"Ты проиграл, за свою игру получаешь {game_drop} голды\n"
        else:
            game_drop = random.choices(self.drop_for_game, weights=[2, 8, 20, 80])[0]
            self.player.add_money(game_drop)
            self.answer += f"Ты выиграл, за свою игру получаешь {game_drop} голды\n"

        lucky_drop = random.choices(self.lucky_chances, weights=[20, 80])[0]
        if lucky_drop == "skin":
            lucky_skin = random.choices(
                self.skins_drop_rarity, weights=[5, 10, 15, 20, 50]
            )[0]
            if lucky_skin == "Nameless":
                nameless_skin = random.choice(market[:4])
                self.player.inventory.add_skin(nameless_skin)
                self.answer += f"За удачу ты получаешь {nameless_skin}!"
                return self.answer

            elif lucky_skin == "Arcane":
                arcane_category = random.choices(self.categories, weights=[70, 20, 10])[
                    0
                ]
                if arcane_category == "regular":
                    arcane_skin = random.choice(market[6], market[12])
                    self.player.inventory.add_skin(arcane_skin)
                    self.answer += f"За удачу ты получаешь {arcane_skin}!"
                    return self.answer

                elif arcane_category == "stattrack":
                    arcane_skin = random.choice(market[5], market[11])
                    self.player.inventory.add_skin(arcane_skin)
                    self.answer += f"За удачу ты получаешь {arcane_skin}!"
                    return self.answer

                else:
                    arcane_skin = random.choice(market[10:7])
                    self.player.inventory.add_skin(arcane_skin)
                    self.answer += f"За удачу ты получаешь {arcane_skin}!"
                    return self.answer

            elif lucky_skin == "Legendary":
                legendary_category = random.choices(
                    self.categories[:2], weights=[80, 20]
                )[0]
                if legendary_category == "regular":
                    legendary_skin = random.choice(market[14], market[16], market[18])
                    self.answer += f"За удачу ты получаешь {legendary_skin}!"
                    return self.answer
                else:
                    legendary_skin = random.choice(market[13], market[15], market[17])
                    self.answer += f"За удачу ты получаешь {legendary_skin}!"
                    return self.answer

            elif lucky_skin == "Epic":
                epic_category = random.choices(self.categories[:2], weights=[80, 20])[0]
                if epic_category == "regular":
                    epic_skin = random.choice(market[19:24])
                    self.answer += f"За удачу ты получаешь {epic_skin}!"
                    return self.answer

            elif lucky_skin == "Rare":
                self.skins_drop_rarity["Rare"].append("М40 Грип")

        if lucky_drop == "gold":
            golds_amount = random.choices(self.lucky_golds, weights=[3, 7, 30, 60])[0]
            self.player.add_money(golds_amount)
