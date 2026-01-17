from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, DECIMAL
from infrastructure.databases.mssql import Base

class Subscription(Base):
    __tablename__ = 'subscriptions'
    __table_args__ = {'extend_existing': True}  # Thêm dòng này

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    clinic_id = Column(Integer, ForeignKey('clinics.id'))
    package_name = Column(String(100), nullable=False)
    analysis_count = Column(Integer, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    is_active = Column(Integer, default=1)  # 0: Inactive, 1: Active
    created_at = Column(DateTime)
    updated_at = Column(DateTime)