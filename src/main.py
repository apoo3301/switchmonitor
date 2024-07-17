import os
import platform
import subprocess
import datetime
import time
 
FILE = os.path.join(os.getcwd(), "logs/networkinfo.log")
 
def ping(host):
    """
    Pings the given host and returns True if the host is reachable, False otherwise.
    """
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", host]
 
    return subprocess.call(command) == 0
 
def calculate_time(start, stop):
    """
    Calculates the time difference between start and stop.
    """
    difference = stop - start
    seconds = float(difference.total_seconds())
    return str(datetime.timedelta(seconds=seconds)).split(".")[0]
 
def first_check(host):
    """
    Performs the initial check if the host is reachable.
    """
    if ping(host):
        live = "\nCONNEXION ÉTABLIE\n"
        print(live)
        connection_acquired_time = datetime.datetime.now()
        acquiring_message = "Connexion établie à: " + str(connection_acquired_time).split(".")[0]
        print(acquiring_message)
 
        with open(FILE, "a") as file:
            file.write(live)
            file.write(acquiring_message + "\n")
 
        return True
    else:
        not_live = "\nCONNEXION IMPOSSIBLE\n"
        print(not_live)
        with open(FILE, "a") as file:
            file.write(not_live + "\n")
        return False
 
def main():
    host = "89.227.241.187"  # WIP: ADD DB & LINK DB TO AN OBJECT
 
    monitor_start_time = datetime.datetime.now()
    monitoring_date_time = "Monitoring started at: " + str(monitor_start_time).split(".")[0]
 
    if first_check(host):
        print(monitoring_date_time)
        with open(FILE, "a") as file:
            file.write(monitoring_date_time + "\n")
    else:
        while True:
            if not ping(host):
                time.sleep(1)
            else:
                first_check(host)
                print(monitoring_date_time)
                break
 
    with open(FILE, "a") as file:
        file.write("\n")
        file.write(monitoring_date_time + "\n")
 
    while True:
        if ping(host):
            time.sleep(5)
        else:
            down_time = datetime.datetime.now()
            fail_msg = "Déconnecté à: " + str(down_time).split(".")[0]
            print(fail_msg)
 
            with open(FILE, "a") as file:
                file.write(fail_msg + "\n")
 
            while not ping(host):
                time.sleep(1)
 
            up_time = datetime.datetime.now()
            uptime_message = "Reconnecté à: " + str(up_time).split(".")[0]
 
            down_time_duration = calculate_time(down_time, up_time)
            unavailability_message = "Connexion indisponible pendant: " + down_time_duration
 
            print(uptime_message)
            print(unavailability_message)
 
            with open(FILE, "a") as file:
                file.write(uptime_message + "\n")
                file.write(unavailability_message + "\n")
 
if __name__ == "__main__":
    main()