import socket

#cria socket UDP
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#IP e porta do servidor
server_address = ('192.168.0.4', 5000)

mensagem = "Ativar Lora"
#envia mensagem p o endereço destino
client.sendto(mensagem.encode(), server_address)

#recebe resposta
resposta, servidor = client.recvfrom(1024)
print(f"Resposta do servidor: {resposta.decode()}")
