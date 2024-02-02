import socket
import json

SERVER_IP="127.0.0.1"
SERVER_PORT=22005
BUFFER_SIZE=1024

dizionarioStudenti={   'Antonio Barbera': [   ['Matematica', 8, 1],
                            ['Italiano', 6, 1],
                            ['Inglese', 9.5, 0],
                            ['Storia', 8, 2],
                            ['Geografia', 8, 1]],
        'Giuseppe Gullo': [   ['Matematica', 9, 0],
                           ['Italiano', 7, 3],
                           ['Inglese', 7.5, 4],
                           ['Storia', 7.5, 4],
                           ['Geografia', 5, 7]],
        'Nicola Spina': [   ['Matematica', 7.5, 2],
                         ['Italiano', 6, 2],
                         ['Inglese', 4, 3],
                         ['Storia', 8.5, 2],
                         ['Geografia', 8, 2]]}

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
                comando=data['comando']
                parametro=data['parametro']
                print(comando)
                print(parametro)
    
                ris=str(ris)
                print("risul:",ris)
                sock_client.sendall(ris.encode())
