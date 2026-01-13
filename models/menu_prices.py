import sqlalchemy.orm as orm
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm.base import Mapped
import sqlalchemy as sa
from models.model_base import ModelBase
from models.product import Product
from models.variation import Variation

class MenuPrice(ModelBase):
    __tablename__ = 'menu_price'

    id: Mapped[int] = mapped_column(sa.BigInteger, primary_key=True, autoincrement=True)

    id_product: Mapped[int] = mapped_column(sa.BigInteger, sa.ForeignKey('products.id', ondelete='CASCADE'))
    product: Mapped['Product'] = orm.relationship('Product', lazy='joined')

    id_variation: Mapped[int] = mapped_column(sa.BigInteger, sa.ForeignKey('variations.id', ondelete='CASCADE'))
    variation: Mapped['Variation'] = orm.relationship('Variation', lazy='joined')

    price: Mapped[float] = mapped_column(sa.Numeric(10, 2), nullable=True)