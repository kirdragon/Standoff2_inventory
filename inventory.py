from skin import Skin


class Inventory:
    def __init__(self):
        self.skins: list[Skin] = []

    def add_skin(self, skin: Skin):
        self.skins.append(skin)

    def remove_skin(self, skin: Skin):
        self.skins.remove(skin)

    def show_skins(self):
        if not self.skins:
            return "Твой инвентарь пуст!"

        output = ""
        rarities = ["Nameless", "Arcane", "Legendary", "Epic", "Rare"]

        for rarity in rarities:
            rarity_skins = [skin for skin in self.skins if skin.rarity == rarity]

            if not rarity_skins:
                continue

            output += f"\nИз {rarity} у тебя есть:\n\n"

            for i, skin in enumerate(rarity_skins, 1):
                category = "StatTrack" if skin.category == "StatTrack" else ""

                output += f"{i}. {skin.name} {category} " f"- {skin.price} голды\n"

        return output.rstrip()
