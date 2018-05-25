import socket, threading
from tabulate import tabulate

final = []
def TCP_connect(ip, port_number, delay, output):
    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPsock.settimeout(delay)
    try:
        TCPsock.connect((ip, port_number))
        output[port_number] = 'Listening'
    except:
        output[port_number] = ''

def scan_ports(host_ip, delay):
    open_ports = []
    threads = []        # To run TCP_connect concurrently
    output = {}         # For printing purposes

    # Spawning threads to scan ports
    for i in range(800):
        t = threading.Thread(target=TCP_connect, args=(host_ip, i, delay, output))
        threads.append(t)

    # Starting threads
    for i in range(800):
        threads[i].start()

    # Locking the script until all threads complete
    for i in range(800):
        threads[i].join()

    for i in range(800):
        if output[i] == 'Listening':
            open_ports.append(i)

    return open_ports

with open("hosts.txt") as f:
    hosts = f.readlines()
print "Loading hosts from hosts.txt"
all_ips = []
hosts = [x.strip() for x in hosts]
name = hosts[0]
hosts_to_ips = []
open_port_ips = []


print "Hosts loaded"
print "Scanning ports 0-800 on each host"
for host in hosts:

    try:
        ip = socket.gethostbyname(host)
        hosts_to_ips.append([host, ip])
        if ip not in all_ips:
            all_ips.append(ip)
    except:
        hosts_to_ips.append([host, "None"])
        all_ips.append("None")

open_port_ips.append(["None", "None"])


for ip in all_ips:
    if ip != "None":
        port_scan = scan_ports(ip, .5)
        open_port_ips.append([ip, port_scan])

with open('result_' + name + '.txt', 'wb') as file:

    for scan in open_port_ips:
        hosts_for_this_ip = []
        try:
            reverse_dns = socket.gethostbyaddr(scan[0])
        except:
            reverse_dns = "None"
        for host in hosts_to_ips:
            if host[1] == scan[0]:
                hosts_for_this_ip.append(host[0])
        final.append([reverse_dns, scan[0], scan[1], hosts_for_this_ip])

    headers = ["REVERSE DNS", "IP ADDRESS", "OPEN PORTS", "DOMAINS"]
    table = tabulate(final, headers, tablefmt="psql")
    print table
    file.write(table)
