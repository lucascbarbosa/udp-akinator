import sys
from src.client import Client

server_port = int(sys.argv[1])
server_name = sys.argv[2]
cli = Client(server_name, server_port)
cli.create_socket()
message = input("Bem-vindo(a) ao Akinator UDP Server! Para começar, digite 'start'\n")
cli.send_message(message)
question = cli.get_message()

rounds = 1
print(f'Round: {rounds}: ', question)
rounds += 1

while rounds <= 80:
    response = input()
    cli.send_message(response)
    question = cli.get_message()
    print(f'Round: {rounds}: ', question)
    rounds += 1

cli.close_socket()


#    python server_akinator.py 8000 192.168.1.113
#    python client_akinator.py 8000 192.168.1.113