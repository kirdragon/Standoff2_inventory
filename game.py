import random
from skin import Skin
from player import Player


class Game:

    drop_for_game = [1000, 100, 50, 20]
    skins_drop_rarity = ["Nameless", "Arcane", "Legendary", "Epic", "Rare"]
    lucky_chances = ["Skin", "Gold"]
    games = ["Win", "Lose"]
    lucky_golds = [1000, 100, 50, 20]
    categories = ["Regular", "StatTrack", "Knife"]

    def __init__(self, player: Player, market: list[Skin]):
        self.player = player
        self.market = market
        self.answer = ""

    def _get_game_result(self):
        return random.choices(self.games, weights=[75, 25])[0]

    def _get_skin_rarity(self):
        return random.choices(self.skins_drop_rarity, weights=[5, 10, 15, 20, 50])[0]

    def _get_skin_category(self, rarity):
        if rarity == "Arcane":
            category = random.choices(self.categories, weights=[70, 20, 10])[0]
        elif rarity == "Nameless":
            category = "Regular"
        else:
            category = random.choices(self.categories[:2], weights=[80, 20])[0]
        return category

    def _get_luck_type_drop(self):
        return random.choices(self.lucky_chances, weights=[25, 75])[0]

    def _get_game_gold_drop(self, game_result):
        if game_result == "Lose":
            game_drop = random.choices(self.drop_for_game, weights=[1, 4, 15, 80])[0]
        else:
            game_drop = random.choices(self.drop_for_game, weights=[2, 8, 20, 70])[0]
        return game_drop

    def _get_luck_gold_drop(self):
        return random.choices(self.lucky_golds, weights=[3, 7, 30, 60])[0]

    def _get_specific_skin(self, category, rarity):
        skins_list = []

        for skin in self.market:
            if skin.category == category and skin.rarity == rarity:
                skins_list.append(skin)

        return random.choice(skins_list)

    def play(self):
        self.answer = ""
        game_result = self._get_game_result()
        game_drop = self._get_game_gold_drop(game_result)
        self.player.add_money(game_drop)
        if game_result == "Lose":
            self.answer += f"Ты проиграл, и за свою игру получаешь {game_drop} голды!\n"
        else:
            self.answer += f"Ты выиграл, и за свою игру получаешь {game_drop} голды!\n"
        luck_type_drop = self._get_luck_type_drop()
        if luck_type_drop == "Gold":
            luck_drop: int = self._get_luck_gold_drop()
            self.player.add_money(luck_drop)
            self.answer += f"За удачу ты получаешь {luck_drop} голды!"
        else:
            skin_rarity = self._get_skin_rarity()
            skin_category = self._get_skin_category(skin_rarity)
            luck_drop: Skin = self._get_specific_skin(skin_category, skin_rarity)
            self.player.inventory.add_skin(luck_drop)
            self.answer += f"За удачу ты получаешь {luck_drop.name} {luck_drop.category if luck_drop.category == "StatTrack" else ''}"
        return self.answer
