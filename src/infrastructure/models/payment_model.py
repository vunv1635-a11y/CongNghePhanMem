from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from infrastructure.databases.mssql import Base

class Payment(Base):
    __tablename__ = 'payments'
    __table_args__ = {'extend_existing': True}  # Thêm dòng này

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    subscription_id = Column(Integer, ForeignKey('subscriptions.id'))
    amount = Column(Integer, nullable=False)
    payment_method = Column(String(50), nullable=False)
    status = Column(String(20), nullable=False, default='pending')  # pending, completed, failed
    payment_date = Column(DateTime, nullable=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)