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


def Mazo(cod): #cod -> ID usuario
    mazos = ''
    with open('BDD/BDD.json') as file:
        reader = json.load(file)
        usuarios = reader['usuarios']
        for row in usuarios:
            if row["ID_Usuario"] == cod:
                 mazos = row["Mazos"]
                 return mazos
    return mazos


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 5002

sock.connect((host, port))
sock.send(b'00010sinitmazos')
data = sock.recv(4096)
print(data.decode())
try:
    while True:
        
        data = sock.recv(4096)
        #print(data.decode())
        data = data.decode()[10:]
        service = 'mazos'

        Mazos = Mazo(data) #IDs de los Mazos del Usuario
        #ID Mazos -> ID Carta -> Nombre Pokemon
        aux = ''

        for m in Mazos:
            aux += m["ID_Mazo"] + ', ' + m["Nombre"] + ';'
        
        if aux == '':
            sock.send(b'00017mazosOKnofound')
            
        else:
            size = len(aux) + len(service)
            msg = getSize(size) + 'mazosOK' + aux
            
            sock.send(msg.encode("utf-8")) 
        
finally:
    print("cerrando socket")
    sock.close()