import socket
import csv
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


def authenticate(username, password):
    with open('BDD/usuarios.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == username and row[2] == password:
                return row
    return False


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 5002

sock.connect((host, port))
sock.send(b'00010sinitlogin')
data = sock.recv(4096)
print(data.decode())
try:
    while True:
        
        data = sock.recv(4096)
        #print(data.decode())
        data = data.decode()[10:]
        data = data.split(' ')
        #print(data)
        usuario = data[0]
        passw = data[1]
        service = 'login'
        #print(usuario + " " + passw)
        aux = authenticate(usuario,passw)
        #print(aux)
        if aux == False:
            sock.send(b'00017loginOKnofound')
            
        else:
            size = len(aux[3]) + len(service) + len(aux[0]) + 2

            msg = getSize(size) + 'loginOK' + aux[3] + aux[0]
            sock.send(msg.encode("utf-8"))
finally:
    print("cerrando socket")
    sock.close()