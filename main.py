import os 
import sys
import socket
import datetime
import time

FILE = os.path.join(os.getcwd(), "networkinfo.log")

def ping():
    try:
        socket.setdefaulttimeout(3)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = ""
        port = ""
        server_address = (host, port)
        s.connect(server_address)

    except OSError as error:
        return False
    else:
        s.close()
        return True

def calc_time(start, stop):
    diff = stop - start
    seconds = float(str(diff.total_seconds()))
    return str(datetime.timedelta(seconds=seconds)).split(".")[0]

def first_check():
    if ping():
        live = "\nConnexion etablie\n"
        print(live)
        connection_etablish_time = datetime.datetime.now()
        accquiring_mess = "connection etablie a: " + \
            str(connection_etablish_time).split(".")[0]
        print(accquiring_mess)

        with open(FILE, "a") as file:
            file.write(live)
            file.write(accquiring_mess)

        return True

    else:
        not_live = "\nConnexion impossible\n"
        print(not_live)
        with open(FILE, "a") as file:
            file.write(not_live)
        return False

def main():
    monitor_start_time = datetime.datetime.now()
    monitoring_date_time = "monitoring started at: " + \
        str(monitor_start_time).split(".")[0]

    if first_check():
        print(monitoring_date_time)

    else:
        while True:
            if not ping():
                time.sleep(1)
            else:
                first_check()
                print(monitoring_date_time)
                break

        with open(FILE, "a") as file:
            file.write("\n")
            file.write(monitoring_date_time + "\n")

        while True:
            if ping():
                time.sleep(5)
            else:
                down_time = datetime.datetime.now()
                fail_mess = "disconnected at: " + str(down_time).split(".")[0]
                print(fail_mess)

                with open(FILE, "a") as file:
                    file.write(fail_mess + "\n")

                while not ping():
                    time.sleep(1)
                up_time = datetime.datetime.now()
                uptime_message = "connected again: " + str(up_time).split(".")[0]
                down_time = calc_time(down_time, up_time)
                unavailablity_time = "connection wad unavailable for: " + down_time
                print(uptime_message)
                print(unavailablity_time)
                with open(FILE, "a") as file:
                    file.write(uptime_message + "\n")
                    file.write(unavailablity_time + "\n")

main()