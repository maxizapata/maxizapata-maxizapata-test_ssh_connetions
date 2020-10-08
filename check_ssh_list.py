from sys import argv, stderr
try:
    import paramiko
except ModuleNotFoundError:
    print("You must install paramiko to use this script")
else:
    ssh = paramiko.SSHClient()

failed_connections = []
success_connections = []
data_source = argv[1]
username = argv[2]

stderr = None
OKBLUE = '\033[94m'
FAIL = '\033[91m'
ENDC = '\033[0m'

with open(argv[1]) as ssh_list:
    for ip_raw in ssh_list:
        ip = ip_raw.strip()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(ip, username=username, key_filename=argv[3])
        except paramiko.ssh_exception.SSHException:
            failed_connections.append(ip)
        else:
            success_connections.append(ip)

def print_connections(server_list, msg, font_color):
    if server_list:
        print(font_color + f'{msg}:' + ENDC)
        for f in server_list:
            print(f'- {f}')
    else:
        print(font_color + f'No {msg.lower()}' + ENDC)

print_connections(failed_connections, 'Failed Connections', FAIL)

print_connections(success_connections, 'Success connections', OKBLUE)
