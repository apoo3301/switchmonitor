import time
from ping3 import ping
from pysnmp.hlapi import *

def ping_switch(ip):
    response = ping(ip, timeout=1)
    return response is not None

def get_switch_status(ip, community, oid):
    iterator = getCmd(SnmpEngine(),
                      CommunityData(community),
                      UdpTransportTarget((ip, 161)),
                      ContextData(),
                      ObjectType(ObjectIdentity(oid)))
    
    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
    
    if errorIndication:
        print(errorIndication)
        return None
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        return None
    else:
        for varBind in varBinds:
            return varBind.prettyPrint()

def monitor_switch(ip, community, oid, interval=5):
    while True:
        is_alive = ping_switch(ip)
        if is_alive:
            print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Switch {ip} is UP")
            status = get_switch_status(ip, community, oid)
            if status:
                print(f"Switch status: {status}")
        else:
            print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Switch {ip} is DOWN")
        
        time.sleep(interval)

if __name__ == "__main__":
    switch_ip = "89.227.241.187"
    snmp_community = "public"
    snmp_oid = "1.3.6.1.2.1.1.1.0"

    monitor_switch(switch_ip, snmp_community, snmp_oid)
