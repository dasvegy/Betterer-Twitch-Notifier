from functions.load_streamer_file import get_usernames
import time

def run_checker_loop(interval_minutes: int = 0.1):
    while True:
        get_usernames()
        print(f"Waiting {interval_minutes} minutes...\n")
        time.sleep(interval_minutes * 60)