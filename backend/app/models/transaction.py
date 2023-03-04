
from sqlalchemy import Column, Boolean, Integer, String, DateTime, Numeric, Text
from sqlalchemy.orm import relationship

from app.database import Base


class Transaction(Base):
    id = Column(Integer, primary_key=True, index=True)
    creation_date = Column(DateTime, nullable=False, index=True)
    payment_date = Column(DateTime, nullable=True)
    amount = Column(Numeric(precision=10, scale=2), nullable=False)
    description = Column(Text, nullable=False)
    currency = Column(String(3), nullable=False)
    category = Column(String(3), nullable=False)
    payment_method = Column(String(3), nullable=False)
    is_egress = Column(Boolean, nullable=False)
