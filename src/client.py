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

    def get_message(self):
        return self.client_socket.recvfrom(2048)[0].decode().lower()

    def close_socket(self):
        self.client_socket.close()
