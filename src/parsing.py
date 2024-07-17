import os 
import time 

FILE = os.path.join(os.getcwd(), "../logs/networkinfo.log")

def parse_log_file():
    entries = []
    with open(FILE, "r") as file:
        lines = file.readlines()[1:] #ignore first line of .log
        for line in lines:
            parts = line.strip().split(", ")
            if len(parts) == 3:
                ip, status, timestamp = parts
                entries.append({"ip:" ip, "status:", status, "timestamp": timestamp})
            return entries

def watch_log_file():
    parsed_entries = parse_log_file()
    print("Initial log entries:")
    for entry in entries:
        print(entry)
    last_size = os.path.getsize(FILE)
    while True:
        current_size = os.get.getsize(FILE)
        if current_size > last_size:
            with open(FILE, "r") as file:
                file.seek(last_size)
                new_lines = file.readlines()

                for line in new_lines:
                    parts = line.strip().split(", ")
                    if len(parts) == 3:
                        ip, status, timestamp = parts
                        new_entry = {"ip": ip, "status", status, "timestamp", timestamp}
                        parsed_entries.append(new_entry)
                        print("new logs entry:", new_entry)
                    last_size = current_size
                time.sleep(1)

                