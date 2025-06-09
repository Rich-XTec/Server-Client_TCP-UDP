import socket

# Configurações do servidor
IP_SERVIDOR = "192.168.3.39"
PORTA_SERVIDOR = 8080

# Criação do socket UDP
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(1)  # 1 segundo de timeout

for i in range(1, 11):
    mensagem = f"ping {i}"
    start_time = time.time()  # Marca o tempo de envio
    
    try:
        # Envia a mensagem
        cliente_socket.sendto(mensagem.encode(), (IP_SERVIDOR, PORTA_SERVIDOR))

        # Recebe a resposta
        resposta, _ = cliente_socket.recvfrom(1024)
        
        end_time = time.time()  # Marca o tempo de recebimento
        rtt = (end_time - start_time) * 1000  # RTT em milissegundos
        
        print("Resposta do servidor:", resposta.decode(), "RTT: ", rtt)

    except socket.timeout:
        print(f"Ping {i}: tempo esgotado (timeout)")    

cliente_socket.close()
