from datetime import datetime

from sqlalchemy import DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

# this base class is used to create the database models. It is inherited by all the models in the app/models directory. It is used to create the tables in the database.

class Base(DeclarativeBase):
    pass

# A mixin is a small class you inherit from to reuse fields. Any model that inherits TimestampMixin gets created_at and updated_at.

class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()  # this makes it update the time when anything changes
    )

# server_default=func.now() makes the database fill in the time when a row is inserted (more reliable than Python doing it). onupdate=func.now() refreshes updated_at on every update. timezone=True stores timezone-aware times, which avoids bugs when servers and users are in different zones.