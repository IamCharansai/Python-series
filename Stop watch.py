import time

def stopwatch():
    print(" Simple Stopwatch")
    print("Press ENTER to start")
    input()
    start_time = time.time()
    print("y Stopwatch started. Press ENTER to stop.")
    input()
    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f" Elapsed Time: {round(elapsed_time, 2)} seconds")

while True:
    stopwatch()
    choice = input("\n Do you want to run it again? (y/n): ").lower()
    if choice != 'y':
        print(" Thanks for using the stopwatch!")
        break
