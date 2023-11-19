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
    id_carta_eliminar = cod  # Reemplaza con el ID de la carta que deseas eliminar

    # Encontrar y eliminar la carta si está presente
    for i, carta in enumerate(datos['cartas']):
        if carta['ID_carta'] == id_carta_eliminar:
            del datos['cartas'][i]
            break  # Romper el bucle una vez que se elimine la carta

    # Guardar los cambios en el archivo JSON
    with open('BDD/BDD.json', 'w') as archivo:
        json.dump(datos, archivo, indent=4)
    
    return "Carta Eliminada"


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

        service = 'elcar'

        aux = Cartas(data) #IDs de los Mazos del Usuario
        
        if aux == False:
            sock.send(b'00014elcarOKnofound')
            
        else:
            size = len(aux) + len(service)
            msg = getSize(size) + 'elcarOK' + aux
            sock.send(msg.encode("utf-8")) 
            
finally:
    print("cerrando socket")
    sock.close()