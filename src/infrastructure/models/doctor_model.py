from sqlalchemy import Column, Integer, String, Boolean, DateTime
from infrastructure.databases.mssql import Base

class Doctor(Base):
    __tablename__ = 'doctors'
    __table_args__ = {'extend_existing': True}  # Thêm dòng này

    id = Column(Integer, primary_key=True)
    clinic_id = Column(Integer, nullable=False)
    name = Column(String(100), nullable=False)
    specialty = Column(String(100), nullable=False)
    license_number = Column(String(50), unique=True, nullable=False)
    phone = Column(String(20), nullable=True)
    email = Column(String(120), nullable=True)
    is_active = Column(Boolean, default=True)  # 0: Inactive, 1: Active
    created_at = Column(DateTime)
    updated_at = Column(DateTime)