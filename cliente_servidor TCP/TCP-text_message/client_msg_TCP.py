import socket

# Configurações do servidor
IP_SERVIDOR = "192.168.3.39"
PORTA_SERVIDOR = 8080

# Criação do socket TCP
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente_socket.connect((IP_SERVIDOR, PORTA_SERVIDOR))

mensagem = input("Digite a mensagem para o servidor: ")

# Envia a mensagem
cliente_socket.sendall(mensagem.encode())

# Recebe a resposta
resposta = cliente_socket.recv(1024)
print("Resposta do servidor:", resposta.decode())

cliente_socket.close()
