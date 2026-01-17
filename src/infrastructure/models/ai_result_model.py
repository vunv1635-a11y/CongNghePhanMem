from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from infrastructure.databases.mssql import Base

class AIResult(Base):
    __tablename__ = 'ai_results'
    __table_args__ = {'extend_existing': True}  # Thêm dòng này

    id = Column(Integer, primary_key=True)
    analysis_id = Column(Integer, ForeignKey('analyses.id'))
    risk_level = Column(String(50), nullable=False)  # e.g., low, medium, high
    confidence_score = Column(Integer, nullable=True)  # Confidence score as a percentage
    summary = Column(String(500), nullable=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)