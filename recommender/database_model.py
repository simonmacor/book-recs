import sqlalchemy as sa
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    username: Mapped[str] = mapped_column(sa.String(100), nullable=False)
    email: Mapped[str] = mapped_column(sa.String(255), nullable=True)

    # Relation avec la table Preferences (un utilisateur peut avoir plusieurs préférences)
    preferences: Mapped["Preference"] = relationship("Preference", back_populates="user", cascade="all, delete-orphan")


class Book(Base):
    __tablename__ = 'books'

    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    title: Mapped[str] = mapped_column(sa.String(50), nullable=False)
    author: Mapped[str] = mapped_column(sa.String(200), nullable=False)
    theme: Mapped[str] = mapped_column(sa.String(200), nullable=False)
    period: Mapped[str] = mapped_column(sa.String(200), nullable=False)
    style: Mapped[str] = mapped_column(sa.String(200), nullable=False)


class Preference(Base):
    __tablename__ = 'preferences'

    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(sa.ForeignKey("users.id"), nullable=False)
    theme: Mapped[str] = mapped_column(sa.String(200), nullable=False)
    period: Mapped[str] = mapped_column(sa.String(200), nullable=False)
    style: Mapped[str] = mapped_column(sa.String(200), nullable=False)

    # Relation avec la table User (chaque préférence appartient à un utilisateur)
    user: Mapped["User"] = relationship("User", back_populates="preferences")
