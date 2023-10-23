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

def cartas(): #cod -> ID Carta
    cartas = []
    with open('BDD/cartas.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            cartas.append(row)
        return cartas
    return False 

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
        carta = cartas()
        aux = 'Nombre : Tipo,'
        for i in carta:
             aux += str( i[1] + ': ' + i[2] + ',')
        
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