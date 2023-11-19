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
    id_carta_eliminar = ID
    id_mazo = ID_mazo
    # Encontrar el usuario en la lista de usuarios
    for usuario in datos['usuarios']:
        if usuario['ID_Usuario'] == id_usuario:
            # Encontrar el mazo al que quieres eliminar la carta
            for mazo in usuario['Mazos']:
                if mazo['ID_Mazo'] == id_mazo:
                    cartas_mazo = mazo['Cartas']
                    # Buscar y eliminar la carta del mazo si está presente
                    for carta in cartas_mazo:
                        if carta['ID_carta'] == id_carta_eliminar:
                            cartas_mazo.remove(carta)
                            break

    # Guardar los cambios en el archivo JSON
    with open('BDD/BDD.json', 'w') as archivo:
        json.dump(datos, archivo, indent=4)

    return "Carta Eliminada con Éxisto"

    
def cartas(ID): #ID -> Nombre Carta
    with open('BDD/BDD.json') as file:
        reader = json.load(file)
        cartas = reader['cartas']
        for row in cartas:
            if row["Nombre"] == ID:
                c = row["ID_carta"]
                print(c)
                return c 

def agregar(cod, ID_mazo, ID):
     # Cargar el JSON desde el archivo
    with open('BDD/BDD.json', 'r') as archivo:
        datos = json.load(archivo)

    # ID del usuario y ID de la carta que quieres eliminar
    id_usuario = cod
    id_carta_a_agregar = ID

    # Encontrar el usuario en la lista de usuarios
    for usuario in datos['usuarios']:
        if usuario['ID_Usuario'] == id_usuario:
            mazos_usuario = usuario['Mazos']
            # agregar id carta a la coleccion del usuario
            for row in mazos_usuario:
                if row["ID_Mazo"] == ID_mazo:
                    mazo_usuario = row["Cartas"]

                    data = {"ID_carta": id_carta_a_agregar}
                    mazo_usuario.append(data)
            
    # Guardar los cambios en el archivo JSON
    with open('BDD/BDD.json', 'w') as archivo:
        json.dump(datos, archivo, indent=4)

    return "Carta agregada con Éxisto"


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 5002

sock.connect((host, port))
sock.send(b'00010sinitedmaz')
data = sock.recv(4096)
print(data.decode())
try:
    while True:
        
        data = sock.recv(4096)
        #print(data.decode())
        data = data.decode()[10:]
        service = 'edmaz'
        nombre, cod, ID_mazo, op = data.split(',')
        nombre = nombre.lower()
        nombre = nombre.capitalize()
        
        car = ''

        if op == '1': #Agregar Carta
            ID_carta = cartas(nombre)
            car = agregar(cod,ID_mazo, ID_carta)

        else: #Eliminar Carta
            ID_carta = cartas(nombre)
            car = Colec(cod, ID_carta)

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