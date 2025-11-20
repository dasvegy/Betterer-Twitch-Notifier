from functions.load_streamer_file import get_usernames
import time

stop_loop = False


# The *loop*
def run_checker_loop(interval_minutes):
    global stop_loop
    while not stop_loop:
        get_usernames()
        print(f"Waiting {interval_minutes} minutes...\n")
        for _ in range(interval_minutes * 60):
            if stop_loop:
                break
            time.sleep(1)
