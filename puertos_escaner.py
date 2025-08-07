import socket

ip = input(f"Ingrese la IP a escanear:\n")
for puerto in range (1, 65535):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    resultado = sock.connect_ex((ip, puerto))

    if resultado == 0:
        print(f'Puerto {puerto}: Abierto  ')
        sock.close()    
    else:
        print(f'Puerto {puerto}: Cerrado')
       