# Message Receiver
import os
from socket import *


class Server(object):
    def run_server(self):
        host = "127.0.0.1"
        port = 13000
        buf = 1024
        addr = (host, port)
        UDPSock = socket(AF_INET, SOCK_DGRAM)
        UDPSock.bind(addr)
        print "Waiting to receive messages..."
        while True:
            (data, addr) = UDPSock.recvfrom(buf)
            UDPSock.sendto(data, addr)
            # print "Received message: " + data
            if data == "exit":
                break
        exit(UDPSock)

    def exit(self, UDPSock):
        UDPSock.close()
        os._exit(0)