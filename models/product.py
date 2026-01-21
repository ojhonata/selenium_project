import sqlalchemy as sa
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm.base import Mapped

from models.model_base import ModelBase


class Product(ModelBase):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(sa.BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(sa.String(50), nullable=False)
    category: Mapped[str] = mapped_column(sa.String(50), nullable=False)
