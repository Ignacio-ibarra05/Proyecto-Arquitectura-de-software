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
    
def eliminar(cod, ID):
    with open('BDD/BDD.json', 'r') as archivo:
        datos = json.load(archivo)

    # ID del usuario y del mazo que quieres eliminar
    id_usuario = cod
    id_mazo_eliminar = ID  # ID del mazo que quieres eliminar

    # Encontrar el usuario en la lista de usuarios
    for usuario in datos['usuarios']:
        if usuario['ID_Usuario'] == id_usuario:
            mazos_usuario = usuario['Mazos']
            # Buscar y eliminar el mazo del usuario si está presente
            for mazo in mazos_usuario:
                if mazo['ID_Mazo'] == id_mazo_eliminar:
                    mazos_usuario.remove(mazo)
                    break  # Romper el bucle una vez que se elimine el mazo

    # Guardar los cambios en el archivo JSON
    with open('BDD/BDD.json', 'w') as archivo:
        json.dump(datos, archivo, indent=4)
    
    return "Mazo eliminado"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 5002

sock.connect((host, port))
sock.send(b'00010sinitelmaz')
data = sock.recv(4096)
print(data.decode())
try:
    while True:
        
        data = sock.recv(4096)
        #print(data.decode())
        data = data.decode()[10:]
        service = 'elmaz'
        cod, ID_mazo = data.split(',')

        car = eliminar(cod, ID_mazo)

        if car == '':
            sock.send(b'00017reticOKnofound')
            
        else:
            size = len(car) + len(service)
            msg = getSize(size) + 'edmazOK' + car 
            #print(msg)
            sock.send(msg.encode("utf-8")) 
        
finally:
    print("cerrando socket")
    sock.close()