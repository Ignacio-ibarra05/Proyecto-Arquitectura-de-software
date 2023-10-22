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


def Mazo(cod): #cod -> ID usuario
    mazos = ''
    with open('BDD/Mazo.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[2] == cod:
                mazos += str(row[0] + ': ' + row[1] + ',') #ID del mazo
    return mazos


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
        print(data.decode())
        data = data.decode()[10:]
        service = 'vemaz'

        aux = Mazo(data) #IDs de los Mazos del Usuario
        #ID Mazos -> ID Carta -> Nombre Pokemon
        
        
        if aux == False:
            sock.send(b'00017vemazOKnofound')
            
        else:
            size = len(aux) + len(service)
            msg = getSize(size) + 'vemazOK' + aux
            #print(msg)
            
            sock.send(msg.encode("utf-8")) 
        
finally:
    print("cerrando socket")
    sock.close()