import socket
import json
#listo

def getSize(size):
    count = 0
    n = size
    while n != 0:
        n //= 10
        count += 1

    size = str(size)
    while count < 5:
        size = '0' + size
        count +=1
    return size

def carta(): #cod -> ID Carta
    with open('BDD/BDD.json', 'r') as archivo:
        datos = json.load(archivo)
    a = ''

    for cartas in datos["cartas"]:
        a = a + str(cartas["ID_carta"]) + ',' + cartas["Nombre"] + ';'

    return a

def usuarios():
    with open('BDD/BDD.json', 'r') as archivo:
        datos = json.load(archivo)
    a = ''
    for usuario in datos['usuarios']:
        a = a + usuario["ID_Usuario"] + ',' + usuario["Nombre"] + ';'

    return a

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 5002

sock.connect((host, port))
sock.send(b'00010sinitlista')
data = sock.recv(4096)
print(data.decode())

try:
    while True:
        
        data = sock.recv(4096)
        #print(data.decode())
        data = data.decode()[10:]
        service = 'lista'
        cliente, op = data.split(',')
        #print(op)
        aux = ''
        
        if op == '1': #Usuario
            aux = usuarios()
        elif op == '2':
            aux = carta()

        if aux == False:
            sock.send(b'00017listaOKnofound')
            
        else:
            size = len(aux) + len(service)
            msg = getSize(size) + 'listaOK' + aux
            #print(msg)
            sock.send(msg.encode("utf-8")) 
        
finally:
    print("cerrando socket")
    sock.close()