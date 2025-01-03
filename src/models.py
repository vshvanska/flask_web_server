from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from .database import Base
from.enums import VerdictEnum


class SourceRecord(Base):
    __tablename__ = "sources"

    id: Mapped[int] = mapped_column(primary_key=True)
    domain: Mapped[str] = mapped_column(String(150), nullable=False)
    verdict: Mapped[VerdictEnum]
