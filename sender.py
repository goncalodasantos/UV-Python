import socket
import sys
from threading import Thread


def client_thread(connection):

    while 1:
        
        message=connection.recv(1024).decode("utf8")
        print(":"+message)











soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 8888

try:
    soc.connect((host, port))
except:
    print("Erro de Ligação")
    sys.exit()

nome = input("Insira o nome: ")


thread=Thread(target=client_thread, args=(soc,))
thread.daemon=True
thread.start()


print("Insira 'sair' para sair")
message = input("")

while message != 'sair':
    message=nome.upper() + ": " + message
    
    soc.sendall(message.encode("utf8"))

    message = input("")
    
soc.send(b'--sair--')




