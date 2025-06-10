import socket

# Configurações do servidor
IP_SERVIDOR = "192.168.3.39"
PORTA_SERVIDOR = 8080

# Criação do socket UDP
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

mensagem = input("Digite a mensagem para o servidor: ")

# Envia a mensagem
cliente_socket.sendto(mensagem.encode(), (IP_SERVIDOR, PORTA_SERVIDOR))

# Recebe a resposta
resposta, _ = cliente_socket.recvfrom(1024)
print("Resposta do servidor:", resposta.decode())

cliente_socket.close()
