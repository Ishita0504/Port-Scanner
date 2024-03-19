import socket
import sys
from datetime import datetime


def scanHost(ip, startPort, endPort):
    print('[*] Starting TCP port scan on host %s %s' % (ip , str(datetime.now())))
    # Begin TCP scan on host
    tcp_scan(ip, startPort, endPort)
    print('[+] TCP scan on host %s complete %s ' % (ip , str(datetime.now())))


def scanRange(network, startPort, endPort):
    print('[*] Starting TCP port scan on network %s  %s .0' % (network,str(datetime.now())))
    for host in range(1, 255):
        ip = network + '.' + str(host)
        tcp_scan(ip, startPort, endPort)

    print('[+] TCP scan on network %s.0 complete %s' % (network,str(datetime.now())))


def tcp_scan(ip, startPort, endPort):
    for port in range(startPort, endPort + 1):
        try:
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if not tcp.connect_ex((ip, port)):
                print('[+]%s %s:%d/TCP Open ' % (str(datetime.now()),ip, port))
                tcp.close()
        except Exception:
            pass


def main():
    socket.setdefaulttimeout(0.01)
    network = input("IP ADDRESS: ")
    startPort = int(input("START PORT: "))
    endPort = int(input("END PORT: "))
    scanHost(network, startPort, endPort)


main()
end = input("Press any key to close")


