import socket


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((socket.gethostname(), 9999))

data = client_socket.recv(1024)
client_socket.close()
print(data.decode('utf-8'))

