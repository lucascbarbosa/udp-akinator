from socket import *

class Server(object):
    
    def __init__(self,server_port):
        self.server_port = server_port
    
    def create_socket(self):
        self.server_socket = socket(AF_INET, SOCK_DGRAM)
        # Cria socket com ip próprio no numero da porta declarada
        self.server_socket.bind(('', self.server_port))
        print ('The server is ready to receive')

    def start_listening(self):
        # Loop para manter servidor pronto para receber/enviar menssagens para algum cliente
        message, client_address = self.server_socket.recvfrom(2048)
        modified_message = message.upper()
        self.server_socket.sendto(modified_message, client_address)
        print(modified_message.decode().lower())


def main():
    server_port = 8000
    server = Server(server_port)
    server.create_socket()
    server.start_listening()


main()