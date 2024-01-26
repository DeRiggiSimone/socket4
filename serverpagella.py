import socket
import json

SERVER_IP="127.0.0.1"
SERVER_PORT=22005
BUFFER_SIZE=1024


with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock_server:
    sock_server.bind((SERVER_IP,SERVER_PORT))
    sock_server.listen()
    print("in ascolto su "+str(SERVER_IP)+" "+str(SERVER_PORT))
    while True:
        sock_service,addr=sock_server.accept()
        with sock_service as sock_client:
            while True:
                data=sock_client.recv(BUFFER_SIZE)
                print(data)
                if not data:
                    break
                data=data.decode()
                data=json.loads(data)
    
                ris=str(ris)
                print("risul:",ris)
                sock_client.sendall(ris.encode())
