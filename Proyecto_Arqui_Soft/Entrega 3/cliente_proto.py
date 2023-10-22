import socket
import sys

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

def inicio_Usuario():
    print("Ingrese la Opción que quiere realizar:")
    print("(1) Ver Colección")
    print("(2) Ver Mazos")
    print("(3) Salir")
    
def inicio_Admin():
    print("Ingrese la Opción que quiere realizar:")
    print("(1) Eliminar Carta")
    print("(2) Eliminar Usuario")
    print("(3) Algo mas...")
    print("(4) Salir")

def acciones_A(op, rol):
    if op == '1':
        service='elcar'
        print("\n----Eliminar Carta-----")
        car = input("ID Carta")
        size = len(car)+len(service)
        msg = getSize(size) + service + car

        sock.send(msg.encode('uft-8'))
        resp = sock.recv(4096)
        data = resp.decode()

        if data[10:11]=="OK":
            if data[12:]=="nofound":
                print("Carta no encontrada")
            else:
                print("Carta Eliminada")
        else:
            print("Servicio 'Elimiinar Carta' no conectado")
    elif op == '2':
        service='eluse'
        print("\n----Eliminar Usuario-----")
        car = input("ID Usuario")
        size = len(car)+len(service)
        msg = getSize(size) + service + car

        sock.send(msg.encode('uft-8'))
        resp = sock.recv(4096)
        data = resp.decode()

        if data[10:11]=="OK":
            if data[12:]=="nofound":
                print("Usuario no encontrado")
            else:
                print("Usuario Eliminado")
        else:
            print("Servicio 'Eliminar Usuario' no conectado")
    elif op == '4' and rol =='admin':
        print("saliendo")

def acciones_U(op, rol):
    if op == '1':
        service='vecol'
        print("\n----Ver Colección-----")
        size = len(service)
        msg = getSize(size) + service

        sock.send(msg.encode('uft-8'))
        resp = sock.recv(4096)
        data = resp.decode()

        if data[10:11]=="OK":
            if data[12:]=="nofound":
                print("Sin Colección")
            else:
                print("\n ---Colección----")
                print(data[12:])
        else:
            print("Servicio 'Ver Colección' no conectado")
    elif op == '2':
        service='vemaz'
        print("\n----Ver Mazos-----")
        size = len(service)
        msg = getSize(size) + service

        sock.send(msg.encode('uft-8'))
        resp = sock.recv(4096)
        data = resp.decode()

        if data[10:11]=="OK":
            if data[12:]=="nofound":
                print("Sin Mazos")
            else:
                print("\n ---Mazos----")
                print(data[12:])
        else:
            print("Servicio 'Ver Mazos' no conectado")
    elif op == '3':
        print("saliendo")


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = "5000"
sock.connect((host, port))
print('Conectando...')
sock.send(b'hola')
try: 
    while True:
        usuario = input("Ingrese su usuario:")
        passw = input("Ingrese su contraseña:")
        service = 'login'
        size = len(usuario) + len(passw) + len(service) + 1
        msg = getSize(size) + 'login' + usuario + ' ' + passw

        sock.send(msg.encode('uft-8'))
        resp = sock.recv(4096)
        data = resp.decode()

        print(data[12:])
        if data[10:12] == 'OK':
            if data[12:] == 'nofound':
                print("Usuario Invalido")
            elif data[12:] == 'admin':
                op = 0
                rol = 'admin'
                while op != '4':
                    inicio_Admin()
                    op = input("Ingrese Opcion")
                    acciones_A(op, rol)
            elif data[12:] == 'jugador':
                op = 0
                rol = 'usuario'
                while op != '3':
                    inicio_Usuario()
                    op = input("Ingrese Opcion")
                    acciones_U(op, rol)
        else:
            print("Servicio de login no conectado")
finally:
    print("Cerrando sesion")
    sock.close()