# Message Sender
import os
from socket import *


class Client(object):

    def run_client(self):
        host = "127.0.0.1"  # set to IP address of target computer
        port = 13000
        addr = (host, port)
        UDPSock = socket(AF_INET, SOCK_DGRAM)
        while True:
            data = raw_input("Enter message to send or type 'exit': ")
            UDPSock.sendto(data, addr)
            if data == "exit":
                break
        exit(UDPSock)

    def exit(self, UDPSock):
        UDPSock.close()
        os._exit(0)
