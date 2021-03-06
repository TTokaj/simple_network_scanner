#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    #broadcast MAC address, when send smth to ff:ff:ff:ff:ff:ff all clients will receive
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #scapy allow to combine previous two lines by using /
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1)[0]
    print(answered_list.summary())



#10.0.2.1/24
scan("192.168.0.1/24")