import json
import os
from infrastructure.models.notification.notification_model import NotificationModel

FILE_NAME = "notifications.json"
def save_notification(notification:NotificationModel):
    """Lưu thông báo vào file JSON."""
    notification_data = {
        "id": notification.id,
        "user_id": notification.user_id,
        "message": notification.message,
        "level": notification.level,
        "is_read": notification.is_read,
        "created_at": notification.created_at.isoformat() if notification.created_at else None,
        "updated_at": notification.updated_at.isoformat() if notification.updated_at else None,
    }

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            data = json.load(file)
    else:
        data = []

    data.append(notification_data)

    with open(FILE_NAME, 'w') as file:
        json.dump(data, file, indent=4)