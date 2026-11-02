from sqlalchemy import select
from sqlalchemy.orm import selectinload

from database import SessionLocal
from models import SkinRecord


def load_market() -> list[SkinRecord]:
    with SessionLocal() as session:
        statement = select(SkinRecord).options(
            selectinload(SkinRecord.rarity),
            selectinload(SkinRecord.collection),
            selectinload(SkinRecord.category),
        )
        records = session.scalars(statement).all()

        return records


def get_skin_by_name(name: str) -> list[SkinRecord] | None:
    with SessionLocal() as session:
        statement = (
            select(SkinRecord)
            .options(
                selectinload(SkinRecord.rarity),
                selectinload(SkinRecord.collection),
                selectinload(SkinRecord.category),
            )
            .where(SkinRecord.name == name)
        )

        skins = session.scalars(statement).all()

        if not skins:
            return None

        return skins
