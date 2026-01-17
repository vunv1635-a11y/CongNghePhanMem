from sqlalchemy import Column, Integer, String, DateTime, Boolean
from infrastructure.databases.mssql import Base

class Clinic(Base):
    __tablename__ = 'clinics'
    __table_args__ = {'extend_existing': True}  # Thêm dòng này

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    address = Column(String(255), nullable=False)
    license_number = Column(String(50), unique=True, nullable=False)
    phone = Column(String(20), nullable=True)
    email = Column(String(120), nullable=True)
    is_verified = Column(Boolean, default=False)  # 0: No, 1: Yes
    credits = Column(Integer, default=0)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)