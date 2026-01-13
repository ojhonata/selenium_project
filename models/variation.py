from sqlalchemy.orm import mapped_column
from sqlalchemy.orm.base import Mapped
import sqlalchemy as sa
from models.model_base import ModelBase

class Variation(ModelBase):
    __tablename__ = 'variations'

    id: Mapped[int] = mapped_column(sa.BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(sa.String(50), nullable=False)
    description: Mapped[str] = mapped_column(sa.String(255), nullable=False)