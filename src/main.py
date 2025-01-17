import os
import platform
import subprocess
import datetime
import time

FILE = os.path.join(os.getcwd(), "../logs/networkinfo.log")

def ping(host):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", host]
    return subprocess.call(command) == 0

def calculate_time(start, stop):
    difference = stop - start
    seconds = float(difference.total_seconds())
    return str(datetime.timedelta(seconds=seconds)).split(".")[0]

def log_status(ip, status, timestamp):
    log_entry = f"{ip}, {status}, {timestamp}\n"
    with open(FILE, "a") as file:
        file.write(log_entry)

def first_check(host):
    if ping(host):
        status = "actif"
        connection_acquired_time = datetime.datetime.now()
        timestamp = str(connection_acquired_time).split(".")[0]
        print(f"\nCONNEXION ÉTABLIE\nConnexion établie à: {timestamp}")
        log_status(host, status, timestamp)
        return True
    else:
        status = "inactif"
        connection_failed_time = datetime.datetime.now()
        timestamp = str(connection_failed_time).split(".")[0]
        print(f"\nCONNEXION IMPOSSIBLE\n")
        log_status(host, status, timestamp)
        return False

def main():
    host = "89.227.241.187" #WIP: convert this var into an object, and put it into the database 
    monitor_start_time = datetime.datetime.now()
    monitoring_date_time = str(monitor_start_time).split(".")[0]
    
    with open(FILE, "a") as file:
        file.write(f"Monitoring started at: {monitoring_date_time}\n")

    if not first_check(host):
        while True:
            if not ping(host):
                time.sleep(1)
            else:
                first_check(host)
                break

    while True:
        if ping(host):
            time.sleep(5)
        else:
            down_time = datetime.datetime.now()
            down_timestamp = str(down_time).split(".")[0]
            print(f"Déconnecté à: {down_timestamp}")
            log_status(host, "inactif", down_timestamp)

            while not ping(host):
                time.sleep(1)

            up_time = datetime.datetime.now()
            up_timestamp = str(up_time).split(".")[0]
            uptime_message = f"Reconnecté à: {up_timestamp}"
            down_time_duration = calculate_time(down_time, up_time)
            unavailability_message = f"Connexion indisponible pendant: {down_time_duration}"

            print(uptime_message)
            print(unavailability_message)

            log_status(host, "actif", up_timestamp)
            log_status(host, "inactif", f"pendant: {down_time_duration}")

if __name__ == "__main__":
    main()