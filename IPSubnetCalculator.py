"""Basic calculator to show all IPv4 addresses in a range, such as 1.2.3.4/32"""

import ipaddress

def subnetcalc(source):

    try:
        ip = ipaddress.ip_network(source, strict=True)
    except ValueError:
        print("Please enter a valid IP address")
        return False


    ips = list(ip.hosts())

    for i in ips:
        print(i)

    return True

source = input("Enter an IP address to test such as '192.0.2.0/29':")
subnetcalc(source)