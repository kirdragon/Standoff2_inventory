from sqlalchemy import select

from database import SessionLocal
from models import SkinRecord
from skin import Skin


def load_market() -> list[Skin]:
    with SessionLocal() as session:
        statement = select(SkinRecord)
        records = session.scalars(statement).all()

        market = []

        for record in records:
            skin = Skin(
                record.name,
                record.rarity.name,
                record.collection.name,
                record.category.name,
                record.price,
            )

            market.append(skin)

        return market
