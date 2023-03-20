from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(
            title = " TAKE REST ",
            message = "Rest is vital for the better mental health",
            app_icon = "Rest.ico",
            timeout = 5)
        time.sleep(10)

#if you run this in the backgound pythonw Notifier.py (pythonw filename.py)