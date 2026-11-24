from sqlalchemy import CheckConstraint, ForeignKey, Integer, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.product import Product


class CartItem(Base):
    __tablename__ = "cart_items"
    __table_args__ = (
        UniqueConstraint("user_id", "product_id", name="one_row_per_product"),
        CheckConstraint("quantity > 0", name="qty_positive"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), index=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id", ondelete="CASCADE"))
    quantity: Mapped[int] = mapped_column(Integer)
    product: Mapped[Product] = relationship(lazy="joined")


#     UniqueConstraint("user_id", "product_id") means a user can have only one row per product; adding the same product again must increase the quantity, not create a duplicate.
# The CHECK rule keeps quantity above zero. Cascade deletes remove cart rows when the user or product is deleted.
# lazy="joined" tells SQLAlchemy to load the product in the same query as the cart item. In async code you cannot load related data on demand later, so you must say how to load it upfront.
