import socket

# Configurações do servidor
IP = "192.168.3.39"
PORTA = 8080
BUFFER_SIZE = 1024

# Criação do socket UDP
servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor_socket.bind((IP, PORTA))

print(f"Servidor UDP ouvindo em {IP}:{PORTA}...")

while True:
    # Espera por dados do cliente
    dados, endereco = servidor_socket.recvfrom(BUFFER_SIZE)
    mensagem = dados.decode()
    print(f"Recebido de {endereco}: {mensagem}")

    # Resposta ao cliente
    resposta = f"Servidor recebeu: {mensagem}"
    servidor_socket.sendto(resposta.encode(), endereco)
