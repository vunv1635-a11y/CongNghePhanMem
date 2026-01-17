from sqlalchemy import Column, Integer, String, DateTime
from infrastructure.databases.mssql import Base

class Analysis(Base):
    __tablename__ = 'analyses'
    __table_args__ = {'extend_existing': True}  # Thêm dòng này

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    doctor_id = Column(Integer, nullable=False)
    clicnic_id = Column(Integer, nullable=False)
    eye_type = Column(String(50), nullable=False)
    status = Column(String(20), nullable=False, default='pending')  # pending, completed, canceled
    upload_time = Column(DateTime, nullable=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)