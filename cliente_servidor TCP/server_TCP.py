import socket

# Configurações do servidor
IP = "192.168.3.39"
PORTA = 8080
BUFFER_SIZE = 1024

# Criação do socket TCP
servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor_socket.bind((IP, PORTA))
servidor_socket.listen(1)  # Aceita 1 conexão por vez

print(f"Servidor TCP ouvindo em {IP}:{PORTA}...")

conn, addr = servidor_socket.accept()
print(f"Conexão estabelecida com {addr}")

while True:
    dados = conn.recv(BUFFER_SIZE)
    if not dados:
        break  # Cliente fechou a conexão
    mensagem = dados.decode()
    print(f"Recebido: {mensagem}")

    resposta = f"Servidor recebeu: {mensagem}"
    conn.sendall(resposta.encode())

conn.close()
servidor_socket.close()
