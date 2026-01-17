from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from infrastructure.databases.mssql import Base

class DoctorNote(Base):
    __tablename__ = 'doctor_notes'
    __table_args__ = {'extend_existing': True}  # Thêm dòng này

    id = Column(Integer, primary_key=True)
    analysis_id = Column(Integer, ForeignKey('analyses.id'))
    doctor_id = Column(Integer, ForeignKey('doctors.id'))
    note_content = Column(String(1000), nullable=False)
    diagnosis = Column(String(500), nullable=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)