# This script allow to test a list of ssh conections
# You must pass two arguments:
# 1 - The file that contains the list of host
# 2 - The user to connect in the remote host
# 3 (Optinal) - The private ssh key

from sys import argv, stderr
from os import environ as env
try:
    import paramiko
except ModuleNotFoundError:
    print("You must install paramiko to use this script")
else:
    ssh = paramiko.SSHClient()


def private_key():
    try:
        argv[3]
    except IndexError:
        priv_key = f"{env['HOME']}/.ssh/id_rsa"
    else:
        priv_key = argv[3]
    return priv_key

hosts_not_reached = []
success_connections = []
error_connections = []
data_source = argv[1]
username = argv[2]
priv_key = private_key()

stderr = None
OKBLUE = '\033[94m'
FAIL = '\033[91m'
ENDC = '\033[0m'

with open(argv[1]) as ssh_list:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    for ip_raw in ssh_list:
        ip = ip_raw.strip()
        print(f'Testing connection for {ip}')
        try:
            # Try if can connect to remote server
            ssh.connect(ip, username=username, key_filename=priv_key)
        except (paramiko.ssh_exception.SSHException, TimeoutError):
            # Cannot reach
            print(FAIL + f'Host {ip} cannot be reached' + ENDC)
            hosts_not_reached.append(ip)
        except ValueError:
            # Connot login with the current ssh key
            # Trying to connect via password
            # Pending to implement
            error_connections.append(ip)
        else:
            success_connections.append(ip)

def print_connections(server_list, msg, font_color):
    if server_list:
        print(font_color + f'{msg}:' + ENDC)
        for f in server_list:
            print(f'- {f}')

print_connections(hosts_not_reached, 'Host not reached', FAIL)
print_connections(error_connections, 'Error connections', FAIL)
print_connections(success_connections, 'Success connections', OKBLUE)
