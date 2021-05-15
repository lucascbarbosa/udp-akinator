import sys
import akinator
from src.server import Server

aki = akinator.Akinator()

q = aki.start_game()

server_port = int(sys.argv[1])
server_name = sys.argv[2]

server = Server(server_name,server_port)
server.create_socket()
start_message,client_address = server.listen()
if start_message == 'start':
    while aki.progression <= 80:
        server.send_message(q+'\n\t',client_address)
        a,client_address = server.listen()
        if a == "b":
            try:
                q = aki.back()
            except akinator.CantGoBackAnyFurther:
                pass
        else:
            q = aki.answer(a)
    aki.win()

    server.send_message(f"It's {aki.first_guess['name']} ({aki.first_guess['description']})! Was I correct?\n{aki.first_guess['absolute_picture_path']}\n\t", client_address)
    correct,client_address = server.listen()
    if correct.lower() == "yes" or correct.lower() == "y":
        server.send_message(f"Yay!")
    else:
        server.send_message(f"Oof...")

else: 
    pass