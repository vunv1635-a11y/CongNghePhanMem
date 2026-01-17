from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from infrastructure.databases.mssql import Base

class Risk(Base):
    __tablename__ = 'risks'
    __table_args__ = {'extend_existing': True}  # Thêm dòng này

    id = Column(Integer, primary_key=True)
    ai_result_id = Column(Integer, ForeignKey('ai_results.id'))
    risk_type = Column(String(100), nullable=False)  # e.g., cardiovascular, diabetes
    risk_level = Column(String(50), nullable=False)  # e.g., low, medium, high
    percentage = Column(Integer, nullable=True)  # Risk percentage
    recommendations = Column(String(500), nullable=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)