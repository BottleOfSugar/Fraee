import socket
import psutil
import re
from colorama import Fore, Style, init
# Inicjalizacja colorama
init(autoreset=True)
import string
import colorama
def network_info():
    info = {}

    # Get hostname
    hostname = socket.gethostname()
    info['Hostname'] = hostname

    # Get local IP address
    local_ip = socket.gethostbyname(hostname)
    info['Local IP'] = local_ip

    # Get all network interfaces and their IP addresses
    interfaces = psutil.net_if_addrs()
    network_interfaces = {}
    for interface_name, interface_addresses in interfaces.items():
        for address in interface_addresses:
            if address.family == socket.AF_INET:  # IPv4
                network_interfaces[interface_name] = address.address
            elif address.family == socket.AF_INET6:  # IPv6
                network_interfaces[interface_name] = address.address

    info['Network Interfaces'] = network_interfaces

    # Get network statistics
    net_stats = psutil.net_io_counters(pernic=True)
    info['Network Stats'] = {
        iface: {
            'Bytes Sent': stat.bytes_sent,
            'Bytes Received': stat.bytes_recv
        }
        for iface, stat in net_stats.items()
    }

    return info

def teczowy_tekst(text):
    # Kolory tęczy do użycia z colorama
    teczowe_kolory = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    
    wynik = ""
    for i, litera in enumerate(text):
        # Wybieramy kolor z listy cyklicznie
        kolor = teczowe_kolory[i % len(teczowe_kolory)]
        wynik += f"{kolor}{litera}"
    
    return wynik

# Przykład użycia

def findlargestnumber(text):
    # Wyszukiwanie wszystkich liczb w tekście
    liczby = list(map(int, re.findall(r'\d+', text)))
    
    # Jeśli liczby istnieją, znajdź największą
    if liczby:
        return max(liczby)
    return None