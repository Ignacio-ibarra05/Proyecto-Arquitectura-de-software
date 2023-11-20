import socket
import getpass
import sys

def getSize(size): #Listo
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

def inicio_Usuario(): #Listo
    print("Ingrese la Opción que quiere realizar: ")
    print("(1) Ver Colección")
    print("(2) Ver Mazos")
    print("(9) Salir")

def inicio_Admin():
    print("Ingresar la Opción que quiere realizar: ")
    print("(1) Eliminar Usuario")
    print("(2) Eliminar carta")
    print("(3) Listar Cartas")
    print("(9) Salir")

def edicion_coleccion(): #Listo
    print("Ingrese la Opción que quiere realizar:")
    print("(1) Agregar carta")
    print("(2) Eliminar carta")
    print("(9) Salir")

def edicion_mazos(): #Listo
    print("Ingrese la Opción que quiere realizar:")
    print("(1) Crear Mazo") #Listo
    print("(2) Ver Mazo") #Listo
    print("(3) Eliminar Mazo") #Listo
    print("(9) Salir")

def edicion_mazo(): #listo
    print("Ingrese la Opción que quiere realizar:")
    print("(1) Agregar carta")
    print("(2) Eliminar carta")
    print("(9) Salir")

def acciones_A(op):
    if op == '2': 
        service='elcar'
        print("\n----Eliminar Carta----")

        service2 = 'lista'
        size2 = len(service2) + 2
        msg = getSize(size2) + service2 + ',2'
        sock.send(msg.encode('utf-8'))
        resp = sock.recv(4096)
        data1 = resp.decode()
        print(data1[10:12])
        if data1[10:12] == "OK":
            if data1[12:] == "nofound":
                print("No hay cartas registradas")
            else:
                data1 = data1.split(';')
                for i in data1:
                    print(i)
                
                car = input("ingresar ID carta a eliminar: ")
                size = len(car)+len(service)
                msg = getSize(size) + service + car

                sock.send(msg.encode('utf-8'))
                resp = sock.recv(4096)
                data = resp.decode()

                if data[10:11]=="OK":
                    if data[12:]=="nofound":
                        print("Usuario no encontrado")
                    else:
                        print("Usuario Eliminado")
        else:
            print("Servicio 'Eliminar Carta' no conectado")
    elif op == '9':
        print("saliendo")
    elif op == '1':
        service='eluse'
        print("\n----Eliminar Usuario----")

        service2 = 'lista'
        size2 = len(service2) + 2
        msg = getSize(size2) + service2 + ',1'
        sock.send(msg.encode('utf-8'))
        resp = sock.recv(4096)
        data1 = resp.decode()
        print(data1[10:12])
        if data1[10:12] == "OK":
            if data1[12:] == "nofound":
                print("No hay usuarios creados")
            else:
                data1 = data1.split(';')
                for i in data1:
                    print(i)
                
                car = input("ingresar ID Usuario a eliminar: ")
                size = len(car)+len(service)
                msg = getSize(size) + service + car

                sock.send(msg.encode('utf-8'))
                resp = sock.recv(4096)
                data = resp.decode()

                if data[10:11]=="OK":
                    if data[12:]=="nofound":
                        print("Usuario no encontrado")
                    else:
                        print("Usuario Eliminado")
        else:
            print("Servicio 'Eliminar Usuario' no conectado")
    elif op == '9':
        print("saliendo")

def acciones_coleccion(op, cod): #Listo
    if op == '1':
        service = 'edcol'
        print("\n---Agregar Carta---")
        q = 0
        while q == 0:
            codc = input("Ingresar nombre de la carta: ")
            size = len(service) + len(codc) + len(cod) + len(op) + 2
            msg = getSize(size) + service + codc + ',' + cod + ',' + op

            sock.send(msg.encode('utf-8'))
            resp = sock.recv(4096)
            data = resp.decode()
            if data[10:12] == "OK":
                if data[12:] == "nofound":
                    print("Carta ingresada no existe")
                else:
                    print(f"Se agregó {codc} a la colección")
            aq = input("quiere continuar? (S/N)")
            aq.lower()
            if aq == 'n':
                q = 1
    elif op == '2':
        service = 'edcol'
        print("\n---Eliminar Carta---")
        q = 0
        while q == 0:
            codc = input("Ingresar nombre de la carta: ")
            size = len(service) + len(codc) + len(cod) +len(op) + 2
            msg = getSize(size) + service + codc + ',' + cod + ',' + op

            sock.send(msg.encode('utf-8'))
            resp = sock.recv(4096)
            data = resp.decode()
            if data[10:12] == "OK":
                if data[12:] == "nofound":
                    print("Carta ingresada no existe")
                else:
                    print(f"Se eliminó {codc} de la colección")
            aq = input("quiere continuar? (S/N)")
            aq.lower()
            if aq == 'n':
                q = 1
            
