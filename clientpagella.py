import socket
import json

SERVER_IP="127.0.0.1"
SERVER_PORT=22005
BUFFER_SIZE=1024

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock_service:
    sock_service.connect((SERVER_IP,SERVER_PORT))
    print("connesso "+str(SERVER_IP)+" "+str(SERVER_PORT))
    comando=print(input("digita il comando: "))
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
    dizionarioStudenti=json.dumps(dizionarioStudenti)
    sock_service.sendall(dizionarioStudenti.encode("UTF-8"))
    data=sock_service.recv(1024)
    print("Risultato: ",data.decode())
    risposta=str(input("fare un altra operazione? si/no"))
