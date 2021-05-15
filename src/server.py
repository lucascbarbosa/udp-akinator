from socket import *
import sys

class Server(object):
    
    def __init__(self,server_name, server_port, lat, long):
        self.server_name = server_name
        self.server_port = server_port
        self.lat = lat
        self.long = long
    
    def create_socket(self):
        self.server_socket = socket(AF_INET, SOCK_DGRAM)
        # Cria socket com ip próprio no numero da porta declarada
        self.server_socket.bind((self.server_name, self.server_port))
        print ('Servidor de ip %s configurado na latitude: %.4f longitude: %.4f'%(self.server_name,self.lat,self.long))

    def start_listening(self):
        # Loop para manter servidor pronto para receber/enviar menssagens para algum cliente
        message, client_address = self.server_socket.recvfrom(2048)
        modified_message = message.lower()
        self.server_socket.sendto(modified_message, client_address)
        print(modified_message.decode())


def main():
    server_port = int(sys.argv[1])
    
    server_name = sys.argv[2]

    lat,long = -23.010209, -43.452613

    server = Server(server_name, server_port, lat, long)
    server.create_socket()
    server.start_listening()


main()