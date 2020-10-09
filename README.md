# Check ssh connections
This script read a file that contains a list of hosts and verify if those hosts have a ssh public key copied.

## Usage
To use this script you must install paramiko with this command:

```bash
pip install paramiko
```
To execute you must to pass those arguments:
1) The file that contains the list of hosts
2) The user that will use to connect
3) The private ssh key with its path. This argument is option if you do not pass it, the script will overwrite for the id_rsa of the user that executed.

Example of execution:

```bash
./chech_ssh_list.py host_list.txt maxi
```

Only works with python 3.6 or later

## Autor
Maximiliano Zapata
maxzm7@gmail.com
