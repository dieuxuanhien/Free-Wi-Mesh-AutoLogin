import psutil
import subprocess
import platform
import time
import os

# Change this to your program's name and path
PROCESS_NAME = "python.exe"  # Change this if you're using a different Python executable name
PROGRAM_PATH = os.path.join(os.path.dirname(__file__), "autoLogin.py")  # Use os.path.join for better cross-platform support

def stop_process():
    for proc in psutil.process_iter(['name', 'cmdline']):
        if proc.info['name'] == PROCESS_NAME and PROGRAM_PATH in " ".join(proc.info['cmdline']):
            proc.terminate()  # or proc.kill() for force stop
            print(f"Stopped {PROGRAM_PATH}")

def start_process():
    if platform.system() == "Windows":
        subprocess.Popen(["python", PROGRAM_PATH])
    elif platform.system() == "Darwin":  # macOS
        subprocess.Popen(["open", "-a", "Terminal", PROGRAM_PATH])
    print(f"Started {PROGRAM_PATH}")

def main():
    start_process()
    last_sleep_state = False
    while True:
        # Check if the system is sleeping or awake
        sleep_state = not psutil.sensors_battery().power_plugged

        if sleep_state and not last_sleep_state:
            print("MACHINE SLEEP DETECTED, CLOSING")
            stop_process()
            last_sleep_state = True
        elif not sleep_state and last_sleep_state:
            print("WAKE EVENT DETECTED, STARTING")
            start_process()
            last_sleep_state = False

        time.sleep(3)  # Check every 3 seconds

if __name__ == "__main__":
    main()