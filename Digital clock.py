import time
from datetime import datetime
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear_screen()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%d-%m-%Y")
    print(" Digital Clock")
    print("-------------------------")
    print(f"Date: {current_date}")
    print(f"Time: {current_time}")
    print("-------------------------")
    time.sleep(1)
