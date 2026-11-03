from sqlalchemy import select

from database import SessionLocal
from models import Player as PlayerModel
from inventory import Inventory


class Player:
    def __init__(self, player_id: int):
        self.id = player_id
        self.inventory = Inventory(player_id)

    @property
    def gold(self):
        with SessionLocal() as session:
            player = session.get(PlayerModel, self.id)
            return player.gold

    def add_money(self, amount):
        with SessionLocal() as session:
            player = session.get(PlayerModel, self.id)
            player.gold += amount
            session.commit()

    def spend_money(self, amount):
        with SessionLocal() as session:
            player = session.get(PlayerModel, self.id)

            if player.gold >= amount:
                player.gold -= amount
                session.commit()
                return True
            return False


def get_or_create_player(username: str) -> int:
    with SessionLocal() as session:
        statement = select(PlayerModel).where(PlayerModel.username == username)
        player = session.scalar(statement)

        is_new = False

        if player is None:
            player = PlayerModel(username=username, gold=0)
            session.add(player)
            session.commit()
            is_new = True

        return player.id, is_new
