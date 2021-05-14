from socket import *
import time
import sys

class Client(object):
    def __init__(self,server_name,server_port):
        self.server_name = server_name 
        self.server_port = server_port

    def create_socket(self):
       # Criando socket chamado client_socket com endereço tipo IPV4 e protocolo UDP
        self.client_socket = socket(AF_INET, SOCK_DGRAM)

    def send_message(self,message):
        # Converter string para bytes
        message = message.encode()
        # Enviando mensagem ao servidor buscando endereço e porta socket
        self.client_socket.sendto(message,(self.server_name, self.server_port))

    def get_time(self):
        return time.time()
    
    def get_ping(self,start,end):
        return end-start

    def get_message(self):
        return self.client_socket.recvfrom(2048)[0].decode().lower()

    def close_socket(self):
        self.client_socket.close()


def main():

    # Nome ou endereço IP e numero da porta socket do servidor 
    server_name = '192.168.56.1'
    
    server_port = sys,argv[1]

    # server_names = []

    # for i in range(3):
    #     server_name = input("Entre IP do servidor:")


    cli = Client(server_name, server_port)
    cli.create_socket()
    start = cli.get_time()
    print(start)
    cli.send_message(message)
    end = cli.get_time()
    print(end)
    return_message = cli.get_message()
    ping = cli.get_ping(start,end)
    print(ping)
    cli.close_socket()

main()