import time
from datetime import datetime

while True:
    t = datetime.now().strftime('%H:%M:%S')
    print(t, end='\r')
    time.sleep(1)
  
