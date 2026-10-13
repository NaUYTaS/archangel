import os
import sys
import time
from datetime import datetime
import psutil

#Terminal colors for cool cyber-punk looking output
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

# Hey I added my custom welcome banner here
def print_welcome_message():
    """Prints our custom project banner"""
    print(f"{CYAN}=================================================={RESET}")
    print(f"{GREEN}   ARCHANGEL v1.0 - MY PERSONAL SECURITY GUARD   {RESET}")
    print(f"{CYAN}   Developed by: NaUYTaS                {RESET}")
    print(f"{CYAN}=================================================={RESET}")

def print_angel_ascii():
     """Original Archangel wings ascii art"""
angel = f"""
{CYAN}                      ___
                     /   \\

                    |  X  |
           _         \\___/         _
          / \\          |          / \\
         /   \\        /|\\        /   \\
        /     \\______/ | \\______/     \\
       /       \\    /  |  \\    /       \\
      /   /\\    \\  /   |   \\  /    /\\   \\

     |   /  \\    \\/    |    \\/    /  \\   |
     |  /    \\   /     |     \\   /    \\  |
     | /      \\_/      |      \\_/      \\ |
     |/                |                \\|
                       |
                       |
                      [-]

                      | |
                      | |
                       v{RESET}
"""
print(angel)

def print_header(title):
     """Helper function to print beautiful section dividers"""
     print(f"\n{'='*20} {title} {'='*20}")

def  check_network_connections():
     """My implementation of traffic monitoring"""
     print_header("NETWORK TRAFFIC MONITORING")
     print(f"{'Application':<25} |  {'Local Address':<22} | {'Remote Address (Destination)':<28} | Status")
     print("-" * 100)


     try:
          connection = psutil.net_connections(kind='inet')
     except psutil.AccessDenied:
        print(f"{RED}[!] Access Denied! Please run terminal as Admin to see connections.{RESET}")
        return

     for conn in connection:
      if conn.status == 'ESTABLISHED':
       local_addr = f"{conn.laddr.ip}:{conn.laddr.port}"
       remote_addr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"

     try:
        proc = psutil.Process(conn.pid)
        proc_name = proc.name()
     except (psutil.NoSuchProcess, psutil.AccessDenied):
        proc_name = f"{YELLOW}Unknown Process (Hidden?){RESET}"

        status_text = f"{GREEN}{conn.status}{RESET}"
        print(f"{proc_name:<25} | {local_addr:<22} | {remote_addr:<28} | {status_text}")

def check_suspicious_processes():
    """Smart Miner Check - Modified to avoid false alarms"""
    print_header("RUNNING PROCESSES ANALYSIS")
    print(f"{'PID':<8} | {'Process Name':<25} | {'CPU Usage':<10} | Memory Usage (MB)")
    print("-" * 75)


    # First snapshot of CPU usage
    for proc in psutil.process_iter(['pid']):
        try:
            proc.cpu_percent(interval=None)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    time.sleep(0.1) # Tiny pause to calculate delta


    # Second snapshot and actual scanning logic
    for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
        try:
            mem_mb = proc.info['memory_info'].rss / (1024 * 1024)
            cpu_usage = proc.cpu_percent(interval=None)


            # Alarm triggers only if RAM > 800MB OR CPU > 40%
            if mem_mb > 800 or cpu_usage > 40.0:
                # Critical alert if CPU usage is crazy high (>50%)
                alert_color = RED if cpu_usage > 50.0 else YELLOW
                print(f"{proc.info['pid']:<8} | {proc.info['name']:<25} | {alert_color}{cpu_usage:>5.1f}%{RESET} | {alert_color}{mem_mb:.2f} MB{RESET}")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

def check_autorun():
    """Checks where registry malware usually hides"""
    if sys.platform != "win32":
        return


    print_header("WINDOWS STARTUP (AUTORUN) CHECK")
    import winreg

    reg_paths = [
        r"Software\Microsoft\Windows\CurrentVersion\Run",
        r"Software\Microsoft\Windows\CurrentVersion\RunOnce"
    ]

    for path in reg_paths:
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, path, 0, winreg.KEY_READ)
            num_keys = winreg.QueryInfoKey(key)[1] # Get number of startup items
            
            if num_keys == 0:
               print(f"No startup items found in: HKEY_CURRENT_USER\\{path}")


            for i in range(0, num_keys):
                name, value, _ = winreg.EnumValue(key, i)
                print(f"App: {YELLOW}{name}{RESET} -> Launches file: {value}")
            winreg.CloseKey(key)
        except WindowsError:
            print(f"{RED}[!] Error reading registry path: {path}{RESET}")
def check_temp_folder():
    """Scans Windows Temp folder for files created TODAY"""
    if sys.platform != "win32":
        return
    print_header("BONUS: TEMP FOLDER SUSPICIOUS FILES")



    temp_dir = os.environ.get('TEMP')
    if not temp_dir or not os.path.exists(temp_dir):
        print("Temp folder not found.")
        return


    today = datetime.now().date()
    found_any = False

    try:
        for file in os.listdir(temp_dir):
            file_path = os.path.join(temp_dir, file)
            if os.path.isfile(file_path):
               # Get file creation time
               creation_time = datetime.fromtimestamp(os.path.getctime(file_path)).date()
               if creation_time == today:
                   print(f"{YELLOW}[!] New file created today:{RESET} {file}")
                   found_any = True
    except Exception:
        print(f"{RED}[!] Couldn't scan Temp directory (Permission issue).{RESET}")

    if not found_any:
        print(f"{GREEN}[+] Temp folder looks clean today.{RESET}")


if __name__ == "__main__":
    if sys.platform == "win32":
        os.system('color') # Fix colors on Windows CMD


    print_welcome_message() # Your personal banner
    print_angel_ascii() 
    check_network_connections()
    check_suspicious_processes()
    check_autorun()
    check_temp_folder() # Your personal new feature
