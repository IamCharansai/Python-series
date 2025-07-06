import time
from tqdm import tqdm

def countdown_timer(seconds):
    print(f"\n Countdown Started for {seconds} seconds:\n")
    for _ in tqdm(range(seconds), desc="Time Remaining", unit="sec"):
        time.sleep(1)
    print("\n Time's up!")

try:
    secs = int(input("Enter countdown time in seconds: "))
    countdown_timer(secs)
except ValueError:
    print(" Please enter a valid number.")
