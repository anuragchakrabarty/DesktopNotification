from plyer import notification
import time

title = "Reminder"
message = "Take a short break and stretch"

notification.notify(
    title=title,
    message=message,
    timeout=5
)

time.sleep(1)