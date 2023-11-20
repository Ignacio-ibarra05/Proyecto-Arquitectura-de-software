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

def Cartas(cod): #cod -> ID usuario
    # Cargar el JSON desde el archivo
    with open('BDD/BDD.json', 'r') as archivo:
        datos = json.load(archivo)

    # ID de la carta que quieres eliminar
    id_carta_eliminar = int(cod)  # Reemplaza con el ID de la carta que deseas eliminar

    # Encontrar y eliminar la carta si está presente
    for carta in datos['cartas']:
        print(carta['ID_carta'])
        if carta['ID_carta'] == id_carta_eliminar:
            datos['cartas'].remove(carta)
            break  # Romper el bucle una vez que se elimine la carta

    # Guardar los cambios en el archivo JSON
    with open('BDD/BDD.json', 'w') as archivo:
        json.dump(datos, archivo, indent=4)
    
    return "Carta Eliminada"

def agregar(nom, tip, rar):
    with open('BDD/BDD.json') as file:
        usuarios = json.load(file)
        #ID MAZO, NOMBRE MAZO, ID USUARIO
    data = {
        "ID_carta": ID_Usuario(),
        "Nombre": nom,
        "Tipo": tip,
        "Raresa": rar
    }
    usuarios['cartas'].append(data)

    with open('BDD/BDD.json', 'w') as archivo:
        json.dump(usuarios, archivo, indent=4)

    return "Carta agregada"

def ID_Usuario():
    a = ''
    with open('BDD/BDD.json') as file:
        read = json.load(file)
    for i in read['cartas']:
        a = i["ID_carta"]
        
    return a+1


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 5002

sock.connect((host, port))
sock.send(b'00010sinitelcar')
data = sock.recv(4096)
print(data.decode())
try:
    while True:
        
        data = sock.recv(4096)
        data = data.decode()[10:]

        data = data.split(',')
        service = 'elcar'
        aux = ''

        if data[0] == '2':
            aux = Cartas(data[1]) #IDs de los Mazos del Usuario
            print(aux)
        elif data[0] == '1':
            aux = agregar(data[1], data[2], data[3])
            print(aux)

        if aux == '':
            sock.send(b'00014elcarOKnofound')
            
        else:
            size = len(aux) + len(service)
            msg = getSize(size) + 'elcarOK' + aux
            sock.send(msg.encode("utf-8")) 
            
finally:
    print("cerrando socket")
    sock.close()