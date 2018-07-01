import socket
import sys
import traceback
from threading import Thread

host = "127.0.0.1"
port = 10000         

list_of_connections=[]

def client_thread(connection):
    while 1:
        received_message = connection.recv(1024)
        client_input = received_message.decode("utf8").rstrip() 
        if(connection not in list_of_connections):
            list_of_connections.append(connection)
        
        if "--SAIR--" in client_input.upper():
            print("Client quitting")
            list_of_connections.remove(connection)
            connection.close()
            return 
        elif ""==client_input:
            continue
        else:
            print("Client said: "+ client_input)
            for c in list_of_connections:
                if(c!=connection):
                    try:
                        c.sendall(client_input.encode("utf8"))
                    except:
                        list_of_connections.remove(c)


socket_created = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_created.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print("Server created")

try:
    socket_created.bind((host, port))
except:
    print("Bind failed. Error : " + str(sys.exc_info()))
    sys.exit()

socket_created.listen(20)
print("Server now listening")

while True:
    connection, address = socket_created.accept()
    ip, port = str(address[0]), str(address[1])
    print("Connected: " + ip + ":" + port)

    try:
        Thread(target=client_thread, args=(connection,)).start()
    except:
        print("Thread did not start.")

socket_created.close()
