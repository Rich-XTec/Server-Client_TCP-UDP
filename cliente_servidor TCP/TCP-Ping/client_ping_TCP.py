import socket
import time

# Configurações do servidor
IP_SERVIDOR = "192.168.3.39"
PORTA_SERVIDOR = 8080

# Criação do socket TCP
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente_socket.connect((IP_SERVIDOR, PORTA_SERVIDOR))
cliente_socket.settimeout(1)  # 1 segundo de timeout

for i in range(1, 11):
    mensagem = f"ping {i}"
    start_time = time.time()  # Marca o tempo de envio

    try:
        # Envia a mensagem
        cliente_socket.sendall(mensagem.encode())

        # Recebe a resposta
        resposta = cliente_socket.recv(1024)
        print("Resposta do servidor:", resposta.decode())

        end_time = time.time()  # Marca o tempo de recebimento
        rtt = (end_time - start_time) * 1000  # RTT em milissegundos
        rtt_rounded = round(rtt,2)

        print("RTT: ", rtt_rounded, "ms\n")

    except socket.timeout:
        print(f"Ping {i}: tempo esgotado (timeout)")

cliente_socket.close()
