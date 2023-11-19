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

def Usuarios(cod): #cod -> ID usuario
    # Cargar el JSON desde el archivo
    with open('BDD/BDD.json', 'r') as archivo:
        datos = json.load(archivo)

    # ID del usuario que quieres eliminar
    id_usuario_eliminar = cod  # Reemplaza con el ID del usuario que deseas eliminar

    # Encontrar y eliminar el usuario si está presente
    for usuario in datos['usuarios']:
        if usuario['ID_Usuario'] == id_usuario_eliminar:
            datos['usuarios'].remove(usuario)
            break  # Romper el bucle una vez que se elimine el usuario

    # Guardar los cambios en el archivo JSON
    with open('BDD/BDD.json', 'w') as archivo:
        json.dump(datos, archivo, indent=4)
    
    return "Usuario Eliminado"


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 5002

sock.connect((host, port))
sock.send(b'00010siniteluse')
data = sock.recv(4096)
print(data.decode())
try:
    while True:
        
        data = sock.recv(4096)
        data = data.decode()[10:]

        service = 'eluse'

        aux = Usuarios(data) #IDs de los Mazos del Usuario
        
        if aux == False:
            sock.send(b'00014eluseOKnofound')
            
        else:
            size = len(aux) + len(service)
            msg = getSize(size) + 'eluseOK' + aux
            sock.send(msg.encode("utf-8")) 
            
finally:
    print("cerrando socket")
    sock.close()