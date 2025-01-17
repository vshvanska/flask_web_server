from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from .database import Base
from .enums import VerdictEnum


class SourceRecord(Base):
    __tablename__ = "sources"

    domain: Mapped[str] = mapped_column(String(150), nullable=False, primary_key=True)
    verdict: Mapped[VerdictEnum]
