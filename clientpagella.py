import socket
import json

SERVER_IP="127.0.0.1"
SERVER_PORT=22005
BUFFER_SIZE=1024

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock_service:
    sock_service.connect((SERVER_IP,SERVER_PORT))
    while(True):
        print("comandi disponobili:")
        print("list : per vedere i voti inseriti")
        print("get /nomestudente : per richiedere i voti di uno studente")
        print("set /nomestudente : per inserire uno studente")
        print("put /nomestudente/materia/voto/ore : per aggiungere i voti della materia allo studente")
        print("close : per chiudere la connessione")
        print("connesso "+str(SERVER_IP)+" "+str(SERVER_PORT))
        comando=print(input("digita il comando: "))
        if comando=="#list":
            parametro=""
        messaggio={'comando':comando,'parametro':parametro}
        print(messaggio)
        messaggio=json.dumps(messaggio)
        sock_service.sendall(messaggio.encode("UTF-8"))
        data=sock_service.recv(1024)
        print("Risultato: ",data.decode())
