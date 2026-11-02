from sqlalchemy import select
from database import SessionLocal
from models import PlayerInventory, SkinRecord
from sqlalchemy.orm import selectinload


class Inventory:
    def __init__(self, player_id: int):
        self.player_id = player_id

    def add_skin(self, skin_id: int):
        with SessionLocal() as session:
            statement = select(PlayerInventory).where(
                PlayerInventory.player_id == self.player_id,
                PlayerInventory.skin_id == skin_id,
            )

            inventory_item = session.scalar(statement)

            if inventory_item:
                inventory_item.quantity += 1
            else:
                inventory_item = PlayerInventory(
                    player_id=self.player_id, skin_id=skin_id, quantity=1
                )
                session.add(inventory_item)

            session.commit()

    def remove_skin(self, skin_id: int):
        with SessionLocal() as session:
            statement = select(PlayerInventory).where(
                PlayerInventory.player_id == self.player_id,
                PlayerInventory.skin_id == skin_id,
            )

            inventory_item = session.scalar(statement)

            if not inventory_item:
                return False
            if inventory_item.quantity > 1:
                inventory_item.quantity -= 1
            else:
                session.delete(inventory_item)
            session.commit()
            return True

    def show_skins(self):
        with SessionLocal() as session:
            statement = (
                select(PlayerInventory)
                .options(
                    selectinload(PlayerInventory.skin).selectinload(SkinRecord.rarity),
                    selectinload(PlayerInventory.skin).selectinload(
                        SkinRecord.category
                    ),
                )
                .where(PlayerInventory.player_id == self.player_id)
            )

        inventory_items = session.scalars(statement).all()

        if not inventory_items:
            return "Твой инвентарь пуст!"

        output = ""
        rarities = ["Nameless", "Arcane", "Legendary", "Epic", "Rare"]

        for rarity in rarities:
            rarity_skins = [
                item for item in inventory_items if item.skin.rarity.name == rarity
            ]

            if not rarity_skins:
                continue

            output += f"\nИз {rarity} у тебя есть:\n\n"

            for i, item in enumerate(rarity_skins, 1):
                skin = item.skin

                category = "StatTrack" if skin.category.name == "StatTrack" else ""
                output += (
                    f"{i}. {skin.name} {category} "
                    f"- {skin.price} голды "
                    f"(Количество: {item.quantity})\n"
                )
        return output.rstrip()
