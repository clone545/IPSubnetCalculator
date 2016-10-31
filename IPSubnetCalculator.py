"""Basic calculator to show all IPv4 addresses in a range, such as 1.2.3.4/32"""

import ipaddress

def subnetcalc(source):

    valid_ips = list(ipaddress.ip_network(source).hosts())

    for i in range(0, len(valid_ips) -1):
        print(valid_ips[i])

source = input(print("Enter an IP address to test such as '192.0.2.0/29':"))
subnetcalc(source)