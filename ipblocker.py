#!/usr/bin/env python

# Author ~ https://github.com/ajdev05
import subprocess

with open("bad_packets_list.txt", "r") as file:
    ip_addresses = file.read().splitlines()

for ip in ip_addresses:
    iptables_rule = f"ip route add blackhole {ip}"

    

    
    subprocess.run(iptables_rule, shell=True)
    print(f"Blocked IP: {ip}")

print("All IP addresses from the file have been blocked.")
