from socket import *
import sys

class Server(object):
    
    def __init__(self,server_name, server_port):
        self.server_name = server_name
        self.server_port = server_port
    
    def create_socket(self):
        self.server_socket = socket(AF_INET, SOCK_DGRAM)
        # Cria socket com ip próprio no numero da porta declarada
        self.server_socket.bind((self.server_name, self.server_port))
        print ('Servidor de ip %s configurado'%(self.server_name))

    def listen(self):
        # Loop para manter servidor pronto para receber/enviar menssagens para algum cliente
        message, client_address = self.server_socket.recvfrom(2048)
        modified_message = message.lower()
        return modified_message.decode(),client_address

    def send_message(self,message,client_address):
        message = message.encode()
        self.server_socket.sendto(message, client_address)
