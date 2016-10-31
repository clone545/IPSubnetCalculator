"""Basic calculator to show all IPv4 addresses in a range, such as 1.2.3.4/32"""

import ipaddress

def subnetcalc(source):

    valid_ips = list(ipaddress.ip_network(source).hosts())

    for i in valid_ips:
        print(i)

    return True

source = input(print("Enter an IP address to test such as '192.0.2.0/29':"))
subnetcalc(source)