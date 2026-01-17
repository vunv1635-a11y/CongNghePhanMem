from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from infrastructure.databases.mssql import Base

class MedicalInfo(Base):
    __tablename__ = 'medical_info'
    __table_args__ = {'extend_existing': True}  # Thêm dòng này

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    blood_type = Column(String(3), nullable=True)
    has_diabetes = Column(Integer, default=0)  # 0: No, 1: Yes
    has_hypertension = Column(Integer, default=0)  # 0: No, 1: Yes
    other_conditions = Column(String(255), nullable=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)