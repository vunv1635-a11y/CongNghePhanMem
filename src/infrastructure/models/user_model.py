from sqlalchemy import Column, Integer, String, DateTime
from infrastructure.databases.mssql import Base
class User(Base): 
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}  # Thêm dòng này
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    phone = Column(String(20), unique=True, nullable=True)
    password_hash = Column(String(128), nullable=False)
    date_of_birth = Column(DateTime, nullable=True)
    role = Column(String(20), nullable=False, default='user')
    is_active = Column(Integer, default=1)
    credits = Column(Integer, default=0)
    create_at = Column(DateTime)
    update_at = Column(DateTime)
    
    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"