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

def Usuarios(data): #cod -> ID usuario
    with open('BDD/usuarios.csv', 'a') as file:
        #ID MAZO, NOMBRE MAZO, ID USUARIO
        file.write("\n" + data)
    file.close()
    return "Usuario_creado"

def ID_Usuario():
    a = ''
    with open('BDD/usuarios.csv', 'r') as file:
        read = csv.reader(file)
        for i in read:
            a = i[0]
        a = int(a)+1
    return Size3(a)

def Size3(size):
    count = 0
    n = size
    while n != 0:
        n //=10
        count += 1
    size = str(size)
    while count < 3:
        size = '0' + size
        count +=1
    return size

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 5002

sock.connect((host, port))
sock.send(b'00010sinitcreus')
data = sock.recv(4096)
print(data.decode())
try:
    while True:
        
        data = sock.recv(4096)
        data = data.decode()[10:]
        data = data.split(' ')
        service = 'creus'
        info = str(ID_Usuario()+ ',' + data[0] + ',' + data[1] + ',usu')
        aux = Usuarios(info) #IDs de los Mazos del Usuario
        
        if aux == False:
            sock.send(b'00014creusOKnofound')
            
        else:
            size = len(aux) + len(service)
            msg = getSize(size) + 'creusOK' + aux
            sock.send(msg.encode("utf-8")) 
            
finally:
    print("cerrando socket")
    sock.close()