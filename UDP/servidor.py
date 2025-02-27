import socket

# cria socket UDP
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# associa servidor à uma porta
server.bind(('0.0.0.0', 5000)) #permite conexões de qualquer IP
print("Servidor aguardando mensagens...")

while 1:
    mensagem, endereco = server.recvfrom(1024) #recebe até 1024 bytes
    print(f"Mensagem recebida de {endereco}: {mensagem.decode()}")

    #confirmação
    resposta = "Mensagem recebida"
    server.sendto(resposta.encode(), endereco)