def acciones_mazos(op, cod, can): #Listo
    if op == '1': #Listo
        service = 'crema'
        print("\n---Crear Mazo---")
        nombre = input("Ingresar nombre para el mazo: ")
        size = len(service) + len(nombre) + len(cod) + len(can) + 2
        msg = getSize(size) + service + nombre +','+cod + ',' + can

        sock.send(msg.encode('utf-8'))
        resp = sock.recv(4096)
        data = resp.decode()
        if data[10:12]=="OK":
            if data[12:]=="nofound":
                print("Algo salió mal")
            else:
                print(f"Mazo {nombre} a sido creado con exito.")
    elif op == '2': #Listo
        service = 'vemaz'
        print("\n----Ver Mazo----")
        ID_mazo = input("Ingresar el ID del Mazo que quiere ver: ")
        size = len(service) + len(ID_mazo) + len(cod) + 1
        msg = getSize(size) + service + ID_mazo + ',' + cod
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
                Mazo = Mazo.split(';')

                for _ in Mazo:
                    print(_)
                
                s = input("\nDesea Editar el mazo? (S/N): ")
                s = s.lower()

                if s == 's':
                    print("\n---Editar Mazo---")
                    op2 = 0
                    edicion_mazo()
                    op2 = input("Ingrese opción: ")
                    acciones_mazo(op2, cod, ID_mazo)             
    elif op == '3': #Listo
        service = 'elmaz'
        print("\n----Eliminar Mazo----")
        ID_mazo = input("Ingresar el ID del mazo que quiere eliminar: ")
        size = len(service) + len(cod) + len(ID_mazo) + 1
        msg = getSize(size) + service + cod + ',' + ID_mazo
        msg1 = msg.encode('utf-8')

        sock.send(msg1)
        resp = sock.recv(4096)
        data = resp.decode()
        if data[10:12]=="OK":
            if data[12:]=="nofound":
                print("Mazo no encontrado")
            else:
                print(f"Mazo {ID_mazo} eliminado")

def acciones_U(op, cod): #Listo
    if op == '1': #Listo
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
                collection = collection.split(';')
                for _ in collection:
                    print(_)
                
                op1 = 0
                while op1 != '9':
                    edicion_coleccion()
                    op1 = input("Ingrese Opcion: ")
                    #can = str(can)
                    acciones_coleccion(op1, cod)

        else:
            print("Servicio 'Ver Colección' no conectado")
    elif op == '2': #Listo
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
                s = input("\nDesea crear un mazo? (S/N)")
                s = s.lower()
                if s == 's':
                    acciones_mazos('1', cod, '1')

            else:
                print("\n ---Mazos----")
                Mazos = data[12:]
                Mazos = Mazos.split(';')
                can = 0
                for _ in Mazos:
                    print(_)
                    can = can + 1
                op1 = 0
                while op1 != '9':
                    edicion_mazos()
                    op1 = input("Ingrese Opcion: ")
                    can = str(can)
                    acciones_mazos(op1, cod, can)
                
        else:
            print("Servicio 'Ver Mazos' no conectado")
    elif op == '9':
        print("saliendo")

def acciones_mazo(op, cod, ID_mazo): #Listo
    if op == '1':
        service = 'edmaz'
        print("\n---Agregar Carta---")
        q = 0
        while q == 0:
            service1 = 'vecol'
            
            size = len(service1) + len(cod)
            msg = getSize(size) + service1 + cod 
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
                    collection = collection.split(';')
                    for _ in collection:
                        print(_)
            print("\n")

            codc = input("Ingresar nombre de la carta: ")
            size = len(service) + len(codc) + len(cod) + len(op) + len(ID_mazo) + 3
            msg = getSize(size) + service + codc + ',' + cod + ','+ ID_mazo +','+ op

            sock.send(msg.encode('utf-8'))
            resp = sock.recv(4096)
            data = resp.decode()
            if data[10:12] == "OK":
                if data[12:] == "nofound":
                    print("Carta ingresada no existe")
                else:
                    print(f"Se agregó {codc} al mazo {ID_mazo}")
            aq = input("quiere continuar? (S/N): ")
            aq.lower()
            if aq == 'n':
                q = 1
    elif op == '2':
        service = 'edmaz'
        print("\n---Eliminar Carta---")
        q = 0
        while q == 0:
            codc = input("Ingresar nombre de la carta: ")
            size = len(service) + len(codc) + len(cod) +len(op) + len(ID_mazo) + 3
            msg = getSize(size) + service + codc + ',' + cod + ',' + ID_mazo +','+ op

            sock.send(msg.encode('utf-8'))
            resp = sock.recv(4096)
            data = resp.decode()
            if data[10:12] == "OK":
                if data[12:] == "nofound":
                    print("Carta ingresada no existe")
                else:
                    print(f"Se eliminó {codc} del mazo {ID_mazo}")
            aq = input("quiere continuar? (S/N): ")
            aq.lower()
            if aq == 'n':
                q = 1
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
                        acciones_U(op, data[15:])
                elif data[12:16] == 'admi':
                    op = 0
                    rol = 'administrador'
                    while op != '9':
                        inicio_Admin()
                        op = input("Ingrese Opcion: ")
                        acciones_A(op)
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
