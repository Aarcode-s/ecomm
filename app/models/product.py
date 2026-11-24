from sqlalchemy import Boolean, CheckConstraint, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base, TimestampMixin


class Category(Base):
    __tablename__ = "categories"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(80), unique=True)

    # back populates connects the relationship between the Category and Product models. It allows us to access the products of a category using category.products and the category of a product using product.category.

    products: Mapped[list["Product"]] = relationship(back_populates="category")


class Product(Base, TimestampMixin):
    __tablename__ = "products"

    # constraints for products to be saved into this table

    __table_args__ = (
        CheckConstraint("price_paise >= 0", name="price_non_negative"),
        CheckConstraint("stock >= 0", name="stock_non_negative"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)

    # index = True make the name a searchable entity in the database. This is useful for searching products by name.

    name: Mapped[str] = mapped_column(String(200), index=True)
    description: Mapped[str] = mapped_column(Text, default="")
    price_paise: Mapped[int] = mapped_column(Integer)
    stock: Mapped[int] = mapped_column(Integer, default=0)
    image_url: Mapped[str | None] = mapped_column(String(500))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    # ondelete="SET NULL" means deleting a category does not delete its products; they just lose the category.

    category_id: Mapped[int | None] = mapped_column(ForeignKey("categories.id", ondelete="SET NULL"))
    category: Mapped[Category | None] = relationship(back_populates="products")


    # relationship() lets you write product.category in Python without writing a join. back_populates connects the two sides so category.products also works.
    # Mapped[str | None] means the column is optional (NULL allowed). Text is for long strings; String(200) has a maximum length.
    # is_active supports "soft delete": hide a product instead of removing it, so old orders still make sense.
