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


def Mazos(cod): #cod -> ID mazo
    mazos = []
    with open('BDD/Agregar_Carta_Mazo.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == cod:
                mazos.append(row[1]) #ID del pokemon
        return mazos
    return False

def Mazo(cod):
    mazos = ''
    with open('BDD/cartas.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == cod:
                mazos = str(row[1] + ': ' + row[2] +',')
        return mazos
    return False


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 5002

sock.connect((host, port))
sock.send(b'00010sinitvemaz')
data = sock.recv(4096)
print(data.decode())

try:
    while True:
        
        data = sock.recv(4096)
        data = data.decode()[10:]
        service = 'vemaz'
        
        aux1 = Mazos(data)
        aux2 = []

        aux = 'Nombre: Tipo,'
        for i in aux1:
            aux += Mazo(i)
        
        
        if aux == False:
            sock.send(b'00014vemazOKnofound')
            
        else:
            size = len(aux) + len(service)
            msg = getSize(size) + 'vemazOK' + aux
            #print(msg)
            
            sock.send(msg.encode("utf-8")) 
        
finally:
    print("cerrando socket")
    sock.close()