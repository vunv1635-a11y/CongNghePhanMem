from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from infrastructure.databases.mssql import Base

class NotificationModel(Base):
    __tablename__ = 'notifications'
    __table_args__ = {'extend_existing': True}  # Thêm dòng này

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    message = Column(String(500), nullable=False)
    level = Column(String(50), nullable=False)  # e.g., info, warning, error
    is_read = Column(Integer, default=0)  # 0 for unread, 1 for read
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    
def send_notification(user_id: int, message: str, level: str):
    """Hàm gửi thông báo đến người dùng."""
    notification = NotificationModel(
        user_id=user_id,
        message=message,
        level=level,
        is_read=0
    )
    # Logic để lưu notification vào database ở đây
    return notification