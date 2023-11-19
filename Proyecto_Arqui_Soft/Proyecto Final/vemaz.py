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


def Mazo(cod, cod_m): #cod -> ID usuario
    col = []
    with open('BDD/BDD.json') as file:
        reader = json.load(file)
        usuarios = reader['usuarios']
        for row in usuarios:
            if row["ID_Usuario"] == cod:
                mazos = row["Mazos"]
                for row1 in mazos:
                    if row1["ID_Mazo"] == cod_m:
                        col = row1["Cartas"]
    return col

def cartas(cod):
    with open('BDD/BDD.json') as file:
        reader = json.load(file)
        cartas = reader['cartas']
        for row in cartas:
            if row["ID_carta"] == cod:
                c = row["Nombre"] + ', ' + row["Tipo"] + ', ' + row["Raresa"]
                return c
    return False


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 5002

sock.connect((host, port))
sock.send(b'00010sinitvemaz')
data = sock.recv(4096)
print(data.decode())

try:
    while True:
        
        data = sock.recv(4096)
        data = data.decode()[10:]
        data, cod = data.split(',')
        service = 'vemaz'
        carta = Mazo(cod, data)
        aux = ''

        if len(carta) == 0:
            aux = "Mazo sin cartas"
        else:

            for i in carta:
                a = cartas(i["ID_carta"])
                aux = aux + a + ';'
        
        if aux == '':
            sock.send(b'00014vemazOKnofound')
            
        else:
            size = len(aux) + len(service)
            msg = getSize(size) + 'vemazOK' + aux
            #print(msg)
            
            sock.send(msg.encode("utf-8")) 
        
finally:
    print("cerrando socket")
    sock.close()