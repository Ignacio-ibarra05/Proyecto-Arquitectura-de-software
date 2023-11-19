import socket
import json
#Listo

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

def authenticate(username, password):
    with open('BDD/BDD.json') as file:
        data = json.load(file)
        usuarios = data['usuarios']
        for user in usuarios:
            if user["Nombre"] == username and user["Contra"] == password:
                return user["ID_Usuario"], user["Rol"]
    return False


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 5002

sock.connect((host, port))
sock.send(b'00010sinitlogin')
data = sock.recv(4096)
#print(data.decode())
try:
    while True:
        
        data = sock.recv(4096)
        print(data.decode())
        data = data.decode()[10:]
        data = data.split(' ')
        print(data)
        usuario = data[0]
        passw = data[1]
        service = 'login'
        #print(usuario + " " + passw)
        aux1, aux2 = authenticate(usuario,passw)
        #print(aux1, aux2)
        if aux1 == False:
            sock.send(b'00017loginOKnofound')
            
        else:
            size = len(aux2) + len(service) + len(aux1) + 2

            msg = getSize(size) + 'loginOK' + aux2 + aux1
            sock.send(msg.encode("utf-8"))
finally:
    print("cerrando socket")
    sock.close()