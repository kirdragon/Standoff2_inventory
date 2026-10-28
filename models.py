from sqlalchemy import String, Float, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Player(Base):
    __tablename__ = "Players"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String)
    gold: Mapped[float] = mapped_column(Float)


class Rarity(Base):
    __tablename__ = "Rarities"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)


class Category(Base):
    __tablename__ = "Categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)


class Collection(Base):
    __tablename__ = "Collections"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)


class SkinRecord(Base):
    __tablename__ = "Skins"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    price: Mapped[int] = mapped_column()

    rarity_id: Mapped[int] = mapped_column(ForeignKey("Rarites.id"))
    collection_id: Mapped[int] = mapped_column(ForeignKey("Collections.id"))
    category_id: Mapped[int] = mapped_column(ForeignKey("Categories.id"))

    rarity: Mapped[Rarity] = relationship()
    collection: Mapped[Collection] = relationship()
    category: Mapped[Category] = relationship()
