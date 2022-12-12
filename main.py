import time
from plyer import notification

print("О чём вам напомнить?:")
a = str(input())

print("Через сколько минут?:")
local_time = float(input())

local_time = local_time * 60
time.sleep(local_time)

notification.notify(message=a, app_name='script', title='Уведомление:', app_icon="2.ico")


