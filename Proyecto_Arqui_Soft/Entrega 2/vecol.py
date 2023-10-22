import socket
import csv
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


def Colec(cod): #cod -> ID usuario
    cartas = []
    with open('BDD/Agregar_Carta_Coleccion.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == cod:
                cartas.append(row[1])
    return cartas

def cartas(cod): #cod -> ID Carta
    with open('BDD/cartas.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == cod:
                return row[1]
    return False 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 5002

sock.connect((host, port))
sock.send(b'00010sinitvecol')
data = sock.recv(4096)
print(data.decode())
try:
    while True:
        
        data = sock.recv(4096)
        print(data.decode())
        data = data.decode()[10:]
        service = 'vecol'
        carta = Colec(data)
        aux = ''
        for i in carta:
             aux += str(cartas(i) + ',')
        
        if aux == False:
            sock.send(b'00017reticOKnofound')
            
        else:
            size = len(aux) + len(service)
            msg = getSize(size) + 'vecolOK' + aux
            #print(msg)
            sock.send(msg.encode("utf-8")) 
        
finally:
    print("cerrando socket")
    sock.close()