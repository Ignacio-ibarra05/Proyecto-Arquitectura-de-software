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


def Colec(cod, ID): #cod -> ID usuario, ID -> ID carta   
    # Cargar el JSON desde el archivo
    with open('BDD/BDD.json', 'r') as archivo:
        datos = json.load(archivo)

    # ID del usuario y ID de la carta que quieres eliminar
    id_usuario = cod
    id_carta_a_eliminar = ID
    a = 0

    # Encontrar el usuario en la lista de usuarios
    for usuario in datos['usuarios']:
        if usuario['ID_Usuario'] == id_usuario:
            coleccion_usuario = usuario['Coleccion']
            # Buscar la carta por su ID y eliminarla si se encuentra
            nueva_coleccion = [carta for carta in coleccion_usuario if carta['ID_carta'] != id_carta_a_eliminar]
            usuario['Coleccion'] = nueva_coleccion

            for mazo in usuario['Mazos']:
                cartas_mazo = mazo['Cartas']
                nuevas_cartas_mazo = [carta for carta in cartas_mazo if carta['ID_carta'] != id_carta_a_eliminar]
                mazo['Cartas'] = nuevas_cartas_mazo
                a = 1

    # Guardar los cambios en el archivo JSON
    with open('BDD/BDD.json', 'w') as archivo:
        json.dump(datos, archivo, indent=4)

    return a

    
def cartas(ID): #ID -> Nombre Carta
    with open('BDD/BDD.json') as file:
        reader = json.load(file)
        cartas = reader['cartas']
        for row in cartas:
            if row["Nombre"] == ID:
                c = row["ID_carta"]
                print(c)
                return c 

def agregar(cod, ID):
     # Cargar el JSON desde el archivo
    with open('BDD/BDD.json', 'r') as archivo:
        datos = json.load(archivo)
    
    # ID del usuario y ID de la carta que quieres eliminar
    id_usuario = cod
    id_carta_a_agregar = ID
    a = 0
    # Encontrar el usuario en la lista de usuarios
    for usuario in datos['usuarios']:
        if usuario['ID_Usuario'] == id_usuario:
            coleccion_usuario = usuario['Coleccion']
            # agregar id carta a la coleccion del usuario
            data = {"ID_carta": id_carta_a_agregar}
            coleccion_usuario.append(data)
            a = 1
            

    # Guardar los cambios en el archivo JSON
    with open('BDD/BDD.json', 'w') as archivo:
        json.dump(datos, archivo, indent=4)

    return a


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 5002

sock.connect((host, port))
sock.send(b'00010sinitedcol')
data = sock.recv(4096)
print(data.decode())
try:
    while True:
        
        data = sock.recv(4096)
        #print(data.decode())
        data = data.decode()[10:]
        service = 'edcol'
        nombre, cod, op = data.split(',')
        nombre = nombre.lower()
        nombre = nombre.capitalize()
        
        car = 0

        if op == '1': #Agregar Carta
            ID_carta = cartas(nombre)
            if ID_carta != False:
                car = agregar(cod, ID_carta)

        else: #Eliminar Carta
            ID_carta = cartas(nombre)
            if ID_carta != False:
                car = Colec(cod, ID_carta)

        if car == 0:
            sock.send(b'00017reticOKnofound')
            
        else:
            size = len("Carta agregada Exitosamente") + len(service)
            msg = getSize(size) + 'edcolOK' + car 
            #print(msg)
            sock.send(msg.encode("utf-8")) 
        
finally:
    print("cerrando socket")
    sock.close()