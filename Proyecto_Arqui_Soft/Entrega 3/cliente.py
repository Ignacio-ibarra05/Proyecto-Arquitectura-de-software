import socket
import getpass
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
    print("Ingrese la Opción que quiere realizar: ")
    print("(1) Ver Colección")
    print("(2) Ver Mazos")
    print("(9) Salir")

def inicio_Admin():
    print("Ingresar la Opción que quiere realizar: ")
    print("(1) Eliminar Usuario (PRÓXIMAMENTE)")
    print("(2) Eliminar carta (PRÓXIMAMENTE)")
    print("(3) Listar Cartas")
    print("(9) Salir")

def edicion_mazos():
    print("Ingrese la Opción que quiere realizar:")
    print("(1) Crear Mazo")
    print("(2) Ver Mazo")
    print("(3) Eliminar Mazo (PRÓXIMAMENTE)")
    print("(9) Salir")

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
            print("Servicio 'Eliminar Carta' no conectado")
    elif op == '2':
        service='eluse'
        print("\n----Eliminar Usuario----")
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
    elif op == '3':
        service = 'lista'
        print("\n----Ver Cartas-----")
        size = len(service)
        msg = getSize(size) + service 
        msg1 = msg.encode('utf-8')
        sock.send(msg1)

        resp = sock.recv(4096)
        data = resp.decode()
        #print(data)
        if data[10:12]=="OK":
            if data[12:]=="nofound":
                print("Sin Cartas en el sistema")
            else:
                #print("\n ---Colección----")
                collection = data[12:]
                collection = collection.split(',')
                for _ in collection:
                    print(_)
        else:
            print("Servicio 'Listar Cartas' no conectado")
    elif op == '9':
        print("saliendo")

def acciones_mazos(op, rol, cod):
    if op == '1':
        service = 'crema'
        print("\n---Crear Mazo---")
        nombre = input("Ingresar nombre para el mazo: ")
        size = len(service) + len(nombre) + len(cod) + 1
        msg = getSize(size) + service + nombre +','+cod

        sock.send(msg.encode('utf-8'))
        resp = sock.recv(4096)
        data = resp.decode()
        if data[10:12]=="OK":
            if data[12:]=="nofound":
                print("Algo salió mal")
            else:
                print(f"Mazo {nombre} a sido creado con exito.")

    elif op == '2':
        service = 'vemaz'
        print("\n----Ver Mazo----")
        ID_mazo = input("Ingresar el ID del Mazo que quiere ver: ")
        size = len(service) + len(ID_mazo)
        msg = getSize(size) + service + ID_mazo
        msg1 = msg.encode('utf-8')

        sock.send(msg1)
        resp = sock.recv(4096)
        data = resp.decode()
        if data[10:12]=="OK":
            if data[12:]=="nofound":
                print("Mazo no encontrado")
            else:
                print(f"\n ---Mazo {ID_mazo}---")
                Mazo = data[12:]
                Mazo = Mazo.split(',')
                for _ in Mazo:
                    print(_)
    elif op == '3':
        service = 'elmaz'
        print("\n----Eliminar Mazo----")
        ID_mazo = input("Ingresar el ID del mazo que quiere eliminar: ")
        size = len(service) + len(cod) + len(ID_mazo) + 1
        msg = getSize(size) + service + cod + ID_mazo
        msg1 = msg.encode('utf-8')

        sock.send(msg1)
        resp = sock.recv(4096)
        data = resp.decode()
        if data[10:12]=="OK":
            if data[12:]=="nofound":
                print("Mazo no encontrado")
            else:
                print(f"Mazo {data[12:]} eliminado")

def acciones_U(op, rol, cod):
    if op == '1':
        service = 'vecol'
        print("\n----Ver Colección-----")
        size = len(service) + len(cod)
        msg = getSize(size) + service + cod 
        msg1 = msg.encode('utf-8')
        sock.send(msg1)

        resp = sock.recv(4096)
        data = resp.decode()
        #print(data)
        if data[10:12]=="OK":
            if data[12:]=="nofound":
                print("Sin Colección")
            else:
                #print("\n ---Colección----")
                collection = data[12:]
                collection = collection.split(',')
                for _ in collection:
                    print(_)
        else:
            print("Servicio 'Ver Colección' no conectado")
    elif op == '2':
        service='mazos'
        print("\n----Ver Mazos-----")
        size = len(service)
        msg = getSize(size) + service + cod
        msg1 = msg.encode('utf-8')

        sock.send(msg1)
        resp = sock.recv(4096)
        data = resp.decode()

        if data[10:12]=="OK":
            if data[12:]=="nofound":
                print("Sin Mazos")
            else:
                print("\n ---Mazos----")
                Mazos = data[12:]
                Mazos = Mazos.split(',')
                for _ in Mazos:
                    print(_)
                op1 = 0
                while op1 != '9':
                    edicion_mazos()
                    op1 = input("Ingrese Opcion: ")
                    acciones_mazos(op1, rol, cod)
                
        else:
            print("Servicio 'Ver Mazos' no conectado")
    elif op == '9':
        print("saliendo")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 5002
sock.connect((host, port))
print('Conectando...')
sock.send(b'hola')

try: 
    while True:
        inicio = input("Bienvenido, seleccione si es que tiene un usuario creado (s/n): ")
        inicio = str(inicio).lower()
        if inicio == 's': 
            usuario = input("Ingrese su usuario: ")
            passw = getpass.getpass("Ingrese su contraseña: ")
            service = 'login'
            size = len(usuario) + len(passw) + len(service) + 1
            msg = getSize(size) + 'login' + usuario + ' ' + passw

            sock.send(msg.encode('utf-8'))
            resp = sock.recv(4096)
            data = resp.decode()

            #print(data[12:])
            if data[10:12] == 'OK':
                if data[12:] == 'nofound':
                    print("Usuario Invalido")
                elif data[12:15] == 'usu':
                    op = 0
                    rol = 'usuario'
                    while op != '9':
                        inicio_Usuario()
                        op = input("Ingrese Opcion: ")
                        acciones_U(op, rol, data[15:])
                elif data[12:16] == 'admi':
                    op = 0
                    rol = 'administrador'
                    while op != '9':
                        inicio_Admin()
                        op = input("Ingrese Opcion: ")
                        acciones_A(op, rol)
            else:
                print("Servicio de login no conectado")
        elif inicio == 'n': 
            print("---Crear Usuario---")
            usuario = input("Ingresar un nombre de usuario: ")
            passw = input("Ingresar una contraseña: ")
            service = 'creus'
            size = len(service) + len(usuario) + len(passw) + 1
            msg = getSize(size) + service + usuario + ' ' + passw

            sock.send(msg.encode('utf-8'))
            resp = sock.recv(4096)
            data = resp.decode()
            if data[10:12] == 'OK':
                if data[12:] == 'nofound':
                    print("Usuario Invalido")
                else:
                    print("Usuario creado con exito")
            else:
                print("Servicio de Crear Usuario no conectado")
        else:
            print("Opción invalida")

finally:
    print("Cerrando sesion")
    sock.close()