import socket

# Crear un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlazar el socket al puerto donde el servidor escuchará
server_address = ('localhost', 5001)
sock.connect(server_address)

try:
    mensaje = b'00010sinitservi'
    sock.sendall(mensaje)

    data = int(sock.recv(5))
    print('', data)

finally:
    # Cerrar la conexión
    sock.close()
