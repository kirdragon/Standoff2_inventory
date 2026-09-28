import random


class Game:

    drop_for_game = [1000, 100, 50, 20]
    skins_drop_rarity = ["Nameless", "Arcane", "Legendary", "Epic", "Rare"]
    lucky_chances = ["skin", "gold"]
    games = ["win", "lose"]
    lucky_golds = [1000, 100, 50, 20]

    def __init__(self, player):
        self.player = player
