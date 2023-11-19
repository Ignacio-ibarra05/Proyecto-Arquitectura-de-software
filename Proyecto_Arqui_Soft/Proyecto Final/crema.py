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

def Mazo(data1, data2, cod): #cod -> ID usuario
    with open('BDD/BDD.json') as file:
        usuario = json.load(file)

        #ID MAZO, NOMBRE MAZO, ID USUARIO
    data = {
        "Nombre": data1,
        "ID_Mazo": data2,
        "Cartas": [
        ] 
    }

    for usu in usuario['usuarios']:
        if usu['ID_Usuario'] == cod:
            usu['Mazos'].append(data)

    with open('BDD/BDD.json', 'w') as archivo:
        json.dump(usuario, archivo, indent=4)

    return "Mazo_creado"

def ID_Mazo(cod, can):
    idm = ''
    milecima = str(cod[len(cod)-1])
    if len(can) == 1:
        idm = milecima + '00' + can
    elif len(can) == 2:
        idm = milecima + '0' + can
    return idm

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 5002

sock.connect((host, port))
sock.send(b'00010sinitcrema')
data = sock.recv(4096)
print(data.decode())
try:
    while True:
        
        data = sock.recv(4096)
        data = data.decode()[10:]
        nombre, cod, can = data.split(',')
        service = 'crema'
        id_mazo = str(ID_Mazo(cod, can))

        aux = Mazo(nombre, id_mazo, cod) #IDs de los Mazos del Usuario
        
        if aux == False:
            sock.send(b'00014cremaOKnofound')
            
        else:
            size = len(aux) + len(service)
            msg = getSize(size) + 'cremaOK' + aux
            sock.send(msg.encode("utf-8")) 
            
finally:
    print("cerrando socket")
    sock.close()