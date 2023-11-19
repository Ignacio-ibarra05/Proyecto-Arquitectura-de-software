import socket
import json
import re
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

def Usuarios(IDU, Nombre, Contra, Rol): #cod -> ID usuario
    with open('BDD/BDD.json') as file:
        usuarios = json.load(file)
        #ID MAZO, NOMBRE MAZO, ID USUARIO
    data = {
        "ID_Usuario": IDU,
        "Nombre": Nombre,
        "Contra": Contra,
        "Rol": Rol,
        "Coleccion": [],
        "Mazos": []
    }
    usuarios['usuarios'].append(data)

    with open('BDD/BDD.json', 'w') as archivo:
        json.dump(usuarios, archivo, indent=4)

    return "Usuario_creado"

def ID_Usuario():
    a = ''
    with open('BDD/BDD.json') as file:
        read = json.load(file)
    for i in read['usuarios']:
        a = i["ID_Usuario"]
        
    return Size2(a)

def Size2(a):
    a = int(a)
    return Size3(a + 1)

def Size3(a):
    size = ''
    a = str(a)
    if len(a) == 1:
        size = '000' + a
    elif len(a) == 2:
        size = '00' + a
    return size

def verificar(nom):
    a = False
    with open('BDD/BDD.json') as file:
        read = json.load(file)
    for i in read['usuarios']:
        if i["Nombre"] == nom:
            a = True
    return a


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
        nombre, contra = data.split(' ')
        idu = ID_Usuario()
        rol = 'usu'
        service = 'creus'
        aux = False
        v = verificar(nombre)
        aux1 = ''
        if v == False:
            aux1 = Usuarios(idu, nombre, contra, rol) #IDs de los Mazos del Usuario
            aux = True
        
        if aux == False:
            sock.send(b'00014creusOKnofound')
            
        else:
            size = len(aux1) + len(service)
            msg = getSize(size) + 'creusOK' + aux1
            sock.send(msg.encode("utf-8")) 
            
finally:
    print("cerrando socket")
    sock.close()
