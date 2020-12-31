import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(), 9999))

server_socket.listen(5)
while True:
    client_sock, addr = server_socket.accept()
    print("client addr:{}".format(str(addr)))
    client_sock.send("hello client, 你好".encode('utf-8'))
    client_sock.close()




