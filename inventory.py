class Inventory:
    def __init__(self):
        self.skins = []

    def add_skin(self, skin):
        self.skins.append(skin)

    def remove_skin(self, skin):
        self.skins.remove(skin)

    def show_skins(self):
        for skin in self.skins:
            print(
                f"{skin.name} | "
                f"{skin.rarity} | "
                f"{skin.collection} | "
                f"{skin.category} | "
                f"{skin.price}"
            )
