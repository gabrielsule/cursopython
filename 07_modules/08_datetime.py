from datetime import datetime
import time

dt = datetime.fromtimestamp(time.time())
print(dt)
print(f"{dt.day}")