import socket
import threading

service = [None] * 12
service_auth = [None] * 12


def main():
    host = 'localhost'
    port = 5002

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((host, port))

    server_socket.listen()

    print(f"Servidor escuchando en {host}:{port}")

    while True:
        # Esperar una conexión entrante
        connect, address = server_socket.accept()

        msg = connect.recv(4096)
        data = msg.decode()

        if data[5:10] == 'sinit':
            service_code = data[10:]
            index = None

            if service_code == 'login':
                index = 0
            elif service_code == 'vecol':
                index = 1
            elif service_code == 'mazos':
                index = 2
            
            if index is not None and service_auth[index] is None:
                service[index] = connect
                service_auth[index] = True
                connect.send(f"00012sinitOK{service_code}".encode())
                print(service[index])

            else:
                connect.send(f"00012sinitNK{service_code}".encode())

        else:
            # Manejar la conexión con el cliente en un hilo separado
            client_thread = threading.Thread(target=handle_connection, args=(connect, data, address))
            client_thread.start()


            

def handle_connection(client_socket,data,address):
    
    print(f"Cliente conectado desde {address[0]}:{address[1]}")

    while True:
        # Recibir datos del cliente
        msg = client_socket.recv(4096)
        data = msg.decode()
        #print("estoy en recibir datos del cliente: ",data)

        
        
        service_code = data[5:10]
        index = None
        print(service_code, index)
        if service_code == 'login':
            index = 0
        elif service_code == 'vecol':
            index = 1
        elif service_code == 'mazos':
                index = 2
                
        print("service_auth: ", service_auth[index])

        if index is not None and service_auth[index] is not None:
            service[index].send(msg)
            aux = service[index].recv(4096)
            client_socket.send(aux)

        else:
            client_socket.send(f"00012{service_code}NK".encode())

        
        
        # Enviar datos al servicio

        
    


if __name__ == '__main__':
    main()
